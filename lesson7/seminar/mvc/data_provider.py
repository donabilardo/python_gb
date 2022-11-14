from random import randint

def get_temperature(sensor): #данные от датчика температуры
    return randint(-20,0) if sensor else randint(0,20)

def get_preassure(sensor):#данные от датчика давления
    if sensor:
        return randint(720,750)
    else:
        return randint(750,775)


def get_wind_speed(sensor):#данные от датчика скорости ветра
    if sensor == 1:
        return randint(0,30)
    else:
        return randint(30,50)


