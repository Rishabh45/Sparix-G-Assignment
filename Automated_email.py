import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd


def send_emails():
    try:
        # Read the CSV file
        data = pd.read_csv(r'D:\Virtual_Environment\Assignment\Task\Companies_Clean_Dataset.csv')
        
        # Ensure the email column exists
        if 'Contact Email' not in data.columns:
            print("The CSV file does not contain an 'email' column.")
            return

        # Your email credentials
        sender_email = "rishabh0393@gmail.com"  # Replace with Sender Email email
        sender_password = "Rishabh@1170"        # Set Password for your email.

        # Email server configuration
        smtp_server = "smtp.gmail.com"  # Update for your email provider
        smtp_port = 587  # Port for TLS

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Iterate through each email in the CSV file
        for index, row in data.iterrows():
            recipient_email = row['Contact Email']

            # Create the email message
            subject = " Unlock Cost-Effective Solutions with Our Offshore Services"
            body = "Dear Recipient's Name,\n\nI am Rishabh Kumar from Sparix G, offering offshore staffing solutions to help businesses like yours save costs and boost efficiency.\n Let me know if you'd be open to a quick discussion about how we can support your goals.\n\nBest regards,\nRishabh Kumar\n position name\n Contact_information."

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            try:
                server.sendmail(sender_email, recipient_email, msg.as_string())
                print(f"Email sent to {recipient_email}")
            except Exception as e:
                print(f"Failed to send email to {recipient_email}: {e}")

        # Close the server connection
        server.quit()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_emails()
