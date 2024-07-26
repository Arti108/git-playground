def word_lengths(phrase):
    # Split the phrase into words
    words = phrase.split()
    
    # Use map to apply len() to each word and get the lengths
    lengths = list(map(len, words))
    
    return lengths

# Example usage:
phrase = 'How long are the words in this phrase'
lengths = word_lengths(phrase)
print(lengths)