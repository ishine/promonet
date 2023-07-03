import argparse
from pathlib import Path

import promonet


###############################################################################
# Speaker adaptation
###############################################################################


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description='Perform speaker adaptation')
    parser.add_argument(
        '--name',
        required=True,
        help='The name of the speaker')
    parser.add_argument(
        '--files',
        type=list,
        required=True,
        help='The audio files to use for adaptation')
    parser.add_argument(
        '--checkpoint',
        type=Path,
        default=promonet.DEFAULT_CHECKPOINT,
        help='The model checkpoint')
    parser.add_argument(
        '--gpus',
        type=int,
        nargs='+',
        help='The gpus to run adaptation on')
    return parser.parse_args()


if __name__ == '__main__':
    promonet.adapt.speaker(**vars(parse_args()))
