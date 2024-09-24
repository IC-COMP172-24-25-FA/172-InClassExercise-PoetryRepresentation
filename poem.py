class PoemWhole:

    def __init__(self, title, author, poem_body):
        """:param poem_body: a string with formatted text for the entire poem"""
        self.title = title
        self.author = author
        self.poem_body = poem_body

    def char_count(self):
        raise RuntimeError("Not implemented yet")

    def line_count(self):
        raise RuntimeError("Not implemented yet")

    def avg_chars_in_line(self):
        raise RuntimeError("Not implemented yet")

    def __str__(self):
        raise RuntimeError("Not implemented yet")



class PoemByLine:

    def __init__(self, title, author, lines_list):
        """:param lines_list: a list of strings, one per line of the poem"""
        self.title = title
        self.author = author
        self.lines_list = lines_list

    def char_count(self):
        raise RuntimeError("Not implemented yet")

    def line_count(self):
        raise RuntimeError("Not implemented yet")

    def avg_chars_in_line(self):
        raise RuntimeError("Not implemented yet")

    def __str__(self):
        raise RuntimeError("Not implemented yet")
