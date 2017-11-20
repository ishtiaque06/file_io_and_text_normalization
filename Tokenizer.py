# tokenizer takes a string and returns a list of the sentences contained in that string.
def tokenizer(text):
	end_punctuation = ['.', '!', '?', ':',';']
	sentence = ''
	sentences = []
	sentences_as_a_list = text.split()
	index = 0

   	#This while block splits the input text by spaces and adds a space after the endof each word
	while index < len(sentences_as_a_list):
   		sentences_as_a_list[index] = sentences_as_a_list[index] + " "
   		index += 1

	#This for block iterates through the list just formed above and is essentially a database of rules
	#to determine whether we're at the end of the sentence.
	for word in sentences_as_a_list:
		if word[-2] in end_punctuation: #The primary check for end of sentence signs.
			if len(word) == 5: #The following block rules out the possibility of an abbrevited month to be the end of a 
								#sentence.
				if word[0:3] in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
					sentence += word
			elif len(word) == 3: #If the word consists of only one letter then it's most likely not the end of a sentence.
				sentence += word
			else: #else we're at the end of the sentence.
				sentence += word
				print sentence
				sentences.append(sentence)
				sentence = ''
		else: #Else we're not at the end of the sentence.
			sentence += word
	return sentences

# print_sentences takes a list of strings and prints them one at a time   
def print_sentences(sentence_list):
   i = 1
   for s in sentence_list:
      print 'Sentence',i,':',s
      i+=1

# Demonstration: rewrite demo() so that it 1) opens the file tokenizertest.txt and reads it into a string, 2) sends that string to tokenizer, 3) sends the result of tokenizer to print_sentences, and 4) closes the file tokenizertest.txt

def demo():
   input_file = open('tokenizertest.txt', 'r')
   string = input_file.read()
   print_sentences(tokenizer(string))
   input_file.close()








if __name__=='__main__':
   demo()
