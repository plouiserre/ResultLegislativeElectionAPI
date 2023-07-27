import unicodedata
from fastapi import HTTPException

def getLabelFormatted(label): 
    label_lower = label.lower()
    label_lower_no_accent = unicodedata.normalize('NFD', label_lower)\
                                            .encode('ascii', 'ignore')\
                                            .decode("utf-8")
    return label_lower_no_accent


def ManageHttpException(exception):
    status_code = 500
    detail_message = "Treatment failed"
    if type(exception) == HTTPException :
        status_code = exception.status_code
        detail_message = "No result"
    raise HTTPException(status_code = status_code, detail= detail_message)