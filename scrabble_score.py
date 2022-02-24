def score(word):
   letter_keys = [['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], ['D', 'G'], ['B', 'C', 'M', 'P'], ['F', 'H', 'V', 'W', 'Y'],['K'],['J', 'X'],['Q','Z']]
   score = 0 
   values_ = [1,2,3,4,5,8,10]
   letters_value={}
   count = len(letter_keys)
   word_count = len(word)
   keys_ = ''
   i = 0
   for keys_ in letter_keys:
       keys_str = ' '.join(keys_)
       print('2',keys_str)
       i+= 1
       if word_count == 1 and word.upper() in keys_str:
          score = values_[i-1]
          return score
          print('4',keys_str.index(word.upper()))