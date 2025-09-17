#Simple Survey for CMPSC 497: DevOps Course


#Asks the user to enter their name, year, and major
print("Please enter your name: ")
name = str(input())

print("\nPlease enter your year: ")
year = str(input())

print("\nPlease enter your major: ")
major = str(input())

print(f"\nHello {name}, Welcome to the CMPSC 497 Course Feedback!")
print("Please answer honestly. \n")



#Ask for rating from 1 to 5
while True:
    try:
        rating = float(input("\nOn a scale of 1-5, how do you like the course so far: "))
        if rating < 1.0 or rating > 5.0:
            print("\nPlease enter a number between 1 and 5.")
        else:
            break
    except ValueError:
        print("\nThat's not a valid number. Please try again.")

#Simple Feedback
if rating == 4.5:
    print("\nWow! Keep up with the best work!")
elif rating >= 3.0:
    print("\nThat's okay. Keep exploring and do the best you can with the command line tools you have.")
else:
    print("\nHmm, that's alright. Just remember that this course is an elective and do your best with your studies!")

#Optional Open-Ended Feedback
feedback = str(input("Want to tell us why you gave that rating? "))
print("\nThanks for your feedback! Your opinion matters to Dr. Vinayak Elangovan and Professor Joe Oakes to help improve this course for future semesters.")