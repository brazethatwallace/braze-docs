---
nav_title: Segment Engage
article_title: Segment Engage
page_order: 3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description: "Cet article de référence décrit le partenariat entre Braze et Segment, une plateforme de données clients qui collecte et achemine des informations entre les sources de votre pile marketing."
page_type: partner
search_tag: Partner

---

# Segment Engage

> [Segment](https://segment.com) est une plateforme de données clients qui vous aide à collecter, nettoyer et activer vos données clients. Cet article de référence donne un aperçu de la connexion entre [Braze et Segment Engage](https://segment.com/docs/destinations/braze/#Engage), et décrit les exigences et les processus pour une mise en œuvre et une utilisation correctes.

L'intégration de Braze et Segment vous permet d'utiliser [Engage](https://segment.com/docs/engage/), la segmentation d'audience intégrée à Segment, pour créer des segments d'utilisateurs sur la base des données que vous avez déjà collectées dans diverses sources. Ces audiences seront ensuite synchronisées avec Braze en tant que cohorte, ou indiquées sur le profil de l'utilisateur par le biais d'[attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) ou d'[événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) qui peuvent être utilisés pour créer des segments Braze à utiliser dans le reciblage de Campaign et de Canvas.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Segment | Un [compte Segment](https://app.segment.com/login) est nécessaire pour bénéficier de ce partenariat. |
| Destination cloud Braze | Vous devez avoir déjà [configuré Braze comme destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) dans votre intégration Segment.<br><br>Vous devez notamment fournir le centre de données et la clé API REST corrects de Braze dans vos [paramètres de connexion]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Clé d'importation des données Braze | Pour synchroniser les audiences Engage avec Braze sous forme de cohortes, vous devez générer une clé d'importation des données.<br><br>L'importation de cohortes est en accès anticipé ; contactez votre gestionnaire de la satisfaction client Braze pour obtenir l'accès à cette fonctionnalité. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration de la destination Cohortes {#cohorts-destination-integration}

### Étape 1 : Créer une audience Engage {#step-1-create-an-engage-audience}
1. Dans Segment, accédez à l'onglet **Audiences** dans Engage, puis cliquez sur **New**.
2. Créez votre audience. Un éclair dans le coin supérieur de la page indique si l'audience se met à jour en temps réel.
3. Sélectionnez ensuite Braze comme destination.
4. Prévisualisez votre audience en cliquant sur **Review & Create**. Par défaut, Segment interroge toutes les données historiques pour définir la valeur actuelle du trait calculé et de l'audience. Pour ne pas tenir compte de ces données, décochez la case **Historical Backfill**.

### Étape 2 : Récupérer votre clé d'importation des données de cohorte {#step-2-capture-your-cohort-data-import-key}

Dans Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Segment**.

Vous y trouverez votre endpoint REST et pourrez générer votre clé d'importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante.

### Étape 3 : Connecter la destination Cohortes Braze {#step-3-connect-the-braze-cohorts-destination}
Suivez [les instructions de Segment](https://segment.com/docs/connections/destinations/catalog/actions-braze-cohorts/#getting-started) sur la configuration de la destination Cohortes pour synchroniser vos audiences Engage en tant que cohortes vers Braze.

### Étape 4 : Créer un segment Braze à partir de l'audience Engage {#step-4-create-a-braze-segment-from-the-engage-audience}
Dans Braze, accédez à **Segments**, créez un nouveau segment et sélectionnez **Segment Cohorts** comme filtre. À partir de là, vous pouvez choisir quelle cohorte Segment vous souhaitez inclure. Une fois le segment de cohorte Segment créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une Campaign ou d'un Canvas.

![]({% image_buster /assets/img/segment/segment3.png %})

## Intégration en mode cloud {#cloud-mode-integration}

### Étape 1 : Créer un trait calculé ou une audience Segment {#step-1-create-a-segment-computed-trait-or-audience}

1. Dans Segment, accédez à l'onglet **Computed Traits** ou **Audiences** dans **Engage**, puis cliquez sur **New**.
2. Créez votre trait calculé ou votre audience. Un éclair dans le coin supérieur de la page indique si le calcul est mis à jour en temps réel.
3. Sélectionnez ensuite **Braze** comme destination.
4. Prévisualisez votre audience en cliquant sur **Review & Create**. Par défaut, Segment interroge toutes les données historiques pour définir la valeur actuelle du trait calculé et de l'audience. Pour ne pas tenir compte de ces données, décochez la case **Historical Backfill**.
5. Dans les paramètres du trait calculé ou de l'audience, ajustez les paramètres de connexion en fonction de la manière dont vous souhaitez que vos données soient envoyées à Braze.

#### Traits et audiences calculés {#computed-traits-and-audiences}

Les [traits calculés](https://segment.com/docs/engage/audiences/computed-traits/) et les [audiences](https://segment.com/docs/Engage/audiences/) peuvent être envoyés à Braze en tant qu'attributs personnalisés ou événements personnalisés.
- Les traits et les audiences envoyés à l'aide de l'appel `identify` apparaîtront dans Braze sous la forme d'attributs personnalisés.
- Les traits et les audiences envoyés à l'aide de l'appel `track` apparaîtront dans Braze sous la forme d'événements personnalisés.

Vous pouvez choisir la méthode à utiliser (ou choisir d'utiliser les deux) lorsque vous connectez le trait calculé à la destination Braze.

{% tabs %}
{% tab Identify %}

Vous pouvez envoyer des traits et des audiences calculés à Braze sous forme d'appels `identify` pour créer des attributs personnalisés dans Braze.

Par exemple, si vous avez un trait calculé Engage pour « Dernier article de produit consulté », vous trouverez `last_product_viewed_item` dans le profil Braze de l'utilisateur sous **Custom Attributes**. S'il s'agit d'une audience Engage, votre audience sera répertoriée sous **Custom Attributes** avec la valeur `true`.

| Trait calculé | Audiences |
| -------------- | --------- |
| ![La section des attributs personnalisés dans un profil utilisateur indique « last_product_viewed_item » comme « Sweater ».]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![La section des attributs personnalisés dans un profil utilisateur indique « dormant_shopper » comme « true ».]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Traits et audiences calculés" }

{% endtab %}
{% tab Track %}

Vous pouvez envoyer des traits et des audiences calculés à Braze sous forme d'appels `track` pour créer des événements personnalisés dans Braze.

En reprenant l'exemple précédent, si un utilisateur dispose d'un trait calculé pour « Dernier article de produit consulté », il apparaîtra sur les profils Braze des utilisateurs sous `Trait Computed` avec le nombre correspondant et l'horodatage le plus récent sous **Custom Events**. S'il s'agit d'une audience Engage, votre audience, le décompte et l'horodatage le plus récent figureront sous **Custom Attributes** avec la valeur `true`.

| Trait calculé | Audiences |
| -------------- | --------- |
| ![La section des événements personnalisés dans un profil utilisateur indique « Trait Computed » « 1 » fois, la dernière occurrence étant « il y a 20 heures ».]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![La section des attributs personnalisés dans un profil utilisateur indique « Audience Entered » « 1 » fois, la dernière occurrence étant le « 9 mars à 1 h 45 ».]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Traits et audiences calculés" }

{% endtab %}
{% endtabs %}

### Étape 2 : Segmenter les utilisateurs dans Braze {#step-2-segment-users-in-braze}

Dans Braze, pour créer un segment de ces utilisateurs, accédez à **Segments** sous **Engagement**, créez un nouveau segment et nommez-le. Ensuite, en fonction de l'appel que vous avez utilisé :
- **Identify** : sélectionnez **custom attribute** comme filtre et localisez votre attribut personnalisé. Ensuite, utilisez l'option « matches regex » (trait) ou l'option « equals » (audience) et saisissez la variable appropriée.
- **Track** : sélectionnez **custom event** comme filtre et localisez votre événement personnalisé. Ensuite, utilisez les options « more than », « less than » ou « exactly » et insérez la valeur souhaitée. Cela dépendra de la manière dont vous souhaitez définir votre segment.

Une fois enregistré, vous pouvez faire référence à ce segment lors de la création d'un Canvas ou d'une Campaign à l'étape du ciblage des utilisateurs.

## Temps de synchronisation {#sync-time}

Bien que le paramètre par défaut de la connexion entre Braze et Segment Engage soit `Realtime`, certains filtres empêcheront le persona d'être synchronisé en temps réel, notamment certains filtres temporels qui limitent la taille de votre audience au moment de l'envoi du message.

## Test du débogueur Segment {#segment-debugger-testing}

Le tableau de bord de Segment offre une fonctionnalité « Debugger » qui permet aux clients de vérifier si les données d'une « Source » sont transférées vers une « Destination » comme prévu.

Cette fonctionnalité se connecte à l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze, ce qui signifie qu'elle ne peut être utilisée que pour des utilisateurs identifiés (utilisateurs qui possèdent déjà un ID utilisateur pour leur profil utilisateur Braze).

Cela ne fonctionnera pas pour une intégration côte à côte de Braze. Aucune donnée serveur ne sera transmise si vous n'avez pas saisi les informations correctes de l'API REST de Braze.