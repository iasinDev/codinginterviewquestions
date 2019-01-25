from collections import Counter
import copy
def findLongestWordsInDictornary(word, dictionary):
    letter_dict = Counter(word)
    maxLength = 0
    result = []
    for word_of_dictionary in dictionary:
        letter_dict_current = copy.deepcopy(letter_dict)
        ok = True
        for c in word_of_dictionary:
            if letter_dict_current[c]>0:
                letter_dict_current[c]-=1
            else:
                ok = False
                break
        if ok:
            if len(word_of_dictionary) > maxLength:
                result=[]
                maxLength = len(word_of_dictionary)
            if len(word_of_dictionary) == maxLength:
                result.append(word_of_dictionary)
    return result

print(findLongestWordsInDictornary("oet", ["to", "toe", "toes"]) == ["toe"])
            

