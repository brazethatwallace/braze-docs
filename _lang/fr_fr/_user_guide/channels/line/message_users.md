---
nav_title: Envoyer des messages aux utilisateurs
article_title: Envoyer des messages aux utilisateurs
page_order: 3
description: "Cet article de référence explique comment échanger avec les utilisateurs en utilisant des Campaigns et des Canvas basés sur des modèles."
page_type: reference
channel:
 - LINE
alias: /line/messaging_users/
---

# Envoyer des messages aux utilisateurs LINE {#message-line-users}

> LINE est un canal de communication bidirectionnelle. Vous pouvez aller au-delà de l'envoi de messages aux utilisateurs et engager des conversations avec eux en utilisant des Campaigns et des Canvas basés sur des modèles. Cet article couvre les détails de l'envoi de messages aux utilisateurs, notamment comment définir des mots déclencheurs pour les messages entrants et les réponses non reconnues.

Il existe plusieurs méthodes pour converser avec les utilisateurs via LINE, comme l'utilisation de mots déclencheurs LINE. Vous pouvez également utiliser des appels à l'action (CTA) pour encourager l'engagement des utilisateurs avec vos messages LINE.

## Déclencheurs basés sur les actions {#action-based-triggers}

Vous pouvez créer des Campaigns et des Canvas qui démarrent, se ramifient et comportent des modifications en cours de parcours lorsque vous recevez un message LINE entrant (un message envoyé par un utilisateur) contenant un mot déclencheur. Assurez-vous de choisir des mots déclencheurs qui correspondent à ce que vous attendez des utilisateurs.

### Campaign

Définissez vos mots déclencheurs lors de la planification d'une Campaign avec livraison par événement.

![Déclencheur basé sur les actions indiquant « Envoyer cette campagne aux utilisateurs qui ont envoyé un LINE entrant au groupe d'abonnement où le corps du message est » suivi d'un champ vide.]({% image_buster /assets/img/line/trigger_word_campaign.png %})

### Canvas

Définissez vos mots déclencheurs dans les [parcours d'actions]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/) de votre Canvas.

![Parcours d'action avec un déclencheur indiquant « Envoyer cette campagne aux utilisateurs qui ont envoyé un LINE entrant au groupe d'abonnement où le corps du message est » suivi d'un champ vide.]({% image_buster /assets/img/line/trigger_word_canvas.png %})

### Exigences {#requirements}

Chaque lettre de votre mot déclencheur doit être en majuscule lors de la création de votre Campaign ou Canvas, même si Braze n'exige pas que les mots déclencheurs entrants soient en majuscules. Par exemple, si votre mot déclencheur est « JOIN2023 », un message entrant « jOin2023 » déclenchera tout de même le Canvas ou la Campaign.

Si aucun mot déclencheur n'est spécifié, la Campaign ou le Canvas s'exécutera pour *tous* les messages LINE entrants. Cela inclut les messages dont les phrases correspondent à celles des Campaigns et Canvas actifs, auquel cas l'utilisateur recevra deux messages LINE.

## Réponses non reconnues {#unrecognized-responses}

Vous devriez inclure une option de déclenchement pour les réponses non reconnues dans les Canvas interactifs. Cela informe les utilisateurs des invites disponibles (ou mots déclencheurs) et définit leurs attentes pour le canal.

### Créer un déclencheur pour les réponses non reconnues {#creating-a-trigger-for-unrecognized-responses}

Après avoir créé des groupes d'actions pour les phrases de filtre personnalisées, ajoutez un autre groupe d'actions au parcours d'action pour **Envoyer un message LINE**, et ne cochez pas **Où le corps du message**. Cela interceptera toutes les réponses non reconnues des utilisateurs, de manière similaire à une clause « else ».

Pour ce message, vous devriez envoyer un message LINE informant l'utilisateur que ce canal n'est pas surveillé par un humain et, si nécessaire, le guider vers un canal d'assistance.