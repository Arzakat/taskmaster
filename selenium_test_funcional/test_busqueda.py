from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

def test_busqueda_inmuebles():
    driver = webdriver.Chrome()  # Asegúrate que chromedriver.exe está en el PATH
    
    try:
        driver.get("https://duckduckgo.com/")
        
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("inmuebles en Bogotá" + Keys.RETURN)
        
        wait = WebDriverWait(driver, 10)
        results = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "article[data-testid='result']")
            )
        )
        
        assert len(results) > 0
        print(f"\n✅ Prueba exitosa! Se encontraron {len(results)} resultados")
        
    finally:
        driver.quit()