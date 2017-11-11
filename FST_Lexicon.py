from FST import *
import os
#os.path.isfile(minidictionary.txt)
class FST_Lexicon:
	def __init__(self, dictionary):
		input_dictionary = dictionary
		input_file = open(input_dictionary, "r+")
		for line in input_file:
			print line
		input_file.close()

	#def build_parameters():

FST_Lexicon("minidictionary.txt")