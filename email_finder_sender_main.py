#########################################################################
#
# Email finder && sender --- script with Python3.10
# Version 1.0
#
##########################################################################
#
#
# Author: Andrei C. Cojocaru
# Linkedin: https://www.linkedin.com/in/andrei-cojocaru-985932204/
# Facebook: https://www.facebook.com/webautomation.romania
# Tiktok: https://www.tiktok.com/@andrei_13.py
# Twitter: https://twitter.com/andrei_reporter
# Youtube: https://www.youtube.com/channel/UCgx_Y9OHi5KPVzLJo9setxw
# GitHub: https://github.com/andreireporter13
# Website: https://webautomation.ro/
# Website: https://virtualhome.ro/
# 
# 
#############################################################################
#
# ------------------------> All logic is HERE <-----------------------------
#
#############################################################################
#
#
# import my modules
#
from google_search import RoGoogleSearch       # module for search site in Google with keywords
from link_requests import ScrapeData           # this script scrape HTML data from link
from email_regex import FindEmailRegex         # module for search mail from HTML 
from email_sender import SendEmailTo           # module for send mail to found gmail in Online

# import another libraries
from time import sleep


# 
def find_links_in_google(keyword: str, num_pages: int) -> list:
    """
    Inside of this function, create a instance of RoGoogleSearch class. 
    This help us find more links in Google without bloking recaptcha. 
    """

    new_links = RoGoogleSearch(keyword, num_pages).make_request()
    print()
    print(new_links)

    # and return links 

    return new_links


def scrape_email_and_send_email(list_site: list, choose_format_message: int, mail_subject_message: str) -> None: 
    """
    This function will scrape links and return a emails from HTML template. 
    If email will be found, this script will send message to mail.
    """

    # make for and scrape links 
    for idx, link in enumerate(list_site):

        # this method from ScrapeData to scrape link with PlayWright
        from_scrape = ScrapeData(link).get_html_code()

        # this method will be scrape emails
        new_emails = FindEmailRegex(from_scrape).extract_email()

        # print numbers of emails.
        print()
        print(new_emails)

        # if mail was founded, send mail ---> 
        if len(set(new_emails)) > 0: 

            # take emails 
            for email in list(set(new_emails)):
                SendEmailTo(email, choose_format_message, mail_subject_message)

                print()
                # print in terminal the status of email sender
                print(f'Message to {email} ---> send!')


def main():
    """
    Main Function -> store all logic of code inside.
    """

    # keyword and numbers of pages ---> google search
    keyword_name = input('Scrie un cuvant cheie pentru a returna emailuri targetate: ')
    number_of_pages = int(input('Introdu numarul linkurilor pe care vrei sa le returnezi (1-10): '))

    # email choose plain ori html_template
    choose_plain_or_html = int(input('Introdu ce mesaj vrei sa trimiti. 1-plain_text; iar 2-html_template: '))
    message_subject = input(('Introdu subiectul mesajului pentru mailurile pe care vrei sa le trimiti: '))

    # check number_ from input
    if 0 < number_of_pages < 11: 
        list_of_site = find_links_in_google(keyword_name, number_of_pages)
        scrape_email_and_send_email(list_of_site, choose_plain_or_html, message_subject)
    else: 
        print('Nu ai introdus valorile cerute...')


if __name__ == "__main__":
    main()