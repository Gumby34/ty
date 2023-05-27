arr = [8, -3, 0, -5, 6, -7, 2, 4, -9, 1]
sum_arr = sum(arr)
count = 0

for num in arr:
    if num < sum_arr:
        count += 1

print("Сумма равна", sum_arr)
print("Меньше этой суммы в массиве", count, "элемента(ов)")