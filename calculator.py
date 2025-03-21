while True:
    c = input('\nChoose: 1-Add, 2-Sub, 3-Mul, 4-Div, 5-Exit: ')
    if c == '5': break
    if c in '1234':
        try:
            a, b = float(input('First: ')), float(input('Second: '))
            ops = {'1': a + b, '2': a - b, '3': a * b, '4': a / b if b != 0 else 'Error'}
            print('Result:', ops[c])
        except: print('Invalid input')
    else: print('Invalid choice')
