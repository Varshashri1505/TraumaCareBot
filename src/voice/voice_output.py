import asyncio
import edge_tts
import pygame
import os

VOICE = "en-IN-NeerjaNeural"   # Indian Female Voice

async def generate_voice(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("response.mp3")


def speak(text):

    asyncio.run(generate_voice(text))

    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.quit()

    os.remove("response.mp3")
