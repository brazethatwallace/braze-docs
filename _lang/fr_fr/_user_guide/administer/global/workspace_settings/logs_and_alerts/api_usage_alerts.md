---
nav_title: "Alertes relatives à l'utilisation de l'API"
article_title: "Alertes d'utilisation de l'API"
description: "Cet article fournit un aperçu des alertes d'utilisation de l'API, qui vous permettent de détecter de manière proactive tout trafic inattendu."
page_order: 0
---

# Alertes relatives à l'utilisation de l'API {#api-usage-alerts}

> Les alertes d'utilisation des API offrent une visibilité essentielle sur l'utilisation de vos API, vous permettant de détecter de manière proactive tout trafic inattendu. En configurant ces alertes pour suivre les volumes de requêtes API clés, vous pouvez recevoir des notifications en temps réel et résoudre les problèmes avant qu'ils n'aient un impact sur vos campagnes marketing.

## À propos des alertes relatives à l'utilisation de l'API {#about-api-usage-alerts}

Vous pouvez utiliser les alertes d'utilisation de l'API pour surveiller les volumes de requêtes pour les catégories suivantes :

| Catégorie d'API | Détails |
|--------------|---------|
| Endpoints de l'API REST | Suivi de l'utilisation de tous les appels API REST effectués vers le backend de Braze, tels que l'envoi de messages, la création de Campaigns ou l'exportation d'utilisateurs. |
| Requêtes d'API SDK | Suivi des requêtes API effectuées à partir des SDK Braze dans les applications clientes, telles que le déclenchement de messages in-app ou la synchronisation des données utilisateur.<br><br>_*Uniquement disponible pour les clients ayant acheté des utilisateurs actifs par mois – CY 24-25._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="About API usage alerts" }

## Création d'une alerte d'utilisation de l'API {#creating-an-api-usage-alert}

Pour créer une alerte d'utilisation de l'API :

1. Rendez-vous dans **Paramètres** > **Clés API** > **Alertes d'utilisation de l'API**, puis créez une nouvelle alerte.
2. Saisissez un nom pour votre alerte et choisissez les endpoints de l'API REST et les clés API pour lesquels vous souhaitez être alerté.
3. Définissez vos critères d'alerte en choisissant un ou plusieurs codes de réponse et en spécifiant les [seuils d'alerte](#api-usage-alert-thresholds).
4. Lorsque vous avez terminé, basculez **Alert enabled**.
    ![Exemple d'alerte d'utilisation de l'API qui envoie des notifications lorsque l'endpoint Track users augmente de 100 pour cent en une heure.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## Seuils d'alerte {#api-usage-alert-thresholds}

Lorsque vous définissez vos critères d'alerte, vous pouvez ajuster les seuils suivants :

<table aria-label="Alert thresholds #api-usage-alert-thresholds">
  <caption>Seuils d'alerte</caption>
  <thead>
    <tr>
      <th>Champ</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Condition de seuil</td>
      <td>
        Définit les conditions menant au volume seuil pour lequel vous souhaitez être alerté. Les conditions suivantes sont prises en charge :<br><br>
        <ul>
          <li><strong>Increased by</strong> ou <strong>Decreased by</strong> : compare les requêtes par rapport à la fenêtre temporelle précédente.</li>
          <li><strong>Increased by percentage</strong> ou <strong>Decreased by percentage</strong> : compare la variation en pourcentage des requêtes par rapport à la fenêtre temporelle précédente.</li>
          <li><strong>Greater than or equal</strong> ou <strong>less than or equal</strong> : compte les requêtes dans une fenêtre temporelle.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Volume seuil</td>
      <td>Utilisé conjointement avec la condition de seuil.</td>
    </tr>
    <tr>
      <td>Période</td>
      <td>La fenêtre temporelle pour l'évaluation de l'alerte.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 aria-label="Alert thresholds #api-usage-alert-thresholds" }

## Configuration des notifications d'alerte {#setting-up-alert-notifications}

Vous pouvez configurer une alerte par e-mail, une alerte par webhook, ou les deux. Les alertes par webhook sont particulièrement utiles pour des cas d'utilisation tels que l'envoi d'une alerte vers des plateformes externes, comme un canal Slack. Pour un exemple, consultez notre [documentation](https://www.braze.com/docs/user_guide/administer/global/admin_settings/notification_preferences#slack-incoming-webhook-integration) sur l'intégration des alertes avec Slack pour nos préférences de notification.

![Un e-mail sera envoyé à l'adresse sélectionnée lorsque les critères de l'alerte sont atteints.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Exemple de payload {#payload}

Voici un exemple de payload pour le corps d'un webhook d'alerte d'utilisation de l'API.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": {
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition": "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    },
    "timeframe_start": "2025-03-20T15:35:00Z",
    "timeframe_end": "2025-03-20T16:35:00Z",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20T14:35:00Z",
    "previous_timeframe_end": "2025-03-20T15:35:00Z",
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### Exemples d'alertes {#example-alerts}

Voici quelques façons de configurer vos alertes d'utilisation de l'API pour être notifié dans les scénarios suivants.

{% tabs local %}
{% tab Santé de l'API %}
Vous pouvez configurer des alertes pour surveiller l'état général de votre API. Par exemple, vous pouvez mettre en place ces alertes pour être prévenu lorsque les erreurs API augmentent de manière drastique, comme de 20 % par rapport à l'heure précédente.

| Endpoint | Clé API | Code de réponse | Condition de seuil | Volume seuil | Période |
| --- | --- | --- | --- | --- | --- |
| Tous les endpoints | Toutes les clés API | `4XX` et `5XX` | Increased by 10% | 10 | 1 heure |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Example alerts" }
{% endtab %}

{% tab Limite de débit d'un endpoint %}
Soyez alerté lorsque votre espace de travail atteint sa limite de débit pour l'endpoint `/users/track`. Vous pouvez également appliquer cette configuration à d'autres endpoints Braze.

| Endpoint | Clé API | Code de réponse | Condition de seuil | Volume seuil | Période |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Toutes les clés API | `429` | Greater than or equal to | 100 | 1 heure |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Example alerts" }
{% endtab %}

{% tab Campaigns déclenchées par API %}
Cette configuration d'alerte vous notifie lorsque des erreurs surviennent pour les Campaigns et Canvas déclenchés par API, dont certains peuvent être hautement prioritaires.

| Endpoint | Clé API | Code de réponse | Condition de seuil | Volume seuil | Période |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | Toutes les clés API | `4XX` et `5XX` | Greater than or equal to | 1 | 1 heure |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Example alerts" }
{% endtab %}

{% tab Intégrations partenaires %}
Utilisez la configuration d'alerte suivante pour être alerté lorsqu'une intégration partenaire cesse d'envoyer des données à Braze.

| Endpoint | Clé API | Code de réponse | Condition de seuil | Volume seuil | Période |
| --- | --- | --- | --- | --- | --- |
| Tous les endpoints | La clé API utilisée pour votre intégration partenaire | Tous les codes de réponse | Less than or equal to | 0 | 1 jour |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Example alerts" }
{% endtab %}
{% endtabs %}

## Considérations {#considerations}

- Chaque alerte active n'enverra qu'une seule notification par e-mail ou webhook toutes les 8 heures, afin d'éviter un trop grand nombre de notifications provenant d'une même alerte. Si votre alerte se déclenche prématurément, envisagez de modifier les critères d'alerte pour mieux correspondre à votre cas d'utilisation.
- Vous pouvez avoir jusqu'à 10 alertes par espace de travail.