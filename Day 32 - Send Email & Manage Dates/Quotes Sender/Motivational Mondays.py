import datetime as dt
import smtplib
import random
# TODO 1: check for the current day
now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 2:

    # TODO 2: read txt file and store the items in a list to retrieve later
    with open('quotes.txt') as file:
        data = file.readlines()
        data_len = len(data)
        random_no = random.randint(0, data_len)
        random_quote = data[random_no]
    # TODO 3: prep the code to send an email with 1 of the quote in the list if it matches the current day
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

        connection.sendmail(from_addr=my_email,
                            to_addrs='clement_dena@yahoo.com',
                            msg=f'Subject: Motivational Wednesday\n\n'
                                f'{random_quote}.')
        # to send email from the email address to another email address
        # put subject as beginning of msg to prevent email going to spam.
        # use \n\n to indicate body of email