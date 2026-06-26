# Häufig gestellte Fragen {#frequently-asked-questions}

> Hier finden Sie Antworten auf häufig gestellte Fragen zu Bannern in Braze. Weitere allgemeine Informationen finden Sie unter [Über Banner]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}/).

## Wann erscheinen Banner-Updates für Nutzer:innen? {#when-do-banner-updates-appear-for-users}

Banner werden bei jedem Aufruf der Aktualisierungsmethode mit den neuesten Daten aktualisiert – es ist nicht nötig, Ihre Banner-Campaign erneut zu senden oder ein Update durchzuführen.

## Wie viele Platzierungen kann ich in einer Sitzung anfragen? {#how-many-placements-can-i-request-in-a-session}

In einer einzelnen Aktualisierungsanfrage können Sie maximal 10 Platzierungen anfragen. Für jede angefragte Platzierung gibt Braze das Banner mit der höchsten Priorität zurück, für das ein:e Nutzer:in berechtigt ist. Weitere Anfragen führen zu einer Fehlermeldung.

Weitere Informationen finden Sie unter [Platzierungsanfragen]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## Wie viele Banner-Campaigns können gleichzeitig aktiv sein? {#how-many-banner-campaigns-can-be-active-simultaneously}

Jeder Workspace kann bis zu 200 aktive Banner-Campaigns unterstützen. Wenn dieses Limit erreicht ist, müssen Sie eine bestehende Campaign [archivieren oder deaktivieren]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status), bevor Sie eine neue erstellen können.

## Welches Banner wird bei Campaigns, die sich eine Platzierung teilen, zuerst angezeigt? {#for-campaigns-sharing-a-placement-which-banner-is-displayed-first}

Wenn sich ein:e Nutzer:in für mehrere Banner-Campaigns qualifiziert, die sich dieselbe Platzierung teilen, wird das Banner mit der höchsten Priorität angezeigt. Weitere Informationen finden Sie unter [Banner-Priorität]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## Kann ich Banner in meinem bestehenden Content-Card-Feed verwenden? {#can-i-use-banners-in-my-existing-content-card-feed}

Banner unterscheiden sich von Content Cards, d. h. Sie können Banner und Content Cards nicht im selben Feed verwenden. Um bestehende Content-Card-Feeds durch Banner zu ersetzen, müssen Sie [Platzierungen in Ihrer App oder Website erstellen]({{site.baseurl}}/developer_guide/banners/placements/).

## Können Banner Video enthalten? {#can-banners-include-video}

Der Standard-Banner-Composer unterstützt Bilder, Text und Buttons. Um ein Video in ein Banner einzubinden, können Sie einen **Custom Code**-Block verwenden und ein Video oder einen eingebetteten Player in Ihrer App oder Website rendern.

## Kann ich ein Banner basierend auf Aktionen von Nutzer:innen triggern? {#can-i-trigger-a-banner-based-on-user-actions}

Obwohl Banner keine [aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) unterstützen, können Sie Nutzer:innen anhand ihrer bisherigen Aktionen mithilfe von Segmentierung und Priorisierung gezielt ansprechen.

Um beispielsweise ein spezielles Banner nur für Nutzer:innen anzuzeigen, die ein `purchase`-Event abgeschlossen haben:
1. **Targeting:** Richten Sie Ihre Campaign an ein Segment von Nutzer:innen, die das angepasste Event `purchase` mindestens einmal durchgeführt haben.
2. **Priorität:** Wenn Sie ein allgemeines Banner für alle Nutzer:innen und dieses spezifische Banner für Käufer:innen haben, die auf dieselbe Platzierung abzielen, setzen Sie die Priorität des spezifischen Banners auf **Hoch** und die des allgemeinen Banners auf **Mittel** oder **Niedrig**.

Wenn ein:e Nutzer:in eine neue Sitzung startet oder Banner nach der Aktion aktualisiert, überprüft Braze die Berechtigung. Wenn die Person dem Segment „Kauf“ entspricht, wird das Banner mit hoher Priorität angezeigt.


## Können Nutzer:innen ein Banner schließen? {#can-users-dismiss-a-banner}

Ja. Sie können Nutzer:innen erlauben, ein Banner manuell zu schließen, indem Sie das Schließverhalten im Banner-Composer aktivieren. Weitere Details finden Sie unter [Schließverhalten konfigurieren]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#dismiss-behavior).

