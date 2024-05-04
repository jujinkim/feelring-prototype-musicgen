
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
from enum import Enum

class MusicGenModel(Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'

class MusicGenerator:
    def __init__(self, model: MusicGenModel, length, isStereo=False):
        modelName = f'facebook/musicgen-{"stereo-" if isStereo else ""}{model.value}'
        model = MusicGen.get_pretrained(modelName)
        model.set_generation_params(length)
        self.model = model

    def generate(self, prompt):
        # turn prompt into array
        if isinstance(prompt, str):
            prompt = [prompt]

        # generate audio
        waves = self.model.generate(prompt)
        
        # get first wave (waves has only one element)
        wave = waves[0]
        return wave
        
    def writeAudio(self, wave, filename):
        audio_write(filename, wave.cpu(), self.model.sample_rate, strategy="loudness", loudness_compressor=True)
