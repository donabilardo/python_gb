""" 5. Напишите программу, которая принимает на вход координаты двух точек
и находит расстояние между ними в 2D пространстве.   """

#from unittest import result


pointA = float(input("Координа точки А >>> "))
pointB = float(input("Координа точки B >>> "))


def dist (pointA, pointB):

    if pointA > pointB:
        result = pointA - pointB
    elif pointB > pointA:
        result = pointB - pointA
    elif pointA == pointB:
        result = 0
    return result

print(dist(pointA, pointB))