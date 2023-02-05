#
#
# This script will returned a list of links from site-s with mails
#
#
# Google Search library
from googlesearch import search
#
#
class RoGoogleSearch:

    "This class scrape links with emails from Google"


    # default parameters
    #
    def __init__(self, search_keyword: str, number_of_results: int, lang='ro'):

        # set arguments for searching
        self.search_keyword = search_keyword + ' mailuri'     # ---> SEO keyword for searching
        self.number_of_results = number_of_results            # ---> how many results need
        self.lang = lang                                      # ---> it set by default for romanian results
        self.list_of_links = []                               # ---> list of links


    # function for check number_of_results
    #
    @staticmethod
    def check_number_of_results(number: int) -> bool:
        '''
        This method check if number for Google results is bigger than 1 and smallest than 30.
        '''
        
        return True if 1 <= number <= 10 else False


    def make_request(self) -> list:
        '''
        This method make a requests to Google server and return a list of links.
        '''

        # check if number of results is ok
        #
        if self.check_number_of_results(self.number_of_results):

            # here make a requests
            #
            for link in search(self.search_keyword, num_results=self.number_of_results, lang=self.lang):
                if link is not None:
                    self.list_of_links.append(link)

        else: 
            print('You are introduce invalid data...')

        return self.list_of_links
