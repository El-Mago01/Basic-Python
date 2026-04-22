import sys
print(sys.path)
sys.path.append("c:\\Users\\marti\\PycharmProjects\\PythonProject\\Intermediate python\\testing_libraries\\")
print(sys.path)
import my_library as my_lib
import masterlib

import countryinfo as country

canada_info=country.CountryInfo("Canada")
print(canada_info.capital())
#print(country("Canada"))


print("Hello World")
print(my_lib.add(4,3))
# The above code fails as my_lib is an external library name that already exists
# In this manner, it is best to tell python where the package is using the:
# ~bash: pip install -e . from the directory where my library is
# i.e. cd /user/Marti/PythonProject/Intermediate python_testing_libraries
# pip install -e