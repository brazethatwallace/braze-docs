---
nav_title: Smartling
article_title: Smartling
description: "Cet article de référence présente le partenariat entre Braze et Smartling, un logiciel de localisation basé sur le cloud. Le connecteur Braze prend en charge la traduction des modèles d'e-mail HTML, des Content Blocks, des Canvas et des messages e-mail de Campaign."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://www.smartling.com/) est un logiciel de gestion de traduction de bout en bout basé dans le cloud, destiné aux clients qui souhaitent automatiser la traduction de sites web, d'applications et d'expériences client.

_Cette intégration est maintenue par Smartling._

## À propos de l'intégration {#about-the-integration}

Le connecteur Braze prend en charge les traductions des messages dans les Campaigns et les Canvas (e-mail, push, messages in-app et bannières), les modèles d'e-mail et les Content Blocks. Consultez le tableau suivant pour connaître les types d'éditeurs pris en charge pour chaque canal ou fonctionnalité.

| Canal/Fonctionnalité | Éditeur traditionnel (ex. HTML) | Éditeur par glisser-déposer |
| --------------- | ----------------------------- | -------------------- |
| [E-mail]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email) | ✅ | ✅ |
| [IAM]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message) | ✅ | ✅ |
| [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push) | ✅ | s/o |
| Modèle d'e-mail | ✅ | ✅ |
| Bannières | s/o | ✅ |
| Content Blocks | ✅ | ✅ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="About the integration" }


## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Smartling | Un [compte Smartling](https://dashboard.smartling.com/) est requis pour profiter de ce partenariat. |
| Projet de traduction Smartling | Pour connecter votre compte Braze à Smartling, vous devez d'abord vous connecter et [créer un projet de traduction](https://help.smartling.com/hc/en-us/articles/115003074093). |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations suivantes : <br>- campaigns.translations.get<br>- campaigns.translations.update<br>- campaigns.list<br>- campaigns.details<br>- canvas.translations.get<br>- canvas.translations.update<br>- campaigns.details<br>- templates.email.create<br>- templates.email.update<br>- templates.email.list<br>- templates.email.info<br>- templates.translations.get<br>- templates.translations.update<br>- content_blocks.info<br>- content_blocks.list<br>- content_blocks.create<br>- content_blocks.update<br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres > Clés API**. |
| Endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/api/basics/#endpoints). Votre endpoint dépend de l'URL Braze de votre instance. |
| Paramètres multilingues de Braze | [Complétez les paramètres multilingues dans Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Intégration {#integration}

### Étape 1 : Configurer les paramètres multilingues dans Braze {#step-1-set-up-multi-language-settings-in-braze}

Consultez [les instructions de configuration multilingue de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) pour configurer les locales dans Braze.

### Étape 2 : Configurer le projet Braze dans Smartling TMS {#step-2-set-up-the-braze-project-in-smartling-tms}

Reportez-vous à la [documentation de Smartling](https://help.smartling.com/hc/en-us/articles/13248549217435) pour plus de détails sur la configuration du connecteur.

### Connexion de Braze à Smartling {#connecting-braze-to-smartling}

1. Dans votre [compte Smartling](https://dashboard.smartling.com/), créez un projet de type [Braze Connector](https://help.smartling.com/hc/en-us/articles/115003074093).

![Connexion Braze dans Smartling.]({% image_buster /assets/img/smartling/image1_Connecting_Braze_to_Smartling.png %})

{: start="2"}
2. Dans ce projet, sélectionnez **Settings** > **Braze Settings** > **Connect to Braze**.
3. Remplissez les champs obligatoires, comme l'URL de l'API et la clé API. Si le test de connexion est réussi, enregistrez la connexion. Si le test échoue, vérifiez que vous avez saisi l'URL et la clé API correctes.

![Paramètres API de la connexion Braze dans Smartling.]({% image_buster /assets/img/smartling/image2_API.png %})

{: start="4"}
4. Ajoutez des langues de projet supplémentaires.

![Langues du projet dans la connexion Braze dans Smartling.]({% image_buster /assets/img/smartling/image3_project_languages.png %})

{: start="5"}
5. Dans les paramètres de Braze, vérifiez que les valeurs de la colonne **Target Language (Braze)** correspondent aux locales configurées dans les paramètres multilingues de Braze. La convention de nommage des locales doit correspondre exactement.

![Confirmation des langues dans la connexion Braze dans Smartling.]({% image_buster /assets/img/smartling/image4_language_confirmation.png %})

### Étape 3 : Ajouter des étiquettes de traduction à votre message Braze {#step-3-add-translation-tags-to-your-braze-message}

Consultez [les instructions de Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/?tab%3Dhtml%2520editor#prerequisites) pour savoir comment ajouter des étiquettes de traduction à vos messages :

- [E-mail]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email)
- [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push)
- [Messages in-app]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message)

Voici un exemple de Campaign e-mail HTML avec des étiquettes de traduction.

![E-mail Braze avec des étiquettes de traduction.]({% image_buster /assets/img/smartling/image5_translation_tags.png %})

Vous devez enregistrer le message en tant que brouillon avant de pouvoir sélectionner les locales.

### Étape 4 : Gérer les traductions dans Smartling {#step-4-manage-translations-in-smartling}

Une fois le connecteur Braze connecté et configuré, retrouvez le contenu Braze dans l'onglet Braze de votre projet Smartling. Pour plus d'informations, consultez la [documentation de Smartling](https://help.smartling.com/hc/en-us/articles/13248577069979).

Smartling propose des fonctionnalités avancées pour rechercher et sélectionner du contenu par :
- Recherche par mot-clé
- Type de contenu Braze
- Étiquetage Braze

1. Dans cet exemple, la Campaign e-mail de promotion du Nouvel An a été créée à l'[étape 3](#step-3-add-translation-tags-to-your-braze-message).

![E-mail Braze avec des étiquettes de traduction.]({% image_buster /assets/img/smartling/image6_ny_promotion.png %})

{: start="2"}
2. Une fois la Campaign à traduire identifiée, sélectionnez le dossier, choisissez les variantes et sélectionnez **Request Translation**.

![Demander des traductions.]({% image_buster /assets/img/smartling/image7_request_translation.png %})

{: start="3"}
3. Créez un nouveau travail pour la traduction.

![Créer un nouveau travail pour la traduction.]({% image_buster /assets/img/smartling/image8_request_translation.png %})

{: start="4"}
4. Une fois le travail autorisé, modifiez chaque traduction dans l'outil de TAO.

![Outil de TAO pour la traduction.]({% image_buster /assets/img/smartling/image9_translation_job.png %})

{: start="5"}
5. Une fois les traductions terminées, enregistrez-les et soumettez-les à Braze.

![Soumettre la traduction à Braze.]({% image_buster /assets/img/smartling/image10_translations.png %})

### Étape 5 : Prévisualiser le message en tant qu'utilisateur multilingue dans Braze {#step-5-preview-the-message-as-a-multi-language-user-in-braze}

Dans Braze, prévisualisez votre Campaign en tant qu'utilisateur multilingue pour vérifier que les traductions sont appliquées correctement.

![Aperçu utilisateur multilingue.]({% image_buster /assets/img/smartling/image11_preview.png %})

## Foire aux questions {#frequently-asked-questions}

### Les étiquettes de traduction sont-elles prises en charge par l'éditeur par glisser-déposer ? {#are-translation-tags-supported-for-the-drag-and-drop-editor}

Pour l'éditeur par glisser-déposer (e-mail, Content Block, message in-app), vous devez ajouter manuellement les étiquettes de traduction en tant qu'étiquettes Liquid.

### Comment traduire du texte à l'intérieur d'une étiquette Liquid ? {#how-do-you-translate-text-within-a-liquid-tag}

Smartling reconnaît les étiquettes Liquid et en fait des variables non modifiables dans le compositeur. Tout autre texte contenu dans l'étiquette Liquid, tel que le texte par défaut ou les filtres comme join, devient également non modifiable dans Smartling. Pour contourner cette limitation, supprimez l'étiquette Liquid dans Smartling et recréez-la avec le texte par défaut traduit. Un avertissement apparaît lorsque vous enregistrez la traduction.