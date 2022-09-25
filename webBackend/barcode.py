import cv2
import urllib.request
import json

can = ["Dose", "Aluminium", "Aluminiumdose"]
plastic_bottle = ["Bottle", "Plastic", "Plastik", "Flasche", "Plastikflasche"]
plastic = ["Plastic", "Plastik", "Produkt", "Product", "en:Plastic", 'Kunststoff', ' Tüte', ' PP - Polypropylen']


def return_barcode(img):
    bardet = cv2.barcode_BarcodeDetector()
    ok, decoded_info, decoded_type, corners = bardet.detectAndDecode(img)
    if ok is True:
        return decoded_info[0]
    else:
        return 1


def return_json(barcode):
    url = 'https://world.openfoodfacts.org/api/v0/product/' + str(barcode) + '.json'
    response = urllib.request.urlopen(url)
    d = json.loads(response.read())
    return d


def scan():
    classification = ''
    name = ''
    imgurl = ''
    pb_score = 0
    c_score = 0
    p_score = 0
    image = cv2.imread('imageToSave.jpg')
    bar = return_barcode(image)
    if not (bar == 1):
        data = return_json(bar)
        if "product" in data:
            product = data["product"]
            name = product["product_name"]
            if "image_front_url" in product:
                imgurl = product["image_front_url"]
            pkg_str = product["packaging"]
            pkg_list = pkg_str.split(',')
            for cat in pkg_list:
                if cat in plastic_bottle:
                    pb_score += 1
                if cat in can:
                    c_score += 1
                if cat in plastic:
                    p_score += 1

                classification = 'Unknown'
                if c_score > pb_score and c_score > p_score:
                    classification = 'Can'
                elif pb_score > c_score and pb_score > c_score:
                    classification = 'Plastic Bottle'
                elif p_score > c_score and p_score > pb_score:
                    classification = 'Plastic'
    return name, classification, imgurl


if __name__ == '__main__':
    scan()
