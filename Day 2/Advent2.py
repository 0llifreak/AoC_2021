#Advent2
#Author:Lara
with open('input.txt') as f:
  report = [int(i) for i in f]
counter= 0
for i in range(len(report)-3):
    j=i+1
    k=i+2
    l=i+3
    sum1= report[j] + report[i] + report[k]
    sum2= report[j] + report[k] + report[l] 
    if sum2 > sum1:
        counter=counter+1
print(counter)
