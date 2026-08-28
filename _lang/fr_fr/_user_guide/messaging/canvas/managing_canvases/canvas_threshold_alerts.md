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

Définissez un seuil de volume ou de pourcentage pour les entrées d'utilisateurs ou les messages envoyés, et Braze vous notifie par e-mail ou webhook si ce seuil est franchi. Vous pouvez également créer plusieurs alertes pour le même Canvas, par exemple une alerte pour les entrées d'utilisateurs et une autre pour les messages envoyés.

Vous ne savez pas par où commencer ? [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) peut vous guider dans la configuration d'une alerte de seuil Canvas.

## Étape 1 : Créer une alerte {#step-1-create-an-alert}

Les alertes sont configurées au niveau du Canvas, et vous pouvez les paramétrer pour les Canvas actifs comme pour les brouillons. Pour ouvrir la page **Gérer les alertes** d'un Canvas, vous pouvez soit :

- Aller dans **Messaging** > **Canvas**, et sélectionner **Gérer les alertes** depuis le menu contextuel d'un Canvas individuel
- Pour les Canvas actifs, ouvrir **Canvas Analytics** et sélectionner **Gérer les alertes**.

Depuis la page **Gérer les alertes**, sélectionnez **Configurer une alerte** pour créer une nouvelle alerte.

## Étape 2 : Nommer votre alerte et sélectionner un Canvas {#step-2-name-your-alert-and-select-a-canvas}

Donnez un nom à votre alerte et confirmez le Canvas auquel elle s'applique.

![Le panneau Configurer l'alerte affichant les champs de nom de l'alerte et de nom du Canvas, un groupe de règles vide et une barre latérale récapitulative pour les règles d'alerte, la planification et les notifications.]({% image_buster /assets/img/canvas_threshold_alerts/configure_alert.png %})

## Étape 3 : Définir les règles d'alerte {#step-3-set-alert-rules}

Les règles d'alerte définissent le seuil qui déclenche une notification. Vous pouvez créer des règles à l'aide de deux indicateurs :

- **Entrées d'utilisateurs :** Nombre d'utilisateurs ayant accédé au Canvas
- **Messages envoyés :** Nombre de messages envoyés depuis le Canvas

Pour chaque règle, choisissez une comparaison (inférieur à, supérieur à, inférieur ou égal à, supérieur ou égal à, ou égal à), une unité et un seuil.

- **Volume :** Compare le nombre absolu dans la fenêtre de vérification en cours. Par exemple, « Entrées d'utilisateurs inférieur à 3 000 » signale un Canvas qui atteint normalement des milliers d'utilisateurs mais qui s'est soudainement arrêté, signe d'un problème en amont lié à l'audience ou à l'entrée qui mérite d'être investigué.
- **Pourcentage :** Compare le nombre actuel à une référence pour ce Canvas. La référence est la moyenne de la même fenêtre temporelle sur les 7 jours précédents. Par exemple, si l'alerte vérifie toutes les 3 heures, une vérification de 14 h à 17 h est comparée à la moyenne des sept fenêtres précédentes de 14 h à 17 h. Une règle « Messages envoyés inférieur à 50 % » signale une baisse à moins de la moitié du volume habituel.

Les seuils sont des nombres entiers. Pour les règles de pourcentage avec **inférieur à** ou **inférieur ou égal à**, saisissez une valeur de 1 à 100. Pour **supérieur à**, **supérieur ou égal à** ou **égal à**, le pourcentage peut être de 0 ou plus, y compris des valeurs supérieures à 100, afin que vous puissiez alerter sur un pic par rapport à la référence.

Vous pouvez regrouper plusieurs règles ensemble, y compris en combinant des règles de volume et de pourcentage, et combiner des groupes de règles avec une logique ET ou OU pour créer des conditions d'alerte plus spécifiques.

## Étape 4 : Définir la planification de l'alerte {#step-4-set-the-alert-schedule}

Définissez la fréquence à laquelle vos règles d'alerte sont vérifiées. Vous pouvez régler la fréquence de vérification entre 3 et 12 heures (par incréments d'une heure), ou toutes les 24 heures. Une fois activée, une alerte continue d'être vérifiée selon cette planification tant que l'alerte et le Canvas associé sont actifs.

