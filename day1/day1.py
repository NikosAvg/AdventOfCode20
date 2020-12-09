with open('input.txt') as f:
    data = f.readlines()

data = [int(x.strip()) for x in data]

for i in range(len(data)):
    for j in range(len(data)):
        if(data[i] + data[j]==2020):
            res1 = data[i]*data[j]
        for k in range(len(data)):
            if(data[i] + data[j] + data[k] == 2020):
                res2 = data[i]*data[j]*data[k]

print(res1,res2)
