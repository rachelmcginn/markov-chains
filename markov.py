"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.


    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    words = text_string.split()
  
    dict_of_words = {}
    word_value = []

 
    for indx in range(len(words) - 2):
       
        word_key = tuple([words[indx], words[indx + 1]])
    
        if word_key in dict_of_words:
            dict_of_words[word_key].append(words[indx + 2])  
        else:
            dict_of_words[word_key] = [words[indx + 2]]


        print("{key} {list} \n".format(key=word_key, list=dict_of_words[word_key]))

    chains = dict_of_words
    return chains


def make_text(chains):
    """Return text from chains."""



    # put links in words list 
    words = []

    for key, value in chains.items():
        #add key to words
        #add random word from value to the list as well



    new_dict = {}

    #new_dict[words[indx + 1]]

    

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
