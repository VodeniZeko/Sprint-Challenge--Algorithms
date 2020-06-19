'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0


def count_th(word):
    # base case
    if len(word) < 2:
        return 0
    # if the first two letters are th
    # return a 1
    else:
        th_in_word = 0
        if word[0:2] == 'th':
            print(word[:2])
            th_in_word = 1
    return th_in_word + count_th(word[1:])


print(count_th('sdsdgsgsgsgsgssd'))
