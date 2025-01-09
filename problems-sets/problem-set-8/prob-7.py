#7. Write a python function to remove a given word from a list ad strip it at the same time

"""def stripped(list1,word):
    n=[]
    for words  in list1:
        stripped_word=words.strip()
        if not(stripped_word==word):
            n.append(stripped_word)
    return n """
def remove_and_strip(word_list, word_to_remove):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each element in the provided list
    for word in word_list:
        # Strip leading and trailing whitespace from the current word
        stripped_word = word.strip()
        
        # If the stripped word is not the word we want to remove, add it to the result list
        if stripped_word != word_to_remove:
            result.append(stripped_word)
    
    return result


word_list=["jayanth","pavan","ajay","hemanth"]
word_to_remove="nth"

print("New list is" ,remove_and_strip(word_list,word_to_remove))