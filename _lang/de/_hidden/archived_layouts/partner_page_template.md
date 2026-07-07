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

## Anforderungen oder Voraussetzungen {#requirements-or-prerequisites}

In diesem Abschnitt erfahren Sie alles, was Sie für die Integration mit dem Partner und die Nutzung seiner Dienste benötigen. Am besten vermitteln Sie diese Informationen in einem kurzen Anleitungsabsatz, der alle nicht-technischen, wichtigen Details beschreibt, die Sie wissen müssen – zum Beispiel, ob Ihre Integration zusätzlichen Sicherheitsprüfungen oder Genehmigungen unterliegt. Anschließend sollten Sie ein Chart verwenden, um die technischen Anforderungen der Integration zu beschreiben.

{% alert important %}
Die folgenden Anforderungen sind typische Anforderungen, die Sie von Braze benötigen könnten. Wir empfehlen, die zugeordneten Titel, Herkunft, Links und Formulierungen zu verwenden, die im folgenden Chart aufgeführt sind. Passen Sie die Beschreibung so an, dass Sie wissen, wozu die einzelnen Anforderungen dienen.
{% endalert %}

| Anforderung | Herkunft | Zugang | Beschreibung |
|---|---|---|---|
| Braze-Workspace-REST-API-Schlüssel | Braze-Plattform | Seite **Settings** > **API Key** | Diese Beschreibung sollte Ihnen erklären, was Sie mit dem REST-API-Schlüssel für den Workspace tun sollen. |
| Braze-API-Endpunkt | Braze-Plattform | Sehen Sie sich unsere [aufgelisteten Endpunkte]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) an oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/). | Beschreibung ausstehend. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## [Art der Integration] Integration {#type-of-integration-integration}

Hier können Sie die Integration in einzelne Schritte aufgliedern. Schreiben Sie nicht einfach endlose Absätze – dies sind technische Dokumente, die von Marketern und Entwickler:innen gleichermaßen verwendet werden, um die Integration zum Laufen zu bringen. Ihr einziges Ziel in diesem Abschnitt ist es, eine beschreibende Dokumentation zu verfassen, die Braze-Nutzer:innen hilft, die Aufgabe zu erledigen. Mit „Art der Integration“ im Abschnittstitel geben wir an, ob es sich um eine Side-by-side-Integration, eine Server-zu-Server-Integration oder eine Standardintegration handelt. So können Sie mehrere Integrationsabschnitte haben, wenn es mehr als eine Möglichkeit der Integration mit diesem Partner gibt.

Wenn es sich um eine Currents-Integration handelt, sollte sich diese Seite im Abschnitt Currents befinden, und es sollte eine entsprechende Navigationsseite erstellt werden, die zu diesem Standort in Currents weiterleitet.

### 1. Schritt: Dies ist eine kurze Beschreibung von Schritt eins {#step-1-this-is-a-short-description-of-step-one}

Gliedern Sie dies einfach auf und fügen Sie bei Bedarf Code hinzu. Denken Sie daran, dass Sie mehrere verschiedene Code-Varianten anbieten können – es ist nicht nötig, nur eine Art der Integration anzubieten.

### 2. Schritt: Dieser Schritt beschreibt Bilder {#step-2-this-step-will-describe-images}

Sie haben die Möglichkeit, Bilder in Ihre Dokumentation aufzunehmen. Wir empfehlen Ihnen, dies zu tun – und zwar mit Bedacht.

### 3. Schritt: Wie viele Schritte {#step-3-how-many-steps}

Skizzieren Sie die Nutzung der Integration – vor allem, wenn es darum geht, Liquid in unseren Nachrichten-Editor einzufügen.

## Anpassung {#customization}

Dies ist ein **optionaler** Abschnitt. Hier könnten Sie alle spezifischen Möglichkeiten zur Anpassung Ihrer Integration zwischen den beiden Partnern skizzieren.

## Diese Integration verwenden {#using-this-integration}

Hier sollten Sie beschreiben, wie die Integration genutzt wird – lassen Sie Ihre Leser:innen wissen, ob sie ein paar Buttons drücken müssen oder ob sie nach der Integration überhaupt nichts mehr tun müssen.

### 1. Schritt: Dies ist eine kurze Beschreibung von Schritt eins

Einfach eine typische Schritt-für-Schritt-Anleitung.

## Anwendungsfälle {#use-cases}

Dies kann ein entscheidender Teil Ihrer Dokumentation sein. Obwohl dieser Abschnitt optional ist, ist er ein guter Ort, um typische oder sogar neuartige Anwendungsfälle für die Integration zu skizzieren. Dies kann als Mittel zum Verkauf oder Upselling der Beziehung genutzt werden – es liefert Kontext, Ideen und vor allem eine Möglichkeit, die Fähigkeiten der Integration zu veranschaulichen.