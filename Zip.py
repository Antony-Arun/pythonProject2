names = ("Arun", "Jeni", "antony")
comps = ("medex","jms", "indo")
zipped = dzip(names,comps)
#zipped = list(zip(names,comps))
#zipped = set(zip(names,comps))
#zipped = dict(zip(names,comps))
#zipped = tuple(zip(names,comps))
#print(zipped)

for (a,b) in zipped:
    print(a,b)