import string as s
a=s.ascii_uppercase
m='.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split()
i=raw_input().split()
print ''.join([{m[i]:a[i]for i in range(26)}[x] for x in i])