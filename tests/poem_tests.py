import json
import pytest
from poem import PoemWhole, PoemByLine


def test_accessors_poem_whole():
    test_poem = PoemWhole("A little Sad", "Toby", "This poem is bad...\nand a little sad")
    assert test_poem.char_count() == 36
    assert test_poem.line_count() == 2
    assert test_poem.avg_chars_in_line() == pytest.approx(18)

def test_accessors_poem_by_line():
    test_poem = PoemByLine("A little Sad", "Toby", ["This poem is bad...", "and a little sad"])
    assert test_poem.char_count() == 36
    assert test_poem.line_count() == 2
    assert test_poem.avg_chars_in_line() == pytest.approx(18)

def create_poem_whole():
    test_poem_1 = PoemWhole("Fire and Ice", "Robert Frost", """Some say the world will end in fire,
Some say in ice.
From what I've tasted of desire
I hold with those who favor fire.
But if it had to perish twice,
I think I know enough of hate
To say that for destruction ice
Is also great
And would suffice.
""")
    return test_poem_1


def create_poem_by_line():
    test_poem_1 = PoemByLine("Fire and Ice", "Robert Frost",
                             ["Some say the world will end in fire,",
                              "Some say in ice.",
                              "From what I've tasted of desire",
                              "I hold with those who favor fire.",
                              "But if it had to perish twice,",
                              "I think I know enough of hate",
                              "To say that for destruction ice",
                              "Is also great",
                              "And would suffice."])
    return test_poem_1
