# Python class for finite-state transducer (FST)
# Jane Chandlee
# Fall 2017
# i_alpha: set of input alphabet symbols
# o_alpha: set of output alphabet symbols
# states: set of states
# start: initial state
# finals: set of final states
# transitions: dictionary of transitions; keys are (state, input) pairs and values are (state, output) pairs

class FST:
   def __init__(self, i_alpha, o_alpha, states, start, finals, transitions):
      self.Sigma = i_alpha
      self.Gamma = o_alpha
      self.Q = states
      self.I = start
      self.F = finals
      self.delta = transitions
      
      
   # helper function that returns the transition for state q and input symbol i. If no such transition exists, returns (None, None)      
   def get_trans(self,q,i):           
      return self.delta.get((q,i), (None, None))

   # takes an input string s and returns the corresponding output string, or None if the FST isn't defined for s
   def get_output_string(self, s):
      output = ''
      state = self.I
      for c in s:
         state, next_output = self.get_trans(state,c)
         if state:
            output += next_output
         else:
            return None
      return output

def demo():
   T = FST(set(['a', 'c', 'b', 'e', 'd', 'g', 'i', 'k', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'v', 'y', 'z']),\
    set(['IY', 'JH', 'EH', 'AA', 'B', 'AE', 'D', 'G', 'K', 'M', 'L', 'N', 'P', 'S', 'R', 'EY', 'T', 'W', 'V', 'AY', 'AX', 'Z', 'IH', 'UW', 'OW']),\
     set([0, 1, 2, 3, 4, 5, 6, 7]), 0, set([0, 1, 2, 3, 4, 5, 6, 7]), {(4, 'g'): (5, 'JH'), (1, 'm'): (2, 'M'), (0, 'r'): (1, 'R'), (0, 'l'): (1, 'L'), (0, 's'): (1, 'S'), (2, 'a'): (3, 'AE'), (1, 'i'): (2, 'AY'), (2, 'n'): (3, 'N'), (3, 'e'): (4, ''), (3, 'n'): (4, 'N'), (2, 's'): (3, 'Z'), (3, 'a'): (4, 'AE'), (0, 'o'): (1, 'OW'), (4, 'z'): (5, 'Z'), (5, 'r'): (6, 'R'), (0, 'b'): (1, 'B'), (3, 'k'): (4, 'K'), (1, 'u'): (2, 'UW'), (3, 'y'): (4, 'IY'), (4, 'r'): (5, 'R'), (1, 'q'): (2, 'K'), (4, 'e'): (5, 'EH'), (1, 'o'): (2, 'OW'), (0, 'p'): (1, 'P'), (2, 'l'): (3, 'L'), (2, 'd'): (3, 'D'), (5, 'e'): (6, ''), (0, 'a'): (1, 'AE'), (0, 'g'): (1, 'G'), (1, 'l'): (2, 'L'), (3, 'l'): (4, 'L'), (2, 'u'): (3, 'UW'), (1, 'e'): (2, 'EH'), (1, 'r'): (2, 'R'), (2, 'b'): (3, 'B'), (5, 't'): (6, 'T'), (3, 'v'): (4, 'V'), (4, 'c'): (5, 'K'), (2, 'o'): (3, 'OW'), (0, 'v'): (1, 'V'), (3, 'd'): (4, 'D')})
   print 'Input: blue Output:',T.get_output_string('blue')
   print 'Input: aqua Output:',T.get_output_string('aqua')
   print 'Input: amber Output:',T.get_output_string('amber')
   print 'Input: bronze Output:',T.get_output_string('bronze')
   print 'Input: gold Output:',T.get_output_string('gold')
   print 'Input: gray Output:',T.get_output_string('gray')
   print 'Input: lilac Output:',T.get_output_string('lilac')
   print 'Input: orange Output:',T.get_output_string('orange')
   print 'Input: pink Output:',T.get_output_string('pink')
   print 'Input: red Output:',T.get_output_string('red')
   print 'Input: rose Output:',T.get_output_string('rose')
   print 'Input: ruby Output:',T.get_output_string('ruby')
   print 'Input: silver Output:',T.get_output_string('silver')
   print 'Input: violet Output:',T.get_output_string('violet')

if __name__=='__main__':
   demo()


