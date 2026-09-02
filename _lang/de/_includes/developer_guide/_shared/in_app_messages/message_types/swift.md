{% tab swift %}
Jeder In-App-Nachrichtentyp ist in Bezug auf Inhalt, Bilder, Symbole, Klickaktionen, Analytics, Anzeige und Zustellung in hohem Maße anpassbar. Sie sind aufgezählte Typen von `Braze.InAppMessage`, die das grundlegende Verhalten und die Eigenschaften aller In-App-Nachrichten definieren. Eine vollständige Liste der Eigenschaften von In-App-Nachrichten und deren Verwendung finden Sie in der [`InAppMessage`-Klasse](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

Dies sind die verfügbaren In-App-Nachrichtentypen in Braze und wie sie für Endnutzer:innen aussehen.

{% subtabs %}
{% subtab Slideup %}

[`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct)-In-App-Nachrichten heißen so, weil sie vom oberen oder unteren Bildschirmrand aus „nach oben“ oder „nach unten“ gleiten. Sie bedecken nur einen kleinen Teil des Bildschirms und bieten eine effektive und unaufdringliche Möglichkeit zur Nachrichtenübermittlung.

![Eine Slideup-In-App-Nachricht am unteren und oberen Rand eines Telefondisplays.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width:35%;border:none;"}


{% endsubtab %}
{% subtab Modal %}

[`Modal`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modal-swift.struct)-In-App-Nachrichten erscheinen in der Mitte des Bildschirms und werden von einem durchscheinenden Panel eingerahmt. Sie eignen sich für wichtigere Nachrichten und können mit bis zu zwei Analytics-fähigen Buttons ausgestattet werden.

![Eine modale In-App-Nachricht in der Mitte eines Telefondisplays.]({% image_buster /assets/img/modal-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Modal Image %}

[`Modal Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modalimage-swift.struct)-In-App-Nachrichten erscheinen in der Mitte des Bildschirms und werden von einem durchscheinenden Panel eingerahmt. Diese Nachrichten ähneln dem Typ `Modal`, jedoch ohne Kopfzeile oder Nachrichtentext. Sie eignen sich für wichtigere Nachrichten und können mit bis zu zwei Analytics-fähigen Buttons ausgestattet werden.

![Eine modale Bild-In-App-Nachricht in der Mitte eines Telefondisplays.]({% image_buster /assets/img/modal-full-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Fullscreen %}

[`Full`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/full-swift.struct)-In-App-Nachrichten sind nützlich, um den Inhalt und die Wirkung Ihrer Kommunikation mit Nutzer:innen zu maximieren. Die obere Hälfte einer `Full`-In-App-Nachricht enthält ein Bild, und die untere Hälfte zeigt Text sowie bis zu zwei Analytics-fähige Buttons an.

![Eine Vollbild-In-App-Nachricht, die auf dem gesamten Telefondisplay angezeigt wird.]({% image_buster /assets/img/full-screen-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Full Screen Image %}

[`Full Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/fullimage-swift.struct)-In-App-Nachrichten ähneln `Full`-In-App-Nachrichten, jedoch ohne Kopfzeile oder Nachrichtentext. Dieser Nachrichtentyp ist nützlich, um den Inhalt und die Wirkung Ihrer Kommunikation mit Nutzer:innen zu maximieren. Eine `Full Image`-In-App-Nachricht enthält ein Bild, das sich über den gesamten Bildschirm erstreckt, mit der Option, bis zu zwei Analytics-fähige Buttons anzuzeigen.

![Eine bildschirmfüllende Bild-In-App-Nachricht, die auf dem gesamten Telefondisplay angezeigt wird.]({% image_buster /assets/img/full-screen-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Custom HTML %}

[`HTML`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/html-swift.struct)-In-App-Nachrichten sind nützlich, um vollständig angepasste Nutzer:innen-Inhalte zu erstellen. Benutzerdefinierte HTML-Full-In-App-Nachrichteninhalte werden in einer `WKWebView` angezeigt und können optional weiteren Rich Content wie Bilder und Schriftarten enthalten, sodass Sie die volle Kontrolle über das Aussehen und die Funktionalität der Nachrichten haben. <br><br>iOS-In-App-Nachrichten unterstützen eine JavaScript-`brazeBridge`-Schnittstelle, um Methoden des Braze Web SDK aus Ihrem HTML-Code heraus aufzurufen. Weitere Details finden Sie in unseren [Best Practices]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices).

Das folgende Beispiel zeigt eine paginierte HTML-Full-In-App-Nachricht:

![Eine HTML-In-App-Nachricht mit einem Karussell von Inhalten und interaktiven Buttons.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

Beachten Sie, dass die Anzeige von angepassten HTML-In-App-Nachrichten in einem iFrame unter iOS und Android derzeit nicht unterstützt wird.

{% endsubtab %}
{% subtab Control %}

[`Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/control-swift.struct)-In-App-Nachrichten enthalten keine UI-Komponente und werden in erster Linie zu Analytics-Zwecken verwendet. Dieser Typ wird verwendet, um den Empfang einer In-App-Nachricht zu überprüfen, die an eine Kontrollgruppe gesendet wurde.

Weitere Einzelheiten zur automatischen Variantenoptimierung und zu Kontrollgruppen finden Sie unter [Mit BrazeAI<sup>TM</sup> optimieren]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

{% endsubtab %}
{% endsubtabs %}
{% endtab %}