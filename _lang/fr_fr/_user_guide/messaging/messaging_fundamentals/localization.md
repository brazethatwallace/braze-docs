---
nav_title: Localisation
article_title: Localisation
page_order: 8
description: "Cet article de référence couvre les bases de la localisation, présente les avantages des différentes approches d'orchestration pour les Campaigns et les Canvas, et répertorie les différentes façons dont les utilisateurs peuvent gérer la personnalisation dans leurs messages."
tool:
    - Campaigns
    - Canvas
---

# Localisation {#localization}

> Pour les entreprises ayant des clients dans de nombreux pays, prendre en charge la localisation dès le début de votre parcours avec Braze peut faire gagner du temps et des ressources à votre entreprise.

## Fonctionnement {#how-it-works}

Les informations de localisation sont stockées dans le profil d'un utilisateur en fonction des données que vous collectez à l'aide d'un [SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration/) (automatiquement) ou de la [REST API]({{ site.baseurl }}/api/endpoints/user_data/post_user_track). La localisation contient la langue et un identifiant de région. Ces informations sont disponibles dans l'outil de segmentation de Braze sous **Pays** et **Langue**.

{% alert tip %}
Pour des détails techniques sur la façon dont la localisation est collectée par nos SDK, consultez la documentation officielle [iOS](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html), [Android](http://developer.android.com/reference/java/util/Locale.html) et [Web](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language).
{% endalert %}

## Gestion des traductions {#translation-management}

Considérez les approches suivantes pour gérer vos traductions.

{% tabs local %}
{% tab campaign %}
### Un modèle pour tous {#one-template-for-all}

Dans cette approche, la localisation est appliquée à un seul modèle dans Braze à l'aide de [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/). Après l'envoi, le tableau de bord fournit des analyses agrégées de la Campaign. L'engagement au niveau de l'utilisateur peut être mesuré à l'aide d'entonnoirs de Segments personnalisés, par exemple en combinant les filtres **Pays** et **Campaign reçue**.

| Avantages | Considérations |
| --- | --- |
| - Approche centralisée<br>- Temps de création d'e-mail réduit, pas besoin de créer un e-mail plusieurs fois | - Création manuelle des rapports<br>- Le rapport de Campaign affiche des indicateurs agrégés plutôt que des indicateurs par pays<br>- Nécessité de tester minutieusement le Liquid pour s'assurer qu'il s'affiche comme prévu<br>- Selon la façon dont vous récupérez la valeur du pays ou le nombre de pays que vous avez configurés, il peut être difficile de tester chaque pays<br>- Plus difficile de planifier des envois à des heures spécifiques selon les fuseaux horaires<br>- Plus difficile à utiliser si vous souhaitez envoyer un contenu distinct par pays. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="One template for all" }

### Un modèle par pays {#one-template-per-country}

Cette approche sépare les modèles en différentes localisations d'envoi. Après l'envoi, le tableau de bord affiche les analyses d'envoi pour chaque pays séparément, et tous les événements [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/#access-currents) en aval au niveau de l'utilisateur seront également liés à une Campaign spécifique.

- Les modèles bénéficient de l'implémentation d'[étiquettes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/#tags) à des fins de maintenance et de suivi.
- Les Campaigns peuvent hériter des configurations du même [modèle Braze]({{site.baseurl}}/user_guide/messaging/templates/) et des [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/) (tels que les [modèles d'e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/) contenant du Liquid).
- Les Campaigns et modèles préexistants peuvent être [dupliqués]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/duplicating/) pour accélérer la mise en œuvre.

| Avantages | Considérations |
| --- | --- |
| - Évolutif pour plusieurs emplacements<br>- Rapports sur le chiffre d'affaires par pays dans Braze (par exemple par Campaign)<br>- Flexibilité si le contenu diffère considérablement d'un pays à l'autre | - Nécessite une structuration stratégique<br>- Effort de création plus important (par exemple des Campaigns distinctes pour chaque pays) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="One template per country" }
{% endtab %}

{% tab canvas %}
### Un parcours pour tous {#one-journey-for-all}

Dans cette approche, la localisation est gérée au sein des [bases de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_basics/#building-the-customer-journey) et du Liquid pour définir les messages pour chaque utilisateur.

Après l'envoi d'un Canvas, le tableau de bord fournit des [analyses Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) agrégées, tandis que l'engagement au niveau de l'utilisateur peut être mesuré via des [entonnoirs de Segments]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size/) personnalisés, par exemple en combinant les filtres [**Pays**]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#country) et [**Étape Canvas reçue**]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#received-canvas-step).

| Avantages | Considérations |
| --- | --- |
| - Approche centralisée<br>- Temps de création d'e-mail réduit — pas besoin de créer un e-mail plusieurs fois. | - Création manuelle des rapports<br>- Le rapport Canvas affiche des indicateurs agrégés plutôt que des indicateurs par pays<br>- Nécessité de tester minutieusement le Liquid pour s'assurer qu'il s'affiche comme prévu<br>- Selon la façon dont vous récupérez la valeur du pays ou le nombre de pays que vous avez configurés, il peut être difficile de tester chaque pays<br>- Plus difficile de planifier des envois à des heures spécifiques selon les fuseaux horaires<br>- Plus difficile à utiliser si vous souhaitez envoyer un contenu distinct par pays. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="One journey for all" }

### Un parcours par pays {#one-journey-per-country}

Dans cette approche, le générateur de parcours [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) offre la flexibilité de créer des parcours utilisateur via plusieurs [composants Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/). Ces composants peuvent être [dupliqués]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/duplicating/) au niveau du composant et du parcours global.

