MODULE = 'ppgs'

# Configuration name
CONFIG = 'w2v2fc'

# Network width
HIDDEN_CHANNELS = 512

# Dimensionality of input representation
INPUT_CHANNELS = 768

# Number of hidden layers
NUM_HIDDEN_LAYERS = 5

# Input representation
REPRESENTATION = 'w2v2fc'

# representation kind
# One of ['ppg', 'latents'].
REPRESENTATION_KIND = 'latents'

# Local checkpoint to use
# If None, Huggingface will be used unless a checkpoint is given in the CLI
LOCAL_CHECKPOINT = f'/repos/ppgs/runs/{CONFIG.split("-")[0]}/00150000.pt'
