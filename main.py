import cv2
import pytesseract
import os

count_valid = []

def read_image(image_name):
    """function to read an image and convert it to grayscale"""
    invalid_list = []
    # convert image to grayscale
    img = cv2.imread(image_name, 0)
    # print(img)

    ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)
    print("Threshold selected : ", ret)
    cv2.imwrite("./output_image.png", thresh)

    #sharpen the image
    gray = cv2.bilateralFilter(img, 11, 17, 17)

    # view image in gray scale
    cv2.imshow("Gray scale image", gray)
    cv2.waitKey(100)

    # detect edges in the image
    edges = cv2.Canny(gray, 100, 200)
    cv2.imshow("Edges of Car", edges)
    cv2.waitKey(100)

    # find contours in the images
    cnts, new = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    img1 = img.copy()
    cv2.drawContours(img1, cnts, -1, (0, 255, 0), 3)
    # display contoured image
    cv2.imshow("All contours", img1)
    cv2.waitKey(100)

    new_img = None
    #display top 10 contours
    sorted_cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
    img2 = img.copy()
    cv2.drawContours(img2, sorted_cnts, -1, (0, 255, 0), 3)
    cv2.imshow("Top 10 Contours sorted", img2)
    cv2.waitKey(100)

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
            cv2.imwrite('Cropped Images' + str(idx)+'.png', new_img)
            idx += 1

            break

    print(NumberPlateCnt)

    if NumberPlateCnt is not None:
        cv2.drawContours(img, [NumberPlateCnt], -1, (0, 255, 0), 3)
        cv2.imshow("image with number plate detected", img)
        cv2.waitKey(0)

        cropped_img = 'Cropped Images7.png'

        text = pytesseract.image_to_string(cropped_img, lang='eng')
        print("Detected text: "+text)
        if len(text) > 5:
            count_valid.append(text)
        else:
            invalid_list.append(image_name)
        return text
    else:
        return None


def read_all():
    path = './images/baza_slika'

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.jpg' in file:
                files.append(os.path.join(r, file))

    print("File size: "+str(len(f)))

    for f in files:
        print("Processing image", f)
        print(read_image(f))

    print("Accuracy: " + str(len(count_valid) / len(f)))
    print("File size: " + str(len(f)))


if __name__ == '__main__':
    read_all()
    #read_image('./images/baza_slika/141002/Pa140021.jpg')
    print("Correctly identified: "+str(len(count_valid)))



