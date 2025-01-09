""" 2. Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user. """

sub1=int(input("Enter 1st subject:"))
sub2=int(input("Enter 2nd subject:"))
sub3=int(input("Enter 3rd subject:"))
total=sub1+sub2+sub3
if(total>120 and sub1>33 and sub2>33 and sub3>33):
    print("Pass")
else:
    print("You are dumb")

