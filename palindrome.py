word="refer"
#check the word character by character (need two indices)
#if the first and last character are same, move to next indices in both left and right
#if the first and last character are differ, print not palindrome and break
#check until it reach the middle value(i.e., r>=l)
l=0
r=len(word)-1

while r>=l:
    if word[l]!=word[r]:
        print("The given word",word,"is not a Palindrome")
        break
    l=l+1
    r=r-1
else:
    print("The given word",word,"is a Palindrome")



