from webdriver_manager.chrome import ChromeDriverManager

# ...

# Utiliza ChromeDriverManager para obtener la ruta del controlador de Chrome
driver_path = ChromeDriverManager().install()

# Crea el controlador de Chrome utilizando la ruta del controlador
navegador = webdriver.Chrome(executable_path=driver_path, options=opc)
