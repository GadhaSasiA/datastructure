a={"brand":"ford","Model":"mustag","year":1954}
print(a)

if "model" in a:
    print("yes")

a["year"]=1956
print(a)

a.update({"type":"raising"})
print(a)

a["color"]=["mutte navy blue","matte black"]
print(a)

a.pop("type")
print(a)

a.popitem()
print(a)

del a["year"]
print(a)

a.clear()
print(a)

