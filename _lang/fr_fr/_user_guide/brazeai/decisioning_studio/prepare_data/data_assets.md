---
nav_title: Ressources de données critiques
article_title: Ressources de données critiques pour Decisioning Studio
page_order: 3
page_type: reference
description: "Cet article de référence couvre les ressources de données requises et facultatives pour BrazeAI Decisioning Studio, y compris les données de retour nécessaires pour boucler la boucle de décision automatisée par IA."
---

# Ressources de données critiques {#critical-data-assets}

> Decisioning Studio nécessite certaines ressources de données pour fonctionner et bénéficie de données facultatives supplémentaires. Cet article décrit chaque ressource, pourquoi elle est importante et quels champs sont requis.

## Boucler la boucle de décision automatisée par IA {#close-the-ai-decisioning-loop}

Les trois ressources d'événements requises (activations, engagements et conversions) forment ensemble la boucle de rétroaction qui permet à Decisioning Studio d'apprendre et de s'améliorer au fil du temps.

- **Les activations** indiquent au modèle ce qu'il a décidé de faire
- **Les engagements** indiquent au modèle comment les clients ont réagi au message
- **Les conversions** indiquent au modèle si le résultat commercial final a été atteint

Chacune de ces ressources doit être structurée sous forme de flux d'événements incrémentiel (et non un instantané). Consultez [Instantanés versus flux d'événements]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams/) pour plus de détails.

{% alert note %}
Si Decisioning Studio est nativement intégré à votre plateforme d'engagement client (comme Braze ou Salesforce Marketing Cloud), les données d'activation et d'engagement peuvent être collectées automatiquement sans configuration supplémentaire. Consultez votre documentation de configuration pour confirmer.
{% endalert %}

## Ressources requises {#required-assets}

### Profil client {#customer-profile}

Les données de profil client décrivent qui sont vos clients. Decisioning Studio utilise ces données pour comprendre l'état actuel de chaque client et générer des recommandations pertinentes.

Les attributs de profil courants incluent :

- Ancienneté en tant que client
- Géographie (lorsque cela est autorisé par votre secteur d'activité et vos exigences en matière de confidentialité)
- Canal d'acquisition (par exemple, web, téléphone, en magasin)
- Score de satisfaction ou de sentiment
- Scores dérivés de modèles (par exemple, propension à l'attrition, estimation de la valeur vie client)
- Niveau de fidélité ou adhésion à un programme

### Données d'activation et d'engagement {#activation-and-engagement-data}

Les données d'activation enregistrent ce que Decisioning Studio a réellement envoyé : quelle recommandation a été délivrée à quel client via quel canal. Les données d'engagement enregistrent ce que le client a fait en réponse : s'il a ouvert, cliqué ou interagi d'une autre manière avec le message.

Pour les intégrations natives avec Braze, les données d'activation et d'engagement peuvent être disponibles automatiquement via Braze Currents. Pour les autres configurations, ces données doivent être fournies explicitement.

Ces données sont essentielles car elles bouclent la boucle entre une recommandation et son résultat. Sans elles, le modèle ne peut pas apprendre quelles décisions fonctionnent.

### Données de conversion {#conversions-data}

Les données de conversion décrivent ce qui s'est passé pour le client après qu'une recommandation a été faite et qu'un message a été envoyé. C'est le signal principal que le modèle utilise pour évaluer si une recommandation a été réussie.

| Exigence | Raison |
|----------|--------|
| Chaque enregistrement contient l'identifiant client, cohérent avec toutes les autres ressources | Decisioning Studio doit pouvoir relier les conversions aux recommandations qui les ont précédées. |
| Chaque enregistrement possède un horodatage indiquant quand l'événement de conversion s'est produit | Un timing précis est essentiel pour l'attribution. Le modèle doit savoir à quelle recommandation une conversion peut être attribuée. |
| Si vous utilisez un indicateur de réussite non binaire (par exemple, le chiffre d'affaires plutôt que converti ou non converti), la valeur de l'indicateur doit être incluse dans chaque enregistrement de conversion | Decisioning Studio utilise la valeur de l'indicateur pour générer des expériences d'entraînement. Sans cette valeur, le modèle peut uniquement apprendre qu'une conversion a eu lieu, mais pas sa valeur. |
| Si les conversions peuvent être directement attribuées à une communication spécifique (par exemple, l'utilisation d'un coupon), incluez les champs nécessaires pour relier la conversion à l'enregistrement d'activation | L'attribution directe fournit au modèle le signal d'apprentissage le plus clair. Si l'attribution directe n'est pas possible, Decisioning Studio utilise une attribution basée sur la proximité comme solution de repli. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Données de conversion" }

## Ressources facultatives {#optional-assets}

Plus de données mènent généralement à de meilleures performances du modèle, mais cela doit être mis en balance avec l'effort d'implémentation requis. Les ressources facultatives suivantes sont couramment utiles :

### Comportement des clients {#customer-behavior}

- Historique de connexion au compte
- Type d'appareil et système d'exploitation
- Interactions avec le service client (par exemple, nombre d'appels au support, sujets abordés)
- Utilisation du produit (par exemple, heures d'utilisation par jour, fonctionnalités utilisées, catégories de contenu consultées)

### Autres transactions {#other-transactions}

- Produits achetés par date, y compris les attributs du produit
- Montants des transactions
- Canaux de transaction (par exemple, en magasin versus en ligne)
- Méthodes de paiement

### Autres engagements marketing {#other-marketing-engagement}

- Communications sortantes envoyées en dehors des recommandations de Decisioning Studio (par exemple, e-mails, SMS)
- Engagement e-mail non déclenché par Decisioning Studio (par exemple, ouvertures, clics)
- Réponses aux enquêtes (par exemple, scores Net Promoter Score, enquêtes d'engagement)
- Activité sur le web et l'application mobile (par exemple, pages consultées, produits visualisés)