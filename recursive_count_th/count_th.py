'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def helper(word, start, end, result):
    if start == end:
        return result
    elif word[start:start + 2] == "th":
        result += 1
        return helper(word, start + 2, end, result)
    else:
        return helper(word, start + 1, end, result)


def count_th(word):
    result = 0
    start = 0
    end = len(word)
    return helper(word, start, end, result)