## Étape 5 : Configurer les notifications {#step-5-set-up-notifications}

Choisissez qui doit être notifié lorsqu'une règle d'alerte est déclenchée, et comment :

- **E-mail :** Ajoutez une ou plusieurs adresses e-mail de destinataires
- **Webhook :** Saisissez l'URL du webhook à notifier, et ajoutez éventuellement des en-têtes de requête personnalisés requis par votre destination webhook

Vous pouvez activer l'une ou les deux méthodes de notification pour une même alerte.

Les alertes webhook sont utiles pour acheminer les notifications vers des plateformes externes, comme un canal Slack. Pour en savoir plus, consultez la documentation de Slack sur l'[envoi de messages à l'aide de webhooks entrants](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/). Chaque notification webhook envoie un payload JSON contenant le nom de l'alerte, la fenêtre d'évaluation et les conditions qui ont déclenché l'alerte. Chaque condition inclut un `threshold_unit` de type `volume` ou `percentage`. Les conditions de pourcentage incluent également `percentage_metric_value` (le nombre observé en tant que pourcentage entier de la référence). `metric_value` correspond toujours au nombre absolu.

### Exemple de payload webhook {#example-webhook-payload}

Voici un exemple de payload JSON envoyé dans une requête POST à votre endpoint webhook lorsqu'une alerte est déclenchée. La première condition est une règle de volume. La seconde est une règle de pourcentage : 51 235 messages envoyés, soit 57 % de la référence sur la même fenêtre de 7 jours, par rapport à un seuil supérieur à 55 %.

```json
{
  "alert": {
    "name": "Canvas Alert - August 6, 2026",
    "target_type": "CANVAS"
  },
  "evaluation_window_start": "2026-08-06T10:28:01Z",
  "evaluation_window_end": "2026-08-06T13:28:01Z",
  "conditions": [
    {
      "subject": "user_entries",
      "operator": "lt",
      "threshold_value": 500,
      "metric_value": 0.0,
      "group_index": 0,
      "threshold_unit": "volume"
    },
    {
      "subject": "messages_sent",
      "operator": "gt",
      "threshold_value": 55,
      "metric_value": 51235.0,
      "group_index": 0,
      "threshold_unit": "percentage",
      "percentage_metric_value": 57
    }
  ]
}
```

## Étape 6 : Enregistrer votre alerte {#step-6-save-your-alert}

Vérifiez les règles de votre alerte, la planification et les paramètres de notification dans le panneau de résumé, puis sélectionnez **Save alert**.

## Étape 7 : Activer l'alerte {#step-7-activate-the-alert}

L'enregistrement d'une alerte ne l'active pas. Pour l'activer, accédez à la page **Manage Alerts** et utilisez le basculeur **Status** pour votre alerte. Une alerte reste active jusqu'à ce que vous la désactiviez ou jusqu'à ce que le Canvas associé ne soit plus actif. La colonne **Alerts Configured** sur la page **Canvas** affiche une icône de cloche pour tout Canvas ayant au moins une alerte enregistrée.

## Considérations {#considerations}

- **Canvas en brouillon :** Vous pouvez configurer une alerte de seuil pour un Canvas encore en brouillon, mais l'alerte ne commencera à vérifier vos règles qu'une fois le Canvas lancé.
- **Référence de pourcentage :** Les règles de pourcentage nécessitent sept jours complets de la même fenêtre temporelle après le lancement du Canvas. Tant que ces fenêtres n'existent pas, ou lorsque la moyenne de référence est nulle (aucune activité dans les fenêtres précédentes), les règles de pourcentage ne déclenchent pas de notification.