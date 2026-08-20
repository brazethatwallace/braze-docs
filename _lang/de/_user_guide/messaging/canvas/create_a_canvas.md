---
nav_title: Canvas erstellen
article_title: Canvas erstellen
page_order: 1
description: "Erfahren Sie, wie Sie ein Canvas erstellen und starten: Grundlagen einrichten, Entry-Zeitplan, Zielgruppe, Sendeeinstellungen, Journey aufbauen und mehr."
tool: Canvas
search_rank: 1
---

# Canvas erstellen {#create-a-canvas}

> Dieser Referenzartikel behandelt die notwendigen Schritte zum Erstellen, Pflegen und Testen eines Canvas. Folgen Sie dieser Anleitung oder schauen Sie sich unseren [Braze-Lernkurs zu Canvas](https://learning.braze.com/quick-overview-canvas-setup) an. Sie können auch mit einem [Braze-Canvas-Template]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) starten, um Ihre Einrichtung zu beschleunigen. Weitere Informationen finden Sie unter [Canvas-Templates]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates). Um ein Canvas aus einer Beschreibung in natürlicher Sprache zu entwerfen, nutzen Sie [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#canvases).

{% details Erweitern für Details zum ursprünglichen Canvas-Editor %}
Sie können keine Canvases mehr mit dem ursprünglichen Canvas-Editor erstellen oder duplizieren. Braze empfiehlt, [Ihre Canvases zu klonen]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases), um den aktuellsten Editor zu verwenden.
{% enddetails %}

## Schritt 1: Ein neues Canvas einrichten {#step-1-set-up-a-new-canvas}

Gehen Sie zunächst zu **Messaging** > **Canvas** und wählen Sie dann **Canvas erstellen**.

Der Canvas-Builder führt Sie Schritt für Schritt durch die Einrichtung Ihres Canvas – von der Benennung über die Festlegung von Konversions-Events bis hin zur Einbindung der gewünschten Nutzer:innen in Ihre Customer Journey. Wählen Sie die folgenden Tabs aus, um zu sehen, welche Einstellungen Sie für jeden Builder-Schritt anpassen können.

