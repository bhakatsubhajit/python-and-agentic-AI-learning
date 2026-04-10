# internal or built-in module
import math
print(math.sqrt(64))

# external module
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
# custom module

import myModuleEx
myModuleEx.welcome("Subhajit")