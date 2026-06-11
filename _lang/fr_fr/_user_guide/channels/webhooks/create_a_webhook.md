---
nav_title: Créer un webhook
article_title: Créer un webhook
page_order: 1
channel:
  - webhooks
description: "Cet article de référence explique comment créer et configurer une campagne webhook."
search_rank: 2
---

# Créer une campagne webhook {#create-a-webhook-campaign}

> La création d'une campagne webhook ou l'inclusion d'un webhook dans une campagne multicanale vous permet de déclencher des actions hors application en fournissant à d'autres systèmes et applications des informations en temps réel.

Vous pouvez utiliser les webhooks pour envoyer des informations à des systèmes tels que Salesforce ou Marketo, ou à vos systèmes backend. Par exemple, vous pourriez vouloir créditer les comptes de vos clients d'une promotion après qu'ils ont effectué un événement personnalisé un certain nombre de fois.

{% alert tip %}
Pour en savoir plus sur les webhooks et comment les utiliser dans Braze, consultez [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks/) avant de continuer.
{% endalert %}

## Étape 1 : Choisir où créer votre message {#step-1-choose-where-to-build-your-message}

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont plus adaptées aux envois de messages ciblés uniques, tandis que les Canvas sont plus adaptés aux parcours utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

**Étapes :**

1. Allez dans **Messaging** > **Campaigns** et sélectionnez **Create Campaign**.
2. Sélectionnez **Webhook** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multichannel**.
3. Donnez à votre campagne un nom clair et significatif.
4. (Facultatif) Ajoutez une description pour expliquer comment cette campagne sera utilisée.
4. Ajoutez des [équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) et des [étiquettes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) selon vos besoins.
   * Les étiquettes facilitent la recherche de vos campagnes et la création de rapports. Par exemple, lorsque vous utilisez le [Générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder/), vous pouvez filtrer par étiquettes spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différents modèles de webhook pour chacune de vos variantes ajoutées. Pour en savoir plus sur ce sujet, consultez [Test multivarié et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% alert tip %}
