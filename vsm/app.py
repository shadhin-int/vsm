# # from pdf2image import convert_from_path
# # import cv2
# # from PIL import Image
# # # pdfs = r'./file.pdf'
# #
# # pages = convert_from_path(pdf_path=f'file.pdf')
# #
# #
# # i = 1
# # for page in pages:
# #     image_name = "Page_" + str(i) + ".jpg"
# #     page.save(image_name, "JPEG")
# #     i += 1
# import json

# import fitz
# import pandas as pd

# doc = fitz.open('file.pdf')
# page1 = doc[0]
# words = page1.get_text("words")

# print(words[0])

# first_annots = []

# rec = page1.first_annot.rect


# def make_text(words):
#     line_dict = {}
#     words.sort(key=lambda w: w[0])

#     for w in words:
#         y1 = round(w[3], 1)
#         word = w[4]
#         line = line_dict.get(y1, [])
#         line.append(word)
#         line_dict[y1] = line

#     lines = list(line_dict.items())
#     lines.sort()

#     return "n".join([" ".join(line[1]) for line in lines])


# mywords = [w for w in words if fitz.Rect(w[:4]) in rec]
# ann = make_text(mywords)
# first_annots.append(ann)

# print(rec, "<---------")

from autoocr import AutoOCR
oa = AutoOCR(lang='bangla')  # specify the language code
oa.set_datapath(r'tesseract')
# oa.set_datapath('/usr/local/Cellar/tesseract/5.2.0/share/tessdata/')
out_text = oa.get_text('Page_1.png')



print(out_text)

