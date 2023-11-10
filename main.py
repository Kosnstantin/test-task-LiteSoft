import json


with open("product_test.json", "r") as file:
    content = file.read()

lst = input("Enter some digitals, you wanna see in productCode: ")
big_list = json.loads(content)
for dct in big_list:
    if any(digit in str(dct["productCode"]) for digit in lst):
        print(f'productCode: {dct["productCode"]}')
 