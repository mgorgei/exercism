#old = {1: ['APPLE', 'ARTICHOKE'], 2: ['BOAT', 'BALLERINA']}
old = {1: "AEIOULNRST",2: "DG",3: "BCMP",4: "FHVWY",5: "K",8: "JX",10: "QZ",}
x = {}
for key in old:
    if type(old[key]) == list:
        for word in old[key]:
            x[word.lower()] = key
    elif type(old[key]) == str:
        for word in old[key]:
            x[word.lower()] = key
#x = dict((word,key) for (word, key) in old.items())
#expected = {'apple': 1,'artichoke': 1,'boat': 2,'ballerina': 2}
expected = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1,"f": 4, "g": 2, "h": 4, "i": 1, "j": 8,"k": 5, "l": 1, "m": 3, "n": 1, "o": 1,"p": 3, "q": 10, "r": 1, "s": 1, "t": 1,"u": 1, "v": 4, "w": 4, "x": 8, "y": 4,"z": 10}
print(x, expected, x == expected)
