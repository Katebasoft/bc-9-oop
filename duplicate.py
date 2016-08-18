def dupl(A):
	temp_num = ''
	new_list = []
	for index in range(len(A)):
		if(A[index]!=temp_num):
			new_list.append(A[index])
			temp_num = A[index]
	return new_list

print dupl([5,5,5,6,10,5])
