from FST import *
import os
#os.path.isfile(minidictionary.txt)
class FST_Lexicon:
	def __init__(self, dictionary):
		input_dictionary = dictionary
		self.input_alphabet = []
		self.output_alphabet = []
		self.phonetic_dictionary = []
		self.FST_function_with_states = {}
		input_file = open(input_dictionary, "r+")
		self.build_parameters(input_file)
		self.input_states = []
		self.output_states = []
		input_states_index = 0
		while input_states_index < len(self.FST_function_with_states):
			self.input_states.append(input_states_index)
			input_states_index += 1
		print self.input_states
		output_states_index = 1
		while output_states_index <= len(self.FST_function_with_states):
			self.output_states.append(output_states_index)
			output_states_index  += 1
		print self.output_states
		self.set_of_states = list(set(self.input_states + self.output_states))
		print self.set_of_states
		sample_FST = FST('blue', self.input_alphabet, self.output_alphabet, self.set_of_states, self.input_states, self.output_states, self.FST_function_with_states)
		sample_FST.transition()

	def build_parameters(self, input_file):
		for line in input_file:
			self.build_input_alphabet(line)
			self.build_output_alphabet(line)
			self.build_phonetic_dictionary(line)
		print self.phonetic_dictionary
		self.build_FST_Lexicon_transition_function(self.phonetic_dictionary)

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
	def build_phonetic_dictionary(self, line):
		word = line.split()[0]
		phones = line.split()[1:]
		if len(word) > len(phones):
			difference = len(word) - len(phones)
			index = 0
			while index < difference:
				phones.append('')
				index += 1
		index = 0
		while index < len(word):
			self.phonetic_dictionary.append((word[index], phones[index]))
			index += 1
		self.phonetic_dictionary = list(set(self.phonetic_dictionary))
		return self.phonetic_dictionary
	def build_FST_Lexicon_transition_function(self, dictionary_as_a_list_of_tuples):
		index = 0
		while index < len(dictionary_as_a_list_of_tuples):
			#if dictionary_as_a_list_of_tuples[index][0] not in 'aeiouc':
			self.FST_function_with_states[(index, dictionary_as_a_list_of_tuples[index][0])] = (dictionary_as_a_list_of_tuples[index][1], index+1)
			#else:
			'''for key in self.FST_function_with_states:
				if dictionary_as_a_list_of_tuples[index][0] in key:
					self.FST_function_with_states[(key[0] + 1), key[1]] = (dictionary_as_a_list_of_tuples[index][1], (key[0] + 2))'''
			index += 1
		return self.FST_function_with_states


FST_Lexicon("minidictionary.txt")

