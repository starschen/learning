m=int(raw_input('Enter an integer: '))
for pwr in range(1,6):
    for root in range(abs(m)+1):
        if root**pwr>abs(m):
            break
        elif root**pwr == abs(m):
            print root, pwr
