def test_string_length(strings):
	lengths = []
	if type(strings) == str:
		lengths.append(len(strings))
		return lengths

	for string in strings:
		lengths.append(len(string))
	return lengths