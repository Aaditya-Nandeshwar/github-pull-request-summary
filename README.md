# GitHub Pull Request Summary

This script retrieves a summary of all opened, closed, and draft pull requests in the last week for a any given public repository using the GitHub API. It then sends a summary email to a configurable email address. The script is written in Python.

---

## Prerequisites

- Python 3.x
- `requests` library (install using `pip3 install requests`)
- `smtplib` library (install using `pip3 install secure-smtplib`)
- `maskpass` library (install using `pip3 install maskpass`)

---

## Reference links

   * [Use the REST API to interact with pull requests](https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#get-a-pull-request)
   
   * [Sending email using Python and Gmail](https://www.interviewqs.com/blog/py-email)

---

## Setup

1. Clone the repository:

   ```shell
   git clone https://github.com/Aaditya-Nandeshwar/github-pull-request-summary.git

2. Install the required libraries:

   ```shell
   pip3 install requests secure-smtplib maskpass

3. Replace the placeholder values in the script:

   * `repo_name`: Replace with the name of the target public GitHub repository(Example: `kubernetes/ingress-nginx`).
   * `receiver_email_address_list`: Replace with the email address to receive the summary. 
   * `smtp_server`: Replace with the SMTP server address for sending emails. 
   * `smtp_port`: Replace with the SMTP server port. 
   * `sender_email`: Replace with the sender's email address. 
   * `sender_password`: Replace with the sender's email password or an app-specific password.
   
---

## Usage

   Run the script by executing the following command:

   ```shell
   python3 pull_request_summary.py
   
   #Enter user input
   Enter public repo name: prometheus-community/helm-charts
   Enter the list of emails separated by comma: aaditya.nandeshwar@cldcvr.com, adityanandeshwar46@gmail.com
   Enter the sender email address: aadityanandeshwar93@gmail.com
   Enter Password: ****************

   ```
   The script will retrieve all opened, closed, and draft pull requests from the specified GitHub repository in the last week. It will then generate an email summarizing the pull requests and send it to the configured email address.

---

## License

   This project is licensed under the [Apache License 2.0](https://github.com/kubernetes/ingress-nginx/blob/main/LICENSE).