import requests


print("hello world")


def greetperson(name_of_person):
    greet = "Hello, {}".format(name_of_person)
    return greet


print(greetperson("Albert babel"))

r = requests.get("https://coreyms.com")
print(r.status_code)

print(r.ok)
