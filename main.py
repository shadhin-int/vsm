from autoocr import AutoOCR


if __name__ == '__main__':
    oa = AutoOCR(lang='bangla')  # specify the language code
    oa.set_datapath(r'tesseract')
    out_text = oa.get_text('Page_1.png')

    data =[]

    for text in out_text:
        data.append(text)

    print(data)


