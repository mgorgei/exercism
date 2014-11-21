import string

def encode(s):
    s = s.lower().translate(str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase,
        string.punctuation.join(string.whitespace)))
    square = 1
    while square * square < len(s):
        square += 1
    result = ""
    for j in range(square * square):
        pos = (j // square) + (j % square) * square
        if pos < len(s):
            result += s[pos]
        if (len(result) + 1) % 6 == 0:
            result += ' '
    return result.rstrip()

def decode(s):
    s = s.translate(str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase,
        string.whitespace))
    square = 1
    while square * square < len(s):
        square += 1
    rows = square
    rows -= square * square > len(s)
    result = ""
    difference = square * rows - len(s)
    #pad the string so that the square can be mathematically traveled
    for j in range(square - difference + 1, square + 1):
        s = s[:j * rows - 1] + '*' + s[j * rows - 1:]
    for j in range(square * rows):
        pos = (j // square) + (j % square) * rows
        if pos < len(s):
            result += s[pos]
    return result[:-difference]
