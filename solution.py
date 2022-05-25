def func(I,tc):
    len_i = len(I)
    digit = str(9 - (sum([int(i) for i in I]) % 9))
    if digit == "9":
        digit = '0'
    allowed_indices = range(len_i+1)
    for idx in allowed_indices:
        if idx == 0:
            if digit == "0":
                continue
            if int(digit) >= int(I[idx]):
                continue
            I_new = int(digit + I)
        elif idx == len_i:
            
            I_new = int(I + digit)
        else:
            if int(digit) >= int(I[idx]):
                continue
            I_new = int(I[:idx]+digit+I[idx:])
        if I_new % 9 == 0:
            break
    return f"Case #{tc}: {I_new}"

t = int(input())
tc = 0
while t>0:
    I = input()
    tc += 1
    print(func(I,tc))
    t -= 1
