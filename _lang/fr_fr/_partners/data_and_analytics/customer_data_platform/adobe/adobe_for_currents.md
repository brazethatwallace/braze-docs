---
nav_title: Adobe pour Currents
article_title: Adobe pour Currents
alias: /partners/adobe_for_currents/
description: "Cet article de référence présente le partenariat entre Braze Currents et Adobe, une plateforme de données client qui permet aux marques de connecter et de mapper leurs données Adobe (attributs personnalisés et segments) à Braze en temps réel."
page_type: partner
tool: Currents
search_tag: Partner
---

# Adobe pour Currents {#adobe-for-currents}

> [Adobe](https://www.adobe.com/) est une plateforme de données client qui permet aux marques de connecter et de mapper leurs données Adobe (attributs personnalisés et segments) à Braze en temps réel.

L'intégration de Braze et d'Adobe vous permet de contrôler de façon fluide le flux d'informations entre les deux systèmes. Avec [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), vous pouvez également connecter les données à Adobe pour les rendre exploitables dans l'ensemble des outils de croissance.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Currents | Pour exporter des données dans Adobe, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
| Compte Adobe Experience Platform | Un [compte Adobe Experience Platform](https://experience.adobe.com/#/platform/home) est nécessaire pour bénéficier de ce partenariat. |
| Autorisation de créer un connecteur | Vous devez disposer des autorisations nécessaires pour créer une connexion de source de streaming afin d'utiliser cette intégration. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Créer un schéma XDM dans Adobe {#step-1-create-an-xdm-schema-in-adobe}

1. Dans Adobe Experience Platform, accédez à **Schemas** > sélectionnez **Create schema** > sélectionnez **Experience Event** > sélectionnez **Next**.<br><br>![Page Adobe Schemas pour le schéma intitulé « Braze Currents Walk-Through ».]({% image_buster /assets/img/adobe/currents_sources.png %})<br><br>
2. Donnez un nom et une description à votre schéma.
3. Dans le panneau **Composition**, configurez les attributs de votre schéma :
- Dans **Field groups**, sélectionnez **Add**, puis ajoutez le groupe de champs **Braze Currents User Event**.
- Sélectionnez **Save**.

Pour plus d'informations sur les schémas, consultez la documentation d'Adobe sur la [création de schémas](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui).

### Étape 2 : Connecter Braze à Adobe Experience Platform {#step-2-connect-braze-to-the-adobe-experience-platform}

1. Dans Adobe Experience Platform, accédez à **Sources** > **Catalog** > **Marketing automation**.
2. Sélectionnez **Add data** pour Braze Currents.
3. Téléchargez le [fichier d'exemple Braze Currents](https://github.com/Appboy/currents-examples/blob/master/sample-data/Adobe/adobe_examples.json).<br><br>![Page Adobe « Add data ».]({% image_buster /assets/img/adobe/currents_add_data.png %})<br><br>
4. Une fois votre fichier téléchargé, fournissez les détails de votre flux de données, y compris des informations sur votre jeu de données et le schéma auquel vous effectuez le mappage.
    - Si vous connectez une source Braze Currents pour la première fois, créez un nouveau jeu de données et veillez à utiliser le schéma que vous avez créé à l'[étape 1](#step-1-create-an-xdm-schema-in-adobe).
    - Si ce n'est pas votre première fois, utilisez n'importe quel jeu de données existant qui fait référence au schéma Braze.
5. Configurez le mappage de vos données et résolvez les problèmes.
    - Modifiez le mappage pour `id` de `to _braze.appID` à `_id` au niveau racine du schéma.
    - Assurez-vous que `properties.is_amp` est mappé à `_braze.messaging.email.isAMP`.
    - Supprimez le mappage `time` et `timestamp`, puis sélectionnez l'icône d'ajout > **Add calculated field** et entrez **time * 1000**. Sélectionnez **Save**.
    - Sélectionnez **Map target field** à côté du nouveau champ source et mappez-le à **timestamp** au niveau racine du schéma. <br><br>![Page Adobe « Add data » avec les mappages.]({% image_buster /assets/img/adobe/currents_mapping.png %})<br><br>
6. Sélectionnez **Validate** pour confirmer que vous avez résolu les problèmes.

{% alert important %}
Les horodatages de Braze sont exprimés en secondes. Pour refléter correctement les horodatages dans Adobe Experience Platform, vos champs calculés doivent être exprimés en millisecondes. Pour convertir les secondes en millisecondes, utilisez le calcul **time * 1000**.
{% endalert %}

{: start="7"}
7. Sélectionnez **Next**, vérifiez les détails de votre flux de données, puis sélectionnez **Finish**.<br><br>![Page Adobe « Add data » sans erreur de mappage.]({% image_buster /assets/img/adobe/currents_no_errors.png %})

### Étape 3 : Rassembler les identifiants {#step-3-gather-credentials}

Recueillez les identifiants suivants pour les saisir dans Braze, ce qui permettra à Braze d'envoyer des données à Adobe Experience Platform.

| Champ         | Description                          |
|---------------|-------------------------------------|
| Client ID     | L'ID client associé à votre source Adobe Experience Platform. |
| Client Secret | Le secret client associé à votre source Adobe Experience Platform. |
| Tenant ID     | L'ID de locataire associé à votre source Adobe Experience Platform. |
| Sandbox Name  | Le sandbox associé à votre source Adobe Experience Platform.   |
| Dataflow ID   | L'ID de flux de données associé à votre source Adobe Experience Platform.   |
| Streaming Endpoint  | L'endpoint de streaming associé à votre source Adobe Experience Platform. Braze le convertit automatiquement en endpoint de streaming par lots. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 3 : Rassembler les identifiants" }

### Étape 4 : Configurer Currents pour transmettre les données à votre source de données {#step-4-configure-currents-to-stream-data-to-your-data-source}

1. Dans Braze, accédez à **Partner Integrations** > **Data Export**, puis sélectionnez **Create New Current**.
2. Fournissez les éléments suivants :
    - Un nom pour le connecteur
    - Les coordonnées pour les notifications concernant le connecteur
    - Les identifiants de l'[étape 3](#step-3-gather-credentials)
3. Sélectionnez les événements que vous souhaitez recevoir.
4. Vous pouvez également configurer les exclusions ou les transformations de champs souhaitées.
5. Sélectionnez **Launch Current**.