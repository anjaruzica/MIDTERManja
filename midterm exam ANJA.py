# Programming for Economists II - Midterm Exam
# Anja Ruzica Cacic Milutinovic


# Question 1
print(25 % 7 * 3 - 4)
# 25 % 7 = 4, then 4 * 3 = 12, then 12 - 4 = 8
# 8

# Question 2

# Answered on BB

# LIST: Mutable
my_list = [1, 3, 5, 7, 9]
print("Original list:", my_list)
my_list[1] = 11
print("Modified list:", my_list)
# Works fine

# STRING: Immutable
my_string = "Cat"
print("Original string:", my_string)
# my_string[0] = "R"   <-- this would give TypeError
# Instead we build a new string using slicing:
my_string2 = "R" + my_string[1:]
print("New string:", my_string2)
# "Cat" stays the same, we just made a new one "Rat"

# Question 3

def is_valid_url(url):
    """Checks if a URL is valid. Returns True or False."""

    # A valid URL starts with http:// or https://
    if url.startswith("https://"):
        after_protocol = url[8:]
    elif url.startswith("http://"):
        after_protocol = url[7:]
    else:
        return False

    # There must be something after the protocol
    if len(after_protocol) == 0:
        return False

    # URLs dont have spaces
    if " " in after_protocol:
        return False

    # Must have a dot for the domain (.com, .org, etc.)
    dot_pos = after_protocol.find(".")
    if dot_pos == -1:
        return False

    # Something must exist before and after the dot
    if dot_pos == 0 or dot_pos == len(after_protocol) - 1:
        return False

    return True

test_urls = ["https://google.com", "http://bbc.co.uk", "hello world",
             "http://", "https://.com", "http://yahoo", "ftp://file.com",
             "https://ie.edu/programs"]

for url in test_urls:
    print(url, "-->", is_valid_url(url))

# Question 4

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

options = [
    "4257304920394478392772938744930294037524",
    "7798338247658278460338648728567428338977",
    "2704702208931031198668911301398022074072",
    "0974101607733149676776769413377061014790"
]

for opt in options:
    result = palindrome(opt)
    print(opt[:20] + "...", "-->", result)
#the second one is NOT a palindrome


# Question 5

def longest_c_word(filename):
    """Takes a filename, finds the longest word starting with c."""
    fp = open(filename, "r")
    longest = ""

    for line in fp:
        # split each line into words
        words = line.split()
        for word in words:
            # lowercase and remove punctuation
            clean_word = word.lower().strip(".,;:!?\"'()")
            if clean_word.startswith("c"):
                if len(clean_word) > len(longest):
                    longest = clean_word

    fp.close()
    return longest


print("Function defined - needs a text file to run")


# Question 6

import datetime
a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()     # Friday = 4
month_of_year = today.month       # February = 2
a = a + day_of_week               # 7 + 4 = 11
b += month_of_year                # 2 + 2 = 4

print(a)                          # 11
print(b)                          # 4
c = a + b
print(c)                          # 15
d = "xyz" * (c // 3)             # "xyz" * 5
print(d)                          # xyzxyzxyzxyzxyz

# Friday Feb 27 2026: weekday()=4, month=2
# a=11, b=4, c=15, 15//3=5, "xyz"*5 = xyzxyzxyzxyzxyz


# Question 7

a = 10
a = a + 2         # a = 12
print(a * 2)      # prints 24, a is still 12
a = 19            # a = 19
print(a + 3)      # prints 22, a is still 19
a = a // 2        # 19 // 2 = 9 (integer division)
print("Final value of a:", a)
#9


# Question 9


import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

print("Original list:", random_numbers)

for i in range(len(random_numbers)):

    # numbers greater than 80 become negative
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]

    # numbers lower than 40 get replaced by the sum of their digits
    elif random_numbers[i] < 40:
        num_str = str(random_numbers[i])
        digit_sum = 0
        for ch in num_str:
            digit_sum = digit_sum + int(ch)
        random_numbers[i] = digit_sum

    # numbers between 40 and 80 stay the same

print("Modified list:", random_numbers)

# Question 10
def days_since_birthday(birthday):
    """Calculates total days in whole years between birth year and current year."""

    # parse the birthday string using slicing (format DD-MM-YYYY)
    day = int(birthday[0:2])
    month = int(birthday[3:5])
    birth_year = int(birthday[6:10])

    # current year hardcoded since we can't import anything
    current_year = 2026

    # we only count whole years: from (birth_year + 1) to (current_year - 1)
    total_days = 0

    for year in range(birth_year + 1, current_year):
        # check if the year is a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            total_days = total_days + 366
        else:
            total_days = total_days + 365

    return total_days


# Testing with my birthday
my_birthday = "26-05-2006"
result = days_since_birthday(my_birthday)
print("Days passed (whole years only):", result)
# Counts years 2007 through 2025 (19 years)
# Leap years in that range: 2008, 2012, 2016, 2020, 2024 (5 leap years)
# 5 * 366 + 14 * 365 = 1830 + 5110 = 6940 days
