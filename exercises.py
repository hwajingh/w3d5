

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
x = sorted(author, key=lambda name: name.split(" ")[-1].lower())
print (x)
print (author)