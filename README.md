# new_library

Fonctionnalités de l'application :

1) Enregistrer un nouvel utilisateur en tant que l'utilisateur normal ou l'administrateur(Seulement l'administrateur a le droit de créer un nouvel administrateur)
![image](https://user-images.githubusercontent.com/80041512/230972663-3544f209-8773-4bf0-b7ba-1cf17711ee70.png)

2) Connexion / Déconnexion des utilisateurs
![image](https://user-images.githubusercontent.com/80041512/230972959-ee2f73ca-dcbf-4889-ad99-1951c386c74d.png)

3) Recherche de livres par titre ou auteur
4) Affichage de la liste des livres disponibles pour les visiteurs de site
![image](https://user-images.githubusercontent.com/80041512/230972812-66b5889f-ce79-44a6-aa31-29d5f43ca976.png)

5) Accès au tableau de bord pour les utilisateurs connectés (affichage de la liste de livres lus, recherche de livres, affichage de la liste      de tous les livres)
![image](https://user-images.githubusercontent.com/80041512/230973672-ce3c1039-e5bd-45a8-bd87-925424cea896.png)

6) Ajouter de livres dans la liste de livres lus de l'utilisateur connecté
![image](https://user-images.githubusercontent.com/80041512/230973485-a33498e5-04a4-44be-90cf-6a9ebb7565ff.png)

7) Accès au panneau d'administration pour les utilisateurs avec des privilèges d'administrateur (ajout d'utilisateurs, voir le list des utilisateurs)
8) Affichage de la page "Trouvez votre livre"(ne pas encore terminer)
9) Il y a également un fichier journal qui enregistre des informations sur les utilisateurs qui accèdent et se déconnectent de l'application

L'application est basée sur Flask et utilise Flask_SQLAlchemy pour la gestion de la base de données. Le formulaire de connexion est protégé avec Flask_Login et la fonctionnalité d'administration est gérée par Flask_Admin. Les informations de connexion et les informations sur les livres sont stockées dans une base de données SQLite.
