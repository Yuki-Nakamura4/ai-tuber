import io
import requests
import soundfile as sf

class StyleBertVitsAdapter:
    def __init__(self, base_url="http://127.0.0.1:5050"):
        self.base_url = base_url

    def get_voice(self, text: str, model_id: int = 0, speaker_id: int = 0,
                  language: str = "JP", style: str | None = None):
        params = {
            "text": text,
            "model_id": model_id,
            "speaker_id": speaker_id,
            "language": language,
        }
        if style is not None:
            params["style"] = style

        # サーバはクエリで受ける設計なので params= を使う
        r = requests.post(f"{self.base_url}/voice", params=params, timeout=120)
        r.raise_for_status()

        # WAVバイナリをPCMへ
        data, sr = sf.read(io.BytesIO(r.content), dtype="float32")
        return data, sr
