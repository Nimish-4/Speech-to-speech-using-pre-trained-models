import edge_tts

"""
ShortName: en-US-AriaNeural
Gender: Female
Locale: en-US


ShortName: en-US-ChristopherNeural
Gender: Male
Locale: en-US

"""

async def generate_speech(text: str, voice: str = "female", pitch: str = "+0Hz", rate: str = "+0%"):
    

    tts = edge_tts.Communicate(text, 
        voice= "en-US-AriaNeural" if voice=="female" else "en-US-ChristopherNeural",
        rate = rate,
        pitch = pitch)
    

    await tts.save("response.mp3")
    return
