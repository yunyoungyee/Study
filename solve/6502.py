import sys
input = lambda: sys.stdin.readline().rstrip()
i=1
while True:
    parts = input().split()

    if parts[0] == '0':
        break

    r, w, l = map(int, parts)
    if r*2*r*2 >= w*w+l*l:
        print('Pizza {count} fits on the table.'.format(count=i))
        i+=1
    elif r*2*r*2 < w*w+l*l:
        print('Pizza {count} does not fit on the table.'.format(count=i))
        i+=1