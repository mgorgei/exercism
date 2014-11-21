def detect_anagrams(anagram, alist):
    """
    (str, list of str)-> list of str
    """
    result = []
    sanagram = sorted(anagram.lower())
    for word in alist:
        #discard an entry if it is the exact word
        if anagram.lower() == word.lower():
            continue
        sword = sorted(word.lower())
        if sanagram == sword:
            result.append(word)
    return result
