# If word starts with a vowel, add 'ay' to the end
# If word does not start with volwel, push first letter to end then add 'ay'


def pig_latin(word):
    
    first_letter = word[0]
    
    # Check if vowel
    if first_letter in 'aeiou' :
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word
    

        
    
        
    