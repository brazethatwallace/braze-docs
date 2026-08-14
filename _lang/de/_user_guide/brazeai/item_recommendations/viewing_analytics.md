---
nav_title: Analytics
article_title: "Analytics für Artikel-Empfehlungen"
description: "Erfahren Sie mehr über Analytics für Artikel-Empfehlungen und wie Sie diese in Braze anzeigen können."
page_order: 1.3
---

# Analytics für Artikel-Empfehlungen {#item-recommendation-analytics}

> Erfahren Sie mehr über Analytics für Artikel-Empfehlungen und wie Sie diese in Braze anzeigen können.

## Analytics anzeigen {#view-analytics}

Sie können die Analytics für Ihre Empfehlung einsehen, um zu sehen, welche Artikel den Nutzer:innen empfohlen wurden und wie genau das Empfehlungsmodell war.

1. Gehen Sie zu **Analytics** > **Item Recommendation**.
2. Wählen Sie Ihre Empfehlung aus der Liste aus.

## Verfügbare Metriken {#available-metrics}

### Zielgruppe {#audience}

Diese Metriken beschreiben Ihre Empfehlungszielgruppe. Je nach Empfehlungstyp und verfügbaren Analytics-Daten kann der Abschnitt **Zielgruppe** die Metriken **Precision** und **Coverage** enthalten.

Bei **KI-personalisierten** Empfehlungen zeigt die Karte **Empfehlungstyp** die geschätzte Personalisierungsrate, Nutzer:innen mit dem konfigurierten Event und die Gesamtpopulation an. Bei **Neueste**-Empfehlungen wird der Anteil der Nutzer:innen angezeigt, die **Neueste**-Empfehlungen erhalten, im Vergleich zum **Beliebteste**-Fallback. **Beliebteste**- und **Trending**-Empfehlungen zeigen keine Aufschlüsselung des Empfehlungstyps auf Nutzer:innen-Ebene.

![Metriken zur Empfehlungszielgruppe mit Precision, Coverage und Empfehlungstypen, aufgeteilt in personalisierte und beliebteste Artikel.]({% image_buster /assets/img/item_recs_analytics_1.png %}){: style="max-width:80%;"}

Weitere Informationen finden Sie in der folgenden Tabelle:

| Metrik              | Beschreibung |
| ------------------- | ---------- |
| **Precision**           | Der prozentuale Anteil, mit dem das Modell den nächsten Artikel, den Nutzer:innen kaufen, korrekt vorhergesagt hat. Precision hängt stark von Ihrer spezifischen Kataloggröße und -zusammensetzung ab und sollte als Orientierung dafür dienen, wie oft das Modell richtig liegt.<br><br>In bisherigen Tests haben Modelle mit Precision-Werten zwischen 6–20 % gut abgeschnitten. Diese Metrik wird beim nächsten Neutraining des Modells aktualisiert. |
| **Coverage**            | Welcher Prozentsatz der verfügbaren Artikel im Katalog mindestens einer/einem Nutzer:in empfohlen wird. Bei personalisierten Artikelempfehlungen ist eine höhere Artikelabdeckung zu erwarten als bei den beliebtesten Artikeln. |
| **Personalisierungsrate** | Bei **KI-personalisierten** Empfehlungen der geschätzte Prozentsatz der Nutzer:innen, für die personalisierte Empfehlungen in ihrem Profil gespeichert sind, berechnet anhand der Gesamtzahl der Nutzer:innen, die das konfigurierte Event in den letzten 24 Monaten ausgeführt haben. Nutzer:innen, die das Event ausgeführt haben, aber nicht über genügend Daten verfügen, um eine personalisierte Empfehlung zu generieren, erhalten beim Versand die beliebtesten Artikel als Fallback. |
| **Empfehlungstyp** | Bei **Neueste**-Empfehlungen der Prozentsatz der Nutzer:innen, die **Neueste**-Empfehlungen erhalten, im Vergleich zum **Beliebteste**-Fallback. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zielgruppe" }

### Artikel {#items}

Diese Tabelle enthält Metriken zu Ihren personalisierten, neuesten und beliebtesten Artikeln aus Ihrem Katalog.

![Nebeneinander stehende Tabellen mit Artikeln, die Nutzer:innen zugewiesen wurden, aufgeteilt in personalisierte Empfehlungen und beliebteste Empfehlungen.]({% image_buster /assets/img/item_recs_analytics_2.png %})

Weitere Informationen finden Sie in der folgenden Tabelle:

| Metrik              | Beschreibung |
| ------------------- | ---------- |
| **Personalisierte Artikel**<br><br>**Neueste Artikel** | Diese Spalte listet jeden Artikel im Katalog in absteigender Reihenfolge der Häufigkeit auf, mit der er Nutzer:innen empfohlen wird. Die Spalte zeigt außerdem, wie vielen Nutzer:innen jeder Artikel vom Modell zugewiesen wurde.<br><br>Je nach [Empfehlungstyp]({{site.baseurl}}/user_guide/brazeai/item_recommendations) werden entweder **personalisierte** oder **neueste** Artikel aufgelistet. |
| **Beliebteste Artikel** | Diese Spalte listet jeden Artikel im Katalog in absteigender Reihenfolge der Beliebtheit auf. Beliebtheit bezieht sich hier auf die Artikel im Katalog, mit denen Nutzer:innen im gesamten Workspace am häufigsten interagieren. Die beliebtesten Artikel werden als Fallback verwendet, wenn personalisierte oder neueste Empfehlungen für einzelne Nutzer:innen nicht berechnet werden können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Artikel" }

### Übersicht {#overview}

Dies ist eine Übersicht Ihrer gewählten Empfehlungskonfiguration, einschließlich des Zeitpunkts der letzten Aktualisierung der Empfehlung.

![Übersichtstabelle der Empfehlung mit Typ, Katalog, Event-Typ, Name des angepassten Events, Eigenschaftsname und Datum der letzten Aktualisierung.]({% image_buster /assets/img/item_recs_analytics_3.png %}){: style="max-width:50%" }