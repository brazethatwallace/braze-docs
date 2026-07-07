---
nav_title: Notifications push
article_title: "Notifications push pour le SDK de Braze"
page_order: 2.3
description: "Cette page regroupe tout ce qui concerne les notifications push."
---

# Notifications push {#push-notifications}

> Les [notifications push]({{site.baseurl}}/user_guide/channels/push) vous permettent d'envoyer des notifications depuis votre application lorsque des événements importants se produisent. Vous pouvez envoyer une notification push lorsque vous avez de nouveaux messages instantanés à livrer, des alertes d'actualité à diffuser ou le dernier épisode de l'émission télévisée préférée de votre utilisateur prêt à être téléchargé pour un visionnage hors ligne. Elles sont également plus efficaces que la récupération en arrière-plan, car votre application ne se lance que lorsque c'est nécessaire.

{% alert note %}
Si l'option **Redirect to web URL** avec **Open web URL inside app** n'est pas sélectionnée, mais que le lien s'ouvre tout de même dans l'application, il est possible que l'application gère l'URL (par exemple, avec les liens universels sur iOS ou les App Links sur Android). Pour ouvrir le lien dans le navigateur, vérifiez que votre application délègue l'URL au navigateur système lorsque l'utilisateur appuie sur la notification, ou ajustez la gestion des URL de votre application afin que l'action au clic corresponde au paramètre du tableau de bord de Braze. Consultez la documentation push de votre plateforme pour savoir comment les actions au clic et la gestion des URL sont configurées.
{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/push_notifications.md %}
{% endsdktab %}

{% sdktab android tv %}
{% multi_lang_include developer_guide/android_tv/push_notifications.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/push_notifications.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/push_notifications.md %}
{% endsdktab %}

{% sdktab huawei %}
{% multi_lang_include developer_guide/huawei/push_notifications.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/push_notifications.md %}
{% endsdktab %}

{% sdktab safari %}
{% multi_lang_include developer_guide/safari/push_notifications.md %}
{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/push_notifications.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin)%}
{% multi_lang_include developer_guide/xamarin/push_notifications.md %}
{% endsdktab %}
{% endsdktabs %}