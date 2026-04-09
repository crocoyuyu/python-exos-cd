import csv
inscriptions=[]
fichier1=open('C:/temp/inscription.csv', encoding='utf-8')
lecteur = csv.DictReader(fichier1, delimiter=';')
for ligne in lecteur:
    inscriptions.append(ligne)

print(inscriptions)

#repérer un ensemble des cours et des noms des étudiants
etudiant=set()
cours=set()
for ligne in inscriptions:
    etudiant.add(ligne["Etudiant"])
    cours.add(ligne["Cours"])

#création d'une liste des dictionnaires 
#dans chaque dicto, insérer le premier champ avec clé : Etudiant et la valeur correspondante
new=[]
for etu in etudiant:
    student={}
    student['Etudiant']=etu
    new.append(student)

#insertion des notes
for student in new:
    for ligne in inscriptions:
        for matiere in cours:
            if student['Etudiant']==ligne['Etudiant']:
                if ligne['Cours']==matiere:
                        student[matiere]=ligne['Note']

#création de header
header=['Etudiant']
for matiere in cours :
    header.append(matiere)

#écriture du fichier
fichier = open('C:/temp/new.csv', 'w', newline='', encoding='utf-8')
writer = csv.DictWriter(fichier, fieldnames=header)
writer.writeheader()
writer.writerows(new)

fichier1.close()
fichier.close()
