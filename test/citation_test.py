from classes.citation import Citation


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
