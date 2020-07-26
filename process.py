import re

from classes.reference import Reference

def process_url_text(urls, req_file):
    """
    given a string of multiple urls, form IEEE reference
    if req_file is True, the server sends a text file back
    """
    r = Reference()
    r.format_list(re.split('\r\n', urls))
    if req_file:
        r.export_to_text()
    return r.get_raw_list()

def process_url_file(file, req_file):
    """
    read txt file
    if req_file is True, the server sends a text file back 
    """
    f = file.read().decode("utf-8")
    return process_url_text(f, req_file)