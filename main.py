import cv2
import pytesseract


def read_image(image_name):
    """function to read an image and convert it to grayscale"""
    # convert image to grayscale
    img = cv2.imread(image_name, cv2.COLOR_BGR2GRAY)
    # print(img)

    gray = cv2.bilateralFilter(img, 11, 17, 17)
    # view image in gray scale
    cv2.imshow("gray", gray)
    cv2.waitKey(0)
    # detect edges in the image
    edges = cv2.Canny(gray, 100, 200)
    cv2.imshow("Edges of Car", edges)
    cv2.waitKey(0)

    # find contours in the images
    cnts, new = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    img1 = img.copy()
    cv2.drawContours(img1, cnts, -1, (0, 255, 0), 3)
    # display contoured image
    cv2.imshow("All contours", img1)
    cv2.waitKey(0)

    # select top 10 contours
    sorted_cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
    img2 = img.copy()
    cv2.drawContours(img2, sorted_cnts, -1, (0, 255, 0), 3)
    cv2.imshow("Top 30 Contours sorted", img2)
    cv2.waitKey(0)

    NumberPlateCnt = None
    idx = 7
    for c in sorted_cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            NumberPlateCnt = approx

            x, y, w, h = cv2.boundingRect(c)
            print("height is ", y + h)
            print("width is " , x + w)
            new_img = img[y:y + h, x:x + w]
            cv2.imwrite('Cropped Images'+ str(idx)+'.png', new_img)
            idx+=1

            break

    print(NumberPlateCnt)
    cv2.drawContours(img, [NumberPlateCnt], -1, (0, 255, 0), 3)
    cv2.imshow("image with number plate detected", img)
    cv2.waitKey(0)

    cropped_img = 'Cropped Images7.png'
    text = pytesseract.image_to_string(cropped_img, lang = 'eng')
    print(text)


if __name__== "__main__":
    #read_image(image_name='images/baza_slika/040603/P1010002.jpg')