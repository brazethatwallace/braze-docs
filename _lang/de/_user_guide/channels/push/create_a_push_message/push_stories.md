---
nav_title: "Push-Storys"
article_title: "Push-Storys"
page_order: 2
page_type: reference
description: "Dieser Referenzartikel behandelt, was Push-Storys sind, wie Sie eine erstellen und beantwortet einige häufig gestellte Fragen."
channel:
  - push

---

# Push-Storys {#push-stories}

> Push-Storys nutzen die von Instagram und Facebook bekannte Fotokarussell-Funktion und ermöglichen es Marketern, ein Karussell aus Seiten innerhalb einer Push-Benachrichtigung zu erstellen, das eine reichhaltige, zusammenhängende Geschichte erzählt. Diese Seiten bestehen aus einem Bild, einer Klickaktion, einem Titel und einer Beschreibung. Ihre Nutzer:innen können durch diese Seiten wischen und die von Ihnen erzählte Geschichte ansehen.

| Android-Beispiel (erweitert) | iOS-Beispiel (erweitert) |
| :-----: | :----------: |
| ![Vorschau von Push-Storys auf Android.]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | ![Vorschau von Push-Storys auf iOS]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push-Storys" }

{% alert note %}
Ab iOS SDK Version 3.13.0+ wird aufgrund einer Änderung beim Herunterladen von Bildern durch das SDK kein Miniaturbild des ersten Bildes mehr in der komprimierten Ansicht der Push-Benachrichtigung angezeigt. Stellen Sie sicher, dass Ihr Nachrichtentext die Nutzer:innen dazu auffordert, die Push-Benachrichtigung zu erweitern, um die Bilder zu sehen.
{% endalert %}

## Voraussetzungen {#prerequisites}

Die folgenden SDK-Versionen sind erforderlich, um Push-Storys zu empfangen:

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## So verwenden Sie Push-Storys {#how-to-use-push-stories}

![Dropdown-Menü im Push-Story-Composer]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Um Push-Storys zu verwenden, gehen Sie wie folgt vor:

1. Erstellen Sie eine [Push-Campaign]({{site.baseurl}}/user_guide/channels/push/create_a_push_message).
2. Wählen Sie als **Notification Type** die Option **Push Stories** aus.
3. Wählen Sie **iOS** oder **Android**. Beachten Sie, dass die Option zum Erstellen einer Push-Story nicht angezeigt wird, wenn Sie beide für eine Push-Nachricht auswählen.

### Push-Story-Composer {#push-story-composer}

Um eine Seite zu erstellen, führen Sie die folgenden Schritte aus:

1. Klicken Sie im Haupt-Composer auf **Add new page**.
2. Fügen Sie für jede Seite ein Bild sowie das Klickverhalten für dieses Bild ein.
3. Fügen Sie bei Bedarf einen **Title** und eine **Description** für jede Seite hinzu. Wenn Sie einen Titel und eine Beschreibung für eine Seite verwenden, müssen diese für alle Seiten eingefügt werden.

Die Vorschauen werden widergespiegelt und sind interaktiv.

![Push-Story-Composer]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
Wenn Sie Bilder mit [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) einbinden, stellen Sie sicher, dass Ihre Bild-URL mit `https://` beginnt. Die Verwendung von `http://` führt zum Absturz Ihrer App.
{% endalert %}

### Bild- und Textspezifikationen {#image-and-text-specifications}

Die folgenden Bild- und Textspezifikationen gelten für den Fotokarussell-Teil von Push-Storys. Informationen zur grundlegenden Push-Benachrichtigung, mit der Nutzer:innen interagieren, um die Push-Story zu aktivieren, finden Sie unter [Push-Nachrichten- und Bildformate]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats).

{% tabs %}
{% tab Bilder %}

- **Bildverhältnis:** 2:1 (erforderlich)
- **Empfohlene Bildgröße:** 500 KB
- **Maximale Bildgröße:** 5 MB
- **Dateitypen:** PNG, JPEG

{% endtab %}
{% tab Text %}

- **Titel:** 30 Zeichen (empfohlen)
- **Beschreibung:** 30 Zeichen (empfohlen)

{% alert note %}
Obwohl die Zeichenlänge von Gerät zu Gerät variieren kann, sind der Titel und die Beschreibung für Push-Storys jeweils auf eine Zeile begrenzt. Der Rest Ihrer Nachricht wird abgeschnitten. Testen Sie Ihre Nachricht immer auf einem echten Gerät.
{% endalert %}

{% endtab %}
{% endtabs %}

### Push-Story-Segmentierung {#push-story-segmentation}

Wenn Sie eine Campaign oder ein Canvas erstellen, können Sie filtern, welche Nutzer:innen Sie ansprechen möchten, basierend darauf, ob sie auf eine Push-Story-Seite geklickt haben. Wählen Sie dann die Campaign und die Seite aus, die Sie verwenden möchten, um Ihre Nutzer:innen anzusprechen.

### Push-Story-Analytics {#push-stories-analytics}

Die Analytics sehen dem aktuellen Analytics-Bereich für Push-Benachrichtigungen sehr ähnlich. Für Push-Story-Analytics können Sie die Metrik **Direct Opens** aufklappen, um die Klicks pro Seite anzuzeigen.

![iOS-Push-Performance-Tabelle mit Beispiel-Analytics und erweiterten Details für die Metrik „Direct Opens“.]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## Fehlerbehebung {#troubleshooting}

### iOS

#### Ich habe mir selbst eine Push-Story gesendet, aber keine Benachrichtigung erhalten {#i-sent-myself-a-push-story-but-didnt-receive-the-notification}

Apple hat bestimmte Regeln, die verhindern, dass bestimmte Arten von Benachrichtigungen basierend auf verschiedenen Faktoren an ein Gerät gesendet werden. Dazu gehört die Bewertung des Datentarifs der Kund:innen, der Benachrichtigungsgröße und der Speicherkapazität der Kund:innen. Infolgedessen wird manchmal keine Benachrichtigung an Ihre Kund:innen gesendet.

Dies sind von Apple auferlegte Einschränkungen, die beim Entwerfen Ihrer Push-Story berücksichtigt werden sollten.

#### Ich habe mir selbst eine Push-Story gesendet, aber nur die komprimierte Ansicht gesehen {#i-sent-myself-a-push-story-but-saw-the-condensed-view-instead}

In bestimmten Situationen, in denen nicht alle Seiten geladen werden, z. B. aufgrund eines Verlusts der Datenverbindung, zeigt die Push-Story nur die komprimierte Benachrichtigung an.

### Android

#### Push-Story wird nach dem Klicken auf das Bild nicht geschlossen {#push-story-doesnt-dismiss-after-clicking-the-image}

Standardmäßig werden Push-Storys auf Android nach dem Klicken auf das Bild nicht geschlossen. Wenn Sie die Benachrichtigung schließen möchten, rufen Sie [`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721) auf.