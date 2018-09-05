import torch


def binary_dice_loss(input, target, smooth=1, weight=None):
    """
    Binary Dice loss.

    Parameters
    ----------
    output : torch tensor
        Output of model.

    target : torch tensor
        True mask of the image.

    smooth : float
        Smoothing factor.

    References
    ----------
    https://github.com/pytorch/pytorch/issues/1249
    """
    input = torch.sigmoid(input)

    input = input.view(-1)
    target = target.view(-1)
    intersection = (input * target).sum()

    loss = 1 - ((2. * intersection + smooth) /
           (input.sum() + target.sum() + smooth))

    if weight is not None:
        loss = loss * weight

    if not reduce:
        return loss

    if size_average:
        return loss.mean()

    return loss


def dice_coefficient(input, target, smooth=1):
    """
    Compute dice coefficient.
    """
    input = torch.sigmoid(input)
    batch_size = input.size(0)
    input = input.view(batch_size, -1)
    target = target.view(batch_size, -1)
    intersection = (input * target).sum()

    return ((2. * intersection + smooth) /
           (input.sum() + target.sum() + smooth))
