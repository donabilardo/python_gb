
inputData = input("Введите выражение: ")

if '+' in inputData:
    index = inputData.find('+')
    a = float(inputData[:index])
    b = float(inputData[index + 1:])
    result = a + b

if '-' in inputData:
    index = inputData.find('-')
    a = float(inputData[:index])
    b = float(inputData[index + 1:])
    result = a - b

if '*' in inputData:
    index = inputData.find('*')
    a = float(inputData[:index])
    b = float(inputData[index + 1:])
    result = a * b

if '/' in inputData:
    index = inputData.find('/')
    a = float(inputData[:index])
    b = float(inputData[index + 1:])
    result = a / b



print(f'Результат выражения {inputData}={result}')