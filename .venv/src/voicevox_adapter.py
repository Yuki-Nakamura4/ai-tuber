import json
import requests
import io
import soundfile


class VoiceVoxAdapter:
    url = "http://127.0.0.1:50021/"

    # 2回postする。一回目で変換、二回目で音声合成
    def __init__(self) -> None:
        pass

    def create_audio_query(self, text: str, speaker_id: int) -> json:
        item_data = {
            "text": text,
            "speaker": speaker_id,
        }
        response = requests.post(self.url + "audio_query", params=item_data)
        return response.json()

    def __create_request_audio(self, query_data, speaker_id: int) -> bytes:
        a_params = {
            "speaker": speaker_id,
        }
        headers = {"accept": "audio/wav", "Content-Type": "application/json"}
        res = requests.post(
            self.URL + "synthesis",
            params=a_params,
            data=json.dumps(query_data),
            headers=headers,
        )
        print(res.status_code)
        return res.content
