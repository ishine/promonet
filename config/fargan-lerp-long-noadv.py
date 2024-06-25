MODULE = 'promonet'

# Configuration name
CONFIG = 'fargan-lerp-long-noadv'

# The model to use.
# One of ['fargan', 'hifigan', 'psola', 'vocos', 'world'].
MODEL = 'fargan'

# Step to start using adversarial loss
ADVERSARIAL_LOSS_START_STEP = 1000000

# Training batch size
BATCH_SIZE = 1024

# Training sequence size in samples
CHUNK_SIZE = 4096

# Whether to use mel spectrogram loss
MEL_LOSS = False

# Type of interpolation method to use to scale PPG features
# Available method are ['linear', 'nearest', 'slerp']
PPG_INTERP_METHOD = 'linear'

# Whether to use multi-resolution spectral convergence loss
SPECTRAL_CONVERGENCE_LOSS = True

# Number of training steps
STEPS = 1000000