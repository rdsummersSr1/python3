print(word_)
    acronym =''
    for word in word_:
        if word.find('-') != -1:
           acronym += word[0].upper()
           print(acronym)
        elif word.find('_') != -1:
           for word2 in word:
               acronym += word2[0].upper()
        else: 
            word3 = word2.strip('_')
            print(word3)
    print (acronym)
    return acronym