import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

# ABRIR LA PAGINA BANREP
driver = webdriver.Edge()
driver.get("https://suameca.banrep.gov.co/estadisticas-economicas/#/dashboard")
time.sleep(5)


#CLICK EN PRECIOS E INFLACION
boton_lista = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "accordion-header-0"))
)
boton_lista.click()
#time.sleep(5)

#CLICK EN INDICE DE PRECIOS AL CONSUMIDOR (IPC)
icono = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="accordion-body-0"]/div/div[2]/mat-tree/mat-nested-tree-node[2]/div[1]/a/mat-icon'))
)
icono.click()
#time.sleep(5)

#CLICK EN BASE 2018
icono = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="accordion-body-0"]/div/div[2]/mat-tree/mat-nested-tree-node[2]/div[2]/mat-nested-tree-node[1]/div[1]/a/mat-icon'))
)
icono.click()
#time.sleep(5)


enlace = driver.find_element(By.XPATH,'//*[@id="accordion-body-0"]/div/div[2]/mat-tree/mat-nested-tree-node[2]/div[2]/mat-nested-tree-node[1]/div[2]/mat-tree-node[2]/a')
enlace.click()

# Esperar hasta que se abra la nueva pestaña
WebDriverWait(driver, 10).until(EC.new_window_is_opened)

# Cambiar a la nueva pestaña
driver.switch_to.window(driver.window_handles[1])

print("Nueva URL:", driver.current_url)
time.sleep(12)


acciones = ActionChains(driver)

# Moverse a una posición (100px a la derecha, 200px abajo) y hacer clic derecho
acciones.move_by_offset(50, 400).context_click().perform()

# Esperar unos segundos para ver el resultado (solo para pruebas)
time.sleep(2)

acciones.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
time.sleep(2)

acciones.send_keys(Keys.ENTER).perform()
time.sleep(2)

desplegable = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="oj-select-choice-idGadgetViewFor_shareFormat"]'))
)
desplegable.click()
time.sleep(4)

acciones.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
#time.sleep(2)

icono = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="bi_share_context_dialog-okbutton"]/button'))
)
icono.click()
time.sleep(12)