{% tabs local %}
  {% tab Grundlagen %}
    Hier richten Sie die Grundlagen Ihres Canvas ein:
    - Benennen Sie Ihr Canvas
    - Fügen Sie Teams hinzu
    - Fügen Sie Tags hinzu
    - Weisen Sie Konversions-Events zu und wählen Sie deren Event-Typen und Fristen

    Erfahren Sie mehr über den [Schritt „Grundlagen“](#step-11-start-with-your-canvas-basics).
  {% endtab %}
  {% tab Eingangsplan %}
    Hier legen Sie fest, wie und wann Ihre Nutzer:innen in Ihr Canvas eintreten:
    - Geplant: Dies ist ein zeitbasierter Canvas-Eintritt
    - Aktionsbasiert: Ihre Nutzer:innen treten in Ihr Canvas ein, nachdem sie eine definierte Aktion ausgeführt haben
    - API-getriggert: Verwenden Sie eine API-Anfrage, um Nutzer:innen in Ihr Canvas einzutragen

    Erfahren Sie mehr über den [Schritt „Eingangsplan“](#step-12-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Zielgruppe %}
    Hier wählen Sie Ihre Zielgruppe aus:
    - Erstellen Sie Ihre Zielgruppe, indem Sie Segments und Filter hinzufügen
    - Verfeinern Sie den Canvas-Wiedereintritt und die Eintritts-Limits
    - Sehen Sie eine Zusammenfassung Ihrer Zielgruppe

    Erfahren Sie mehr über den [Schritt „Zielgruppe“](#step-13-set-your-target-entry-audience).
  {% endtab %}
  {% tab Sendeeinstellungen %}
    Hier wählen Sie Ihre Canvas-Sendeeinstellungen aus:
    - Wählen Sie Ihre Abo-Einstellungen
    - Legen Sie ein Rate-Limit für Ihre Canvas-Nachrichten fest
    - Aktivieren und konfigurieren Sie Ruhezeiten

    Erfahren Sie mehr über den [Schritt „Sendeeinstellungen“](#step-14-select-your-send-settings).
  {% endtab %}
  {% tab Canvas erstellen %}
    Hier erstellen Sie Ihr Canvas.

    Erfahren Sie, wie Sie mit dem Canvas-Builder [Ihr Canvas erstellen](#step-2-build-your-canvas).
  {% endtab %}
  {% tab Zusammenfassung %}
    Hier finden Sie die Zusammenfassung Ihrer Canvas-Details. Wenn Sie den [Canvas-Genehmigungsworkflow]({{site.baseurl}}/user_guide/messaging/governance/approvals) aktiviert haben, können Sie die aufgelisteten Canvas-Details vor dem Start genehmigen.

  {% endtab %}
{% endtabs %}

### Schritt 1.1: Beginnen Sie mit den Canvas-Grundlagen {#step-11-start-with-your-canvas-basics}

Hier benennen Sie Ihr Canvas, weisen [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) zu und erstellen oder fügen [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu. Sie können auch Konversions-Events für das Canvas zuweisen.

{% alert tip %}
Versehen Sie Ihre Canvases mit Tags, damit sie leicht zu finden sind und Berichte daraus erstellt werden können. Wenn Sie beispielsweise den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder) verwenden, können Sie nach bestimmten Tags filtern.
{% endalert %}

![Die Canvas-Detailseite mit Feldern für den Canvas-Namen, die Beschreibung, den Standort und Tags.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

#### Konversions-Events auswählen {#choose-conversion-events}

Wählen Sie Ihren Konversions-Event-Typ und dann die Konversionen aus, die aufgezeichnet werden sollen. Diese [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) messen die Effizienz Ihres Canvas.

![Primäres Konversions-Event A mit dem Konversions-Event-Typ „Kauf tätigen“, um Konversionen für Nutzer:innen aufzuzeichnen, die innerhalb einer dreitägigen Konversionsfrist einen beliebigen Kauf tätigen.]({% image_buster /assets/img/add_canvas_conversions.png %})

Wenn Ihr Canvas mehrere Varianten oder eine Kontrollgruppe hat, verwendet Braze dieses Konversions-Event, um die beste Variante zur Erreichung dieses Konversionsziels zu bestimmen. Mit derselben Logik können Sie mehrere Konversions-Events erstellen.

### Schritt 1.2: Bestimmen Sie Ihren Canvas-Eingangsplan {#step-12-determine-your-canvas-entry-schedule}

Sie können eine von drei Möglichkeiten wählen, wie Nutzer:innen in Ihr Canvas eintreten können.

#### Eingangsplan-Typen {#entry-schedule-types}

{% tabs local %}
{% tab Geplante Zustellung %}
Bei der geplanten Zustellung treten Nutzer:innen nach einem Zeitplan ein, ähnlich wie Sie eine Campaign planen würden. Sie können Nutzer:innen in ein Canvas eintragen, sobald es gestartet wird, sie zu einem zukünftigen Zeitpunkt in Ihre Journey eintreten lassen oder auf wiederkehrender Basis (täglich, wöchentlich oder monatlich).

Wenn Sie einen monatlich wiederkehrenden Zeitplan auswählen, beachten Sie, dass einige Monate den ausgewählten Tag möglicherweise nicht haben. Nehmen wir zum Beispiel an, Sie haben ein Canvas so eingerichtet, dass es monatlich am 31. Tag gesendet wird. In diesem Szenario sendet Braze am letzten Tag des jeweiligen Monats, z. B. am 30. April, da der 31. April nicht existiert.

In diesem Beispiel treten Nutzer:innen basierend auf den zeitbasierten Optionen jeden Dienstag um 12:00 Uhr in ihrer Ortszeit wöchentlich in dieses Canvas ein, beginnend am 14. November 2025 bis zum 31. Dezember 2025.

![Die Seite „Eingangsplan“ mit dem Typ „Geplant“. Aufgrund der Auswahl werden zeitbasierte Optionen angezeigt, einschließlich Häufigkeit, Startzeit, Wiederholung, Tage und mehr.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})

Bei der Zustellung in der Ortszeit bewertet Braze die Eintritts-Berechtigung zweimal: zuerst zur Samoa-Zeit (UTC+13) am geplanten Tag und dann zur Ortszeit der Nutzer:innen. Ein:e Nutzer:in muss beide Prüfungen bestehen, um in das Canvas einzutreten. Wenn Ihre Eingangsfilter relative Zeitfenster verwenden (z. B. „vor mehr als 2 Tagen“), ist der 24-Stunden-Zeitraum zum Zeitpunkt der ersten Prüfung möglicherweise noch nicht abgelaufen, was dazu führen kann, dass Nutzer:innen einen Tag zu spät eintreten. Um dies zu vermeiden, verwenden Sie ein breiteres Zeitfenster, z. B. mindestens zwei Tage. Weitere Details finden Sie unter [Wann bewertet Braze Nutzer:innen für die Zustellung in der Ortszeit?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery)
{% endtab %}
{% tab Aktionsbasierte Zustellung %}
Bei der aktionsbasierten Zustellung treten Nutzer:innen in das Canvas ein und beginnen Nachrichten zu erhalten, wenn sie bestimmte Aktionen ausführen, z. B. Ihre App öffnen, einen Kauf tätigen oder ein angepasstes Event triggern.

Sie können weitere Aspekte des Canvas-Verhaltens über das Fenster **Eingangs-Zielgruppe** steuern, einschließlich Regeln für die Wiederberechtigung und Frequency-Capping-Einstellungen. Beachten Sie, dass die aktionsbasierte Zustellung für Canvas-Komponenten mit In-App-Nachrichten nicht verfügbar ist.

![Ein Beispiel für aktionsbasierte Zustellung. Nutzer:innen treten in das Canvas ein, wenn sie einen Kauf tätigen, mit einem Eintritts-Fenster, das am 10. Juni 2025 um 13:30 Uhr beginnt.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

{% alert note %}
**Mit Canvas-Schritt interagieren** ist nicht als aktionsbasierter Eingangs-Trigger für Canvases verfügbar. Es kann nur als Trigger für Campaigns verwendet werden. Um ein Canvas von einem anderen zu triggern, verwenden Sie die Canvas-Komponente [An Ziel senden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) oder erstellen Sie einen [Braze-zu-Braze-Webhook]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook#trigger-a-second-canvas-from-an-initial-canvas), der den Endpunkt `/canvas/trigger/send` aufruft.
{% endalert %}

{% alert important %}
Wenn Ihr aktionsbasiertes Canvas Nachrichten früher als erwartet sendet, überprüfen Sie, ob Ihr angepasster Event-Zeitstempel mit der aktuellen Zeit gesendet wird und nicht mit einer rückdatierten Zeit. Wenn beispielsweise ein aktionsbasiertes Canvas eine dreistündige Verzögerung nach Ausführung eines angepassten Events durch eine:n Nutzer:in hat, verwendet Braze den mit dem angepassten Event gesendeten Zeitstempel, um diese Verzögerung zu bewerten. Wenn der Zeitstempel um mehr als drei Stunden rückdatiert ist, behandelt Braze die Verzögerung als bereits abgelaufen und sendet die Nachricht sofort.
{% endalert %}
{% endtab %}
{% tab API-getriggerte Zustellung %}
Bei der API-getriggerten Zustellung treten Nutzer:innen in Ihr Canvas ein und beginnen Nachrichten zu erhalten, nachdem sie über den [Endpunkt `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) via API hinzugefügt wurden. Im Dashboard finden Sie ein Beispiel für eine cURL-Anfrage, die dies durchführt, sowie die Möglichkeit, optionale [`context`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)-Daten über das [Context-Objekt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) zuzuweisen.

![Ein Beispiel für API-getriggerte Zustellung mit einer Canvas-ID und einem Beispiel einer cURL-Anfrage.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

Sie können die folgenden Endpunkte für die API-getriggerte Zustellung verwenden:
- [POST: Canvas-Nachrichten über API-getriggerte Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [POST: API-getriggerte Canvases planen]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)
- [POST: Geplante API-getriggerte Canvases aktualisieren]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases)
{% endtab %}
{% endtabs %}

Nachdem Sie Ihre Zustellungsmethode ausgewählt haben, passen Sie die Einstellungen an Ihren Anwendungsfall an und fahren Sie dann mit der Festlegung Ihrer Zielgruppe fort.

{% details Deduplizierungsverhalten für Canvases mit dem Original-Editor %}
Sollte das Fenster für die Wiederberechtigung kürzer sein als die maximale Dauer des Canvas, kann ein:e Nutzer:in erneut eintreten und Nachrichten von mehr als einer Komponente erhalten. Im Grenzfall, dass der Wiedereintritt einer Nutzerin oder eines Nutzers dieselbe Komponente wie der vorherige Eintritt erreicht, dedupliziert Braze die Nachrichten dieser Komponente.

Wenn ein:e Nutzer:in erneut in das Canvas eintritt, dieselbe Komponente wie beim vorherigen Eintritt erreicht und für eine In-App-Nachricht bei jedem Eintritt berechtigt ist, erhält die Person die Nachricht zweimal (abhängig von der In-App-Nachrichten-Priorität), solange sie zweimal eine Sitzung erneut öffnet.
{% enddetails %}

### Schritt 1.3: Legen Sie Ihre Eingangs-Zielgruppe fest {#step-13-set-your-target-entry-audience}

Nur Nutzer:innen, die Ihren definierten Kriterien entsprechen, können im Schritt **Zielgruppe** in die Journey eintreten, d. h. Braze bewertet die Zielgruppe auf Berechtigung zuerst, **bevor** Nutzer:innen in die Canvas-Journey eintreten. Wenn Sie beispielsweise neue Nutzer:innen ansprechen möchten, können Sie ein Segment von Nutzer:innen auswählen, die Ihre App vor weniger als einer Woche zum ersten Mal verwendet haben.

{% alert important %}
In Workspaces mit mehreren Apps wird die Berechtigung der Canvas-Eingangs-Zielgruppe (einschließlich Segments und Filter) nur beim Eintritt der Nutzer:innen in das Canvas bewertet, nicht bei einzelnen Nachrichten-Schritten. Wenn Ihr Workspace mehrere Apps hat und Sie sicherstellen müssen, dass Nachrichten-Schritte nur Nutzer:innen einer bestimmten App ansprechen, verwenden Sie einen der folgenden Ansätze in jedem Nachrichten-Schritt:
- Aktivieren Sie **Zielgruppe beim Nachrichtenversand validieren** in den [Zustellungsvalidierungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) des Nachrichten-Schritts und fügen Sie app-spezifische Segments oder Filter hinzu.
- Verwenden Sie Liquid, um das Zielgerät oder die App zum Sendezeitpunkt zu prüfen.

Ohne diese Schutzmaßnahmen können Nutzer:innen, die sich in einer App für die Journey qualifiziert haben, Nachrichten erhalten, die für eine andere App bestimmt sind, wenn sie auch andere Apps in Ihrem Workspace verwenden.
{% endalert %}

Unter **Eingangskontrollen** können Sie die Anzahl der Nutzer:innen begrenzen, die jedes Mal eintreten, wenn das Canvas planmäßig ausgeführt wird. Für API-trigger-basierte und aktionsbasierte Canvases gilt dieses Limit zu jeder UTC-Stunde.

{% multi_lang_include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

#### Ihre Zielgruppe testen {#testing-your-audience}

Nachdem Sie Segments und Filter zu Ihrer Zielgruppe hinzugefügt haben, können Sie testen, ob Ihre Zielgruppe wie erwartet eingerichtet ist, indem Sie [eine:n Nutzer:in nachschlagen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), um zu bestätigen, ob sie den Zielgruppenkriterien entsprechen.

![Das Feld „Nutzer:innen-Suche“, mit dem Sie nach externer Nutzer:innen-ID oder Braze-ID suchen können.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Eingangskontrollen auswählen {#selecting-entry-controls}

Eingangskontrollen bestimmen, ob Nutzer:innen erneut in ein Canvas eintreten dürfen. Sie können auch die Anzahl der Personen begrenzen, die potenziell in dieses Canvas eintreten, mit einer ausgewählten Kadenz abhängig von Ihrem Eingangsplan-Typ:

- **Geplant:** Lebensdauer des Canvas oder jedes Mal, wenn das Canvas geplant ist
- **Aktionsbasiert:** Stündlich, täglich oder die Lebensdauer des Canvas
- **API-getriggert:** Stündlich, täglich oder die Lebensdauer des Canvas

Wenn Sie beispielsweise ein geplantes Canvas haben und **Eingangsvolumen begrenzen** auswählen und das Feld **Maximale Eintritte** auf 500.000 Nutzer:innen mit **Jedes Mal, wenn Canvas geplant ist** als Limit-Kadenz setzen, sendet das Canvas nur an 500.000 Nutzer:innen pro geplantem Versand.

![Die Seite „Eingangskontrollen“ mit Kontrollkästchen für „Nutzer:innen erlauben, erneut in Canvas einzutreten“ und „Eingangsvolumen begrenzen“.]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze empfiehlt nicht, **Jedes Mal, wenn Canvas geplant ist** für IP-Warming auszuwählen, da dies zu erhöhten Sendevolumen führen kann.
{% endalert %}

#### Ausstiegskriterien festlegen {#setting-exit-criteria}

Das Festlegen der [Ausstiegskriterien]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) bestimmt, welche Nutzer:innen ein Canvas verlassen sollen. Wenn ein:e Nutzer:in das Ausnahme-Event ausführt oder den Segments und Filtern entspricht, erhält sie keine weiteren Nachrichten.

#### Zielpopulation berechnen {#calculating-target-population}

Im Abschnitt **Zielpopulation** können Sie eine Zusammenfassung Ihrer Zielgruppe einsehen, z. B. Ihre ausgewählten Segments und zusätzlichen Filter, sowie eine Aufschlüsselung, wie viele Nutzer:innen pro Messaging-Kanal erreichbar sind. Um die genaue Anzahl der erreichbaren Nutzer:innen in Ihrer Zielgruppe anstelle der Standardschätzung zu berechnen, wählen Sie [Exakte Statistiken berechnen]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#calculating-exact-statistics).

Beachten Sie Folgendes:

- Die Berechnung exakter Statistiken kann einige Minuten dauern. Diese Funktion berechnet die exakten Statistiken nur auf Segment-Ebene, nicht auf Filter- oder Filtergruppen-Ebene.
- Während die exakten Statistiken geladen werden, kann eine gerundete Schätzung angezeigt werden. Die exakte Zahl erscheint im Abschnitt **Erreichbare Nutzer:innen**, wenn sie geladen ist. Sie können **Zusätzliche Statistiken anzeigen** auswählen, um eine detaillierte Aufschlüsselung zu erhalten.
- Bei großen Segments ist es normal, dass selbst bei der Berechnung exakter Statistiken leichte Abweichungen auftreten. Die Genauigkeit dieser Funktion liegt bei 99,999 % oder höher.

Um zusätzliche Statistiken anzuzeigen, wie z. B. den durchschnittlichen Lifetime-Umsatz für angesprochene Nutzer:innen, wählen Sie **Zusätzliche Statistiken anzeigen**.

![Aufschlüsselung der Zielpopulation mit der Option, exakte Statistiken zu berechnen.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

#### Warum die Zielgruppen-Anzahl von der Anzahl erreichbarer Nutzer:innen abweichen kann {#why-the-target-audience-count-could-differ-from-the-reachable-users-count}

{% multi_lang_include audience/segments.md section='Differing audience size' %}

### Schritt 1.4: Wählen Sie Ihre Sendeeinstellungen {#step-14-select-your-send-settings}

Wählen Sie **Sendeeinstellungen**, um Ihre Abo-Einstellungen zu bearbeiten, Rate-Limiting zu aktivieren und [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) einzuschalten. Durch die Aktivierung von [Rate-Limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting) oder [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping) können Sie den Marketing-Druck auf Ihre Nutzer:innen verringern und sicherstellen, dass Sie sie nicht mit zu vielen Nachrichten überhäufen.

Für Canvases, die auf E-Mail- und Push-Kanäle abzielen, möchten Sie Ihr Canvas möglicherweise so einschränken, dass nur Nutzer:innen, die ausdrücklich ein Opt-in gegeben haben, die Nachricht erhalten (unter Ausschluss von abonnierten oder abgemeldeten Nutzer:innen). Nehmen wir zum Beispiel an, Sie haben drei Nutzer:innen mit unterschiedlichem Opt-in-Status:

{% multi_lang_include messaging/intelligent_channel_user_examples.md %}

Setzen Sie dazu die **Abo-Einstellungen** auf „Dieses Canvas nur an Nutzer:innen mit Opt-in senden“. Diese Option stellt sicher, dass nur Nutzer:innen mit Opt-in Ihre E-Mail erhalten, und Braze sendet Ihren Push standardmäßig nur an Nutzer:innen, die Push-fähig sind.

Diese Abo-Einstellungen werden pro Schritt angewendet, d. h. sie haben keine Auswirkung auf die Eingangs-Zielgruppe. Diese Einstellung wird also verwendet, um die Berechtigung einer Nutzerin oder eines Nutzers für den Empfang jedes Canvas-Schritts zu bewerten.

{% alert important %}
Fügen Sie bei dieser Konfiguration keine Filter in den Schritt **Zielgruppe** ein, die die Zielgruppe auf einen einzelnen Kanal beschränken (z. B. `Foreground Push Enabled = True` oder `Email Subscription = Opted-In`).
{% endalert %}

Sie können [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) (die Zeit, in der Ihre Nachrichten nicht gesendet werden) für Ihr Canvas festlegen. Aktivieren Sie **Ruhezeiten aktivieren** in Ihren **Sendeeinstellungen**. Wählen Sie dann Ihre Ruhezeiten in der Ortszeit Ihrer Nutzer:innen und ob die Nachricht abgebrochen oder zum nächsten verfügbaren Zeitpunkt gesendet werden soll.

Wenn **Zum nächsten verfügbaren Zeitpunkt senden** ausgewählt ist, unterdrücken die Ruhezeiten die Nachricht und senden sie zum nächsten verfügbaren Zeitpunkt außerhalb der Ruhezeiten. Nehmen wir zum Beispiel an, die Ruhezeiten sind so eingerichtet, dass Nachrichten zwischen 11:30 Uhr und 14:30 Uhr in der Ortszeit der Nutzer:innen nicht gesendet werden, und ein:e Nutzer:in erreicht einen Nachrichten-Schritt um 11:35 Uhr. Da diese Zeit innerhalb der Ruhezeiten liegt, wird die Nachricht noch nicht gesendet, und die Person erhält den Nachrichten-Schritt um 14:30 Uhr, also nach den Ruhezeiten.

![Die Seite „Ruhezeiten“ mit einem Kontrollkästchen zum Aktivieren der Ruhezeiten. Wenn aktiviert, können Startzeit, Endzeit und Fallback-Verhalten festgelegt werden.]({% image_buster /assets/img/quiet_hours.png %})

## Schritt 2: Canvas erstellen {#step-2-build-your-canvas}

{% alert tip %}
Sparen Sie Zeit und optimieren Sie Ihre Canvas-Erstellung, indem Sie [Braze-Canvas-Templates]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) verwenden! Durchsuchen Sie unsere Bibliothek vorgefertigter Templates, um eines zu finden, das zu Ihrem Anwendungsfall passt, und passen Sie es an Ihre spezifischen Anforderungen an. Weitere Informationen finden Sie unter [Canvas-Templates]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates).
{% endalert %}

### Schritt 2.1: Variante hinzufügen {#step-21-add-a-variant}

![Der Button „Variante hinzufügen“ ist ausgewählt und zeigt ein Kontextmenü mit der Option „Variante hinzufügen“.]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Wählen Sie **Variante hinzufügen** und fügen Sie dann eine neue Variante zu Ihrem Canvas hinzu. Varianten stellen eine Journey dar, die Ihre Nutzer:innen durchlaufen, und können mehrere Schritte und Verzweigungen enthalten.

Sie können weitere Varianten hinzufügen, indem Sie den <i class="fas fa-plus-circle"></i> Plus-Button auswählen. Wenn Sie neue Varianten hinzufügen, können Sie anpassen, wie Ihre Nutzer:innen auf diese verteilt werden, sodass Sie verschiedene Engagement-Strategien vergleichen und deren Wirksamkeit analysieren können.

![Zwei Beispielvarianten in einem Braze-Canvas.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
Standardmäßig wird die Canvas-Variantenzuweisung durch einen deterministischen Hash der Nutzer-ID und der Canvas-ID bestimmt (nicht durch die [zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) der Nutzer:innen). Das bedeutet, dass Nutzer:innen bei erneutem Eintritt konsistent derselben Variante zugewiesen werden, solange die Prozentsätze der Variantenverteilung unverändert bleiben. Wenn Sie die Variantenverteilung nach dem Start anpassen, können Nutzer:innen bei erneutem Eintritt in den Canvas einer anderen Variante zugewiesen werden. <br><br>Wenn Sie eine Zuweisung benötigen, die auch bei Änderung der Verteilungsprozentsätze fest bleibt, verwenden Sie eine einzelne Canvas-Variante und leiten Sie Nutzer:innen mit einem [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)-Schritt weiter. Verwenden Sie zu Beginn der Journey einen [Nutzer-Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritt, um eine Zufallszahl in einem angepassten Attribut zu speichern, und filtern Sie dann in den Zielgruppenpfaden nach diesem Attribut.

{% details Für Schritte aufklappen %}

1. Erstellen Sie ein angepasstes Attribut vom Typ **Number**, um Ihre Zufallszahl zu speichern. Benennen Sie es so, dass es leicht zu finden ist, z. B. `lottery_number` oder `random_assignment`. Gehen Sie in Ihrem Dashboard zu **Dateneinstellungen** > **Angepasste Attribute**.<br><br>
2. Verwenden Sie eine einzelne Canvas-Variante (oder fügen Sie denselben Nutzer-Update-Schritt zu jeder Variante hinzu). Fügen Sie einen [Nutzer-Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritt am Anfang der Journey hinzu. Dieser Schritt generiert und speichert die Zufallszahl, bevor Nutzer:innen Ihren Zielgruppenpfade-Schritt erreichen.<br><br>
3. Wählen Sie im Nutzer-Update-Schritt den [Erweiterten JSON-Editor]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor). Verwenden Sie den {% raw %}{% random %}{% endraw %}-Tag, um die Zahl zu generieren. Weitere Details finden Sie unter [Nachrichten mit einer Zufallszahl senden]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#send-messages-with-a-random-number). Zum Beispiel gibt {% raw %}`{% random 10 %}`{% endraw %} eine Ganzzahl von 0 bis 9 zurück. Setzen Sie das angepasste Attribut aus Schritt 1 mit JSON wie folgt:<br><br>{% raw %}
```json
{% if {{custom_attribute.${lottery_number}}} == blank %}
{% capture lottery_number_str %}{% random 10 %}{% endcapture %}
{
  "attributes": [
    {
      "lottery_number": {{ lottery_number_str | plus: 0 }}
    }
  ]
}
{% endif %}
```
{% endraw %}
<br><br>
Der {% raw %}`{% if %}`{% endraw %}-Block setzt die Zahl nur, wenn das Attribut leer ist, sodass Nutzer:innen bei erneutem Eintritt in den Canvas dieselbe Zuweisung behalten.<br><br>

{: start="4"}
4. Fügen Sie nach dem Nutzer-Update-Schritt einen [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)-Schritt hinzu. Fügen Sie in jeder Zielgruppe Filter basierend auf Ihrem angepassten Attribut hinzu, anstatt Prozentsätze für die Variantenverteilung zu verwenden.<br><br>Wenn Sie beispielsweise {% raw %}`{% random 10 %}`{% endraw %} verwendet haben, könnte eine Gruppe `lottery_number` **ist kleiner als 4** verwenden, eine andere **ist größer als 3 und kleiner als 7** und eine dritte **ist größer als 6 und kleiner als 10**.

{% enddetails %}
{% endalert %}

### Schritt 2.2: Canvas-Schritte hinzufügen {#step-22-add-canvas-steps}

Sie können weitere Schritte zu Ihrem Canvas-Workflow hinzufügen, indem Sie Komponenten aus der **Komponenten**-Seitenleiste per Drag-and-Drop ziehen. Oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button, um eine Komponente über das Popover-Menü hinzuzufügen.

{% alert tip %}
Wenn Sie weitere Schritte hinzufügen, können Sie die Zoomstufe ändern, um sich auf Details zu konzentrieren oder die gesamte Nutzer-Journey zu überblicken. Zoomen Sie mit <kbd>Shift</kbd> + <kbd>+</kbd> hinein oder mit <kbd>Shift</kbd> + <kbd>-</kbd> heraus.
{% endalert %}

![Das Komponentensuchfenster, das einen Delay-Schritt zum Braze-Canvas hinzufügt.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
Sie können bis zu 200 Schritte in einem Canvas hinzufügen. Wenn Ihr Canvas 200 Schritte überschreitet, können Ladeprobleme auftreten.
{% endalert %}

#### Maximale Dauer {#maximum-duration}

Wenn Ihre Canvas-Journey an Schritten zunimmt, ist die maximale Dauer die längstmögliche Zeit, die Nutzer:innen benötigen können, um diesen Canvas abzuschließen. Diese wird berechnet, indem die Verzögerungen und Trigger-Fenster jedes Schritts für jede Variante auf dem längsten Pfad addiert werden. Wenn Ihr Canvas beispielsweise einen Delay-Schritt mit einer Verzögerung von 3 Tagen und einen Nachrichten-Schritt hat, beträgt die maximale Dauer Ihres Canvas 3 Tage.

#### Einen Schritt bearbeiten {#editing-a-step}

Möchten Sie einen Schritt in Ihrer Nutzer-Journey bearbeiten? Hier erfahren Sie, wie das je nach Canvas-Workflow funktioniert!

Sie können jeden Schritt in Ihrem Canvas-Workflow bearbeiten, indem Sie eine der Komponenten auswählen. Nehmen wir beispielsweise an, Sie möchten Ihren ersten Schritt, eine [Delay]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)-Komponente, in Ihrem Workflow auf einen bestimmten Tag einstellen. Wählen Sie den Schritt aus, um seine Einstellungen anzuzeigen, und passen Sie Ihre Verzögerung auf den 1. März an. Das bedeutet, dass Ihre Nutzer:innen am 1. März zum nächsten Schritt in Ihrem Canvas weitergeleitet werden.

![Ein Beispiel für einen „Delay“-Schritt mit der Verzögerung auf „Bis zu einem bestimmten Tag“ eingestellt.]({% image_buster /assets/img_archive/edit_delay_flow.png %})

Oder Sie können die **Aktionseinstellungen** Ihres [Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)-Schritts schnell bearbeiten und anpassen, um Nutzer:innen für ein Zeitfenster zu halten. Dies priorisiert ihren nächsten Pfad basierend auf den Aktionen während dieses Auswertungszeitraums.

![Der zweite Schritt im Canvas, „Aktionseinstellungen“, mit einem Auswertungsfenster von 1 Tag.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Die leichtgewichtigen Komponenten in Canvas ermöglichen eine einfache Bearbeitungserfahrung, sodass die Anpassung der feineren Details Ihres Canvas erleichtert wird.

#### Nachrichten in Canvas {#messages-in-canvas}

Bearbeiten Sie die Nachrichten in einer Canvas-Komponente, um die Nachrichten zu steuern, die ein bestimmter Schritt senden wird. Canvas kann E-Mail-, mobile und Web-Push-Nachrichten sowie Webhooks zur Integration mit anderen Systemen senden. Ähnlich wie bei Campaigns können Sie bestimmte [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid)-Templates verwenden, um Ihre Nachrichten zu personalisieren.

{% alert tip %}
Wussten Sie, dass Sie Canvas-Komponentennamen in Ihre Nachrichten und Link-Templates einfügen können?<br>
Verwenden Sie den `campaign.${name}` Liquid-Tag in Canvas, um den aktuellen Canvas-Komponentennamen anzuzeigen.
{% endalert %}

Die Nachrichten-Komponente verwaltet die an Nutzer:innen gesendeten Nachrichten. Sie können Ihre **Messaging-Kanäle** auswählen und die **Zustellungseinstellungen** anpassen, um Ihr Canvas-Messaging zu optimieren. Weitere Details zu dieser Komponente finden Sie unter [Nachricht]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

![Der Schritt „Nachrichten einrichten“ mit ausgewählten „Messaging-Kanälen“, der die Liste der verfügbaren Messaging-Kanäle anzeigt, wie z. B. Android-Push, Content Cards, E-Mail und mehr.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Wählen Sie **Fertig**, nachdem Sie die Konfiguration Ihrer Canvas-Komponente abgeschlossen haben.

{% tabs local %}
{% tab Context-Eigenschaften %}

Das [`context`-Objekt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) wird im Schritt **Eingangs-Zeitplan** bei der Erstellung eines Canvas konfiguriert und gibt den Trigger an, der Nutzer:innen in einen Canvas eintreten lässt. Diese Eigenschaften können auch auf die Eigenschaften von Eingangs-Payloads in API-getriggerten Canvases zugreifen. Beachten Sie, dass das `context`-Objekt bis zu 50 KB groß sein kann.

Verwenden Sie das folgende Liquid, wenn Sie auf diese beim Eintritt in den Canvas erstellten Eigenschaften verweisen: {% raw %} ``context.${property_name}`` {% endraw %}. Beachten Sie, dass die Events angepasste Events oder Kauf-Events sein müssen, um auf diese Weise verwendet werden zu können.

{% raw %}
Betrachten Sie beispielsweise die folgende Anfrage: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`. Sie könnten das Wort „shoes“ mit diesem Liquid zu einer Nachricht hinzufügen: ``{{context.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Event-Eigenschaften %}
Event-Eigenschaften sind die Eigenschaften, die Sie für angepasste Events und Käufe festlegen. Diese `event_properties` können in Campaigns mit aktionsbasierter Zustellung sowie in Canvases verwendet werden.

In Canvas können angepasste Event- und Kauf-Event-Eigenschaften in Liquid in jedem Nachrichten-Schritt verwendet werden, der auf einen Aktionspfade-Schritt folgt. Verwenden Sie dieses Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %}, wenn Sie auf diese `event_properties` verweisen. Diese Events müssen angepasste Events oder Kauf-Events sein, um auf diese Weise in der Nachrichten-Komponente verwendet werden zu können.

Im ersten Nachrichten-Schritt nach einem Aktionspfad können Sie `event_properties` verwenden, die sich auf das in diesem Aktionspfad referenzierte Event beziehen. Sie können andere Schritte (die kein weiterer Aktionspfade- oder Nachrichten-Schritt sind) zwischen diesem Aktionspfade-Schritt und dem Nachrichten-Schritt haben. Beachten Sie, dass Sie nur Zugriff auf `event_properties` haben, wenn Ihr Nachrichten-Schritt auf einen Nicht-Alle-anderen-Pfad in einem Aktionspfade-Schritt zurückverfolgt werden kann.

{% endtab %}
{% endtabs %}

### Schritt 2.3: Verbindungen bearbeiten {#step-23-edit-connections}

Um eine Verbindung zwischen Schritten zu verschieben, wählen Sie den Pfeil aus, der die beiden Komponenten verbindet, und wählen Sie eine andere Komponente aus. Um die Verbindung zu entfernen, wählen Sie den Pfeil und dann **Verbindung abbrechen** in der Fußzeile des Canvas-Composers.

Wenn eine einzelne Variante mehrere Verzweigungen mit derselben Zielgruppe und Sendezeit hat, garantiert Braze keine gleichmäßige Aufteilung auf diese Verzweigungen. Die Verteilung kann die zuerst erstellte Verzweigung bevorzugen. Für eine gleichmäßige Aufteilung verwenden Sie [zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)-Filter für jede Verzweigung. Weitere Informationen finden Sie unter [Was passiert, wenn die Zielgruppe und die Sendezeit für einen Canvas mit einer Variante, aber mehreren Verzweigungen identisch sind?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches).

## Schritt 3: Kontrollgruppe hinzufügen {#step-3-add-a-control-group}

Sie können eine Kontrollgruppe zu Ihrem Canvas hinzufügen, indem Sie den <i class="fas fa-plus-circle"></i> Plus-Button auswählen, um eine neue Variante hinzuzufügen.

Braze erfasst die Konversionen für Nutzer:innen, die in die Kontrollgruppe eingeteilt werden, obwohl sie keine Nachrichten erhalten. Um einen genauen Test zu gewährleisten, erfassen wir die Anzahl der Konversionen für Ihre Varianten und die Kontrollgruppe über exakt denselben Zeitraum, wie auf dem Auswahlbildschirm für Konversions-Events angezeigt.

Sie können die Verteilung zwischen Ihren Nachrichten anpassen, indem Sie auf die **Variant Name**-Überschriften doppelklicken.

In diesem Beispiel ist unser Canvas in zwei Varianten aufgeteilt. Variante 1 enthält 70 % der Nutzer:innen. Die zweite Variante ist eine Kontrollgruppe mit den verbleibenden 30 % der Nutzer:innen.

![Ein Beispiel für eine Variante in einem Braze-Canvas, bei der 70 % zu „Variante 1“ gehen, die im ersten Schritt eine Verzögerung von 1 Tag hat und im zweiten Schritt eine Nachricht sendet. Die anderen 30 % gehen in eine „Kontrollgruppe“, die keine weiteren Schritte enthält.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

### Intelligente Auswahl für Canvas {#intelligent-selection-for-canvas}

Die Funktionen der intelligenten Auswahl sind jetzt in multivariaten Canvases verfügbar. Ähnlich wie das Feature [Intelligente Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) für multivariate Campaigns analysiert die intelligente Auswahl für Canvas die Performance jeder Canvas-Variante und passt den Prozentsatz der Nutzer:innen an, die durch jede Variante geleitet werden. Diese Verteilung basiert auf den Performance-Metriken jeder Variante, um die erwartete Gesamtzahl der Konversionen zu maximieren.

Beachten Sie, dass multivariate Canvases es Ihnen ermöglichen, nicht nur Texte zu testen, sondern auch Timing und Kanäle. Durch die intelligente Auswahl können Sie Canvases effizienter testen und sicher sein, dass Ihre Nutzer:innen auf die bestmögliche Canvas-Journey geschickt werden.

![Die Option „Intelligente Auswahl“ ist auf der Seite „Variantenverteilung bearbeiten“ aktiviert. Während sie das Canvas analysiert und optimiert, wird ein horizontaler Balken über die Seite angezeigt, der in mehrere Abschnitte unterteilt ist, die sich in Farbe und Größe unterscheiden. Dies ist nur eine visuelle Darstellung und korreliert nicht mit bestimmten Analytics-Daten.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

Die intelligente Auswahl für Canvas optimiert Ihre Canvas-Ergebnisse, indem sie schrittweise Realtime-Anpassungen an der Verteilung der Nutzer:innen vornimmt, die in jede Variante eingeteilt werden. Wenn der statistische Algorithmus eine:n eindeutige:n Gewinner:in unter Ihren Varianten ermittelt, schließt er die leistungsschwächeren Varianten aus und leitet alle zukünftigen berechtigten Empfänger:innen des Canvas in die Gewinnervarianten.

Aus diesem Grund funktioniert die intelligente Auswahl am besten bei Canvases, in die regelmäßig neue Nutzer:innen eintreten.

## Schritt 4: Speichern und starten {#step-4-save-and-launch}

Wenn Sie Ihr Canvas fertig erstellt haben, wählen Sie **Launch Canvas**, um Ihr Canvas zu speichern und zu starten. Nachdem Sie Ihr Canvas gestartet haben, können Sie die Analytics für Ihre Journey auf der Seite **Canvas Details** einsehen, sobald diese verfügbar sind.

Sie können Ihr Canvas auch als Entwurf speichern, wenn Sie später darauf zurückkommen möchten.

![Ein Beispiel-Canvas in Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
Müssen Sie nach dem Start Änderungen an Ihrem Canvas vornehmen? Das ist möglich! Weitere Informationen finden Sie unter [Canvases nach dem Start bearbeiten]({{site.baseurl}}/post-launch_edits).
{% endalert %}