# Дано натуральное число N. Выведите слово YES, если число N
# является точной степенью двойки, или слово NO в противном
# случае. Операцией возведения в степень пользоваться нельзя!
def exponent(n):
    if n == 1:
        return 'yes'
    elif n < 1:
        return 'no'
    return exponent(n/2)
print(exponent(8))