# Häufig gestellte Fragen {#frequently-asked-questions}

> Hier finden Sie Antworten auf häufig gestellte Fragen zu Bannern in Braze. Weitere allgemeine Informationen finden Sie unter [Über Banner]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## Wann werden Banner-Aktualisierungen für Nutzer:innen angezeigt? {#when-do-banner-updates-appear-for-users}

Banner werden mit ihren neuesten Daten aktualisiert, sobald Sie die Refresh-Methode aufrufen – es ist nicht nötig, Ihre Banner-Campaign erneut zu senden oder zu aktualisieren.

## Wie viele Placements kann ich in einer Sitzung anfordern? {#how-many-placements-can-i-request-in-a-session}

In einer einzelnen Aktualisierungsanfrage können Sie maximal 10 Placements anfordern. Für jedes angeforderte Placement gibt Braze das Banner mit der höchsten Priorität zurück, für das ein:e Nutzer:in berechtigt ist. Zusätzliche Anfragen geben einen Fehler zurück.

Weitere Informationen finden Sie unter [Placement-Anfragen]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## Wie viele Banner-Campaigns können gleichzeitig aktiv sein? {#how-many-banner-campaigns-can-be-active-simultaneously}

Jeder Workspace kann bis zu 200 aktive Banner-Campaigns unterstützen. Wenn dieses Limit erreicht ist, müssen Sie eine bestehende Campaign [archivieren oder deaktivieren]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses#changing-the-status), bevor Sie eine neue erstellen können.

## Welches Banner wird zuerst angezeigt, wenn sich mehrere Campaigns eine Platzierung teilen? {#for-campaigns-sharing-a-placement-which-banner-is-displayed-first}

Wenn ein:e Nutzer:in für mehrere Banner-Campaigns qualifiziert ist, die dieselbe Platzierung verwenden, wird das Banner mit der höchsten Priorität angezeigt. Weitere Informationen finden Sie unter [Banner-Priorität]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## Kann ich Banner in meinem bestehenden Content-Card-Feed verwenden? {#can-i-use-banners-in-my-existing-content-card-feed}

Banner unterscheiden sich von Content Cards, das heißt, Sie können Banner und Content Cards nicht im selben Feed verwenden. Um bestehende Content-Card-Feeds durch Banner zu ersetzen, müssen Sie [Placements in Ihrer App oder Website erstellen]({{site.baseurl}}/developer_guide/banners/placements).

## Wie unterscheiden sich Banner von In-App-Nachrichten? {#how-are-banners-different-from-in-app-messages}

Banner und [In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages) erreichen Nutzer:innen innerhalb Ihrer App oder Website, verwenden jedoch unterschiedliche Zustellungsmodelle. Wenn Sie Banner mit einem bestehenden In-App-Nachrichten-Setup vergleichen, erwarten Sie Unterschiede bei Triggern, Aktualisierungszeitpunkten und Tests – nicht einen Eins-zu-eins-Austausch.

| Thema | Banner | In-App-Nachrichten |
| --- | --- | --- |
| Wo Nachrichten erscheinen | Inline an [Placements]({{site.baseurl}}/developer_guide/banners/placements), die Sie in Ihrer App oder Website definieren | Vollbild-, Modal- oder Slide-up-Overlays, die vom SDK verwaltet werden |
| Wann Inhalte aktualisiert werden | Wenn Ihre App oder Website eine Banner-Aktualisierung auslöst (zum Beispiel beim Sitzungsstart oder während der Sitzung) | Templated-Nachrichten werten Liquid aus, wenn die In-App-Nachricht getriggert wird (zum Beispiel bei einem angepassten Event oder Sitzungsstart), nachdem die Payload auf dem Gerät zwischengespeichert wurde |
| Aktionsbasierte Trigger | Keine [aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery); verwenden Sie stattdessen Segments, Priorität und Aktualisierungszeitpunkte | Unterstützt aktionsbasierte und API-getriggerte Zustellung |
| Tests | Zeigen Sie eine:n Nutzer:in in der Vorschau an und bestätigen Sie dann, dass die Placement-Aktualisierung in Ihrer App oder Website das erwartete Banner anzeigt | Verwenden Sie **Testsendung** oder In-App-Vorschau-Abläufe für triggerbasierte Anzeige |
| Reporting | Banner-Aufrufe und -Klicks folgen der Banner-Analytics | In-App-Impressionen und -Klicks folgen der In-App-Nachrichten-Analytics |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Wie unterscheiden sich Banner von In-App-Nachrichten?" }

