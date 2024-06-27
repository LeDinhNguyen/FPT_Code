import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('meotrai.jpg')
img2 = cv2.imread('meophai.jpg')
fig, ax = plt.subplots(1,2, figsize=(8,10))
# ax[0].imshow(img1)
# ax[0].set_title('part1')
# ax[0].axis('off')
# ax[1].imshow(img2)
# ax[1].set_title('part2')
# ax[1].axis('off')
# plt.show()
stitcher = cv2.Stitcher_create()
status, stitched_img = stitcher.stitch((img1, img2))
if status == cv2.Stitcher_OK:
    ## Display the stitched image:
    plt.figure(figsize=(14,10))
    plt.imshow(stitched_img)
    plt.title("Stitched_Image")
    plt.axis("off")
    plt.show()
elif status == cv2.Stitcher_ERR_NEED_MORE_IMGS:
    print('Not enough images for stitching')
elif status == cv2.Stitcher_ERR_HOMOGRAPHY_EST_FAIL:
    print('Homography estimation failed')
else:
    print('Image stitching failed')