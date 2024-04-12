import re
str1 = "yes I said yes I will Yes."
res = re.sub("[yY]es","no", str1)
print(res)


