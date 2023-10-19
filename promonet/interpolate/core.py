import ppgs
import torch

import promonet


###############################################################################
# Feature interpolation
###############################################################################


def pitch(sequence, grid):
    """Interpolate pitch using a grid"""
    return 2 ** grid_sample(torch.log2(sequence), grid)


def ppgs(sequence, grid):
    """Interpolate ppgs using a grid"""
    return grid_sample(sequence, grid, promonet.PPG_INTERP_METHOD)


###############################################################################
# Grid sampling
###############################################################################


def grid_sample(sequence, grid, method='linear'):
    """Perform 1D grid-based sampling"""
    x = grid
    fp = sequence

    # Linear grid interpolation
    if method == 'linear':
        xp = torch.arange(sequence.shape[-1], device=sequence.device)
        i = torch.clip(torch.searchsorted(xp, x, right=True), 1, len(xp) - 1)
        return (
            (fp[..., i - 1] * (xp[i] - x) + fp[..., i] * (x - xp[i - 1])) /
            (xp[i] - xp[i - 1]))

    # Nearest neighbors grid interpolation
    elif method == 'nearest':
        return fp[..., torch.round(x).to(torch.long)]

    # Spherical linear interpolation
    elif method == 'slerp':
        return ppgs.edit.grid.sample(sequence, grid)

    else:
        raise ValueError(f'Grid sampling method {method} is not defined')
