import math

print('Введите координаты для точки A:')
xA = int(input())
yA = int(input())
print('Введите координаты для точки B:')
xB = int(input())
yB = int(input())

answer = math.sqrt((xB-xA)*(xB-xA)+(yB-yA)*(yB-yA))
print(answer)