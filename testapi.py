import requests as requests
codigo = input('Ingrese el código del producto: ')
url = 'http://localhost/apis/productos.php?codigo='+codigo
requests = requests.get(url)
print(responsive.json())