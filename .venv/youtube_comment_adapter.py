import pytchat
import json


class YoutubeCommentAdapter:
    def __init__(self, video_id) -> None:
        self.chat = pytchat.create(video_id=video_id, interruptable=False)

    def get_comment(self):
        # コメントを一括で取得
        comments = self.__get_comments()
        if comments == None:
            return None
        comment = comments[-1]  # 最新のコメント
        # コメントの情報の中からコメントのみを取得
        message = comment.get("message")
        return message

    def __get_comments(self):
        if self.chat.is_alive() == False:
            print("開始していません")
            return None
        comments = json.loads(self.chat.get().json())
        if comments == []:
            print("コメントが取得できませんでした")
            return None
        return comments


if __name__ == "__main__":
    import time

    video_id = "任意のvideo_id"
    chat = YoutubeCommentAdapter(video_id)
    time.sleep(1)  # コメント取得のために少し待つ
    print(chat.get_comment())