Nutzer:innen können Banner nur dann manuell schließen, wenn das Schließverhalten aktiviert ist. Wenn das Schließen nicht aktiviert ist, können Sie die Sichtbarkeit von Bannern steuern, indem Sie die Segment-Berechtigung der Nutzer:innen verwalten. Wenn ein:e Nutzer:in die Targeting-Kriterien für eine Banner-Campaign nicht mehr erfüllt, wird das Banner bei der nächsten Sitzung nicht mehr angezeigt.

Wenn ein:e Nutzer:in ein Banner schließt, ist diese Person standardmäßig nicht mehr für diese Campaign berechtigt. Um geschlossene Banner erneut anzuzeigen, [konfigurieren Sie die erneute Berechtigung]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#re-eligibility) im Schritt **Zustellungs-Kontrollgruppen** der Campaign. Canvas-Banner-Schritte verwenden stattdessen die Canvas-Wiedereintrittseinstellungen zur Steuerung der erneuten Berechtigung.

Wenn Sie beispielsweise ein Werbebanner anzeigen, bis ein:e Nutzer:in einen Kauf tätigt, kann die Protokollierung eines Events wie `purchase_completed` diese:n Nutzer:in aus dem Ziel-Segment entfernen und das Banner in nachfolgenden Sitzungen effektiv ausblenden.

## Kann ich die Analytics von Banner-Campaigns über die Braze-API exportieren? {#can-i-export-banners-campaign-analytics-using-the-braze-api}

Ja. Über den [Endpunkt `/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) können Sie Daten darüber abrufen, wie oft Banner-Campaigns angesehen, angeklickt oder konvertiert wurden.

## Wann werden Nutzer:innen segmentiert? {#when-are-users-segmented}

Nutzer:innen werden zu Beginn der Sitzung segmentiert. Wenn die Ziel-Segmente einer Campaign von angepassten Attributen, angepassten Events oder anderen Targeting-Attributen abhängen, müssen diese bei der/dem Nutzer:in zu Beginn der Sitzung vorhanden sein.

## Wie kann ich Banner gestalten, um die geringste Latenz zu gewährleisten? {#how-can-i-compose-banners-to-ensure-the-lowest-latency}

Je einfacher das Messaging in Ihrem Banner ist, desto schneller wird es gerendert. Testen Sie Ihre Banner-Campaign am besten anhand der erwarteten Latenz für Ihren Anwendungsfall. Testen Sie zum Beispiel unbedingt Liquid-Attribute wie `catalog_items`.

## Werden alle Liquid-Tags unterstützt? {#are-all-liquid-tags-supported}

Nein. Die meisten Liquid-Tags werden jedoch für Banner-Nachrichten unterstützt, mit Ausnahme von `catalog_items`, die mit dem [`:rerender`-Tag]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid) neu gerendert werden.

## Kann ich Klick-Events erfassen? {#can-i-capture-click-events}

Ja. Wie Klick-Events erfasst werden, hängt davon ab, wie Ihr Banner gerendert wird:

- **Standard-Editor-Komponenten:** Wenn Ihr Banner Standard-Editor-Komponenten (Bilder, Buttons, Text) verwendet, werden Klicks automatisch getrackt, wenn Sie die Einfügemethoden des SDK verwenden.
- **Custom-Code-Blöcke:** Wenn Sie Klicks für Elemente innerhalb eines Custom-Code-Editor-Blocks tracken möchten, müssen Sie `brazeBridge.logClick()` in Ihrem angepassten HTML aufrufen, um Klicks zu erfassen. Dies gilt auch bei der Verwendung der SDK-Methoden zum Einfügen und Rendern des Banners. Die vollständige Referenz finden Sie unter [Angepasster Code und JavaScript-Bridge für Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/custom_code/#javascript-bridge).
- **Angepasste UI (Headless):** Wenn Sie eine vollständig angepasste UI unter Verwendung der angepassten Eigenschaften des Banners erstellen, anstatt das Banner-HTML zu rendern, rufen Sie `logClick()` auf dem Banner-Objekt aus Ihrem Anwendungscode auf.

Weitere Informationen finden Sie unter [Klicks protokollieren]({{site.baseurl}}/developer_guide/banners/placements/#logging-clicks).