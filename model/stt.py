from transformers import pipeline

stt = pipeline(model="JRHuy/whisper-vietnamese-2", max_new_tokens=4000)