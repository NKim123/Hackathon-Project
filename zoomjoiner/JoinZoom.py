from selenium import webdriver

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.headless = True
browser = webdriver.Firefox(options=fireFoxOptions)



