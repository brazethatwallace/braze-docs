---
nav_title: SDK integrieren
article_title: Integrieren Sie das Braze SDK
description: "Erfahren Sie, wie Sie das Braze SDK integrieren können."
page_order: 2.0
---

# ![Braze-Logo]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"}Integrieren Sie das Braze SDK {#braze-logo-image_buster-assetsbraze_primary_icon_blacksvg-stylefloatrightwidth120pxborder0-classnoimgborderintegrate-the-braze-sdk}

> Erfahren Sie, wie Sie das Braze SDK integrieren können. Jedes SDK wird in seinem eigenen öffentlichen GitHub-Repository gehostet, das vollständig kompilierbare Beispiel-Apps enthält, mit denen Sie die Features von Braze testen oder neben Ihren eigenen Anwendungen implementieren können. Weitere Informationen finden Sie unter [Referenzen, Repositories und Beispiel-Apps]({{site.baseurl}}/developer_guide/references). Allgemeine Informationen über das SDK finden Sie unter [Erste Schritte: Übersicht über die Integration]({{site.baseurl}}/developer_guide/getting_started/integration_overview).

Gespiegelte SDK-README-Inhalte in der Dokumentation finden Sie unter [Repository-Leitfäden]({{site.baseurl}}/developer_guide/sdk_repository_guides).

{% alert tip %}
Nach der Integration des SDK können Sie die [SDK-Authentifizierung]({{site.baseurl}}/developer_guide/sdk_integration/authentication) aktivieren, um eine zusätzliche Sicherheitsebene hinzuzufügen, indem Sie unbefugte SDK-Anfragen verhindern. Die SDK-Authentifizierung ist für Internet, Android, Swift, React Native, Flutter, Unity, Cordova, .NET MAUI (Xamarin) und Expo verfügbar.
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
Verwenden Sie bei der QA Ihrer SDK-Integration den [SDK-Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging), um Probleme zu beheben, ohne die ausführliche Protokollierung für Ihre App aktivieren zu müssen.
{% endalert %}