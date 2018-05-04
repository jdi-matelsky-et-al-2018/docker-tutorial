#!/usr/bin/env python3

import sys
import os

import pydicom
import numpy as np


def main(fname, outdirectory, minval=0, maxval=100):
    minval = int(minval)
    maxval = int(maxval)
    data = pydicom.read_file(fname)
    normalized_pixels = data.pixel_array

    normalized_pixels = (
        normalized_pixels - np.min(normalized_pixels)
    )

    normalized_pixels = (
        normalized_pixels / np.max(normalized_pixels)
    ) * int(maxval - minval)

    normalized_pixels += int(minval)

    data.PixelData = normalized_pixels.tostring()

    outname = ".".join(
        os.path.basename(fname).split(".")[:-1]
    ) + "-normalized.dcm"

    pydicom.write_file("{}/{}".format(
        outdirectory, outname
    ), data)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
