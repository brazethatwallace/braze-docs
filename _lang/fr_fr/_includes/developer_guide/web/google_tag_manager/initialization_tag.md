### Conditions préalables {#prerequisites}

Avant de pouvoir utiliser cette méthode d'intégration, vous devez [créer un compte et un conteneur pour Google Tag gestionnaire](https://support.google.com/tagmanager/answer/14842164).

### Étape 1 : Ouvrir la galerie de modèles de balises {#step-1-open-the-tag-template-gallery}

Dans [Google Tag gestionnaire](https://tagmanager.google.com/), sélectionnez votre espace de travail, puis choisissez **Templates**. Dans le volet **Tag Template**, sélectionnez **Search Gallery**.

![La page des modèles pour un exemple d'espace de travail dans Google Tag Manager.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### Étape 2 : Ajouter le modèle de balise d'initialisation {#step-2-add-the-initialization-tag-template}

Dans la galerie de modèles, recherchez `braze-inc`, puis sélectionnez **Braze Initialization Tag**.

![La galerie de modèles présentant les différents modèles « braze-inc ».]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

Sélectionnez **Add to workspace** > **Add**.

![La page « Braze Initialization Tag » dans Google Tag Manager.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### Étape 3 : Configurer la balise {#step-3-configure-the-tag}

Dans la section **Templates**, sélectionnez le modèle que vous venez d'ajouter.

![La page « Templates » dans Google Tag Manager affichant le modèle Braze Initialization Tag.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

Sélectionnez l'icône en forme de crayon pour ouvrir le menu déroulant **Tag Configuration**.

![La vignette Tag Configuration avec l'icône « crayon » affichée.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

Saisissez les informations minimales requises :

| Champ         | Description |
| ------------- | ----------- |
| **API Key**   | Votre [clé API Braze]({{site.baseurl}}/api/basics#about-rest-api-keys), disponible dans le tableau de bord de Braze sous **Settings** > **App Settings**. |
| **API Endpoint** | L'URL de votre endpoint REST. Votre endpoint dépend de l'URL de Braze pour [votre instance]({{site.baseurl}}/api/basics#endpoints). |
| **SDK Version**  | La version `MAJOR.MINOR` la plus récente du SDK Web Braze indiquée dans le [journal des modifications]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web). Par exemple, si la dernière version est `4.1.2`, saisissez `4.1`. Pour en savoir plus, consultez [À propos de la gestion des versions du SDK]({{site.baseurl}}/developer_guide/sdk_integration/version_management). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 3 : Configurer la balise" }

Pour accéder à des paramètres d'initialisation supplémentaires, sélectionnez **Braze Initialization Options** et choisissez les options dont vous avez besoin.

![La liste des options d'initialisation Braze sous « Tag Configuration ».]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### Étape 4 : Choisir les options d'initialisation {#step-4-choose-initialization-options}

La balise d'initialisation Braze propose les options suivantes. La plupart correspondent directement aux [`InitializationOptions` du SDK Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions), et certaines correspondent à des méthodes du SDK Web que la balise appellera lors de l'initialisation. Sélectionnez les options qui correspondent à vos besoins d'intégration :

| Option GTM | Configuration ou méthode du SDK Web | Description |
| --- | --- | --- |
| **Allow HTML In-App Messages** | `allowUserSuppliedJavascript` | Active les messages in-app HTML, les bannières et les actions de clic JavaScript fournies par l'utilisateur. Nécessaire pour les [messages in-app HTML]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html) et les [bannières]({{site.baseurl}}/developer_guide/banners/placements/?sdktab=web) utilisant du HTML personnalisé. Activez cette option uniquement si vous faites confiance au contenu HTML et JavaScript, car elle autorise l'exécution de JavaScript fourni par l'utilisateur. |
| **App Version Number** | `appVersion`, `appVersionNumber` | Version de l'application pour la segmentation (par exemple, `1.2.3.4`). |
| **Automatically Open New Session** | `braze.openSession()` | Ouvre une nouvelle session après l'initialisation du SDK en appelant cette méthode automatiquement. |
| **Automatically show new in app messages** | `braze.automaticallyShowInAppMessages()` | Affiche automatiquement les nouveaux messages in-app lorsqu'ils arrivent du serveur, en appelant cette méthode après l'initialisation. |
| **Disable Automatic Push Token Maintenance** | `disablePushTokenMaintenance` | Empêche le SDK de synchroniser les jetons de notification push avec le backend de Braze lors des nouvelles sessions. |
| **Disable Automatic Service Worker Registration** | `manageServiceWorkerExternally` | À utiliser si vous enregistrez et gérez vous-même le service de traitement. |
| **Disable Cookies** | `noCookies` | Utilise localStorage à la place des cookies pour les données utilisateur/session. Empêche la reconnaissance entre sous-domaines. |
| **Disable Font Awesome** | `doNotLoadFontAwesome` | Empêche le SDK de charger Font Awesome depuis le CDN. À utiliser si votre site dispose déjà de Font Awesome. |
| **Enable SDK Authentication** | `enableSdkAuthentication` | Active l'[authentification SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication). |
| **Enable Web SDK Logging** | `enableLogging` | Active la journalisation dans la console à des fins de débogage. À retirer avant la mise en production. |
| **Minimum Interval Between Triggered Messages** | `minimumIntervalBetweenTriggerActionsInSeconds` | Nombre minimum de secondes entre les actions de déclenchement (valeur par défaut : 30). |
| **Open Cards in New Tab** | `openCardsInNewTab` | Ouvre les liens des Content Cards dans un nouvel onglet lorsque l'interface par défaut du flux est utilisée. |
| **Service Worker Location** | `serviceWorkerLocation` | Chemin personnalisé pour le fichier du service de traitement (par défaut : `/service-worker.js`). |
| **Session Timeout (seconds)** | `sessionTimeoutInSeconds` | Délai d'expiration de la session en secondes (valeur par défaut : 1 800). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 4 : Choisir les options d'initialisation" }

{% alert note %}
Pour activer les [messages in-app HTML personnalisés]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html) lorsque vous utilisez la balise d'initialisation Braze de Google Tag gestionnaire, sélectionnez **Allow HTML In-App Messages** dans **Braze Initialization Options**. Cette case correspond à l'option d'initialisation `allowUserSuppliedJavascript` dans `braze.initialize()` et la définit sur `true`. La balise d'initialisation Braze de Google Tag gestionnaire utilise ce libellé à la place du nom de l'option.
{% endalert %}

Pour les options non exposées dans le modèle GTM (telles que `contentSecurityNonce`, `localization` ou `devicePropertyAllowlist`), utilisez plutôt l'[initialisation à l'exécution]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web).

### Étape 5 : Configurer le déclenchement sur *toutes les pages* {#step-5-set-to-trigger-on-all-pages}

La balise d'initialisation doit être exécutée sur toutes les pages de votre site. Cela vous permet d'utiliser les méthodes du SDK Braze et d'enregistrer les analyses des notifications push Web.

{% alert important %}
**Séquencement des balises :** la balise d'initialisation Braze doit se déclencher avant toute autre balise qui appelle des méthodes du SDK Braze (telles que `braze.getUser()` ou `braze.logCustomEvent()`). Si des événements personnalisés, des attributs utilisateur ou d'autres appels de méthodes Braze se déclenchent avant l'initialisation du SDK, vous risquez de rencontrer des erreurs telles que `Uncaught TypeError: Cannot read properties of undefined (reading 'getUser')`. Pour garantir un séquencement correct, configurez votre balise d'initialisation Braze comme balise de configuration ou utilisez la fonctionnalité de séquencement des balises de GTM pour vous assurer qu'elle se déclenche en premier. Pour en savoir plus, consultez [Séquencement des balises pour les balises d'action Braze]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager/?sdktab=web#web_tag-sequencing-for-braze-action-tags).
{% endalert %}

### Étape 6 : Vérifier votre intégration {#step-6-verify-your-integration}

Vous pouvez vérifier votre intégration en utilisant l'une des options suivantes :

- **Option 1 :** À l'aide de l'[outil de débogage](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag gestionnaire, vérifiez que la balise d'initialisation Braze se déclenche correctement sur les pages ou événements configurés.
- **Option 2 :** Vérifiez les requêtes réseau envoyées à Braze depuis votre page Web. De plus, la bibliothèque globale `window.braze` devrait maintenant être définie.