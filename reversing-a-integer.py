def reverse_integer(num):
    reversed_num = 0
    sign = 1 if num >= 0 else -1
    num = abs(num)
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return reversed_num * sign
number = 12345
number_1=reverse_integer(number)
print(number_1)
print(f"{number_1:,}")



