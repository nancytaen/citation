import sys
from concurrent.futures import ThreadPoolExecutor

from classes.citation import Citation


class Reference:
    """
    represents the entire reference section
    """
    def __init__(self):
        self.reference_list = []
    
    def format_list(self, raw_list):
        with ThreadPoolExecutor(max_workers=50) as executor:
            for i in range(len(raw_list)):
                executor.submit(self.create_citation, raw_list[i])
    
    def create_citation(self, source):        
        source = source.strip(' ')
        if source:
            c = Citation(source)
            self.reference_list.append(c.format())
    
    def print_list(self):
        for i in range(len(self.reference_list)):
            print("[{}] {}\n".format(str(i=1), self.reference_list[i]))

    def export_to_text(self):
        with open('referece.txt', 'w') as sys.stdout:
            self.print_list()

    def get_raw_list(self):
        return self.reference_list
        


# r = Reference()
# r.format_list(["https://gen.medium.com/we-dont-view-you-as-americans-that-s-the-bottom-line-c084c7fe8edd?source=topic_page---------------------------20",
# "https://www.economist.com/middle-east-and-africa/2020/07/18/covid-19-has-throttled-south-africas-economy", 
# "https://www.economist.com/business/2020/07/18/the-varying-american-fortunes-of-grindr-and-blued"
# ])
# r.export_to_text()