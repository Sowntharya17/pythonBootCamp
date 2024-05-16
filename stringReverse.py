word="year"
#to reverse a string,last character should be printed first.
#create an empty variable to store the character one by one.
#while condition to stop the loop.

new_word=''
i=len(word)-1

while i>=0:
    new_word = new_word + word[i]
    i=i-1
word=new_word
print(word)
