import random
from obs_adapter import OBSAdapter
from style_bert_vits_adapter import StyleBertVitsAdapter
from openai_adapter import OpenAIAdapter
from youtube_comment_adapter import YoutubeCommentAdapter
from play_sound import PlaySound
from dotenv import load_dotenv

load_dotenv()
import os


class AITuberSystem:
    def __init__(self) -> None:
        video_id = os.getenv("YOUTUBE_VIDEO_ID")
        self.youtube_comment_adapter = YoutubeCommentAdapter(video_id)
        self.openai_adapter = OpenAIAdapter()
        self.obs_adapter = OBSAdapter()
        self.play_sound = PlaySound(output_device_name="VB-Cable")

    def talk_with_comment(self) -> bool:
        print("コメントを読み込みます...")
        comment = self.youtube_comment_adapter.get_comment()
        if comment is None:
            print("コメントがありませんでした")
            return False
        
        response_text = self.openai_adapter.create_chat(comment)

        # OBSに反映
        self.obs_adapter.set_question(comment)
        self.obs_adapter.set_answer(response_text)

        # 直接play_soundでTTS & 再生（アミちゃん / ノーマル）
        self.play_sound.play_sound(
            response_text,
            api_base=5050, 
            model_id=0, 
            speaker_id=0,
            style="Neutral",      # スタイル指定
            speed=0.8,
            noise=0.0,
            noisew=0.8,
            sdp_ratio=0.2
        )

        return True
