def judge_dna(to_be_judged):
	for char in to_be_judged:
		if char not in ['A', 'T', 'C', 'G','U']:
			return 'None'
	if 'U' in to_be_judged and 'T' in to_be_judged:
		return 'None'
	if 'U' in to_be_judged:
		return 'RNA'
	else:
		return 'DNA'
print(judge_dna('AUCGT'))