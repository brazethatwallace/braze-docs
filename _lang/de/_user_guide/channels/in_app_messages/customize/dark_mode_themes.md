---
nav_title: Dark-Mode-Themes
article_title: Dark-Mode-Themes
page_order: 2
description: "Dieser Referenzartikel behandelt die Dark-Mode-Unterstützung für Braze In-App-Nachrichten, einschließlich der Einrichtung eines Dark-Mode-Themes und Kompatibilitätshinweisen."
channel:
  - in-app messages

---

# Dark-Mode-Themes {#dark-mode-themes}

> Dieser Artikel gilt für den [traditionellen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional). Der Dark Mode bietet Nutzer:innen die Möglichkeit, eine systemweite Farbpräferenz festzulegen (eingeführt mit [Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) und [iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)). „Dunkle“ Themes sollen den Akkuverbrauch senken und die Augen der Nutzer:innen schonen, während sie App-Entwickler:innen die Möglichkeit bieten, dunkle Farbthemen zu implementieren.

Braze In-App-Nachrichten unterstützen das Hinzufügen eines alternativen Dark-Themes, um Ihren Nutzer:innen basierend auf deren Präferenz die passende Farbnachricht zu liefern und die Konsistenz mit dem Design Ihrer App zu wahren.

## So funktioniert der Dark Mode {#how-dark-mode-works}

Nutzer:innen mit mindestens Android 10 oder iOS 13 und höher können den Dark Mode in den Geräteeinstellungen ein- oder ausschalten.

Wenn der Dark Mode aktiviert ist, wechseln die nativen Menüs und Bildschirme des Geräts (Push-Benachrichtigungen, Geräteeinstellungen usw.) zu einem dunklen Grau. Apps können den Dark Mode ebenfalls unterstützen, indem alternative Themes im App-Code festgelegt werden.

## Ein Dark-Mode-Theme einrichten {#setting-a-dark-mode-theme}

Der Dark Mode befindet sich im Tab **Entwerfen** beim [Erstellen einer In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) und ermöglicht es Ihnen, ein alternatives Farbthema für Nutzer:innen hinzuzufügen, die den Dark Mode auf ihrem Gerät verwenden.

![Nutzer:in wechselt zwischen Light-Mode-Stil und Dark-Mode-Stil im Tab „Stil“ beim Erstellen einer In-App-Nachricht.]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

Wenn diese Option aktiviert ist, können Sie dunkle Themenfarben für Ihre In-App-Nachricht über den Farbwähler auswählen oder vorhandene [Farbprofile]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/in_app_message_template#color-profile) verwenden, um bestehende dunkle oder helle Themes wiederzuverwenden.

{% alert note %}
Sie können dieses Feature auch nutzen, wenn Ihre App kein eigenes dunkles Theme anbietet. Geräte, die den Dark Mode nicht unterstützen, zeigen jedoch standardmäßig das helle Theme an. Das Ändern des Geräte-Themes auf Android, während eine In-App-Nachricht angezeigt wird, ändert nicht das Theme, das für diese In-App-Nachricht verwendet wird.
{% endalert %}

### Den Dark Mode konsistent verwenden {#using-dark-mode-consistently}

Um den Dark Mode für alle In-App-Nachrichten zu verwenden, erstellen Sie zunächst ein Farbprofil, das zu Ihrem Dark-Mode-Theme passt.

1. Gehen Sie zu **Inhalt** > **In-App Message**.
2. Wählen Sie **Templates erstellen** und dann [Farbprofil]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/in_app_message_template#color-profile) aus dem Dropdown-Menü.
3. Erstellen und speichern Sie Ihr Farbprofil.

Wenn Sie eine Dark-Mode-Version einer In-App-Nachricht erstellen, können Sie dieses Farbprofil auswählen, um das Erscheinungsbild Ihrer In-App-Nachrichten konsistent zu halten.

## Kompatibilität {#compatibility}

- Ihre Nutzer:innen müssen iOS-Geräte mit Version 13 oder höher oder Android-Geräte mit Version 10 oder höher verwenden.
- Braze iOS SDK or Software-Development-Kit v3.21.0+ und Braze Android SDK or Software-Development-Kit v3.8.0+ sind erforderlich.

{% alert note %}
Dark-Mode-Apps wurden mit Android 10 und iOS 13 eingeführt. Nutzer:innen, die ihre Geräte nicht mindestens auf diese Versionen aktualisiert haben, sehen nur das helle Theme. <br><br>Campaigns werden weiterhin an alle Nutzer:innen ausgeliefert, die für die von Ihnen ausgewählte Zielgruppe berechtigt sind, unabhängig von der Dark-Mode-Einstellung oder der Betriebssystemversion der Nutzer:innen.
{% endalert %}

## HTML-In-App-Nachrichten verwenden {#using-html-in-app-messages}

Um ein dunkles und helles Theme für HTML-In-App-Nachrichten zu erstellen, können Sie das CSS-Media-Feature [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) verwenden, um die Präferenz der Nutzer:innen zu erkennen.

Zum Beispiel:

```css
@media (prefers-color-scheme: dark) {
  body {
    background: #333;
    color: white;
  }
}

@media (prefers-color-scheme: light) {
  body {
    background: white;
    color: #555;
  }
}
```

