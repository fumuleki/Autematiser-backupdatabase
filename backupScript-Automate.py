#!/usr/bin/python3


###########################################################
#
# Ce script python est utilisé pour la sauvegarde de la base de données mysql
# 
#
##########################################################
 
# Importer les bibliothèques python requises
 
import os
import time
import datetime
import pipes
 
# Détails de la base de données MySQL sur laquelle la sauvegarde doit être effectuée. Assurez-vous que l'utilisateur ci-dessous dispose de suffisamment de privilèges pour effectuer une sauvegarde de base de données.
# Pour effectuer une sauvegarde de plusieurs bases de données, créez n'importe quel fichier comme /backup/dbnames.txt et placez les noms de bases de données un sur chaque ligne et attribués à la variable DB_NAME.
 
DB_HOST = '192.168.0.28' 
DB_USER = 'root'
DB_USER_PASSWORD = 'Cedrick1987'
#DB_NAME = '/backup/dbnameslist.txt'
DB_NAME = '/home/cedrick/dbnamelist.txt'
BACKUP_PATH = '/home/cedrick/dbbackup'

website_folder = '/var/www/html' 
# Obtenir la date et l'heure actuelle pour créer le dossier de sauvegarde séparé comme "20210912-123433".
DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME
 
# Vérifier si le dossier de sauvegarde existe déjà ou non. S'il n'existe pas, le créera 
try:
    os.stat(TODAYBACKUPPATH)
except:
    os.mkdir(TODAYBACKUPPATH)
 
# Code pour vérifier si vous souhaitez effectuer une sauvegarde de base de données unique ou attribuer plusieurs sauvegardes dans DBNAME .
print ("checking for databases names file.")
if os.path.exists(DB_NAME):
    file1 = open(DB_NAME)
    multi = 1
    print ("Databases file found...")
    print ("Starting backup of all dbs listed in file " + DB_NAME)
else:
    print ("Databases file not found...")
    print ("Starting backup of database " + DB_NAME)
    multi = 0
 
# Démarrage du processus de sauvegarde de la base de données réelle.
if multi:
   in_file = open(DB_NAME,"r")
   flength = len(in_file.readlines())
   in_file.close()
   p = 1
   dbfile = open(DB_NAME,"r")
 
   while p <= flength:
       db = dbfile.readline()   # lecture du nom de la base de données à partir du fichier
       db = db[:-1]         # supprime la ligne supplémentaire
       dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
       os.system(dumpcmd)
       gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
       os.system(gzipcmd)
       p = p + 1
   dbfile.close()
else:
   db = DB_NAME
   dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
   os.system(dumpcmd)
   gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
   os.system(gzipcmd)
 
print ("")
print ("Backup script completed")
print ("Your backups have been created in '" + TODAYBACKUPPATH + "' directory")

# Automatiser  0 1 * * * /home/cedrick/Documents/Scripts/backupScript-Automate.py
