MODULE = 'promonet'

# Configuration name
CONFIG = 'bottleneck-latents'

# Whether to perform speaker adaptation (instead of multi-speaker)
ADAPTATION = False

# Input features
INPUT_FEATURES = ['pitch', 'ppg']

# Number of training steps
STEPS = 800000

# Number of channels in the phonetic posteriorgram features
PPG_CHANNELS = 144
