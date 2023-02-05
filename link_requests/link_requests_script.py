#
#
# This script will scrape all links from Google Search
#
#
# This code have a PlayWright Engine
#
#
#
from playwright.sync_api import sync_playwright


class ScrapeData:

    'Scrape data from links.'

    def __init__(self, link: str):
        self.link = link

    
    def get_html_code(self):

        with sync_playwright() as response:
           
            # set browser
            browser = response.firefox.launch(
                
                # if False show, if True do not show
                headless=True,
            ) # <- end browser block


            # get context
            context = browser.new_context(

                # most common interface is 1920x1080
                viewport={"width": 1920, "height": 1080}
            ) # <- end context block

            # create page aka browser tab which we'll be using to do everything
            page = context.new_page()

            page.goto(self.link) # go to url
            
            return page.content() # return html page content!!!
