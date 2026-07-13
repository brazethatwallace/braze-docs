---
nav_title: Analytics
article_title: "Analytics für Artikel-Empfehlungen"
description: "Erfahren Sie mehr über Analytics für Artikel-Empfehlungen und wie Sie diese in Braze anzeigen können."
page_order: 1.3
---

# Analytics für Artikel-Empfehlungen {#item-recommendation-analytics}

> Erfahren Sie mehr über Analytics für Artikel-Empfehlungen und wie Sie diese in Braze anzeigen können.

## Analytics anzeigen {#viewing-analytics}

Sie können die Analytics für Ihre Empfehlung einsehen, um zu sehen, welche Artikel Nutzer:innen empfohlen wurden und wie genau das Empfehlungsmodell war.

1. Gehen Sie zu **Analytics** > **Item Recommendation**.
2. Wählen Sie Ihre Empfehlung aus der Liste aus.

## Verfügbare Metriken {#available-metrics}

### Zielgruppe {#audience}

Dies sind Metriken, die sich auf Ihre Empfehlungs-Zielgruppe beziehen. Dazu gehören Präzision, Abdeckung und Empfehlungstyp.

![Empfehlungs-Zielgruppen-Metriken, die Präzision, Abdeckung und Empfehlungstypen, unterteilt in personalisierte und beliebteste Artikel, anzeigen.]({% image_buster /assets/img/item_recs_analytics_1.png %})

Weitere Informationen finden Sie in der folgenden Tabelle:

| Metrik | Beschreibung |
| ------------------- | ---------- |
| **Präzision** | Der Prozentsatz der Fälle, in denen das Modell den nächsten Artikel, den ein:e Nutzer:in gekauft hat, korrekt vorhergesagt hat. Die Präzision hängt stark von Ihrer spezifischen Kataloggröße und -zusammensetzung ab und sollte als Richtwert dienen, um zu verstehen, wie oft das Modell korrekt liegt.<br><br>Bei bisherigen Tests haben wir festgestellt, dass Modelle mit Präzisionswerten von 6–20 % gut abschneiden. Diese Metrik wird aktualisiert, wenn das Modell das nächste Mal neu trainiert wird. |
| **Abdeckung** | Welcher Prozentsatz der verfügbaren Artikel im Katalog mindestens einer Nutzer:in empfohlen wird. Sie können davon ausgehen, dass Sie mit personalisierten Artikel-Empfehlungen eine höhere Artikelabdeckung erzielen als mit den beliebtesten Artikeln. |
| **Empfehlungstyp** | Der Prozentsatz der Nutzer:innen, die personalisierte oder neueste Empfehlungen erhalten, im Vergleich zum Fallback der beliebtesten Artikel. Der Fallback wird an Nutzer:innen gesendet, die nicht über genügend Daten verfügen, um eine personalisierte oder aktuelle Empfehlung zu generieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zielgruppe" }

### Artikel {#items}

Diese Tabelle enthält Metriken zu Ihren personalisierten, neuesten und beliebtesten Artikeln aus Ihrem Katalog.

![Nebeneinander angeordnete Tabellen mit den Nutzer:innen zugewiesenen Artikeln, getrennt nach personalisierten Empfehlungen und beliebtesten Empfehlungen.]({% image_buster /assets/img/item_recs_analytics_2.png %})

Weitere Informationen finden Sie in der folgenden Tabelle:

| Metrik | Beschreibung |
| ------------------- | ---------- |
| **Personalisierte Artikel**<br><br>**Neueste Artikel** | Diese Spalte listet jeden Artikel im Katalog in absteigender Reihenfolge der Häufigkeit auf, mit der er Nutzer:innen empfohlen wurde. Diese Spalte zeigt auch, wie vielen Nutzer:innen jeder Artikel durch das Modell zugewiesen wurde.<br><br>Je nach [Empfehlungstyp]({{site.baseurl}}/user_guide/brazeai/item_recommendations) werden entweder **personalisierte** oder **neueste** Artikel aufgelistet. |
| **Beliebteste Artikel** | Diese Spalte listet jeden Artikel im Katalog in absteigender Reihenfolge seiner Beliebtheit auf. Beliebtheit bezieht sich hier auf die Artikel im Katalog, mit denen Nutzer:innen im gesamten Workspace am häufigsten interagieren. „Beliebteste“ wird als Fallback verwendet, wenn für eine:n einzelne:n Nutzer:in keine personalisierte oder neueste Empfehlung berechnet werden kann. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Artikel" }

### Übersicht {#overview}

Dies ist eine Übersicht über die von Ihnen gewählte Empfehlungskonfiguration, einschließlich des Zeitpunkts, zu dem die Empfehlung zuletzt aktualisiert wurde.

![Übersichtstabelle für Empfehlungen mit Typ, Katalog, Event-Typ, Name des angepassten Events, Name der Eigenschaft und Datum der letzten Aktualisierung.]({% image_buster /assets/img/item_recs_analytics_3.png %}){: style="max-width:50%" }