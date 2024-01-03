import datetime

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

