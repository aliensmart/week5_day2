#write a function that takes in two strings as inputs returning wether or not the strings are permutations of one another

def permute_test(str1, str2):
    if str1==str2:
        return True
    elif len(str1) !=len(str2):
        return False

    
def permute_test2(str1, str2):
    return sorted(str1)==sorted(str2)

    
def letter_count(str):
    letters = {}
    for i in str:
        if i in letters:
            letters[i] +=1
        else:
            letters[i]=1

        return letters
