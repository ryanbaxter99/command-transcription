
import whisper

model = whisper.load_model('base.en')

result = model.transcribe('samples/test.wav')

# with open('result.txt', 'w') as f:
#     f.write(result["text"])

print(result["text"])
