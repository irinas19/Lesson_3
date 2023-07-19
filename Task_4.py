# Палиндром
# Дано слово, состоящее только из строчных латинских букв. Проверьте, является ли это
# слово палиндромом. Выведите YES или NO.
# При решении этой задачи нельзя пользоваться циклами, в решениях на питоне нельзя
# использовать срезы с шагом, отличным от 1.

def palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return palindrome(word[1:-1])
    return False
if palindrome("mnbnm") == True:
    print("YES")
else:
    print("NO")