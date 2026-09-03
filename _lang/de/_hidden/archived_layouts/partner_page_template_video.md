---
nav_title: Partnerseite mit Video

page_order: 4

#Required
description: "Dies ist die Beschreibung der Google-Suche. Zeichen, die über 160 hinausgehen, werden abgeschnitten, fassen Sie sich kurz."
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

{% multi_lang_include video.html id="XY5uXoKIvFY" align="right" %}

> Willkommen beim Template für die Partnerseite! Hier finden Sie alles, was Sie brauchen, um Ihre eigene Partnerseite zu erstellen. In diesem ersten Abschnitt sollten Sie den Partner im ersten Absatz in ein oder zwei Sätzen beschreiben. Fügen Sie außerdem einen Link zur Hauptseite des Partners hinzu.

Im zweiten Absatz sollten Sie die Beziehung zwischen Braze und diesem Partner untersuchen und erklären. Dieser Absatz sollte erklären, wie Braze und dieser Partner zusammenarbeiten, um die Bindung zwischen Braze-Nutzer:innen und ihren Kund:innen zu festigen. Erläutern Sie den Mehrwert, der entsteht, wenn Braze-Nutzer:innen diesen Partner und seine Dienste integrieren oder nutzen.

## Voraussetzungen {#requirements-or-prerequisites}

In diesem Abschnitt geht es darum, was Sie für die Integration mit dem Partner benötigen, um dessen Dienste nutzen zu können. Am besten vermitteln Sie diese Informationen in einem kurzen Absatz, der alle wichtigen, nicht-technischen Details beschreibt, die man wissen sollte – zum Beispiel, ob Ihre Integration zusätzlichen Sicherheitsprüfungen oder Freigaben unterliegt. Anschließend sollten Sie die technischen Anforderungen der Integration in einer Tabelle darstellen.

{% alert important %}
Die folgenden Anforderungen sind typische Voraussetzungen, die Sie möglicherweise von Braze benötigen. Wir empfehlen, die zugeordneten Bezeichnungen, Herkunft, Links und Formulierungen wie in der folgenden Tabelle aufgeführt zu verwenden. Passen Sie die Beschreibung unbedingt so an, dass klar ist, wofür die einzelnen Anforderungen verwendet werden.
{% endalert %}

| Anforderung | Herkunft | Zugang | Beschreibung |
|---|---|---|---|
| REST-API-Schlüssel des Braze-Workspace | Braze-Plattform | Seite **Einstellungen** > **App-Einstellungen** | Diese Beschreibung sollte erklären, was mit dem REST-API-Schlüssel des Workspace zu tun ist. |
| Braze-API-Endpunkt | Braze-Plattform | Sehen Sie sich unsere [aufgelisteten Endpunkte]({{site.baseurl}}/api/basics#endpoints) an oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support). | Beschreibung ausstehend. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Voraussetzungen" }

## [Integrationstyp]-Integration {#type-of-integration-integration}

Hier wird die Integration in einzelne Schritte aufgeschlüsselt. Schreiben Sie keine endlosen Absätze – dies sind technische Dokumente, die sowohl von Marketern als auch von Entwickler:innen genutzt werden, um die Integration zum Laufen zu bringen. Ihr einziges Ziel in diesem Abschnitt ist es, eine verständliche Dokumentation zu verfassen, die Braze-Nutzer:innen hilft, die Aufgabe zu erledigen. Mit „Integrationstyp“ im Abschnittstitel ist gemeint, ob es sich um eine Side-by-side-Integration, eine Server-zu-Server-Integration oder eine Standard-Integration handelt. So können Sie mehrere Integrationsabschnitte anlegen, wenn es mehr als einen Weg gibt, mit diesem Partner zu integrieren.

Wenn es sich um eine Currents-Integration handelt, sollte sich diese Seite im Currents-Bereich befinden. Eine entsprechende Navigationsseite sollte erstellt werden, die zu diesem Currents-Standort weiterleitet.

### Schritt 1: Dies ist eine kurze Beschreibung von Schritt eins {#step-1-this-is-a-short-description-of-step-one}

Schlüsseln Sie dies einfach auf und fügen Sie bei Bedarf Code ein. Beachten Sie, dass Sie mehrere Code-Varianten anbieten können – es ist nicht nötig, nur einen Integrationsweg aufzuzeigen.

### Schritt 2: In diesem Schritt werden Bilder beschrieben {#step-2-this-step-will-describe-images}

Sie haben die Möglichkeit, Bilder in Ihre Dokumentation einzufügen. Wir empfehlen, dies zu tun – und zwar bewusst.

### Code-Beispiel {#code-sample}

Wenn Sie ein technisches Konzept erklären, weisen Sie hier darauf hin und zeigen Sie ein Code-Beispiel.

```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```

Stellen Sie sicher, dass Sie Parameter oder Elemente definieren, die Nutzer:innen möglicherweise im Code-Beispiel anpassen müssen. Viele Nutzer:innen werden den Code einfach kopieren und einfügen.

| Variable | Beschreibung |
| -------- | ----------- |
| Page Title | Sie können Ihrer Seite einen beliebigen Titel geben. Dieser ist erforderlich. |
| My First Heading | Wir empfehlen, dies in Großbuchstaben zu schreiben. Dieser Eintrag ist optional. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Code-Beispiel" }


### Schritt 3: Wie viele Schritte {#step-3-how-many-steps}

Beschreiben Sie die Nutzung der Integration – insbesondere wenn dabei Liquid in den Nachrichten-Editor eingefügt werden muss.

## Anpassung {#customization}

Dies ist ein **optionaler** Abschnitt. Hier können Sie spezifische Möglichkeiten zur Anpassung Ihrer Integration zwischen den beiden Partnern beschreiben.

## Diese Integration verwenden {#using-this-integration}

Hier sollte beschrieben werden, wie die Integration verwendet wird – teilen Sie Ihren Lesenden mit, ob sie ein paar Buttons drücken müssen oder ob nach der Integration nichts weiter zu tun ist.

### Schritt 1: Dies ist eine kurze Beschreibung von Schritt eins

Einfach eine typische Schritt-für-Schritt-Anleitung.

### Code-Beispiel

Wenn Sie ein technisches Konzept erklären, vermerken Sie dies hier und zeigen Sie ein Code-Beispiel.

```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```

Stellen Sie sicher, dass Sie Parameter oder Elemente definieren, die Nutzer:innen möglicherweise aus dem Code-Beispiel anpassen müssen. Viele Nutzer:innen werden den Code einfach kopieren und einfügen.

| Variable | Beschreibung |
| -------- | ----------- |
| Page Title | Sie können Ihre Seite beliebig benennen. Dieses Element ist erforderlich. |
| My First Heading | Wir empfehlen, dies in Großbuchstaben zu schreiben. Dieses Element ist optional. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Code-Beispiel" }

## Anwendungsfälle {#use-cases}

Dies kann ein entscheidender Teil Ihrer Dokumentation sein. Auch wenn dieser Abschnitt optional ist, eignet er sich hervorragend, um typische oder auch neuartige Anwendungsfälle für die Integration darzustellen. Dies kann genutzt werden, um die Partnerschaft zu fördern oder auszubauen – es bietet Kontext, Ideen und vor allem eine Möglichkeit, die Funktionen der Integration zu veranschaulichen.