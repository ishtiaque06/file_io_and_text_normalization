from FST import *
import os
#os.path.isfile(minidictionary.txt)
class FST_Lexicon:
	def __init__(self, dictionary):
		input_dictionary = dictionary
		self.input_alphabet = []
		self.output_alphabet = []
		self.set_of_states = []
		self.initial_state = None
		self.output_states = []
		self.FST_function_with_states = {}
		input_file = open(input_dictionary, "r+")
		self.build_parameters(input_file)
		'''print set(self.set_of_states)
		print set(self.input_alphabet)
		print set(self.output_alphabet)
		print set(self.output_states)
		print self.FST_function_with_states'''

	def build_parameters(self, input_file):
		for line in input_file:
			self.build_input_alphabet(line)
			self.build_output_alphabet(line)
			self.build_word_to_phones_FST_function(line)
	def build_input_alphabet(self, line):
		word = line.split()[0]
		index = 0
		while index < len(word):
			if word[index] not in self.input_alphabet:
				self.input_alphabet += word[index]
			index += 1
		return self.input_alphabet
	def build_output_alphabet(self, line):
		phonetic_word = line.split()[1:]
		index = 0
		while index < len(phonetic_word):
			if phonetic_word[index] not in self.output_alphabet:
				self.output_alphabet.append(phonetic_word[index])
			index += 1
		return self.output_alphabet

	def build_word_to_phones_FST_function(self, line):
		word = line.split()[0]
		phones = line.split()[1:]
		index = 0
		self.initial_state = 0
		self.set_of_states.append(self.initial_state)
		if len(word) > len(phones):
			difference = len(word) - len(phones)
			index_for_word = 0
			while index_for_word < difference:
				phones.append('')
				index_for_word += 1
		while index < len(word):
			'''if (index, word[index]) in self.FST_function_with_states.keys():
				self.FST_function_with_states[(index), (word[index])] = (index + 1), (phones[index])
				self.set_of_states.append(index)
				self.set_of_states.append(index + 2)
				self.output_states.append(index)
				self.output_states.append(index + 2)
			else:'''
			self.FST_function_with_states[(index), (word[index])] = ((index + 1), (phones[index]))
			self.set_of_states.append(index)
			self.set_of_states.append(index + 1)
			self.output_states.append(index)
			self.output_states.append(index + 1)
			index += 1
		return self.FST_function_with_states

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
