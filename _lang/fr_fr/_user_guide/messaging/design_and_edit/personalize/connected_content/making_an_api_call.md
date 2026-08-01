---
nav_title: Effectuer un appel de contenu connecté
article_title: Effectuer un appel API de contenu connecté
page_order: 0
description: "Cet article de référence explique comment effectuer un appel API de contenu connecté, avec des exemples utiles et des cas d'usage avancés du contenu connecté."
search_rank: 2
toc_headers: h2
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}Effectuer un appel API de contenu connecté {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomconnected-content-stylefloatrightwidth120pxborder0-classnoimgbordermake-a-connected-content-api-call}

> Utilisez le contenu connecté pour insérer toute information accessible par API directement dans les messages que vous envoyez aux utilisateurs. Vous pouvez extraire du contenu directement depuis votre serveur web ou depuis des API accessibles publiquement.<br><br>Cette page explique comment effectuer des appels API de contenu connecté, les cas d'usage avancés du contenu connecté, la gestion des erreurs, et plus encore.

## Comprendre le volume d'appels de contenu connecté {#understanding-connected-content-call-volume}

{% alert important %}
Un envoi n'est pas égal à un appel de contenu connecté. Braze ne garantit pas un ratio 1:1 entre les envois de messages et les requêtes de contenu connecté. Le système est conçu pour privilégier le rendu et la distribution corrects des messages plutôt que la minimisation du nombre d'appels. Vos endpoints doivent être conçus pour gérer plus de requêtes que le nombre de destinataires ou de messages envoyés.
{% endalert %}

Braze peut effectuer le même appel API de contenu connecté plus d'une fois par destinataire. Les raisons courantes incluent :

- **E-mail avec plusieurs parties :** Un seul e-mail peut déclencher des passes de rendu distinctes pour le corps HTML, le corps en texte brut et la version pages mobiles accélérées (AMP) (si présente). Chaque passe peut déclencher le contenu connecté dans cette partie, de sorte qu'un destinataire peut générer plusieurs appels identiques ou similaires.
- **Validation et nouvelles tentatives :** Les payloads de messages peuvent être rendus plusieurs fois par destinataire pour la validation, la logique de nouvelles tentatives ou d'autres raisons internes.
- **Comportement par canal :** Le contenu connecté s'exécute lorsque le message est rendu. Pour les messages in-app, le message est rendu au moment de l'impression.