La localisation peut être réalisée avec les méthodes suivantes :

- Des Canvas distincts par pays, ce qui garantit que les parcours utilisateur complexes sont définis en haut de l'entonnoir à l'aide de filtres d'audience
- Des parcours utilisateur personnalisés par pays, grâce à l'implémentation de [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) pour segmenter intuitivement les utilisateurs à grande échelle pour chaque parcours en créant des fils de messages distincts pour chaque pays dans un seul Canvas

Une fois envoyé, le tableau de bord fournit des analyses dynamiques par pays et au sein des événements [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/#access-currents) au niveau de l'utilisateur en fonction de la localisation actuelle du client.

| Avantages | Considérations |
| --- | --- |
| - Rapports sur le chiffre d'affaires par pays dans Braze (par exemple par Canvas, variante ou étape)<br>- Flexibilité si le contenu diffère considérablement d'un pays à l'autre<br>- Possibilité d'ajouter d'autres canaux dans le parcours à l'avenir | - Nécessite une structuration stratégique<br>- Effort de création plus important (par exemple des étapes de message distinctes pour chaque pays)<br>- Le Canvas peut devenir volumineux et difficile à lire si vous avez des parcours personnalisés et complexes pour chaque pays dans un seul Canvas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="One journey per country" }
{% endtab %}
{% endtabs %}

## Envoi de messages traduits {#sending-translated-messages}

Pour envoyer des messages personnalisés en fonction de la langue, de la localisation ou des attributs personnalisés d'un utilisateur, utilisez l'une des méthodes suivantes.

### Étiquettes Liquid de traduction (recommandé) {#translation-liquid-tag}

Braze prend en charge une étiquette Liquid {% raw %}`{% translation salutation %}Hello!{% endtranslation %}`{% endraw %} pour cibler les utilisateurs dans différentes langues avec un seul message.

