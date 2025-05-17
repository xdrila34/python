data = {
    "name":"Jon Doe",
    "age": 30,
    "address":{
        "street":"street 1230",
        "city": "prishtina"

    },
    "contact":
        [
            {
                "type1": "email"

            },
            {
              "type2": "phone"
            }
        ]

}
print(data["address"]["street"])
print(data["contact"][0]["type1"])