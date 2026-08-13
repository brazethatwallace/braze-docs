---
nav_title: PassKit
article_title: PassKit
alias: /partners/passkit/
description: "Cet article de référence décrit le partenariat entre Braze et Passkit. Ce partenariat vous permet d'étendre votre portée mobile en intégrant les pass Apple Wallet et Google Pay à l'expérience de vos clients."
page_type: partner
search_tag: Partner

---

# PassKit

> PassKit vous permet d'étendre votre portée mobile en intégrant les pass Apple Wallet et Google Pay à l'expérience de vos clients. Créez, gérez, distribuez et analysez facilement les performances des coupons numériques, des cartes de fidélité, des cartes de membre, des billets et bien plus encore, sans que vos clients aient besoin d'une autre application.

_Cette intégration est maintenue par Passkit._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et PassKit vous permet d'augmenter et de mesurer l'engagement de vos campagnes en ligne en fournissant instantanément des pass Apple Wallet et Google Pay personnalisés. Vous pouvez ensuite analyser l'utilisation et effectuer des ajustements en temps réel pour augmenter le trafic en magasin en déclenchant des messages géolocalisés et des mises à jour personnalisées et dynamiques sur le portefeuille mobile de votre client.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte PassKit | Vous devez disposer d'un compte PassKit et d'un gestionnaire de compte PassKit. |
| `userDefinedID` | Pour mettre à jour de manière appropriée les événements personnalisés et les attributs personnalisés de vos utilisateurs entre PassKit et Braze, vous devez définir l'ID externe de Braze comme `userDefinedID`. Ce `userDefinedID` est utilisé lors des appels d'API aux endpoints PassKit. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze  | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Pour enrichir davantage les expériences de portefeuille mobile de vos clients, depuis votre tableau de bord PassKit, vous pouvez choisir de transmettre des données à Braze par le biais de l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) de Braze.

Voici des exemples de données à partager depuis PassKit :
- **Pass créé** : lorsqu'un client clique sur le lien d'un pass et qu'un pass lui est présenté pour la première fois.
- **Installation du pass** : lorsque le client ajoute et enregistre le pass dans son application de portefeuille.
- **Mises à jour du pass** : lorsqu'un pass est mis à jour.
- **Suppression du pass** : lorsqu'un client supprime le pass de son application de portefeuille.

Une fois les données transmises à Braze, vous pouvez créer des audiences, personnaliser le contenu via Liquid et déclencher des Campaigns ou des Canvas une fois ces actions effectuées.

## Connecter PassKit à Braze {#connect-passkit-to-braze}

Pour transmettre des données depuis PassKit, assurez-vous d'avoir défini votre ID externe Braze comme `externalId` de PassKit.

1. Dans **Settings**, sous **Integrations** de votre projet ou programme PassKit Pass, cliquez sur **Connect** sous l'onglet **Braze**.<br>![La vignette d'intégration Braze dans la plateforme PassKit.]({% image_buster /assets/img/passkit/passkit5.png %}){: style="max-width:80%"}<br><br>
2. Renseignez votre clé API Braze, l'URL de votre endpoint et donnez un nom à votre connecteur.<br><br>
3. Activez **Enable Integration** et les événements que vous souhaitez dans Braze pour déclencher ou personnaliser vos messages.<br>![La vignette d'intégration PassKit Braze étendue pour accepter la clé API, l'URL de l'endpoint, le nom de l'intégration, les paramètres d'activation, les paramètres d'adhésion et les paramètres de pass.]({% image_buster /assets/img/passkit/passkit4.png %}){: style="max-width:70%"}

## Créer un pass à l'aide d'un lien SmartPass {#create-pass-using-a-smartpass-link}

Dans Braze, vous pouvez configurer un lien SmartPass pour générer une URL unique permettant à vos clients d'installer leur pass sur Android ou iOS. Pour ce faire, vous devez définir un payload de données SmartPass chiffré qui peut être appelé depuis un bloc de contenu Braze. Ce [bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) peut ensuite être réutilisé pour les futurs pass et coupons. Les éléments suivants sont utilisés lors de votre intégration :

