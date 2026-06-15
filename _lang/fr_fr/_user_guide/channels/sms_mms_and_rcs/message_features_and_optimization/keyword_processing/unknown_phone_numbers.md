---
nav_title: Gérer les numéros de téléphone inconnus
article_title: Gérer les numéros de téléphone inconnus
page_order: 3
description: "Cet article de référence explique comment Braze traite les numéros de téléphone inconnus provenant de nouveaux utilisateurs."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# Gérer les numéros de téléphone inconnus - nouveaux utilisateurs {#handle-unknown-phone-numbers-new-users}

> Il est possible qu'après avoir mis en place les SMS, MMS et RCS avec Braze, vous receviez des messages de la part d'utilisateurs inconnus. Les étapes suivantes décrivent comment un utilisateur et un numéro non identifiés sont traités.

## Flux d'abonnement/désabonnement et de mots-clés personnalisés pour les numéros inconnus {#opt-inout-and-custom-keyword-workflow-for-unknown-numbers}

Braze traite automatiquement un numéro inconnu de l'une des trois manières suivantes :

1. Si un mot-clé d'abonnement est envoyé par SMS :
  * Braze crée un profil anonyme
  * Notre système définit l'attribut de téléphone
  * L'utilisateur est abonné au groupe d'abonnement correspondant en fonction du mot-clé d'abonnement reçu par Braze.<br><br>
2. Si un mot-clé de désabonnement est envoyé par SMS :
  * Braze crée un profil anonyme
  * Notre système définit l'attribut de téléphone
  * L'utilisateur est désabonné du groupe d'abonnement correspondant en fonction du mot-clé de désabonnement reçu par Braze.<br><br>
3. Si tout autre mot-clé personnalisé est envoyé par SMS :
  * Braze ignore le message et ne fait rien.