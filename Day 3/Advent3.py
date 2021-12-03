with open('input3.txt') as f:
  report = [str(i) for i in f]
with open('input3.txt') as f:  
  report_oxygen = [str(i) for i in f]
with open('input3.txt') as f:  
  report_co2 = [str(i) for i in f]

def get_gamma(report):
    counter0=0
    counter1=0
    bitgamma=""
    num=report[0] #to get length
    for j in range(len(num)-1):
        for k in range(len(report)):
            digit=report[k][j]
            if digit == "0":
                counter0=counter0+1
            else:
                counter1=counter1+1
        if counter0 > counter1:
            bitgamma=bitgamma+"0"
        elif counter0 == counter1:
            bitgamma=bitgamma+"1"
        else:
            bitgamma=bitgamma+"1"
        counter0=0
        counter1=0
    return bitgamma

def get_epsilon(report):
    counter0=0
    counter1=0
    bitepsilon=""
    num=report[0] #to get length
    for j in range(len(num)-1):
        for k in range(len(report)):
            digit=report[k][j]
            if digit == "0":
                counter0=counter0+1
            else:
                counter1=counter1+1
        if counter0 > counter1:
            bitepsilon=bitepsilon+"1"
        elif counter0 == counter1:
            bitepsilon=bitepsilon+"0"
        else:
            bitepsilon=bitepsilon+"0"
        counter0=0
        counter1=0
    return bitepsilon

#Part1
bitgamma=get_gamma(report)
bitepsilon=get_epsilon(report)
gamma=int(bitgamma,2)
epsilon=int(bitepsilon,2)
power= gamma*epsilon
print("power",power)
print("bitgamma",bitgamma)
print("bitepsilon",bitepsilon)

#Part 2

for i in range(len(report_oxygen)):
    x=get_gamma(report_oxygen)
    m=0   
    for j in range(len(report_oxygen)):

        if len(report_oxygen)==1:
            break
        elif x[i]==report_oxygen[m][i]:
            m=m+1
        else: 
            report_oxygen.pop(m)

for i in range(len(report_co2)):
    x=get_epsilon(report_co2)
    m=0   
    for j in range(len(report_co2)):
        if len(report_co2)==1:
            break
        elif x[i]==report_co2[m][i]:
            m=m+1
        else: 
            report_co2.pop(m)
report_co2=str(report_co2[0])
report_oxygen=str(report_oxygen[0])
oxygen=int(report_oxygen,2)#convert
co2=int(report_co2,2)
life_support=oxygen*co2
print("life_supprot",life_support)

