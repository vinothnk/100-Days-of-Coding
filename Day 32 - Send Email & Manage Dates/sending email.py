import smtplib

my_email = 'vinoth.nanda.kumaran.sg@gmail.com'
# vinoth.nanda.kumaran.sg -> identity of email account
# @gmail.com -> identity of email provider
password = 'logitechmx3200'

my_email2 = 'wooo_hoooo07@hotmail.com'
password2 = 'Mx3200Logitech'

# with smtplib.SMTP('smtp.gmail.com') as connection:
#     # smtp servers
#     # gmail -> smtp.gmail.com
#     # hotmail -> smtp.live.com
#     # yahoo -> smtp.mail.yahoo.com
#
#     connection.starttls()
#     # tls -> transport layer security -> to secure the connection between me and the server. encrypted
#
#     connection.login(user= my_email, password= password)
#
#     connection.sendmail(from_addr=my_email,
#                         to_addrs='wooo_hoooo07@hotmail.com',
#                         msg='Subject: testing out\n\nThis is the body of the email.')
#     # to send email from the email address to another email address
#     # put subject as beginning of msg to prevent email going to spam.
#     # use \n\n to indicate body of email

with smtplib.SMTP('smtp-mail.outlook.com') as connection:
    # smtp servers
    # gmail -> smtp.gmail.com
    # hotmail -> smtp.live.com
    # yahoo -> smtp.mail.yahoo.com

    connection.starttls()
    # tls -> transport layer security -> to secure the connection between me and the server. encrypted

    connection.login(user= my_email2, password= password2)

    connection.sendmail(from_addr=my_email2,
                        to_addrs= my_email,
                        msg='Subject: testing out\n\nThis is the body of the email.')
    # to send email from the email address to another email address
    # put subject as beginning of msg to prevent email going to spam.
    # use \n\n to indicate body of email
