import smtplib, ssl, os

def send_email(user_input):
    """Send an email using SMTP with the provided input."""
    host = "smtp.gmail.com"  # SMTP server for Gmail
    port = 465  # Port for SSL

    # Email credentials
    username = "ssk98.automations@gmail.com"
    password = os.getenv("PortfolioEmailsAppPassword")  # Fetch password from environment variables

    receiver = "ssk98.automations@gmail.com"  # Receiver email address

    context = ssl.create_default_context()  # SSL context for secure connection

    message = user_input  # Email content

    # Send the email using SMTP_SSL
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

