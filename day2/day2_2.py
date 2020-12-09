with open('input.txt') as f:
    data = f.readlines()

for i in range(len(data)):
	data[i] = data[i].split(' ')

def extract_and_validate(data):
	index1 = int(data[0].split('-')[0])-1
	index2 = int(data[0].split('-')[1])-1
	letter = data[1].split(':')[0]
	pwd = data[2].split('\n')[0]
	if pwd[index1] != letter and pwd[index2] == letter:
		return 1
	elif pwd[index1] == letter and pwd[index2] != letter:
		return 1
	else:
		return 0
	
valid = 0
for i in range(len(data)):
	#valid += extract_and_validate(data[i])
	valid += extract_and_validate(data[i])

print(valid)