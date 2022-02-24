def add_prefix_un(word):
    """
    :param word: str of a root word
    :return:  str of root word with un prefix


    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """


    return 'un'+word




def make_word_groups(vocab_words):
    """


    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.


    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    [<prefix>, <word_1>, <word_2> .... <word_n>]
    '<prefix> :: <prefix><word_1> :: <prefix><word_2> :: <prefix><word_n>'
    """ 
    r_vocab_words = ''
    ' '.join(vocab_words)
    for word in vocab_words:
        if word == vocab_words[0]:
           r_vocab_words = word
        else:
           r_vocab_words += (' :: ' + vocab_words[0] + word)
    
    return r_vocab_words
           
    
















def remove_suffix_ness(word):
    """


    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.


    This function takes in a word and returns the base word with `ness` removed.
    """


    print(word)
    if word[-5] == 'i':
        return word[:-5] + 'y'
    else:
        print(word[:-5])
        return word[:-4]
        
    
    




def adjective_to_verb(sentence, index):
    """
    adjective_to_verb('I need to make that bright.', -1 )
     'brighten'    
    
    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.


    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    new_sentence = ‘’
    sentence_without_period = sentence[:-1]
    print(sentence[:index])
    new_sentence = sentence_without_period.split()
    print (new_sentence[index]+'en')
    return new_sentence[index]+'en'
