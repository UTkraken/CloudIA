def process_string(str : str):
    # filtre de char utf prepare char with -> https://www.i18nqa.com/debug/utf8-debug.html
    str = str.replace("Ã©", "é")
    str = str.replace("Ãª", "ê")
    str = str.replace("Ã¨", "è")
    str = str.replace("Ã¡", "à")
    str = str.replace("Ã", "à")
    str = str.replace("Ã§", "ç")
    str = str.replace("Ã¯", "ï")
    str = str.replace("à§", "ç")
    str = str.replace("à‰", "é")
    str = str.replace("à®", "î")
    str = str.replace("à´", "ô")
    str = str.replace("à‰", "é")
    str = str.replace("à¢", "â")
    str = str.replace("Å“", "e")
    str = str.replace("Â»", "")
    str = str.replace("Â«", "")
    str = str.replace("à€", "À")
    str = str.replace("\n", " ")

    return str