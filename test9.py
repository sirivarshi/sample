import random
import string

result = [random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits)for n in range(10)]
print(result)