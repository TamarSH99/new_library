# new_library

Fonctionnalités de l'application :

1) Enregistrer un nouvel utilisateur en tant que l'utilisateur normal ou l'administrateur(Seulement l'administrateur a le droit de créer un nouvel administrateur) 
2) Connexion / Déconnexion des utilisateurs
3) Recherche de livres par titre ou auteur
4) Affichage de la liste des livres disponibles
5) Ajouter de livres dans la liste de livres lus de l'utilisateur connecté
6) Accès au tableau de bord pour les utilisateurs connectés (affichage de la liste de livres lus, recherche de livres, affichage de la liste      de tous les livres)
7) Accès au panneau d'administration pour les utilisateurs avec des privilèges d'administrateur (ajout d'utilisateurs, voir le list des utilisateurs)
8) Affichage de la page "Trouvez votre livre"(ne pas encore terminer)
9) Il y a également un fichier journal qui enregistre des informations sur les utilisateurs qui accèdent et se déconnectent de l'application

L'application est basée sur Flask et utilise Flask_SQLAlchemy pour la gestion de la base de données. Le formulaire de connexion est protégé avec Flask_Login et la fonctionnalité d'administration est gérée par Flask_Admin. Les informations de connexion et les informations sur les livres sont stockées dans une base de données SQLite.
