---
nav_title: "Gérer les numéros de téléphone inconnus"
article_title: "Gérer les numéros de téléphone inconnus"
description: "Cet article de référence explique comment Braze gère les numéros de téléphone inconnus pour les utilisateurs WhatsApp."
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# Gérer les numéros de téléphone inconnus {#handle-unknown-phone-numbers}

> Il est possible qu'après avoir mis en place WhatsApp avec Braze, vous receviez des messages d'utilisateurs inconnus. Les étapes suivantes décrivent comment un utilisateur et un numéro non identifiés sont traités.

## Flux d'abonnement/désabonnement et de mots-clés personnalisés pour les numéros inconnus {#opt-inout-and-custom-keyword-workflow-for-unknown-numbers}

Braze tente d'abord de trouver un utilisateur avec un numéro correspondant. Si aucun n'est trouvé, Braze traite automatiquement un numéro inconnu de l'une des deux manières suivantes :

1. **Si un mot déclencheur avec un [Canvas d'abonnement]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) est configuré :**
- Braze crée un profil anonyme
- Un alias d'utilisateur est affecté au profil avec les détails suivants :
  - Un `alias_name` dont la valeur est le numéro de téléphone fourni par l'utilisateur
  - Un `alias_label` dont la valeur est `phone`
- Le système définit l'attribut de téléphone
- L'utilisateur est abonné au groupe d'abonnement correspondant en fonction de la logique configurée dans le Canvas<br><br>
2. **Si aucun Canvas d'abonnement n'est configuré :**
- Braze crée un profil anonyme
- Un alias d'utilisateur est affecté au profil avec les détails suivants :
  - Un `alias_name` dont la valeur est le numéro de téléphone fourni par l'utilisateur
  - Un `alias_label` dont la valeur est `phone`
- Le système définit l'attribut de téléphone
- L'état d'abonnement de l'utilisateur est par défaut `unsubscribed` pour tous les groupes d'abonnement WhatsApp<br><br>