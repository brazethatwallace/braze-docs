---
nav_title: Débogueur de contenu connecté
article_title: Débogueur de contenu connecté
page_order: 3.5
description: "Cet article de référence explique comment utiliser le débogueur de contenu connecté pour résoudre les problèmes avant de lancer votre message."
---

# Débogueur de contenu connecté {#connected-content-debugger}

> Utilisez le débogueur de contenu connecté pour visualiser la requête et la réponse en direct de chaque appel de contenu connecté, afin de vérifier votre endpoint, vos en-têtes et vos étiquettes Liquid avant de lancer une Campaign ou un Canvas.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Connected Content Debugger' %}

## À propos du débogueur {#about-the-debugger}

Le contenu connecté vous permet d'enrichir vos messages avec des données en temps réel en effectuant un appel HTTP vers une API externe au moment du rendu, puis en insérant la réponse dans votre message avec Liquid. Comme cet appel se produit en dehors de Braze, il peut être difficile de voir exactement quelle requête Braze a envoyée, ce que l'endpoint a renvoyé, ou pourquoi un appel a échoué, avant qu'une Campaign ou un Canvas ne soit en production.

Le débogueur de contenu connecté vous aide à résoudre ces problèmes avant le lancement. Il vous montre la requête et la réponse en direct pour chaque appel de contenu connecté dans votre message, dans la section **Preview & Test**. Ainsi, vous pouvez confirmer que votre endpoint, vos en-têtes et vos étiquettes Liquid sont correctement configurés, le tout depuis le tableau de bord de Braze.

### Canaux pris en charge {#supported-channels}

Le débogueur de contenu connecté est disponible pour les canaux suivants :

- Content Cards
- E-mail
    - Inclut les modèles
    - Exclut les pieds de page et les pages d'abonnement
- Messages in-app
- Notifications push
- SMS/MMS/RCS
- Webhooks
    - Inclut les modèles
- WhatsApp

{% alert note %}
Pendant l'accès anticipé, le débogueur est disponible pour la plupart des canaux, mais pas encore pour KakaoTalk, LINE, les bannières ou les surfaces de composition non spécifiques à un canal (telles que les Content Blocks, l'étape de mise à jour utilisateur Canvas et l'étape de contexte). Si vous ne voyez pas le débogueur, le débogage du contenu connecté n'est peut-être pas encore pris en charge pour cette fonctionnalité.
{% endalert %}

## Utiliser le débogueur {#use-the-debugger}

Chaque fois que vous exécutez un aperçu, Braze affiche automatiquement les résultats des appels de contenu connecté dans l'onglet **Aperçu**. Pour utiliser le débogueur :

1. Configurez votre message avec la balise {% raw %}`{% connected_content %}`{% endraw %}.
2. Accédez à la section **Aperçu et test**. Si votre message inclut une balise de contenu connecté, vous pouvez voir un résumé indiquant le nombre d'appels de contenu connecté ainsi que les statuts de réussite et d'erreur.

![Section de contenu connecté dans la section Test.]({% image_buster /assets/img/connected_content/debugger1.png %})

{:start="3"}
3. Sélectionnez **Voir les détails** pour ouvrir le débogueur à côté de votre aperçu. Le panneau affiche un tableau avec l'URL et le résultat de chaque appel de contenu connecté.

![Appels de contenu connecté avec trois URL à examiner.]({% image_buster /assets/img/connected_content/debugger3.png %})

{:start="4"}
4. À côté de chaque URL et résultat, sélectionnez **Voir** pour afficher les en-têtes de requête et de réponse, le payload, la méthode, la durée et les informations de mise en cache.

![Appel de contenu connecté avec les détails de la requête et de la réponse.]({% image_buster /assets/img/connected_content/debugger4.png %})

{:start="5"}
5. Examinez les résultats, ajustez votre balise, vos en-têtes ou votre endpoint selon les besoins. Ensuite, générez un nouvel aperçu pour confirmer la correction.

