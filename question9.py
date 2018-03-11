def remove_letter(letter, word):
    new = ""
    for ch in word:
        if ch != letter:
            new += ch
    return new

remove_letter("a", "apple")
