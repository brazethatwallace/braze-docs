---
nav_title: Effectuer un appel de contenu connecté
article_title: Effectuer un appel API de contenu connecté
page_order: 0
description: "Cet article de référence explique comment effectuer un appel API de contenu connecté, avec des exemples utiles et des cas d'utilisation avancés du contenu connecté."
search_rank: 2
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}Effectuer un appel API de contenu connecté {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomconnected-content-stylefloatrightwidth120pxborder0-classnoimgbordermake-a-connected-content-api-call}

> Utilisez le contenu connecté pour insérer toute information accessible par API directement dans les messages que vous envoyez aux utilisateurs. Vous pouvez extraire du contenu directement depuis votre serveur web ou depuis des API accessibles publiquement.<br><br>Cette page explique comment effectuer des appels API de contenu connecté, les cas d'utilisation avancés du contenu connecté, la gestion des erreurs, et plus encore.

## Comprendre le volume d'appels de contenu connecté {#understanding-connected-content-call-volume}

{% alert important %}
Un envoi n'est pas égal à un appel de contenu connecté. Braze ne garantit pas un ratio 1:1 entre les envois de messages et les requêtes de contenu connecté. Le système est conçu pour privilégier le rendu et la distribution corrects des messages plutôt que la minimisation du nombre d'appels. Vos endpoints doivent être conçus pour gérer plus de requêtes que le nombre de destinataires ou de messages envoyés.
{% endalert %}

Braze peut effectuer le même appel API de contenu connecté plus d'une fois par destinataire. Les raisons courantes incluent :

- **E-mail avec plusieurs parties :** Un seul e-mail peut déclencher des passes de rendu distinctes pour le corps HTML, le corps en texte brut et la version pages mobiles accélérées (AMP) (si présente). Chaque passe peut déclencher le contenu connecté dans cette partie, de sorte qu'un destinataire peut générer plusieurs appels identiques ou similaires.
- **Validation et nouvelles tentatives :** Les payloads de messages peuvent être rendus plusieurs fois par destinataire pour la validation, la logique de nouvelles tentatives ou d'autres raisons internes.
- **Comportement par canal :** Le contenu connecté s'exécute lorsque le message est rendu. Pour les messages in-app, le message est rendu au moment de l'impression.

