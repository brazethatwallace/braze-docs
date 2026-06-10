---
nav_title: Intégrer le SDK
article_title: Intégrer le SDK Braze
description: "Découvrez comment intégrer le SDK de Braze."
page_order: 2.0
---

# ![Logo Braze]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"}Intégrer le SDK Braze {#braze-logo-image_buster-assetsbraze_primary_icon_blacksvg-stylefloatrightwidth120pxborder0-classnoimgborderintegrate-the-braze-sdk}

> Découvrez comment intégrer le SDK de Braze. Chaque SDK est hébergé dans son propre dépôt public GitHub, qui comprend des exemples d'applications entièrement compilables que vous pouvez utiliser pour tester les fonctionnalités de Braze ou implémenter parallèlement à vos propres applications. Pour en savoir plus, consultez [Références, dépôts et exemples d'applications]({{site.baseurl}}/developer_guide/references/). Pour plus d'informations générales sur le SDK, consultez [Premiers pas : aperçu de l'intégration]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

Pour consulter le contenu des fichiers README du SDK reproduit dans la documentation, voir [Guides des dépôts]({{site.baseurl}}/developer_guide/sdk_repository_guides/).

{% alert tip %}
Après avoir intégré le SDK, vous pouvez activer l'[authentification SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication/) afin d'ajouter un niveau de sécurité supplémentaire en empêchant les requêtes SDK non autorisées. L'authentification SDK est disponible pour Web, Android, Swift, React Native, Flutter, Unity, Cordova, .NET MAUI (Xamarin) et Expo.
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
{% multi_lang_include developer_guide/roku/sdk_integration.md %}
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
Lors de l'assurance qualité de votre intégration SDK, utilisez l'[outil de débogage du SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging/) pour résoudre les problèmes sans avoir à activer la journalisation détaillée dans votre application.
{% endalert %}