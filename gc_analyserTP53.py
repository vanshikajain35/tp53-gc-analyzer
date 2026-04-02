def calculate_gc(seq):
    G = seq.count("G")
    C = seq.count("C")
    return (G + C) / len(seq) * 100

file = open("tp53_all.fasta", "r")
data = file.read()
file.close()

lines = data.split("\n")
sequences = []
names = []

for line in lines:
    line = line.strip()
    if line.startswith(">"):
        names.append(line[1:])
    elif line !="":
        sequences.append(line)

print("Names:", len(names))
print("Sequences:", len(sequences))
print()

for name, seq in zip(names, sequences):
    gc = calculate_gc(seq)

    print("Sequence Name:", name)
    print("Sequence:", seq)
    print("GC Content:", gc)
    print()

results = []

for name, seq in zip(names, sequences):
    gc = calculate_gc(seq)
    results.append((name, gc))

# Sort by GC
results.sort(key=lambda x: x[1], reverse=True)

print("---- GC Ranking ----")
for name, gc in results:
    print(name, ":", round(gc, 2))