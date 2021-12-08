#Advent7
#Author: Lara

text_file = open("input7.txt", "r")
report = text_file.read().split(',')
input= [int(i) for i in report]

highestnumber=0
for i in range(len(input)):
    if input[i]>highestnumber:
            highestnumber=int(input[i])
print("highestnumber",highestnumber)

distance_array=[0 for i in range(len(input))]
fuel_needed_1=[0 for j in range(highestnumber)]
fuel_needed_2=[0 for j in range(highestnumber)]
for pos in range(highestnumber):
    #Part1
    for i in range(len(input)):
        distance_array[i]=abs(input[i]-pos)
    fuel_needed_1[pos]=sum(distance_array)
    #Part2
    fuel_total=0
    for i in range(len(distance_array)):
        n=distance_array[i]
        fuel= (n**2+n)/2
        distance_array[i]=fuel
    fuel_needed_2[pos]=sum(distance_array)

lowest_fuel_1=min(fuel_needed_1)
lowest_fuel_2=min(fuel_needed_2)

print("Part 1:", lowest_fuel_1)
print("Part 2:", lowest_fuel_2)