Si vous constatez plus d'appels de contenu connecté dans vos journaux que d'envois ou de destinataires, ce comportement est attendu. Pour des conseils sur la réduction de la charge et la planification de la montée en charge, consultez [Bonnes pratiques pour les endpoints à haut volume](#best-practices-for-high-volume-endpoints).

## Envoyer un appel de contenu connecté {#sending-a-connected-content-call}

{% raw %}

Pour envoyer un appel de contenu connecté, utilisez la balise `{% connected_content %}`. Avec cette balise, vous pouvez assigner ou déclarer des variables en utilisant `:save`. Des aspects de ces variables peuvent être référencés plus tard dans le message avec [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/).

Par exemple, le corps de message suivant accède à l'URL `http://numbersapi.com/random/trivia` et inclut une anecdote amusante dans votre message :

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is some fun trivia for you!: {{result.text}}
```

### Ajouter des variables {#adding-variables}

Vous pouvez également inclure des attributs de profil utilisateur comme variables dans la chaîne d'URL lors des requêtes de contenu connecté.

Par exemple, vous pouvez avoir un service web qui renvoie du contenu basé sur l'adresse e-mail et l'ID d'un utilisateur. Si vous transmettez des attributs contenant des caractères spéciaux, comme le signe arobase (@), assurez-vous d'utiliser le filtre Liquid `url_param_escape` pour remplacer les caractères non autorisés dans les URL par leurs versions échappées compatibles URL, comme illustré dans l'attribut d'adresse e-mail suivant.

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Les valeurs d'attributs doivent être entourées de `${}` pour fonctionner correctement dans notre version de la syntaxe Liquid.
{% endalert %}

Les requêtes de contenu connecté ne prennent en charge que les requêtes GET et POST.

## Gestion des erreurs {#error-handling}

Si l'URL est indisponible et atteint une page 404, Braze affichera une chaîne vide à la place. Si l'URL atteint une page HTTP 500 ou 502, l'URL échouera selon la logique de nouvelles tentatives.

Si l'endpoint renvoie du JSON, vous pouvez le détecter en vérifiant si la valeur `connected` est null, puis [abandonner conditionnellement le message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content/). Braze n'autorise que les URL qui communiquent via le port 80 (HTTP) et 443 (HTTPS).

### Détection d'hôte défaillant {#unhealthy-host-detection}

Le contenu connecté utilise un mécanisme de détection d'hôte défaillant pour détecter lorsque l'hôte cible connaît un taux élevé de ralentissements significatifs ou de surcharge, entraînant des délais d'attente dépassés, trop de requêtes ou d'autres situations empêchant Braze de communiquer avec succès avec l'endpoint cible. Ce mécanisme agit comme une protection pour réduire la charge inutile qui peut causer des difficultés à l'hôte cible. Il sert également à stabiliser l'infrastructure de Braze et à maintenir des vitesses d'envoi de messages rapides.

Si l'hôte cible connaît un taux élevé de ralentissements significatifs ou de surcharge, Braze interrompra temporairement les requêtes vers l'hôte cible pendant une minute, simulant à la place des réponses indiquant l'échec. Après une minute, Braze sondera la santé de l'hôte avec un petit nombre de requêtes avant de reprendre les requêtes à pleine vitesse si l'hôte est jugé sain. Si l'hôte est toujours défaillant, Braze attendra une minute supplémentaire avant de réessayer.

Si les requêtes vers l'hôte cible sont interrompues par le détecteur d'hôte défaillant, Braze continuera à rendre les messages et à suivre votre logique Liquid comme s'il avait reçu un code de réponse d'erreur. Si vous souhaitez vous assurer que ces requêtes de contenu connecté sont réessayées lorsqu'elles sont interrompues par le détecteur d'hôte défaillant, utilisez l'option `:retry`. Pour plus d'informations sur l'option `:retry`, consultez [Nouvelles tentatives de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries/).

Si vous pensez que la détection d'hôte défaillant cause des problèmes, contactez l'[assistance Braze]({{site.baseurl}}/support_contact/).

{% alert note %}
Vous pouvez ajouter des URL spécifiques à une liste d'autorisation pour le contenu connecté. Pour accéder à cette fonctionnalité, contactez votre gestionnaire de la satisfaction client.
{% endalert %}

{% alert tip %}
Pour en savoir plus sur les codes d'erreur courants, consultez [Résolution des problèmes de requêtes webhook et de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content/#unhealthy-host-detection).
{% endalert %}

### Limites de débit (429) versus détection d'hôte défaillant {#rate-limits-429-versus-unhealthy-host-detection}

Les mécanismes suivants sont différents :

- **429 Too Many Requests :** Votre endpoint (ou un service en amont) renvoie cette réponse. Cela signifie que votre serveur ou middleware refuse le trafic, souvent parce qu'il a sa propre limite de débit. Braze n'applique pas de limite de débit distincte au contenu connecté ; le volume de requêtes de contenu connecté évolue directement avec votre [limite de débit de vitesse de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-speed-rate-limiting). Comme les messages peuvent être rendus plusieurs fois par destinataire (par exemple, pour le HTML de l'e-mail, le texte brut et l'AMP), le nombre de requêtes de contenu connecté peut dépasser cette limite de débit — ne supposez pas qu'il sera inférieur ou égal au nombre de messages par minute que vous avez défini. Si vous constatez des erreurs 429, augmentez la capacité de votre endpoint ou middleware pour gérer le volume de requêtes attendu, ou réduisez la limite de débit de la campagne ou de l'étape du Canvas afin que moins de messages (et donc moins d'appels de contenu connecté) soient envoyés par minute.
- **Détection d'hôte défaillant :** Une protection côté Braze qui se déclenche après un taux et un volume élevés d'*échecs* dans une fenêtre d'une minute. Le nombre d'échecs inclut les codes de statut `408`, `429`, `502`, `503`, `504` et `529`. Lorsqu'elle est déclenchée, Braze interrompt temporairement les requêtes vers cet hôte et simule une réponse d'échec. Cela est indépendant de votre propre limitation de débit. Pour les seuils de détection et plus de détails, consultez [Résolution des problèmes de requêtes webhook et de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content/#unhealthy-host-detection). Pour éviter de déclencher la détection d'hôte défaillant, assurez-vous que votre endpoint peut gérer le volume d'appels décrit dans [Comprendre le volume d'appels de contenu connecté](#understanding-connected-content-call-volume) et [Bonnes pratiques pour les endpoints à haut volume](#best-practices-for-high-volume-endpoints).

## Permettre des performances efficaces {#allowing-for-efficient-performance}

Comme Braze distribue les messages à un rythme très rapide, assurez-vous que votre serveur peut gérer des milliers de connexions simultanées afin qu'il ne soit pas surchargé lors de l'extraction de contenu. Lorsque vous utilisez des API publiques, vérifiez que votre utilisation ne viole pas les limites de débit que le fournisseur d'API peut appliquer. Braze exige que le temps de réponse du serveur soit inférieur à deux secondes pour des raisons de performance ; si le serveur met plus de deux secondes à répondre, le contenu n'est pas inséré.

Pour en savoir plus sur la planification de la capacité des endpoints et la réduction du volume d'appels, consultez [Bonnes pratiques pour les endpoints à haut volume](#best-practices-for-high-volume-endpoints).

## Bon à savoir {#things-to-know}

* Braze ne facture pas les appels API et ils ne sont pas comptabilisés dans votre utilisation de points de donnée.
* Il y a une limite de 1 Mo pour les réponses de contenu connecté.
* Le contenu connecté s'exécute lorsque le message est rendu. Pour les messages in-app, le message est rendu au moment de l'impression.
* Les appels de contenu connecté ne suivent pas les redirections.

## Bonnes pratiques pour les endpoints à haut volume {#best-practices-for-high-volume-endpoints}

Si vos messages utilisent du contenu connecté et que vous envoyez à haut volume, prévoyez plus de requêtes que le nombre de destinataires ou d'envois :

1. **Estimez la charge de pointe :** Utilisez un multiplicateur conservateur lors du dimensionnement de votre endpoint ou middleware — les requêtes de contenu connecté peuvent dépasser le nombre de destinataires ou de messages envoyés. Par exemple, pour l'e-mail, un seul destinataire peut générer plusieurs appels (HTML, texte brut et AMP), donc destinataires × 2 ou × 3 est souvent utilisé comme estimation conservatrice.
2. **Utilisez la mise en cache lorsque c'est approprié :** Les requêtes GET sont mises en cache par défaut. Pour les requêtes POST, ajoutez `:cache_max_age` lorsque la réponse peut être réutilisée pendant une période (par exemple, un jeton ou du contenu qui ne change pas par requête). Consultez [Mise en cache des réponses]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/) et la [FAQ sur la mise en cache POST](#what-is-caching-behavior) ci-dessous.
3. **Définissez une limite de débit de vitesse de distribution :** La [limite de débit de vitesse de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-speed-rate-limiting) sur les Campaigns ou les étapes du Canvas est le seul levier pour limiter indirectement le volume de requêtes de contenu connecté — Braze ne limite pas le débit du contenu connecté lui-même. Ce n'est qu'un indicateur approximatif, et pas parfait, car les requêtes de contenu connecté ne sont pas en ratio 1:1 avec les messages. Utilisez-le pour maintenir le volume de messages (et donc de contenu connecté) dans les limites de ce que votre endpoint peut gérer.
4. **Concevez pour l'idempotence et les nouvelles tentatives :** Braze peut appeler votre endpoint plus d'une fois par destinataire. Assurez-vous que votre endpoint peut tolérer des requêtes en double sans effets secondaires incorrects.

## Types d'authentification {#authentication-types}

### Utiliser l'authentification basique {#using-basic-authentication}

Si l'URL nécessite une authentification basique, Braze peut stocker des identifiants d'authentification basique que vous pouvez utiliser dans votre appel API. Vous pouvez gérer les identifiants d'authentification basique existants et en ajouter de nouveaux dans **Paramètres** > **Contenu connecté**.

![Les paramètres de contenu connecté dans le tableau de bord de Braze.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

Pour ajouter un nouvel identifiant, sélectionnez **Add credential** > **Basic authentication**.

![Menu déroulant « Add credential » avec l'option d'utiliser l'authentification basique ou l'authentification par jeton.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

Donnez un nom à votre identifiant et saisissez le nom d'utilisateur et le mot de passe.

![La fenêtre « Create New Credential » avec l'option de saisir un nom, un nom d'utilisateur et un mot de passe.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

Vous pouvez ensuite utiliser cet identifiant d'authentification basique dans vos appels API en référençant le nom du jeton :

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Si vous supprimez un identifiant, gardez à l'esprit que tous les appels de contenu connecté essayant de l'utiliser seront abandonnés.
{% endalert %}

Les identifiants stockés s'appliquent aux requêtes {% raw %}`{% connected_content %}`{% endraw %} lorsque Braze rend un message. Ils ne sont pas appliqués à la requête HTTP principale configurée dans une étape de [webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/#authentication-and-connected-content-credentials). Utilisez les en-têtes de requête ou une balise {% raw %}`{% connected_content %}`{% endraw %} dans un champ d'en-tête ou de corps de webhook lorsque vous devez récupérer des secrets pour cet appel.

### Utiliser l'authentification par jeton {#using-token-authentication}

Lorsque vous utilisez le contenu connecté de Braze, vous pouvez constater que certaines API nécessitent un jeton au lieu d'un nom d'utilisateur et d'un mot de passe. Braze peut également stocker des identifiants contenant des valeurs d'en-tête d'authentification par jeton.

Pour ajouter un identifiant contenant des valeurs de jeton, sélectionnez **Add credential** > **Token authentication**. Ajoutez ensuite les paires clé-valeur pour les en-têtes de votre appel API et le domaine autorisé.

![Un exemple de jeton « token_credential_abc » avec les détails d'authentification par jeton.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

Vous pouvez ensuite utiliser cet identifiant dans vos appels API en référençant le nom de l'identifiant :

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://api.endpoint.com/your_path
     :method post
     :auth_credentials token_credential_abc
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### Utiliser Open Authentication (OAuth) {#using-open-authentication-oauth}

Certaines configurations d'API nécessitent la récupération d'un jeton d'accès qui peut ensuite être utilisé pour authentifier l'endpoint API auquel vous souhaitez accéder.

#### Étape 1 : Récupérer le jeton d'accès {#step-1-retrieve-the-access-token}

L'exemple suivant illustre la récupération et l'enregistrement d'un jeton d'accès dans une variable locale, qui peut ensuite être utilisée pour authentifier l'appel API suivant. Un paramètre `:cache_max_age` peut être ajouté pour correspondre à la durée de validité du jeton d'accès et réduire le nombre d'appels sortants de contenu connecté. Consultez [Mise en cache configurable]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/local_connected_content_variables/#configurable-caching) pour plus d'informations.

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :auth_credentials access_token_credential_abc
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### Étape 2 : Autoriser l'API en utilisant le jeton d'accès récupéré {#step-2-authorize-the-api-using-the-retrieved-access-token}

Une fois le jeton enregistré, il peut être injecté dynamiquement dans l'appel de contenu connecté suivant pour autoriser la requête :

{% raw %}
```
{% connected_content
     https://your_API_endpoint_here/
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "{{token_response}}"
     }
     :body key1=value1&key2=value2
     :save response
%}
```
{% endraw %}

### Modifier les identifiants {#editing-credentials}

Vous pouvez modifier le nom de l'identifiant pour les types d'authentification.

- Pour l'authentification basique, vous pouvez mettre à jour le nom d'utilisateur et le mot de passe. Notez que le mot de passe précédemment saisi ne sera pas visible.
- Pour l'authentification par jeton, vous pouvez mettre à jour les paires clé-valeur d'en-tête et le domaine autorisé. Notez que les valeurs d'en-tête précédemment définies ne seront pas visibles.


## Liste d'autorisation des IP de contenu connecté {#connected-content-ip-allowlisting}

Lorsqu'un message utilisant du contenu connecté est envoyé depuis Braze, les serveurs de Braze effectuent automatiquement des requêtes réseau vers les serveurs de nos clients ou de tiers pour récupérer des données. Avec la liste d'autorisation des IP, vous pouvez vérifier que les requêtes de contenu connecté proviennent bien de Braze, ajoutant une couche de sécurité.

Braze enverra les requêtes de contenu connecté depuis les plages d'IP suivantes. Les plages listées sont automatiquement et dynamiquement ajoutées à toutes les clés API qui ont été activées pour la liste d'autorisation.

Braze dispose d'un ensemble réservé d'IP utilisées pour tous les services, qui ne sont pas toutes actives à un moment donné. Cela est conçu pour que Braze puisse envoyer depuis un centre de données différent ou effectuer de la maintenance, si nécessaire, sans impacter les clients. Braze peut utiliser une, un sous-ensemble ou toutes les IP suivantes lors des requêtes de contenu connecté.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### En-tête `User-Agent` {#user-agent-header}

Braze inclut un en-tête `User-Agent` dans toutes les requêtes de contenu connecté et de webhook, similaire au suivant :

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
Gardez à l'esprit que la valeur de hachage change régulièrement. Si vous filtrez le trafic par `User-Agent`, autorisez toutes les valeurs commençant par `Braze Sender`.
{% endalert %}

## Résolution des problèmes {#troubleshooting}

Utilisez [Webhook.site](https://webhook.site/) pour résoudre les problèmes de vos appels de contenu connecté et diagnostiquer les problèmes liés aux en-têtes de requête, au corps de requête et aux autres informations envoyées dans l'appel.

1. Remplacez l'URL dans votre appel de contenu connecté par l'URL unique générée sur le site.
2. Prévisualisez et testez votre campagne ou étape du Canvas pour voir les requêtes arriver sur ce site web.

Vous pouvez également vérifier que la balise Liquid inclut les paramètres attendus par votre endpoint (par exemple, `:method`, `:headers`, `:content_type`, `:body` et `:basic_auth` lorsque requis). Si vous vous appuyez sur la clé de code de statut HTTP dans un objet JSON enregistré, l'endpoint doit renvoyer un objet JSON et un statut `2XX`.

En cas de taux d'erreur élevé de votre hôte, consultez [Détection d'hôte défaillant]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors/#unhealthy-host-detection) et [Volume d'appels de contenu connecté](#understanding-connected-content-call-volume).

## Questions fréquentes {#frequently-asked-questions}

### Pourquoi y a-t-il plus d'appels de contenu connecté que d'utilisateurs ou d'envois ? {#why-are-there-more-connected-content-calls-than-users-or-sends}

Braze peut effectuer le même appel API de contenu connecté plus d'une fois par destinataire pour rendre un payload de message. Les payloads de messages peuvent être rendus plusieurs fois par destinataire pour la validation, la logique de nouvelles tentatives ou d'autres raisons internes. Cependant, notez qu'un seul des appels de contenu connecté alimente un message.

Il est attendu qu'un appel API de contenu connecté puisse être effectué plus d'une fois par destinataire, même si la logique de nouvelles tentatives n'est pas utilisée dans l'appel. Nous recommandons de définir la limite de débit de tous les messages contenant du contenu connecté ou de configurer vos serveurs pour mieux gérer le volume attendu qui tient compte de plusieurs appels de contenu connecté effectués par envoi de message.

Consultez [Comprendre le volume d'appels de contenu connecté](#understanding-connected-content-call-volume) et [Bonnes pratiques pour les endpoints à haut volume](#best-practices-for-high-volume-endpoints) pour les détails et les mesures d'atténuation.

### Comment fonctionne la limitation de débit avec le contenu connecté ? {#how-does-rate-limiting-work-with-connected-content}

Le contenu connecté n'a pas sa propre limite de débit. La limite de débit est plutôt basée sur le taux d'envoi de messages. Nous recommandons de définir la limite de débit d'envoi de messages en dessous de votre limite de débit prévue pour le contenu connecté s'il y a plus d'appels de contenu connecté que de messages envoyés.

### Quel est le comportement de mise en cache ? {#what-is-caching-behavior}

Les requêtes GET sont mises en cache par défaut (consultez [Mise en cache des réponses]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/)). **Les requêtes POST ne sont pas mises en cache par défaut**, mais vous pouvez activer la mise en cache en ajoutant `:cache_max_age` à l'appel de contenu connecté. Cela peut réduire la charge sur l'endpoint lorsque la même requête POST (par exemple, une requête de jeton ou de contenu) serait effectuée de manière répétée dans la fenêtre de cache.

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

La mise en cache peut aider à réduire les appels de contenu connecté en double, mais ne garantit pas un seul appel par utilisateur. La durée du cache est comprise entre cinq minutes et quatre heures. Pour tous les détails, consultez [Mise en cache des réponses]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/).

### Quel est le comportement HTTP par défaut du contenu connecté ? {#what-is-the-connected-content-http-default-behavior}

{% multi_lang_include connected_content/sections.md section='default behavior' %}

{% multi_lang_include connected_content/sections.md section='http post' %}

### Que se passe-t-il si j'utilise le même appel de contenu connecté à plusieurs endroits ? {#what-happens-if-i-use-the-same-connected-content-call-in-multiple-places}

Chaque balise de contenu connecté est évaluée séparément, même si plusieurs balises utilisent la même URL et les mêmes paramètres. Lorsque l'URL et les paramètres de cache le permettent, les requêtes identiques peuvent être servies depuis le cache plutôt que de déclencher une nouvelle requête sortante (consultez [Mise en cache des réponses]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/) pour les détails).