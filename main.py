def acceptare(cuvant, s, gram):
    if not cuvant:
        return "lambda" in gram[s]
    for x in gram[s]:
        if x[0] == cuvant[0]:
            if acceptare(cuvant[1:], x[1:], gram):
                return True
    return False


with open("gramatica", "r") as f:
    gram = {}
    for linie in f:
        linie = linie.split("->")
        simbol = linie[0].strip()
        regula = linie[1].strip()
        regula = regula.split("|")
        regula = [x.strip() for x in regula]
        gram[simbol] = regula

with open("cuvinte", "r") as f:
    cuvinte = [linie.strip() for linie in f]

with open("simbol", "r") as f:
    s = f.read()

for cuv in cuvinte:
    if acceptare(cuv, s, gram):
        print(f"Cuvantul {cuv} este acceptat de gramatica")
    else:
        print(f"Cuvantul {cuv} nu este acceptat de gramatica")
