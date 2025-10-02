p = "In botany, a tree is a perennial plant with an elongated stem, or trunk, usually supporting branches and leaves. In some usages, the definition of a tree may be narrower, e.g., including only woody plants with secondary growth, only plants that are usable as lumber, or only plants above a specified height. Wider definitions include taller palms, tree ferns, bananas, and bamboos."

d = dict()
for i in p:
    d[i] = d.get(i , 0) + 1
print(d)

"""
first i wrote this :
 
for i in p:
    d[i] = d.count(i)
print(d)

but tought this may be slow for big paragraphs later so asked ai if there is any faster way .
it told me to use "d.get(i, 0) + 1" since it would only scan the whole string only one time.

how does d.get... works ? 
first it gets a word/chr of a string and adds it as a new Key in our dict "d".
then adds 1 value in whatever the Key it is on right now.
It keeps this loop going till it reaches the end of our stirng.
"""