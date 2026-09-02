---
nav_title: "Video in benutzerdefiniertem HTML"
article_title: "Video in benutzerdefiniertem HTML"
page_order: 4
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie Videos in Ihre HTML-In-App-Nachrichten einbetten können."
channel:
  - in-app messages
---

# Video in benutzerdefinierten HTML-In-App-Nachrichten {#video}

> Dieser Artikel gilt für [benutzerdefinierte HTML-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html) im [traditionellen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

## Videos einbetten {#embed-videos}

Um ein Video in einer HTML-In-App-Nachricht abzuspielen, fügen Sie das folgende `<video>`-Element in Ihr HTML ein und ersetzen Sie die Videonamen durch den Dateinamen Ihrer Datei (oder die URL des Remote-Assets). Weitere mögliche `<video>`-Optionen finden Sie in den [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video).

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

Um ein lokales Video-Asset zu verwenden, stellen Sie sicher, dass Sie diese Datei beim Hochladen von Assets in Ihre Campaign einschließen.

{% alert note %}
Videoinhalte sind nur verfügbar, wenn das Gerät eine angemessene Netzwerkgeschwindigkeit hat, es sei denn, das Video wird lokal vom Gerät geladen.
{% endalert %}

## Hinweise für Android {#android-considerations}

Um Videos und andere HTML5-Inhalte in HTML-In-App-Nachrichten auf Android einzubetten, muss die Hardwarebeschleunigung in der Activity aktiviert sein, in der die In-App-Nachricht angezeigt wird. Weitere Informationen finden Sie im [Android-Entwicklerhandbuch]({{site.baseurl}}/developer_guide/in_app_messages/html_messages#android_embedding-youtube-content).

**Automatische Wiedergabe**: Auch bei aktivierter Hardwarebeschleunigung können Android-WebViews eine Geste der Nutzer:innen erfordern, um die Medienwiedergabe zu starten. Wenn Sie die automatische Wiedergabe benötigen, konfigurieren Sie die WebView, die zum Rendern von HTML-In-App-Nachrichten verwendet wird, so, dass die Anforderung einer Geste deaktiviert wird, indem Sie [`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean)) setzen. Dies erfordert eine Anpassung auf SDK-Ebene, wie HTML-In-App-Nachrichten angezeigt werden. Eine Anleitung zur Einrichtung finden Sie unter [In-App-Nachrichten für das Braze SDK anpassen]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android).

## Hinweise für iOS {#ios-considerations}

Zur Unterstützung von iOS-Geräten:

- Sie müssen das Attribut `playsinline` einfügen, da die Vollbildwiedergabe nicht unterstützt wird.
- **Die automatische Wiedergabe ist auf iOS nicht garantiert**. Das Wiedergabeverhalten auf iOS hängt von `WKWebView` und den Medienrichtlinien auf Betriebssystemebene ab und kann eine Geste der Nutzer:innen erfordern, selbst wenn `autoplay` und `muted` gesetzt sind. Testen Sie Ihre HTML-In-App-Nachricht auf Ihren Ziel-iOS-Versionen und -Geräten.

Wenn die automatische Wiedergabe erforderlich ist und Ihre Tests zeigen, dass sie standardmäßig nicht funktioniert, können Sie die `WKWebViewConfiguration`, die von HTML-In-App-Nachrichten verwendet wird, anpassen, um die Anforderung einer Nutzeraktion für die Medienwiedergabe zu ändern, beispielsweise durch Setzen der Eigenschaft `mediaTypesRequiringUserActionForPlayback`. Dies erfordert eine Anpassung auf SDK-Ebene. Für Swift-Ressourcen siehe [In-App-Nachrichten für das Braze SDK anpassen]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=swift) und [Hinzufügen der Braze-JavaScript-Schnittstelle zu WebViews für Swift]({{site.baseurl}}/developer_guide/in_app_messages/html_messages?sdktab=swift).

## Hinweise für Web {#web-considerations}

Die meisten modernen Browser erlauben die automatische Wiedergabe nur unter bestimmten Bedingungen (üblicherweise wenn das Video stummgeschaltet ist). Wenn Sie `autoplay` in einer Web-In-App-Nachricht verwenden, fügen Sie `muted` hinzu und testen Sie in Ihren unterstützten Browsern und auf Ihren Geräten, da die Browser-Richtlinien variieren und in einigen Fällen möglicherweise eine Geste der Nutzer:innen erfordern.

Um YouTube-Videos in einer Web-In-App-Nachricht automatisch abzuspielen, fügen Sie den URL-Parameter `&autoplay=1` hinzu. Zum Beispiel wird das folgende Video automatisch abgespielt, stummgeschaltet (`&mute=1`) und ohne Steuerelemente (`&controls=0`) angezeigt:

```html
<iframe class="video" src="https://www.youtube.com/embed/VPIPAc4oQqw?autoplay=1&mute=1&controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Wie YouTube-Videos angezeigt werden {#how-youtube-videos-display}

- In YouTube eingebettete In-App-Nachrichten können je nach Plattform direkt in der App oder in einem separaten Tab innerhalb der App angezeigt werden.
- Der Text der In-App-Nachricht wird möglicherweise nicht angezeigt, wenn die YouTube-Einbettung dargestellt wird.

## Fehlerbehebung {#troubleshooting}

Wenn Ihre In-App-Nachricht Ihr Video nicht anzeigt:

- Überprüfen Sie, ob Ihre URL gültig ist.
- Überprüfen Sie, ob die Deklaration `type="video/mp4"` vorhanden ist (bei Nicht-YouTube-Videos).
- Fügen Sie fehlende schließende Tags hinzu und beheben Sie Tippfehler.