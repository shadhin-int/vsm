import cv2
from PIL import Image


def mark_region(imagE_path):
    im = cv2.imread(imagE_path)

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 30)

    # Dilate to combine adjacent text contours
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    dilate = cv2.dilate(thresh, kernel, iterations=4)

    # Find contours, highlight text areas, and extract ROIs
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    image = None

    line_items_coordinates = []
    for c in cnts:
        # print(c, "<------ccccccccc")
        area = cv2.contourArea(c)
        print(area, "<------aaaaa")
        x, y, w, h = cv2.boundingRect(c)
        print(x, y, w, h, "<------dasdsadasd")

        if y >= 6 and x <= 10:
            if area > 10000:
                image = cv2.rectangle(
                    im, (x, y), (2200, y + h), color=(255, 0, 255), thickness=3)
                line_items_coordinates.append([(x, y), (2200, y + h)])
                print(image, "<------------asadsa")

        if y >= 24 and x <= 20:
            image = cv2.rectangle(im, (x, y), (2200, y + h),
                                  color=(255, 0, 255), thickness=3)
            line_items_coordinates.append([(x, y), (2200, y + h)])
            print(image, "<------------asadsa")

    return image, line_items_coordinates


a = mark_region(imagE_path=f'Page_1.jpg')

print(a, "<-----------")
