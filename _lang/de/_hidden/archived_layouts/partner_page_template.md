---
nav_title: Partnerseite

page_order: 4

#Required
description: "Dies ist die Beschreibung für die Google-Suche. Zeichen nach 160 werden abgeschnitten, fassen Sie sich kurz."
page_type: partner
tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks


noindex: true
#ATTENTION: remove noindex and this alert from template

---

# [Name des Partners] {#partner-name}

> Willkommen beim Template für die Partnerseite! Hier finden Sie alles, was Sie brauchen, um Ihre eigene Partnerseite zu erstellen. In diesem ersten Abschnitt sollten Sie den Partner im ersten Absatz in ein oder zwei Sätzen beschreiben. Fügen Sie außerdem einen Link zur Hauptseite des Partners hinzu.

Im zweiten Absatz sollten Sie die Beziehung zwischen Braze und diesem Partner untersuchen und erklären. Dieser Absatz sollte erläutern, wie Braze und dieser Partner zusammenarbeiten, um die Bindung zwischen Braze-Nutzer:innen und ihren Kund:innen zu stärken. Erklären Sie den Mehrwert, der entsteht, wenn Braze-Nutzer:innen diesen Partner und seine Dienste integrieren oder nutzen.

## Voraussetzungen {#requirements-or-prerequisites}

In diesem Abschnitt geht es darum, was Sie benötigen, um den Partner zu integrieren und seine Dienste zu nutzen. Am besten vermitteln Sie diese Informationen in einem kurzen Anleitungsabschnitt, der alle wichtigen, nicht-technischen Details beschreibt, die man wissen sollte – beispielsweise, ob Ihre Integration zusätzlichen Sicherheitsprüfungen oder Freigaben unterliegt. Anschließend sollten Sie die technischen Anforderungen der Integration in einer Tabelle darstellen.

{% alert important %}
Die folgenden Anforderungen sind typische Anforderungen, die Sie möglicherweise von Braze benötigen. Wir empfehlen, die angegebenen Titel, Herkunftsangaben, Links und Formulierungen wie in der folgenden Tabelle aufgeführt zu verwenden. Passen Sie die Beschreibung so an, dass klar ist, wofür die einzelnen Anforderungen verwendet werden.
{% endalert %}

| Anforderung | Herkunft | Zugang | Beschreibung |
|---|---|---|---|
| REST-API-Schlüssel des Braze-Workspace | Braze-Plattform | Seite **Einstellungen** > **API-Schlüssel** | Diese Beschreibung sollte erklären, was mit dem REST-API-Schlüssel des Workspace zu tun ist. |
| Braze-API-Endpunkt | Braze-Plattform | Sehen Sie sich unsere [aufgelisteten Endpunkte]({{site.baseurl}}/api/basics#endpoints) an oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support). | Beschreibung ausstehend. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Voraussetzungen" }

## [Art der Integration] Integration {#type-of-integration-integration}

Hier wird die Integration in einzelne Schritte unterteilt. Schreiben Sie keine endlosen Textabschnitte – dies sind technische Dokumente, die sowohl von Marketern als auch von Entwickler:innen genutzt werden, um die Integration einzurichten und in Betrieb zu nehmen. Ihr einziges Ziel in diesem Abschnitt ist es, eine beschreibende Dokumentation zu verfassen, die Braze-Nutzer:innen dabei hilft, die Aufgabe zu erledigen. Mit „Art der Integration“ im Abschnittstitel meinen wir, ob es sich um eine Side-by-side-Integration, eine Server-zu-Server-Integration oder eine Standard-Integration handelt. So können Sie mehrere Integrationsabschnitte anlegen, wenn es mehr als eine Möglichkeit gibt, sich mit diesem Partner zu integrieren.

Wenn es sich um eine Currents-Integration handelt, sollte diese Seite im Currents-Bereich platziert werden, und es sollte eine entsprechende Navigationsseite erstellt werden, die zu diesem Ort in Currents weiterleitet.

### Schritt 1: Dies ist eine kurze Beschreibung von Schritt eins {#step-1-this-is-a-short-description-of-step-one}

Gliedern Sie den Vorgang einfach auf und fügen Sie bei Bedarf Code ein. Denken Sie daran, dass Sie mehrere verschiedene Code-Varianten anbieten können – es ist nicht nötig, nur einen Integrationsweg aufzuzeigen.

### Schritt 2: Dieser Schritt beschreibt Bilder {#step-2-this-step-will-describe-images}

Sie haben die Möglichkeit, Bilder in Ihre Dokumentation einzufügen. Wir empfehlen, dies zu tun – und zwar mit Bedacht.

### Schritt 3: Wie viele Schritte {#step-3-how-many-steps}

Veranschaulichen Sie die Nutzung der Integration – insbesondere wenn dies das Einfügen von Liquid in den Nachrichten-Editor beinhaltet.

## Anpassung {#customization}

Dies ist ein **optionaler** Abschnitt. Hier können Sie spezifische Möglichkeiten zur Anpassung Ihrer Integration zwischen den beiden Partnern beschreiben.

## Diese Integration verwenden {#using-this-integration}

Hier sollte beschrieben werden, wie die Integration verwendet wird – teilen Sie Ihren Leser:innen mit, ob sie ein paar Buttons drücken müssen oder ob nach der Integration nichts weiter zu tun ist.

### Schritt 1: Dies ist eine kurze Beschreibung von Schritt eins

Einfach Ihre typische Schritt-für-Schritt-Anleitung.

## Anwendungsfälle {#use-cases}

Dies kann ein entscheidender Teil Ihrer Dokumentation sein. Obwohl dieser Abschnitt optional ist, eignet er sich hervorragend, um typische oder auch neuartige Anwendungsfälle für die Integration darzustellen. Er kann dazu genutzt werden, die Partnerschaft zu fördern oder auszubauen – er liefert Kontext, Ideen und vor allem eine Möglichkeit, die Fähigkeiten der Integration zu veranschaulichen.