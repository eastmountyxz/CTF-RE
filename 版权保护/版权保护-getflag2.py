with open( '题目.txt', 'rb') as f:
    str = f.read()
    print(str)
    length = len(str)
    i = 0
    s = 0
    sum = 0
    while i < length:
        if (int(str[i]) == 226 and int(str[i+1]) == 128 and int(str[i+2]) == 141):
            sum = sum*2
            s = s+1
            if s % 8 == 0:
                print(chr(sum), end='')
                sum = 0
        if (int(str[i]) == 226 and int(str[i+1]) == 128 and int(str[i+2]) == 140):
            sum = sum*2
            sum = sum+1
            s = s+1
            if s % 8 == 0:
                print(chr(sum), end='')
                sum = 0
        i = i+3
