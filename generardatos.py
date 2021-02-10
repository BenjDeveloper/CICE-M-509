
from random import randint
# 8

for i in range(0,10):
    # print (i)
    dia=randint(1,28)
    mes=randint(1,12)
    año=randint(1970,2002)
    dia=randint(1,28)
    print (str(dia)+"/"+str(mes)+"/"+str(año))

print()
# Resto	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22
letra=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
# for i in range(0,23):
#     print(letra[i])

for i in range(0,10):
    dninum=randint(100000000000,999999999999)
    index=dninum%23
    dniletr=letra[index]
    dni=str(dninum)+dniletr
    print(dni)

print()
for i in range(0,10):
    num=randint(97,122)
    letter1=chr(num)
    num=randint(97,122)
    letter2=chr(num)
    num=randint(97,122)
    letter3=chr(num)
    num=randint(97,122)
    letter4=chr(num)
    num=randint(97,122)
    letter5=chr(num)
    # print(letter1+letter2+letter3+letter4+letter5+"@asdf.com")
    print(letter1+letter2+letter3+letter4+letter5)


# for j in range(97,122):
#     letter=chr(j)
#     print(letter)

print()

for i in range(0,10):
    salario=randint(800,2200)
    print(salario)