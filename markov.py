from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # making a variable called contents and setting it equal to opening the file, 
    # reading over the file and making it all into one big string
    contents = open(file_path).read()
    return contents
    
# print (open_and_read_file("green-eggs.txt"))


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}

    """
    # Creating an empty dictionary
    chains = {}

    # Splitting the long string from our file on the whitespace
    words = text_string.split()
    
    # Iterating through the words for the whole string, except the last two words
    for i in range(len(words)-2):
        # Creating a bigram variable that is a tuple of a word and the following word
        bigram = (words[i], words[i+1])
        # If the tuples are in the dictionary, append the third word to the values list
        if bigram in chains:
            chains[bigram].append(words[i+2])

        # If the tuples are not in the dictionary, add the tuple as a key, and the third
        # word to the values list
        else:
            chains[bigram] = [words[i+2]]
        
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # text = [random.choice(chains.values()) for key, value in chains.items()]

    # for key, value in chains.items():
    #     return random.choice(key), value

    text = ""
    # get the keys from the dict and randomize
    rndom_bigram = choice(chains.keys())

    while len(text) < 140:
        # get the values from the corresponding value lists and randomize 
        rndom_value = choice(chains[rndom_bigram])
        
        text = text + " " + rndom_bigram[0] + " " + rndom_bigram[1] + " " + rndom_value

        #Make a new key out of the second word in the first key and the random 
        #word you pulled out from the list of words that followed it.
        new_key_dict = {}
        # new_key = (rndom_bigram[1], rndom_value)

        for i in text:
            new_key_dict[i] = new_key_dict.get(rndom_bigram[1], rndom_value)


    return text




input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
# print chains

# Produce random text
random_text = make_text(chains)

print random_text