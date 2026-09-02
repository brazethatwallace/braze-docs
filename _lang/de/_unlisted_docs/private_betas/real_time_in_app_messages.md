---
nav_title: Realtime-Zustellung von In-App-Nachrichten
article_title: Realtime-Zustellung von In-App-Nachrichten
permalink: "/real_time_in_app_messages/"
description: "Diese Seite behandelt den Early Access für die Realtime-Zustellung von In-App-Nachrichten, die In-App-Nachrichten an ein Gerät sendet, sobald Nutzer:innen berechtigt werden, anstatt auf den nächsten Sitzungsstart zu warten."
page_type: reference
hidden: true
noindex: true
---

# Realtime-Zustellung von In-App-Nachrichten {#real-time-in-app-message-delivery}

> Mit der Realtime-Zustellung sendet Braze eine In-App-Nachricht an das Gerät, sobald Nutzer:innen dafür berechtigt werden. Nutzer:innen müssen nicht mehr eine neue Sitzung starten, um eine In-App-Nachricht zu erhalten, für die sie während einer laufenden Sitzung berechtigt wurden.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Real-time in-app message delivery' type='early_access' %}

## Funktionsweise {#how-it-works}

Ohne Realtime-Zustellung fordert das SDK or Software-Development-Kit berechtigte In-App-Nachrichten beim Sitzungsstart an und speichert sie auf dem Gerät im Cache. Nutzer:innen, die während einer Sitzung berechtigt werden, erhalten die Nachricht erst beim nächsten Sitzungsstart. Weitere Informationen zu diesem Verhalten finden Sie unter [In-App-Nachrichten Trigger or triggern or triggern]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages).

Mit der Realtime-Zustellung überträgt Braze die Nachricht über eine Live-Verbindung an das Gerät, die das SDK or Software-Development-Kit während der Sitzung aufrechterhält. Braze sendet eine Nachricht in zwei Fällen:

- Nutzer:innen werden für eine In-App-Nachrichten-Campaign berechtigt.
- Nutzer:innen erreichen einen In-App-Nachrichten-Schritt in einem Canvas.

Die Realtime-Zustellung ändert, wann eine Nachricht das Gerät erreicht. Das Anzeigeverhalten bleibt gleich: Die Nachricht wartet auf ihr Trigger or triggern-Ereignis, bevor sie erscheint.

### Was das für Ihre Campaigns bedeutet {#what-this-means-for-your-campaigns}

| Szenario | Ohne Realtime-Zustellung | Mit Realtime-Zustellung |
| --- | --- | --- |
| Nutzer:innen werden während einer Sitzung für eine In-App-Nachrichten-Campaign berechtigt | Die Nachricht kommt beim nächsten Sitzungsstart an | Die Nachricht kommt während der aktuellen Sitzung an |
| Nutzer:innen erreichen einen In-App-Nachrichten-Schritt in einem Canvas während einer Sitzung | Die Nachricht kommt beim nächsten Sitzungsstart an | Die Nachricht kommt während der aktuellen Sitzung an |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Vergleich der Realtime-Zustellung von In-App-Nachrichten" }

## SDK or Software-Development-Kit-Anforderungen {#sdk-requirements}

Die Realtime-Zustellung erfordert die folgenden Mindest-SDK or Software-Development-Kit-Versionen:

{% sdk_min_versions swift:18.0.0 android:43.1.1 %}

Geräte erhalten unabhängig von der SDK or Software-Development-Kit-Version weiterhin In-App-Nachrichten beim Sitzungsstart.

## Aktuelle Einschränkungen {#current-limitations}

- **Das Web-SDK or Software-Development-Kit wird noch nicht unterstützt:** Die Realtime-Zustellung ist während des Early Access für die Swift- und Android-SDKs verfügbar.
- **Änderungen an einer laufenden Campaign werden beim nächsten Sitzungsstart übernommen:** Wenn Sie eine In-App-Nachricht ändern, die ein Gerät bereits erhalten hat, behält dieses Gerät die vorhandene Version bis zum nächsten Sitzungsstart.

## Am Early Access teilnehmen {#participate-in-early-access}

1. Kontaktieren Sie Ihren Braze Account Manager:in, um Ihren Workspace zum Early Access hinzufügen zu lassen.
2. Update or aktualisieren or aktualisieren Sie Ihre App auf die Mindest-SDK or Software-Development-Kit-Version für Ihre Plattform.
3. Veröffentlichen Sie die aktualisierte App für Ihre Nutzer:innen.

Die Realtime-Zustellung erfordert keine Dashboard-Konfiguration, keine Campaign-Änderungen und keine SDK or Software-Development-Kit-Code-Änderungen. Nachdem Ihr Workspace zum Early Access hinzugefügt wurde, gilt die Realtime-Zustellung für Ihre bestehenden In-App-Nachrichten-Campaigns und Canvase.

## Feedback teilen {#share-feedback}

Braze entwickelt dieses Feature aktiv weiter, und Ihr Feedback beeinflusst, was bei der allgemeinen Verfügbarkeit veröffentlicht wird. Teilen Sie Ihrem Account Manager:in Ihre Beobachtungen zur Zustellzeit mit, alles, was sich anders verhalten hat als erwartet, und die Szenarien, die die Realtime-Zustellung als Nächstes abdecken soll.