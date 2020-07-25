import sys
from concurrent.futures import ThreadPoolExecutor

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
        with open('reference.txt', 'w') as sys.stdout:
            self.print_list()

    def get_raw_list(self):
        return self.reference_list
        


# r = Reference()
# r.format_list(["https://gen.medium.com/we-dont-view-you-as-americans-that-s-the-bottom-line-c084c7fe8edd?source=topic_page---------------------------20",
# "https://www.economist.com/middle-east-and-africa/2020/07/18/covid-19-has-throttled-south-africas-economy", 
# "https://www.economist.com/business/2020/07/18/the-varying-american-fortunes-of-grindr-and-blued"
# ])
# r.print_list()