## Können Banner Videos enthalten? {#can-banners-include-video}

Der Standard-Banner-Builder unterstützt Bilder, Text und Buttons. Um ein Video in ein Banner einzubinden, können Sie einen **Custom Code**-Block im Builder verwenden oder das gesamte Banner mit dem HTML-Editor erstellen und einen Videoplayer direkt in Ihr HTML einbetten.

## Kann ich ein Banner basierend auf Nutzeraktionen triggern? {#can-i-trigger-a-banner-based-on-user-actions}

Obwohl Banner keine [aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery) unterstützen, können Sie Nutzer:innen anhand ihrer vergangenen Aktionen mithilfe von Segmentierung und Priorität ansprechen.

Um beispielsweise ein spezielles Banner nur Nutzer:innen anzuzeigen, die ein `purchase`-Event abgeschlossen haben:
1. **Targeting:** Wählen Sie in Ihrer Campaign ein Segment von Nutzer:innen aus, die das angepasste Event `purchase` mindestens einmal ausgeführt haben.
2. **Priorität:** Wenn Sie ein allgemeines Banner für alle Nutzer:innen und dieses spezifische Banner für Käufer:innen haben, die auf dieselbe Platzierung abzielen, setzen Sie die Priorität des spezifischen Banners auf **Hoch** und die des allgemeinen Banners auf **Mittel** oder **Niedrig**.

Wenn Nutzer:innen eine neue Sitzung starten oder Banner nach Ausführung der Aktion aktualisieren, bewertet Braze ihre Berechtigung. Wenn sie dem Segment „Kauf“ entsprechen, wird das Banner mit hoher Priorität angezeigt.

## Können Nutzer:innen ein Banner schließen? {#can-users-dismiss-a-banner}

Ja. Sie können Nutzer:innen erlauben, ein Banner manuell zu schließen. Unter [Schließverhalten konfigurieren]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#dismiss-behavior) finden Sie Details zur Konfiguration des Schließverhaltens sowohl im Builder als auch im HTML-Editor.

Nutzer:innen können Banner nur dann manuell schließen, wenn das Schließverhalten aktiviert ist. Wenn das Schließen nicht aktiviert ist, können Sie die Sichtbarkeit von Bannern steuern, indem Sie die Segmentzugehörigkeit der Nutzer:innen verwalten. Wenn ein:e Nutzer:in die Targeting-Kriterien für eine Banner-Campaign nicht mehr erfüllt, wird das Banner in der nächsten Sitzung nicht mehr angezeigt.

Wenn ein:e Nutzer:in ein Banner schließt, ist diese:r standardmäßig nicht mehr für diese Campaign berechtigt. Um geschlossene Banner erneut anzuzeigen, [konfigurieren Sie die erneute Berechtigung]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility) im Schritt **Zustellungskontrollen** der Campaign. Canvas-Banner-Schritte verwenden stattdessen die Canvas-Wiedereintrittseinstellungen, um die erneute Berechtigung zu steuern.

Wenn Sie beispielsweise ein Aktionsbanner anzeigen, bis ein:e Nutzer:in einen Kauf tätigt, kann das Protokollieren eines Events wie `purchase_completed` diese:n Nutzer:in aus dem Zielsegment entfernen und das Banner in nachfolgenden Sitzungen effektiv ausblenden.

## Kann ich die Analytics von Banner-Campaigns über die Braze-API exportieren? {#can-i-export-banners-campaign-analytics-using-the-braze-api}

