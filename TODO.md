# TODO

1. **Problème CORS avec la méthode PUT :**
   - Actuellement, il y a un problème de CORS pour les requêtes `PUT`. Swagger ne peut pas exécuter correctement cette méthode à cause des restrictions CORS. Une solution possible serait de configurer de manière plus fine Flask-CORS pour gérer les méthodes `PUT` et les pré-requêtes (`OPTIONS`).
   - Investiguer et appliquer une configuration CORS plus adaptée pour les méthodes `PUT`.

2. **Gestion d'erreurs plus robuste :**
   - Ajouter une meilleure gestion des erreurs pour éviter les crashs du serveur lorsqu'une opération est effectuée sur une pile vide.
   - Améliorer les messages d'erreur dans les réponses de l'API.

3. **Tests unitaires :**
   - Ajouter des tests unitaires pour valider les fonctionnalités principales : ajout à la pile, récupération de la pile, opérations mathématiques (addition, soustraction, multiplication, division).

4. **Amélioration de la documentation Swagger :**
   - Ajouter des descriptions plus détaillées pour chaque endpoint dans le fichier `swagger.json`.
   - Inclure des exemples pour chaque type de requête afin de faciliter les tests.

5. **Ajout de nouvelles fonctionnalités :**
   - Gérer des opérations plus complexes (exponentiation, racine carrée, etc.).
   - Ajouter une persistance des données (sauvegarder la pile dans une base de données pour que la pile survive aux redémarrages du serveur).
