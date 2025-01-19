import whisper
import torch
import gc

def convert_to_text(query):
        try:
            
            model = whisper.load_model("small.en")
            result = model.transcribe(query)
            print("Successfully used Whisper to transcribe audio. Deleting model.")
            del model
            gc.collect()
            torch.cuda.empty_cache()
            return result['text']

        except Exception as e:
            print(f"Error loading model: {e}")
            return None

