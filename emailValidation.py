# conditions
# a-z alphabet small case
# 0-9 digit
# . _ only 1 time
# @ one time
# . on 2 3 position from backword

import re

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input('Enter Your Email : ')
if re.search(email_condition, user_email):
    print("Right EMail")
else:
    print("Wrong Email")
