import io
import requests
import sounddevice as sd
import soundfile as sf
from typing import Optional, Union


class PlaySound:
    def __init__(self, output_device_name="MacBook Airのスピーカー") -> None:
        output_device_id = self._search_output_device_id(output_device_name)
        input_device_id = 0
        sd.default.device = [input_device_id, output_device_id]

    def _search_output_device_id(self, output_device_name: str, output_device_host_api: int = 0) -> int:
        devices = sd.query_devices()
        for device in devices:
            if output_device_name in device["name"] and device["hostapi"] == output_device_host_api:
                return device["index"]
        raise RuntimeError(f"output_deviceが見つかりません: {output_device_name}")

    def _build_base_url(self, api_base: Union[str, int]) -> str:
        if isinstance(api_base, int):
            return f"http://127.0.0.1:{api_base}"
        elif isinstance(api_base, str):
            return api_base.rstrip("/")
        else:
            raise TypeError(f"api_base must be int(port) or str(url), got {type(api_base)}")

    def play_sound(
        self,
        text: str,
        api_base: Union[str, int] = 5050,
        *,
        model_id: int = 2,        # アミちゃん
        speaker_id: int = 0,
        language: str = "JP",
        speed: float = 1.0,
        noise: float = 0.0,
        noisew: float = 0.8,
        sdp_ratio: float = 0.2,
        style: Optional[str] = None,           # 例: "ノーマル"
        style_weight: Optional[float] = None,
        style_text: Optional[str] = None,
        style_text_weight: Optional[float] = None,
        timeout: int = 120,
    ) -> bool:

        base = self._build_base_url(api_base)
        length = 1.0 / max(0.25, min(4.0, float(speed)))

        params = {
            "text": text,
            "model_id": model_id,
            "speaker_id": speaker_id,
            "language": language,
            "sdp_ratio": sdp_ratio,
            "noise": noise,
            "noisew": noisew,
            "length": length,
        }
        if style is not None:
            params["style"] = style
        if style_weight is not None:
            params["style_weight"] = style_weight
        if style_text is not None:
            params["assist_text"] = style_text
        if style_text_weight is not None:
            params["assist_text_weight"] = style_text_weight

        try:
            r = requests.post(f"{base}/voice", params=params, timeout=timeout)
            r.raise_for_status()
        except requests.RequestException as e:
            print(f"音声生成リクエストでエラー: {e}")
            return False

        wav_bytes = r.content
        if not wav_bytes:
            print("音声データが空でした")
            return False

        with sf.SoundFile(io.BytesIO(wav_bytes)) as f:
            data = f.read(dtype="float32")
            rate = f.samplerate

        # 音量調整（0.0〜1.0）
        volume = 0.8  # 60%にする
        data = data * volume

        sd.play(data, rate)
        sd.wait()
        return True
