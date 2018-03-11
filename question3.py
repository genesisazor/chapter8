def find(strng, ch, start=0):
    index = start
    while index < len(strng):
          if strng[index] == ch:
              return index
          index += 1
    return -1

def count_letters(word, letter):
    a    = find(word, letter, 0)
    count = 0
    while a != -1:
        a    = find(word, letter, a+1)
        count += 1
    return count