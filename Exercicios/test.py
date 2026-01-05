base = 5

num2 = base
calc = 1  # fatorial sempre começa com 1

while num2 > 1:
    anterior = calc
    calc *= num2  # calc = calc * num2

    print(f'{anterior} x {num2} = {calc}')


    num2 -= 1
