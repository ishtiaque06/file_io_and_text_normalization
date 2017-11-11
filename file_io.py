#This function takes in a sample text file as input and returns how many characters it has, how many lines it has, and how many words each line has. 
def lines_in_a_file():
	input_file = open('test.txt', 'r')#Opens the input file to read.
	output_file = open('Ishtiaque.txt', 'r+') #Opens the output file to read and write on.

	#This section outputs the number of characters present in the input file to the output file. The number of characters include \n characters. 
	length = str(len(input_file.read()))#This makes use of the read method which returns a string. The length takes in the resulting length in the string 
										#and stores it as string type for output.
	output_file.write("This file has " + length + " characters.\n") #This writes the length of the input file to the output file.
	input_file.seek(0) #This enables the whole file to be read again from the start.

	#This part finds out how many lines the file has.
	count = 0 #This variable tracks the number of lines in the file. 
	for line in input_file: #This block loops through the file line by line and increases the count for the number of lines.
		count += 1 
	count_as_a_string = str(count) #This converts the integer type of count to string type. 
	output_file.write("This file has " + count_as_a_string + " lines.\n") #This writes the new count of lines in the output file. 
	input_file.seek(0) #This enables the whole file to be read again from the start.

	#This part reads the file line by line and outputs the number of words in each line to the output file.
	temp_string = "initial" #This sets the initial value of the string to non-empty. 
	line_number = 0 #This keeps count of the line number the program is in.
	while temp_string != '': #When the readline() method reaches EOF, it returns the empty string. I'm using this as the loop guard.
		temp_string = input_file.readline() #This stores the current line in a temporary string to count the number of words in the string.
		if temp_string == '': #If EOF is reached, readline() returns empty string so we don't need to count the number of characters in that line. Note:
							#if the line is empty in a text editor, it essentially contains the "\n" character so it's not technically empty.
			break #We know we've reached EOF so we check the EOF condition again for the loop to be able to exit. 
		else: #Then the EOF isn't reached so we do the following. 
			no_of_words = len(temp_string.split()) #This finds out how many word s
			no_of_words_as_string = str(no_of_words)
			line_number_as_string = str(line_number)
			output_file.write("line " + line_number_as_string + " has " + no_of_words_as_string + " words.\n")
			line_number += 1

	input_file.close()#Closes the input file to free up memory.
	output_file.close()#Closesthe output file to free up memory. 
