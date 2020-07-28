import sys
from concurrent.futures import ThreadPoolExecutor
import hashlib
from datetime import datetime

from classes.citation import Citation


class Reference:
    """
    represents the entire reference section
    """
    def __init__(self):
        self.reference_list = {}
    
    def format_list(self, raw_list):
        """
        format each citation given a list of urls
        """
        with ThreadPoolExecutor(max_workers=50) as executor:
            for i in range(len(raw_list)):
                executor.submit(self.create_citation, raw_list[i], i)
        self.sort_dict()

    def sort_dict(self):
        """
        sort reference dict in order of keys
        """
        self.reference_list = dict(sorted(self.reference_list.items()))
    
    def create_citation(self, source, num):
        """
        helper function; create and format single url using IEEE
        """    
        source = source.strip(' ')
        if source:    
            c = Citation(source)
            self.reference_list[num + 1] = c.format()
    
    def print_list(self):
        for num, citation in self.reference_list.items():
            print("[{}] {}\n".format(str(num), citation))

    def export_to_text(self):
        filename = hashlib.sha256(("reference" + str(datetime.now())).encode()).hexdigest() + ".txt"
        with open('static/client/' + filename, 'w') as sys.stdout:
            self.print_list()
        return filename

    def get_raw_list(self):
        return self.reference_list
        