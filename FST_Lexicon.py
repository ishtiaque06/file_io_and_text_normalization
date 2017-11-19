from FST import * #This imports the FST Class to build an FST lexicon.

class FST_Lexicon: #This class takes in a file with words and their corresponding sounds and builds a lexicon mapping based on that.
	def __init__(self, dictionary): #The init function declares variables to be used as parameters to build an FST object.
		input_dictionary = dictionary #This variable stores the name of the file input into the program.

		#The following variables are declared to be parameters of the FST Class.
		self.input_alphabet = []
		self.output_alphabet = []
		self.set_of_states = []
		self.initial_state = None
		self.output_states = []
		self.FST_function_with_states = {}

		#This creates a file object with the file input into the program.
		input_file = open(input_dictionary, "r+")
		#This method builds all the parameters to be input into the FST Class.
		self.build_parameters(input_file)

	#The build parameters method calls upon other methods which build each parameter for the FST.
	def build_parameters(self, input_file):
		#The following block loops through the whole file line by line and calls methods to build parameters while it's in each line. 
		for line in input_file:
			self.build_input_alphabet(line)
			self.build_output_alphabet(line)
			self.build_word_to_phones_FST_function(line)

	#This builds the set of input alphabets, which is a set of every letter present in the file. 
	def build_input_alphabet(self, line):
		word = line.split()[0] #This line takes the first word in the line to build the input alphabet from it.
		index = 0 #This counter iterates through the word. 
		while index < len(word):
			if word[index] not in self.input_alphabet: #This makes sure letters aren't repeated, although in retrospect this isn't quite necessary if 
														#the set function is called upon the whole string. Will fix later given time. 
				self.input_alphabet += word[index]
			index += 1
		return self.input_alphabet

	#This builds the output alphabet, which is a collect of phonemes in each line. 
	def build_output_alphabet(self, line):
		phonetic_word = line.split()[1:]
		index = 0
		while index < len(phonetic_word):
			if phonetic_word[index] not in self.output_alphabet:
				self.output_alphabet.append(phonetic_word[index])
			index += 1
		return self.output_alphabet

	#This method makes the actual FST transition function, and while it's at it, it also builds the set of output states. 
	def build_word_to_phones_FST_function(self, line):
		word = line.split()[0]
		phones = line.split()[1:]
		index = 0
		self.initial_state = 0
		self.set_of_states.append(self.initial_state)
		#The following if block takes into account if there are less phonemes for a particular word than the number of letters in that word. 
		if len(word) > len(phones):
			difference = len(word) - len(phones)
			index_for_word = 0
			while index_for_word < difference:
				phones.append('')
				index_for_word += 1

		#This while block builds the dictionary that represents the transition function, and also builds input and output state sets. 
		while index < len(word):
			self.FST_function_with_states[(index), (word[index])] = ((index + 1), (phones[index]))
			self.set_of_states.append(index)
			self.set_of_states.append(index + 1)
			self.output_states.append(index)
			self.output_states.append(index + 1)
			index += 1
		return self.FST_function_with_states

#Simple UI to let user input a word that is present in the dictionary and get the corresponding sequence of phonemes for that word. 
def ui():
        print "Using minidictionary.txt file to build the dictionary of phones... \n"
        dictionary_of_phones = FST_Lexicon("minidictionary.txt")
        sample_FST = FST(set(dictionary_of_phones.input_alphabet), set(dictionary_of_phones.output_alphabet),\
					 set(dictionary_of_phones.set_of_states), dictionary_of_phones.initial_state,\
					 set(dictionary_of_phones.output_states), dictionary_of_phones.FST_function_with_states)
        cont = 'y'
        while cont == 'y':
                word = raw_input("Enter the word you want to convert to phonemes: ")
                print word + '\t' + sample_FST.get_output_string(word)
                cont = raw_input("Would you like to test another word? (y/n)" )
ui()
