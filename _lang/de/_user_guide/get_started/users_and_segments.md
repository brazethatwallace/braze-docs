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

In Braze werden die Informationen über Ihre Zielgruppe in Nutzerprofilen gespeichert. Ein [Nutzerprofil]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) ist eine umfassende Sammlung von Informationen und Attributen, die eine:n individuelle:n Verbraucher:in beschreiben. Es dient als zentraler Speicher für die Verwaltung von Daten über Verhalten, Vorlieben und demografische Details.

### Bestandteile eines Nutzerprofils {#parts-of-a-user-profile}

Wenn Sie Nutzerprofile verstehen, können Sie Insights über Ihre Zielgruppe gewinnen und sie gezielt und personalisiert ansprechen. Ein Nutzerprofil enthält eine Vielzahl von Informationen. Hier sind einige der wichtigsten Bestandteile:

- **Nutzerkennung:** Jedes Nutzerprofil wird durch eine Nutzer-ID, `external_id` genannt, eindeutig identifiziert. Diese Kennung ermöglicht es Braze, Nutzerdaten über verschiedene Kanäle und Geräte hinweg zu verfolgen und zuzuordnen, sodass Sie einen einheitlichen Überblick über die Interaktionen der einzelnen Nutzer:innen mit Ihrer Marke erhalten. [Anonyme Nutzerprofile]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) (Nutzer:innen, die Ihre Website oder Anwendung besuchen, ohne sich anzumelden) haben keine `external_id`, können aber als alternativer Bezeichner mit [Nutzer-Aliase]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#assigning-user-aliases) versehen werden.
- [Attribute](#attributes)**:** Dabei handelt es sich um spezifische Informationen über die Nutzer:innen, wie z. B. Name, Alter, Standort oder andere demografische Informationen. Sie können diese Attribute nutzen, um Ihre Zielgruppe zu segmentieren und Ihre Nachrichten zu personalisieren.
- [Events](#events)**:** Das sind Aktionen, die Nutzer:innen durchführen, z. B. einen Kauf tätigen, auf einen Link klicken oder eine App öffnen. Braze verfolgt diese Events, um Ihnen zu helfen, das Verhalten und das Engagement der Nutzer:innen nachzuvollziehen. Ähnlich wie bei Attributen können Sie auch Events zur Segmentierung und Personalisierung verwenden.
- **Käufe:** In diesem Bereich wird die Kaufhistorie der Nutzer:innen aufgezeichnet. Das ist wichtig, um die Kaufgewohnheiten und Vorlieben zu verstehen.
- **Geräte:** Dieser Abschnitt listet die Geräte auf, die Nutzer:innen verwendet haben, um mit Ihrer Marke zu interagieren. Dazu gehören mobile Geräte, Webbrowser und verbundene Geräte (wie Wearables und Smart-TVs).
- **Engagement:** Dieser Bereich enthält Informationen über die Interaktionen der Nutzer:innen mit den von Ihnen gesendeten Nachrichten, zu welchen Segmenten sie gehören, den Abonnementstatus und mehr.
- **Nachrichtenverlauf:** Dies ist eine Aufzeichnung aller Nachrichten, die über den jeweiligen Messaging-Kanal (z. B. E-Mail oder Push) an die Nutzer:innen gesendet wurden.

{% alert tip %}
Die SDKs von Braze erfassen automatisch 27 verschiedene Attribute und Events. Mithilfe dieser Standard-Events und -Attribute können Sie Segmente erstellen, sobald Sie das SDK integrieren.
{% endalert %}

### Attribute {#attributes}

Attribute sind spezifische Merkmale oder Eigenschaften, die mit Nutzer:innen verbunden sind. Diese Attribute helfen Ihnen dabei, Nutzer:innen auf der Grundlage ihrer einzigartigen Eigenschaften und Interessen zu segmentieren und anzusprechen. In Braze gibt es zwei Arten von Attributen: Standardattribute und angepasste Attribute.

#### Standardattribute {#standard-attributes}

Standardattribute sind vorgegebene Attribute, die Sie mit Braze verfolgen können, nachdem Sie das SDK in Ihre App integriert haben. Es handelt sich dabei um allgemeine Nutzerinformationen, die für die meisten Apps nützlich sind, wie z. B. demografische Daten und Gerätedaten. Beispiele hierfür sind:

- Vorname
- Nachname
- E-Mail
- Geschlecht
- Geburtsdatum
- Land
- Ort
- Letzte App-Nutzung
- Sprache
- Zeitzone

#### Angepasste Attribute {#custom-attributes}

[Angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) sind Attribute, die Sie auf der Grundlage Ihrer spezifischen Geschäftsanforderungen definieren. Sie ermöglichen es Ihnen, Daten zu verfolgen, die Ihre App oder Ihr Unternehmen auszeichnen.

Eine Musikstreaming-App könnte zum Beispiel folgende angepasste Attribute verfolgen:

- Bevorzugtes Genre
- Anzahl der gespielten Titel
- Premium-Abonnent:in (Ja/Nein)
- Lieblingskünstler:in

Eine Einzelhandels-App hingegen könnte angepasste Attribute wie diese verfolgen:

- Bevorzugte Kleidergröße
- Lieblingsmarke
- Anzahl der Käufe
- Mitglied im Kundenbindungs-Programm (Ja/Nein)

Angepasste Attribute geben Ihnen die Flexibilität, die Daten zu sammeln und zu analysieren, die für Ihr Unternehmen am relevantesten sind. Sie erfordern jedoch eine zusätzliche Einrichtung.

Sowohl Standard- als auch angepasste Attribute können verwendet werden, um Ihre Zielgruppe zu segmentieren und Ihre Marketingbotschaften zu personalisieren. Sie könnten zum Beispiel ein spezielles Angebot an Nutzer:innen in einer bestimmten Stadt (Standardattribut) senden, die mehr als 10 Käufe getätigt haben (angepasstes Attribut).

### Events {#events}

Events stellen bestimmte Aktionen oder Verhaltensweisen dar, die von Nutzer:innen innerhalb Ihrer App oder Website ausgeführt werden. Beispiele für Events sind das Starten von Apps, Käufe, das Aufrufen von Inhalten oder andere Aktionen. Wenn Sie diese Events verfolgen und analysieren, erhalten Sie Einblicke in Nutzerverhalten und Engagement-Muster.

#### Standard-Events {#standard-events}

[Standard-Events]({{site.baseurl}}/user_guide/data/activation/events) sind vorgegebene Events, die Braze automatisch verfolgt, nachdem das SDK in Ihre App oder Website integriert wurde. Einige Beispiele für Standard-Events sind:

- **Sitzungsbeginn:** Dieses Event wird ausgelöst, wenn Nutzer:innen die App öffnen.
- **Sitzungsende:** Dieses Event wird ausgelöst, wenn Nutzer:innen die App schließen.
- **Kauf:** Dieses Event wird ausgelöst, wenn Nutzer:innen in der App einen Kauf tätigen.
- **Klick auf Push-Benachrichtigung:** Dieses Event wird ausgelöst, wenn Nutzer:innen auf eine Push-Benachrichtigung klicken.

#### Angepasste Events {#custom-events}

[Angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events) sind Events, die Sie auf der Grundlage der spezifischen Aktionen definieren, die Sie innerhalb Ihrer App oder Website verfolgen möchten. Eine Musikstreaming-App könnte zum Beispiel folgende angepasste Events verfolgen:

- Song abgespielt
- Wiedergabeliste erstellt
- Anzeige übersprungen

Eine Fitness-App hingegen könnte angepasste Events wie diese verfolgen:

- Workout gestartet
- Workout abgeschlossen
- Persönlicher Rekord aufgestellt

Angepasste Events geben Ihnen die Flexibilität, die Aktionen zu verfolgen, die für Ihre App und Ihr Unternehmen am relevantesten sind. Wie angepasste Attribute erfordern sie jedoch eine zusätzliche Einrichtung.

### Datenpunkte {#data-points}

Braze verwendet Datenpunkte, damit Sie die wichtigsten Informationen für Ihr Unternehmen bestimmen können. Datenpunkte sind ein wesentlicher Bestandteil der Funktionsweise von Braze und werden für die Abrechnung, Preisgestaltung und vor allem für die Personalisierung und Optimierung Ihrer Marketingkampagnen verwendet.

Datenpunkte werden verbraucht, wenn die Profildaten von Nutzer:innen aktualisiert werden oder wenn sie bestimmte Aktionen durchführen. Diese Aktionen können der Beginn einer Sitzung, das Ende einer Sitzung, das Aufzeichnen eines angepassten Events oder ein Kauf sein. Dabei ist es wichtig zu wissen, dass nicht alle von Braze erfassten Daten als Datenpunkte zählen. So werden beispielsweise Daten und Events, die standardmäßig von den Braze-Diensten erfasst werden, wie Push-Token, Geräteinformationen und alle Engagement-Tracking-Events für Campaigns – wie das Öffnen von E-Mails und das Klicken auf Push-Benachrichtigungen – nicht als Datenpunkte gezählt.

Wenn Sie sich genau überlegen, welche Informationen Sie als Datenpunkte verfolgen möchten, zielen Sie auf die Daten mit dem größten Einfluss auf die Erfahrung Ihrer Nutzer:innen ab. Ihr Braze Account Manager hilft Ihnen dabei, geeignete Datenpraktiken für Ihre Bedürfnisse zu empfehlen.

In unserem Artikel erfahren Sie mehr über [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points).

## Segmente {#segments}

[Segmentierung]({{site.baseurl}}/user_guide/audience/segments) ermöglicht es Ihnen, Nutzer:innen auf der Grundlage ihrer demografischen, verhaltensbezogenen, sozialen oder technischen Merkmale und Aktionen (d. h. Attribute und Events) gezielt anzusprechen. Durch den kreativen und intelligenten Einsatz von Segmentierung und Messaging-Automatisierung können Sie Ihre Nutzer:innen nahtlos durch ihren Kundenlebenszyklus führen.

Tipps für die Arbeit mit Segmenten:

- Segmente in Braze sind dynamisch: Nutzer:innen fließen ständig in Segmente hinein und wieder heraus, da sie nicht immer die Kriterien erfüllen. Nutzer:innen, die zum Versandzeitpunkt die Kriterien eines Segments erfüllen, sind die Empfänger:innen der jeweiligen Campaign oder des Canvas.
    - Wenn Sie statische Segmente wünschen, können Sie Segmenterweiterungen verwenden. Segmenterweiterungen ([ohne Regeneration]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-4-designate-refresh-settings-optional)) bilden Ihre Zielgruppe als einzelne Momentaufnahme ab.
- Sie sind nicht auf einen einzelnen Filter beschränkt. Erstellen Sie exakt abgegrenzte, granulare Segmente, indem Sie mehrere Filter übereinander legen.
- Sie können die Aktionen oder Nicht-Aktionen Ihrer Nutzer:innen nutzen, um zu verstehen, wie Sie sie dort erreichen, wo sie mit Ihnen in Kontakt treten möchten. Bei diesen Aktionen kann es sich um angepasste Events, Engagement mit einer bestehenden Campaign oder einem Canvas oder sogar um eine bestimmte Nachricht innerhalb eines Canvas handeln.

### Anwendungsfall {#use-case}

Nehmen wir an, Sie betreiben ein Online-Bekleidungsgeschäft und haben einen Messaging-Flow eingerichtet, um eine Reihe von E-Mails an Nutzer:innen zu senden, die einen Artikel in ihren Warenkorb gelegt, den Kauf aber nicht abgeschlossen haben. Dieser Warenkorb-Abbruch-Flow könnte eine erste Erinnerungs-E-Mail, eine Folge-E-Mail mit einem Rabattangebot und eine abschließende Erinnerungs-E-Mail umfassen.

![Screenshot zum Anwendungsfall.]({% image_buster /assets/img/getting_started/segment_example.png %}){: style="max-width:70%" }

Sie könnten ein Segment von Nutzer:innen erstellen, die das angepasste Event „Artikel in den Warenkorb gelegt“ ausgelöst, aber nicht das angepasste Event „Kauf abgeschlossen“ ausgelöst haben. Innerhalb dieses Segments könnten Sie dann die Nutzer:innen identifizieren, die die erste Erinnerungs-E-Mail geöffnet (Engagement mit einer bestimmten Nachricht), aber keinen Kauf getätigt haben.

![Sie könnten ein Segment von Nutzer:innen erstellen, die das angepasste Event „Artikel in den Warenkorb gelegt“ ausgelöst, aber nicht das angepasste Event „Kauf abgeschlossen“ ausgelöst haben. Innerhalb dieses Segments könnten Sie dann die Nutzer:innen identifizieren, die die erste Erinnerungs-E-Mail geöffnet (Engagement mit einer bestimmten Nachricht), aber keinen Kauf getätigt haben.]({% image_buster /assets/img/getting_started/segment_example_breakdown.png %})

Dieses Segment könnte dann mit einer aggressiveren Campaign angesprochen werden, um diese Nutzer:innen zu Käufer:innen zu konvertieren. Sie könnten ihnen zum Beispiel ein Sonderangebot oder eine personalisierte Empfehlung auf der Grundlage der Artikel in ihrem Warenkorb senden.

Dies ist nur ein Beispiel dafür, wie Sie Nutzeraktionen und -inaktionen, angepasste Events und Engagement-Daten nutzen können, um Segmente zu erstellen und Ihre Marketingstrategien in Braze anzupassen.