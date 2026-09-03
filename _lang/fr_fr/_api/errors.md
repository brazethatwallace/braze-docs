---
nav_title: Erreurs et réponses
article_title: Erreurs et réponses d'API
description: "Cet article de référence couvre les diverses erreurs et réponses du serveur qui peuvent apparaître lors de l'utilisation de l'API Braze et la façon de les résoudre."
page_type: reference
page_order: 2.3

---
# Erreurs et réponses d'API {#api-errors-and-responses}

> Cet article de référence couvre les diverses erreurs et réponses du serveur qui peuvent apparaître lors de l'utilisation de l'API Braze et la façon de les résoudre.

## Réponses du serveur {#server-responses}

Si votre payload POST a été accepté par nos serveurs, les messages envoyés avec succès reçoivent la réponse suivante :

```json
{
  "message" : "success"
}
```

Notez que la réussite signifie uniquement que le payload de l'API RESTful était correctement formé et transmis à notre service de notifications push, d'e-mail ou d'autres services de communication. Cela ne signifie pas que les messages ont été effectivement distribués, car d'autres facteurs peuvent empêcher la distribution du message (par exemple, un appareil peut être hors ligne, le jeton push peut être rejeté par les serveurs d'Apple, ou vous avez peut-être fourni un ID utilisateur inconnu).

### Pourquoi ma requête renvoie-t-elle un succès alors qu'aucun message n'a été distribué ? {#why-does-my-request-return-success-when-no-message-was-delivered}

Une réponse `message: success` ou `2XX` signifie que Braze a accepté et mis en file d'attente la requête pour les endpoints concernés, et non que chaque destinataire a reçu un message. Pour la communication, la distribution dépend toujours de l'éligibilité du canal, des jetons, des erreurs du fournisseur et de la validation du contenu. Consultez le tableau des [erreurs fatales]({{site.baseurl}}/api/errors#fatal-errors) pour les erreurs HTTP qui bloquent les envois, ainsi que l'analyse de votre Campaign ou Canvas pour les indicateurs de distribution en aval.

Pour les endpoints tels que [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify), qui n'envoient pas de messages, un message de succès signifie uniquement que Braze a reçu la requête pour traitement. S'il n'y a aucune correspondance pour l'alias après le traitement, la requête est arrêtée.

Si votre message a été traité avec succès mais comporte des erreurs non fatales, vous recevez la réponse suivante :

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

En cas de succès, tous les messages qui n'ont pas été affectés par une erreur dans le tableau `errors` sont tout de même distribués. Si votre message comporte une erreur fatale, vous recevez la réponse suivante :

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## Réponses pour les ID d'envoi suivis {#responses-for-tracked-send-ids}

Les analyses sont toujours disponibles pour les Campaigns. De plus, les analyses sont disponibles pour une instance d'envoi spécifique d'une Campaign lorsque celle-ci est envoyée en tant que diffusion. Lorsque le suivi est disponible pour une instance d'envoi spécifique d'une Campaign, vous recevez la réponse suivante :

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

L'ID d'envoi fourni peut être utilisé comme paramètre pour l'endpoint `/send/data_series` afin de récupérer les analyses spécifiques à l'envoi.

## Erreurs {#errors}

L'élément de code de statut d'une réponse serveur est un nombre à 3 chiffres dont le premier chiffre définit la classe de la réponse.

- La **classe 2XX** de code de statut (non fatale) indique que **votre requête** a été reçue, comprise et acceptée avec succès.
- La **classe 4XX** de code de statut (fatale) indique une **erreur client**. Consultez le tableau des erreurs fatales pour obtenir la liste complète des codes d'erreur 4XX et leurs descriptions.
- La **classe 5XX** de code de statut (fatale) indique une **erreur serveur**. Il existe plusieurs causes potentielles, par exemple le serveur auquel vous essayez d'accéder n'est pas en mesure d'exécuter la requête, le serveur est en maintenance et ne peut pas exécuter la requête, ou le serveur subit un niveau de trafic élevé. Lorsque cela se produit, nous vous recommandons de relancer votre requête avec des délais exponentiels. En cas d'incident ou de panne, Braze n'est pas en mesure de rejouer les appels à la REST API qui ont échoué pendant la fenêtre d'incident. Vous devez relancer tout appel ayant échoué pendant la fenêtre d'incident.
  - Une **erreur 502** est un échec avant d'atteindre le serveur de destination.
  - Une **erreur 503** signifie que la requête a atteint le serveur de destination, mais qu'il n'est pas possible de la traiter en raison d'une capacité insuffisante, d'un problème réseau, ou autre.
  - Une **erreur 504** indique qu'un serveur n'a pas reçu de réponse d'un autre serveur en amont.

### Erreurs fatales {#fatal-errors}

Les codes de statut et messages d'erreur associés suivants sont renvoyés si votre requête rencontre une erreur fatale.

{% alert warning %}
Tous les codes d'erreur suivants indiquent qu'aucun message n'est envoyé.
{% endalert %}

| Code d'erreur | Description |
|---|---|
| `5XX Internal Server Error` | Relancez votre requête avec des délais exponentiels.|
| `400 Bad Request` | Syntaxe incorrecte. Un JSON non valide renvoie HTTP 400. Le champ `error` peut inclure un message indiquant que vous devez transmettre du `application/json` valide dans le corps de la requête, ou `Error while parsing request body. Please check your syntax.` Voir [Erreur lors de l'analyse du corps de la requête](#error-while-parsing-request-body).|
| `400 No Recipients` | Il n'y a pas d'ID externes, d'ID de segment, ni de jetons push dans la requête.|
| `400 Invalid Campaign ID` | Aucune Campaign API n'a été trouvée pour l'ID de Campaign fourni.|
| `400 Message Variant Unspecified` | Vous fournissez un ID de Campaign mais pas d'ID de variante de message.|
| `400 Invalid Message Variant` | Vous avez fourni un ID de Campaign valide, mais l'ID de variante de message ne correspond à aucun des messages de cette Campaign.|
| `400 Mismatched Message Type` | Vous avez fourni une variante de message du mauvais type de message pour au moins un de vos messages.|
| `400 Invalid Extra Push Payload` | Vous fournissez la clé `extra` pour `apple_push` ou `android_push` mais ce n'est pas un dictionnaire.|
| `400 Max Input Length Exceeded` | Pour `/users/track`, cette erreur est causée par le dépassement du nombre maximum d'objets autorisés dans une seule requête. La limite dépend du modèle de limite de débit : pour la plupart des clients, chaque requête prend en charge jusqu'à 75 objets au total combinés entre `attributes`, `events` et `purchases`. Pour les clients soumis aux limites de débit héritées, chaque tableau prend en charge jusqu'à 75 objets indépendamment. Pour plus d'informations, consultez [POST : Créer et mettre à jour des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track).|
| `400 The max number of external_ids and aliases per request was exceeded` | Causé par l'appel de plus de 50 ID externes.|
| `400 The max number of ids per request was exceeded` | Causé par l'appel de plus de 50 ID externes.|
| `400 No message to send` | Aucun payload n'est spécifié pour le message.|
| `400 Slideup Message Length Exceeded` | Le message contextuel contient plus de 140 caractères.|
| `400 Apple Push Length Exceeded` | Le payload JSON dépasse 1 912 octets.|
| `400 Android Push Length Exceeded` | Le payload JSON dépasse 4 000 octets.|
| `400 Bad Request` | Impossible d'analyser la date/heure `send_at`.|
| `400 Bad Request` | Dans votre requête, `in_local_time` est défini sur true mais `time` est déjà passé dans le fuseau horaire de votre entreprise.|
| `401 Unauthorized` | Clé API non valide. Les causes courantes incluent :<br><br>- **En-tête Authorization manquant ou mal formé.** La valeur de l'en-tête doit être `Bearer` suivi d'un espace puis de votre clé API : `Authorization: Bearer YOUR-API-KEY`. Les erreurs courantes incluent l'omission de `Bearer`, l'omission de la clé après `Bearer`, ou l'encapsulation de la valeur entre guillemets.<br>- **Mauvais endpoint REST.** Vous envoyez la requête à la mauvaise [instance]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Par exemple, si votre compte est sur notre instance UE (`https://dashboard-01.braze.eu`), la requête doit être envoyée à `https://rest.fra-01.braze.eu`.<br>- **Permissions insuffisantes.** Chaque clé API est limitée à un espace de travail et un ensemble de permissions spécifiques. Vérifiez les permissions de la clé sous **Paramètres** > **Clés API** dans le tableau de bord.<br>- **Mauvaise clé API.** Les clés API sont spécifiques à l'espace de travail. Une clé d'un espace de travail ne peut pas être utilisée pour authentifier les requêtes d'un autre espace de travail. |
| `403 Forbidden` | Le forfait ne prend pas en charge cette fonctionnalité, ou le compte est autrement désactivé.|
| `403 Access Denied` | La clé REST API que vous utilisez ne dispose pas de permissions suffisantes. Les causes courantes incluent : {::nomarkdown}<ul><li><strong>La clé API est antérieure à la fonctionnalité.</strong> Si la clé API a été créée avant le lancement d'une fonctionnalité (comme les groupes d'abonnement ou les catalogues), la clé n'hérite pas automatiquement de ces permissions. Créez une nouvelle clé API avec les permissions requises sous <strong>Paramètres</strong> &gt; <strong>Clés API</strong>.</li><li><strong>Permission spécifique à l'endpoint manquante.</strong> Chaque endpoint API nécessite un périmètre de permission spécifique (par exemple, <code>users.track</code> ou <code>email.status</code>). Vérifiez que les permissions de la clé correspondent à l'endpoint que vous appelez.</li><li><strong>Barre oblique finale ou faute de frappe dans l'URL.</strong> Par exemple, <code>/users/track/</code> (avec une barre oblique finale) au lieu de <code>/users/track</code> peut produire des erreurs inattendues.</li></ul>{:/}|
| `404 Not Found` | URL non valide. |
| `415 Unsupported Media Type` | L'en-tête de requête `Content-Type` est manquant ou incorrect. Dans la page **Paramètres**, ajoutez `Content-Type` avec la valeur `application/json`. |
| `429 Rate Limited` | Limite de débit dépassée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erreurs fatales" }

### Erreur lors de l'analyse du corps de la requête {#error-while-parsing-request-body}

Braze renvoie HTTP 400 lorsque le corps de la requête n'est pas un JSON valide. Cela s'applique aux endpoints REST qui acceptent un corps JSON, tels que POST, PUT et PATCH.

Le champ `error` inclut un message indiquant que vous devez transmettre du `application/json` valide dans le corps de la requête. Vous pouvez également voir `Error while parsing request body. Please check your syntax.`

Les causes courantes incluent les virgules en fin de ligne, les commentaires à l'intérieur du JSON, les chaînes de caractères entre guillemets simples, une accolade ouvrante `{` supplémentaire avant le payload, ou l'envoi d'une chaîne concaténée au lieu d'un objet encodé en JSON.

Avant de relancer :

1. Validez le payload avec un linter JSON.
2. Définissez `Content-Type: application/json` et envoyez du JSON encodé en UTF-8.
3. Confirmez que votre client HTTP encode l'objet en JSON plutôt que de concaténer des chaînes brutes.

Pour les limites de taille du payload et les limites d'objets par requête de `/users/track`, consultez [Pourquoi est-ce que j'obtiens `400 Bad Request` avec une erreur de syntaxe ou d'analyse ?]({{site.baseurl}}/api/endpoints/user_data/post_user_track#why-do-i-get-400-bad-request-with-a-bad-syntax-or-parse-error).