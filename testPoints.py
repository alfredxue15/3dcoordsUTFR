import cv2

points0 = [[315,357], [358, 357], [358, 400], [315, 400], [514, 409], [238, 84], [237, 268], [432, 228], [556, 229], [440, 348], [538, 348]]
points1 = [[146, 112], [150, 268], [249, 342], [288, 341], [250, 379], [288, 379], [417, 384], [362, 228], [470, 228], [373, 330], [457, 330]]
frame0 = cv2.imread('test_img_pair/camera0_0.png')
frame1 = cv2.imread('test_img_pair/camera1_0.png')

for i in range(len(points0)):
    frame0 = cv2.circle(frame0, points0[i], radius=0, color=(0, 0, 255), thickness=4)
for i in range(len(points1)):
    frame1 = cv2.circle(frame1, points1[i], radius=0, color=(0, 0, 255), thickness=4)


cv2.imshow("Frame", frame0)
cv2.waitKey()
cv2.imshow("Frame", frame1)
cv2.waitKey()
