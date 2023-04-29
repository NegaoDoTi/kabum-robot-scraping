import pandas
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from waits import Waits
from kabum_selectors import KabumSelectors
#from selenium.webdriver.firefox.options import Options


class KabumScrapping:
    
    def __init__(self):
        self.__link = "https://www.kabum.com.br/computadores/notebooks/notebook-gamer"
        
        # options = Options()
        # options.add_argument("--headless")
        self.__driver = webdriver.Firefox()
        
        self.__wait = Waits(self.__driver)
        
        
    def main(self):
        try:
            loading = self.loading()
            if(loading["error"] == True):
                raise Exception(f'{loading["type"]}{loading["mesage"]}')
            
            number_pages = self.number_pages()
            if(number_pages["error"] == True):
                raise Exception(f'{loading["type"]}{loading["mesage"]}')
            number_pages = number_pages["number"]
            
            
            values = []
            for i in range(1, number_pages+1):
                
                page = self.page(i)
                if(page["error"] == True):
                    raise Exception(f'{page["type"]}{page["mesage"]}')
                search_produts = self.search_products()
                if(search_produts["error"] == True):
                    raise Exception(f'{search_produts["type"]}{search_produts["mesage"]}')
                
                for i in range(len(search_produts["names"])):
                    values.append([search_produts["names"][i], search_produts["prices"][i], search_produts["links"][i]])
                    
             
                
            excel = self.export_excel(values)
            if(excel["error"] == True):
                raise Exception(f'{excel["type"]}{excel["mesage"]}')
            self.__driver.quit()
            
        except Exception as e:
            with open("log_kabum.txt", "a+") as archive:
                archive.write(f"{e}")
                archive.close()
            
    
    def loading(self):
        try:
            self.__driver.get(self.__link)
            
            return {"error" : False}
        except Exception as e:
            return {"error" : True, "type" : 'Erro ao carregar site', "mesage" : f"\n{e}\n{traceback.format_exc()}"}
        
    def number_pages(self):
        try:
            number_pages = self.__wait.wait_visibility(KabumSelectors.b_price).text
            
            number_pages = int(number_pages)/20
            
            return {"error" : False, "number" : int(number_pages)}
        except Exception as e:
            return {"error" : True, "type" : "erro ao achar numero de paginas", "mesage" : f"\n{e}\n{traceback.format_exc()}"}        
    
    def search_products(self):
        try:
            product_divs = self.__wait.wait_visibility_all(KabumSelectors.product_div)
            
            names = []
            prices = []
            links = []
            
            for div in product_divs:
                
                product_name = div.find_element(*KabumSelectors.span_name).text
                
                product_price = div.find_element(*KabumSelectors.span_price).text
                product_link = div.find_element(By.TAG_NAME, "a").get_attribute('href')
                
                names.append(product_name)
                prices.append(product_price)
                links.append(product_link)
                        
            return {"error" : False, "names" : names, "prices" : prices, "links" : links}
        
        except Exception as e:
            return {"error" : True, "type" : "erro ao procurar nomes e preço dos produtos", "mesage" : f"\n{e}\n{traceback.format_exc()}"}
        
    def page(self, number):
        try:
            self.__driver.get(f"https://www.kabum.com.br/computadores/notebooks/notebook-gamer?page_number={number}&page_size=20&facet_filters=&sort=price")

            return {"error" : False}
        except Exception as e:
            return {"error":True, "type" : "Erro ao pegar site", "mesage" : f"\n{e}\n{traceback.format_exc()}"}
        
    def export_excel(self, infos:list):
        try:
            hearders = ["Modelos", "Preços", "Links"]
            
            df = pandas.DataFrame(data = infos, columns = hearders)
            print(df)
            excel_archive = pandas.ExcelWriter("notebooks_kabum.xlsx", engine = "openpyxl")
            
            df.to_excel(excel_archive, sheet_name="router_list", index = False)
            excel_archive.close()

            print("Arquivo Excel Gerado com sucesso!")
            
            return {"error" : False}
            
        except Exception as e:
            return {"error" : True, "type" : "erro ao exportar arquivo xlsx", "mesage" : f"\n{e}\n{traceback.format_exc()}"}


if __name__ == "__main__":
    
    teste = KabumScrapping()
    teste.main()