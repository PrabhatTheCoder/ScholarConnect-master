from _future_ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

def rejection_email(content):    
    subject = "My Subject"
    html_content = "<html><body><h1>my name is {{name}}</h1></body></html>"
    sender = {"name":"John Doe","email":"example@example.com"}
    to = [{"email":"example@example.com","name":"Jane Doe"}]
    params = {"name":"prabhat","subject":"New Subject"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, bcc=None, cc=None, reply_to=None, headers=None, html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
        
def approval_email(content):    
    subject = "My Subject"
    html_content = "<html><body><h1>Your scholarship has been approved {{name}}</h1></body></html>"
    sender = {"name":" Prabhat ","email":"prabhat.patel9134@gmail.com"}
    to = [{"email":"akankshadangri@gmail.com","name":"Akanksha "}]
    params = {"name":"Akanksha","subject":"New Subject"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, bcc=None, cc=None, reply_to=None, headers=None, html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
        
approval_email("Hello Bug Byters")