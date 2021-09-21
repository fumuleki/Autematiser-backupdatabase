# Autematiser-backupdatabase

Le script a comme tâche de sauvegarde (backup) nos base de données mysql tous les jours la nuit. les backup nous permettent de bien garder et proteger nos données de l'entreprise pendant un crash de données, blocage de la base et la perte d'informations. Mieux vaux se prevenir avant que le drame se produise.

# Le projet comporte 2 parties
1. L'installation de l'environnement permettant la mise en place d'un serveur web
2. Le script de sauvegarde de base de données qui pourra éventuellement utiliser le site web wordpress

# Présentation du projet:
# Prérequis
Pour installer et faire fonctionner correctement le projet, vous aurez besoin :

1. D'opérer sur un système Linux Ubuntu 20.04
2. D'un accès root sur votre système
3. D'un accès à l'utilisateur MySQL : root
4. De la commande sudo

# Partie 1:
Mise en place d'un serveur web avec :

1. Apache2
2. MySQL
3. PHP
4. phpMyAdmin

# Partie 2:
Création d'un script python permettant :

1. De sauvegarder nos base de données MySQL dans une archive compressée
2. Création de la tâche cron

# Installation:
# Etape 1: Update

Veillez à ce que votre système soit à jour avec les commandes :

       - sudo apt-get update
       - sudo apt-get upgrade

# Etape 2: Installation Git

Veillez à installer Git si ce n'est pas déjà fait

     - sudo apt-get install git-all
     
# Partie 1: Installation 

Pour installer le serveur web (apache/mysql/php/phpmyadmin/wordpress) 

    - sudo apt-get install apache2
    - sudo apt-get install mariadb-server
    - sudo apt-get install php7.4 php-mysal php-xml
    - sudo wget https://files.phpmyadmin.net/phpMyAdmin/5.1.1/phpMyAdmin-5.1.1-all-languages.tar.gz
    - sudo wget https://fr.wordpress.org/latest-fr_FR.tar.gz
   
# Décompressée archive: phpmyadmin et wordpress
    - sudo tar xvf nom_fichier phpmyadmin et worpress
 
 # Partie 2: Script sauvegarde 
 
 Il s’agit d’un script python pour sauvegarder les bases de données MySQL à l’aide de l’utilitaire mysqldump. Ce script est testé avec Python 3.8.
 
 Sauvegarde de plusieurs bases de données : pour sauvegarder plusieurs bases de données, créez un fichier texte tel que /home/cedrick/dbnamelist.txt et ajoutez des noms de bases de données un par ligne comme ci-dessous.
    
    - sudo cat /home/cedrick/namelist.txt
      - wordpress
      - vanely
      
 Et ajoutez ce fichier au script comme ci-dessous.
 
    - DB_NAME = '/home/cedrick/dbnamelist.txt
      
Créer l’emplacement du chemin de sauvegarde :
   
     - BACKUP_PATH = '/home/cedrick/dbbackup'
     
# Script de sauvegarde Base de données Python

On commence par le script de backup toujours dans le scripts ajouter le fichier avec le code:

    -  backupScript-Automate.py
 
# Création de la cron:

Nos scripts sont prêts, nous voulons donc automatiser les backups afin que celle-ci soit faite tous les jours à 01H00. Pour ce faire nous allons créer un fichier crontab à la racine du dossier cron et ajouter le code suivant :

     - crontab -e
     - 0 1 * * * /home/cedrick/Documents/Scripts/backupScript-Automate.py
  
# Exécuter un script Python 

Après avoir copié le script, rendez le script exécutable à l'aide de la commande suivante:

    - chmod +x backupScript-Automate.py
   
et exécuter ce script comme ci-dessous:

    - python3 backupScript-Automate.py
    
# Redémarrer crontab 

     - sudo /etc/init.d/cron restart
     

    
    

