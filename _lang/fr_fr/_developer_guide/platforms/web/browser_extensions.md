---
nav_title: Extensions de navigateur
article_title: Intégration des extensions de navigateur pour le Web
platform: Web
page_order: 20
page_type: reference
description: "Cet article décrit comment utiliser le SDK Braze pour le Web dans vos extensions de navigateur (Google Chrome, Firefox)."

---

# Extension de navigateur {#browser-extension}

> Cet article décrit comment utiliser le SDK Braze pour le Web dans vos extensions de navigateur (Google Chrome, Firefox).

Intégrez le SDK Braze pour le Web au sein de votre extension de navigateur pour collecter des données d'analyse et afficher des messages enrichis aux utilisateurs. Cela comprend les **extensions Google Chrome** et les **modules complémentaires Firefox**.

## Ce qui est pris en charge {#whats-supported}

En général, comme les extensions sont composées de HTML et de JavaScript, vous pouvez utiliser Braze pour ce qui suit :

* **Analyses** : Capturez des événements personnalisés, des attributs et identifiez même les utilisateurs récurrents au sein de votre extension. Utilisez ces caractéristiques de profil pour alimenter la communication cross-canal.
* **Messages in-app** : Déclenchez des messages in-app lorsque les utilisateurs agissent au sein de votre extension, en utilisant notre messagerie HTML native ou personnalisée.
* **Content Cards** : Ajoutez un flux de cartes natives à votre extension pour l'onboarding ou le contenu promotionnel.
* **Notification push Web** : Envoyez des notifications en temps opportun, même lorsque votre page Web n'est pas actuellement ouverte.

## Ce qui n'est pas pris en charge {#whats-not-supported}

* L'utilisation du SDK Braze depuis un service de traitement n'est pas prise en charge. Vous pouvez toutefois utiliser le SDK Braze dans la fenêtre contextuelle ou la page de paramètres de votre extension.

## Types d'extensions {#extension-types}

Braze peut être inclus dans les parties suivantes de votre extension :

| Partie | Détails | Ce qui est pris en charge |
|--------|-------|------|
| Page contextuelle | La page [Popup](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups) est une boîte de dialogue qui peut être affichée aux utilisateurs lorsqu'ils cliquent sur l'icône de votre extension dans la barre d'outils du navigateur. | Analyses, messages in-app et Content Cards |
| Scripts d'arrière-plan | Les [scripts d'arrière-plan](https://developer.chrome.com/extensions/background_pages) (Manifest v2 uniquement) permettent à votre extension d'inspecter et d'interagir avec la navigation de l'utilisateur ou de modifier les pages Web (par exemple, comment les bloqueurs de publicité détectent et modifient le contenu des pages). | Analyses, messages in-app et Content Cards.<br><br>Les scripts d'arrière-plan ne sont pas visibles des utilisateurs, donc en ce qui concerne l'envoi de messages, vous devez communiquer à l'aide des onglets du navigateur ou de votre page contextuelle lors de l'affichage des messages. |
| Pages d'options | La [page d'options](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages) permet à vos utilisateurs de basculer les paramètres de votre extension. Il s'agit d'une page HTML autonome qui ouvre un nouvel onglet. | Analyses, messages in-app et Content Cards |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3 aria-label="Types d'extensions" }

## Autorisations {#permissions}

Aucune autorisation supplémentaire n'est requise dans votre `manifest.json` lors de l'intégration du SDK Braze (`braze.min.js`) en tant que fichier local associé à votre extension.

Toutefois, si vous utilisez [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/), si vous faites référence au SDK Braze à partir d'une URL externe, ou si vous avez défini une politique de sécurité du contenu stricte pour votre extension, vous devrez ajuster le paramètre [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) dans votre `manifest.json` pour autoriser les sources de scripts distantes.

## Démarrage {#getting-started}

{% alert tip %}
Avant de commencer, assurez-vous d'avoir lu le [guide de configuration initiale du SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) pour le Web afin d'en savoir plus sur notre intégration JavaScript en général.  <br><br>Vous pouvez également mettre en signet la [référence du SDK JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) pour obtenir tous les détails sur les différentes méthodes et options de configuration du SDK.
{% endalert %}

Pour intégrer le SDK Braze pour le Web, vous devez d'abord télécharger une copie de la dernière bibliothèque JavaScript. Cela peut se faire en utilisant NPM ou en le téléchargeant directement depuis le [CDN de Braze](https://js.appboycdn.com/web-sdk/latest/braze.min.js).

Sinon, si vous préférez utiliser [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/) ou une copie hébergée à l'extérieur du SDK Braze, gardez à l'esprit que le chargement de ressources externes nécessite d'ajuster le paramètre [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) dans votre `manifest.json`.

Une fois téléchargé, assurez-vous de copier le fichier `braze.min.js` dans le répertoire de votre extension.

### Fenêtres contextuelles d'extension {#popup}

Pour ajouter Braze à une fenêtre contextuelle d'extension, référencez le fichier JavaScript local dans votre `popup.html`, comme vous le feriez sur un site Web classique. Si vous utilisez Google Tag Manager, vous pouvez ajouter Braze en utilisant nos [modèles Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/).

```html
<html>
    <title>popup.html</title>
    <!-- Add the Braze library -->
    <script src="/relative/path/to/braze.min.js"></script>
    <script>
    // Initialize Braze here
    </script>
</html>
```

### Script d'arrière-plan (Manifest v2 uniquement) {#background-script}

Pour utiliser Braze dans le script d'arrière-plan de votre extension, ajoutez la bibliothèque Braze à votre `manifest.json` dans le tableau `background.scripts`. La variable globale `braze` sera alors disponible dans le contexte de votre script d'arrière-plan.


```json
{
    "manifest_version": 2,
    "background": {
        "scripts": [
            "relative/path/to/braze.min.js",
            "background.js"
        ]
    }
}
```

### Page d'options {#options-page}

Si vous utilisez une page d'options (via les propriétés de manifeste `options` ou `options_ui`), vous pouvez inclure Braze comme vous le feriez dans les [instructions `popup.html`](#popup).

## Initialisation {#initialization}

Une fois le SDK inclus, vous pouvez initialiser la bibliothèque comme d'habitude.

Étant donné que les cookies ne sont pas pris en charge dans les extensions de navigateur, vous pouvez les désactiver en initialisant avec `noCookies: true`.

```javascript
braze.initialize("YOUR-API-KEY-HERE", {
    baseUrl: "YOUR-API-ENDPOINT",
    enableLogging: true,
    noCookies: true
});
```

Pour plus d'informations sur les options d'initialisation prises en charge, consultez la [référence du SDK Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

## Notification push {#push}

Les boîtes de dialogue contextuelles d'extension ne permettent pas de demander des notifications push (elles ne disposent pas de barre d'URL dans la navigation). Pour vous enregistrer et demander une autorisation de notification push dans la boîte de dialogue contextuelle d'une extension, vous devrez utiliser un contournement par un domaine alternatif, tel que décrit dans [Domaine alternatif de notification push]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain).