words = ["hacker", "bounty", "hunter"]

def is_word_in_string(string):
    for word in words:
        if word in string:
            return "It exists!"
    return "It does not exist!"

is_word_in_string("hacker")

is_word_in_string("bounty")

is_word_in_string("hunter")

is_word_in_string("white-hacker")