customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("birthdate","Jan 1 1980")) ##Workaround to avoid key error
## when the key is not defined. You may also add a replacement value
## if you use square bracket in calling a non-existent key, it will throw an error
