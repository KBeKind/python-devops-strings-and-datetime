

# strftime()   strptime()  DATE AND TIME FORMATTING
# THE FORMATTING CODES ARE:
# %a  - abbreviated weekday name
# %A  - full weekday name
# %b  - abbreviated month name
# %B  - full month name
# %c  - date and time
# %d  - day of the month as a decimal number
# %H  - hour as a decimal number (24-hour clock)
# %I  - hour as a decimal number (12-hour clock)
# %j  - day of the year as a decimal number
# %m  - month as a decimal number
# %M  - minute as a decimal number
# %p  - either AM or PM
# %S  - second as a decimal number
# %U  - week number of the year (Sunday as the first day of the week)
# %w  - weekday as a decimal number (Monday is 0)
# %W  - week number of the year (Monday as the first day of the week)
# %x  - date


# strptime() RETURNS A DATETIME OBJECT CORRESPONDING TO date_string PARSED ACCORDING TO FORMAT
# dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")

# GETTING CURRENT DATE AND TIME
# x = datetime.datetime.now()

#strftime() RETURNS A STRING REPRESENTING THE TIME, CRONTROLLED BY AN EXPLICIT FORMAT STRING
# dtstring = now.strftime("%d/%m/%y %H:%M")



# STRINGS SLICING
# x = "Hello World"

#MIDDLE SLICE (DOESNT INCLUDE THE 5)
# print (x[2:5])

#END SLICE
# print (x[2:])

#FRONT SLICE (DOESNT INCLUDE THE 5)
# print (x[:5])



#MODIFYING STRINGS
# x = "Hello World"

# TO UPPERCASE (DOESNT MODIFY THE ORIGINAL STRING)
# x = x.upper()

# TO LOWERCASE (DOESNT MODIFY THE ORIGINAL STRING)
# x = x.lower()

# REMOVES ANY WHITESPACE FROM THE BEGINNING AND END OF THE STRING (DOESNT MODIFY THE ORIGINAL STRING)
# x = "   Hello World "
# x = x.strip()


# REPLACING SUBSTRINGS (DOESNT MODIFY THE ORIGINAL STRING)
# x = "Hello World"
# x = x.replace("World", "Universe")


# FORMAT METHOD
# x = "Hello World"
# y = "John"
# z = "Doe"
# my_greeting = "Hello {0} {1} {2}".format(x, y, z)
# OR
# my_greeting = "Hello {} {} {}".format(x, y, z)

# FORMAT SPECIFICATION 
# : SEPARATES THE FORMAT SPECIFICATION FROM THE REST OF THE REPLACEMENT FIELD
# <fill> SPECIFIES HOW TO PAD VALUES THAT DONT OCCUPY THE ENTIRE FIELD WIDTH
# <align> SPECIFIES HOW TO ALIGN VALUES IN A FIELD
# <sign> SPECIFIES IF A VALUE IS POSITIVE OR NEGATIVE
# <width> SPECIFIES THE MINIMUM WIDTH OF THE FIELD
# # SELECTS AN ALTERNATE OUTPUT FORM FOR CERTAIN PRESENTATION TYPES
# 0 CAUSES VALUES TO BE PADDED ON THE LEFT WITH ZEROES INSTEAD OF SPACE
# <group> SPECIFIES A GROUPING CHARACTER FOR NUMERIC OUTPUT
# <prec> SPECIFIES THE NUMBER OF DECIMAL PLACES TO PRESENT NUMERIC OUTPUT AND MAXIMUM OUTPUT WIDTH FOR STRINGS
# <type> SPECIFIES THE TYPE OF PRESENTATION TO USE FOR A VALUE
# TYPE SPECIFICATIONS:
    # s - String
    # d - Decimal
    # f - Floating point
    # b - Binary
    # o - Octal
    # x - Hexadecimal
    # e - Exponential
    # c - Character
    # g - Floating point or Exponential
    # % - Percentage


import datetime

# Write a program that reads in a number and prints the date that number of days from now in this format: Saturday, February 06, 2021.

# current_date = datetime.date.today()
# days_to_add = int(input())
# future_date = current_date + datetime.timedelta(days=days_to_add)
# print(future_date.strftime("%A, %B %d, %Y"))


# Write a program that reads in numbers until a -1 is entered and prints the sum of all numbers
# entered in decimal format with two digits after the decimal.
# For example, if the user enters 5000 10 15 -1 the program should display 5025.00 
# (Each number will be separated by a carriage return).

# current_input = int(input())
# sum = 0

# while current_input != -1:
#     sum += current_input
#     current_input = int(input())

# print(f"{sum:.2f}")


