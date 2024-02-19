mydict = dict(name="john", age=36, country="norway")
print(mydict)


a={"brand":"ford","Model":"mustag","year":1954}
print(a)

x=a.get("model")
print(x)

y=a.keys()
print(y)

z=a.values()
print(z)

t=a.items()
print(t)

a.update({"model":"renault"})
print(a)
a["type"]="raising"
print(a)

a["color"]=["mutte navy blue","matte black"]
print(a)