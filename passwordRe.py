import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
password2 = re.compile(r"([a-zA-Z0-9#$%&]{8,}\d)")
string = 'Password'
password = 'hagsjwbd$%#@9'

a = pattern.search(string)
check = password2.fullmatch(password)
print(check)