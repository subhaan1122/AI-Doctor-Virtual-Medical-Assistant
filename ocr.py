from paddleocr import PaddleOCR
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False)

def perform_ocr(path_to_test):
    result = ocr.predict(
        input=path_to_test)

    for res in result:
        res.save_to_img("output")
        res.save_to_json("output")
