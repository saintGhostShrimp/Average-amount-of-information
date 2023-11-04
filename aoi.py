import math

def calculate_avg_information(probabilities):
    avg_info = 0
    for probability in probabilities:
        try:
            avg_info += probability * math.log2(probability)
        except ValueError:
            avg_info += 0
    avg_info = -avg_info
    return avg_info

def table_pxy (x,y):
    pxy = []
    print ("|x1", end="")
    for i in y:
        pxy.append(x * i)
        print ("|", x * i, end="")
    print("|")
    return pxy
    
print ('| |y1|y2|y3|y4|y5|y6|')
print ('|-|-|-|-|-|-|-|')
p = [0.125, 0.25, 0.25, 0.375]
pyx1 = [0.5, 0.25, 0.0625, 0.0625, 0.0625, 0.0625]
pyx2 = [0.25, 0.0625, 0.25, 0.0625, 0.125, 0.25]
pyx3 = [0.125, 0.5, 0.125, 0.0, 0.125, 0.125]
pyx4 = [0.0, 0.25, 0.25, 0.125, 0.25, 0.125]

pxy1 = table_pxy (p[0],pyx1)
pxy2 = table_pxy (p[1],pyx2)
pxy3 = table_pxy (p[2],pyx3)
pxy4 = table_pxy (p[3],pyx4)

average_information1 = calculate_avg_information(pxy1)
average_information2 = calculate_avg_information(pxy2)
average_information3 = calculate_avg_information(pxy3)
average_information4 = calculate_avg_information(pxy4)
average_information = average_information1 + average_information2 +average_information3 + average_information4 

print(f"Average-amount-of-information: {average_information} bit")
