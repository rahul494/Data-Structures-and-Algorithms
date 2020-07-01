def isValidSubsequence(array, sequence):
    arr_idx = 0
	seq_idx = 0
	
	while arr_idx < len(array) and seq_idx < len(sequence):
		if array[arr_idx] == sequence[seq_idx]:
			arr_idx += 1
			seq_idx += 1
		else: 
			arr_idx += 1
			
	return seq_idx == len(sequence)
