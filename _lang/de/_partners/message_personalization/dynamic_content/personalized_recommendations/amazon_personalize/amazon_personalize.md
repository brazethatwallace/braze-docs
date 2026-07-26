---
nav_title: Amazon Personalize
article_title: Amazon Personalize
alias: "/partners/amazon_personalize_overview/"
description: "Dieser Referenzartikel beschreibt eine Referenzarchitektur für die Integration von Braze und Amazon Personalize. In diesem Artikel erfahren Sie, welche Anwendungsfälle Amazon Personalize bietet, mit welchen Daten es arbeitet, wie Sie den Dienst konfigurieren und wie Sie ihn in Braze integrieren können."
page_type: partner
search_tag: Partner
---

# Amazon Personalize
<!--
{% multi_lang_include video.html id="xFZ3HMleYYE" align="right" %}
-->
> [Amazon Personalize](https://aws.amazon.com/personalize/) ist so, als hätten Sie Ihr eigenes Empfehlungssystem für maschinelles Lernen, das den ganzen Tag läuft. Basierend auf mehr als 20 Jahren Erfahrung mit Empfehlungen ermöglicht Ihnen Amazon Personalize, das geschäftskunden-Engagement zu verbessern, indem es personalisierte Produkt- und Inhaltsempfehlungen in Echtzeit sowie gezielte Marketing-Aktionen ermöglicht.

_Diese Integration wird von Amazon Personalize gepflegt._

## Über die Integration {#about-the-integration}

Mithilfe von maschinellem Lernen und einem Algorithmus, den Sie mit definieren, kann Amazon Personalize Ihnen helfen, ein Modell zu trainieren, das hochwertige Empfehlungen für Ihre Websites und Anwendungen ausgibt. Mit diesen Modellen können Sie Empfehlungslisten auf der Grundlage des bisherigen Verhaltens der Nutzer:innen erstellen, Artikel nach Relevanz sortieren und andere Artikel auf der Grundlage von Ähnlichkeiten empfehlen. Die von der Amazon Personalize API erhaltenen Listen können dann in Braze Connected-Content verwendet werden, um personalisierte Braze-Empfehlungskampagnen durchzuführen. Durch die Integration mit Amazon Personalize haben Kund:innen die Freiheit, die Parameter zu kontrollieren, die zum Trainieren der Modelle verwendet werden, und optionale Geschäftsziele zu definieren, die die Ausgabe des Algorithmus optimieren.

In diesem Referenzartikel erfahren Sie, welche Anwendungsfälle Amazon Personalize bietet, mit welchen Daten es arbeitet, wie Sie den Dienst konfigurieren und wie Sie ihn in Braze integrieren können.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Amazon Web Service Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein AWS-Konto. Nachdem Sie über ein AWS-Konto verfügen, können Sie über die Amazon Personalize-Konsole, die AWS Command Line Interface (AWS CLI) oder die AWS SDKs auf Amazon Personalize zugreifen. |
| Definierte Anwendungsfälle | Bevor Sie ein Modell erstellen, müssen Sie Ihren Anwendungsfall für diese Integration festlegen. In der folgenden Liste finden Sie gängige Anwendungsfälle. |
| Datensätze | Amazon Personalize Empfehlungsmodelle benötigen drei verschiedene Arten von Datensätzen: Interaktionen, Nutzer:innen und Artikel. In den folgenden Details finden Sie die Anforderungen für jeden Datensatz. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% tabs %}
{% tab Anwendungsfälle %}

**Anwendungsfälle**

Bevor Sie ein Modell erstellen, müssen Sie Ihren Anwendungsfall für diese Integration festlegen. Einige häufige Anwendungsfälle sind:
- Empfehlen Sie Nutzer:innen Artikel auf der Grundlage ihrer bisherigen Interaktionen und schaffen Sie so ein wirklich personalisiertes Erlebnis.
- Stellen Sie eine Liste von Artikeln oder Suchergebnissen bereit, die auf jede:n Nutzer:in zugeschnitten sind, und erhöhen Sie das Engagement, indem Sie Artikel nach Relevanz für die Nutzer:innen anzeigen.
- Finden Sie Empfehlungen für ähnliche Artikel und helfen Sie den Nutzer:innen, neue Dinge zu entdecken.

In der folgenden Anleitung konzentrieren wir uns auf das Rezept für personalisierte Nutzer:innen-Empfehlungen.

{% endtab %}
{% tab Datensätze %}

**Datensätze**

Um mit den Empfehlungsmodellen von Amazon Personalize zu beginnen, benötigen Sie drei Arten von Datensätzen:

