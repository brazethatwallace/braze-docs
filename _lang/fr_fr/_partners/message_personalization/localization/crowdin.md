---
nav_title: Crowdin
article_title: Crowdin
description: "Utilisez l'intégration Crowdin pour traduire vos Campaigns, vos expériences Canvas, vos modèles d'e-mail et vos Content Blocks grâce à la mémoire de traduction, aux glossaires et à la traduction automatique."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> [Crowdin](https://crowdin.com/) est une plateforme de gestion de la localisation basée sur l'intelligence artificielle qui aide les équipes à automatiser la traduction de leurs logiciels, applications et contenus marketing.

Connectez Crowdin à Braze pour gérer les traductions de vos Campaigns et expériences Canvas. La synchronisation automatisée fonctionne avec la traduction automatique, la mémoire de traduction et les glossaires, garantissant ainsi la cohérence entre les flux de travail humains et automatisés.

_Cette intégration est maintenue par Crowdin._

## À propos de l'intégration {#about-the-integration}

Crowdin propose deux applications pour Braze : [Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) et [Braze Email Templates](https://store.crowdin.com/braze-app). Choisissez en fonction des fonctionnalités de Braze que vous localisez. Le tableau suivant les compare.

### Choisir la bonne application Crowdin {#choose-the-right-crowdin-app}

| Canal ou fonctionnalité | Braze Campaigns & Canvas | Braze Email Templates |
| --- | --- | --- |
| **Campaigns** | ✅ Pris en charge | ❌ Non pris en charge |
| **Étapes du Canvas** | ✅ Pris en charge | ❌ Non pris en charge |
| **Modèles d'e-mail** | ❌ Non pris en charge | ✅ Pris en charge |
| **Content Blocks** | ❌ Non pris en charge | ✅ Pris en charge |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Choisir la bonne application Crowdin" }

## Prérequis {#prerequisites}

| Condition requise | Description |
| --- | --- |
| **Compte Crowdin** | Un [compte Crowdin.com](https://accounts.crowdin.com/register) ou un [compte Crowdin Enterprise](https://accounts.crowdin.com/workspace/create) est requis. |
| **Projet Crowdin** | Avant de connecter Braze, [créez un projet de traduction](https://support.crowdin.com/creating-project/) dans Crowdin ou Crowdin Enterprise. |
| **Clé API REST Braze** | Une clé API REST Braze disposant des autorisations pour les Campaigns, Canvas, Content Blocks, les attributs personnalisés, les e-mails et les modèles. |
| **Endpoint REST Braze** | L'URL de votre endpoint REST Braze spécifique (par exemple, `https://rest.iad-03.braze.com`). |
| **Paramètres multilingues Braze** | Les locales doivent être configurées dans votre tableau de bord de Braze sous **Paramètres** > **Paramètres de localisation**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration Braze Campaigns & Canvas {#braze-campaigns-canvas-integration}

Si vous localisez du contenu dans des messages en direct or en ligne/en production/instantané, utilisez l'[application Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) pour synchroniser les chaînes traduisibles de vos brouillons de Campaign et Canvas avec le support multilingue de Braze.

Pour une présentation vidéo, consultez [Intégration Braze Campaigns & Canvas](https://youtu.be/ahG1ET4VRKA).

### Étape 1 : Configurer les paramètres multilingues dans Braze {#step-1-set-up-multi-language-settings-in-braze}

Avant de connecter Crowdin, ajoutez vos langues cibles dans Braze.

1. Dans Braze, accédez à **Paramètres** > **Paramètres de localisation**.
2. Ajoutez les langues que vous prévoyez de prendre en charge.

![Page des locales Braze sous Paramètres, affichant les noms des locales, les clés des locales et le bouton Ajouter une locale.]({% image_buster /assets/img/crowdin/braze_locales.png %})

{: start="3"}
3. Notez chaque **clé de locale** (par exemple, `en-US`, `fr-FR`, `es-ES`). Vous utiliserez ces valeurs pour mapper les langues dans Crowdin.

### Étape 2 : Configurer le projet Braze dans Crowdin {#step-2-set-up-the-braze-project-in-crowdin}

1. Dans votre compte Crowdin Enterprise ou Crowdin.com, accédez à **Store** dans le menu de navigation.
2. Recherchez **Braze Campaigns & Canvas**, puis sélectionnez **Install**.

![Crowdin Store avec Braze Campaigns & Canvas sélectionné et Install mis en surbrillance.]({% image_buster /assets/img/crowdin/crowdin_store_campaigns_canvas.png %})

{: start="3"}
3. Sélectionnez le ou les projets dans lesquels vous souhaitez utiliser cette intégration.
4. Pour ouvrir l'intégration, accédez à **Integrations** > **Braze Campaigns & Canvas** dans votre projet.

#### Connecter Braze à Crowdin {#connecting-braze-to-crowdin}

Autorisez la connexion avec vos identifiants d'API Braze :

![Formulaire de connexion Crowdin Braze Campaigns & Canvas avec la clé REST API, l'endpoint REST et le bouton Log in with Braze Campaigns & Canvas.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_login.png %})

- **Clé REST API Braze :** Créez-la dans Braze sous **Paramètres** > **API et identifiants** > **Clés API**. Accordez les permissions nécessaires à cette intégration (Campaigns, Canvas, Content Blocks et attributs personnalisés).
- **Endpoint REST Braze :** Saisissez l'URL de votre instance Braze (par exemple, `https://rest.iad-03.braze.com`). Pour en savoir plus, consultez [Endpoints REST API]({{site.baseurl}}/api/basics#endpoints).

![Page des clés REST API Braze avec le bouton Create API Key et le contrôle de copie de l'endpoint REST.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

Sélectionnez **Log in with Braze Campaigns & Canvas**.

### Étape 3 : Configurer le mappage des langues dans Crowdin {#step-3-configure-language-mapping-in-crowdin}

Après avoir connecté votre compte, mappez chaque langue de projet Crowdin à la locale Braze correspondante.

1. Dans le tableau de bord de l'intégration **Braze Campaigns & Canvas**, sélectionnez l'icône d'engrenage **Settings** dans la barre d'actions supérieure.

![Écran de l'intégration Braze Campaigns & Canvas avec Settings dans la barre d'actions supérieure.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_settings.png %})

{: start="2"}
2. Ouvrez l'onglet **General Settings**.
3. Saisissez les clés de locale. Crowdin liste les langues de votre projet (par exemple, français, italien). Dans chaque champ, saisissez la **clé de locale Braze** correspondante.
   - Par exemple, si Braze utilise `it` pour l'italien, saisissez `it` en face de l'italien dans Crowdin.
   - Chaque entrée doit correspondre exactement à la **clé de locale** de cette locale dans les **Paramètres de localisation** de Braze.

![Fenêtre modale des paramètres sur l'onglet General Settings, affichant les champs de filtre de fichiers et les lignes de mappage des langues (par exemple, français mappé à fr).]({% image_buster /assets/img/crowdin/crowdin_language_mapping_settings.png %})

{: start="4"}
4. Sélectionnez **Save** pour confirmer le mappage.

### Étape 4 : Ajouter des balises de traduction à votre message Braze {#step-4-add-translation-tags-to-your-braze-message}

Crowdin lit les mêmes **balises de traduction** Liquid que Braze utilise pour les messages multilingues. Ajoutez {% raw %}`{% translation your_id_here %}` et `{% endtranslation %}`{% endraw %} autour de chaque élément de texte, URL d'image ou URL de lien que vous souhaitez traduire. Chaque bloc nécessite un `id` unique (par exemple, `greeting` ou `welcome_header`).

**Exemple :**

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

Pour le HTML, le Liquid dans les liens et d'autres cas de figure, suivez les mêmes règles que dans [Traduire les locales]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) (par exemple, placez les balises autour des segments les plus petits possibles, et n'encadrez que les parties spécifiques à la langue des URL lors de la localisation des liens).

Enregistrez votre message Braze en tant que **brouillon** avant que Crowdin puisse détecter et récupérer le contenu.

### Étape 5 : Gérer les traductions dans Crowdin {#step-5-manage-translations-in-crowdin}

L'écran d'intégration comporte deux volets :

- **Volet Braze :** Vos Campaigns et Canvas.
- **Volet Crowdin :** Le contenu déjà synchronisé pour la traduction.

![Volets Crowdin et Braze Campaigns & Canvas avec les dossiers des Campaigns et des locales, Sync to Braze et Sync to Crowdin.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_sync_panels.png %})

#### Synchroniser le contenu {#syncing-content}

1. Dans le volet **Braze**, cochez la case de la Campaign ou du Canvas à traduire.
2. Sélectionnez **Sync to Crowdin**.
3. Une fois la synchronisation terminée, le fichier apparaît dans le volet **Crowdin**. Les traducteurs peuvent ouvrir les chaînes dans l'éditeur Crowdin.

#### Renvoyer les traductions vers Braze {#returning-translations-to-braze}

1. Lorsque les traductions sont complètes à 100 % dans Crowdin, revenez à l'onglet **Integrations**.
2. Sélectionnez le contenu terminé dans le volet **Crowdin**.
3. Sélectionnez **Sync to Braze**. Cela pousse les chaînes traduites dans les variantes linguistiques correspondantes de votre Campaign Braze.

### Étape 6 : Prévisualiser le message en tant qu'utilisateur multilingue dans Braze {#step-6-preview-the-message-as-a-multi-language-user-in-braze}

Pour confirmer l'intégration :

1. Ouvrez votre Campaign dans le **Braze Message Composer**.
2. Accédez à l'onglet **Test**.
3. Sélectionnez **Preview Message as User**.
4. Recherchez un profil utilisateur dont l'attribut `language` correspond à l'une de vos locales traduites.
5. Confirmez que le contenu passe de la langue source à la version traduite.

## Intégration Braze Email Templates {#braze-email-templates-integration}

Si vous localisez vos e-mails au niveau des modèles, utilisez l'[application Braze Email Templates](https://store.crowdin.com/braze-app) pour synchroniser le HTML depuis votre bibliothèque multimédia Braze.

Pour un tutoriel vidéo, consultez [Intégration Braze Email Templates](https://youtu.be/g0YMKW3jEjk).

### Étape 1 : Installer l'application {#step-1-install-the-app}

1. Dans votre projet Crowdin, accédez à l'onglet **Store**.
2. Recherchez **Braze Email Templates** et sélectionnez **Install**.

![Store Crowdin avec Braze Email Templates sélectionné et Install mis en évidence.]({% image_buster /assets/img/crowdin/crowdin_store_email_templates.png %})

{: start="3"}
3. Sélectionnez le ou les projets dans lesquels vous souhaitez utiliser cette intégration.
4. Pour ouvrir l'intégration, accédez à **Integrations** > **Braze Email Templates** dans votre projet.

### Étape 2 : Se connecter à Braze {#step-2-connect-to-braze}

Autorisez la connexion avec vos identifiants API Braze :

![Formulaire de connexion Crowdin Braze Email Templates avec la clé REST API, l'endpoint REST et Log in with Braze Email Templates.]({% image_buster /assets/img/crowdin/crowdin_email_templates_login.png %}){: style="max-width:85%;"}

1. **Clé REST API Braze :** Accordez les permissions `templates.email` et `content_blocks` (lecture et écriture). Créez la clé dans Braze sous **Paramètres** > **API et identifiants** > **Clés API**.

![Page des clés REST API de Braze avec Create API Key et le contrôle de copie de l'endpoint REST.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

{: start="2"}
2. Pour l'**endpoint REST Braze**, utilisez l'URL spécifique à votre instance (par exemple, `https://rest.iad-03.braze.com`).
3. Sélectionnez **Log in with Braze Email Templates**.

### Étape 3 : Synchroniser le contenu pour la traduction {#step-3-sync-content-for-translation}

L'écran d'intégration affiche votre bibliothèque Braze :

- **Panneau Braze :** Les **Email Templates** et les **Content Blocks** que vous pouvez synchroniser.
- **Panneau Crowdin :** Le contenu en cours de traduction.

1. Dans le panneau **Braze**, cochez la case à côté des modèles ou blocs que vous souhaitez localiser.
2. Sélectionnez **Sync to Crowdin**.
3. Crowdin récupère le code HTML source. Les traducteurs travaillent dans l'éditeur Crowdin avec un **aperçu WYSIWYG** en direct or en ligne/en production/instantané pour préserver la mise en page.

![Onglet d'aperçu de l'éditeur Crowdin montrant le HTML d'e-mail localisé et les chaînes traduisibles.]({% image_buster /assets/img/crowdin/crowdin_editor_wysiwyg_preview.png %}){: style="max-width:85%;"}

### Étape 4 : Livrer les modèles traduits {#step-4-deliver-translated-templates}

Lorsque les traductions atteignent 100 % :

1. Sélectionnez les fichiers terminés dans le panneau **Crowdin**.
2. Sélectionnez **Sync to Braze**.
3. Crowdin crée automatiquement des versions localisées de ces ressources dans votre bibliothèque multimédia Braze (par exemple, `Template_Name_fr`).

![Panneaux Crowdin et Braze Email Templates listant les Email Templates et Content Blocks, avec Sync to Braze et Sync to Crowdin.]({% image_buster /assets/img/crowdin/crowdin_email_templates_sync_panels.png %})