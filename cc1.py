#Yuan Ding Python CC1 27.3.26

activites = [
    ["Alice","cinema"],
    ["Bob","sport"],
    ["Claire","lecture"],
    ["Alice","voyage"],
    ["David","sport"],
    ["Emma","cinema"],
    ["Bob","musique"],
    ["Claire","cinema"]    
]

#1

membre=[]

for personne in activites:
    membre.append(personne[0])

membre=list(set(membre))

membre.sort(reverse=False)

print("Voici les membres : ")
print(membre)

#2
activite=[]

for personne in activites:
    activite.append(personne[1])

activiteUnique=list(set(activite))

activiteUnique.sort(reverse=False)

print("Voici les activités : ")
print(activiteUnique)
print("Le nombre total des activités est "+str(len(activiteUnique)))

#3
dicActivite={}

for i in activiteUnique:
    dicActivite[i]=0

for k in dicActivite.keys():
    for act in activite:
        if k==act:
            dicActivite[k]=dicActivite[k]+1

for k,v in dicActivite.items():
    print(k+" : "+str(v))


#4

dicPersonne={}

for i in membre:
    dicPersonne[i]=[]

for k in dicPersonne.keys():
    for personne in activites:
        if k == personne[0]:
            dicPersonne[k].append(personne[1])

for k,v in dicPersonne.items():
    print(k+" : "+", ".join(v))

#5
diff=False

while(not diff):
    nom1=input("Saisir le nom d'un premier membre \n")
    nom2=input("Saisir le nom d'un deuxième membre \n")
    diff=True
    if (nom1 not in membre) or (nom2 not in membre):
        print("Entrez des membres qui existent!")
        diff=False
    if nom1==nom2:
        print("Entrez deux membres différents!")
        diff=False

set1={}
set2={}

for k,v in dicPersonne.items():
    if k==nom1:
        set1=set(v)

for k,v in dicPersonne.items():
    if k==nom2:
        set2=set(v)

commune=list(set1&set2)

if len(commune)!=0:
    print("Leur activite commune est "+" ".join(commune))
else:
    print("Ils n'ont pas d'activité commune.")

#6
def interetCommun(dicPersonne, nom):
    interet=set()
    partenaire=[]
    for k,v in dicPersonne.items():
        if nom==k:
            interet=set(v)
    for k,v in dicPersonne.items():
        if nom!=k:
            interetCommune=list(interet&set(v))
            if len(interetCommune)!=0:
                partenaire.append(k)

    return " ".join(partenaire)


print(interetCommun(dicPersonne,"Alice"))
