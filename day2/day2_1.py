with open('input.txt') as f:
    data = f.readlines()

for i in range(len(data)):
	data[i] = data[i].split(' ')
#Split each data point at the space
#Extract numbers letter and password 

def extract_and_validate(data):
	count=0
	for i in data[2].split('\n')[0]:
		if i==data[1].split(':')[0]:
			count+=1
	if count>=int(data[0].split('-')[0]) and count<=int(data[0].split('-')[1]):
		return 1
	else:
		return 0
	#print(int(data[0].split('-')[0]),int(data[0].split('-')[1]),data[1].split(':')[0],data[2].split('\n')[0])
valid = 0
for i in range(len(data)):
	valid += extract_and_validate(data[i])

print(valid)