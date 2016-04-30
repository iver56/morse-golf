import string as s
a=s.ascii_uppercase
print ''.join([{'.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split()[i]:a[i]for i in range(26)}[x] for x in raw_input().split()])