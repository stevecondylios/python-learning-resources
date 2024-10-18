

import whisper

model = whisper.load_model("base")

result = model.transcribe("/Users/st/Downloads/football.mp3")

print(result["text"])





