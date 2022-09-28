# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# количество знаков полсле запятой ограничено 4-мя. версия работы с числом.

# 4.(ЕСЛИ НЕ ЗНАЕТЕ КАК ДЕЛАТЬ, МОЖНО НЕ ВЫПОЛНЯТЬ) Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

    # 5 Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
    # 10
    # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]


    N = int(input('Enter number for create list [0,N] >> '))
    numbers = []
    for i in range(N):
        numbers.append(i)
    print(f'-> {numbers}')
    randomIndex=0
    for i in range(N):
        randomIndex=random.randrange(N)
        tempNumber=numbers[i]
        numbers[i]=numbers[randomIndex]
        numbers[randomIndex]=tempNumber
    print(f'-> {numbers}')
    # positionOne = int(input('Enter positionOne numbers list >> '))
    # positionTwo = int(input('Enter positionTwo numbers list >> '))
    # if positionOne<len(numbers) and positionOne>0 and positionTwo < len(numbers) and positionTwo>0:
    #     print(numbers[positionOne-1]*numbers[positionTwo-1])
    # else:
    #     print('No correct entering position list!')
    #     # if i!=0:

        #     numbers.append(i)
        #     numbers.append(-i)
        # else:
        #     numbers.append(i)
        #numbers.append(random.randint(-N, N + 1))



    #3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
    insertNum=int(input('Enter number list >> '))
    numList=[]

    for i in range(1, insertNum + 1):
        numList.append(round((1 + 1 / i) ** i))
    print(f'n={insertNum}:{numList} -> {sum(numList)}')
        #num_list.append(3 * i + 1)

    #print(num_list)

    print(round((1 + 1 / 4) ** 4))
    print(round((1 + 1 / 5) ** 5))
    print(round((1+1/6)**6))

print('Task 1 seminar 2')
inputString = input('Введите число, количество обрабатываемых знаков после запятой не более 4х ')
inputDigit=float(inputString)
intPast = int(inputDigit)
floatPast = round(inputDigit%1,4)

print(intPast,floatPast)

def findSumDigit(chekDidit):
    sumDigit = 0
    while chekDidit != 0:
        if chekDidit < 10:
            sumDigit += chekDidit
        else:
            sumDigit += chekDidit % 10
        chekDidit = chekDidit // 10
    return sumDigit



#2 Обработка целой части числа
sumDigit=0
sumDigit+=findSumDigit(intPast)
# while intPast!=0:
#      if intPast < 10:
#             sumDigit+= intPast
#      else:
#         sumDigit+=intPast%10
#      intPast=intPast//10

print(sumDigit)
#3 Обработка дробной части числа
floatPast = int(floatPast*10000)
print(floatPast)
sumDigit+=findSumDigit(floatPast)
print(sumDigit)

n=45.4568
m=45.45
print(f'{n-int(n)}')
print(f'{n%1.0}')
print(f'{float(round(m%1,4))}');
print(f'{round(m%1,2)}');


lst = [1.1, 1.2, 3.1, 5, 10.01]

new_lst = [round(i%1.0,2) for i in lst if i%1!=0]
#Нужно удалить из списка нулевые значения

print(max(new_lst))
print(min(new_lst,key=lambda x:float(x)))
print(min(new_lst))
#print(new_lst[4])
print(new_lst, '=>', max(new_lst) - min(new_lst)) #- Вариант проще


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
##old_list = ['1', '2', '3', '4', '5', '6', '7']
# old_list='123.45'
# new_list = []
# for item in old_list:
#    if item != ',' and item != '.':
#        new_list.append(int(item))

# print (new_list)

##[1, 2, 3, 4, 5, 6, 7]
# old_list = ['1', '2', '3', '4', '5', '6', '7']
# new_list = list(map(int, old_list))
# print (new_list)

# [1, 2, 3, 4, 5, 6, 7]