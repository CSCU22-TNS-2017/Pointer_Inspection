import cv2
import matplotlib.pyplot as plt
import matplotlib.image as pimg
import copy as cp
import time as t
import os
import numpy as np

def write_line(img):
    cv2.line(img, (0, 160), (640, 160), (0, 0, 255), 1)
    cv2.line(img, (0, 165), (640, 165), (0, 255, 0), 1)
    cv2.line(img, (0, 170), (640, 170), (0, 0, 255), 1)
    cv2.line(img, (0, 240), (640, 240), (255, 255, 255), 1)
    # cv2.line(orig, (0, 310), (640, 310), (0, 0, 255), 1)
    cv2.line(img, (0, 315), (640, 315), (0, 255, 0), 1)

def find_pos(img):
    height,width = img.shape
    order = []
    for i in range(width):
        for j in range(height):
            if img[j][i]==0:
                a = (j,i)
                order.append(a)
                break
            continue

    return order


cap = cv2.VideoCapture(0)
t.sleep(5)
os.system('C:\\Users\\DP\\Desktop\\LED_off.bat')
n=22
while True:
    ret, orig = cap.read()
    img = cp.copy(orig)
    copy1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(copy1, 80, 255, cv2.THRESH_BINARY)
    cv2.imshow('thres', thresh1)
    write_line(img)
    lapla = cv2.Laplacian(thresh1, cv2.CV_64F)
    sobely = cv2.Sobel(thresh1, cv2.CV_64F, 0, 1, ksize=1)
    sobely+=255
    sobely = np.uint8(sobely)
    plt.imshow(sobely,cmap='gray')
    plt.show()
    # area = thresh1[0:160,0:640]
    # boo = 0 in area
    # # cv2.line(orig, (0, 320), (640, 320), (0, 0, 255), 1)
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # if boo:
    #     cv2.putText(img, 'Ng', (10, 350), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    # else:
    #     cv2.putText(img, 'good', (10, 350), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    allpoint = (find_pos(sobely))
    firstpoint = allpoint[0]
    midpoint = allpoint[int(len(allpoint)/2)]
    lastpoint = allpoint[len(allpoint)-1]
    # plt.imshow(thresh1,cmap='gray')
    # plt.show()
    # cv2.line(img, (midpoint[1],midpoint[0]), (lastpoint[1],lastpoint[0]), (0, 0, 255), 1)
    cv2.circle(img, (firstpoint[1], firstpoint[0]), 20, (0, 0, 255), 2)
    cv2.circle(img, (lastpoint[1],lastpoint[0]), 20, (0, 0, 255), 2)
    # plt.imshow(sobely,cmap='gray')
    # plt.show()
    cv2.imshow('orig', img)
    cv2.imshow('sobelY', sobely)
    # cv2.imshow('area',area)
    # if cv2.waitKey(1) & 0xFF == ord('c'):
    #     print(n)
    #     cv2.imwrite(str(n)+'.png', orig)
    #     n+=1
    if cv2.waitKey(1) and 0xFF == ord('q'):#or (move_x=='Ok' and move_y == 'Ok'):
        # cv2.imwrite('4.jpg', orig)
        break
# img = pimg.imread('22.png')
# plt.imshow(img)
# plt.show()
cap.release()
cv2.destroyAllWindows()