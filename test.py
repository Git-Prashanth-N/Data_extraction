# Created by Prashanth.N

# libraries for converting image_to_text
from PIL import Image
import pytesseract
import re
import cv2
import numpy as np

try:

    # Create an image object of PIL library.................................
    image = Image.open('load/img1.jpeg')
    image = np.array(image)

    # Adding Filters to image .............................................
    img_a0 = cv2.resize(image, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
    img_a0 = cv2.bilateralFilter(img_a0, 9, 76.1, 76.1)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_a1 = cv2.resize(gray, None, fx=3.1, fy=3.1, interpolation=cv2.INTER_AREA)
    img_a1 = cv2.bilateralFilter(img_a1, 9, 76.1, 76.1)

    img_a2 = cv2.resize(image, None, fx=7.1, fy=7.1, interpolation=cv2.INTER_AREA)
    img_a2 = cv2.bilateralFilter(img_a2, 11, 78, 78)

    img0 = cv2.resize(image, None, fx=2.1, fy=2.1, interpolation=cv2.INTER_AREA)
    img0 = cv2.bilateralFilter(img0, 9, 76.1, 76.1)

    img1 = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)
    img1 = cv2.bilateralFilter(img1, 9, 76.1, 76.1)

    img2 = cv2.resize(image, None, fx=8, fy=8, interpolation=cv2.INTER_AREA)
    img2 = cv2.bilateralFilter(img2, 9, 75, 75)

    img3 = cv2.resize(image, None, fx=3, fy=3, interpolation=cv2.INTER_AREA)
    img3 = cv2.bilateralFilter(img3, 9, 74, 74)

    img4 = cv2.resize(image, None, fx=4.1, fy=4.1, interpolation=cv2.INTER_AREA)
    img4 = cv2.bilateralFilter(img4, 9, 75, 75)

    img5 = cv2.resize(image, None, fx=4, fy=4, interpolation=cv2.INTER_AREA)
    img5 = cv2.bilateralFilter(img5, 9, 75, 75)

    img6 = cv2.resize(image, None, fx=3, fy=3, interpolation=cv2.INTER_AREA)
    img6 = cv2.bilateralFilter(img6, 9, 75, 75)

    img7 = cv2.resize(image, None, fx=4.2, fy=4.2, interpolation=cv2.INTER_AREA)
    img7 = cv2.bilateralFilter(img7, 9, 76.1, 76.1)

    # pass image into pytesseract module to extract the text from image.....................................
    a0 = pytesseract.image_to_string(img_a0, lang='eng')
    a1 = pytesseract.image_to_string(img_a1, lang='eng')
    a2 = pytesseract.image_to_string(img_a2, lang='eng')
    a = pytesseract.image_to_string(img0, lang='eng')
    b = pytesseract.image_to_string(img1, lang='eng')
    c = pytesseract.image_to_string(img2, lang='eng')
    d = pytesseract.image_to_string(img3, lang='eng')
    e = pytesseract.image_to_string(img4, lang='eng')
    f = pytesseract.image_to_string(img5, lang='eng')
    g = pytesseract.image_to_string(img6, lang='eng')
    h = pytesseract.image_to_string(img7, lang='eng')

    sub1 = a + b + c + d
    sub2 = e + f + g + h
    sub3 = a0 + a1 + a2
    # concatinating the text extracted from different filtered images
    Final_extract = sub1 + sub2 + sub3

    # # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # img1 = cv2.resize(image, None, fx=6.1, fy=6.1, interpolation=cv2.INTER_AREA)
    # img1 = cv2.bilateralFilter(img1, 9, 74, 74)
    # Final_extract = pytesseract.image_to_string(img1, lang='eng')

    print(Final_extract)

    # regex to find  particular date pattern in the image provided..........................
    regex = "[0-9]{2}-[A-Z]{3}\s-[0-9]{4}|[0-9]{2}/[A-Z|a-z]{3}/[0-9]{4}|[0-9]{2}/[0-9]{2}/[0-9]{4}|[0-9]{2}-[A-Z]{3}-[0-9]{4}|[0-9]{2}/[0-9]{2}/[0-9]{4}|" \
            "[0-9]{1}/[0-9]{2}/[0-9]{4}|[0-9]{2}-[A-Z|a-z]{3}-[0-9]{4}|[0-9]{1}/[A-Z|a-z]{3}/[0-9]{4}|[0-9]{2}/[0-9]{2}/[0|1|9|8|6|7|5]{2}|" \
            "[0-9]{2}-[0-9]{2}-[0-9]{4}|[0-9]{2}-[A-Z|a-z]{3}-[0-9]{2}|[A-Z|a-z]{3}\s[0-9]{2},\s[0-9]{4}|[A-Z|a-z]{3}\s[0-9]{1},\s[0-9]{4}|" \
            "[0-9]{2}-[0-9]{2}-[0-9]{2}|[A-Z|a-z]{2}-[0-9]{2}-[0-9]{2}-[A-Z|a-z]{1}|[0-9&A-Z&a-z]{5}'\s[0-9]{2}|[0-9]{2}[A-Z|a-z]{3}'[0-9]{2}|" \
            "[A-Z|a-z]{4}\s[0-9]{2},\s[0-9]{4}|[0-9]{2}/[0-9]{2}/[0-9]{2}|[0-9]{1}/[0-9]{2}/[0-9]{2}|[0-9]{4}-[0-9]{2}-[0-9]{2}" \

    x = re.search(regex, Final_extract)

    if x:
        print("date:", x.group(0))
    else:
        print("date:", x)

except Exception as ex:
    print(ex)
