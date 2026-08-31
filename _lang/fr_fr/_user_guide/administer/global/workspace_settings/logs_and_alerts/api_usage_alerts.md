---
nav_title: "Alertes relatives à l'utilisation de l'API"
article_title: "Alertes d'utilisation de l'API"
description: "Cet article fournit un aperçu des alertes d'utilisation de l'API, qui vous permettent de détecter de manière proactive tout trafic inattendu."
page_order: 0
---

# Alertes relatives à l'utilisation de l'API {#api-usage-alerts}

> Les alertes d'utilisation des API offrent une visibilité essentielle sur l'utilisation de vos API, vous permettant de détecter de manière proactive tout trafic inattendu. En configurant ces alertes pour suivre les volumes de requêtes API clés, vous pouvez recevoir des notifications en temps réel et résoudre les problèmes avant qu'ils n'aient un impact sur vos campagnes marketing.

## À propos des alertes d'utilisation de l'API {#about-api-usage-alerts}

Vous pouvez utiliser les alertes d'utilisation de l'API pour surveiller les volumes de requêtes dans les catégories suivantes :

| Catégorie d'API | Détails |
|--------------|---------|
| Endpoints REST API | Suit l'utilisation de tous les appels REST API effectués vers le backend de Braze, tels que l'envoi de messages, la création de Campaigns ou l'exportation d'utilisateurs. |
| Requêtes API du SDK | Suit les requêtes API effectuées depuis les SDK Braze dans les applications clientes, telles que le déclenchement de messages in-app ou la synchronisation des données utilisateur.<br><br>_*Uniquement disponible pour les clients ayant acheté le forfait Utilisateurs actifs mensuels – CY 24-25._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="À propos des alertes d'utilisation de l'API" }

## Créer une alerte d'utilisation de l'API {#creating-an-api-usage-alert}

Pour créer une alerte d'utilisation de l'API :