Pour un guide complet, consultez le [guide sur l'utilisation des étiquettes de traduction]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/).

### Approches alternatives {#alternative-approaches}

{% tabs local %}
{% tab Liquid personnalisé %}
Vous pouvez coller manuellement votre contenu dans le corps de votre message et utiliser [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/) pour afficher [conditionnellement]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/#conditional-logic) la bonne langue au destinataire. Pour ce faire :

1. Rédigez votre message, puis sélectionnez **Langue** pour générer la logique conditionnelle Liquid pour chacune de vos langues sélectionnées.
2. Vous pouvez utiliser le modèle Liquid suivant pour construire votre message. Pour chaque champ avec un modèle, vous devez saisir les variantes après le segment de modèle entre crochets. La variante doit correspondre au code de langue référencé entre crochets avant elle.
    {% raw %}
    ```liquid
    {% if ${language} == 'en' %}
    This is a message in English from Braze!
    {% elsif ${language} == 'es' %}
    Este es un mensaje en español de Braze !
    {% elsif ${language} == 'zh' %}
    这是一条来自Braze的中文消息。
    {% else %}
    This is a message from Braze! This will go to anyone who does not match the other specified languages!
    {% endif %}
    ```
    {% endraw %}
3. Testez votre message avant de l'envoyer en saisissant l'ID ou l'e-mail d'un utilisateur pour vérifier comment un message apparaîtrait à un individu en fonction de sa langue.

{% alert tip %}
Nous recommandons toujours d'inclure une instruction {% raw %}`{% else %}`{% endraw %} dans vos messages. Bien que la plupart des utilisateurs verront le message dans leur langue spécifique, le texte sera visible pour ceux qui :
- N'ont pas de langue sélectionnée
- Ont une langue que Braze ne prend pas en charge
- Ont un appareil dont la langue est indétectable
{% endalert %}
{% endtab %}

{% tab Content Blocks %}
Les [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/) de Braze sont des blocs de contenu réutilisables. Lorsqu'un bloc est modifié, toutes les références à ce bloc sont mises à jour. Par exemple, les mises à jour d'un en-tête ou d'un pied de page d'e-mail seront reflétées dans tous les e-mails, ou pour héberger des traductions. Ces blocs peuvent également être [créés]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/#create-content-block) et [mis à jour]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) via la REST API, et les utilisateurs peuvent télécharger des traductions de manière programmatique.

Lors de la création d'une Campaign dans le tableau de bord, les Content Blocks peuvent être référencés à l'aide de l'étiquette {% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %}. Ces blocs peuvent contenir toutes les traductions hébergées dans une logique conditionnelle pour chaque langue, comme indiqué dans l'option 1, ou un bloc distinct pour chaque langue peut être utilisé.

Les Content Blocks peuvent également être utilisés comme processus de gestion des traductions où le contenu nécessitant une traduction est hébergé dans un Content Block, récupéré, traduit, puis mis à jour :
1. Créez manuellement un Content Block dans le tableau de bord avec l'étiquette « Needs Translation ».
2. Votre service effectue une récupération nocturne de tous les Content Blocks à l'aide de l'[endpoint `/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/).
3. Votre service récupère les détails de chaque Content Block via l'[endpoint `/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) pour voir quels blocs sont étiquetés pour la traduction.
4. Votre service de traduction traduit le corps de tous les Content Blocks « Needs Translation ».
5. Votre service appelle l'[endpoint `/content_block/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) pour mettre à jour le contenu traduit et modifier l'étiquette en « Translation Complete ».
{% endtab %}

{% tab Catalogues %}
Les [Catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/) vous permettent d'accéder à des données provenant d'objets JSON importés via API et fichiers CSV pour enrichir vos messages, de manière similaire aux attributs personnalisés ou aux propriétés d'événement personnalisées via Liquid. Par exemple :

{% subtabs local %}
{% subtab API %}

Créez un catalogue via l'appel API suivant :
```bash
curl --location --request POST 'https://your_api_endpoint/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "catalogs": [
   {
     "name": "translations",
     "description": "My localization samples",
     "fields": [
       {
         "name": "id",
         "type": "string"
       },
       {
         "name": "context",
         "type": "string"
       },
       {
         "name": "language",
         "type": "string"
       },
       {
         "name": "body",
         "type": "string"
       }
     ]
   }
 ]
}'
```

Ajoutez des éléments via l'appel API suivant :

```bash
curl --location --request POST 'https://your_api_endpoint/catalogs/translations/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
   {
     "id": "1",
     "context": "1",
     "language": "en",
     "body": "Hey"
   },
   {
     "id": "2",
     "context": "1",
     "language": "es",
     "body": "Hola"
   },
   {
     "id": "3",
     "context": "1",
     "language": "pt",
     "body": "Oi"
   },
   {
     "id": "4",
     "context": "1",
     "language": "de",
     "body": "Hallo"
   }
 ]
}'
```
{% endsubtab%}
{% subtab CSV %}
Créez un fichier CSV au format suivant :

| id | context | language | body |
| --- | --- | --- | --- |
| 1 | 1 | en | Hey |
| 2 | 1 | es | Hola |
| 3 | 1 | pt | Oi |
| 4 | 1 | de | Hallo |
| 5 | 2 | en | Hey |
| 6 | 2 | es | Hola |
| 7 | 2 | pt | Oi |
| 8 | 2 | de | Hallo |
| 9 | 3 | en | Hey |
| 10 | 3 | es | Hola |
| 11 | 3 | pt | Oi |
| 12 | 3 | de | Hallo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Alternative approaches" }
{% endsubtab %}
{% endsubtabs %}

Ces éléments de catalogue peuvent ensuite être référencés à l'aide de la [personnalisation]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#using-catalogs-in-a-message), comme illustré ci-dessous, ou des [sélections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) qui vous permettent de créer des groupes de données.

{% raw %}
```liquid
{% catalog_items translations 1 %}
{{items[0].body}}
//returns “Hey”
```
{% endraw %}
{% endtab %}

{% tab Partenaires Braze %}
De nombreux partenaires Braze proposent des solutions de localisation, notamment [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/#about-transifex) et [Crowdin](https://crowdin.com/). En général, les utilisateurs utilisent la plateforme en complément d'une équipe interne et d'une agence de traduction. Ces traductions sont ensuite téléchargées et deviennent accessibles via la REST API. Ces services exploitent également souvent le [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), permettant aux utilisateurs de récupérer les traductions via API.

Par exemple, les appels de Contenu connecté suivants appellent Transifex et Crowdin pour récupérer une traduction, en utilisant {% raw %}`{{${language}}}`{% endraw %} pour identifier la traduction correcte pour un utilisateur donné. Cette traduction est ensuite enregistrée dans le bloc JSON « strings » et référencée.

{% subtabs local %}
{% subtab Exemple Transifex %}
{% raw %}
```liquid
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}
```
{% endraw %}
{% endsubtab %}
{% subtab Exemple Crowdin %}
{% raw %}
```liquid
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Tableurs %}
Hébergez les traductions dans un tableur, puis utilisez l'une des méthodes suivantes pour envoyer votre message dans la langue appropriée.

{% subtabs local %}
{% subtab Contenu connecté %}
Vous pouvez travailler avec une agence de traduction pour stocker les traductions dans un tableur Google Sheets, puis interroger ce contenu à l'aide du [Contenu connecté de Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/). Lorsque vous envoyez un message, la traduction correspondante pour chaque utilisateur sera intégrée dans le corps de votre Campaign en fonction de la langue sélectionnée.

{% alert note %}
L'API Google Sheets a une limite de 500 requêtes par 100 secondes par projet. Les appels de Contenu connecté peuvent être mis en cache, mais cette solution n'est pas adaptée à une Campaign à fort trafic.
{% endalert %}
{% endsubtab %}

{% subtab API JSON via SheetDB %}
Cette option fournit une méthode alternative pour transformer des Google Sheets en objets JSON interrogés via le Contenu connecté. En transformant un tableur en API JSON via SheetDB, vous pouvez choisir parmi [plusieurs niveaux d'abonnement](https://sheetdb.io/pricing) en fonction de la fréquence des appels API.

La structure du tableur suit les étapes de l'option 4, mais SheetDB fournit également des [filtres supplémentaires](https://docs.sheetdb.io/#sheetdb-api) pour interroger les objets.

Certains utilisateurs peuvent préférer implémenter SheetDB avec moins de dépendances Liquid et de blocs connectés en utilisant la [méthode de recherche](https://docs.sheetdb.io/#get-search-in-document) de SheetDB dans les appels de requête GET pour filtrer les objets JSON en fonction de l'étiquette Liquid {% raw %}`{{${language}}}`{% endraw %} afin de retourner automatiquement les résultats pour une seule langue plutôt que de construire de grands blocs conditionnels.

#### Étape 1 : Formater le tableur Google {#step-1-format-the-google-sheet}

Tout d'abord, construisez le tableur Google de sorte que les langues soient des objets différents :

| language | title1 | body1 | title2 | body2 |
| en | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Hallo | 4 | Hallo2 | 8 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Step 1: Format the Google sheet" }

#### Étape 2 : Utiliser l'étiquette Liquid de langue dans un appel de Contenu connecté {#step-2-use-the-language-liquid-tag-in-a-connected-content-call}

Ensuite, implémentez l'étiquette Liquid {% raw %}`{{${language}}}`{% endraw %} dans un appel de Contenu connecté. Notez que SheetDB générera automatiquement le `sheet_id` lors de la création du tableur.

{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}

#### Étape 3 : Modéliser vos messages {#step-3-template-your-messages}

Enfin, utilisez Liquid pour modéliser vos messages :

{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}

##### Considérations {#considerations}

- Le champ {% raw %}`{{${language}}}`{% endraw %} doit être défini pour tous les utilisateurs ; sinon, un bloc conditionnel Liquid doit être prévu comme gestionnaire de secours pour les utilisateurs sans langue définie.
- La modélisation des données dans Google Sheets doit suivre une structure verticale orientée par langue, par opposition à des objets de message.
- SheetDB propose un compte gratuit limité et plusieurs options payantes qui doivent être évaluées en fonction de votre stratégie de Campaign.
- Les appels de Contenu connecté peuvent être mis en cache. Nous recommandons de mesurer la fréquence projetée des appels API et d'envisager une approche alternative consistant à appeler l'endpoint principal de SheetDB au lieu d'utiliser la méthode de recherche.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}