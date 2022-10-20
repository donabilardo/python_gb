""" 4. Напишите программу, которая по заданному номеру четверти,
 показывает диапазон возможных координат точек в этой четверти (x и y). """


number = int(input())
first, second, third, fourth = 0, 0, 0, 0

for _ in range(number):
    x, y = map(int, input().split())
    first += x > 0 and y > 0
    second += x < 0 and y > 0
    third += x < 0 and y < 0
    fourth += x > 0 and y < 0

print(f"Первая четверть: {first}")
print(f"Вторая четверть: {second}")
print(f"Третья четверть: {third}")
print(f"Четвертая четверть: {fourth}")