1. Accédez à **Paramètres** > **API et identifiants** > **Alertes d'utilisation de l'API**, puis créez une nouvelle alerte.
2. Saisissez un nom pour votre alerte et choisissez les endpoints REST API et les clés API pour lesquels vous souhaitez être alerté.
3. Définissez vos critères d'alerte en choisissant un ou plusieurs codes de réponse et en spécifiant les [seuils d'alerte](#api-usage-alert-thresholds).
4. Lorsque vous avez terminé, activez **Alert enabled**.
    ![Exemple d'alerte d'utilisation de l'API qui envoie des notifications lorsque l'endpoint Track users augmente de 100 pour cent en une heure.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## Seuils d'alerte {#api-usage-alert-thresholds}

Lorsque vous définissez vos critères d'alerte, vous pouvez ajuster les seuils suivants :

<table aria-label="Seuils d'alerte">
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Seuils d'alerte" }

## Configuration des notifications d'alerte {#setting-up-alert-notifications}

Vous pouvez configurer une alerte par e-mail, une alerte par webhook, ou les deux. Les alertes par webhook peuvent être très utiles pour des cas d'usage tels que l'envoi d'une alerte vers des plateformes externes, comme un canal Slack. Pour un exemple, consultez notre [documentation]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) sur l'intégration des alertes avec Slack pour nos préférences de notification.

![Un e-mail sera envoyé à l'adresse sélectionnée lorsque les critères de l'alerte sont atteints.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Exemple de payload {#payload}

Voici un exemple de payload pour le corps d'un webhook d'alerte d'utilisation de l'API.

```json
{
  "text": "Your My First API Usage Alert alert has triggered. Please note that this alert is reset every 8 hours, and only one notification will be sent per reset period. You can view your alert and usage here: <link>.",
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "app_group_name": "My Workspace",
    "alert_criteria": {
      "response_codes": "201, 202 and 203",
      "threshold_condition": "increase by",
      "threshold_volume": "50%",
      "within": "1 hour"
    },
    "timeframe_start": "2025-03-20 15:35:00",
    "timeframe_end": "2025-03-20 16:35:00",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20 14:35:00",
    "previous_timeframe_end": "2025-03-20 15:35:00",
    "previous_volume": 1000
  }
}
```

{% alert note %}
Les champs `previous_timeframe_start`, `previous_timeframe_end` et `previous_volume` sont facultatifs et n'apparaissent que lorsque l'alerte utilise une condition de seuil comparative (`increase by`, `decrease by`). Ces champs sont omis pour les alertes `greater than or equal` ou `less than or equal`.
{% endalert %}

#### Détails des champs du payload {#payload-field-details}

| Champ | Type | Description |
|-------|------|-------------|
| `text` | chaîne de caractères | Message d'alerte lisible par un humain. |
| `data.alert_name` | chaîne de caractères | Nom de l'alerte. |
| `data.alert_type` | chaîne de caractères | Type d'alerte (toujours `"API Usage Alert"`). |
| `data.app_group_name` | chaîne de caractères | Nom de l'espace de travail. |
| `data.alert_criteria.response_codes` | chaîne de caractères | Codes de réponse sélectionnés pour l'alerte. Renvoie `"all response codes"` si aucun n'est sélectionné, un code unique comme `"201"`, ou plusieurs codes comme `"201, 202 and 203"`. |
| `data.alert_criteria.threshold_condition` | chaîne de caractères | Type de condition : `"increase by"`, `"decrease by"`, `"greater than or equal"` ou `"less than or equal"`. |
| `data.alert_criteria.threshold_volume` | chaîne de caractères ou nombre | Valeur du seuil. Lorsque la condition utilise un pourcentage, il s'agit d'une chaîne de caractères se terminant par `%` (par exemple, `"50%"`). Lorsque la condition utilise une valeur numérique, il s'agit d'un nombre (par exemple, `50`). |
| `data.alert_criteria.within` | chaîne de caractères | Fenêtre temporelle pour l'évaluation de l'alerte (par exemple, `"1 day"`). |
| `data.timeframe_start` | chaîne de caractères | Début de la période de l'alerte au format UTC `YYYY-MM-DD HH:MM:SS`. |
| `data.timeframe_end` | chaîne de caractères | Fin de la période de l'alerte au format UTC `YYYY-MM-DD HH:MM:SS`. |
| `data.volume` | nombre | Volume de requêtes pendant la période de l'alerte. |
| `data.previous_timeframe_start` | chaîne de caractères | (Facultatif) Début de la période précédente. Présent uniquement pour les conditions de seuil comparatives. |
| `data.previous_timeframe_end` | chaîne de caractères | (Facultatif) Fin de la période précédente. Présent uniquement pour les conditions de seuil comparatives. |
| `data.previous_volume` | nombre | (Facultatif) Volume de requêtes pendant la période précédente. Présent uniquement pour les conditions de seuil comparatives. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Détails des champs du payload" }

### Exemples d'alertes {#example-alerts}

Voici quelques façons de configurer vos alertes d'utilisation de l'API pour être notifié dans les scénarios suivants.

{% tabs local %}
{% tab Santé de l'API %}
Vous pouvez configurer des alertes pour surveiller l'état général de votre API. Par exemple, vous pouvez configurer ces alertes lorsque les erreurs API augmentent de façon drastique, comme de 20 % par rapport à l'heure précédente.

| Endpoint | Clé API | Code de réponse | Condition de seuil | Volume du seuil | Dans |
| --- | --- | --- | --- | --- | --- |
| Tous les endpoints | Toutes les clés API | `4XX` et `5XX` | Augmentation de 10 % | 10 | 1 heure |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Exemples d'alertes" }
{% endtab %}

{% tab Limite de débit d'endpoint %}
Soyez alerté lorsque votre espace de travail atteint sa limite de débit pour l'endpoint `/users/track`. Vous pouvez également appliquer cette configuration à d'autres endpoints Braze.

| Endpoint | Clé API | Code de réponse | Condition de seuil | Volume du seuil | Dans |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Toutes les clés API | `429` | Supérieur ou égal à | 100 | 1 heure |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Exemples d'alertes" }
{% endtab %}

{% tab Campaigns déclenchées par API %}
Cette configuration d'alerte vous notifie lorsque des erreurs surviennent pour les Campaigns et Canvas déclenchés par API, dont certains peuvent être de haute priorité.

| Endpoint | Clé API | Code de réponse | Condition de seuil | Volume du seuil | Dans |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | Toutes les clés API | `4XX` et `5XX` | Supérieur ou égal à | 1 | 1 heure |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Exemples d'alertes" }
{% endtab %}

{% tab Intégrations partenaires %}
Utilisez la configuration d'alerte suivante pour être alerté lorsqu'une intégration partenaire cesse d'envoyer des données à Braze.

| Endpoint | Clé API | Code de réponse | Condition de seuil | Volume du seuil | Dans |
| --- | --- | --- | --- | --- | --- |
| Tous les endpoints | La clé API utilisée pour votre intégration partenaire | Tous les codes de réponse | Inférieur ou égal à | 0 | 1 jour |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Exemples d'alertes" }
{% endtab %}
{% endtabs %}

## Considérations {#considerations}

- Chaque alerte active n'enverra qu'un seul e-mail ou une seule notification webhook toutes les 8 heures. Cela permet d'éviter un nombre excessif de notifications provenant d'une même alerte. Si votre alerte vous notifie prématurément, envisagez de modifier les critères de l'alerte pour mieux correspondre à votre cas d'usage.
- Vous pouvez avoir jusqu'à 10 alertes par espace de travail.