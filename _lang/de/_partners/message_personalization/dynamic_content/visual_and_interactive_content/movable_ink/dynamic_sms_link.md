---
nav_title: Dynamische SMS-Link-Vorschau
article_title: Dynamische SMS-Link-Vorschau
description: "Dieser Referenzartikel beschreibt, wie Sie das Feature der SMS-Link-Vorschau von Movable Ink aktivieren und nutzen können."
page_type: partner
search_tag: Partner
---

# Dynamische SMS-Link-Vorschau {#dynamic-sms-link-preview}

> Mit der dynamischen SMS-Link-Vorschau von Movable Ink können Sie die Unmittelbarkeit von MMS zu den gleichen Kosten wie bei SMS nutzen. Dies erlaubt es Ihnen, mit Braze und Movable Ink kostengünstige, personalisierte Messaging-Erlebnisse zu liefern.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Movable Ink-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Movable Ink-Konto. |
| Datenquelle | Sie müssen eine Datenquelle mit Movable Ink verbinden. Dies kann über CSV, Website-Import oder API geschehen. |
| MMS-Versandmöglichkeiten | Bestätigen Sie, dass Sie für MMS über Braze eingerichtet sind. |
| [Link-Verkürzung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) | Vergewissern Sie sich, dass die Link-Verkürzung aktiviert ist. |
| Kontaktkarte | Ihre Marke (der Sender) muss als Kontakt auf dem Telefon der Nutzer:innen gespeichert sein, damit die Link-Vorschau unter iOS funktioniert. Dies kann mit einer Kontaktkarte oder einer anderen Methode geschehen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Folgen Sie den jeweiligen Schritten in diesem Abschnitt, um dynamische SMS-Links für iOS- und Android-Betriebssysteme zu versenden.

### iOS

{% alert important %}
Um Link-Vorschaubilder für iOS zu ermöglichen, müssen Nutzer:innen Ihre Marke (den Sender) als Kontakt hinzufügen.
{% endalert %}

#### Schritt 1: Erstellen Sie eine Kontaktkarten-Campaign {#step-1-create-a-contact-card-campaign}

Nachdem Nutzer:innen Ihre Marke als Kontakt gespeichert haben, entweder über eine [Kontaktkarte]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card) oder eine andere Methode, können sie die Aufforderungen **Tap to Load Preview** und Movable Ink-Links sehen.

![Ein iOS-Gerät zeigt die Aufforderung „Tap to Load Preview“ für eine SMS-Link-Vorschau an][1]{: style="max-width:30%;"}

#### Schritt 2: Movable Ink-Links versenden {#step-2-send-movable-ink-links}

1. Erstellen Sie eine SMS-Campaign in Movable Ink und generieren Sie Ihre Klick, der-through-URL.
2. Gehen Sie im Braze-Dashboard zu **Campaigns** und richten Sie eine neue SMS/MMS-Campaign über das Dropdown-Menü **Campaign erstellen** ein.
3. Im SMS-Campaign-Composer:
    - Legen Sie Ihre Abo-Gruppe fest.
    - Geben Sie Ihre Nachricht ein.
    - Fügen Sie Ihren Movable Ink-Link **als Letztes** ein, nach allen anderen Texten im Nachrichtentext. <br><br>![Der SMS-Campaign-Composer mit einem Movable Ink-Link am Ende des Nachrichtentexts][2]{: style="max-width:50%;"}

{% alert tip %}
Sehen Sie sich [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) an, um Ihr Wissen zur Liquid-Personalisierung aufzufrischen.
{% endalert %}

{: start="4"}
4. Jetzt können Sie Ihre dynamische SMS-Link-Vorschau-Campaign testen und starten.

![Vorschau und Testoptionen für eine dynamische SMS-Link-Vorschau-Campaign][3]{: style="max-width:70%;"}

Nachdem Nutzer:innen die Link-Vorschau geladen haben, wird ein personalisiertes Bild gerendert, mit der Möglichkeit, auf Ihre Website, App oder Landing-Page zu verlinken.

![Ein iOS-Gerät zeigt ein personalisiertes Vorschaubild mit einem Link zu einer Website][4]{: style="max-width:30%;"}

### Android (Google- und Samsung-Geräte) {#android-google-and-samsung-devices}

Android-Nutzer:innen müssen Ihre Marke nicht als Kontakt speichern, um dynamische SMS-Link-Vorschauen zu erhalten. Es ist aber dennoch empfehlenswert, damit das Gerät die Link-Vorschauen automatisch laden kann.

![Ein Android-Gerät zeigt eine automatisch geladene SMS-Link-Vorschau an][5]{: style="max-width:30%;"}

Nutzer:innen, die Ihre Marke nicht als Kontakt gespeichert und die automatische Vorschau aktiviert haben, müssen **Tap to load preview** auswählen, um das Vorschaubild zu laden.

![Ein Android-Gerät zeigt die Aufforderung „Tap to load preview“ für eine SMS-Link-Vorschau an][6]{: style="max-width:30%;"}

## Hinweise {#considerations}

- Fügen Sie nur einen Vorschau-Link in Ihre Nachricht ein. Bei mehreren Links in Ihrem SMS-Text werden keine Inhalte generiert.
- Fügen Sie keine Zeichen nach Ihrem Vorschau-Link ein, da sonst das Erlebnis beeinträchtigt werden könnte.


[1]: {% image_buster /assets/img/movable_ink/ios_link.png %}
[2]: {% image_buster /assets/img/movable_ink/ios_message.png %}
[3]: {% image_buster /assets/img/movable_ink/ios_test_launch.png %}
[4]: {% image_buster /assets/img/movable_ink/ios_example.png %}
[5]: {% image_buster /assets/img/movable_ink/android_automatic.png %}
[6]: {% image_buster /assets/img/movable_ink/android_tap.png %}