#Advent 2
#Author: Lara
with open('input2.txt') as f:
  report = [str(i) for i in f]
#Part 1
position_x=0
position_y=0
for i in range(len(report)):
  number=""
  for c in report[i]:
    if c.isdigit():
      number=number + c
      num=int(number)
  if report[i][0]=="f":
    position_x=position_x+num
  elif report[i][0]=="d":
    position_y=position_y+num
  elif report[i][0]=="u":
    position_y=position_y-num
position=position_x*position_y
print("position 1:", position)

#Part 2
aim=0
position_x=0
position_y=0
for i in range(len(report)):
  number=""
  for c in report[i]:
    if c.isdigit():
      number=number + c
      num=int(number)
  if report[i][0]=="f":
    position_x=position_x+num
    position_y=position_y+(aim*num)
  elif report[i][0]=="d":
    aim=aim+num
  elif report[i][0]=="u":
    aim=aim-num
position=position_x*position_y
print("position 2:", position)
