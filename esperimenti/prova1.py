from fuzzywuzzy import fuzz as fw
import distance
import pyxdameraulevenshtein as levv

w1 = "Avelino"
w2 = "Avellinoooo"

lev = levv.damerau_levenshtein_distance(w1, w2)

w1.lower()
w2.lower()

print("lev", lev)

fuz1 = fw.ratio(w1, w2)
fuz2 = fw.partial_ratio(w1, w2)
fuz3 = fw.token_set_ratio(w1, w2)

fuzAverage = (fuz1 + fuz2 + fuz3) / 3

print("ratio", fuz1)
print("partialratio", fuz2)
print("token", fuz3)
print(fuzAverage)
print("fuzsums", (fuz2+fuz3)/2)

if (fuzAverage >= 80) or ((fuz2 + fuz3)/2 >= 85):
    print("Simili ")

