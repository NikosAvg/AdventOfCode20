import re
#Read text and split on empty lines
data = open('input.txt').read().split('\n\n')

def ValidatePassport(passport):
	#Replace new lines with space
	passport = passport.replace('\n',' ')
	#Split on individual fields
	passport = passport.split(' ')
	#Create a dictionary with its field and its value
	Pass = dict(x.split(':') for x in passport)
	#Remove cid field if exists
	Pass.pop("cid", None)
	#Check if valid
	if(len(Pass)==7):
		return 1
	else:
		return 0

count=0
for d in data:
	count+=ValidatePassport(d)

print('Answer 1: ',count)

def ValidatePassport2(passport):
	#Replace new lines with space
	passport = passport.replace('\n',' ')
	#Split on individual fields
	passport = passport.split(' ')
	#Create a dictionary with its field and its value
	Pass = dict(x.split(':') for x in passport)
	#Remove cid field if exists
	Pass.pop("cid", None)
	#Check if valid
	valid_count=0
	if len(Pass)<7:
		valid_count=0
	else:
		#Check Birth year
		if int(Pass['byr']) >= 1920 and int(Pass['byr']) <= 2002:
			valid_count+=1
			#print('Passed check 1')

		#Check Issue Year
		if int(Pass['iyr']) >= 2010 and int(Pass['iyr']) <= 2020:
			valid_count+=1
			#print('Passed check 2')
		#Check expiration year
		if int(Pass['eyr']) >= 2020  and int(Pass['eyr']) <= 2030:
			valid_count+=1
			#print('Passed check 3')
		#Split number and letters
		r = re.compile("([0-9]+)([a-zA-Z]+)")
		if r.match(Pass['hgt']) != None:
			h = r.match(Pass['hgt']).groups()
			#Check height
			if (h[1]=='cm' and int(h[0])>=150 and int(h[0])<=193) or (h[1]=='in' and int(h[0])>=59 and int(h[0])<=76):
				valid_count+=1
				#print('Passed check 4')

		#Check hair color
		if (Pass['hcl'].find('#')!= -1) and len(Pass['hcl'].split("#")[1])==6:
			valid_count+=1
			#print('Passed check 5')

		#Check eyecolor
		accepted_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
		if Pass['ecl'] in accepted_eye_colors:
			valid_count+=1
			#print('Passed check 6')


		#Check pid
		if(len(Pass['pid'])==9):
			valid_count+=1
			#print('Passed check 7')
	return valid_count

count2=0
for d in data:
	if ValidatePassport2(d)==7:
		count2+=1

print('Answer 2: ',count2)
