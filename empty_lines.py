import os


def remove_empty_lines(text):
    text = os.linesep.join([s for s in text.splitlines() if s])
    return text


my_text = "hi there here is\na big line\n\nof empty\nline\neven some with spaces\n\nlike that\n\n\nokay now what?\n"
t = remove_empty_lines(my_text)
print(my_text)
print()
print()
print(t)
print()
