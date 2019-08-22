import cv2
# import imutils
# import pytesseract


def read_image(image):
    """function to read an image and convert it to grayscale"""
    return image + " : ok?"

# img = cv2.imread('images/P1010001.jpg', 0)
# gray = cv2.bilateralFilter(img, 11, 17, 17)
# cv2.imshow("gray", gray)
# cv2.waitKey(0)
# edges = cv2.Canny(gray, 100, 200)
# #cv2.imshow("car", edges)
# #cv2.waitKey(0)
# cnts, new = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# img1 = img.copy()
# cv2.drawContours(img1, cnts, -1, (0, 255, 0), 3)
# cv2.imshow("contour", img1)
# cv2.waitKey(0)
# sorted_cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
# img2 = img.copy()
# cv2.drawContours(img1, sorted_cnts, -1, (0, 255, 0), 3)
# cv2.imshow("contour", img2)
# cv2.waitKey(0)
# NumberPlateCnt = None


# def main():
#     print("hello world!")
#
# if __name__== "__main__":
#     read_image(img=1)