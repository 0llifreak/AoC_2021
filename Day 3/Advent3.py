#Advent3
#Author:Lara
with open('input3.txt') as f:
  report = [str(i) for i in f]
counter0=0
counter1= 0
bitgamma=""
bitepsilon=""
num=report[1] #to get length
for j in range(len(num)-1):
    for k in range(len(report)):
        digit=report[k][j]
        if digit == "0":
            counter0=counter0+1
        else:
            counter1=counter1+1

    if counter0 > counter1:
        bitgamma=bitgamma+"0"
        bitepsilon= bitepsilon+"1"
    else:
        bitgamma=bitgamma+"1"
        bitepsilon=bitepsilon+"0"
    counter0=0
    counter1=0
gamma=int(bitgamma,2)
epsilon=int(bitepsilon,2)
power= gamma*epsilon
print(power)
