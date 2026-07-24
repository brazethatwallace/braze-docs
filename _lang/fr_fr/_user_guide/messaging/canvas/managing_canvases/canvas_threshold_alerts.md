---
nav_title: Alertes Canvas
article_title: Alertes de seuil Canvas
page_order: 4
page_type: reference
description: "Cet article de référence explique comment configurer des alertes de seuil pour un Canvas afin d'être notifié de manière proactive lorsque les entrées d'utilisateurs ou les messages envoyés sortent de la plage attendue."
tool: Canvas
channel:
- email
- webhooks
---

# Alertes de seuil Canvas {#canvas-threshold-alerts}

> Les alertes de seuil Canvas vous informent lorsque quelque chose dans un Canvas ne se passe pas comme prévu, afin que vous puissiez détecter un parcours bloqué ou une baisse inattendue avant que cela n'affecte vos clients.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Canvas threshold alerts' %}

Définissez un seuil de volume pour les entrées d'utilisateurs ou les messages envoyés, et Braze vous notifie par e-mail ou webhook si ce seuil est franchi. Vous pouvez également créer plusieurs alertes pour le même Canvas, par exemple une alerte pour les entrées d'utilisateurs et une autre pour les messages envoyés.

Vous ne savez pas par où commencer ? [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) peut vous guider dans la configuration d'une alerte de seuil Canvas.

## Étape 1 : Créer une alerte {#step-1-create-an-alert}

Les alertes sont définies au niveau du Canvas, et vous pouvez les configurer pour les Canvas actifs comme pour les brouillons. Pour ouvrir la page **Gérer les alertes** d'un Canvas, vous pouvez :

- Aller dans **Messaging** > **Canvas**, puis sélectionner **Gérer les alertes** dans le menu contextuel d'un Canvas individuel
- Pour les Canvas actifs, ouvrir **Canvas Analytics** et sélectionner **Gérer les alertes**.

Depuis la page **Gérer les alertes**, sélectionnez **Configurer l'alerte** pour créer une nouvelle alerte.

## Étape 2 : Nommer votre alerte et sélectionner un Canvas {#step-2-name-your-alert-and-select-a-canvas}

Donnez un nom à votre alerte et confirmez le Canvas auquel elle s'applique.

![Le panneau Configurer l'alerte affichant les champs de nom de l'alerte et de nom du Canvas, un groupe de règles vide, et une barre latérale de résumé pour les règles d'alerte, la planification et les notifications.]({% image_buster /assets/img/canvas_threshold_alerts/configure_alert.png %})

## Étape 3 : Définir les règles d'alerte {#step-3-set-alert-rules}

Les règles d'alerte définissent le seuil qui déclenche une notification. Vous pouvez créer des règles à l'aide de deux indicateurs :

- **Entrées d'utilisateurs :** nombre d'utilisateurs ayant intégré le Canvas
- **Messages envoyés :** nombre de messages envoyés depuis le Canvas

Pour chaque règle, choisissez une comparaison (inférieur à ou supérieur à) et un seuil de volume. Par exemple, une règle « Entrées d'utilisateurs inférieur à 3 000 » signale un Canvas qui atteint normalement des milliers d'utilisateurs mais qui s'est soudainement arrêté — signe d'un problème d'audience ou d'entrée en amont qui mérite d'être investigué.

Vous pouvez regrouper plusieurs règles ensemble et combiner des groupes de règles avec une logique ET ou OU pour créer des conditions d'alerte plus spécifiques.

## Étape 4 : Définir la planification de l'alerte {#step-4-set-the-alert-schedule}

Définissez la fréquence à laquelle vos règles d'alerte sont vérifiées. Vous pouvez définir la fréquence de vérification de 3 à 12 heures (par incréments d'une heure), ou toutes les 24 heures. Une fois activée, une alerte continue de vérifier selon cette planification tant que l'alerte et le Canvas associé sont actifs.

## Étape 5 : Configurer les notifications {#step-5-set-up-notifications}

Choisissez qui doit être notifié lorsqu'une règle d'alerte est remplie, et comment :

- **E-mail :** ajoutez une ou plusieurs adresses e-mail de destinataires
- **Webhook :** saisissez l'URL du webhook à notifier, et ajoutez éventuellement des en-têtes de requête personnalisés requis par votre destination webhook

Vous pouvez activer l'une ou les deux méthodes de notification pour une même alerte.

![La section Notifications du panneau Configurer l'alerte, affichant les bascules E-mail et Webhook, un champ de destinataires e-mail, un champ d'URL webhook, une note sur le contenu du payload, et des champs optionnels d'en-têtes de requête.]({% image_buster /assets/img/canvas_threshold_alerts/notifications.png %})

Les alertes webhook sont utiles pour acheminer les notifications vers des plateformes externes, comme un canal Slack. Pour en savoir plus, consultez la documentation de Slack sur l'[envoi de messages à l'aide de webhooks entrants](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/). Chaque notification webhook inclut un payload contenant le nom du Canvas, l'indicateur de l'alerte, la direction du seuil, la valeur ayant déclenché l'alerte et un lien direct vers le Canvas.

## Étape 6 : Enregistrer votre alerte {#step-6-save-your-alert}

Vérifiez vos règles d'alerte, la planification et les paramètres de notification dans le panneau de résumé, puis sélectionnez **Enregistrer l'alerte**.

## Étape 7 : Activer l'alerte {#step-7-activate-the-alert}

Enregistrer une alerte ne l'active pas. Pour l'activer, accédez à la page **Gérer les alertes** et utilisez la bascule **Statut** de votre alerte. Une alerte reste active jusqu'à ce que vous la désactiviez ou que le Canvas associé ne soit plus actif. La colonne **Alertes configurées** sur la page **Canvas** affiche une icône de cloche pour tout Canvas ayant au moins une alerte enregistrée.

## Considérations {#considerations}

- **Canvas en brouillon :** vous pouvez configurer une alerte de seuil pour un Canvas encore en brouillon, mais l'alerte ne commencera à vérifier vos règles qu'une fois le Canvas lancé.