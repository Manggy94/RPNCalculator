# Roadmap - Calculatrice RPN

## Version 1.1 : Améliorations du front-end et de l'expérience utilisateur

1. **Interface web dédiée :**
   - Créer une interface web simple avec React, Vue.js ou Angular pour permettre aux utilisateurs de manipuler la pile visuellement.
   - Offrir une vue en temps réel de l'état de la pile ainsi qu'une interface pour ajouter des nombres et effectuer des opérations.

2. **Améliorations de Swagger :**
   - Ajouter des exemples pour chaque requête dans la documentation Swagger pour rendre les tests plus intuitifs.
   - Inclure des explications sur chaque opération, ainsi que des erreurs potentielles.

3. **Optimisation des performances :**
   - Améliorer les performances de l'API pour la gestion de grands nombres d'opérations et d'utilisateurs concurrents.
   - Ajouter des mécanismes de mise en cache pour certaines requêtes GET.


## Version 1.2 : Nouvelles fonctionnalités

1. **Opérations avancées :**
   - Ajouter des opérations mathématiques avancées telles que :
     - Exponentiation
     - Racine carrée
     - Modulo
     - Fonctions trigonométriques (sin, cos, tan)
   
2. **Prise en charge des nombres complexes :**
   - Permettre d'ajouter et d'opérer sur des nombres complexes dans la pile.
   - Ajouter des opérations spécifiques aux nombres complexes (module, argument, etc.).

3. **Limite de la pile :**
   - Implémenter une gestion des limites sur la taille de la pile (nombre maximum d'éléments).
   - Ajouter une option pour configurer cette limite via un fichier de configuration.



## Version 2.0 : Fonctionnalités avancées et intégrations

1. **API publique :**
   - Rendre l'API publiquement disponible avec des quotas d'utilisation et des clés API.
   - Mettre en place un portail de gestion des clés API pour que les utilisateurs puissent gérer leurs accès.

2. **Intégration avec des systèmes externes :**
   - Ajouter des fonctionnalités permettant de connecter l'API à d'autres systèmes, par exemple, pour importer/exporter des piles depuis/vers des fichiers ou des bases de données externes.

3. **Mode hors ligne :**
   - Ajouter une option permettant aux utilisateurs de sauvegarder temporairement la pile dans leur navigateur (localStorage) pour l'utiliser même sans connexion réseau.
