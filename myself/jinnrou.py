#coding:utf-8
import random, sys

players = int(input('enter the player numbers：') )

#配役用のリスト
role_list_all = ['civil', 'wolf', 'fortune teller']
role_list_cw = ['civil', 'wolf']
role_list_cf = ['civil', 'fortune teller']
role_list_wf = ['wolf', 'fortune teller']
role_list_c = ['civil']
role_list_w = ['wolf']
role_list_f = ['fortune teller']

i = 1
c = 0
w = 0
f = 0

#場合分けで、wolf２人、fortune teller１人、他iscivilになるように指定。
while i <= players:
    if c == players - 3 and w < 2 and f == 0:
        n = random.choice(role_list_wf)
        print(str(i) + ' is ' + n )
    elif c == players -3 and w < 2 and f == 1:
        n = random.choice(role_list_w)
        print(str(i) + ' is ' + n )
    elif c == players -3 and w == 2 and f == 0:
        n = random.choice(role_list_f)
        print(str(i) + ' is ' + n )
    elif w == 2 and f == 1:
        n = random.choice(role_list_c)
        print(str(i) + ' is ' + n )
    elif w < 2 and f == 1:
        n = random.choice(role_list_cw)
        print(str(i) + ' is ' + n )
    else:
        n = random.choice(role_list_all)
        print(str(i) + ' is ' + n )

    if n == 'civil':
        c += 1

    if n == 'wolf':
        w += 1

    if n == 'fortune teller':
        f += 1

    i += 1

 

print('\nall roles is determined')

