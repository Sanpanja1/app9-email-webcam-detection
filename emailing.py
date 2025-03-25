import email
import smtplib
import filetype
from email.message import EmailMessage

PASSWORD = "lkjryorqtvlyjnun"
SENDER = "panjasanjit640@gmail.com"
RECEIVER = "panjasanjit640@gmail.com"
def send_email(image_path):
    print("send email function has started")
    email_message = EmailMessage()
    email_message["subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just showed a new customer!")

    with open(image_path,"rb") as file:
        content = file.read()
        kind = filetype.guess(content)
        if kind is None:
            print('Cannot guess file type!')
        else:
            email_message.add_attachment(content, maintype="image", subtype=kind.mime.split('/')[1])

        gmail = smtplib.SMTP("smtp.gmail.com",587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(SENDER, PASSWORD)
        gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
        gmail.quit()
        print("send email function has ended")

    if __name__ == "__main__":
        send_email(image_path="image/209.jpeg")
