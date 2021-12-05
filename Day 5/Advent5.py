#Advent5
#Author Lara
import re
from collections import Counter



with open('input5.txt') as f:
    report = f.read()

lines = re.findall('(\d+),(\d+) -> (\d+),(\d+)', report)

highestnumber=0
for i in range(len(lines)):
    for j in range(3):
        if int(lines[i][j])>highestnumber:
            highestnumber=int(lines[i][j])

rows, cols = (highestnumber+1, highestnumber+1)
diagramm=[[0 for i in range(cols)]for j in range(rows)]

for line in range(len(lines)):
    x1=int(lines[line][0])
    y1=int(lines[line][1])
    x2=int(lines[line][2])
    y2=int(lines[line][3])
    #print(x1, x2, y1, y2)
    if x1==x2: #horizontal
        num=y2-y1
        if num < 0:
            num=abs(num)
            for i in range(num+1):
                diagramm[y1-i][x1]=int(diagramm[y1-i][x1])+1
                #print(y1-i, x1, diagramm[y1-i][x1])  
        else:    
            for i in range(num+1):
                diagramm[y1+i][x1]=int(diagramm[y1+i][x1])+1
                #print(y1+i, x1, diagramm[y1+i][x1])
    elif y1==y2:#vertical
        num=x2-x1
        #print("y", num)
        if num<0:
            num=abs(num)
            for i in range(num+1):
                diagramm[y1][x1-i]=int(diagramm[y1][x1-i])+1
                #print(y1, x1-i, diagramm[y1][x1-i])
        else:
            for i in range(num+1):
                diagramm[y1][x1+i]=int(diagramm[y1][x1+i])+1 
                #print(y1, x1+i, diagramm[y1][x1+i])   
    else:#diagonal (für part 1 weglassen)
        num_y=y2-y1
        num_x=x2-x1
        if num_x < 0 and num_y<0:#nach links oben
            num_y=abs(num_y)
            for i in range(num_y+1):
                diagramm[y1-i][x1-i]=int(diagramm[y1-i][x1-i])+1
                #print(y1-i, x1-i, diagramm[y1-i][x1-i])  
        elif num_x>0 and num_y>0: #nach nach rechts unten
            for i in range(num_y+1):
                diagramm[y1+i][x1+i]=int(diagramm[y1+i][x1+i])+1
                #print(y1+i, x1+i, diagramm[y1+i][x1+i])
        elif num_x>0 and num_y<0: #nach recht oben
            num_y=abs(num_y)
            for i in range(num_y+1):
                diagramm[y1-i][x1+i]=int(diagramm[y1-i][x1+i])+1
                #print(y1-i, x1+i, diagramm[y1-i][x1+i])
        else:    #nach links unten
            for i in range(num_y+1):
                diagramm[y1+i][x1-i]=int(diagramm[y1+i][x1-i])+1
                #print(y1+i, x1-i, diagramm[y1+i][x1-i])
        

print(diagramm) 
sum=0          
for i in range(highestnumber+1):
    for j in range(highestnumber+1):
        if int(diagramm[i][j])>1:
            sum=sum+1
print(sum)
    
    
    