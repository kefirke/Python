L = '2 15 45 34 51 4 8 3 65 1 78 9'
array = list(map(int, L.split()))
print(array)

n = int(input('Введите целое число: '))
try:
    if max(array) < n or n < min(array):
        raise ValueError("ОШИБКА. Неверное значение:")
except ValueError as error:
    print('Число не удовлетворяет условиям задачи', error)
if n in array:
    print('Число есть в списке')
else:
    array.append(n)

print(array)

def sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array

print('Отсортированный список:', sort(array))


def binary_search(array, n, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == n:
        return middle
    elif n < array[middle]:
        return binary_search(array, n, left, middle - 1)
    else:
        return binary_search(array, n, middle + 1, right)

index = binary_search(sort(array), n, 0, len(array))

print('Номер позиции элемента, который меньше введенного пользователем числа:', index-1)