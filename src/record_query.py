import models.whisper_asr as whisper_asr
import models.phi_2 as phi_2
import inference_api
import text_to_speech
import pyaudio
import wave
import numpy as np
import asyncio
import warnings


warnings.simplefilter(action='ignore', category=UserWarning)        # suppress warnings for readability
warnings.simplefilter(action='ignore', category=FutureWarning)

SAMPLING_RATE = 16000  
CHANNELS = 1           
VAD_THRESHOLD = 0.5    



def is_voice(data, threshold=VAD_THRESHOLD):
    return np.max(np.abs(data)) > threshold


def record_audio(filename, duration=5):
    p = pyaudio.PyAudio()

    
    stream = p.open(format=pyaudio.paInt16,
                    channels=CHANNELS,
                    rate=SAMPLING_RATE,
                    input=True,
                    frames_per_buffer=1024)

    print("Recording...")
    frames = []

    for _ in range(0, int(SAMPLING_RATE / 1024 * duration)):
        data = stream.read(1024)
        data_np = np.frombuffer(data, dtype=np.int16)
        if is_voice(data_np):
            frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(SAMPLING_RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


if __name__ == "__main__":

    audio_file = "query.wav"
    record_audio(audio_file)

    transcription = whisper_asr.convert_to_text(audio_file)
    print("Transcription:",transcription)

    #response = phi_2.query_response(transcription)
    response = inference_api.query_response(transcription+"Use two sentences.")
    print("Generated Text:")
    print(response)

    
    voice = "male"  # male or female voice
    pitch = "-5Hz"  # pitch adjustment above standard pitch
    rate = "+10%"   # speed adjustment over normal rate

    asyncio.run(text_to_speech.generate_speech(response,voice,pitch,rate))

