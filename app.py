import pydub
pydub.AudioSegment.converter = r"C:\FFmpeg"

src = "audio.mp3"
dst = "audio.wav"

sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")