import smtplib
import requests
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import maskpass


def get_pull_requests(repo_name):
    """Get all pull request form the given repo"""
    url = f"https://api.github.com/repos/{repo_name}/pulls"
    params = {
        "state": "all",
        "sort": "created",
        "direction": "desc",
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def filter_pull_requests(pull_requests):
    """Filtered the pull requests created within one week"""
    # Get the date of one week ago
    one_week_ago = datetime.now() - timedelta(days=7)
    # Filter pull requests created in the last week
    filtered_pull_requests = []
    for pr in pull_requests:
        created_date = datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        if created_date > one_week_ago:
            filtered_pull_requests.append(pr)
    return filtered_pull_requests


def generate_email_content(pull_requests):
    """Generate email content form the filtered pull request"""
    email_content = ""
    for pr in pull_requests:
        pr_title = pr["title"]
        pr_state = pr["state"]
        pr_url = pr["html_url"]
        pr_draft = pr["draft"]
        email_content += f"Title: {pr_title}\n"
        email_content += f"State: {pr_state}\n"
        email_content += f"URL: {pr_url}\n"
        email_content += f"Draft: {pr_draft}\n\n"
    return email_content


def send_summary_email(email_address_list, email_content, smtp_server, smtp_port, sender_email, sender_password, repo_name):
    """Send the summary email to users"""
    for user_email in email_address_list:
        BODY_HTML = """<html>
        <head></head>
        <body>
          <h1>GitHub Alerts!!!</h1>
          <p>Dear User,</p>
          <p>Please find the summary of all opened, closed, and in draft pull requests in the last week for a given 
          <b>{repo_name}</b> repository:\n\n</p>
        </body> </html>""".format(repo_name=repo_name)

        msg = MIMEMultipart('mixed')
        part1 = MIMEText(f"{BODY_HTML}", 'html')
        msg.attach(part1)
        part2 = MIMEText(email_content)
        msg.attach(part2)
        msg['Subject'] = "GitHub Pull Request Summary"
        msg['From'] = sender_email
        msg['To'] = user_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            server.close()


def main():
    """Main function is used to get the input form the user & call other functions"""

    # GitHub repository information
    repo_name = input("Enter public repo name: ")

    # Email configuration
    receiver_email_address_list = input("Enter the list of emails separated by comma: ").split(",")
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = input("Enter the sender email address: ")
    sender_password = maskpass.askpass(prompt="Enter Password: ", mask="*")

    try:
        pull_requests = get_pull_requests(repo_name)
        filtered_pull_requests = filter_pull_requests(pull_requests)
        email_content = generate_email_content(filtered_pull_requests)
        send_summary_email(receiver_email_address_list, email_content, smtp_server, smtp_port, sender_email, sender_password, repo_name)
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
