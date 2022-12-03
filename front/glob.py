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

    return str