import emails 
# Compose the email you want to send...
message = emails.html(
    html = "<h1>This is an email</h1><strong>We love sending emails</strong>",
    subject = "Hey, look in here!",
    mail_from = "",
)

# Now you can send the email!
r = message.send(
    to = "", 
    smtp = {
        "host": "", 
        "port": 587, 
        "timeout": 5,
        "user": "",
        "password": "",
        "tls": True,
    },
)

# See if the email was successfully sent
print( r.status_code == 250 )