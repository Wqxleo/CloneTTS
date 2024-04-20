import os.path

import torchaudio

wavs_dir = "wavs"

for sub_dir in os.listdir(wavs_dir):
    sub_path = os.path.join(wavs_dir,sub_dir)

    for audio_name in os.listdir(sub_path):
        audio_path = os.path.join(sub_path,audio_name)
        audio,sr = torchaudio.load(audio_path)
        if(sr != 24000):
            audio = torchaudio.transforms.Resample(orig_freq=sr,new_freq=24000)(audio)
            torchaudio.save(audio_path,audio,sample_rate=24000)