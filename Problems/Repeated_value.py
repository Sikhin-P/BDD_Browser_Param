
def repeat_finder(word):
    letter_dict = dict()
    for w in word:
        if w in letter_dict:
            letter_dict[w] += 1
        else:
            letter_dict[w] = 1
    return letter_dict

print(repeat_finder('Good Morning'))