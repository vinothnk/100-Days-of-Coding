##################### Normal Starting Project ######################
import datetime as dt
import pandas as pd
import smtplib
import random

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

# HINT 2: Use pandas to read the birthdays.csv
data = pd.read_csv('birthdays.csv')
print(data)

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }


#Dictionary comprehension template for pandas DataFrame looks like this:
birthdays_dict = {(data_row['month'],data_row['day']): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if (today_month, today_day) in birthdays_dict:
    placeholder = "[NAME]"
    random_no = random.randint(1,3)
    with open(f'C:/Users/wooo_/PycharmProjects/Day 32 - Send Email & Manage Dates/Birthday Wisher/letter_templates/letter_{random_no}.txt') as file:
        openned_letter = file.read()
        stripped_name = birthdays_dict[(today_month, today_day)]['name'].strip()
        print(stripped_name)
        new_letter = openned_letter.replace(placeholder, stripped_name)
        with open(f'C:/Users/wooo_/PycharmProjects/Day 32 - Send Email & Manage Dates/Birthday Wisher/letter_templates/letter_to_send.txt', mode='w') as completed_letter:
            completed_letter.write(new_letter)
            completed_letter.close()
# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.
my_email = 'vinoth.nanda.kumaran.sg@gmail.com'
# vinoth.nanda.kumaran.sg -> identity of email account
# @gmail.com -> identity of email provider
password = 'logitechmx3200'

my_email2 = 'wooo_hoooo07@hotmail.com'
password2 = 'Mx3200Logitech'

with smtplib.SMTP('smtp.gmail.com') as connection:
    # smtp servers
    # gmail -> smtp.gmail.com
    # hotmail -> smtp.live.com
    # yahoo -> smtp.mail.yahoo.com

    connection.starttls()
    # tls -> transport layer security -> to secure the connection between me and the server. encrypted

    connection.login(user= my_email, password= password)
    with open(f'C:/Users/wooo_/PycharmProjects/Day 32 - Send Email & Manage Dates/Birthday Wisher/letter_templates/letter_to_send.txt', mode='r') as file:
        letter_contents = file.read()
        connection.sendmail(from_addr=my_email,
                        to_addrs='wooo_hoooo07@hotmail.com',
                        msg=f'Subject: Happy Birthday\n\n{letter_contents}')
    # to send email from the email address to another email address
    # put subject as beginning of msg to prevent email going to spam.
    # use \n\n to indicate body of email


