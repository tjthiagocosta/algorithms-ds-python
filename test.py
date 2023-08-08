def anagrams(string_set): 
    d= {}
    
    # group words according to the signature
    for word in string_set:
        s = ''.join(sorted(word)) # calculate the signature 
        if s in d:
            d[s].append(word) # append a word to an existing signature 
        else:
            d[s] = [word] # add a new signature and its first word 
            
    # -- extract anagrams, ingoring anagram groups of size 1
    return [d[s] for s in d if len(d[s]) > 1]

set_quote = set("below the car is a rat drinking cider and bending its elbow while this thing is an arc that can act like a cat which cried during the night caused by pain in its bowel".split(' '))
print(set_quote)
words = anagrams(set_quote)
print(words)