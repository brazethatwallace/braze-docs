---
nav_title: Berichte zur Bindung
article_title: Berichte zur Bindung für Campaigns und Canvases
page_order: 9
tool: Reports
page_type: reference
description: "Diese Seite beschreibt, wie Sie die Nutzerbindung für Nutzer:innen messen, die ein ausgewähltes Bindungsereignis in einer bestimmten Campaign oder einem Canvas durchgeführt haben."
---

# Berichte zur Bindung {#retention-reports}

> Die Nutzerbindung ist eine der wichtigsten Metriken für jeden Marketer. Engagierte Nutzer:innen, die immer wieder zurückkehren, zeigen, dass das Unternehmen gesund ist. Mit Braze können Sie die Nutzerbindung direkt auf der **Analytics**-Seite Ihrer Campaign oder Ihres Canvas messen.

{% alert important %}
Berichte zur Bindung sind für API-getriggerte Campaigns nicht verfügbar.
{% endalert %}

## Einen Bindungsbericht ausführen {#running-a-retention-report}

### Schritt 1: Einen Datumsbereich auswählen {#step-1-select-a-date-range}

![Berichtsdatum]({% image_buster /assets/img/date_select_retention.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Beginnen Sie, indem Sie eine beliebige Campaign oder ein Canvas in Ihrem Braze-Dashboard aufrufen und einen Datumsbereich für Ihren Bericht auswählen. Die Auswahl eines geeigneten Datumsbereichs ist entscheidend, da er sich auf die Berichte zur Bindung auswirkt.

Dieser Bericht umfasst alle Nutzer:innen, die die Campaign oder das Canvas während dieses Zeitfensters erstmals betreten haben. Von diesen Nutzer:innen werden die Daten derjenigen, die ihr Bindungsereignis innerhalb des Datumsbereichs durchgeführt haben, im Bericht angezeigt.

Um einen Datumsbereich auszuwählen, navigieren Sie zur **Analytics**-Seite der Campaign oder des Canvas und wählen Sie verschiedene Bereiche aus oder legen Sie einen benutzerdefinierten Bereich für Ihren Bericht fest.

### Schritt 2: Ein Bindungsereignis auswählen {#step-2-select-a-retention-event}

{% tabs %}
{% tab Campaign %}

Gehen Sie als Nächstes zum Abschnitt **Campaign Retention**. Die Campaign-Bindung zeigt Ihnen die Rate, mit der Nutzer:innen, die diese bestimmte Campaign erhalten haben, ein Bindungsereignis (von Ihnen im Bindungsbericht festgelegt) innerhalb von 30 Tagen nach Erhalt der Campaign durchgeführt haben.

{% endtab %}
{% tab Canvas %}

Wählen Sie als Nächstes **Analyze Variants** aus. Von hier aus können Sie Ihre Varianten analysieren, Ihren Funnel-Bericht einsehen und Ihren Bindungsbericht anzeigen. Die Canvas-Bindung zeigt Ihnen die Rate, mit der Nutzer:innen, die dieses bestimmte Canvas erhalten haben, ein Bindungsereignis (von Ihnen im Bindungsbericht festgelegt) innerhalb von 30 Tagen nach Erhalt des Canvas durchgeführt haben.

{% endtab %}
{% endtabs %}

![Ein Bindungsereignis auswählen]({% image_buster /assets/img/retention_1.png %}){: style="max-width:80%"}

### Schritt 3: Den Bericht generieren {#step-3-generate-the-report}

Nachdem Sie ein Bindungsereignis ausgewählt haben, wählen Sie **Run Report**, um die Abfrage zu starten.

![Bericht ausführen]({% image_buster /assets/img/retention_2.png %}){: style="max-width:80%"}

Diese Abfrage kann je nach Datenmenge einige Minuten dauern. Wenn es zu lange dauert, werden Sie durch eine Benachrichtigung aufgefordert, das Laden des Berichts erneut zu versuchen. Möglicherweise müssen Sie bis zu fünf Minuten warten, bevor der Bericht geladen wird.

Nachdem der Bericht generiert wurde, kann er für 24 Stunden nicht erneut mit demselben Bindungsereignis ausgeführt werden. Sie sehen immer einen Zeitstempel, wann der Bericht zuletzt generiert wurde, sowie eine Option zur Neugenerierung, wenn mehr als ein Tag vergangen ist. Sie können jedoch das Bindungsereignis ändern und den Bericht erneut ausführen, um die Auswirkungen der Campaign auf verschiedene KPIs zu untersuchen.

Der Bericht listet nur Tage auf, an denen die Campaign oder das Canvas Nachrichten gesendet hat. Bei einigen Campaigns und Canvases kann das bedeuten, dass der Bericht nur einen Tag anzeigt, wenn die Nachricht nur einmal gesendet wurde. Bei wiederkehrenden oder getriggerten Campaigns sehen Sie möglicherweise mehrere Tage in der Tabelle.

{% tabs %}
{% tab Campaign %}

![Vollständiger Bericht]({% image_buster /assets/img/campaign_retention3.png %})

{% endtab %}
{% tab Canvas %}

![Vollständiger Bericht]({% image_buster /assets/img/canvas_retention_report.png %}){: style="max-width:70%"}

{% endtab %}
{% endtabs %}

## Erklärung des Berichts {#report-explanation}

Der Bindungsbericht bietet sowohl eine Rolling-Retention- als auch eine Range-Retention-Formel. Um Ihren Campaign- oder Canvas-Bericht mit einem dieser Bindungstypen anzuzeigen, wählen Sie entweder **Rolling Retention** oder **Range Retention** für Ihren **Type of Retention** aus.

### Rolling Retention {#rolling-retention}

Rolling Retention misst, wie viele Nutzer:innen zurückkehren und das Bindungsereignis an oder nach einem der oben im Bericht aufgeführten Tage durchführen. Wenn also eine Nutzerin oder ein Nutzer zwischen Tag drei und sieben eine Sitzung gestartet hat, wird diese Person in den Spalten „3 Tage“, „1 Tag“ und „0 Tage“ als gebunden gezählt. Alle Nutzer:innen, die nach der 30-Tage-Marke ab dem Versand der Campaign oder des Canvas als gebunden gezählt werden, erscheinen in der Spalte „30 Tage“ in dieser Zeile.

Nutzer:innen, die das Ereignis mehrmals innerhalb eines Zeitfensters von 30+ Tagen durchführen, werden in mehreren Zeitrahmen gezählt. Wenn beispielsweise eine Nutzerin oder ein Nutzer nach einem Tag eine Sitzung abschließt, wird die Person in den Spalten für >0 und >1 hochgezählt. Wenn sie dann nach drei Tagen das Ereignis erneut durchführt, wird sie erneut in den vorherigen Spalten (>0 und >1) hochgezählt, was dazu führen kann, dass die Bindungsrate 100 % übersteigt.

#### So lesen Sie Rolling-Retention-Berichte {#how-to-read-rolling-retention-reports}

Die Interpretation des Bindungsbericht-Charts für eine Tag-drei-Spalte lautet: Y % oder Y Nutzer:innen (je nach gewählter Einheit) haben das Ereignis drei oder mehr Tage nach Erhalt der Campaign an Tag Z durchgeführt.

![Rolling-Bericht]({% image_buster /assets/img/campaign_retention3.png %})

Ein weiteres Beispiel: Bezogen auf die Tabelle im vorherigen Bild haben am 25. März insgesamt 38 Nutzer:innen das Bindungsereignis durchgeführt. Die Tag-null-Bindung betrug 68,42 %, was bedeutet, dass 68,42 % der Nutzer:innen das Bindungsereignis null oder mehr Tage (an Tag null oder später) nach Erhalt der Campaign durchgeführt haben. Die Tag-sieben-Bindung betrug 57,89 %, was bedeutet, dass 57,89 % der Nutzer:innen das Ereignis sieben oder mehr Tage (an Tag sieben oder später) nach Erhalt der Campaign durchgeführt haben.

Diese Informationen können nützlich sein, wenn Sie wissen möchten, welcher Prozentsatz der Nutzer:innen Ihr Produkt 30+ Tage nach der ersten Nutzung verwendet hat und welcher nicht. Ein Prozent- oder Zahlenwert in der Tag-30-Spalte gibt Ihnen den Prozentsatz der Nutzer:innen an, die an Tag 30 oder danach zurückgekehrt sind.

### Range Retention {#range-retention}

Range Retention misst, wie viele Nutzer:innen innerhalb der oben im Bericht aufgeführten Tagesbereiche zurückkehren. Wenn also eine Nutzerin oder ein Nutzer zwischen Tag drei und sieben eine Sitzung gestartet hat und dann erneut an Tag 13, wird die Person sowohl unter „Tag 3-7“ als auch unter „Tag 7-14“ als gebunden gezählt.

#### So lesen Sie Range-Retention-Berichte {#how-to-read-range-retention-reports}

Range-Berichte gehören zu den intuitivsten Berichten. Sie geben klar an, welcher Prozentsatz der Nutzer:innen einer Kohorte das Bindungsereignis innerhalb eines bestimmten Datumsbereichs durchgeführt hat. Im folgenden Bild beispielsweise haben in der Kohorte „Alle Nutzer:innen“ im Datumsbereich „Tag 0 (0-24 Std.)“ 35,71 % der Kohorte das Bindungsereignis durchgeführt. Wenn Nutzer:innen mehrere Bindungsereignisse in mehreren Datumsbereichen durchführen, werden sie für jeden Bereich als gebunden gezählt.

![Bindungsbericht]({% image_buster /assets/img/range_retention.png %})

### Komponenten des Bindungsberichts {#retention-report-components}

- **Spalte „Nutzer:innen“**: Der angezeigte Wert ist die Anzahl der eindeutigen Nutzer:innen, die die Startaktion innerhalb des ausgewählten Zeitraums durchgeführt haben; die Anzahl der Nutzer:innen für den aktuellen Tag wird ausgeschlossen, da sie noch berechnet wird.
- **Zeilen „Kohorte Z“**: Zeigt die Tage an, an denen die Campaign oder das Canvas Nachrichten gesendet hat.
- **Spalten „Tag X“**: Tage im Bereich von 0 bis 30 Tagen in verschiedenen Intervallen.
- **Zeile „Alle Nutzer:innen“**: Auch als Berichtszusammenfassungszeile bekannt, fasst sie die Bindungsdaten für den gesamten Zeitraum zusammen. Beachten Sie, dass die Ergebnisse von Nutzer:innen, die die Campaign oder das Canvas in mehreren Kohorten erhalten haben, hier doppelt gezählt werden.
- **Prozentsätze/Zahlen**: Zeigt den Prozentsatz oder die Anzahl der Nutzer:innen, die das Ereignis X oder mehr Tage nach Erhalt der Campaign oder des Canvas an Tag Z durchgeführt haben. Diese Prozentsätze sind gewichtete Durchschnittsprozentsätze. Unvollständige Werte werden durch ein Sternchen gekennzeichnet.
- **Datumsbereich**: Wird auf der **Details**-Seite der Campaign oder des Canvas festgelegt. Der Datumsbereich umfasst alle Nutzer:innen, die die Campaign oder das Canvas während dieses Zeitfensters erhalten haben. Von diesen Nutzer:innen werden die Daten derjenigen, die ihr Bindungsereignis innerhalb des Datumsbereichs durchgeführt haben, im Bericht angezeigt.
- **Einheiten**: Sie können die Einheiten zwischen dem Prozentsatz der Nutzer:innen und der Anzahl der Nutzer:innen über die Chart-Steuerung umschalten. Bestimmte Einheiten können bei der Beurteilung der Auswirkungen einer Campaign oder eines Canvas aussagekräftiger sein.
- **Farbzuordnung**: In Ihrem Bindungsbericht werden höheren Prozentsätzen oder Nutzer:innenzahlen dunklere Blautöne zugewiesen. Niedrigeren Prozentsätzen oder Nutzer:innenzahlen werden hellere Blautöne zugewiesen. Dies dient der besseren Visualisierung der Daten.
- **Bindungsbericht-Diagramm**: Dieses Diagramm fasst die Ergebnisse für alle Kohorten im ausgewählten Datumsbereich zusammen.

### Performance nach Variante {#performance-by-variant}

Die Anzeige Ihres Bindungsberichts nach Variante ermöglicht es Ihnen, die Rolling Retention für jede Variante oder Nachrichtenvariante im ausgewählten Zeitraum sowie die Kontrollgruppe zu vergleichen. Dieser Bericht kann angezeigt werden, indem Sie **Show Performance For** auf **By Variant** umschalten.

Einige Anwendungsfälle für die Anzeige der Performance nach Variante:

- Haben einige Varianten oder Experimente Ergebnisse, die wie verschwendeter Aufwand erscheinen oder keine statistische Signifikanz aufweisen? Schauen Sie noch einmal genauer hin und prüfen Sie, ob eine der Varianten eine längerfristige Auswirkung hatte.
- Sehen Sie, wie die Bindung aussieht, wenn Sie keine Nachricht senden, indem Sie die Bindungsdaten der Kontrollgruppe untersuchen.

{% tabs %}
{% tab Campaign %}

![Ansicht nach Variante]({% image_buster /assets/img/variant_view.png %})

{% endtab %}
{% tab Canvas %}

![Ansicht nach Variante]({% image_buster /assets/img/variant_view_canvas.png %})

{% endtab %}
{% endtabs %}

#### Komponenten des Bindungsberichts nach Variante {#retention-report-by-variant-components}

- **Datumsbereich**: Wird auf der **Details**-Seite der Campaign oder des Canvas festgelegt. Der Datumsbereich umfasst alle Nutzer:innen, die die Campaign oder das Canvas während dieses Zeitfensters erhalten haben. Von diesen Nutzer:innen werden die Daten derjenigen, die ihr Bindungsereignis innerhalb des Datumsbereichs durchgeführt haben, im Bericht angezeigt. Jeden Tag werden die Bindungsrate, die prozentuale Veränderung gegenüber der Kontrollgruppe und die Konfidenz gemessen.
- **Bindungsrate**: Zeigt die Bindungsrate nach Variante. Die Bindungsrate entspricht der Anzahl der Nutzer:innen, die das Bindungsereignis durchgeführt haben, geteilt durch die Gesamtzahl der Nutzer:innen, die die Campaign oder das Canvas erhalten haben.
- **Prozentuale Veränderung gegenüber der Kontrollgruppe**: Quantifiziert die prozentuale Veränderung pro Variante im Vergleich zur Kontrollgruppe.
- **Konfidenz**: {% multi_lang_include analytics/metrics.md metric='Confidence' %} Braze vergleicht die Konversionsrate jeder Variante mit der Konversionsrate der Kontrollgruppe mithilfe eines statistischen Verfahrens namens Z-Test, um einen [Konfidenz]({{site.baseurl}}/user_guide/messaging/ab_testing#understanding-confidence)-Prozentsatz zu berechnen.
- **Einheiten**: Sie können die Einheiten zwischen dem Prozentsatz der Nutzer:innen und der Anzahl der Nutzer:innen über die Chart-Steuerung umschalten. Bestimmte Einheiten können bei der Beurteilung der Auswirkungen einer Campaign oder eines Canvas aussagekräftiger sein.
- **Varianten-Diagramm**: Dieses Diagramm fasst die Ergebnisse nach Variante für den ausgewählten Datumsbereich zusammen.

## Worauf Sie in Ihren Bindungsberichten achten sollten {#things-to-look-for-in-your-retention-reports}

Berichte zur Bindung sind einfach zu generieren, aber schwierig zu interpretieren und darauf zu reagieren. Die folgenden Themen und Fragen können Ihnen helfen, mehr aus Ihren Berichten zur Bindung herauszuholen.

- Berücksichtigen Sie Wochentags-Trends bei wiederkehrenden Campaigns (z. B.: Schneiden Montags-Kohorten besser ab als Samstags-Kohorten?).
- Wo beginnt die Wirkung nachzulassen? Dies könnte ein Signal dafür sein, dass eine neue Campaign oder ein neues Canvas benötigt wird, das Nutzer:innen zu diesem Zeitpunkt anspricht, um die Bindung weiter zu stärken.
- Beobachten Sie eine Messaging-Ermüdung?
- Hatte eine bestimmte Optimierung, die Sie vor X Tagen an einer Campaign oder einem Canvas vorgenommen haben, eine positive Auswirkung?