word="geeksforgeeks"
sub="for"
if(sub in word):
    for i in range(len(word)):
        if(sub[0]==word[i]):
            print(f"yes substring is present and index number is {i}")
else:
    print("sub string is npot present in it -1")