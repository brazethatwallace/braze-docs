{% multi_lang_include developer_guide/prerequisites/web.md %} Es ist jedoch keine zusätzliche Einrichtung erforderlich.

## Nachrichtentypen {#message-types}

Alle In-App-Nachrichten erben ihren Prototyp von [`InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html), das grundlegendes Verhalten und Eigenschaften für alle In-App-Nachrichten definiert. Die prototypischen Unterklassen sind [`SlideUpMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html), [`ModalMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html), [`FullScreenMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) und [`HtmlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html).

Jeder In-App-Nachrichtentyp ist über Inhalt, Bilder, Icons, Klickaktionen, Analytics, Anzeige und Zustellung anpassbar.

{% tabs %}
{% tab Slideup %}

[`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html)-In-App-Nachrichten tragen diesen Namen, weil sie auf mobilen Plattformen traditionell vom oberen oder unteren Bildschirmrand nach oben oder unten „gleiten“. Im Braze Web SDK werden diese Nachrichten eher als Growl- oder Toast-Benachrichtigung angezeigt, um dem vorherrschenden Paradigma im Internet zu entsprechen. Sie nehmen nur einen kleinen Teil des Bildschirms ein und bieten eine effektive, unaufdringliche Messaging-Funktion.

![Eine In-App-Nachricht, die vom unteren Rand eines Telefonbildschirms hereinschiebt und „Humans are complicated. Custom engagement shouldn't be.“ anzeigt. Im Hintergrund wird dieselbe In-App-Nachricht in der unteren Ecke einer Webseite dargestellt.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

[`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html)-In-App-Nachrichten erscheinen in der Mitte des Bildschirms und sind von einem halbtransparenten Panel umrahmt. Sie eignen sich für wichtigere Nachrichten und können mit bis zu zwei Klickaktion- und Analytics-fähigen Buttons ausgestattet werden.

![Eine modale In-App-Nachricht in der Mitte eines Telefonbildschirms mit dem Text „Humans are complicated. Custom engagement shouldn't be.“ Im Hintergrund wird dieselbe In-App-Nachricht in der Mitte einer Webseite dargestellt.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Vollbild %}

[`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html)-In-App-Nachrichten eignen sich hervorragend, um den Inhalt und die Wirkung Ihrer Kommunikation mit Nutzer:innen zu maximieren. In schmalen Browserfenstern (z. B. im mobilen Internet) nehmen `full`-In-App-Nachrichten das gesamte Browserfenster ein. In größeren Browserfenstern werden `full`-In-App-Nachrichten ähnlich wie `modal`-In-App-Nachrichten angezeigt. Die obere Hälfte einer `full`-In-App-Nachricht enthält ein Bild, und die untere Hälfte ermöglicht bis zu acht Textzeilen sowie bis zu zwei Klickaktion- und Analytics-fähige Buttons.

![Eine Vollbild-In-App-Nachricht, die auf dem gesamten Telefonbildschirm angezeigt wird und „Humans are complicated. Custom engagement shouldn't be.“ zeigt. Im Hintergrund wird dieselbe In-App-Nachricht groß in der Mitte einer Webseite dargestellt.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Benutzerdefiniertes HTML %}

[`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html)-In-App-Nachrichten eignen sich für vollständig angepasste Nutzerinhalte. Benutzerdefiniertes HTML wird in einem iFrame angezeigt und kann umfangreiche Inhalte wie Bilder, Schriftarten, Videos und interaktive Elemente enthalten, was die volle Kontrolle über Aussehen und Funktionalität der Nachricht ermöglicht. Diese unterstützen eine JavaScript-Schnittstelle `brazeBridge`, um Methoden des Braze Web SDK aus Ihrem HTML heraus aufzurufen. Weitere Details finden Sie in unseren [Best Practices]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices).

{% alert important %}
Um HTML-In-App-Nachrichten über das Web SDK zu aktivieren, **müssen** Sie die Initialisierungsoption `allowUserSuppliedJavascript` an Braze übergeben, z. B. `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Dies geschieht aus Sicherheitsgründen. HTML-In-App-Nachrichten können JavaScript ausführen, daher muss ein:e Website-Administrator:in sie aktivieren.
{% endalert %}

Das folgende Beispiel zeigt eine paginierte HTML-In-App-Nachricht:

![Eine HTML-In-App-Nachricht mit einem Karussell aus Inhalten und interaktiven Buttons.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}