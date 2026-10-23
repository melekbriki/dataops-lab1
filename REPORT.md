\# TP2 - Versionner le code avec Git et les données avec DVC



\## Q1. Pourquoi utiliser une branche Git ?

Une branche permet de développer une nouvelle fonctionnalité sans modifier directement la branche principale.



\## Q2. Pourquoi utiliser DVC pour les données ?

DVC permet de versionner les données volumineuses séparément du code Git.



\## Q3. Quel est le rôle de data-v1 et data-v2 ?

data-v1 représente les données originales.

data-v2 représente les données après l'ajout de cinq commandes tardives.



\## Q4. Pourquoi utiliser un stockage distant DVC ?

Il permet de partager les données et de les récupérer sur une autre machine.



\## Q5. Pourquoi les fichiers DVC utilisent-ils des hashes ?

Les hashes identifient le contenu des fichiers et permettent de détecter les changements.



\## Q6. Comment restaurer une ancienne version des données ?

On restaure le fichier .dvc correspondant à la version voulue, puis on exécute dvc checkout.



\## Q7. Quel est le chiffre d'affaires de data-v1 ?

Le chiffre d'affaires total est de 7655.90.



\## Q8. Quel est le chiffre d'affaires de data-v2 ?

Le chiffre d'affaires total est de 8835.40.



\## Q9. Pourquoi utiliser git clone et dvc pull ?

git clone récupère le code et les fichiers de suivi. dvc pull récupère les données stockées dans le remote DVC.



\## Q10. Que se passe-t-il si le remote DVC n'est pas accessible ?

Le code peut être cloné avec Git, mais les données suivies par DVC ne peuvent pas être récupérées depuis ce remote.



\## Q11. Que se passe-t-il si on oublie dvc push ?

Les nouvelles données ne sont pas disponibles dans le remote DVC pour les autres membres de l'équipe.



\## Q12. Quels problèmes de TP1 sont améliorés par TP2 ?

Git et DVC facilitent le versionnement, le partage et la reproductibilité du projet. L'automatisation et les alertes restent des améliorations possibles.

