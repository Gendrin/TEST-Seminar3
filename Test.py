# coding=windows-1251
def CheckInputInt(testInput):
    try:
        return int(testInput)
    except ValueError:
        print('Incorrect data entry')
        return None

print('������')
# ������� ������ �� ���������� �����. �������� ���������, ������� ����� ����� ��������� ������, ������� �� �������� �������.
print('Seminar3 Task N1')
insertString = input("Enter numbers list separated by spaces -> ")
arrString = insertString.split()
arrIntDigits = []
# check input variable
flagInsertData = True
for numI in arrString:
    if CheckInputInt(numI) == None:
        flagInsertData = False
    else:
        arrIntDigits.append(CheckInputInt(numI))
sumNechetDigitList = 0
if flagInsertData:
    for i in range(len(arrIntDigits)):
        if i % 2 != 0:
            sumNechetDigitList += arrIntDigits[i]
    print(f'{arrIntDigits} -> {sumNechetDigitList}')

# �������� ���������, ������� ����� ������������ ��� ����� ������. ����� ������� ������ � ��������� �������, ������ � ������������� � �.�.
print('Seminar3 Task N2')
