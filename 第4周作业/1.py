def convert(dna_str):
	rna_str=[]
	for letter in dna_str:
		if letter not in ['A', 'T', 'C', 'G']:
			return "Invalid DNA sequence"
		if letter == 'A':
			rna_str.append('U')
		elif letter == 'T':
			rna_str.append('A')
		elif letter == 'C':
			rna_str.append('G')
		else:
			rna_str.append('C')
	return ''.join(rna_str)