Ja. Sie können den [`/campaigns/data_series`-Endpunkt]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) verwenden, um Daten darüber abzurufen, wie viele Banner-Campaigns angesehen, angeklickt oder konvertiert wurden.

## Wann werden Nutzer:innen segmentiert? {#when-are-users-segmented}

Nutzer:innen werden zu Beginn der Sitzung segmentiert. Wenn die Zielsegmente einer Campaign von angepassten Attributen, angepassten Events oder anderen Targeting-Attributen abhängen, müssen diese zu Beginn der Sitzung bei den Nutzer:innen vorhanden sein.

## Wie kann ich Banner so gestalten, dass die Latenz möglichst gering bleibt? {#how-can-i-compose-banners-to-ensure-the-lowest-latency}

Je einfacher der Inhalt Ihres Banners ist, desto schneller wird es gerendert. Testen Sie Ihre Banner-Campaign am besten gegen die erwartete Latenz für Ihren Anwendungsfall. Achten Sie beispielsweise darauf, Liquid-Attribute wie `catalog_items` zu testen.

Wenn Sie [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) verwenden (im Early Access), beachten Sie, dass jeder Aufruf auf ein gemeinsames Rendering-Budget von etwa zwei Sekunden angerechnet wird, das für alle Platzierungen in einer einzelnen Aktualisierung gilt. Wenn das Budget überschritten wird oder ein Aufruf das Zeitlimit erreicht, wird das Connected-Content-Ergebnis als null behandelt, und Banner führen keinen erneuten Versuch durch. Um die Latenz zu minimieren:

- Halten Sie Ihre Endpunkte schnell und [cachen Sie Antworten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses), wann immer möglich.
- Begrenzen Sie die Anzahl eindeutiger Connected-Content-URLs über Platzierungen hinweg, die zusammen gerendert werden.
- Vermeiden Sie verkettete Aufrufe, bei denen eine Connected-Content-Antwort die URL für den nächsten Aufruf bestimmt.
- Verwenden Sie Liquid-Guard-Anweisungen oder den [`default`-Filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values), um null-Ergebnisse zu behandeln und leere Banner zu vermeiden.

## Werden alle Liquid-Tags unterstützt? {#are-all-liquid-tags-supported}

Nein. Die meisten Liquid-Tags werden jedoch für Banner-Nachrichten unterstützt, mit Ausnahme von `catalog_items`, die mit dem [`:rerender`-Tag]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs#using-liquid) neu gerendert werden.

## Kann ich Klick-Events erfassen? {#can-i-capture-click-events}

Ja. Wie Klick-Events erfasst werden, hängt davon ab, wie Ihr Banner gerendert wird:

- **Builder – Standardkomponenten:** Wenn Ihr Banner Standard-Editor-Komponenten (Bilder, Buttons, Text) verwendet, werden Klicks automatisch getrackt, wenn Sie die Einfügemethoden des SDK verwenden.
- **Builder – Custom-Code-Blöcke:** Wenn Sie Klicks für Elemente innerhalb eines Custom-Code-Editor-Blocks tracken möchten, müssen Sie `brazeBridge.logClick()` aus Ihrem angepassten HTML heraus aufrufen. Dies gilt auch dann, wenn Sie die SDK-Methoden zum Einfügen und Rendern des Banners verwenden.
- **HTML-Editor:** Klick-Tracking erfolgt nicht automatisch. Sie müssen `brazeBridge.logClick()` für jedes klickbare Element aufrufen, das Sie tracken möchten. Die vollständige Referenz finden Sie unter [Angepasster Code und JavaScript-Bridge für Banner]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).
- **Angepasste UI (Headless):** Wenn Sie eine vollständig angepasste UI mithilfe der angepassten Eigenschaften des Banners erstellen, anstatt das Banner-HTML zu rendern, rufen Sie `logClick()` auf dem Banner-Objekt aus Ihrem Anwendungscode auf.

Weitere Informationen finden Sie unter [Klicks protokollieren]({{site.baseurl}}/developer_guide/banners/placements#logging-clicks).