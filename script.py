import sys
import requests

print(sys.version)
print("hello world")


def greetperson(name_of_person):
    greet = "Hello, {}".format(name_of_person)
    return greet


print("hello")

print(greetperson("Albert"))

r = requests.get("https://coreyms.com")
print(r.status_code)

print(r.ok)
