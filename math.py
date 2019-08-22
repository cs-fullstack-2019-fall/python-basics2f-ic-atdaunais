# # Practice random and f-string formatting
#
# import random
#
# nameList = ["Boib", "Joe", "Clark", "You"]
# # random_number = random.randint(0, (len(nameList)-1))
# # print(nameList[random_number])
#
# # can use with arrays/lists
#
# rand_people = random.sample(nameList, 4)
# print(rand_people)

fname = "Andrew"
lname = "Daunais"
city = "Memphis"

str_welcome_text = "Hello "+fname+" "+lname+" from "+city+"!!!"
tem_welcome_text = f"Hello {fname} {lname} from {city}!!!"
print(str_welcome_text)
print(tem_welcome_text)