---
nav_title: Nutzer:innen und Segmente
article_title: "Erste Schritte: Nutzer:innen und Segmente"
page_order: 2
page_type: reference
description: "Dieser Artikel gibt Ihnen einen Überblick über Nutzer:innen und Segmente, ihre Bedeutung und wie Sie sie nutzen können, um Ihre Zielgruppe anzusprechen."
---

# Erste Schritte: Nutzer:innen und Segmente {#get-started-users-and-segments}

> Um personalisierte und gezielte Marketingkampagnen zu versenden, ist es entscheidend, Ihre Nutzer:innen zu verstehen und sie effektiv anzusprechen. Dieser Artikel gibt Ihnen einen Überblick über Nutzer:innen und Segmente, ihre Bedeutung und wie Sie sie nutzen können, um Ihre Zielgruppe anzusprechen.

## Nutzer:innen {#users}

In Braze werden Informationen über Ihre Zielgruppe in Nutzerprofilen gespeichert. Ein [Nutzerprofil]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) ist eine umfassende Sammlung von Informationen und Attributen, die eine:n individuelle:n Verbraucher:in beschreiben. Es dient als zentrales Repository zum Speichern und Verwalten von Daten, die sich auf Verhalten, Präferenzen und demografische Details beziehen.

### Bestandteile eines Nutzerprofils {#parts-of-a-user-profile}

Wenn Sie Nutzerprofile verstehen, können Sie Insights über Ihre Zielgruppe gewinnen und auf personalisierter und zielgerichteter Ebene mit ihr interagieren. Das Profil einer Nutzerin oder eines Nutzers enthält viele Informationen, hier aber einige der wichtigsten Bestandteile:

