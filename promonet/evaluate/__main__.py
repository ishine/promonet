import argparse
from pathlib import Path

import promonet


###############################################################################
# Evaluate
###############################################################################


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description='Perform evaluation')
    parser.add_argument(
        '--datasets',
        nargs='+',
        default=promonet.DATASETS,
        help='The datasets to evaluate')
    parser.add_argument(
        '--checkpoint',
        type=Path,
        default=promonet.DEFAULT_CHECKPOINT,
        help='The checkpoint to use')
    parser.add_argument(
        '--gpu',
        type=int,
        help='The index of the gpu to use for evaluation')
    return parser.parse_known_args()[0]


promonet.evaluate.datasets(**vars(parse_args()))
