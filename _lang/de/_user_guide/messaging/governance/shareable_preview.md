---
nav_title: Teilbare Vorschau
article_title: Nachrichtenvorschau mit Stakeholdern teilen
page_order: 5
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie einen Vorschau-Link für eine Nachricht oder einen Inhalt generieren und mit Stakeholdern teilen können, damit Beteiligte ohne Dashboard-Zugang den Inhalt vor dem Versand überprüfen können."
---

# Nachrichtenvorschau mit Stakeholdern teilen {#share-a-message-preview-with-stakeholders}

> Mit der teilbaren Vorschau können Sie einen Link zu einer Vorschau Ihrer Nachricht oder Ihres Inhalts generieren und ihn mit Prüfenden teilen – beispielsweise Stakeholdern, Rechtsabteilungen oder Compliance-Teams –, die keinen Zugang zu Ihrem Braze-Dashboard haben. Empfänger:innen können die Vorschau in ihrem Browser ansehen, ohne sich bei Braze anzumelden.

## Unterstützte Kanäle {#supported-channels}

Sie können einen teilbaren Vorschau-Link für die folgenden Kanäle und Inhaltstypen generieren:

- Banner
- Content Blocks
- Content Cards
- E-Mail und E-Mail-Fußzeile
- Landing-Pages
- LINE
- Push-Benachrichtigungen
- Abo-Seiten
- SMS und RCS
- WhatsApp

{% alert note %}
Die teilbare Vorschau wird schrittweise eingeführt und ist möglicherweise noch nicht für jeden Kanal in Ihrem Workspace verfügbar. Wenden Sie sich an Ihren Braze Account Manager:in, wenn Sie die Option für einen in diesem Abschnitt aufgeführten Kanal nicht sehen.
{% endalert %}

## So funktioniert die teilbare Vorschau {#how-shareable-preview-works}

Das folgende Verhalten gilt einheitlich für alle unterstützten Kanäle.

### Link generieren {#generating-a-link}

Wählen Sie beim Verfassen Ihrer Nachricht oder Ihres Inhalts **Copy preview link** aus, um einen teilbaren Link zu generieren. Braze kopiert den Link automatisch in Ihre Zwischenablage.

- Der Link öffnet einen statischen, schreibgeschützten Snapshot Ihrer Nachricht, wie sie zum Zeitpunkt der Link-Generierung aussah. Er wird nicht automatisch aktualisiert, wenn Sie weiter bearbeiten. Generieren Sie einen neuen Link, um Ihre neuesten Änderungen zu erfassen.
- Wenn Ihre Nachricht Personalisierung enthält – etwa Liquid oder Connected-Content, das gegen eine:n Testnutzer:in, ein angepasstes Kundenprofil oder eine:n zufällige:n Nutzer:in aufgelöst wird –, spiegelt die Vorschau dieselbe Personalisierung wider und entspricht dem, was Sie unter **Preview and Test** sehen.
- Durch Auswahl von **Regenerate link** wird ein neuer Snapshot mit einem eigenen neuen Ablaufdatum erstellt. Der vorherige Link wird dadurch nicht ungültig. Beide Links funktionieren unabhängig voneinander, bis sie jeweils ablaufen.

### Link anzeigen {#viewing-the-link}

Jede Person mit dem Link kann die Vorschau ansehen. Es ist keine Braze-Anmeldung und keine Dashboard-Berechtigung erforderlich.

{% alert important %}
Behandeln Sie einen Link wie jedes andere teilbare Dokument: Senden Sie ihn nur an Personen, die Zugang haben sollen, und vermeiden Sie es, ihn öffentlich zu posten.
{% endalert %}

### Link-Ablauf {#link-expiration}

