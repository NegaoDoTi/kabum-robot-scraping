from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.webdriver import WebDriver


class Waits:

    def __init__(self, driver:WebDriver) -> None:
        self.locators = {
            'id': ['', ''],
            'xpath' : ['', ''],
            'link_text':['', ''],
            'partial_link_text': ['', ''],
            'name': ['', ''],
            'tag_name': ['', ''],
            'class_name': ['', ''],
            'css_selector': ['', '']
        }
        self._wait = None
        self.driver = driver


    def get_locators(self, locator):

        """
        
        Tipos esperado no dicionário exemplo {'id': 'teste'}

        "id"
        "xpath"
        "link_text"
        "partial_link_text"
        "name"
        "tag_name"
        "class_name"
        "css_selector"
        """
        
        for key in self.locators:
            if isinstance(self.locators[key], tuple):
                self.locators[key] = ['', '']

        if not isinstance(locator, dict):
            raise ValueError('Tipo de entrada inválida, o locator deve ser do tipo dict')
        
        if len(locator.keys()) > 1:
            raise ValueError('Apenas um parâmetro é esperado.')
        
        key_entry = locator.keys()
        for ky in key_entry:
            key_entry = ky
        
        new_key_entry = str(key_entry).replace('_', ' ')
        
        value_entry = locator.values()
        for it in value_entry:
            value_entry = it

        try:
            self.locators[key_entry][0] = new_key_entry
            self.locators[key_entry][1] = value_entry

            selector = tuple(self.locators[key_entry])

            return selector
        except:
            raise ValueError('Entrada inválida')


    def wait_presence(self, locator:dict, time=10):
        '''
        Espera o elemento estar presente na tela
        Retorna um web element ou lança uma exception
        '''
        self._wait = WebDriverWait(self.driver, time)
        this_locator = self.get_locators(locator)
        element = self._wait.until(ec.presence_of_element_located(this_locator))
        return element


    def wait_all_presence(self, locator:dict, time=10):
        '''
        Espera o elemento estar presente na tela
        Retorna um web element ou lança uma exception
        '''
        self._wait = WebDriverWait(self.driver, time)
        this_locator = self.get_locators(locator)
        elements = self._wait.until(ec.presence_of_all_elements_located(this_locator))
        return elements
    

    def wait_clickable(self, locator:dict, time=10):
        '''
        Espera o elemento estar presente na tela e ser possível executar o comando click
        Retorna um web element ou lança uma exception
        '''
        self._wait = WebDriverWait(self.driver, time)
        this_locator = self.get_locators(locator)
        element = self._wait.until(ec.element_to_be_clickable(this_locator))
        return element


    def wait_visibility(self, locator:dict, time=10):
        '''
        Espera o elemento estar presente na tela, altura e largura maiores que 0px
        Retorna um web element ou lança uma exception
        '''
        self._wait = WebDriverWait(self.driver, time)
        this_locator = self.get_locators(locator)
        element = self._wait.until(ec.visibility_of_element_located(this_locator))
        return element
    
    def wait_visibility_all(self, locator:dict, time=10):
        '''
        Espera os elementos estarem presentes na tela, altura e largura maiores que 0px
        Retorna um web element ou lança uma exception
        '''
        self._wait = WebDriverWait(self.driver, time)
        this_locator = self.get_locators(locator)
        element = self._wait.until(ec.visibility_of_all_elements_located(this_locator))
        return element
    

    def wait_alert(self, time=10):
        '''
        Espera pelo alert estar presente na página
        Retorna um web element ou lança uma exception
        '''
        self._wait = WebDriverWait(self.driver, time)
        element = self._wait.until(ec.alert_is_present())
        return element
    

    def wait_frame_and_switch(self, locator:dict, time=10):
        '''
        Espe o iframe estar presente na tela e muda para o mesmo caso esteja presente
        Retorna um web element ou lança uma exception
        '''
        self._wait = WebDriverWait(self.driver, time)
        this_locator = self.get_locators(locator)
        element = self._wait.until(ec.frame_to_be_available_and_switch_to_it(this_locator))
        return element
    

    def wait_invisibility(self, locator:dict, time=10):
        '''
        Espera o elemento não estar presente na tela, altura e largura maiores que 0px
        Retorna um web element ou lança uma exception
        '''
        self._wait = WebDriverWait(self.driver, time)
        this_locator = self.get_locators(locator)
        element = self._wait.until(ec.invisibility_of_element_located(this_locator))