- Interaktionen
  - Speichert historische Interaktionen zwischen Nutzer:innen und Artikeln
  - Erfordert die Werte `USER_ID`, `ITEM_ID`, `EVENT_TYPE` und `TIMESTAMP` und akzeptiert optional Metadaten über das Ereignis
- Nutzer:innen
  - Speichert Metadaten über die Nutzer:innen
  - Erfordert einen `USER_ID`-Wert und mindestens ein Metadatenfeld (String oder numerisch) wie Geschlecht, Alter, Treue-Mitgliedschaft
- Artikel
  - Speichert Metadaten über Artikel
  - Erfordert eine `ITEM_ID` und mindestens ein Metadatenfeld (textuell, kategorisch oder numerisch), das den Artikel beschreibt

Für ein Rezept für Nutzer:innen-Empfehlungen müssen Sie einen Interaktionsdatensatz mit mindestens 1000 Datenpunkten von mindestens 25 eindeutigen Nutzer:innen mit jeweils mindestens zwei Interaktionen bereitstellen. Diese Datensätze können in großen Mengen über in S3 gespeicherte CSV-Dateien oder inkrementell über die API hochgeladen werden.

{% endtab %}
{% endtabs %}

## Modelle erstellen {#creating-models}

### 1. Schritt: Training {#step-1-training}

Sobald die Datensätze importiert sind, können Sie eine Lösung erstellen. Eine Lösung verwendet eines der Amazon Personalize [Rezepte](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html) (Algorithmen), um ein Modell zu trainieren. In unserem Fall werden wir das Rezept `USER_PERSONALIZATION` verwenden. Durch das Trainieren der Lösung wird eine Lösungsversion (trainiertes Modell) erstellt, die Sie anhand der Performance-Metriken des Modells bewerten können.

Mit Amazon Personalize können Sie die Hyperparameter anpassen, die das Modell beim Training verwendet. Zum Beispiel:
- Mit dem Parameter „Perzentil der Länge des Nutzer:innen-Verlaufs“ in der Amazon Personalize-Konsole können Sie das Perzentil des Nutzer:innen-Verlaufs anpassen, das beim Training berücksichtigt werden soll:<br><br>![Minimal- und Maximaleinstellung des Nutzerprofils]({% image_buster /assets/img/amazon_personalize/min_and_max_user_percentile.png %})
  - `min_user_history_length_percentile`: Schließt einen Prozentsatz der Nutzer:innen mit sehr kurzen Verläufen aus, was hilfreich sein kann, um beliebte Artikel zu eliminieren und Empfehlungen zu erstellen, die auf tiefer liegenden Mustern basieren.
  - `max_user_history_length_percentile`: Passt den Prozentsatz der Nutzer:innen an, der beim Training mit sehr langen Verläufen berücksichtigt werden soll.

Die Anzahl der verborgenen Dimensionen hilft, kompliziertere Muster für komplexe Datensätze zu erkennen, während die Back-Propagation-Through-Time-Technik (BPTT) die Rewards für ein frühes Ereignis anpasst, nachdem eine Kette von Ereignissen stattgefunden hat, die zu einer hochwertigen Aktion geführt haben.

Zusätzlich bietet Amazon Personalize eine automatische Abstimmung der Hyperparameter, indem mehrere Versionen der Lösung mit unterschiedlichen Werten gleichzeitig ausgeführt werden. Um die Abstimmung zu nutzen, aktivieren Sie **Perform HPO**, wenn Sie eine Lösung erstellen.

### 2. Schritt: Auswerten und vergleichen {#step-2-evaluate-and-compare}

Sobald eine Lösung fertig trainiert ist, können Sie sie bewerten und verschiedene Versionen vergleichen. Jede Lösungsversion zeigt berechnete Metriken an. Einige der verfügbaren Metriken sind:

- **Normalisierter diskontierter kumulativer Gewinn:** Vergleicht die empfohlene Reihenfolge der Artikel mit der tatsächlichen Liste der Artikel und gibt jedem Artikel ein Gewicht, das seiner Position in der Liste entspricht
- **Präzision @k:** Die Anzahl der richtig empfohlenen Artikel geteilt durch die Anzahl aller empfohlenen Artikel, wobei `k` die Anzahl der Artikel ist
- **Mittlerer reziproker Rang:** Konzentriert sich auf die erste, höchstrangige Empfehlung und berechnet, wie viele empfohlene Artikel gesehen werden, bevor die erste übereinstimmende Empfehlung erscheint
- **Abdeckungsgrad:** Der Anteil der eindeutig empfohlenen Artikel an der Gesamtzahl der eindeutigen Artikel im Datensatz

## Empfehlungen erhalten {#getting-recommendations}

