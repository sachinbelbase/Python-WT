with open("JSON\\demo.json", "w") as file:
    json.dump(demo, file, indent=5)
    print(type(demo))