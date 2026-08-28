---
nav_title: Transformation des données
hidden: true
---

# Transformation des données Braze {#braze-data-transformation}

> La [Transformation des données]({{site.baseurl}}/data_transformation) de Braze peut ingérer un webhook depuis une plateforme partenaire et permettre à un client de définir un mappage pour convertir le payload de ce webhook en données utilisateur souhaitées, telles que les attributs, les événements ou les achats sur les profils utilisateur de Braze.

## À quoi ressemblerait une intégration basée sur la Transformation des données {#what-a-data-transformation-based-integration-would-look-like}

Une intégration partenaire basée sur la fonctionnalité de Transformation des données pourrait prendre la forme d'un modèle de code de transformation partagé avec les clients via une documentation publique.

Pour les clients communs, cela ressemblerait à quelque chose comme ceci :

1. Ils se connectent à votre plateforme et configurent les webhooks.
2. Ils travaillent avec leur équipe Braze pour obtenir l'accès à la Transformation des données Braze et créer une nouvelle transformation dans leur tableau de bord de Braze.
3. L'URL générée par la transformation est copiée.
4. De retour dans Braze, ils envoient un webhook de test à l'URL de transformation copiée.
5. Dans Braze, ils copient et collent le modèle de code de transformation.
6. Ils activent la transformation.
7. Une fois activée, ils peuvent vérifier via l'outil de recherche d'utilisateurs de Braze que le profil utilisateur est mis à jour en fonction du webhook, et modifier le code de transformation selon leurs besoins.

{% alert tip %}
Il est recommandé de créer une transformation par type de webhook envoyé à Braze lors de l'élaboration d'exemples de code de transformation.
{% endalert %}