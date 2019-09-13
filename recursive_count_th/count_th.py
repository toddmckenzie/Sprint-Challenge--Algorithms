'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):
   new_word = word.split(' ')
   
   if len(word) < 2:
       return count
   else:
        if word[0:2] == "th":
            count += 1
            return count_th(word[1:], count)
        else:
            return count_th(word[1:], count)


