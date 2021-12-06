#Advent6
#Author Lara

text_file = open("input6.txt", "r")
report = text_file.read().split(',')
report= [int(i) for i in report]

def iteration(input, days):
    fishies=[0 for i in range(9)]
    for i in range(len(input)):
        for j in range(8):
            if input[i]==j:
                fishies[j]=fishies[j]+1
         

    for i in range(days):
        add= fishies[0]  
        fishies.pop(0)
        fishies.append(0)
        fishies[6]=fishies[6]+add 
        fishies[8]=fishies[8]+add 
        
    return sum(fishies)

print("part1:", iteration(report, 80))
print("part2: ", iteration(report, 256))    

#Part1
# def lanternfishs(report, days):
#     counter=0
#     for n in range(days):
#         #counter=0
#         for i in (range(len(report))):
#             if report[i]==0:
#                 counter=counter+1
#                 report[i]=6
#             else:
#                 report[i]=report[i]-1
#         while counter>0:
#             report.append(8)
#             counter=counter-1
#         #print(report)
#     return len(report)

# #Part1
# print("part1: ", lanternfishs(report,80))
# #Part2
# #print("part2: ", lanternfishs(report,256))