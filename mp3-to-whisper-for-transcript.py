
# note: another way to do this is via the c++ approach which is documented in the
# quick start instructions in the github readme:
# https://github.com/ggerganov/whisper.cpp?tab=readme-ov-file#quick-start


import whisper

model = whisper.load_model("base")

result = model.transcribe("/Users/st/Downloads/football.mp3")

print(result["text"])





