from classes.citation import Citation

"""
python3 -m pytest test/
"""

def format_authors(authors, is_name):
    """
    authors: List of authors
    is_name: boolean; indicates people name or corporate name
    """
    c = Citation("", is_test=True)
    c.authors = authors
    c.is_name = is_name
    c.format_authors()
    return c.authors


class TestCitation:
    """
    includes all tests related to citation class
    """

    def test_authors(self):
        assert format_authors(["The Economist"], False) == "The Economist,"
        assert format_authors(["Louis Bass"], True) == "L. Bass,"
        assert format_authors(["Michael Toby Kimour"], True) == "M. T. Kimour,"
        assert format_authors(["Connor Wilson-Clark"], True) == "C. Wilson-Clark,"