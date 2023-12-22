words = ["hacker", "bounty", "hunter"]

def is_word_in_string(string):
    if string in words:
        print("It exists!")
        return
    return print("It does not exist!")

is_word_in_string("hacker")

is_word_in_string("bounty")

is_word_in_string("hunter")

is_word_in_string("white-hacker")