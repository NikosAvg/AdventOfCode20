data=[]
with open('input.txt','r') as f:
	for line in f.readlines():
		data.append(line.strip())

# 0,0 -> 1,3 -> 2,6

#print(data)

#slope 3,1
def tree_count(dx,dy):
	count=0
	x=0

	for y in range(dy,len(data),dy):
		row = data[y]
		x = ( x + dx ) % len(row)
		#print(f"{x}x{y}: {row[x]}")
		if row[x]=="#":
			count+=1
		y+=dy
	return count


print(tree_count(1,1),tree_count(3,1),tree_count(5,1),tree_count(7,1),tree_count(1,2))
print("Result = ",tree_count(1,1)*tree_count(3,1)*tree_count(5,1)*tree_count(7,1)*tree_count(1,2))

#slope 1,1
#slope 3,1
#slope 5,1
#slope 7,1
#slope 1,2