import unicodedata

def getLabelFormatted(label): 
    label_lower = label.lower()
    label_lower_no_accent = unicodedata.normalize('NFD', label_lower)\
                                            .encode('ascii', 'ignore')\
                                            .decode("utf-8")
    return label_lower_no_accent