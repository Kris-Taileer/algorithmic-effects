import sys

import numpy as np
from PIL import Image

path = sys.argv[1]
shift = int(sys.argv[2]) if len(sys.argv) > 2 else 20

img = np.array(Image.open(path).convert("RGB"))

r = np.roll(img[:, :, 0], shift, axis=1)
g = img[:, :, 1]
b = np.roll(img[:, :, 2], -shift, axis=1)

out = np.stack([r, g, b], axis=2)
Image.fromarray(out).save("out.jpg")
print("saved: out.jpg")
