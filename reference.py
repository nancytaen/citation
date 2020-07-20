from source import Citation

class Reference:
    """
    represents the entire reference section
    """
    def __init__(self):
        self.reference_list = []
    
    def format_list(self, raw_list):
        for i in range(len(raw_list)):
            c = Citation(raw_list[i])
            self.reference_list.append(c.format())
    
    def print_list(self):
        print(self.reference_list)


r = Reference()
r.format_list(["https://gen.medium.com/we-dont-view-you-as-americans-that-s-the-bottom-line-c084c7fe8edd?source=topic_page---------------------------20",
"https://www.economist.com/middle-east-and-africa/2020/07/18/covid-19-has-throttled-south-africas-economy", 
"https://www.economist.com/business/2020/07/18/the-varying-american-fortunes-of-grindr-and-blued"
])
r.print_list()