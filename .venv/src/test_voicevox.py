from voicevox_adapter import VoicevoxAdapter
from play_sound import PlaySound

input_str = "いらっしゃいませ"
Voicevox_adapter = VoicevoxAdapter()
play_sound = PlaySound("MacBook Airのスピーカー")
data, rate = Voicevox_adapter.get_voice(input_str)
play_sound.play_sound(data, rate)
