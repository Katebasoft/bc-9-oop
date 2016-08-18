def find_missing(list_one, list_two):
	status = False
	if len(list_two) > len(list_one):
		status = True
	missing = ''
	if status == True:
		for index in range(list_two):
			if list_one.count(list_two[index]) == 0:
				missing = list_two[index]
	else:
		for index in range(list_one):
			if list_two.count(list_one[index]) == 0:
				missing = list_one[index]
	return missing

