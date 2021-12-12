import re

text = "Vreau sa merg la mare in vacanta de vara. Deja imi e dor de valuri si de sunetul apei. Nu am mai fost de cativa ani pe acolo si chiar as vrea sa merg anul acesta. Sper sa pot ajunge impreuna cu sotul si copiii mei si sa ne putem distra impreuna."
text = text.lower()
z = re.sub("[^A-Za-z0-9]+", "", text)
w = re.sub(r"[^A-Za-z0-9 ]+", "", text)
print(z)
print(w)
print(u)
s = w.split()
print(s)
i = s.count("impreuna")
print(i)