- **Nutzer-Bezeichner:** Jedes Nutzerprofil wird eindeutig durch eine Nutzer-ID identifiziert, die als `external_id` bezeichnet wird. Dieser Bezeichner ermöglicht es Braze, Nutzerdaten über verschiedene Kanäle und Geräte hinweg zu verfolgen und zuzuordnen, wodurch ein einheitliches Bild der Interaktionen jeder Nutzerin und jedes Nutzers mit Ihrer Marke entsteht. [Anonyme Nutzerprofile]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) (Nutzer:innen, die Ihre Website oder App besuchen, ohne sich anzumelden) haben keine `external_id`, können aber [Nutzer-Aliase]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#assigning-user-aliases) als alternativen Bezeichner zugewiesen bekommen.
- [Attribute](#attributes)**:** Dabei handelt es sich um spezifische Informationen über die Nutzerin oder den Nutzer, wie Name, Alter, Standort oder andere demografische Daten. Sie können diese Attribute nutzen, um Ihre Zielgruppe zu segmentieren und Ihre Nachrichten zu personalisieren.
- [Events](#events)**:** Dies sind Aktionen, die Nutzer:innen ausführen, wie z. B. einen Kauf tätigen, auf einen Link klicken oder eine App öffnen. Braze verfolgt diese Events, um Ihnen dabei zu helfen, das Verhalten und das Engagement der Nutzer:innen zu verstehen. Ähnlich wie Attribute können Sie auch Events zur Segmentierung und Personalisierung verwenden.
- **Käufe:** Dieser Bereich erfasst den Kaufverlauf der Nutzerin oder des Nutzers. Er ist entscheidend, um die Kaufgewohnheiten und Präferenzen zu verstehen.
- **Geräte:** Dieser Bereich listet die Geräte auf, die Nutzer:innen für die Interaktion mit Ihrer Marke verwendet haben. Dies kann Mobilgeräte, Webbrowser und verbundene Geräte (wie Wearables und Smart-TVs) umfassen.
- **Engagement:** Dieser Bereich enthält Informationen über die Interaktionen der Nutzerin oder des Nutzers mit den gesendeten Nachrichten, zu welchen Segments sie gehören, den Abo-Status und mehr.
- **Nachrichtenverlauf:** Dies ist eine Aufzeichnung aller Nachrichten, die über den jeweiligen Messaging-Kanal (wie E-Mail oder Push) an die Nutzerin oder den Nutzer gesendet wurden.

{% alert tip %}
Die SDKs der Braze-Plattform erfassen automatisch 27 verschiedene Attribute und Events. Mit diesen Standard-Events und -Attributen können Sie Segments erstellen, sobald Sie das SDK integriert haben.
{% endalert %}

### Attribute {#attributes}

Attribute sind spezifische Merkmale oder Eigenschaften, die mit Nutzer:innen verknüpft sind. Diese Attribute helfen Ihnen, Nutzer:innen auf Basis ihrer individuellen Eigenschaften und Interessen zu segmentieren und gezielt anzusprechen. Es gibt zwei Arten von Attributen in Braze: Standardattribute und angepasste Attribute.

#### Standardattribute {#standard-attributes}

Standardattribute sind vordefinierte Attribute, die Sie nach der Integration des SDK in Ihre App mit Braze verfolgen können. Es handelt sich um gängige Nutzerinformationen, die die meisten Apps als nützlich erachten, wie demografische Daten und Gerätedaten. Beispiele sind:

- Vorname
- Nachname
- E-Mail
- Geschlecht
- Geburtsdatum
- Land
- Ort
- Zuletzt verwendete App
- Sprache
- Zeitzone

#### Angepasste Attribute {#custom-attributes}

[Angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) sind Attribute, die Sie basierend auf Ihren spezifischen Geschäftsanforderungen definieren. Sie ermöglichen es Ihnen, Informationen zu verfolgen, die einzigartig für Ihre App oder Ihr Unternehmen sind.

Beispielsweise könnte eine Musik-Streaming-App folgende angepasste Attribute verfolgen:

- Lieblingsgenre
- Anzahl abgespielter Songs
- Premium-Abonnent:in (Ja/Nein)
- Lieblingskünstler:in

Eine Einzelhandels-App hingegen könnte folgende angepasste Attribute verfolgen:

- Bevorzugte Kleidungsgröße
- Lieblingsmarke
- Anzahl der Käufe
- Mitglied im Kundenbindungs-Programm (Ja/Nein)

Angepasste Attribute geben Ihnen die Flexibilität, die für Ihr Unternehmen relevantesten Daten zu erfassen und zu analysieren. Sie erfordern jedoch eine zusätzliche Einrichtung.

Sowohl Standard- als auch angepasste Attribute können verwendet werden, um Ihre Zielgruppe zu segmentieren und Ihre Marketing-Nachrichten zu personalisieren. Beispielsweise könnten Sie ein Sonderangebot an Nutzer:innen in einem bestimmten Ort (Standardattribut) senden, die mehr als 10 Käufe getätigt haben (angepasstes Attribut).

### Events {#events}

Events repräsentieren spezifische Aktionen oder Verhaltensweisen, die Nutzer:innen innerhalb Ihrer App oder Website ausführen. Beispiele für Events können App-Starts, Käufe, Inhaltsaufrufe oder andere Aktionen sein. Durch das Verfolgen und Analysieren dieser Events können Sie Insights über das Nutzerverhalten und Engagement-Muster gewinnen.

#### Standard-Events {#standard-events}

[Standard-Events]({{site.baseurl}}/user_guide/data/activation/events) sind vordefinierte Events, die Braze nach der Integration des SDK in Ihre App oder Website automatisch verfolgt. Einige Beispiele für Standard-Events sind:

- **Sitzungsstart:** Dieses Event wird ausgelöst, wenn eine Nutzerin oder ein Nutzer die App öffnet.
- **Sitzungsende:** Dieses Event wird ausgelöst, wenn eine Nutzerin oder ein Nutzer die App schließt.
- **Kauf:** Dieses Event wird ausgelöst, wenn eine Nutzerin oder ein Nutzer einen In-App-Kauf tätigt.
- **Klick auf Push-Benachrichtigung:** Dieses Event wird ausgelöst, wenn eine Nutzerin oder ein Nutzer auf eine Push-Benachrichtigung klickt.

#### Angepasste Events {#custom-events}

[Angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events) sind Events, die Sie basierend auf den spezifischen Aktionen definieren, die Sie innerhalb Ihrer App oder Website verfolgen möchten. Beispielsweise könnte eine Musik-Streaming-App folgende angepasste Events verfolgen:

- Song abgespielt
- Playlist erstellt
- Werbung übersprungen

Eine Fitness-App hingegen könnte folgende angepasste Events verfolgen:

- Training gestartet
- Training abgeschlossen
- Persönlicher Rekord aufgestellt

Angepasste Events geben Ihnen die Flexibilität, die für Ihre App und Ihr Unternehmen relevantesten Aktionen zu verfolgen. Wie angepasste Attribute erfordern sie jedoch eine zusätzliche Einrichtung.

### Datenpunkte {#data-points}

Braze verwendet Datenpunkte, um Ihnen dabei zu helfen, die wirkungsvollsten Informationen für Ihr Unternehmen zu definieren. Datenpunkte sind ein entscheidender Bestandteil der Funktionsweise von Braze und werden für Abrechnung, Preisgestaltung und – am wichtigsten – für die Personalisierung und Optimierung Ihrer Marketing-Campaigns verwendet.

Datenpunkte werden verbraucht, wenn die Profildaten von Nutzer:innen aktualisiert werden oder wenn diese bestimmte Aktionen ausführen. Zu diesen Aktionen können das Starten einer Sitzung, das Beenden einer Sitzung, das Aufzeichnen eines angepassten Events oder das Tätigen eines Kaufs gehören. Es ist wichtig zu beachten, dass nicht alle von Braze erfassten Daten als Datenpunkte zählen. Beispielsweise werden Daten und Events, die standardmäßig von den Braze-Diensten erfasst werden – wie Push-Token, Geräteinformationen und alle Engagement-Tracking-Events von Campaigns wie E-Mail-Öffnungen und Klicks auf Push-Benachrichtigungen – nicht als Datenpunkte gezählt.

Indem Sie sorgfältig abwägen, welche Informationen Sie als Datenpunkte verfolgen, zielen Sie auf die Daten mit der größten Wirkung für das Erlebnis Ihrer Nutzer:innen ab. Ihre Account Manager:in bei Braze wird Ihnen helfen, bewährte Datenstrategien zu empfehlen, die Ihren Anforderungen entsprechen.

Besuchen Sie unseren speziellen Artikel, um mehr über [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points) zu erfahren.

## Segments {#segments}

[Segmentierung]({{site.baseurl}}/user_guide/audience/segments) ermöglicht es Ihnen, Nutzer:innen auf Basis ihrer demografischen, verhaltensbezogenen, sozialen oder technischen Merkmale und Aktionen (also Attribute und Events) gezielt anzusprechen. Der kreative und intelligente Einsatz von Segmentierung und Messaging-Automatisierung ermöglicht es Ihnen, Ihre Nutzer:innen nahtlos durch ihren Kundenlebenszyklus zu begleiten.

Tipps für die Arbeit mit Segments:

- Segments in Braze sind dynamisch: Nutzer:innen fließen ständig in Segmente hinein und wieder heraus, da sie nicht immer die Kriterien erfüllen. Nutzer:innen, die zum Zeitpunkt des Versands die Kriterien eines Segments erfüllen, sind die Empfänger:innen dieser Campaign oder dieses Canvas.
    - Wenn Ihr Segment statisch sein soll, können Sie Segmenterweiterungen verwenden. Segmenterweiterungen (mit [deaktivierter Regenerierung]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-4-designate-refresh-settings-optional)) stellen Ihre Zielgruppe als einzelne Momentaufnahme dar.
- Sie sind nicht auf die Verwendung eines einzelnen Filters beschränkt. Erstellen Sie fein abgestimmte, granulare Segmente, indem Sie mehrere Filter übereinander schichten.
- Sie können die Aktionen oder Inaktivitäten Ihrer Nutzer:innen nutzen, um zu verstehen, wie Sie Ihre Nutzer:innen dort erreichen, wo sie mit Ihnen interagieren möchten. Diese Aktionen können angepasste Events, Engagement mit einer bestehenden Campaign oder einem Canvas oder sogar eine bestimmte Nachricht innerhalb eines Canvas sein.

### Anwendungsfall {#use-case}

Angenommen, Sie betreiben einen Online-Bekleidungsshop und haben einen Messaging-Flow eingerichtet, der eine Reihe von E-Mails an Nutzer:innen sendet, die einen Artikel in ihren Warenkorb gelegt, den Kauf aber nicht abgeschlossen haben. Dieser Warenkorb-Abbruch-Flow könnte eine erste Erinnerungs-E-Mail, eine Folge-E-Mail mit einem Rabattangebot und eine abschließende Erinnerungs-E-Mail umfassen.

![Screenshot zum Anwendungsfall.]({% image_buster /assets/img/getting_started/segment_example.png %}){: style="max-width:70%" }

Sie könnten ein Segment von Nutzer:innen erstellen, die das angepasste Event „Artikel in den Warenkorb gelegt“ ausgelöst haben, aber nicht das angepasste Event „Kauf abgeschlossen“. Innerhalb dieses Segments könnten Sie dann weitere Nutzer:innen identifizieren, die die erste Erinnerungs-E-Mail geöffnet haben (Engagement mit einer bestimmten Nachricht), aber keinen Kauf getätigt haben.

![Sie könnten ein Segment von Nutzer:innen erstellen, die das angepasste Event „Artikel in den Warenkorb gelegt“ ausgelöst haben, aber nicht das angepasste Event „Kauf abgeschlossen“. Innerhalb dieses Segments könnten Sie dann weitere Nutzer:innen identifizieren, die die erste Erinnerungs-E-Mail geöffnet haben (Engagement mit einer bestimmten Nachricht), aber keinen Kauf getätigt haben.]({% image_buster /assets/img/getting_started/segment_example_breakdown.png %})

Dieses Segment könnte mit einer aggressiveren Campaign angesprochen werden, um diese Nutzer:innen in Käufer:innen zu verwandeln. Sie könnten ihnen beispielsweise ein Sonderangebot oder eine personalisierte Empfehlung basierend auf den Artikeln in ihrem Warenkorb senden.

Dies ist nur ein Beispiel dafür, wie Sie Nutzeraktionen und -inaktivitäten, angepasste Events und Engagement-Daten verwenden können, um Segmente zu erstellen und Ihre Marketingstrategien in Braze maßzuschneidern.