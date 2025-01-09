# 7. Write a program to find out whether a given post is talking about “Harry” or not.
"""post="Jayanth is a good boy"
if("jayanth" in post):
    print("yes")
else:
    print("No") # N0"""
post="Harry is a good boy"
if("harry".lower() in post.lower()):
    print("yes")
else:
    print("No") # this way it can be always true no matter the case
    
