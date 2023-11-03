import torch

import promonet


###############################################################################
# Sampler selection
###############################################################################


def sampler(dataset, partition):
    """Create batch sampler"""
    # Deterministic random sampler for training and validation
    if partition.startswith('train') or partition.startswith('valid'):
        return Sampler(dataset)

    # Sample test data sequentially
    elif partition.startswith('test'):
        return torch.utils.data.BatchSampler(
            torch.utils.data.SequentialSampler(dataset),
            1,
            False)

    else:
        raise ValueError(f'Partition {partition} is not defined')


###############################################################################
# Samplers
###############################################################################


class Sampler:

    def __init__(self, dataset):
        self.epoch = 0
        self.length = len(dataset)
        self.buckets = dataset.buckets()

    def __iter__(self):
        return iter(self.batch())

    def __len__(self):
        return self.length

    def batch(self):
        """Produces batch indices for one epoch"""
        # Deterministic shuffling based on epoch
        generator = torch.Generator()
        generator.manual_seed(promonet.RANDOM_SEED + self.epoch)

        # Make batches with roughly equal number of frames
        batches = []
        for _, bucket in self.buckets:

            # Shuffle bucket
            bucket = bucket[
                torch.randperm(len(bucket), generator=generator).tolist()]

            # Get current batch size
            size = promonet.BATCH_SIZE

            # Make batches
            batches.extend(
                [bucket[i:i + size] for i in range(0, len(bucket), size)])

        # Shuffle
        return [
            batches[i] for i in
            torch.randperm(len(batches), generator=generator).tolist()]

    def set_epoch(self, epoch):
        self.epoch = epoch
