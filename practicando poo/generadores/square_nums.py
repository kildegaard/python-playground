def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result


def gen_square_numbers(nums):
    for i in nums:
        yield i * i


lista = [1, 2, 3, 4, 5]

my_nums = square_numbers(lista)
print(my_nums)


def rango(start, stop):
    while start < stop:
        yield start
        start += 1


rangoo = rango(0, 10)

for i in rangoo:
    print(i)
