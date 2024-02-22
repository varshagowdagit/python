import re
txt = "the rain in spain"
x = re.findall("ai",txt)
print(x)

y = re.search("rain",txt)
print(y)

z = re.split("\s",txt)
print(z)

a = re.sub('a','b',txt)
print(a)


import re
email_pattern = r"^[a-zA-Z0-9.]+@[a-zA-Z0-9]+.com$"
email = "user@example.com"

if re.match(email_pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")


import re

phone_pattern = r"(\d{3})-(\d{3})-(\d{4})"
text = "Phone numbers: 123-456-7890, 987-654-3210"

matches = re.findall(phone_pattern, text)
for match in matches:
    print("Phone number:", "-".join(match))

email_pattern = r'^[a-zA-Z0-9.]+@[a-zA-Z0-9]+.com$'
email1="varsha.@capgemini.com"
if re.match(email_pattern,email1):
    print("valid")
else:
    print("invalid")

import re

password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
password = "SecureP@ssw0rd"

if re.match(password_pattern, password):
    print("Valid password")
else:
    print("Invalid password")


import re

html_pattern = r"<([a-zA-Z][^\s>]*)\s*[^>]*>(.*?)<\/\1>"
html = "<p>This is a <b>bold</b> text.</p>"

matches = re.findall(html_pattern, html)
for match in matches:
    print("Tag:", match[0])
    print("Content:", match[1])
