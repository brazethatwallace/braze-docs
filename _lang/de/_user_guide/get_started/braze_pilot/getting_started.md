---
nav_title: Erste Schritte
article_title: Erste Schritte mit Braze Pilot
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt kurz die Integrationsschritte, die von Ihren Entwickler:innen durchgeführt werden müssen."
---

# Erste Schritte mit Braze Pilot {#get-started-with-braze-pilot}

> Dieser Artikel beschreibt, wie Sie mit Braze Pilot loslegen. Wir führen Sie durch den Download der App, die Initialisierung der Verbindung mit Ihrem Braze-Dashboard und den Abschluss der Einrichtung.

## Schritt 1: Braze Pilot herunterladen {#step-1-download-braze-pilot}

Um Braze Pilot nutzen zu können, müssen Sie zunächst die App aus dem Apple App Store oder dem Google Play Store herunterladen. Sie können im App Store nach der App suchen oder die QR-Codes im folgenden Abschnitt scannen, um die App-Seite für Ihr Gerät aufzurufen.

## Schritt 2: Allgemeine Geschäftsbedingungen akzeptieren {#step-2-accept-the-terms-and-conditions}

Akzeptieren Sie anschließend die Allgemeinen Geschäftsbedingungen und geben Sie Ihre geschäftliche E-Mail-Adresse in das Formular ein. Ihre E-Mail-Adresse wird ausschließlich für Analytics zur App-Nutzung verwendet und nicht für Marketingzwecke eingesetzt.

![Willkommensseite von Braze Pilot.]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"} ![Option zur Eingabe Ihrer geschäftlichen E-Mail-Adresse.]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## Schritt 3: Verbindung mit dem Braze SDK initialisieren {#step-3-initialize-the-connection-with-the-braze-sdk}

Mit Braze Pilot können Sie das Braze SDK für jedes beliebige Braze-Dashboard initialisieren. Sobald das SDK initialisiert ist, beginnt Pilot mit der Übermittlung von Engagement-Daten an Braze und ermöglicht es Ihnen, alle Nachrichten zu triggern, die über dieses Braze-Dashboard gestartet werden.

Es gibt zwei Methoden zur Konfiguration der SDK-Verbindung in Pilot: Demo-QR-Codes und den Einrichtungsassistenten.

{% tabs local %}
{% tab Demo-QR-Codes %}

### Methode 1: Demo-QR-Codes {#method-1-demo-qr-codes}

Scannen Sie einen QR-Code, der alle erforderlichen Details zur Initialisierung des SDK enthält, Ihr Kundenprofil erstellt und Sie per Deeplink zu einer bestimmten App-Simulation in Braze Pilot weiterleitet. Demo-QR-Codes werden in der Begleitleiste für bestimmte Demo-Kampagnen in Ihrer kostenlosen Demo angezeigt.

| Pilot für Android | Pilot für iOS |
| --- | --- |
| ![QR-Code für Android.]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | ![QR-Code für iOS.]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Methode 1: Demo-QR-Codes" }

{% endtab %}
{% tab Einrichtungsassistent %}

### Methode 2: Einrichtungsassistent {#method-2-setup-wizard}

Folgen Sie der Schritt-für-Schritt-Anleitung zur Initialisierung der Verbindung mit Ihrem Dashboard-Workspace auf der Seite **App Settings** in Ihrem Braze-Dashboard.

![Schritt 1 des Einrichtungsassistenten für Braze Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Diese Verbindung ist Workspace-spezifisch. Das bedeutet: Wenn Sie die Verbindung vom Demo-Workspace aus initialisieren und dann in Ihrem Dashboard der kostenlosen Demo zum Live-Workspace wechseln, müssen Sie das SDK von diesem Workspace aus neu initialisieren, um dort gestartete Kampagnen empfangen zu können.

![Das Workspace-Dropdown-Menü im Braze-Dashboard mit „Demo – Braze“ als ausgewähltem aktiven Workspace.]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## Schritt 4: Push-Berechtigungen erteilen {#step-4-allow-push-permissions}

Abschließend empfehlen wir, der App die Berechtigung zum Senden von Push-Benachrichtigungen zu erteilen, wenn Sie die Push-Funktionen über die App testen möchten. Sie können der App diese Berechtigungen auf folgende Weise erteilen: über die Einstellungen der App in Ihren Geräteeinstellungen oder durch das Starten einer Push-Primer-Nachricht von Braze an die App.

{% tabs local %}
{% tab Einstellungen der App aktualisieren %}

Öffnen Sie Ihre Geräteeinstellungen und suchen Sie nach Braze Pilot. Aktualisieren Sie anschließend die Einstellungen, damit Benachrichtigungen auf Ihrem Sperrbildschirm angezeigt werden.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/device_settings.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Push-Primer-Nachricht starten %}

Sie können eine Braze-In-App-Nachricht verwenden, um Push-Berechtigungen für die App anzufordern – genau wie Sie es für Ihre eigenen Verbraucher:innen tun würden. Informationen zum Erstellen dieser Art von Nachricht in Braze finden Sie unter [Push-Primer-In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Schritt 5: Braze-Messaging in Pilot erleben {#step-5-experience-braze-messaging-in-pilot}

Jetzt sind Sie bereit, als Nutzer:in von Braze Pilot Campaigns und Canvases über Ihr Braze-Dashboard zu empfangen! Besuchen Sie eine der gestarteten Kampagnen in Ihrem Demo-Workspace, um eine kurze Demonstration der Braze-Anwendungsfälle zu erhalten, und wechseln Sie dann zu Ihrem Live-Workspace, um mit dem Versand Ihrer eigenen Nachrichten zu beginnen.

Weitere Informationen zum Einrichten von Campaigns und Canvases in Braze finden Sie unter [Erste Schritte: Campaigns und Canvases]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases).