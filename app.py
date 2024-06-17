
import logging
from twilio.rest import Client
import time
import subprocess

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Twilio credentials
account_sid = 'Twilio SID'
auth_token = 'Twilio Secret Key'
client = Client(account_sid, auth_token)

# Phone numbers
to_phone_number = '+'  # Correct format for calling Australian toll-free number
from_phone_number = '+'  # Your Twilio number

def send_email_ps(subject, body):
    """Send an email using PowerShell."""
    cmd = [
        "powershell",
        "-ExecutionPolicy",
        "Bypass",
        "-Command",
        "Send-MailMessage",
        "-To",
        "'yourtoemail@email.com'",
        "-From",
        "'yourfromemail@email.com'",
        "-Subject",
        f"'{subject}'",
        "-Body",
        f"'{body}'",
        "-SmtpServer",
        "'enteryourSMTP'"
    ]
    try:
        subprocess.run(cmd, check=True)
        logging.info("Email sent successfully via PowerShell")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to send email via PowerShell due to: {str(e)}")

def make_call_and_handle_response():
    """Initiate a Twilio call and monitor its status."""
    try:
        call = client.calls.create(
            to=to_phone_number,
            from_=from_phone_number,
            url='your tiwlio handler',
            #status_callback='Heroku APP',
            status_callback_event=['initiated', 'ringing', 'answered', 'completed', 'failed', 'busy', 'no-answer', 'canceled']
        )
        logging.info(f"Call initiated, Call SID: {call.sid}")

        # Polling for call status updates
        while True:
            call_update = client.calls(call.sid).fetch()
            logging.info(f"Current call status: {call_update.status}")
            if call_update.status in ['completed', 'failed', 'busy', 'no-answer', 'canceled']:
                break
            time.sleep(5)

        # Compose email body and subject based on the call status
        email_body = (f"Call completed with status: {call_update.status}\n"
                      f"Number Dialed: {to_phone_number}\n"
                      f"Call SID: {call.sid}")
        email_subject = f"Twilio Call Notification - {call_update.status}"
        logging.info(email_body)
        send_email_ps(email_subject, email_body)

    except Exception as e:
        error_message = (f"Failed to make a call due to: {str(e)}\n"
                         f"Number Dialed: {to_phone_number}\n"
                         f"Call SID: N/A")
        logging.error(error_message)
        send_email_ps("Twilio Call Exception Notification", error_message)

if __name__ == "__main__":
    make_call_and_handle_response()
