def read_file_line_by_line(file_path):
	"""Yield lines from a file one at a time."""
	with open(file_path, "r", encoding="utf-8") as file:
		for line in file:
			yield line.rstrip("\n") # returns the lines in the file one-by-one not all of them at once
			
def splitting_line_of_bit(line):
	# Splitting where there is "0b" text in the bit.
	parts = line.split("0b", 1)
	if len(parts) != 2:
		# If a line has no binary section, keep line as-is and use empty bits.
		return line, ""
	return parts[0], parts[1]

def flipping_bits(line, bits):
	# Build flipped bits as strings
	new_bit = []
	for j in bits:
		if j == "0":
			new_bit.append("1")
		elif j == "1":
			new_bit.append("0")
		else:
			# Preserve any non-bit characters unchanged.
			new_bit.append(j)
    # Then concatenate "a label" with the "newbit" to form one line.
	return f"{line}0b{''.join(new_bit)}" # I used join to convert the list to one long string, straiht-up
	
def composing_output(result):
	# Append each processed line to the output file.
	with open("end_file.txt", "a", encoding="utf8") as file:
		file.write(result + "\n")


def main():
	file_path = "bit.txt"

	# Start a fresh end_file on each run.
	with open("end_file.txt", "w", encoding="utf8"):
		pass

	for line in read_file_line_by_line(file_path):
		# Extract label/text part and binary part, then flip the bits.
		line, bits = splitting_line_of_bit(line)
		flipped_bit = flipping_bits(line, bits)
		composing_output(flipped_bit)
	print("Done")

if __name__ == "__main__":
	main()
