# smtp (Simple Mail Transfer Protocol) is going to allows us to create a smtp server. Smtp communicates the language is used. 
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# Read the index.html file using the Path class and create a Template object.
html = Template(Path("index.html").read_text())
# We create our Email object
email = EmailMessage()
email["from"] = "<your_name>"
# For multiple email put them in a list.
email["to"] = "<your_recipient's email>"
email["subject"] = "<your_email's_subject>"

# In the content we can text, html, images etc
# We replace the $name in index.html with "Gregory"
email.set_content(html.substitute({"name": "<the_recipient's_name>"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    # The initial message to inform that this is a server
    smtp.ehlo()
    # tls is an ecryption mechanism
    smtp.starttls()
    # Connect to the email account
    smtp.login("<your_gmail>", "<your_gmail_password>")
    smtp.send_message(email)