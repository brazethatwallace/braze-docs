---
nav_title: Intégrer le SDK
article_title: Intégrer le SDK Braze
description: "Découvrez comment intégrer le SDK de Braze."
page_order: 2.0
---

# ![Logo Braze]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"}Intégrer le SDK Braze {#braze-logo-image_buster-assetsbraze_primary_icon_blacksvg-stylefloatrightwidth120pxborder0-classnoimgborderintegrate-the-braze-sdk}

> Découvrez comment intégrer le SDK de Braze. Chaque SDK est hébergé dans son propre dépôt public GitHub, qui comprend des exemples d'applications entièrement compilables que vous pouvez utiliser pour tester les fonctionnalités de Braze ou implémenter parallèlement à vos propres applications. Pour en savoir plus, consultez [Références, dépôts et exemples d'applications]({{site.baseurl}}/developer_guide/references). Pour plus d'informations générales sur le SDK, consultez [Premiers pas : aperçu de l'intégration]({{site.baseurl}}/developer_guide/getting_started/integration_overview).

Pour consulter le contenu des fichiers README du SDK reproduit dans la documentation, voir [Guides des dépôts]({{site.baseurl}}/developer_guide/sdk_repository_guides).

{% alert tip %}
Après avoir intégré le SDK, vous pouvez activer l'[authentification SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication) afin d'ajouter un niveau de sécurité supplémentaire en empêchant les requêtes SDK non autorisées. L'authentification SDK est disponible pour Web, Android, Swift, React Native, Flutter, Unity, Cordova, .NET MAUI (Xamarin) et Expo.
{% endalert %}

{% alert note %}
Si l'initialisation du SDK échoue avec des erreurs de confiance de certificat HTTPS (par exemple, `SSLHandshakeException` avec `Trust anchor for certification path not found`), consultez [Résolution des erreurs de confiance de certificat du SDK]({{site.baseurl}}/developer_guide/sdk_integration/troubleshooting_certificate_errors).
{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/sdk_integration.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/sdk_integration.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/sdk_integration.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/sdk_integration.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/sdk_integration.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/sdk_integration.md %}
{% endsdktab %}

{% sdktab roku %}
## Intégrer le SDK Roku {#integrating-the-roku-sdk}

### Étape 1 : Ajouter les fichiers {#step-1-add-files}

Les fichiers du SDK Braze se trouvent dans le répertoire `sdk_files` du [dépôt du SDK Roku de Braze](https://github.com/braze-inc/braze-roku-sdk).

1. Ajoutez `BrazeSDK.brs` à votre application dans le répertoire `source`.
2. Ajoutez `BrazeTask.brs` et `BrazeTask.xml` à votre application dans le répertoire `components`.

### Étape 2 : Ajouter les références {#step-2-add-references}

Ajoutez une référence à `BrazeSDK.brs` dans votre scène principale à l'aide de l'élément `script` suivant :

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### Étape 3 : Configurer {#step-3-configure}

Dans `main.brs`, définissez la configuration de Braze sur le nœud global :

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

Vous pouvez trouver votre [endpoint SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) et votre clé API dans le tableau de bord de Braze.

### Étape 4 : Initialiser Braze {#step-4-initialize-braze}

Initialisez l'instance de Braze :

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Configurations optionnelles {#optional-configurations}

### Journalisation {#logging}

Pour déboguer votre intégration Braze, vous pouvez consulter la console de débogage Roku pour les journaux de Braze. Reportez-vous à la section [Debugging code](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) de Roku Developers pour en savoir plus.

{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/sdk_integration.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/sdk_integration.md %}
{% endsdktab %}

{% sdktab chatgpt apps %}
{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}
{% endsdktab %}

{% sdktab vega %}
{% multi_lang_include developer_guide/vega/sdk_integration.md %}
{% endsdktab %}
{% endsdktabs %}

{% alert note %}
Lors de l'assurance qualité de votre intégration SDK, utilisez le [débogueur du SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) pour résoudre les problèmes sans avoir à activer la journalisation détaillée dans votre application.
{% endalert %}