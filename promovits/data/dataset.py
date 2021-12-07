import os

import torch

import promovits


###############################################################################
# Base dataset
###############################################################################


class Dataset(torch.utils.data.Dataset):

    def __init__(self, dataset, partition):
        super().__init__()
        self.stems = promovits.load.partition(dataset)[partition]
        self.cache = promovits.CACHE_DIR / dataset

        # Store spectrogram lengths for bucketing
        audio_files = list([self.cache / f'{stem}.wav' for stem in self.stems])
        self.spectrogram_lengths = [
            os.path.getsize(audio_file) // (2 * promovits.HOPSIZE)
            for audio_file in audio_files]

    def __len__(self):
        return len(self.stems)


###############################################################################
# Datasets
###############################################################################


class PPGDataset(torch.utils.data.Dataset):

    def __init__(self, dataset, partition, interp_method='nearest'):
        super().__init__(dataset, partition)
        self.interp_method = interp_method

    def __getitem__(self, index):
        stem = self.stems[index]
        audio = promovits.load.audio(self.cache / f'{stem}.wav')
        speaker = torch.tensor(int(stem.split('-')[0]), dtype=torch.long)
        spectrogram = torch.load(self.cache / f'{stem}-spectrogram.pt')
        ppg = self.get_ppg(self.cache / f'{stem}-ppg.pt', spectrogram.shape[1])
        return (ppg, spectrogram, audio, speaker)

    def get_ppg(self, filename, length):
        """Load PPG features"""
        ppg = torch.load(filename)

        # Maybe resample length
        if ppg.shape[1] != length:
            ppg = torch.nn.functional.interpolate(
                ppg[None],
                size=length,
                mode=self.interp_method)[0]

        return ppg


class TextDataset(Dataset):

    def __getitem__(self, index):
        stem = self.stems[index]
        audio = promovits.load.audio(self.cache / f'{stem}.wav')
        text = promovits.load.phonemes(self.cache / f'{stem}-phonemes.pt')
        speaker = torch.tensor(int(stem.split('-')[0]), dtype=torch.long)
        spectrogram = torch.load(self.cache / f'{stem}-spectrogram.pt')
        return (text, spectrogram, audio, speaker)