{% alert note %}
Wie in der [Shopify-Übersicht]({{site.baseurl}}/shopify_overview) erwähnt, müssen Ihre Entwickler:innen Braze-SDK-Code integrieren, wenn Sie ein Erfassungsformular eines Drittanbieters verwenden möchten. Damit können Sie die E-Mail-Adresse und den globalen E-Mail-Abo-Status aus Formularübermittlungen erfassen. Konkret müssen Sie diese Methoden in Ihrer `theme.liquid`-Datei implementieren und testen:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Legt die E-Mail-Adresse im Nutzerprofil fest
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Aktualisiert den globalen E-Mail-Abo-Status
{% endalert %}