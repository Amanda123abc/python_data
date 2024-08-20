animals={
    "Lion":"cub",
    "Pigeon":"Squab",
    "Gecko":"baby gecko",
    "Hedgehog":"hoglet"
}

print(animals["Gecko"])

print(animals.keys())
print(animals.values())
print(animals.items())

animals["Gecko"]="hatchling"
print(animals["Gecko"])

print(animals.get("Gecko"))
print(animals.get("cat"))

print(animals.setdefault("Lion", "baby lion"))

animals.setdefault("zebra","foal")
print(animals)

animals.update({"fish":"fry","crab":"zoea"})
print(animals)

animals.pop("Lion")
print(animals)

#Activity 3 - week 3
languages={
    "england":"english",
    "spain":"spanish",
    "ethopia":"amharic",
    "iran":"farsi"
}
print(languages)

#Activity 4 - week 3

animals={
    "lion":"cub",
    "pigeon":"squab",
    "gecko":"hatchling",
    "hedgehod":"hoglet"
}
print(animals)
print(animals.get("lion"))