- Jeder teilbare Vorschau-Link läuft sieben Tage nach seiner Generierung ab.
- Wenn ein Link abläuft, kann er nicht mehr geöffnet werden. Generieren Sie im Composer einen neuen Link, um einen aktuellen zu erhalten.
- Es gibt keine Möglichkeit, einen Link vor seinem Ablauf manuell zu widerrufen oder zu deaktivieren. Das erneute Generieren eines Links widerruft den vorherigen nicht; jeder Link läuft einfach nach seinem eigenen Sieben-Tage-Zeitplan ab.

## Kanalspezifische Besonderheiten {#per-channel-nuances}

Obwohl die grundlegende Funktionsweise überall gleich ist, gibt es bei einigen Kanälen kleine Unterschiede, die erwähnenswert sind.

{% alert note %}
Die teilbare Vorschau ist für In-App-Nachrichten nicht verfügbar.
{% endalert %}

| Kanal | Was ist anders |
|---|---|
| E-Mail | Die Vorschau enthält neben dem Nachrichtentext auch die Felder „An“, „Von“ und „Betreffzeile“. <br><br>Wenn Sie als angepasste:r Nutzer:in personalisieren, werden Werte, die als API-Trigger-Eigenschaften oder Event-Eigenschaften eingegeben wurden, möglicherweise nicht in der Vorschau angezeigt, obwohl sie unter **Preview and Test** korrekt dargestellt werden. Angepasste Attribute, Testnutzer:innen und zufällige Nutzer:innen sind davon nicht betroffen. |
| Banner (Drag-and-Drop-Editor) | Die Vorschau spiegelt den Inhalt zum Zeitpunkt wider, als Sie zuletzt den Tab **Vorschau** im Composer geöffnet haben, nicht unbedingt Ihre neuesten Bearbeitungen. <br><br>Öffnen Sie **Vorschau** erneut, bevor Sie einen Link generieren oder neu generieren, um sicherzustellen, dass er aktuell ist. |
| SMS und RCS | Beide unterliegen derselben Funktionalität für teilbare Vorschauen, generieren jedoch jeweils einen eigenen unabhängigen Link. |
| WhatsApp | Die teilbare Vorschau ist separat für WhatsApp-Template-Nachrichten und WhatsApp-Antwortnachrichten verfügbar. |
| Content Blocks, E-Mail-Fußzeilen und Abo-Seiten | Diese generieren eine Vorschau des eigenständigen Inhalts, unabhängig von einer bestimmten Campaign oder einem bestimmten Canvas, in dem er verwendet wird. |
| Landing-Pages | Die Vorschau verhält sich bei Landing-Pages anders als bei anderen Kanälen. Weitere Informationen finden Sie unter [Seite in der Vorschau anzeigen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-5-preview-the-page). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Kanalspezifische Besonderheiten" }

## Häufig gestellte Fragen {#frequently-asked-questions}

{% details Benötigen Empfänger:innen ein Braze-Konto, um die Vorschau anzuzeigen? %}
Nein. Jede Person mit dem Link kann die Vorschau in ihrem Browser ansehen, ohne sich anzumelden.
{% enddetails %}

{% details Wird die Vorschau aktualisiert, wenn ich meine Nachricht weiter bearbeite? %}
Nein. Ein teilbarer Vorschau-Link ist ein Snapshot zum Zeitpunkt seiner Erstellung. Wählen Sie **Regenerate link** aus, um Ihre neuesten Änderungen zu erfassen und einen neuen Link zu erhalten.
{% enddetails %}

{% details Wie lange bleibt der Link aktiv? %}
Sieben Tage ab dem Zeitpunkt der Generierung. Wenn Sie den Link neu generieren, erhält der neue Link ein eigenes Sieben-Tage-Ablaufdatum, unabhängig vom vorherigen.
{% enddetails %}

{% details Kann ich einen Link vorzeitig widerrufen? %}
Nein, Sie können einen Link nicht widerrufen. Das erneute Generieren des Links macht den vorherigen nicht ungültig. Alle Links funktionieren, bis sie nach sieben Tagen ablaufen.
{% enddetails %}