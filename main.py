def acceptare(cuvant,s,gram):
    if not cuvant:
        return "lambda" in gram[s]
    for x in gram[s]:
        if x[0]==cuvant[0] :
            if acceptare(cuvant[1:],x[1:],gram):
                return True
    return False

f=open("gramatica","r")
gram=dict()
for linie in f:
    linie=linie.split("->")
    simbol=linie[0].strip()
    regula=linie[1].strip()
    regula=regula.split("|")
    regula=[x.strip() for x in regula]
    gram.update({simbol:regula})
f.close()
f=open("cuvinte")
cuvinte=[linie.strip() for linie in f]
f.close()
f=open("simbol")
s=f.read()
f.close()
for cuv in cuvinte:
    if acceptare(cuv,s,gram):
        print(f"Cuvantul {cuv} este acceptat de gramatica")
    else:
        print(f"Cuvantul {cuv} nu este acceptat de gramatica")

