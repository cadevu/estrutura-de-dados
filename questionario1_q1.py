def format_date(date):
    date = date.split()
    temp = date[1].split(":")
    temp.insert(0,date[0])
    temp = [int(i) for i in temp]
    return temp
minutos = 0
horas= 0
d1 = format_date(input())
d2 = format_date(input())
if (d1[0] > d2[0]) :
    print("Data inválida!")
    exit()
result = [int(d2[i]-d1[i]) for i in range(0,4) ]
if result[0] == 0 and (result[1]  < 0):
    print("Data inválida!")
    exit()

if result[1] == 0 and (result[2]  < 0):
    print("Data inválida!")
    exit()
if result[2] == 0 and (result[3]  < 0):
    print("Data inválida!")
    exit()

if result[3] < 0 :
    result[3] = result[3] + 60
    result[2] = result[2] -1
if result[2] < 0:
    result[2] = result[2] + 60
    result[1] = result[1] - 1
if result[1] < 0:
    result[1] = result[1] + 24


if not (result[1]==result[2]==result[3]==0 or  result[0]==0):
    result[0] = result[0]-1

print(f"{result[0]} dia(s)\n{result[1]} hora(s)\n{result[2]} minuto(s)\n{result[3]} segundo(s)")



        
