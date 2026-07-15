---
nav_title: Rich-Benachrichtigungen erstellen
article_title: "Rich-Push-Benachrichtigungen für Android erstellen"
page_order: 3
page_layout: tutorial
description: "Dieses Tutorial behandelt die Einrichtung von Android-Rich-Benachrichtigungen für Ihre Braze Campaigns."
platform: Android
channel:
  - Push
tool:
  - Campaigns

---

# Rich-Push-Benachrichtigungen für Android erstellen {#create-rich-push-notifications-for-android}

> Rich-Benachrichtigungen ermöglichen eine stärkere Anpassung Ihrer Push-Benachrichtigungen, indem zusätzliche Inhalte über reinen Text hinaus hinzugefügt werden. Android-Benachrichtigungen unterstützen bereits seit einiger Zeit Bilder in Push-Benachrichtigungen – diese werden als „erweitertes Benachrichtigungsbild“ bezeichnet.

## Voraussetzungen {#prerequisites}

Bevor Sie eine Rich-Push-Benachrichtigung für Android erstellen, beachten Sie die folgenden Details:

- Erweiterte Android-Benachrichtigungsbilder müssen ein Seitenverhältnis von 2:1 haben, es gibt jedoch keine Größenbeschränkung.
- Android ermöglicht außerdem die Festlegung eines separaten Bildes für die Standard-Benachrichtigungsansicht. Die empfohlenen Bildgrößen sind:
  - **Klein:** 512x256
  - **Mittel:** 1024x512
  - **Groß:** 2048x1024
- Derzeit unterstützen Android-Rich-Benachrichtigungen nur statische Bilder, einschließlich der Bildformate JPEG und PNG. GIF und andere Bildformate werden noch nicht unterstützt.
- Das Hinzufügen von Aktions-Buttons zu Ihrer Push-Benachrichtigung kann den anzeigbaren Bereich des Bildes beeinflussen. Testen Sie mit der Dashboard-Vorschau und auf echten Geräten, um sicherzustellen, dass die Ergebnisse wie erwartet ausfallen.
- Das Braze Android SDK muss aktiviert sein, damit das Bild gerendert wird.

{% alert note %}
Braze stellt zwar Anleitungen zur Einrichtung von Rich-Push-Benachrichtigungen bereit, das tatsächliche Rendering kann jedoch je nach externen Faktoren wie Seitenverhältnis des Geräts, Android-Version, OEM-spezifischen Einschränkungen und anderen variieren. Wir empfehlen, einen Testversand an mehrere Android-Geräte durchzuführen, um sicherzustellen, dass Ihre Rich-Push-Benachrichtigungen wie beabsichtigt angezeigt werden.
{% endalert %}

## Einrichten Ihrer Android-Rich-Benachrichtigung {#setting-up-your-android-rich-notification}

### Schritt 1: Push-Campaign erstellen {#step-1-create-a-push-campaign}

Folgen Sie den Schritten zum [Erstellen einer Campaign]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#create-a-push-message), um eine Push-Benachrichtigung für Android zu verfassen. Sie verwenden denselben Composer für die Einrichtung von Push-Benachrichtigungen, die keinen Rich-Inhalt enthalten.

### Schritt 2: Beschriftung hinzufügen {#step-2-add-captioning}

Fügen Sie den **Summary Text** hinzu, der vor dem Bild in der Benachrichtigung angezeigt werden soll.

![Eine Rich-Push-Benachrichtigung von einer Tierfutter-App namens „Dog“, die darauf hinweist, dass es Zeit ist, mehr Futter für Spot zu bestellen, mit Zusammenfassungstext.]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### Schritt 3: Medien hinzufügen {#step-3-add-media}

Fügen Sie Ihr Bild im Feld **Android Notification Image** im Composer der Nachricht hinzu. Bilder können direkt über das Dashboard hochgeladen oder durch Angabe einer Content-URL, die an anderer Stelle gehostet wird, hinzugefügt werden.

Einzelheiten zu unterstützten Bildern finden Sie unter [Bildspezifikationen]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#image-specifications).

![Der Abschnitt „Android Notification Image“, in dem Sie ein Bild hinzufügen oder eine Bild-URL eingeben können.]({% image_buster /assets/img_archive/android_rich_image.png %})

### Schritt 4: Campaign weiter erstellen {#step-4-continue-creating-your-campaign}

Nachdem Ihr Rich-Benachrichtigungsinhalt in das Dashboard hochgeladen wurde, können Sie mit der [Planung Ihrer Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign) fortfahren.