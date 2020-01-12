n = int(input())

for i in range(n):
    line = input()
    if 'R' == line[0] and line[1].isdigit() and 'C' in line:
        x,y = line.replace('R','').replace('C','').split()
        y = int(y)

        prefix = ''
        while y > 0:
            if y%26:
                prefix += chr(ord('A') + y%26 - 1)
                y //= 26
            else:
                prefix += 'Z'
                y = y//26 -1
        print(''.join(list(reversed(prefix)))) + x

    else:
        for i,c in enumerate(line):
            if c.isdigit():
                prefix = line[:i]
                break

        num = 0

        for j,c in enumerate(prefix):
            num += (ord(c) - ord('A') + 1)*26**(len(prefix)-1-j)
        print('R'+line[i:] + 'C' + str(num))
