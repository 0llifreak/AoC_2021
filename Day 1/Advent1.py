#Advent1
#Author:Lara
#Part 1:
with open('input.txt') as f:
  report = [int(i) for i in f]
counter1= 0
for i in range(len(report)-1):
    j=i+1
    if report[j] > report[i]:
        counter1= counter1+1
print(counter1)

#Part 2:
counter2= 0
for m in range(len(report)-3):
    j=m+1
    k=m+2
    l=m+3
    sum1= report[j] + report[m] + report[k]
    sum2= report[j] + report[k] + report[l] 
    if sum2 > sum1:
        counter2=counter2+1
print(counter2)
