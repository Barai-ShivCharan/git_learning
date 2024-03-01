a1="elbow"
a2="below"
if len(a1)==len(a2):

    a1_sorted=sorted(a1)
    a2_sorted=sorted(a2)
    if a1_sorted==a2_sorted:
        print("THe string is an Anagram")
    else:
        print("the String is not a Anagram")
else:
    print("The atring is not anagram")
