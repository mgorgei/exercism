import string
s="AS DF.GhIJKLMNOP"
i = 1
s = s.lower().translate(str.maketrans(
    string.ascii_lowercase,
    string.ascii_lowercase,
    string.punctuation.join(string.whitespace)))
while i*i < len(s):
    i+=1
    #1 4 9 16 25 36 49 64 81 100
#string.digits + string.ascii_lowercase
print(len(s), s, i)
temp = ""
for j in range(1,i+1):
    print(i, j)
    temp = temp + s[i*(j-1):i*j] + '\n'
#pad with spaces to avoid code to trip around i-th row that is empty in list
s = temp + ' ' * (i*i - len(temp))
print(s)
result = ""
s = s.split()
print(s)
for row in s:
    for j in row:
        
