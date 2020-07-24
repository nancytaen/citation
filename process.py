from classes.reference import Reference

def process_url_text(urls):
    """
    """
    r = Reference()
    r.format_list(urls.split('\n'))
    return r.get_raw_list()


def process_url_file(file):
    print(file)
    return