Si tous les messages de votre campagne sont similaires ou ont le même contenu, rédigez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copy from Variant** dans le menu déroulant **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Étapes :**

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) à l'aide du compositeur Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le générateur Canvas. Donnez à votre étape un nom clair et significatif.
3. Choisissez une [planification d'étape]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#schedule-your-canvas-step) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape selon vos besoins. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience seront vérifiées après le délai, au moment de l'envoi des messages.
5. Choisissez votre [comportement d'avancement]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#advancement-behavior).
6. Choisissez tout autre canal de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Créer votre webhook {#step-2-build-your-webhook}

Vous pouvez choisir de créer un webhook à partir de zéro, d'utiliser un modèle existant ou d'utiliser l'un de nos modèles prédéfinis. Ensuite, créez votre webhook dans l'onglet **Compose** de l'éditeur.

L'onglet **Compose** comprend les champs suivants :

- Langue
- URL du webhook
- Méthode HTTP
- Corps de la requête

![L'onglet « Compose » avec un exemple de modèle de webhook.]({% image_buster /assets/img_archive/webhook_compose.png %})

#### Langue {#internationalization}

L'[internationalisation]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/#campaigns-in-multiple-languages) est prise en charge dans l'URL et le corps de la requête. Pour internationaliser votre message, sélectionnez **Add languages** et remplissez les champs requis.

Nous vous recommandons de sélectionner vos langues avant de rédiger votre contenu afin de pouvoir insérer votre texte aux emplacements appropriés dans le Liquid. Pour consulter notre liste complète des langues disponibles, reportez-vous à [Langues prises en charge]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

Si vous ajoutez du texte dans une langue qui s'écrit de droite à gauche, notez que l'apparence finale des messages de droite à gauche dépend en grande partie de la façon dont les fournisseurs de services les affichent. Pour les bonnes pratiques de rédaction de messages de droite à gauche qui s'affichent aussi fidèlement que possible, consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/).

#### URL du webhook {#webhook-url}

L'URL du webhook, ou URL HTTP, spécifie votre endpoint. L'endpoint est l'endroit où vous enverrez les informations que vous capturez dans le webhook.

Si vous souhaitez envoyer des informations à un fournisseur, celui-ci doit fournir cette URL dans sa documentation API. Si vous envoyez des informations à vos propres systèmes, vérifiez auprès de votre équipe de développement ou d'ingénierie que vous utilisez la bonne URL.

Braze n'autorise que les URL qui communiquent via les ports standard `80` (HTTP) et `443` (HTTPS).

##### Utiliser Liquid {#using-liquid}

Vous pouvez personnaliser vos URL de webhook à l'aide de [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/). Parfois, certains endpoints peuvent nécessiter que vous identifiiez un utilisateur ou fournissiez des informations spécifiques à l'utilisateur dans votre URL. Lorsque vous utilisez Liquid, assurez-vous d'inclure une [valeur par défaut]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) pour chaque information spécifique à l'utilisateur que vous utilisez dans votre URL.

#### Méthode HTTP {#http-method}

La méthode HTTP à utiliser varie en fonction de l'endpoint auquel vous envoyez des informations. Dans la plupart des cas, vous utiliserez POST.

| Méthode HTTP | Description |
| ----------- | ----------- |
| POST | Écrit de nouvelles informations sur le serveur récepteur. C'est la méthode la plus couramment utilisée lors de l'envoi de données. |
| GET | Récupère des informations existantes, par opposition à l'écriture de nouvelles informations. Par définition, une requête GET ne prend pas en charge de corps de requête. |
| PUT | Met à jour les informations sur l'endpoint, en remplaçant toute information existante par ce qui se trouve dans le corps de la requête. |
| DELETE | Supprime la ressource dans l'URL HTTP. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTTP method" }

#### Corps de la requête {#request-body}

Le corps de la requête contient les informations qui seront envoyées à l'URL que vous avez spécifiée. Vous pouvez créer le corps de votre requête webhook avec des paires clé-valeur JSON ou du texte brut.

##### Paires clé-valeur JSON {#json-key-value-pairs}

Les paires clé-valeur JSON vous permettent d'écrire facilement une requête pour un endpoint qui attend un format JSON. Vous ne pouvez utiliser cette option qu'avec un endpoint qui attend une requête JSON. Par exemple, si votre clé est `message_body`, la valeur correspondante pourrait être `Your order just arrived!`. Une fois votre paire clé-valeur saisie, le compositeur configurera votre requête en syntaxe JSON, et un aperçu de votre requête JSON s'affichera automatiquement.

![Corps de la requête défini sur des paires clé-valeur JSON.]({% image_buster /assets/img/webhook_json_1.png %})

Vous pouvez personnaliser vos paires clé-valeur à l'aide de Liquid, en incluant par exemple tout attribut utilisateur, [attribut personnalisé]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#additional-notes-and-best-practices) ou [propriété d'événement]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) dans votre requête. Par exemple, vous pouvez inclure le prénom et l'adresse e-mail d'un client dans votre requête. Assurez-vous d'inclure une [valeur par défaut]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) pour chaque attribut.

##### Texte brut {#raw-text}

L'option texte brut vous offre la flexibilité d'écrire une requête pour un endpoint qui attend un corps dans n'importe quel format. Par exemple, vous pourriez l'utiliser pour écrire une requête pour un endpoint qui attend que votre requête soit au format XML.

La [personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) et l'[internationalisation]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/#campaigns-in-multiple-languages) via Liquid sont prises en charge dans le texte brut.

![Un exemple de corps de requête en texte brut utilisant Liquid.]({% image_buster /assets/img_archive/webhook_rawtext.png %})

Si vous définissez l'[en-tête de requête](#request-headers-optional) `Content-Type` sur `application/x-www-form-url-encoded`, le corps de la requête doit être formaté comme une chaîne encodée en URL. Par exemple :

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![Corps de la requête avec une chaîne encodée en URL.]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## Étape 3 : Configurer les paramètres supplémentaires {#step-3-configure-additional-settings}

#### En-têtes de requête (facultatif) {#request-headers-optional}

Certains endpoints peuvent nécessiter que vous incluiez des en-têtes dans votre requête. Dans la section **Compose** du compositeur, vous pouvez ajouter autant d'en-têtes que nécessaire.

![Exemples d'en-têtes de requête pour la clé « Authorization » et la clé « Content-type ».]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

Les en-têtes de requête courants sont les spécifications `Content-Type` (qui décrivent le type de données attendu dans le corps, comme XML ou JSON) et les en-têtes d'autorisation qui contiennent vos identifiants auprès de votre fournisseur ou système.

Les spécifications de type de contenu doivent utiliser la clé `Content-Type`. Les valeurs courantes sont `application/json` ou `application/x-www-form-urlencoded`.

Les en-têtes d'autorisation doivent utiliser la clé `Authorization`. Les valeurs courantes sont {% raw %} `Bearer {{YOUR_TOKEN}}` ou `Basic {{YOUR_TOKEN}}` {% endraw %} où `YOUR_TOKEN` correspond aux identifiants fournis par votre fournisseur ou système.

## Étape 4 : Tester l'envoi de votre message {#step-4-test-send-your-message}

Avant de mettre votre campagne en ligne, Braze recommande de tester le webhook pour vous assurer que la requête est correctement formatée.

Pour ce faire, passez à l'onglet **Test** et envoyez un webhook de test. Vous pouvez tester le webhook en tant qu'utilisateur aléatoire, un utilisateur spécifique (en saisissant son adresse e-mail ou son ID utilisateur externe), ou un utilisateur personnalisé avec les attributs de votre choix.

Après l'envoi du webhook de test, une boîte de dialogue apparaîtra avec le message de réponse. Si la requête webhook échoue, consultez le message d'erreur pour vous aider à résoudre le problème de votre webhook. L'exemple suivant détaille la réponse d'un webhook avec une URL de webhook invalide.

```http
404 Not Found

{
  "error": {
    "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
    "status_code": 404
  }
}

```

Pour plus d'informations, consultez [Envoyer des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=webhook).

## Étape 5 : Construire le reste de votre campagne ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Ensuite, construisez le reste de votre campagne. Consultez les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des webhooks.

#### Choisir la planification ou le déclencheur de livraison {#choose-delivery-schedule-or-trigger}

Les webhooks peuvent être envoyés selon une planification, une action ou un déclencheur API. Pour en savoir plus, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

Pour la livraison par événement, vous pouvez également définir la durée de la campagne et les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/).

Cette étape vous permet également de spécifier les contrôles de livraison, comme permettre aux utilisateurs de devenir [rééligibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/#campaigns) pour recevoir la campagne, ou activer les règles de [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping).

#### Choisir les utilisateurs à cibler {#choose-users-to-target}

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/) en choisissant des segments ou des filtres pour affiner votre audience. À cette étape, vous sélectionnez l'audience la plus large parmi vos segments, puis vous affinez ce segment davantage avec nos filtres, si vous le souhaitez. Vous obtenez automatiquement un aperçu de la population approximative de ce segment. Gardez à l'esprit que l'appartenance exacte au segment est toujours calculée avant l'envoi du message.

{% multi_lang_include target_audiences.md %}

#### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}

{% tab Canvas %}

Si ce n'est pas déjà fait, complétez les sections restantes de votre étape Canvas. Pour plus de détails sur la façon de construire le reste de votre Canvas, d'implémenter le test multivarié et la Sélection intelligente, et plus encore, consultez l'étape [Construire votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation Canvas.

{% endtab %}
{% endtabs %}

## Étape 6 : Vérifier et déployer {#step-6-review-and-deploy}

Après avoir terminé la construction de votre campagne ou Canvas, vérifiez ses détails, testez-la, puis envoyez-la !

## Bon à savoir {#things-to-know}

### Erreurs, logique de nouvelle tentative et délais d'expiration {#errors-retry-logic-and-timeouts}

Les webhooks reposent sur les serveurs Braze qui envoient des requêtes à un endpoint externe, et des erreurs peuvent occasionnellement survenir. Les erreurs les plus courantes incluent les erreurs de syntaxe, les clés API expirées, les limites de débit et les problèmes inattendus côté serveur. Avant d'envoyer une campagne webhook :

- Testez votre webhook pour détecter les erreurs de syntaxe
- Assurez-vous que les variables personnalisées ont des valeurs par défaut

Si votre webhook ne parvient pas à s'envoyer, un message d'erreur est enregistré dans le [Journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/), et inclut des détails tels que l'horodatage de l'erreur, le nom de l'application et des détails sur l'erreur.

![Erreur de webhook avec le message « An active access token must be used to query information about the current user ».]({% image_buster /assets/img_archive/webhook-error.png %})

Si le message d'erreur n'est pas suffisamment clair quant à la source de l'erreur, vous devriez consulter la documentation de l'endpoint API que vous utilisez. Celle-ci fournit généralement une explication des codes d'erreur utilisés par l'endpoint ainsi que leurs causes habituelles.

#### Codes de réponse et logique de nouvelle tentative {#response-codes-and-retry-logic}

Lorsque la requête webhook est envoyée, le serveur récepteur renvoie un code de réponse indiquant ce qui s'est passé avec la requête. Le tableau suivant résume les différentes réponses que le serveur peut envoyer, leur impact sur l'analytique de la campagne et si, en cas d'erreur, Braze tentera de renvoyer la campagne :

| Code de réponse | Marqué comme reçu ? | Nouvelles tentatives ? |
|---------------|-----------|----------|
| `20x` (succès) | Oui | N/A |
| `30x` (redirection) | Non | Non |
| `408` (délai d'expiration de la requête) | Non | Oui |
| `429` (limite de débit atteinte) | Non | Oui |
| `Autre 4XX` (erreur client) | Non | Non |
| `5XX` (erreur serveur) | Non | Oui |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Response codes and retry logic" }

{% alert note %}
Braze effectue de nouvelles tentatives pour les codes d'état ci-dessus jusqu'à cinq fois dans un délai de 30 minutes en utilisant des délais exponentiels. Si nous ne parvenons pas à atteindre votre endpoint, les nouvelles tentatives peuvent s'étaler sur une période de 24 heures.<br><br>Chaque webhook dispose de 90 secondes avant d'expirer.
{% endalert %}

Les en-têtes de réponse `Retry-After` et de limite de débit peuvent affecter le temps d'attente de Braze avant une tentative **réessayable** (par exemple, après `408`, `429` ou `5XX`). Ils ne rendent pas les réponses non réessayables, comme `401`, éligibles à une nouvelle tentative.

#### Authentification et identifiants de Contenu connecté {#authentication-and-connected-content-credentials}

La requête HTTP sortante du webhook ne prend pas en charge l'ajout d'[identifiants de Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/#authentication-types) (`:basic_auth` ou `:auth_credentials`) pour s'authentifier auprès de votre endpoint. Configurez l'authentification en utilisant les **en-têtes de requête** du webhook à la place. Pour récupérer un jeton ou un secret au moment de l'envoi, vous pouvez placer une balise {% raw %}`{% connected_content %}`{% endraw %} dans un champ d'en-tête ou de corps afin que Liquid le résolve avant l'envoi du webhook.

#### Modèles de webhook enregistrés et utilisation dans les campagnes {#saved-webhook-templates-and-campaign-usage}

Braze ne fournit pas de rapport intégré listant chaque campagne ou étape Canvas qui fait référence à un **modèle de webhook enregistré** donné. Pour auditer l'utilisation, examinez les étapes webhook qui utilisent la même URL et la même méthode HTTP, ou contactez l'[assistance Braze]({{site.baseurl}}/support_contact/).

#### Résolution des problèmes et détails supplémentaires sur les erreurs {#troubleshooting-and-additional-error-details}

Pour des explications détaillées, des étapes de résolution des problèmes et des conseils pour résoudre des erreurs webhook spécifiques, consultez [Résolution des problèmes liés aux requêtes webhook et Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content/). Vous y trouverez également des explications sur le fonctionnement de notre système de détection d'hôtes défaillants et sur la façon dont Braze fournit des notifications d'erreur via des e-mails automatisés et une journalisation supplémentaire dans Braze Currents.

### Liste d'autorisation IP {#ip-allowlisting}

Lorsqu'un webhook est envoyé depuis Braze, les serveurs Braze effectuent des requêtes réseau vers les serveurs de nos clients ou de tiers. Avec la liste d'autorisation IP, vous pouvez vérifier que les requêtes webhook proviennent bien de Braze, ajoutant ainsi une couche de sécurité.

Braze enverra les webhooks depuis les adresses IP suivantes. Les adresses IP listées sont automatiquement et dynamiquement ajoutées à toutes les clés API qui ont été activées pour la liste d'autorisation.

{% alert important %}
Si vous effectuez un webhook Braze vers Braze et utilisez la liste d'autorisation, vous devez autoriser toutes les adresses IP suivantes, y compris `127.0.0.1`.
{% endalert %}

{% multi_lang_include data_centers.md datacenters='ips' %}