---
nav_title: Vorbereitungsleitfaden
article_title: Vorbereitungsleitfaden für In-App-Nachrichten
page_order: 0.5

page_type: reference
description: "Dieser Artikel behandelt Fragen und Best Practices, die Sie vor dem Erstellen von In-App-Nachrichten berücksichtigen sollten, einschließlich Targeting, Zeitplanung, Inhalt, Performance und Konversionen."
channel: in-app messages
toc_headers: h2
---

# Vorbereitungsleitfaden für In-App-Nachrichten {#in-app-message-prep-guide}

> Bevor Sie Ihre In-App-Nachrichten erstellen, sollten Sie die folgenden Themen berücksichtigen, um den Prozess effizienter zu gestalten.

## Allgemeine Überlegungen {#general-considerations}

- Wenn Sie eine Campaign erstellen: Wie viele Varianten dieser Nachricht möchten Sie anzeigen? Ideen für Variantentests finden Sie unter [Tipps für verschiedene Kanäle]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#tips-different-channels).
- Wenn Sie einen Canvas erstellen: Wird diese Nachricht in diesem Schritt mit anderen Messaging-Kanälen kombiniert?
- Wann soll [Ihre Nachricht ablaufen]({{site.baseurl}}/canvas_in-app_messages)?

## Überlegungen zum Targeting {#targeting-considerations}

- In-App-Nachrichten eignen sich am besten für Nutzer:innen, die Ihre App regelmäßig besuchen. Schließen Sie diese Zielgruppe ein?
- Wo sollen Ihre Nutzer:innen Ihre Nachricht sehen? In Ihrer Web-App? In Ihrer mobilen App?
- Welches Event soll diese Nachricht triggern?
- Verwenden einige Ihrer Nutzer:innen ältere Versionen Ihrer App? Falls ja, können sie möglicherweise einige Elemente Ihrer Nachricht nicht sehen.
- Für welchen Gerätetyp oder welche Geräte erstellen Sie diese Nachricht? Denken Sie daran, dass Sie Ihre Nachricht über das Feld **Vorschau** oder den Tab **Test** in der Vorschau ansehen können. Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message).

## Zeitplanung, Verzögerungen und Sitzungsstarts {#scheduling-delays-and-session-starts}

Wenn eine In-App-Nachrichten-Campaign mit **Schedule Delay** einen Trigger beim Sitzungsstart hat, kann eine Nutzer:in, die eine Sitzung startet und dann die App schließt, bevor die In-App-Nachricht angezeigt wird, diese Nachricht beim nächsten Sitzungsstart erhalten, nachdem die Verzögerung abgelaufen ist.

In-App-Nachrichten-Campaigns können die Zustellung nach dem Trigger um bis zu zwei Stunden verzögern. Für eine längere Wartezeit fügen Sie einen [Delay]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)-Schritt vor einem In-App-Nachrichten-Schritt in einem Canvas hinzu. Informationen zur Einrichtung der Verzögerung finden Sie unter [Aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-2-select-delay-length).

Dieses Timing kann zu unerwartetem Anzeigeverhalten führen, insbesondere wenn **Re-evaluate campaign eligibility before displaying** in der Campaign nicht ausgewählt ist.

Beispielsweise könnte eine Nutzer:in eine In-App-Nachricht mit einer Verzögerung von acht Sekunden einen Monat nach dem Start der Campaign erhalten. Das kann passieren, wenn sie eine Sitzung gestartet, die Sitzung sofort beendet, einen Monat später eine neue Sitzung gestartet hat und dann acht Sekunden später die In-App-Nachricht erhalten hat. Wenn sie die App verlässt, ohne sie zu schließen, wird die In-App-Nachricht angezeigt, wenn sie zur App zurückkehrt.

## Überlegungen zum Inhalt {#content-considerations}

