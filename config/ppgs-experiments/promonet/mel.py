MODULE = 'promonet'

# Configuration name
CONFIG = 'mel'

# Batch size
BATCH_SIZE = 32

# Number of samples generated during training
CHUNK_SIZE = 8192

# Evaluation ratios for pitch-shifting, time-stretching, and loudness-scaling
EVALUATION_RATIOS = [.891, 1.12]

# Input features
INPUT_FEATURES = ['pitch', 'ppg']

# The model to use. One of ['hifigan', 'psola', 'vits', 'vocos', 'world'].
MODEL = 'vits'

# Number of training steps
STEPS = 250000