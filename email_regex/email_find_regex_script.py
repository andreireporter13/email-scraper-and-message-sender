#
#
# This script will return emails from HTML documents...
#
#
# search mails with regex
import re 


class FindEmailRegex:
    
    'This blueprint will return emails from text.'


    def __init__(self, html_text: str):
        self.html_text = html_text

    
    def extract_email(self):

        '''
        This method return all emails from html code.
        '''

        # extract emails with regex
        email_from_html = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}\b", re.IGNORECASE)

        return re.findall(email_from_html, self.html_text)

