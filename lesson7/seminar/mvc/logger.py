from datetime import datetime as dt
from time import time


def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('lesson7\seminar\mvc\log.cvs', 'a') as file:
        file.write('{}; temperature; {} \n'.format(time, data))


def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('lesson7\seminar\mvc\log.cvs', 'a') as file:
        file.write('{}; ressure_; {}'.format(time, data))


def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('lesson7\seminar\mvc\log.cvs', 'a') as file:
        file.write('{}; wind_speed; {}'.format(time, data))