- **URL PassKit** : l'URL de votre PassKit est une URL unique pour votre programme PassKit.<br>Chaque programme possède une URL unique, que vous trouverez dans l'onglet **Distribution** de votre programme ou projet PassKit. (par exemple, https://pub1.pskt.io/c/ww0jir)<br><br>
- **Secret PassKit** : en plus de l'URL, vous devez avoir à portée de main la clé PassKit pour ce programme.<br>Elle est disponible sur la même page que l'URL de PassKit.<br><br>
- **ID du programme (ou du projet)** : votre ID de programme PassKit est nécessaire pour créer l'URL du SmartPass. <br>Vous pouvez le trouver dans l'onglet **Settings** de votre projet ou programme.

Pour plus d'informations sur la création de liens SmartPass chiffrés, consultez cet [article de PassKit](https://help.passkit.com/en/articles/3742778-hashed-smartpass-links).

### Étape 1 : Définir le payload des données de votre pass {#passkit-integrations}

Tout d'abord, vous devez définir le coupon ou le payload du membre.

Vous pouvez inclure de nombreux composants dans votre payload, mais voici deux éléments importants à noter :

| Composant | Requis | Type | Description |
| --------- | -------- | ---- | ----------- |
| `person.externalId` | Requis | Chaîne de caractères | Défini comme l'ID externe de Braze, il est crucial pour que les rappels de PassKit vers Braze fonctionnent, car il permet aux utilisateurs de l'entreprise d'obtenir des coupons pour plusieurs offres au cours d'une seule Campaign. Non imposé comme unique. |
| `members.member.externalId` | Facultatif | Chaîne de caractères | Défini comme l'ID externe de Braze, vous pouvez utiliser votre ID externe pour mettre à jour le pass de membre. La définition de ce champ impose l'unicité de l'utilisateur au sein du programme d'adhésion. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Étape 1 : Définir le payload des données de votre pass" }

Pour une liste complète des champs disponibles, de leurs types et des descriptions utiles, consultez la [documentation GitHub de PassKit](https://github.com/PassKit/smart-pass-link-from-csv-generator).

#### Exemple de payload {#example-payload}
{% raw %}
```liquid
{
  "members.member.externalId": "{{${user_id}}}",
  "members.member.points": "100",
  "members.tier.name": "current_customer",
  "person.displayName": "{{${first_name}}} {{${last_name}}}",
  "person.externalId": "{{${user_id}}}",
  "universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"
}
```
{% endraw %}

### Étape 2 : Créer et encoder une variable de payload non définie {#step-2-create-and-encode-an-undefined-payload-variable}

Créez et nommez un nouveau bloc de contenu en accédant à **Contenu** > **Blocs de contenu** dans le tableau de bord de Braze.

Sélectionnez **Créer un bloc de contenu** pour commencer.

Ensuite, vous devez définir votre **balise Liquid de bloc de contenu**. Après avoir enregistré ce bloc de contenu, cette balise Liquid peut être référencée lors de la rédaction de messages. Dans cet exemple, nous avons attribué à la balise Liquid la valeur {% raw %}`{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %}.

Dans ce bloc de contenu, nous n'inclurons pas directement le payload, mais nous le référencerons dans une variable {% raw %}`{{passData}}`{% endraw %}. Le premier extrait de code que vous devez ajouter à votre bloc de contenu capture un encodage Base64 de la variable {% raw %}`{{passData}}`{% endraw %}.
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passDatapassData|base64_encode}}{% endcapture %}
```
{% endraw %}

### Étape 3 : Créer votre signature de chiffrement à l'aide d'un hachage HMAC SHA1 {#step-3-create-your-encryption-signature-using-a-sha1-hmac-hash}

Ensuite, vous allez créer votre signature de chiffrement en utilisant un hachage [SHA1 HMAC](https://en.wikipedia.org/wiki/HMAC) de l'URL du projet et du payload.

Le deuxième extrait de code que vous devez ajouter à votre bloc de contenu capture l'URL à utiliser pour le hachage.
{% raw %}
```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```
{% endraw %}

Ensuite, vous devez générer une signature à l'aide de ce hachage et de votre `Project Secret`. Cela peut être fait en incluant un troisième extrait de code :
{% raw %}
```liquid
{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}
```
{% endraw %}

Enfin, ajoutez la signature à l'URL complète à l'aide du cinquième extrait de code :
{% raw %}
```liquid
{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}{% endcapture %}
```
{% endraw %}

### Étape 4 : Imprimer votre URL {#step-4-print-your-url}

Enfin, assurez-vous d'appeler votre URL finale afin qu'elle affiche votre URL SmartPass dans votre message.
{% raw %}
```liquid
{{longURL}}
```
{% endraw %}

À ce stade, vous avez créé un bloc de contenu qui ressemble à ceci :

{% raw %}
```liquid
{% capture base64JsonPayload %}{{passData|base64_encode}}{% endcapture %}

{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}

{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}

{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}&utm_source=braze&utm_campaign={{campaign.${name}}}{% endcapture %}{% capture longURL %}{{longURL | url_encode}}{% endcapture %}

{{longURL}}
```
{% endraw %}

Dans cet exemple, des paramètres UTM ont été ajoutés pour suivre la source de ces installations jusqu'à Braze et cette Campaign.

{% alert tip %}
N'oubliez pas d'enregistrer votre bloc de contenu avant de quitter la page.
{% endalert %}

### Étape 5 : Assembler tous les éléments {#step-5-putting-it-all-together}

Une fois ce bloc de contenu créé, il peut être réutilisé ultérieurement.

Vous remarquerez peut-être que deux variables ne sont pas définies dans l'exemple de bloc de contenu.<br>
{% raw %}`{{passData}}`{% endraw %} - Votre payload de données de pass JSON défini à l'[étape 1](#passkit-integrations) <br>
{% raw %}`{{projectUrl}}`{% endraw %} - L'URL de votre projet ou programme que vous trouverez dans l'onglet de distribution de votre projet PassKit.

Cette décision est intentionnelle et favorise la réutilisation du bloc de contenu. Comme ces variables sont uniquement référencées et ne sont pas créées dans le bloc de contenu, elles peuvent être modifiées sans avoir à recréer le bloc de contenu.

Par exemple, vous souhaitez peut-être modifier l'offre de lancement pour inclure davantage de points initiaux dans votre programme de fidélité, ou peut-être souhaitez-vous créer une carte de membre ou un coupon secondaire. Ces scénarios nécessiteraient différents `projectURLs` PassKit ou différents payloads de pass, que vous définiriez par Campaign dans Braze.

#### Composition du corps du message {#composing-the-message-body}

Vous devez capturer ces deux variables dans le corps de votre message, puis appeler votre bloc de contenu.
Capturez votre payload JSON minifié à partir de l'[étape 1](#passkit-integrations) :

**Attribuer l'URL du projet**
{% raw %}
```liquid
{% assign projectUrl = "https://pub1.pskt.io/c/ww0jir" %}
```
{% endraw %}

**Capturer le JSON**
{% raw %}
```liquid
{% capture passData %}{"members.member.externalId": "{{${user_id}}}","members.member.points": "100","members.tier.name": "current_customer","person.displayName": "{{${first_name}}} {{${last_name}}}","person.externalId": "{{${user_id}}}","universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"}{% endcapture %}
```
{% endraw %}

**Référencer le bloc de contenu que vous venez de créer**
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

Le corps de votre message devrait ressembler à ceci :
![Image du compositeur de messages du bloc de contenu avec le JSON capturé et la référence du bloc de contenu affichée.]({% image_buster /assets/img/passkit/passkit1.png %}){: style="max-width:70%"}

L'URL de sortie de l'exemple est la suivante :
![URL de sortie qui inclut une longue chaîne de caractères alphanumériques générée de manière aléatoire.]({% image_buster /assets/img/passkit/passkit2.png %}){: style="max-width:70%"}

L'URL de sortie sera longue. La raison en est qu'elle contient toutes les données du pass et intègre une sécurité de premier ordre pour garantir l'intégrité des données et empêcher toute modification via l'URL. Si vous utilisez le SMS pour distribuer cette URL, vous pouvez la faire passer par un processus de raccourcissement de lien tel que [bit.ly](https://dev.bitly.com/v4/#operation/createFullBitlink). Cela peut se faire par le biais d'un appel de contenu connecté à un endpoint bit.ly.

## Mettre à jour le pass à l'aide du webhook PassKit {#update-pass-using-the-passkit-webhook}

Dans Braze, vous pouvez configurer une campagne webhook ou un webhook dans un Canvas pour mettre à jour un pass existant en fonction du comportement de votre utilisateur. Consultez les liens suivants pour obtenir des informations sur les endpoints PassKit utiles.
- [Projets de membres](https://docs.passkit.io/protocols/member/)
- [Projets de coupons](https://docs.passkit.io/protocols/coupon/)
- [Projets de vols](https://docs.passkit.io/protocols/boarding/)

### Paramètres du payload {#payload-parameters}

Avant de commencer, voici les paramètres de payload JSON courants que vous pouvez inclure dans vos webhooks de création et de mise à jour vers PassKit.

| Données | Type | Description |
| ---- | ---- | ----------- |
| `externalId` | Chaîne de caractères | Permet d'ajouter un identifiant unique à l'enregistrement du pass pour assurer la compatibilité avec un système existant utilisant des identifiants clients uniques (par exemple, des numéros de membre). Vous pouvez récupérer les données du pass en utilisant cet endpoint via `userDefinedId` et `campaignName` à la place de l'ID du pass. Cette valeur doit être unique au sein d'une Campaign, et une fois cette valeur définie, elle ne peut pas être modifiée.<br><br>Pour l'intégration de Braze, nous vous recommandons d'utiliser l'ID externe de Braze : {% raw %}`{{${user_id}}}`{% endraw %} |
| `campaignId` (coupon) <br><br> `programId` (adhésion) | Chaîne de caractères | L'ID du modèle de Campaign ou de programme que vous avez créé dans PassKit. Pour le trouver, rendez-vous dans l'onglet **Settings** de votre projet PassKit Pass. |
| `expiryDate` | Date/heure IO8601 | La date d'expiration du pass. Après la date d'expiration, le pass est automatiquement annulé (voir `isVoided`). Cette valeur remplacera le modèle et la valeur de la date de fin de Campaign. |
| `status` | Chaîne de caractères | L'état actuel d'un coupon, tel que `REDEEMED` ou `UNREDEEMED`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paramètres du payload" }

### Étape 1 : Créer votre modèle de webhook Braze {#step-1-create-your-braze-webhook-template}

Pour créer un modèle de webhook PassKit à utiliser dans de futures Campaigns ou Canvas, accédez à la section **Modèles et médias** dans le tableau de bord de Braze. Si vous souhaitez créer une campagne webhook PassKit unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d'une nouvelle campagne.

Une fois que vous avez sélectionné le modèle de webhook PassKit, vous devriez voir ce qui suit :
- **URL du webhook** : `https://api-pub1.passkit.io/coupon/singleUse/coupon`
- **Corps de la requête** : texte brut

#### En-têtes de requête et méthode {#request-headers-and-method}

PassKit requiert un `HTTP Header` pour l'autorisation qui inclut votre clé API PassKit encodée en base 64. Les éléments suivants seront déjà inclus dans le modèle en tant que paire clé-valeur, mais dans l'onglet **Settings**, vous devez remplacer `<PASSKIT_LONG_LIVED_TOKEN>` par votre jeton PassKit. Pour récupérer votre jeton, accédez à votre projet/programme PassKit, puis accédez à **Settings > Integrations > Long Lived Token**.

{% raw %}
- **Méthode HTTP** : PUT
- **En-tête de la requête** :
  - **Authorization** : Bearer `<PASSKIT_LONG_LIVED_TOKEN>`
  - **Content-Type** : application/json
{% endraw %}

#### Corps de la requête {#request-body}

Pour configurer le webhook, renseignez les nouveaux détails de l'événement dans le corps de la requête, y compris les paramètres de payload nécessaires à votre cas d'usage :

```json
{% raw %}{
  "externalId": "{{${user_id}}}",
  "campaignId": " 2xa1lRy8dBz4eEElBfmIz8",
  "expiryDate": "2020-05-10T00:00:00Z"
}{% endraw %}
```

### Étape 2 : Prévisualiser la requête {#step-2-preview-your-request}

Votre texte brut sera automatiquement mis en évidence s'il s'agit d'une balise Braze applicable.

Prévisualisez votre requête dans le panneau **Prévisualisation** ou accédez à l'onglet **Test**, où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser le vôtre pour tester votre webhook.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page ! <br>Les modèles de webhook mis à jour se trouvent dans la liste **Modèles de webhook enregistrés** lors de la création d'une nouvelle [campagne webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook).
{% endalert %}

## Récupérer les détails du pass via le contenu connecté {#retrieve-pass-details-via-connected-content}

Outre la création et la mise à jour des pass, vous pouvez également récupérer les métadonnées des pass de vos utilisateurs via le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) de Braze afin d'incorporer les détails personnalisés des pass dans vos campagnes de communication.

**Appel de contenu connecté PassKit**

{% raw %}
```liquid
{% connected_content  https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer <PASSKIT_LONG_LIVED_TOKEN>","Content-Type": "application/json"} :save passes %}

{{passes.status}}
```
{% endraw %}

**Exemples de réponses Liquid**

{% tabs local %}
{% tab passes redemptionDetails %}

```json
{
    "redemptionDate": null,
    "redemptionCode": "",
    "lat": 0,
    "lon": 0,
    "alt": 0,
    "redemptionSource": "",
    "redemptionReference": "",
    "transactionReference": "",
    "transactionAmount": 0
}
```

{% endtab %}
{% tab passes status %}
```
UNREDEEMED
```
{% endtab %}
{% endtabs %}