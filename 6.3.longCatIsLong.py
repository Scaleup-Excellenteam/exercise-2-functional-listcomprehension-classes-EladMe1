def count_words(sentence):
    # This line removes any punctuation marks from the sentence and converts all words to lowercase
    remove_words = [word.strip(',.:;!?').lower() for word in sentence.split() if word.strip(',.:;!?').isalpha()]
    # This line creates a dictionary where each word from the sentence is a key and the value is its length
    to_dict = {the_word: len(the_word) for the_word in remove_words}
    return to_dict