Sobald Sie eine Lösungsversion erstellt haben, mit der Sie zufrieden sind, ist es an der Zeit, die Empfehlungen in die Tat umzusetzen. Es gibt zwei Möglichkeiten, auf die Empfehlungen zuzugreifen:

1. Realtime-Kampagne<br>Eine Kampagne ist eine eingesetzte Lösungsversion mit einem definierten Mindestdurchsatz an Transaktionen. Eine Transaktion ist ein einzelner API-Aufruf, um die Ausgabe einer Empfehlung zu erhalten. Sie ist definiert als TPS oder Transaktionen pro Sekunde mit einem Mindestwert von eins. Die Kampagne skaliert die Ressourcen im Falle einer erhöhten Belastung, fällt aber nicht unter Ihren Mindestwert. Sie können die Empfehlungen in der Konsole, der AWS CLI oder über AWS SDKs in Ihrem Code abfragen.<br><br>
2. Batch-Auftrag<br>Ein Batch-Auftrag exportiert die Empfehlungen in einen S3-Bucket. Der Auftrag nimmt als Eingabe eine JSON-Datei mit einer Liste von Nutzer-IDs, für die Sie die Empfehlungen exportieren möchten. Nachdem Sie die richtigen Berechtigungen und das Ausgabeziel angegeben haben, können Sie den Auftrag ausführen. Die Laufzeit hängt von der Größe Ihrer Datensätze und der Länge der Empfehlungsliste ab.

### Filter {#filters}

Mit Filtern können Sie die Ausgabe der Empfehlungen anpassen, indem Sie Artikel auf der Grundlage der Artikel-ID, des Ereignistyps oder der Metadaten ausschließen. Sie können Nutzer:innen auch anhand ihrer Metadaten filtern, z. B. Alter oder Status der Treue-Mitgliedschaft. Filter können nützlich sein, um zu verhindern, dass Artikel empfohlen werden, mit denen Nutzer:innen bereits interagiert haben.

## Integration der Ergebnisse in Braze {#integrating-results-with-braze}

Mit dem erstellten Modell und der Empfehlungskampagne sind Sie bereit, eine Braze-Kampagne für Ihre Nutzer:innen mit Content Cards und Connected-Content durchzuführen.
Bevor Sie eine Braze-Kampagne starten, müssen Sie einen Dienst erstellen, der diese Empfehlungen über eine API bereitstellen kann. Sie können [Schritt 3 des Workshop-Artikels]({{site.baseurl}}/partners/amazon_personalize_workshop#step-3-send-personalized-emails-from-braze) befolgen, um den Dienst mithilfe der AWS-Dienste bereitzustellen. Sie können auch Ihren eigenen unabhängigen Backend-Dienst einsetzen, der die Empfehlungen bereitstellt.

### Anwendungsfall: Content-Card-Kampagne {#content-card-campaign-use-case}

Lassen Sie uns eine Content-Card-Kampagne mit dem ersten empfohlenen Artikel aus der Liste durchführen.<br><br>
In den folgenden Beispielen werden wir den Endpunkt
`GET http://<service-endpoint.com>/recommendations?user_id=user123` mit einem `user_id`-Parameter abfragen, der eine Liste der empfohlenen Artikel zurückgibt:

```json
[
  {
    "id": "abc123",
    "url": "http://productpage.com/product/abc123",
    "name": "First Item",
    "price": 39.99,
    "image": "http://pp.cdn.com/abvh3321pjb1j"
  },
  {
    "id": "xyz987",
    "url": "http://productpage.com/product/xyz987",
    "name": "Great Item",
    "price": 19.99,
    "image": "http://pp.cdn.com/234bjl1gioj1b2b"
  },
  ...
]
```

Erstellen Sie im Braze-Dashboard eine neue [Content-Card-Kampagne]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card). Erstellen Sie im Feld für den Nachrichtentext einen Connected-Content-Liquid-Block, um die API abzufragen und die Antwort in der Variablen `recommendations` zu speichern:

{% raw %}

```liquid
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```

Sie können dann den ersten Artikel im resultierenden Array referenzieren und den Nutzer:innen den Inhalt anzeigen:

```liquid
This seems like a great fit for you:
{% recommendations[0].name %}
{% recommendations[0].price %}
```

{% endraw %}

Einschließlich des Titels, des Bildes und der Verlinkung der URL würde die komplette Content-Card so aussehen:

![Ein Bild einer Kampagne mit Connected-Content, das dem Nachrichtentext und dem Feld „Bild hinzufügen“ hinzugefügt wurde. Dieses Bild zeigt auch die Connected-Content-Logik, die dem Feld „Redirect to Web URL“ hinzugefügt wurde und die Nutzer:innen mit einer Empfehlungs-URL verbindet.]({% image_buster /assets/img/amazon_personalize/content-card-campaign.png %})