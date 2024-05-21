import numpy as np
import cv2
import matplotlib.pyplot as plt

"""
Singular Value Decomposition
  Left-singular vector (columns of U)
  Singular values (diagonal entries of singular matrix `Sigma`)
  Right-singular vector (columns of V)

A = U. Sigma. V^T
"""

def compress_image(channel: np.ndarray, k: int):
  U, S, Vt = np.linalg.svd(channel)
  channel_compress = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))

  return channel_compress

def compare_image(original_image, compressed_image):
  # Original Image
  plt.figure(figsize=(10, 5))
  plt.subplot(1, 2, 1)
  plt.title('Original Image')
  plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))

  # Compressed Image
  plt.subplot(1, 2, 2)
  plt.title(f'Compressed Image (k={k})')
  plt.imshow(cv2.cvtColor(compressed_image.astype(np.uint8), cv2.COLOR_BGR2RGB))

  plt.show()

if __name__ == "__main__":
  image = cv2.imread("./image/dog.png")
  b, g, r = cv2.split(image)
  k = int(input())

  compressed_b = compress_image(b, k)
  compressed_g = compress_image(g, k)
  compressed_r = compress_image(r, k)

  compressed_image = cv2.merge((compressed_b, compressed_g, compressed_r))

  compare_image(image, compressed_image)