import sys

import numpy as np
from PIL import Image

path = sys.argv[1]
threshold = int(sys.argv[2]) if len(sys.argv) > 2 else 120

img = np.array(Image.open(path).convert("RGB"), dtype=np.float32)


def luminance(row):
    return 0.2126 * row[:, 0] + 0.7152 * row[:, 1] + 0.0722 * row[:, 2]


def sort_row(row):
    bright = luminance(row) > threshold
    out = row.copy()
    i = 0
    while i < len(row):
        if bright[i]:
            j = i
            while j < len(row) and bright[j]:
                j += 1
            span = row[i:j]
            out[i:j] = span[np.argsort(luminance(span))]
            i = j
        else:
            i += 1
    return out


result = np.array([sort_row(row) for row in img])

Image.fromarray(result.astype(np.uint8)).save("out.jpg")
print("saved: out.jpg")
