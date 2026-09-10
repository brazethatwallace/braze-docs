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

## So funktioniert es {#how-it-works}

Ohne Realtime-Zustellung fordert das SDK berechtigte In-App-Nachrichten beim Sitzungsstart an und speichert sie auf dem Gerät zwischen. Nutzer:innen, die während einer Sitzung berechtigt werden, erhalten die Nachricht erst, wenn ihre nächste Sitzung beginnt. Weitere Informationen zu diesem Verhalten finden Sie unter [In-App-Nachrichten triggern]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages).

Mit Realtime-Zustellung überträgt Braze die Nachricht über eine Live-Verbindung an das Gerät, die das SDK während der Sitzung aufrechterhält. Braze sendet eine Nachricht in zwei Fällen:

- Nutzer:innen werden für eine In-App-Nachrichten-Campaign berechtigt.
- Nutzer:innen gelangen zu einem In-App-Nachrichten-Schritt in einem Canvas.

Realtime-Zustellung ändert, wann eine Nachricht das Gerät erreicht. Das Anzeigeverhalten bleibt gleich: Die Nachricht wartet auf ihr Trigger-Ereignis, bevor sie erscheint.

### Was das für Ihre Campaigns bedeutet {#what-this-means-for-your-campaigns}

| Szenario | Ohne Realtime-Zustellung | Mit Realtime-Zustellung |
| --- | --- | --- |
| Nutzer:innen werden während einer Sitzung für eine In-App-Nachrichten-Campaign berechtigt | Die Nachricht kommt beim nächsten Sitzungsstart an | Die Nachricht kommt während der aktuellen Sitzung an |
| Nutzer:innen erreichen während einer Sitzung einen In-App-Nachrichten-Schritt in einem Canvas | Die Nachricht kommt beim nächsten Sitzungsstart an | Die Nachricht kommt während der aktuellen Sitzung an |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Vergleich der Realtime-Zustellung von In-App-Nachrichten" }

## SDK-Anforderungen {#sdk-requirements}

Für die Realtime-Zustellung sind die folgenden Mindest-SDK-Versionen erforderlich:

{% sdk_min_versions swift:18.0.0 android:43.1.1 web:6.12.0 %}

Geräte erhalten weiterhin In-App-Nachrichten beim Sitzungsstart, unabhängig von der SDK-Version.

## Aktuelle Einschränkungen {#current-limitations}

- **Änderungen an einer laufenden Campaign werden beim nächsten Sitzungsstart wirksam:** Wenn Sie eine In-App-Nachricht ändern, die ein Gerät bereits empfangen hat, behält dieses Gerät die vorhandene Version bei, bis die nächste Sitzung der Nutzer:innen beginnt.

## An Early Access teilnehmen {#participate-in-early-access}

1. Kontaktieren Sie Ihren Braze Account Manager, um Ihren Workspace zum Early Access hinzufügen zu lassen.
2. Führen Sie ein Upgrade Ihrer App auf die mindestens erforderliche SDK-Version für Ihre Plattform durch.
3. Veröffentlichen Sie die aktualisierte App für Ihre Nutzer:innen.

Realtime-Zustellung erfordert keine Dashboard-Konfiguration, keine Änderungen an Campaigns und keine Änderungen am SDK-Code. Nachdem Ihr Workspace zum Early Access hinzugefügt wurde, gilt die Realtime-Zustellung für Ihre bestehenden In-App-Nachrichten-Campaigns und Canvases.

## Feedback teilen {#share-feedback}

Braze entwickelt dieses Feature aktiv weiter, und Ihr Feedback beeinflusst, was bei der allgemeinen Verfügbarkeit ausgeliefert wird. Senden Sie Ihrem Account Manager Ihre Beobachtungen zur Zustellungszeit, alles, was sich anders verhalten hat als erwartet, und die Szenarien, die Realtime-Zustellung als Nächstes abdecken soll.