- Welche Sprachen werden Sie in dieser Nachricht verwenden?
- Wie lauten Ihre Überschrift und Ihr Fließtext? Sind sie ansprechend und relevant für Ihre Nutzer:innen?
- In-App-Nachrichten werden nur für eine begrenzte Zeit angezeigt. Ist Ihr Text prägnant und einprägsam?
- Werden Sie [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) verwenden, um angepasste Texte hinzuzufügen?
- Müssen Nutzer:innen Nachrichtentext kopieren (z. B. einen Rabatt- oder Gutscheincode)? Auf iOS und Android können Nutzer:innen durch langes Drücken auf Text oder Texteingabefelder Inhalte kopieren. Langes Drücken funktioniert nicht bei Bildern – verwenden Sie daher Text oder Texteingabefelder anstelle von Bildern, die Codes oder andere Texte enthalten, die Nutzer:innen möglicherweise kopieren müssen.
- Befindet sich bei Vollbild-In-App-Nachrichten Ihr Bild oder anderes Medium innerhalb der [Safe Zone]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen#image-safe-zone)?
- Möchten Sie bei Umfrage-In-App-Nachrichten Attribute oder Einreichungen protokollieren? Haben Sie Ihre Bestätigungsseite eingerichtet?
- Enthält Ihr HTML bei angepassten HTML-In-App-Nachrichten UTF-8-Codierung, um Sonderzeichen korrekt anzuzeigen? Weitere Informationen finden Sie unter [Angepasste HTML-In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#character-encoding).
- Wenn Sie Video in Ihre In-App-Nachricht einbinden: Braze erzwingt zwar keine technische Begrenzung der Videodateigröße für die lokale Wiedergabe auf dem Gerät, bedenken Sie jedoch, dass Nutzer:innen möglicherweise langsame Verbindungen, kostspielige Datentarife oder begrenzten Speicher haben. Optimieren Sie Videodateien, um Qualität und Dateigröße auszubalancieren.

## Performance von In-App-Nachrichten optimieren {#optimize-in-app-message-performance}

Braze liefert berechtigte In-App-Nachrichten-Trigger zu Beginn der Sitzung an Nutzer:innen. Die Vorbereitung vieler Nachrichten mit Liquid kann den Sitzungsstart verzögern und die App-Performance beeinträchtigen.

Wenn dieser Vorgang mehr als einige Sekunden dauert, kann Braze das verbleibende Liquid-Rendering zurückstellen. Jede Nachricht wird dann beim Auslösen gerendert und bei Bedarf abgerufen. Diese [Templated Delivery]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages) schützt Ihre Nutzer:innen vor schlechter App-Performance durch erhöhte Antwortlatenz.

Nutzen Sie diese Best Practices, um Ihre Nachrichtenzustellung zu beschleunigen:

- Richten Sie das Targeting nur auf Nutzer:innen aus, die den Trigger der Campaign auslösen können. Zu breites Targeting kann dazu führen, dass Nutzer:innen einen In-App-Nachrichten-Trigger erhalten, den sie nie aktivieren können. Zum Beispiel kann eine In-App-Nachricht, die durch eine bestimmte Push-Campaign getriggert wird, im Umfang eingeschränkt werden, sodass sie dieselbe Zielgruppe verwendet. Dies lässt sich ähnlich auf andere Campaign-Typen, Canvases, angepasste Events, die nur von bestimmten Nutzer:innen getriggert werden können, und mehr anwenden.
- Legen Sie ein Enddatum für zeitkritische Campaigns fest. Stoppen Sie Campaigns, wenn Sie nicht mehr erwarten, dass sie Impressionen erhalten.
- Vermeiden Sie es, große statische Stylesheets, Skripte oder Base64-kodierte Medien-Assets direkt in die Nachricht oder über einen Content-Block einzufügen. Verwenden Sie stattdessen die [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library), um die Renderzeit Ihrer Nachricht zu reduzieren.
- Reduzieren Sie komplexe Verzweigungs- oder Schleifen-Liquid-Logik.
- Aktivieren Sie die erneute Berechtigung nur, wenn Nutzer:innen eine Nachricht mehrmals erhalten sollen. Wenn die erneute Berechtigung deaktiviert bleibt, stoppt Braze die Zustellung des In-App-Nachrichten-Triggers, nachdem Nutzer:innen ihn gesehen haben. Weitere Informationen finden Sie unter [Erneute Berechtigung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).
- Geben Sie wichtigen Campaigns eine höhere Priorität. Braze rendert berechtigte Nachrichten mit höherer Priorität zuerst, wodurch Templated Delivery weniger wahrscheinlich wird, wenn Nutzer:innen für viele Campaigns qualifiziert sind. Weitere Informationen finden Sie unter [Priorität wählen]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority).

### Statischen Code und Assets trennen {#separate-static-code-and-assets}

Behalten Sie personalisierte Werte und bedingte Regeln in der Nachricht. Hosten Sie wiederverwendbare CSS-, JavaScript- und Medien-Assets in der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) und verlinken Sie diese.

Dies muss nicht für alle Skripte und Styles durchgeführt werden. Es ist vor allem hilfreich, um Aufblähung durch große Assets wie gemeinsame Marken-Styles und komplexe Skripte wie interaktive Widgets zu reduzieren.

Stylesheets und Skripte der Medienbibliothek werten kein Liquid aus, sodass das Gerät der Nutzer:innen sie cachen kann. Das folgende Beispiel behält dynamische Werte inline und lädt wiederverwendbaren Code aus statischen Dateien:

{% raw %}

```liquid
<head>
  <style>
    /* Select a hero image URL based on the user's subscription tier. */
    {% capture hero_image_url %}
      {% if custom_attribute.${subscription_tier} == 'premium' %}
        https://braze-images.com/path/to/premium/hero.jpg
      {% else %}
        https://braze-images.com/path/to/standard/hero.jpg
      {% endif %}
    {% endcapture %}
    /* Assigning to a CSS variable so it can be used inside our stylesheet. */
    :root {
      --hero-image: url("{{ hero_image_url | url_escape }}");
    }
  </style>
  <script>
    // Assigning to the global window object so the value can be referenced in our script.
    window.brandConfig = {
      subscriptionTier: "{{custom_attribute.${subscription_tier} | json_escape }}"
    };
  </script>
  <!-- Linking to a stylesheet from the Braze media library. -->
  <link rel="stylesheet" href="https://braze-images.com/path/to/media/library/asset.css">
  <!-- Linking to a script from the Braze media library. -->
  <script src="https://braze-images.com/path/to/other/media/library/asset.js" defer></script>
</head>

<body>
  <div class="hero"></div>
  <div class="user-styles" data-subscription-tier="{{custom_attribute.${subscription_tier} | escape}}">
    ...
  </div>
</body>
```

