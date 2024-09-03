import random
from colorama import Fore, Back, Style

question = "will it rain tomorrow?"

bad_fortune=["doubtful","no chance","unlikely","no way"]

good_fortune=["afraid so","you bet","likely","for sure"]

rand_number= random.randint(1,8)
print(rand_number)

if rand_number%2==0:
    print(random.choice(good_fortune))
else:
    print(random.choice(bad_fortune))

print(Fore.GREEN + "good_fortune")

print(Fore.RED + "bad_fortune")
















      










