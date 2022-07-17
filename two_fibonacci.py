def get_fib(position):
    if position < 2:
        return position
    else:
        return get_fib(position-2) + get_fib(position-1)

fibo = []
number = 0
position = 2

while number < 4000000:
    number = get_fib(position)
    fibo.append(number)
    position += 1

fibo.pop()
print(sum([number for number in fibo if number%2==0]))