{% endraw %}

Das Stylesheet der Medienbibliothek kann die CSS-Variablen referenzieren und andere wiederverwendbare Styles definieren:

```css
.hero {
  background-image: var(--hero-image);
}

.user-styles {
  /* styles for all users */
}

.user-styles[data-subscription-tier="premium"] {
  /* premium subscription tier user styles, color scheme, etc */
}

.user-styles[data-subscription-tier="standard"] {
  /* standard subscription tier user styles, color scheme, etc */
}
```

Das Skript der Medienbibliothek kann die Inline-JavaScript-Variablen verwenden, um wiederverwendbares Verhalten hinzuzufügen:

```javascript
const config = window.brandConfig || {};

if (config.subscriptionTier === "standard") {
  // add some sort of logic to show a "subscribe to premium" button
} else if (config.subscriptionTier === "premium") {
  // thank the user for being a premium user
}
```

## Überlegungen zur Konversion {#conversion-considerations}

- Was ist Ihr Ziel für diese Nachricht? Wie können Sie das in Ihrer Nachricht darstellen?
- Bieten Ihre Buttons Optionen, die für Ihre Nutzer:innen sinnvoll sind? Was ist Ihr [primärer Call-to-Action]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#buttons)?
- Verlinken Sie per [Deeplink auf andere In-App-Inhalte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content)? Verwenden Sie diese In-App-Nachricht, um eine [Berechtigungs- oder Push-Voranfrage]({{site.baseurl}}/user_guide/channels/push/best_practices) zu senden und zu akzeptieren?
- Haben Sie eine Option zum Schließen der Nachricht? Falls nicht, können Sie jederzeit dieses Snippet kopieren und einfügen, um einen schnellen Button zu erstellen:
  ```html
  <a href="appboy://close">X</a>
  ```

## Überlegungen zum Drag-and-Drop-Editor {#drag-and-drop-editor-considerations}

### Deeplinks für verschiedene Geräte hinzufügen {#adding-deep-links-for-different-devices}

Der Drag-and-Drop-Editor unterstützt das Hinzufügen unterschiedlicher Deeplinks für verschiedene Geräte nicht (im Gegensatz zum traditionellen Editor).

### Hintergrundbilddeckkraft anpassen {#adjusting-background-image-opacity}

Die Deckkrafteinstellung erlaubt keine vollständige Transparenz von Hintergrundbildern (im Gegensatz zum traditionellen IAM-Editor). Sie können die Deckkrafteinstellungen verwenden, um die Hintergrundfarbe der Nachricht vollständig transparent zu machen.

### Maximale Breite festlegen {#setting-the-maximum-width}

Die maximale Breite im Drag-and-Drop-Editor ist auf 325 px begrenzt; dies dient in erster Linie der Anpassung an die Dashboard-Vorschau. Nachrichten können auf Geräten mit kleinerem Bildschirm korrekt angezeigt werden.

### Verschiedene Hintergründe für verschiedene Plattformen auswählen {#selecting-different-backgrounds-for-different-platforms}

Es ist nicht möglich, zwei verschiedene Hintergründe für dieselbe Nachricht auf verschiedenen Plattformen (z. B. Internet und Mobilgerät) anzuzeigen.

### Nachrichtenstile anwenden {#applying-message-styles}

Hintergrundbilder gelten für die gesamte Nachricht und können nicht pro Seite angepasst werden. Nachrichtenstile gelten für die gesamte Nachricht, nicht für einzelne Seiten.

### Höhe von Spacer-Blöcken messen {#measuring-spacer-blocks-height}

Die Maßeinheit für Spacer-Blöcke ist Pixel (px) und kann nicht geändert werden.

### Unterstützte Formate {#supported-formats}

Derzeit werden im Drag-and-Drop-Editor nur modale und Vollbild-In-App-Nachrichten unterstützt.

### An Größe und Seitenverhältnis anpassen {#adjusting-to-size-and-aspect-ratio}

Das Hintergrundbild dehnt die In-App-Nachricht, da sich das Modal an die Größe und das Seitenverhältnis des Hintergrundbildes anpasst; Sie können das Verhältnis bei Bedarf anpassen.

### Hintergrundbilder und Klickverhalten {#background-images-and-on-click-behavior}

Diese bleiben seitenübergreifend bestehen. Fügen Sie bei mehrseitigen In-App-Nachrichten mit unterschiedlichen Vollbildern auf jeder Seite einen Button hinzu, damit Nutzer:innen zur nächsten Seite klicken können.