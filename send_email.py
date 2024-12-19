import smtplib, ssl, os


def send_email(user_input):
    host = "smtp.gmail.com"
    port = 465

    username = "ssk98.automations@gmail.com"
    password = os.getenv("PortfolioEmailsAppPassword")

    receiver = "ssk98.automations@gmail.com"

    context = ssl.create_default_context()

    message = user_input

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

