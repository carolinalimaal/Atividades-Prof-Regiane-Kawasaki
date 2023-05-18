a = 35000000
b = 48000000
i = 0
while a <= b:
    a += 0.03*a
    b += 0.02*b
    i += 1
print(f'Para a população do país A ultrapassar a do país B serão necessários {i} anos.')