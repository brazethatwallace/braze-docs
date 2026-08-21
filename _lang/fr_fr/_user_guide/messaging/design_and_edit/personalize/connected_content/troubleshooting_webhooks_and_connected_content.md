---
nav_title: Résolution des problèmes de webhooks et de contenu connecté
article_title: Résolution des problèmes de requêtes webhook et de contenu connecté
page_order: 4
description: "Diagnostiquez les erreurs de webhooks et de contenu connecté à l'aide d'un index de symptômes, de tableaux d'erreurs HTTP et de conseils sur la détection d'hôte non sain."
---

# Résolution des problèmes de requêtes webhook et de contenu connecté {#troubleshoot-webhook-and-connected-content-requests}

> Utilisez cette page pour résoudre les codes d'erreur courants liés aux webhooks et au contenu connecté. Pour la configuration, consultez [Créer un webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) et [Effectuer un appel API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call).

## Commencez ici : identifiez votre symptôme {#start-here-match-your-symptom}

Identifiez votre symptôme dans le tableau pour accéder à la section correspondante.

| Symptôme | Aller à |
| --- | --- |
| Erreur client `4XX` dans le journal d'activité des messages | [Erreurs 4XX](#4xx-errors) |
| Erreur serveur `5XX` ou délai d'attente dépassé | [Erreurs 5XX](#5xx-errors) |
| `598 Host Unhealthy` ou requêtes brièvement interrompues | [Détection d'hôte non sain](#unhealthy-host-detection) |
| Le contenu connecté s'affiche vide dans l'aperçu ou l'envoi | [Le contenu connecté ne renvoie aucun corps de réponse](#connected-content-returns-no-response-body) |
| E-mail d'erreur automatisé de Braze | [E-mails automatisés et entrées du journal d'activité des messages](#automated-emails-and-message-activity-log-entries) |
| Besoin d'événements d'échec de webhook dans Currents | [Informations supplémentaires sur les échecs dans Braze Currents](#additional-failure-insights-in-braze-currents) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptômes liés aux webhooks et au contenu connecté" }

## Parcours d'investigation standard {#standard-investigation-path}

Utilisez ce workflow lorsqu'un webhook ou une requête de contenu connecté échoue ou s'affiche incorrectement. Commencez à l'étape 1.

1. Ouvrez le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) et notez le code d'erreur, l'horodatage et l'URL de l'endpoint.
2. Pour les erreurs `4XX`, vérifiez la syntaxe de la requête, les en-têtes d'authentification, le chemin de l'URL et la méthode HTTP par rapport à la documentation de l'endpoint.
3. Pour les erreurs `5XX`, vérifiez l'état de l'endpoint, les limites de débit et si Braze a signalé l'hôte comme non sain.
4. Pour le contenu connecté, prévisualisez le message pour un utilisateur test et confirmez que le Liquid ne résout pas vers des valeurs vides ou incompatibles avec le JSON.
5. Si la détection d'hôte non sain peut être en cause, consultez la section [Détection d'hôte non sain](#unhealthy-host-detection) avant de contacter le [support Braze]({{site.baseurl}}/support_contact).

## Erreurs 4XX {#4xx-errors}

Les erreurs `4XX` indiquent un problème avec la requête envoyée à l'endpoint. Ces erreurs sont généralement causées par des requêtes erronées, notamment des paramètres mal formés, des en-têtes d'authentification manquants ou des URL incorrectes. Notez que ces erreurs s'appliquent également au [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

Consultez le tableau suivant pour obtenir les détails des codes d'erreur et les étapes de résolution :

<style>
table td {
    word-break: break-word;
}
</style>

<table aria-label="Erreurs 4XX">
  <thead>
    <tr>
      <th>Code d'erreur</th>
      <th>Signification</th>
      <th>Étapes de résolution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>400 Bad Request</b></td>
      <td>La syntaxe de la requête est invalide.</td>
      <td>
        <ul>
          <li>Vérifiez le payload de la requête pour détecter d'éventuelles erreurs de syntaxe.</li>
          <li>Confirmez que tous les champs obligatoires sont inclus et correctement formatés.</li>
          <li>Si vous envoyez un payload JSON, validez la structure JSON.</li>
          <li>Si vous utilisez Liquid pour intégrer des tags de personnalisation dans la requête webhook, vérifiez que le Liquid ne produit pas une valeur vide ou des caractères qui cassent le JSON (comme des guillemets non échappés). Prévisualisez le message pour un utilisateur test afin de confirmer que le rendu est valide.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>401 Unauthorized</b></td>
      <td>La requête nécessite une authentification de l'utilisateur.</td>
      <td>
        <ul>
          <li>Vérifiez que les identifiants d'authentification corrects (tels que les clés API ou les jetons) sont inclus dans les en-têtes de la requête.</li>
          <li>Confirmez que vous disposez des permissions utilisateur nécessaires pour accéder à l'endpoint.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 Forbidden</b></td>
      <td>L'endpoint comprend la requête mais refuse de l'autoriser.</td>
      <td>
        <ul>
          <li>Vérifiez si la clé API ou le jeton dispose des permissions requises.</li>
          <li>Confirmez que vous disposez des permissions utilisateur nécessaires pour accéder à l'endpoint.</li>
          <li>Si les requêtes renvoient systématiquement <code>403</code> et que l'authentification semble correcte, votre serveur, passerelle API ou WAF bloque peut-être les adresses IP sortantes de Braze. Ajoutez les IP de votre cluster Braze à la liste d'autorisation. Pour les webhooks, consultez <a href="{{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting">Liste d'autorisation des IP</a>. Pour le contenu connecté, consultez <a href="{{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting">Liste d'autorisation des IP pour le contenu connecté</a>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 Not Found</b></td>
      <td>L'endpoint ne trouve pas la ressource demandée.</td>
      <td>
        <ul>
          <li>Vérifiez l'URL de l'endpoint pour détecter d'éventuelles fautes de frappe ou chemins incorrects.</li>
          <li>Confirmez que la ressource à laquelle vous essayez d'accéder existe.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 Method Not Allowed</b></td>
      <td>La méthode de requête est connue par l'endpoint mais n'est pas prise en charge par la ressource cible.</td>
      <td>
        <ul>
          <li>Vérifiez la méthode HTTP (DELETE, GET, POST, PUT) utilisée dans la requête.</li>
          <li>Confirmez que l'endpoint prend en charge la méthode que vous utilisez.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 Request Timeout</b></td>
      <td>L'endpoint a expiré lors du traitement de la requête.</td>
      <td>
        <ul>
          <li>Vérifiez la méthode HTTP (DELETE, GET, POST, PUT) utilisée dans la requête.</li>
          <li>Confirmez que l'endpoint prend en charge la méthode que vous utilisez.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 Conflict</b></td>
      <td>La requête est incomplète en raison d'un conflit avec l'état actuel de la ressource.</td>
      <td>
        <ul>
          <li>Vérifiez la méthode HTTP (DELETE, GET, POST, PUT) utilisée dans la requête.</li>
          <li>Confirmez que l'endpoint prend en charge la méthode que vous utilisez.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 Too Many Requests</b></td>
      <td>Trop de requêtes ont été envoyées dans un laps de temps donné.</td>
      <td>
        <ul>
          <li>Réduisez la limite de débit de votre Campaign ou de votre étape Canvas.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Erreurs 5XX {#5xx-errors}

Les erreurs `5XX` indiquent un problème au niveau de l'endpoint. Ces erreurs sont généralement causées par des problèmes côté serveur.

| Code d'erreur                 | Signification                                                                                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **500 Internal Server Error** | L'endpoint a rencontré une condition inattendue qui l'a empêché de traiter la requête.                                                               |
| **502 Bad Gateway**           | L'endpoint a reçu une réponse invalide du serveur en amont.                                                                                          |
| **503 Service Unavailable**   | L'endpoint est actuellement incapable de traiter la requête en raison d'une surcharge temporaire ou d'une maintenance.                                |
| **504 Gateway Timeout**       | L'endpoint n'a pas reçu de réponse dans les délais impartis de la part du serveur en amont.                                                          |
| **529 Host Overloaded**       | L'hôte de l'endpoint est surchargé et n'a pas pu répondre. |
| **598 Host Unhealthy**        | Braze a simulé la réponse car l'hôte de l'endpoint est temporairement marqué comme non sain. Pour plus d'informations, consultez [Détection d'hôte non sain](#unhealthy-host-detection). |
| **599 Connection Error**      | Braze a rencontré une erreur de délai de connexion réseau en essayant d'établir une connexion avec l'endpoint, ce qui signifie que l'endpoint peut être instable ou indisponible. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erreurs 5XX" }

### Résoudre les erreurs 5XX {#resolving-5xx-errors}

Voici des conseils pour résoudre les erreurs `5XX` courantes :

- Consultez le message d'erreur pour obtenir des détails spécifiques disponibles dans le **Journal d'activité des messages**. Pour les webhooks, accédez à la section **Performance Over Time** sur la page d'accueil de Braze et sélectionnez les statistiques pour les webhooks. Vous pourrez y trouver l'horodatage indiquant le moment où les erreurs se sont produites.
- Assurez-vous de ne pas envoyer trop de requêtes qui surchargent l'endpoint. Vous pouvez envoyer par lots ou ajuster la limite de débit pour vérifier si cela réduit les erreurs.

## Détection d'hôte non sain {#unhealthy-host-detection}

Les webhooks et le contenu connecté de Braze utilisent un mécanisme de détection d'hôte non sain pour détecter lorsque l'hôte cible connaît un taux élevé de lenteurs significatives ou de surcharges entraînant des délais d'expiration, un trop grand nombre de requêtes ou d'autres résultats empêchant Braze de communiquer avec l'endpoint cible. Ce mécanisme agit comme une protection pour réduire la charge inutile qui peut causer des difficultés à l'hôte cible. Il sert également à stabiliser l'infrastructure de Braze et à maintenir des vitesses d'envoi de messages rapides.

Les seuils de détection diffèrent entre les webhooks et le contenu connecté :
- **Pour les webhooks** : si le nombre d'échecs dépasse 3 000 dans une fenêtre glissante d'une minute (par combinaison unique de nom d'hôte et de groupe d'applications&#8212;pas par chemin d'endpoint), Braze interrompt temporairement les requêtes vers l'hôte cible pendant une minute.
- **Pour le contenu connecté** : si le nombre d'échecs dépasse 3 000 ET que le taux d'erreur dépasse 90 % dans une fenêtre glissante d'une minute (par combinaison unique de nom d'hôte et de groupe d'applications&#8212;pas par chemin d'endpoint), Braze interrompt temporairement les requêtes vers l'hôte cible pendant une minute.

Lorsque les requêtes sont interrompues, Braze simule des réponses avec un code d'erreur `598` pour indiquer le mauvais état de santé. Après une minute, Braze reprend les requêtes à pleine vitesse si l'hôte est considéré comme sain. Si l'hôte est toujours non sain, Braze attend une minute supplémentaire avant de réessayer.

Les codes d'erreur suivants contribuent au compteur d'échecs du détecteur d'hôte non sain : `408`, `429`, `502`, `503`, `504`, `529`.

Pour les webhooks, Braze réessaie automatiquement les requêtes HTTP qui ont été interrompues par le détecteur d'hôte non sain. Cette nouvelle tentative automatique utilise des délais exponentiels et ne réessaie que quelques fois avant d'échouer. Pour plus d'informations sur les erreurs de webhook, consultez [Erreurs, logique de nouvelle tentative et délais d'expiration]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#errors-retry-logic-and-timeouts).

Pour le contenu connecté, si les requêtes vers l'hôte cible sont interrompues par le détecteur d'hôte non sain, Braze continue de rendre les messages et de suivre votre logique Liquid comme s'il avait reçu un code de réponse d'erreur. Si vous souhaitez vous assurer que ces requêtes de contenu connecté sont réessayées lorsqu'elles sont interrompues par le détecteur d'hôte non sain, utilisez l'option `:retry`. Pour plus d'informations sur l'option `:retry`, consultez [Nouvelles tentatives de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries).

Si vous pensez que la détection d'hôte non sain cause des problèmes, contactez l'[assistance Braze]({{site.baseurl}}/support_contact).

### Le contenu connecté ne renvoie aucun corps de réponse {#connected-content-returns-no-response-body}

**Symptôme :** un appel de contenu connecté s'affiche vide dans la prévisualisation ou l'envoi de votre message.

Si un appel de contenu connecté s'affiche vide dans la prévisualisation ou l'envoi de votre message, vérifiez les points suivants :

- **Espaces insécables dans l'URL :** Braze supprime les espaces insécables (`&nbsp;` ou Unicode `U+00A0`) des URL de contenu connecté avant d'effectuer la requête. Si votre URL a été copiée depuis un document ou un champ du tableau de bord qui a inséré des espaces insécables entre les caractères, la requête peut échouer ou ne renvoyer aucun corps exploitable. Retapez l'URL en texte brut ou supprimez les espaces masqués, puis prévisualisez à nouveau.
- **Réponses de redirection (`3xx`) :** le contenu connecté ne suit pas les redirections. Seules les réponses `2xx` sont considérées comme réussies, de sorte qu'une réponse `301` ou `302` peut s'afficher vide même lorsque la même URL fonctionne dans Postman. Utilisez l'URL de destination finale ou configurez l'endpoint pour renvoyer une réponse `2xx` (généralement `200`) à l'URL appelée par Braze. Consultez [Pourquoi le contenu connecté échoue-t-il lorsque mon endpoint renvoie une redirection ?]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#why-does-connected-content-fail-when-my-endpoint-returns-a-redirect-301-or-302).
- **Erreurs HTTP et corps vides :** pour les codes de statut en dehors de la plage `2xx` ou les hôtes bloqués, le contenu connecté peut renvoyer une chaîne vide. Consultez [Effectuer un appel API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) et examinez les échecs dans le **Journal d'activité des messages**.

## E-mails automatisés et entrées du journal d'activité des messages {#automated-emails-and-message-activity-log-entries}

### Configuration des e-mails automatisés {#setting-up-automated-emails}

Si vous rencontrez plus de 100 000 erreurs d'endpoint webhook ou de contenu connecté (y compris les nouvelles tentatives) dans un espace de travail sur une période de 24 heures, Braze vous envoie un e-mail contenant les informations suivantes pour résoudre les erreurs.

- Nom de l'espace de travail
- Un lien vers le Canvas ou la campagne
- URL de l'endpoint
- Code d'erreur
- Heure de la dernière observation de l'erreur
- Liens vers le journal d'activité des messages et la documentation associée

{% alert note %}
Vous pouvez configurer le seuil d'erreur par espace de travail. Pour ajuster ce seuil, contactez l'[assistance Braze]({{site.baseurl}}/support_contact).
{% endalert %}

Les erreurs d'endpoint sont :

- **`4XX` :** `400`, `401`, `403`, `404`, `405`, `408`, `409`, `429`
- **`5XX` :** `500`, `502`, `503`, `504`, `598`, `599`

Ces e-mails ne sont envoyés qu'une fois par jour au niveau de l'espace de travail. Si aucun utilisateur ne s'inscrit pour recevoir ces e-mails, Braze notifie tous les administrateurs de la société.

Pour vous inscrire afin de recevoir ces e-mails, procédez comme suit :

1. Accédez à **Paramètres** > **Paramètres d'administration** > **Préférences de notification**.
2. Sélectionnez **Connected Content Errors** et **Webhook Errors** dans la section **Canvas & Campaigns**.

### Entrées du journal d'activité des messages {#message-activity-log-entries}

En cas d'échec, il y a au moins une entrée dans le [Journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) qui y est liée. Si la requête est réessayée et finit par réussir, ces détails sont disponibles dans Currents et le partage de données Snowflake. Notez que même si une requête finit par réussir après une nouvelle tentative, les erreurs peuvent toujours déclencher l'e-mail automatisé.

### Informations supplémentaires sur les échecs dans Braze Currents {#additional-failure-insights-in-braze-currents}

Pour accroître la transparence sur les problèmes liés aux webhooks, Braze diffuse des événements détaillés d'échec de webhook vers Currents et le partage de données Snowflake. Ces événements incluent les requêtes webhook échouées (telles que les réponses HTTP `4xx` ou `5xx`), offrant une meilleure observabilité sur la manière dont les problèmes de webhook peuvent affecter la distribution des messages. Notez que les événements d'échec incluent à la fois les erreurs terminales et les erreurs en cours de nouvelle tentative.

{% alert note %}
Les requêtes de contenu connecté ne sont pas incluses dans ces événements d'échec de webhook.
{% endalert %}

Pour plus d'informations, consultez le [Glossaire des événements d'engagement liés aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).