Si votre modèle contient plus d'une balise {% raw %}`{% connected_content %}`{% endraw %}, le débogueur répertorie chaque appel effectué. Pour les canaux qui génèrent plusieurs corps de message à partir d'un seul modèle (par exemple, l'e-mail, qui génère des corps HTML, texte brut et AMP séparés, ou Quick Push, qui génère des corps distincts spécifiques à chaque appareil), le débogueur affiche tous les appels de contenu connecté effectués sur l'ensemble des corps, et pas uniquement celui que vous prévisualisez actuellement.

## Comprendre la sortie de débogage {#understand-the-debug-output}

Chaque appel de contenu connecté apparaît avec ses propres onglets **Response** et **Request**. L'onglet **Response** est affiché par défaut, car c'est généralement le premier indicateur pour confirmer si un appel a réussi.

### Détails de l'URL {#url-details}

| Champ | Description |
| --- | --- |
| URL | L'URL entièrement rendue que Braze a appelée, avec toutes les étiquettes Liquid résolues. |
| Method | La méthode HTTP utilisée (GET ou POST). |
| Status code | Le code de statut HTTP renvoyé par votre endpoint (par exemple, `200`, `404`, `500`). Consultez [Résolution des problèmes liés aux codes de réponse](#troubleshooting-response-codes) pour les codes spécifiques à Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Détails de l'URL" }

### Onglet Response {#response-tab}

| Champ | Description |
| --- | --- |
| Duration | Durée nécessaire pour compléter la requête, en secondes. La durée est affichée uniquement pour les appels en direct (non mis en cache). |
| Served from cache | Indique si cette réponse a été servie depuis le cache de contenu connecté de Braze plutôt que par un appel en direct à votre endpoint (`Yes` ou `No`). Un résultat mis en cache reflète une réponse antérieure, pas nécessairement l'état actuel de votre endpoint. |
| Response body | Le corps de la réponse renvoyé par votre endpoint. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Onglet Response" }

### Onglet Request {#request-tab}

| Champ | Description |
| --- | --- |
| Headers | Les en-têtes de requête envoyés par Braze, y compris ceux définis avec `:headers`. |
| Body | Le corps de la requête envoyé, le cas échéant (requêtes POST). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Onglet Request" }

## Masquage des identifiants {#credential-redaction}

Si votre balise de contenu connecté utilise `:basic_auth`, des en-têtes secrets courants, des clés ou d'autres [options d'identifiants d'authentification]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types), le débogueur masque ces valeurs dans l'onglet **Request** et les remplace par une série d'astérisques (*). Cela vous permet de confirmer que les identifiants ont été inclus dans la requête sans exposer les valeurs dans **Preview & Test**.

Les échecs d'authentification restent visibles même lorsque les identifiants sont masqués : si votre endpoint renvoie un code `401` ou `403`, ce code de statut apparaît normalement dans l'onglet **Response**, ce qui vous permet de savoir que votre requête a été rejetée en raison de l'authentification, même si l'identifiant lui-même est masqué.

## Résolution des problèmes liés aux codes de réponse {#troubleshooting-response-codes}

### Erreurs d'endpoint versus limites imposées par Braze {#endpoint-errors-versus-braze-imposed-limits}

Tous les codes de statut non-`2XX` dans l'onglet **Response** ne proviennent pas de votre endpoint. Braze applique ses propres limites sur les appels de contenu connecté, et celles-ci peuvent produire des réponses qui ressemblent à une erreur d'endpoint.

Si vous voyez des [codes de réponse]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#start-here-match-your-symptom) tels que `408`, `429`, `502`, `503`, `504` ou `599`, le problème se situe généralement du côté de Braze — lié à l'état de l'hôte, au délai d'expiration ou à la taille du payload. Si votre endpoint renvoie systématiquement des réponses volumineuses, envisagez de réduire le payload de la réponse aux seuls champs dont votre message a besoin.

### L'endpoint a renvoyé un code de statut inattendu {#endpoint-returned-an-unexpected-status-code}

Utilisez l'onglet **Request** pour confirmer l'URL exacte, les en-têtes et le corps envoyés par Braze. Une cause fréquente de réponses `4XX` inattendues est une étiquette Liquid dans l'URL, les en-têtes ou le corps qui ne s'est pas résolue comme prévu. Vérifiez que toutes les références {% raw %}`{{ }}`{% endraw %} pointent vers des champs qui existent pour l'utilisateur ou le contexte avec lequel vous effectuez la prévisualisation.

### La réponse semble obsolète {#response-looks-stale}

Vérifiez **Served from cache** dans l'onglet **Response**. Si la valeur affichée est `Yes`, le débogueur affiche une réponse précédemment mise en cache plutôt qu'un appel en temps réel. Ajoutez temporairement `:no_cache` à votre étiquette, ou attendez l'expiration du cache (selon `:cache_max_age`), pour confirmer le comportement actuel de l'endpoint.

## Articles connexes {#related-articles}

- [Référence du contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Effectuer un appel API de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [Résolution des problèmes liés aux webhooks et aux requêtes de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content)