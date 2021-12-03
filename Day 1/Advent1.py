#Advent1
#Author:Lara
with open('input.txt') as f:
  report = [int(i) for i in f]
counter= 0
for i in range(len(report)-1):
    j=i+1
    if report[j] > report[i]:
        counter= counter+1
print(counter)
