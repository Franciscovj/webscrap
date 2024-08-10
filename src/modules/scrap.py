import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep
import os
import warnings

warnings.filterwarnings("ignore")

class PlayersInfo:
    def __init__(self, url):
        self.url = url

    def extract_fbre_data(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()

        try:
            driver.get(self.url)
            sleep(5)

            elemento = driver.find_element(By.XPATH, '//*[@id="div_stats_standard"]')
            html_content = elemento.get_attribute("outerHTML")

            soup = BeautifulSoup(html_content, "html.parser")

            tab = soup.find(name="table")
            table_str = str(tab)

            dfc = pd.read_html(table_str)[0]
                        
            # Resetar o MultiIndex das colunas
            if isinstance(dfc.columns, pd.MultiIndex):
                dfc.columns = ['_'.join(col).strip() for col in dfc.columns.values]

            diretorio = 'data'
            if not os.path.exists(diretorio):
                os.makedirs(diretorio)
                

            dfc.to_excel(os.path.join(diretorio, 'players.xlsx'), index=False)
        except Exception as e:
            print(f"Erro ao extrair dados da URL {self.url}: {str(e)}")
        finally:
            driver.quit()

