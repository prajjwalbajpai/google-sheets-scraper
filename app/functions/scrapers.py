import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import google.generativeai as genai
from dotenv import load_dotenv
import os
from googleapiclient.discovery import build
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()


CUSTOM_SEARCH_URL = 'https://www.googleapis.com/customsearch/v1'
CUSTOM_SEARCH_API_KEY = os.getenv('GOOGLE_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")



class WebScraper:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        # self.service = Service(chromedrier_path)

    def google_search(self, query):
        driver = webdriver.Chrome(options=self.options)
        encoded_query = query.replace(" ", "%20")
        links = []
        try:
            url = f"https://www.googleapis.com/customsearch/v1?key={CUSTOM_SEARCH_API_KEY}&cx={SEARCH_ENGINE_ID}&q={encoded_query}&gl=in"
            response = requests.get(url)
            data = response.json()
            ans =  str()
            if data['items']: ans = data['items'][0]['link']
            else: return "NO RESULTS FOUND"

            return ans
        
        except Exception as e:
            return f"Search error: {e}"
        finally:
            driver.quit()
        

    # Scrape webpage content using Selenium and BeautifulSoup to extract both text and links.
    def scrape_page(self,url):
            driver = webdriver.Chrome(options=self.options)
            content = []
            
            try:
                driver.get(url)
                page_source = driver.page_source
                time.sleep(2)
                
                soup = BeautifulSoup(page_source, 'html.parser')
                
                # Extract text content
                text = soup.get_text()
                lines = (line.strip() for line in text.splitlines())
                content = ' '.join(line for line in lines if line)
                
            except Exception as e:
                return f"Scraping error for {url}: {e}"
            finally:
                driver.quit()
            
            return content

    def prompt(self,content: str, type : int):
        # type 1 == normal search
        # type 2 == about company in brief

        prompt = f""

        if(type == 1):
            prompt = content + f"\n Tell in short"

        elif(type == 2):
            prompt = f"""
            Give a brief description of the company from the given data the description should be less than 50 words:
            Data: {content}
            
            """
        
        try:
            response = model.generate_content(prompt)
            text = response.text

            return text
            
        except Exception as e:
            return f"LLM error"



def find_linkedin(name, pos):
    scraper = WebScraper()
    search_prompt =  f"site:linkedin.com \"{name}\" \"{pos}\""
    print(search_prompt)

    return scraper.google_search(search_prompt)

def simple_prompt(text):
    scraper = WebScraper()

    return scraper.prompt(text, 1)

def short_company_inf(name):
    scraper = WebScraper()
    query = name + " about page"
    link = scraper.google_search(query) 
    data = scraper.scrape_page(link)
    text = scraper.prompt(data, 2)

    return text