Si vous constatez plus d'appels de contenu connecté dans vos journaux que d'envois ou de destinataires, ce comportement est attendu. Pour des conseils sur la réduction de la charge et la planification de la montée en charge, consultez [Bonnes pratiques pour les endpoints à haut volume](#best-practices-for-high-volume-endpoints).

## Envoyer un appel de contenu connecté {#send-a-connected-content-call}

Pour envoyer un appel de contenu connecté, utilisez la balise {% raw %}`{% connected_content %}`{% endraw %}. Avec cette balise, vous pouvez assigner ou déclarer des variables en utilisant `:save`. Des aspects de ces variables peuvent être référencés ultérieurement dans le message avec [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid).

### Décomposer l'appel API {#break-down-the-api-call}

L'exemple suivant utilise l'API Sunrise-Sunset et inclut l'heure du lever de soleil du jour dans un message :

{% raw %}
```
{% connected_content https://api.sunrise-sunset.org/v2?lat=40.7128&lng=-74.0060&date=today :save result %}
Hi there, today's sunrise in NYC is at {{result.sunrise}}.
```
{% endraw %}

Voici ce que fait chaque partie :

| Composant | Ce qu'il fait |
| --- | --- |
| Balise `connected_content` | Indique à Braze d'effectuer une requête HTTP lors du rendu du message. |
| `https://api.sunrise-sunset.org/v2` | L'endpoint API que Braze appelle. |
| `lat=40.7128&lng=-74.0060` | Paramètres de requête pour les coordonnées de New York. |
| `date=today` | Demande les données du jour en cours pour ces coordonnées. |
| `:save result` | Stocke la réponse de l'API dans une variable locale nommée `result`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Décomposer l'appel API" }

### Fonctionnement de la réponse de l'API Sunrise-Sunset {#how-the-sunrise-sunset-api-response-works}

Cet endpoint renvoie du JSON avec des champs de premier niveau tels que `sunrise`, `sunset` et `tzid`. Les heures sont renvoyées dans le fuseau horaire du lieu par défaut (pour cet exemple, l'heure de New York).

Par exemple, la structure de la réponse est similaire à :

```json
{
  "date": "2026-07-23",
  "tzid": "America/New_York",
  "sunrise": "2026-07-23T05:42:11-04:00",
  "sunset": "2026-07-23T20:21:32-04:00"
}
```

### Associer la réponse de l'API à Liquid {#map-the-api-response-to-liquid}

Comme la réponse est enregistrée sous `result`, référencez chaque champ directement depuis cet objet.

{% raw %}
```liquid
{{result.sunrise}}
{{result.sunset}}
{{result.tzid}}
```
{% endraw %}

Utilisez ce modèle chaque fois que vous enregistrez du JSON à partir du contenu connecté :

1. Enregistrez la réponse de l'API avec `:save`.
2. Trouvez le champ souhaité dans la réponse JSON.
3. Référencez-le en Liquid sous la forme `saved_variable.field_name`.

### Ajouter des variables {#add-variables}

Vous pouvez également inclure des attributs de profil utilisateur en tant que variables dans la chaîne d'URL lors des requêtes de contenu connecté.

Par exemple, vous pouvez avoir un service web qui renvoie du contenu en fonction de l'adresse e-mail et de l'ID d'un utilisateur. Si vous transmettez des attributs contenant des caractères spéciaux, comme l'arobase (@), assurez-vous d'utiliser le filtre Liquid `url_param_escape` pour remplacer les caractères non autorisés dans les URL par leurs versions échappées compatibles, comme illustré dans l'attribut d'adresse e-mail suivant.

{% raw %}
```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Les valeurs d'attributs doivent être entourées de `${}` pour fonctionner correctement dans notre version de la syntaxe Liquid.
{% endalert %}

Les requêtes de contenu connecté prennent en charge uniquement les requêtes GET et POST.

## Gestion des erreurs {#error-handling}

Si l'URL est indisponible et atteint une page 404, Braze affiche une chaîne de caractères vide à la place. Si l'URL atteint une page HTTP 500 ou 502, l'URL échoue selon la logique de nouvelle tentative.

Si l'endpoint renvoie du JSON, vous pouvez le détecter en vérifiant si la valeur `connected` est nulle, puis [abandonner conditionnellement le message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content). Braze n'autorise que les URL qui communiquent via le port 80 (HTTP) et le port 443 (HTTPS).

### Détection d'hôte défaillant {#unhealthy-host-detection}

Le contenu connecté utilise un mécanisme de détection d'hôte défaillant pour identifier quand l'hôte cible connaît un taux élevé de ralentissements significatifs ou de surcharge, entraînant des délais d'attente dépassés, un trop grand nombre de requêtes ou d'autres situations empêchant Braze de communiquer avec l'endpoint cible. Ce mécanisme agit comme une protection pour réduire la charge inutile qui pourrait mettre l'hôte cible en difficulté. Il contribue également à stabiliser l'infrastructure de Braze et à maintenir des vitesses d'envoi de messages rapides.

Si l'hôte cible connaît un taux élevé de ralentissements significatifs ou de surcharge, Braze interrompt temporairement les requêtes vers l'hôte cible pendant une minute, simulant à la place des réponses indiquant l'échec. Après une minute, Braze sonde l'état de santé de l'hôte à l'aide d'un petit nombre de requêtes avant de reprendre les requêtes à pleine vitesse si l'hôte est jugé sain. Si l'hôte est toujours défaillant, Braze attend une minute supplémentaire avant de réessayer.

Si les requêtes vers l'hôte cible sont interrompues par le détecteur d'hôte défaillant, Braze continue de générer les messages et de suivre votre logique Liquid comme s'il avait reçu un code de réponse d'erreur. Si vous souhaitez vous assurer que ces requêtes de contenu connecté sont réessayées lorsqu'elles sont interrompues par le détecteur d'hôte défaillant, utilisez l'option `:retry`. Pour plus d'informations sur l'option `:retry`, consultez [Nouvelles tentatives de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries).

Si vous pensez que la détection d'hôte défaillant cause des problèmes, contactez le [support Braze]({{site.baseurl}}/support_contact).

{% alert note %}
Vous pouvez ajouter des URL spécifiques à une liste d'autorisation pour le contenu connecté. Pour accéder à cette fonctionnalité, contactez votre gestionnaire du succès des clients.
{% endalert %}

{% alert tip %}
Pour plus d'informations sur les codes d'erreur courants, consultez [Résoudre les problèmes de requêtes webhook et de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection).
{% endalert %}

### Limitation du débit (429) versus détection d'hôte défaillant {#rate-limits-429-versus-unhealthy-host-detection}

Les mécanismes suivants sont différents :

- **429 Too Many Requests :** Votre endpoint (ou un service en amont) renvoie cette réponse. Cela signifie que votre serveur ou middleware refuse le trafic, souvent parce qu'il possède sa propre limite de débit. Braze n'applique pas de limite de débit distincte au contenu connecté ; le volume de requêtes de contenu connecté évolue directement avec votre [limite de débit de vitesse de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting). Étant donné que les messages peuvent être générés plusieurs fois par destinataire (par exemple, pour le HTML d'e-mail, le texte brut et l'AMP), le nombre de requêtes de contenu connecté peut dépasser cette limite de débit — ne supposez pas qu'il sera inférieur ou égal au nombre de messages par minute que vous avez défini. Si vous observez des erreurs 429, dimensionnez votre endpoint ou middleware pour gérer le volume de requêtes attendu, ou réduisez la [limite de débit de vitesse de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) de la Campaign ou du Canvas afin que moins de messages (et donc moins d'appels de contenu connecté) soient envoyés par minute.
- **Détection d'hôte défaillant :** Une protection côté Braze qui se déclenche après un taux et un volume élevés d'*échecs* dans une fenêtre d'une minute. Le nombre d'échecs inclut les codes de statut `408`, `429`, `502`, `503`, `504` et `529`. Lorsqu'elle est déclenchée, Braze interrompt temporairement les requêtes vers cet hôte et simule une réponse d'échec. Ce mécanisme est indépendant de votre propre limitation de débit. Pour les seuils de détection et plus de détails, consultez [Résoudre les problèmes de requêtes webhook et de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection). Pour éviter de déclencher la détection d'hôte défaillant, assurez-vous que votre endpoint peut gérer le volume d'appels décrit dans [Comprendre le volume d'appels de contenu connecté](#understanding-connected-content-call-volume) et [Bonnes pratiques pour les endpoints à fort volume](#best-practices-for-high-volume-endpoints).

## Permettre des performances efficaces {#allowing-for-efficient-performance}

Comme Braze distribue les messages à un rythme très rapide, assurez-vous que votre serveur peut gérer des milliers de connexions simultanées afin qu'il ne soit pas surchargé lors de l'extraction de contenu. Lorsque vous utilisez des API publiques, vérifiez que votre utilisation ne viole pas les limites de débit que le fournisseur d'API peut appliquer. Braze exige que le temps de réponse du serveur soit inférieur à deux secondes pour des raisons de performance ; si le serveur met plus de deux secondes à répondre, le contenu n'est pas inséré.

Pour en savoir plus sur la planification de la capacité des endpoints et la réduction du volume d'appels, consultez [Bonnes pratiques pour les endpoints à haut volume](#best-practices-for-high-volume-endpoints).

## Ce qu'il faut savoir {#things-to-know}

- Braze ne facture pas les appels API et ceux-ci ne sont pas comptabilisés dans votre consommation de points de donnée.
- Les réponses du contenu connecté sont limitées à 1 Mo.
- Le contenu connecté s'exécute au moment du rendu du message. Pour les messages in-app, le rendu a lieu au moment de l'impression.
- Les appels de contenu connecté ne suivent pas les redirections.

### Comment les appels de contenu connecté sont traités {#how-connected-content-calls-are-processed}

Les appels de contenu connecté au sein d'un même modèle de message sont exécutés séquentiellement (de haut en bas) lors du rendu Liquid. Cela signifie que les appels en aval peuvent référencer des variables définies par les appels en amont. Dans cet exemple, le premier appel récupère les données utilisateur, et le second utilise ces données pour obtenir les préférences :

{% raw %}
```liquid
{% connected_content https://api.example.com/user :save user_data %}
{% connected_content https://api.example.com/preferences?user_id={{user_data.id}} :save preferences %}
```
{% endraw %}

### Envoi global et volume de requêtes {#global-sending-and-request-volume}

Bien que les appels de contenu connecté s'exécutent séquentiellement au sein d'un même message, les messages sont envoyés en parallèle à travers vos Campaigns et Canvas. Les envois à fort volume peuvent générer un trafic de requêtes important vers vos endpoints pendant les périodes d'envoi de pointe. Pour gérer et limiter ce trafic — y compris les limites de débit de messaging de l'espace de travail, la limitation de la vitesse de distribution et la mise en cache — consultez les [Bonnes pratiques pour les endpoints à fort volume](#best-practices-for-high-volume-endpoints).

## Bonnes pratiques pour les endpoints à haut volume {#best-practices-for-high-volume-endpoints}

Si vos messages utilisent le contenu connecté et que vous envoyez en grand volume, prévoyez un nombre de requêtes supérieur au nombre de destinataires ou d'envois :

- **Estimez la charge de pointe :** utilisez un multiplicateur conservateur lors du dimensionnement de votre endpoint ou middleware — les requêtes de contenu connecté peuvent dépasser le nombre de destinataires ou de messages envoyés. Par exemple, pour l'e-mail, un seul destinataire peut générer plusieurs appels (HTML, texte brut et AMP), donc destinataires × 2 ou × 3 est souvent utilisé comme estimation prudente.
- **Utilisez la mise en cache lorsque c'est approprié :** les requêtes GET sont mises en cache par défaut. Pour les requêtes POST, ajoutez `:cache_max_age` lorsque la réponse peut être réutilisée pendant une période (par exemple, un jeton ou un contenu qui ne change pas à chaque requête). Consultez [Mise en cache des réponses]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) et la [FAQ sur la mise en cache POST](#what-is-caching-behavior) dans la section suivante.
- **Définissez des limites de débit pour les messages :** les [limites de débit de messaging de l'espace de travail]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) et la [limitation de la vitesse de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) sur les Campaigns ou les Canvas limitent indirectement le volume de requêtes de contenu connecté — Braze ne limite pas le débit du contenu connecté lui-même. Ce sont des approximations, pas des mesures exactes, car les requêtes de contenu connecté ne sont pas en correspondance 1:1 avec les messages. Utilisez-les pour maintenir le volume de messages (et donc de contenu connecté) dans les limites de ce que votre endpoint peut gérer.
- **Concevez pour l'idempotence et les nouvelles tentatives :** Braze peut appeler votre endpoint plus d'une fois par destinataire. Assurez-vous que votre endpoint peut tolérer des requêtes en double sans effets secondaires indésirables.

## Types d'authentification {#authentication-types}

### Utiliser l'authentification basique {#using-basic-authentication}

Si l'URL nécessite une authentification basique, Braze peut stocker des identifiants d'authentification basique que vous pouvez utiliser dans votre appel API. Vous pouvez gérer les identifiants d'authentification basique existants et en ajouter de nouveaux dans **Paramètres** > **Contenu connecté**.

![Les paramètres de contenu connecté dans le tableau de bord de Braze.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

Pour ajouter un nouvel identifiant, sélectionnez **Ajouter un identifiant** > **Authentification basique**.

![Menu déroulant « Ajouter un identifiant » avec l'option d'utiliser l'authentification basique ou l'authentification par jeton.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

Donnez un nom à votre identifiant et saisissez le nom d'utilisateur et le mot de passe.

![La fenêtre « Créer un nouvel identifiant » avec l'option de saisir un nom, un nom d'utilisateur et un mot de passe.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

Vous pouvez ensuite utiliser cet identifiant d'authentification basique dans vos appels API en référençant le nom du jeton :

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Si vous supprimez un identifiant, gardez à l'esprit que tous les appels de contenu connecté qui tentent de l'utiliser seront annulés.
{% endalert %}

Les identifiants stockés s'appliquent aux requêtes {% raw %}`{% connected_content %}`{% endraw %} lorsque Braze effectue le rendu d'un message. Ils ne sont pas appliqués à la requête HTTP principale configurée dans une étape de [webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#authentication-and-connected-content-credentials). Utilisez les en-têtes de requête ou une balise {% raw %}`{% connected_content %}`{% endraw %} dans un champ d'en-tête ou de corps de webhook lorsque vous devez récupérer des secrets pour cet appel.

### Utiliser l'authentification par jeton {#using-token-authentication}

Lorsque vous utilisez le contenu connecté de Braze, vous pouvez constater que certaines API nécessitent un jeton au lieu d'un nom d'utilisateur et d'un mot de passe. Braze peut également stocker des identifiants contenant des valeurs d'en-tête d'authentification par jeton.

Pour ajouter un identifiant contenant des valeurs de jeton, sélectionnez **Ajouter un identifiant** > **Authentification par jeton**. Ajoutez ensuite les paires clé-valeur pour les en-têtes de votre appel API et le domaine autorisé.

![Un exemple de jeton « token_credential_abc » avec les détails de l'authentification par jeton.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

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

### Utiliser l'authentification ouverte (OAuth) {#use-open-authentication-oauth}

Certaines configurations d'API nécessitent la récupération d'un jeton d'accès qui peut ensuite être utilisé pour authentifier l'endpoint API auquel vous souhaitez accéder.

#### Étape 1 : Récupérer le jeton d'accès {#step-1-retrieve-the-access-token}

L'exemple suivant illustre la récupération et l'enregistrement d'un jeton d'accès dans une variable locale, qui peut ensuite être utilisée pour authentifier l'appel API suivant. Un paramètre `:cache_max_age` peut être ajouté pour correspondre à la durée de validité du jeton d'accès et réduire le nombre d'appels sortants de contenu connecté. Consultez [Mise en cache configurable]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) pour plus d'informations.

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

{% alert note %}
Lorsque l'endpoint de jeton attend `application/x-www-form-urlencoded` et que vous transmettez des identifiants dans `:body`, encodez en URL tous les caractères spéciaux dans les valeurs des paramètres. Par exemple, les barres obliques (`/`) deviennent `%2F` et les signes plus (`+`) deviennent `%2B`. Les caractères spéciaux non encodés peuvent entraîner l'échec des requêtes de jeton OAuth.
{% endalert %}

#### Étape 2 : Autoriser l'API à l'aide du jeton d'accès récupéré {#step-2-authorize-the-api-using-the-retrieved-access-token}

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
- Pour l'authentification par jeton, vous pouvez mettre à jour les paires clé-valeur de l'en-tête et le domaine autorisé. Notez que les valeurs d'en-tête précédemment définies ne seront pas visibles.

## Liste d'autorisation des adresses IP pour le contenu connecté {#connected-content-ip-allowlisting}

Lorsqu'un message utilisant le contenu connecté est envoyé depuis Braze, les serveurs Braze effectuent automatiquement des requêtes réseau vers les serveurs de nos clients ou de tiers pour récupérer des données. Grâce à la liste d'autorisation des adresses IP, vous pouvez vérifier que les requêtes de contenu connecté proviennent bien de Braze, ajoutant ainsi une couche de sécurité supplémentaire.

Braze enverra les requêtes de contenu connecté à partir des plages d'adresses IP suivantes. Les plages répertoriées sont automatiquement et dynamiquement ajoutées à toutes les clés API pour lesquelles la liste d'autorisation a été activée.

Braze dispose d'un ensemble réservé d'adresses IP utilisées pour tous les services, qui ne sont pas toutes actives à un moment donné. Cela permet à Braze d'envoyer depuis un autre centre de données ou d'effectuer des opérations de maintenance, si nécessaire, sans impact sur les clients. Braze peut utiliser une, un sous-ensemble ou la totalité des adresses IP suivantes lors des requêtes de contenu connecté.

Si les requêtes de contenu connecté renvoient systématiquement une erreur `403 Forbidden` et que l'authentification est correctement configurée, ajoutez ces adresses IP à la liste d'autorisation du serveur qui reçoit la requête. Une erreur `403` peut également indiquer des permissions insuffisantes ou des identifiants invalides, vérifiez donc à la fois les paramètres réseau et d'authentification. Pour des conseils spécifiques aux webhooks, consultez [403 Forbidden et liste d'autorisation des adresses IP]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#403-forbidden-and-ip-allowlisting).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Utiliser la liste d'autorisation des adresses IP avec Amazon S3 {#using-ip-allowlisting-with-amazon-s3}

Lorsque vous utilisez le contenu connecté pour récupérer des fichiers depuis Amazon S3, configurez votre compartiment pour autoriser les requêtes HTTP `GET` non authentifiées provenant des adresses IP de Braze.

1. **Ajoutez une politique de compartiment avec des conditions IP :** Accordez l'autorisation `s3:GetObject` sur les objets de votre compartiment avec `Principal: "*"` et une condition `IpAddress` qui utilise les [plages d'adresses IP de Braze](#connected-content-ip-allowlisting) pour votre instance. Vous n'avez pas besoin de définir des ACL public-read sur les objets individuels.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": ["{YOUR_BRAZE_IP_RANGE}"]
        }
      }
    }
  ]
}
```

Remplacez `{YOUR_BRAZE_IP_RANGE}` par les plages d'adresses IP de Braze pour votre instance répertoriées dans [Liste d'autorisation des adresses IP pour le contenu connecté](#connected-content-ip-allowlisting). Vous pouvez ajouter une ou plusieurs plages en tant que valeurs distinctes dans le tableau `aws:SourceIp`.

{: start="2"}
2. **Vérifiez les paramètres S3 Block Public Access :** Les politiques de compartiment qui utilisent `Principal: "*"` sont considérées comme un accès public par AWS, même avec des conditions IP. Vous devrez peut-être autoriser l'accès public basé sur la politique de compartiment tout en maintenant l'accès public basé sur les ACL bloqué.

3. **Utilisez l'URL de l'objet S3 dans votre balise de contenu connecté :** Référencez l'objet avec son URL S3 standard (par exemple, `https://your-bucket.s3.amazonaws.com/path/to/object.json`).

Pour plus d'informations sur les politiques de compartiment et les clés de condition, consultez la [documentation AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html).

### En-tête `User-Agent` {#user-agent-header}

Braze inclut un en-tête `User-Agent` dans toutes les requêtes de contenu connecté et de webhook, similaire à ce qui suit :

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
Gardez à l'esprit que la valeur de hachage change régulièrement. Si vous filtrez le trafic par `User-Agent`, autorisez toutes les valeurs commençant par `Braze Sender`.
{% endalert %}

## Résolution des problèmes {#troubleshooting}

Si votre appel de contenu connecté ne s'affiche pas correctement ou pas du tout, vérifiez les points suivants :

- **Confirmez qu'un appel de contenu connecté a été effectué :** Vous pouvez vérifier qu'un appel a été effectué dans l'[onglet Historique des messages]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab). Vous pouvez également envoyer un test avec une seule requête de contenu connecté.
- **Vérifiez via Postman ou une requête CURL que la requête souhaitée aboutit :** Si la requête fonctionne et renvoie une réponse, comparez la requête en détail (y compris les en-têtes). Confirmez que les en-têtes sont capturés dans des paires clé-valeur avec des guillemets doubles.
- **Validez que l'autorisation est gérée correctement :** Confirmez que l'option `:basic_auth`/`:auth_credentials` est utilisée et que l'autorisation de contenu connecté a été ajoutée aux paramètres de l'espace de travail de contenu connecté. Parfois, l'URL de contenu connecté nécessite des en-têtes supplémentaires au-delà de l'authentification qui doivent être renseignés.
- **Vérifiez que les données sont dans un format attendu :** Pour le corps de la réponse, Braze analyse le JSON valide en un objet Liquid ; sinon, la réponse est traitée comme du texte brut (y compris le HTML). L'option `:content_type` définit les en-têtes `Content-Type` et `Accept` sortants de votre requête et n'affecte pas l'analyse de la réponse. Pour le `:body` de la requête, si votre JSON contient des espaces, suivez les instructions de la section [Fournir un corps JSON]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/local_connected_content_variables#providing-json-body).
- **Confirmez que les données ont été analysées correctement :** Vérifiez que le Liquid référence correctement le champ attendu. Pour du JSON imbriqué, utilisez {% raw %}`{{sampleresult.data[0].sample_field}}`{% endraw %} pour pointer vers le champ imbriqué souhaité. Vous pouvez vérifier les propriétés JSON imbriquées en affichant le résultat attendu avec {% raw %}`RESPONSE:{{sampleresult.data}}`{% endraw %}.
- **Vérifiez le code de statut de la réponse :** Le code de statut de la réponse doit être un code `2XX`. Le contenu connecté ne permet pas de consommer la réponse lorsque le code n'est pas `2XX`.

Vous pouvez également utiliser [Webhook.site](https://webhook.site/) pour résoudre les problèmes liés à vos appels de contenu connecté et diagnostiquer les problèmes concernant les en-têtes de requête, le corps de la requête et les autres informations envoyées dans l'appel.

1. Remplacez l'URL de votre appel de contenu connecté par l'URL unique générée sur le site.
2. Prévisualisez et testez votre Campaign ou étape Canvas pour voir les requêtes arriver sur ce site.

Vous pouvez également vérifier que l'étiquette Liquid inclut les paramètres attendus par votre endpoint (par exemple, `:method`, `:headers`, `:content_type`, `:body` et `:basic_auth` lorsque nécessaire). Si vous vous appuyez sur la clé du code de statut HTTP dans un objet JSON enregistré, l'endpoint doit renvoyer un objet JSON et un statut `2XX`.

Pour des taux d'erreur élevés provenant de votre hôte, consultez [Détection d'hôte défaillant]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection) et [Volume d'appels de contenu connecté](#understanding-connected-content-call-volume).

## Questions fréquentes {#frequently-asked-questions}

### Pourquoi y a-t-il plus d'appels de contenu connecté que d'utilisateurs ou d'envois ? {#why-are-there-more-connected-content-calls-than-users-or-sends}

Braze peut effectuer le même appel d'API de contenu connecté plus d'une fois par destinataire pour générer le payload d'un message. Les payloads de messages peuvent être générés plusieurs fois par destinataire à des fins de validation, de logique de nouvelle tentative ou pour d'autres raisons internes. Cependant, notez qu'un seul des appels de contenu connecté alimente réellement un message.

Il est normal qu'un appel d'API de contenu connecté puisse être effectué plus d'une fois par destinataire, même si la logique de nouvelle tentative n'est pas utilisée dans l'appel. Nous recommandons de définir la limite de débit de tout message contenant du contenu connecté ou de configurer vos serveurs pour mieux gérer le volume attendu qui tient compte des multiples appels de contenu connecté effectués par envoi de message.

Consultez [Comprendre le volume d'appels de contenu connecté](#understanding-connected-content-call-volume) et [Bonnes pratiques pour les endpoints à fort volume](#best-practices-for-high-volume-endpoints) pour plus de détails et des mesures d'atténuation.

### Comment fonctionne la limitation du débit avec le contenu connecté ? {#how-does-rate-limiting-work-with-connected-content}

Le contenu connecté ne dispose pas de sa propre limite de débit. La limite de débit est plutôt basée sur le taux d'envoi des messages. Nous recommandons de définir la limite de débit de messagerie à un niveau supérieur à la limite de débit prévue pour le contenu connecté s'il y a plus d'appels de contenu connecté que de messages envoyés.

### Quel est le comportement de mise en cache ? {#what-is-caching-behavior}

Les requêtes GET sont mises en cache par défaut (voir [Mise en cache des réponses]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)). **Les requêtes POST ne sont pas mises en cache par défaut**, mais vous pouvez activer la mise en cache en ajoutant `:cache_max_age` à l'appel de contenu connecté. Cela peut réduire la charge sur l'endpoint lorsque la même requête POST (par exemple, une requête de jeton ou de contenu) serait effectuée de manière répétée dans la fenêtre de cache.

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

La mise en cache peut aider à réduire les appels de contenu connecté en double, mais il n'est pas garanti qu'elle aboutisse à un seul appel par utilisateur. La durée du cache est comprise entre cinq minutes et quatre heures. Pour tous les détails, consultez [Mise en cache des réponses]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses).

### Quel est le comportement HTTP par défaut du contenu connecté ? {#what-is-the-connected-content-http-default-behavior}

{% multi_lang_include connected_content/sections.md section='default behavior' %}

{% multi_lang_include connected_content/sections.md section='http post' %}

### Que se passe-t-il si j'utilise le même appel de contenu connecté à plusieurs endroits ? {#what-happens-if-i-use-the-same-connected-content-call-in-multiple-places}

Chaque balise de contenu connecté est évaluée séparément, même si plusieurs balises utilisent la même URL et les mêmes paramètres. Lorsque l'URL et les paramètres de cache le permettent, les requêtes identiques peuvent être servies depuis le cache plutôt que de déclencher une nouvelle requête sortante (voir [Mise en cache des réponses]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses) pour plus de détails).