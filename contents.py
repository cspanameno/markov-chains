words = [ "I", "am", "very", "confused"]
chains = {}
    
for i in range(len(words)-2):
    x = (words[i], words[i+1])

        
for tup in x:
    chains[tup] = chains.get(tup, []).append(tup[i+2])

print chains 


