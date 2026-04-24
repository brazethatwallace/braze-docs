---
nav_title: Erste Schritte
article_title: Erste Schritte mit Braze Pilot
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt kurz die Integrationsschritte, die von Ihren Entwickler:innen durchgeführt werden müssen."
---

# Erste Schritte mit Braze Pilot

> Dieser Artikel beschreibt, wie Sie mit Braze Pilot loslegen. Wir führen Sie durch den Download der App, die Initialisierung der Verbindung mit Ihrem Braze-Dashboard und den Abschluss der Einrichtung.

## 1. Schritt: Braze Pilot herunterladen

Um Braze Pilot nutzen zu können, müssen Sie zunächst die App aus dem Apple App Store oder dem Google Play Store herunterladen. Sie können im App Store nach der App suchen oder die untenstehenden QR-Codes scannen, um die App-Seite für Ihr Gerät aufzurufen.

## 2. Schritt: Allgemeine Geschäftsbedingungen akzeptieren

Akzeptieren Sie anschließend die Allgemeinen Geschäftsbedingungen und geben Sie Ihre geschäftliche E-Mail-Adresse in das Formular ein. Ihre E-Mail-Adresse wird ausschließlich für Analytics zur App-Nutzung verwendet und nicht für Marketingzwecke eingesetzt.

![Willkommensseite von Braze Pilot.]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"} ![Option zur Eingabe Ihrer geschäftlichen E-Mail-Adresse.]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## 3. Schritt: Verbindung mit dem Braze SDK initialisieren

Mit Braze Pilot können Sie das Braze SDK für jedes beliebige Braze-Dashboard initialisieren. Sobald das SDK initialisiert ist, beginnt Pilot mit der Übermittlung von Engagement-Daten an Braze und ermöglicht es Ihnen, alle Nachrichten zu triggern, die über dieses Braze-Dashboard gestartet werden.

Es gibt zwei Methoden zur Konfiguration der SDK-Verbindung in Pilot: Demo-QR-Codes und den Einrichtungsassistenten.

{% tabs local %}
{% tab Demo QR codes %}

### Methode 1: Demo-QR-Codes

Scannen Sie einen QR-Code, der alle erforderlichen Details zur Initialisierung des SDK enthält, Ihr Nutzerprofil erstellt und Sie per Deeplink zu einer bestimmten App-Simulation in Braze Pilot weiterleitet. Demo-QR-Codes werden in der Begleitleiste für bestimmte Demo-Kampagnen in Ihrer kostenlosen Demo angezeigt.

| Pilot für Android | Pilot für iOS |
| --- | --- |
| ![QR-Code für Android.]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | ![QR-Code für iOS.]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Setup wizard %}

### Methode 2: Einrichtungsassistent

Folgen Sie der Schritt-für-Schritt-Anleitung zur Initialisierung der Verbindung mit Ihrem Dashboard-Workspace auf der Seite **App-Einstellungen** in Ihrem Braze-Dashboard.

![Schritt 1 des Einrichtungsassistenten für Braze Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Diese Verbindung ist Workspace-spezifisch. Das bedeutet: Wenn Sie die Verbindung vom Demo-Workspace aus initialisieren und dann in Ihrem Dashboard der kostenlosen Demo zum Live-Workspace wechseln, müssen Sie das SDK von diesem Workspace aus neu initialisieren, um dort gestartete Kampagnen empfangen zu können.

![Das Workspace-Dropdown-Menü im Braze-Dashboard mit „Demo – Braze“ als ausgewähltem aktiven Workspace.]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## 4. Schritt: Push-Berechtigungen erteilen

Abschließend empfehlen wir, der App die Berechtigung zum Senden von Push-Benachrichtigungen zu erteilen, wenn Sie die Push-Funktionen über die App testen möchten. Sie können der App diese Berechtigungen auf folgende Weise erteilen: über die Einstellungen der App in Ihren Geräteeinstellungen oder durch das Starten einer Push-Primer-Nachricht von Braze an die App.

{% tabs local %}
{% tab Update the settings for the app %}

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
{% tab Launch a push primer message %}

Sie können eine Braze-In-App-Nachricht verwenden, um Push-Berechtigungen für die App anzufordern – genau wie Sie es für Ihre eigenen Verbraucher:innen tun würden. Informationen zum Erstellen dieser Art von Nachricht in Braze finden Sie unter [Push-Primer-In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages#push-primer-in-app-messages).

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## 5. Schritt: Braze Messaging in Pilot erleben

Jetzt sind Sie bereit, als Nutzer:in von Braze Pilot Kampagnen und Canvases über Ihr Braze-Dashboard zu empfangen! Besuchen Sie eine der gestarteten Kampagnen in Ihrem Demo-Workspace, um eine kurze Demonstration der Braze-Anwendungsfälle zu erhalten, und wechseln Sie dann zu Ihrem Live-Workspace, um mit dem Versand Ihrer eigenen Kampagnen zu beginnen.

Weitere Informationen zum Einrichten von Kampagnen und Canvases in Braze finden Sie unter [Erste Schritte: Kampagnen und Canvases]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases/).
