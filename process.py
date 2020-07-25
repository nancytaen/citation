import re

from classes.reference import Reference

def process_url_text(urls):
    """
    given a string of multiple urls, form IEEE reference
    """
    r = Reference()
    r.format_list(re.split('\r\n', urls))
    return r.get_raw_list()

def process_url_file(file):
    print(file)
    return