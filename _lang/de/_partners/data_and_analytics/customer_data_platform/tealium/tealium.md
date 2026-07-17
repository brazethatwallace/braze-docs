---
nav_title: Tealium
article_title: Tealium
page_order: 1
alias: /partners/tealium/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Tealium, einem universellen Daten-Hub, der es Ihnen ermöglicht, mobile, Web- und alternative Daten mit anderen Drittanbieter-Quellen zu verbinden."
page_type: partner
search_tag: Partner

---

# Tealium

> [Tealium](https://tealium.com/) ist ein universeller Daten-Hub und eine Customer Data Platform, bestehend aus EventStream, AudienceStream und iQ Tag-Management, die es Ihnen ermöglicht, Mobil-, Web- und alternative Daten aus Drittanbieter-Quellen zu verbinden. Die Verbindung von Tealium mit Braze ermöglicht einen Datenfluss von angepassten Events, Nutzerattributen und Käufen, die Sie in die Lage versetzen, Ihre Daten in Realtime zu nutzen.

![Eine Übersichtsgrafik von Tealium, die zeigt, wie die verschiedenen Produkte von Tealium und die Braze-Plattform zusammenpassen, um kanalübergreifende Campaigns in Realtime zu aktivieren.]({% image_buster /assets/img/tealium/tealium_overview.png %}){: style="border:0;"}

Die Integration von Braze und Tealium erlaubt es Ihnen, Ihre Nutzer:innen zu tracken und Daten an verschiedene Anbieter von Analytics weiterzuleiten. Tealium ermöglicht es Ihnen:
- Tealium-Zielgruppen mit [AudienceStream]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream) mit Braze zu synchronisieren, um Braze-Campaigns und Canvases zu personalisieren oder Segmente zu erstellen.
- [Daten plattformübergreifend zu importieren](#choose-your-integration-type). Braze bietet sowohl eine [Side-by-side](#side-by-side-sdk-integration)-SDK-Integration für Ihre Android-, iOS- und Web-Anwendungen als auch eine [Server-zu-Server](#server-to-server-integration)-Integration, die innerhalb jeder Plattform verwendet werden kann, die Event-Daten melden kann.<br><br>

{% tabs %}
{% tab EventStream %}
Tealium EventStream ist eine Datenerfassungs- und API-Drehscheibe, die im Zentrum Ihrer Daten steht. EventStream wickelt die gesamte Datenlieferkette ab, von der Einrichtung und Installation bis hin zur Identifizierung, Validierung und Verbesserung der eingehenden Nutzerdaten. EventStream arbeitet in Realtime mit Event-Feeds und Konnektoren. Im Folgenden finden Sie die Features, aus denen der [EventStream](https://docs.tealium.com/server-side/getting-started/eventstream-api-hub/introduction/) besteht.
- Datenquellen (Installation und Datenerfassung)
- Live-Events (Prüfung von Echtzeitdaten)
- Event-Spezifikationen und Attribute (Anforderungen an die Datenebene und Validierung)
- Event-Feeds (gefilterte Event-Typen)
- Event-Konnektoren (API-Hub-Aktionen)

{% endtab %}
{% tab AudienceStream %}

Tealium AudienceStream ist eine Omnichannel-Kundensegmentierung und Realtime-Action-Engine. AudienceStream nimmt die Daten, die in EventStream einfließen, und erstellt Besucherprofile, die die wichtigsten Attribute des Engagements Ihrer Kund:innen mit Ihrer Marke darstellen. Weitere Informationen zur Einrichtung finden Sie in unserem [AudienceStream]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream)-Artikel.

{% endtab %}
{% tab iQ Tag-Management %}
Tealium iQ erlaubt es Ihnen, Code in Ihren Apps über ein Tag in der Tealium iQ Tag-Management-UI zu triggern. Dieser Tag sammelt, kontrolliert und liefert Event-Daten von Mobil- und Webplattformen und erlaubt es Ihnen, eine native Braze-Implementierung zu konfigurieren, ohne Braze-spezifischen Code zu Ihren Apps hinzuzufügen. Nutzer:innen können Mobile Remote Commands über iQ Tag-Management oder JSON-Konfigurationsdateien integrieren (empfohlener Ansatz von Tealium). Nutzer:innen, die das Braze Web SDK verwenden, müssen die Integration über den Web-iQ-Tag vornehmen.

Wenn Sie mehr über die Vor- und Nachteile der einzelnen Methoden erfahren möchten, lesen Sie den folgenden Abschnitt [Tealium iQ Tag Manager](#mobile-remote-commands).
{% endtab %}
{% endtabs %}

{% alert important %}
Tealium bietet sowohl Batch- als auch Non-Batch-Konnektor-Aktionen an. Der Non-Batch-Konnektor sollte verwendet werden, wenn Anfragen in Realtime für den Anwendungsfall wichtig sind und keine Bedenken bestehen, dass die Spezifikationen für die Rate-Limits der Braze-API überschritten werden. Kontaktieren Sie den Braze-Support oder Ihren Customer-Success-Manager, wenn Sie Fragen haben.<br><br>

Bei Batch-Konnektoren werden Anfragen in eine Warteschlange gestellt, bis einer der folgenden Schwellenwerte erreicht ist:<br><br>
- Maximale Anzahl von Anfragen: 75
- Maximale Zeit seit der ältesten Anfrage: 10 Minuten
- Maximale Größe der Anfragen: 1 MB

Tealium bündelt standardmäßig keine Zustimmungs-Events (Abo-Einstellungen) oder Events zur Löschung von Nutzer:innen.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Tealium-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Tealium-Konto](https://my.tealiumiq.com/) mit Server- und/oder Client-seitigem Zugriff. |
| Installierte Quelle und Tealium-Quell-[Bibliotheken](https://docs.tealium.com/platforms/) | Die Herkunft der Daten, die an Tealium gesendet werden, z. B. von mobilen Apps, Websites oder Backend-Servern.<br><br>Sie müssen die Bibliotheken in Ihrer App, Ihrer Website oder Ihrem Server installieren, bevor Sie einen erfolgreichen Tealium-Konnektor einrichten können. |
| Braze-REST- und SDK-Endpunkt | Ihre REST- oder SDK-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics#endpoints) ab. |
| Braze-App-Bezeichner-Schlüssel (nur bei Side-by-side) | Ihr App-Bezeichner-Schlüssel. <br><br>Diesen finden Sie unter **Braze Dashboard > Manage Settings > API Key**. |
| Code-Version (nur bei Side-by-side) | Entspricht der SDK-Version und sollte im Format major.minor angegeben werden (zum Beispiel 3.2 und nicht 3.0.1). Die Code-Version sollte 3.0 oder höher sein. |
| REST-API-Schlüssel (nur bei Server-zu-Server) | Ein Braze-REST-API-Schlüssel mit den Berechtigungen `users.track` und `users.delete`. <br><br>Dieser kann über **Braze Dashboard > Developer Console > REST API Key > Create New API Key** erstellt werden.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Wählen Sie Ihren Integrationstyp {#choose-your-integration-type}

| Integration | Details |
| ----------- | ------- |
| [Side-by-side](#side-by-side-sdk-integration) | Verwendet das SDK von Tealium, um Events in die nativen Aufrufe von Braze zu übersetzen, was den Zugriff auf tiefere Features und eine umfassendere Nutzung von Braze ermöglicht als die Server-zu-Server-Integration.<br><br>Wenn Sie Braze Remote Commands verwenden möchten, beachten Sie, dass Tealium nicht alle Braze-Methoden (z. B. Content Cards) unterstützt. Um eine Braze-Methode zu verwenden, die nicht durch einen entsprechenden Remote Command abgebildet wird, müssen Sie die Methode durch Hinzufügen von nativem Braze-Code zu Ihrer Codebasis aufrufen.|
| [Server-zu-Server](#server-to-server-integration) | Leitet Daten von Tealium an die REST-API-Endpunkte von Braze weiter.<br><br>Unterstützt keine Braze-UI-Features wie In-App-Nachrichten, Content Cards oder Push-Benachrichtigungen. Es gibt auch automatisch erfasste Daten, wie z. B. Felder auf Geräteebene, die mit dieser Methode nicht verfügbar sind.<br><br>Ziehen Sie eine Side-by-side-Integration in Betracht, wenn Sie diese Features nutzen möchten.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Wählen Sie Ihren Integrationstyp" }

## Side-by-side-SDK-Integration {#side-by-side-sdk-integration}

### Remote Commands

Remote Commands sind ein Feature der Tealium-iOS- und Android-Bibliotheken, das es Ihnen erlaubt, vom Tealium SDK – über die Braze-Server – Braze aufzurufen. Das Braze-Remote-Command-Modul installiert und erstellt automatisch die erforderlichen Braze-Bibliotheken und kümmert sich um die Darstellung von Nachrichten und das Analytics-Tracking. Um Braze Mobile Remote Commands zu verwenden, müssen Sie Tealium-Bibliotheken in Ihren Apps installiert haben.

Tealium bietet zwei Möglichkeiten zur Integration von Mobile Remote Commands. Es gibt keinen Funktionsverlust zwischen den Integrationstypen, und der zugrunde liegende native Code ist identisch.

| Mobile-Remote-Command-Methode | Vorteile | Nachteile |
| --- | --- | --- |
| **Remote-Command-Tag** | Ändern Sie die Abbildungen und Daten, die an den Remote Command gesendet werden, ganz einfach über die Tealium iQ UI.<br><br>Dies erlaubt es, zusätzliche Daten oder Events an ein SDK eines Drittanbieters zu senden, nachdem die App bereits im App Store ist, ohne dass der Client die App aktualisieren muss. | Das Tag-Management-Modul in der App stützt sich auf eine ausgeblendete Webansicht, um JavaScript zu verarbeiten. |
| **JSON-Konfigurationsdatei**<br>([Empfohlen](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#how-it-works)) | Die Verwendung der JSON-Methode macht eine ausgeblendete Webansicht in der App überflüssig und reduziert den Speicherverbrauch erheblich.<br><br>Die JSON-Datei kann per Fernzugriff oder lokal in der App der Kund:in gehostet werden. | Im Moment gibt es keine UI, um dies zu verwalten, so dass es ein wenig zusätzlichen Aufwand erfordert.<br><br>Hinweis: Tealium arbeitet an einer Verwaltungs-UI, die dieses Problem lösen und den JSON-Remote-Commands das gleiche Maß an Flexibilität verleihen wird, das sie mit der iQ-Tag-Management-Version haben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Remote Commands" }

Verwenden Sie die Datenabbildungen von Braze Mobile Remote Commands, um Standard-Nutzerattribute und angepasste Attribute festzulegen und Käufe und angepasste Events zu verfolgen. Die entsprechenden Braze-Methoden finden Sie in der folgenden Tabelle.

| Remote Command | Braze-Methode |
| -------------- | ------------ |
| appendcustomarrayattribute | addToCustomAttributeArrayWithKey()|
| emailnotification | setEmailNotificationSubscriptionType() |
| incrementcustomattribute | incrementCustomAttribute() |
| initialize | startWithApiKey() |
| logcustomevent | logCustomEvent() |
| logpurchase | logPurchase() |
| pushnotification | setPushNotificationSubscriptionType() |
| removecustomattribute | setCustomAttributeWithKey() |
| setcustomattribute | setCustomAttributeArrayWithKey() |
| setcustomarrayattribute | setCustomAttributeArrayWithKey() |
| setlastknownlocation | setLastKnownLocationWithLatitude() |
| unsetcustomattribute | unsetCustomAttributeWithKey() |
| useralias | addAlias() |
| userattribute | ABKUser() |
| useridentifier | changeUser() |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Remote Commands" }

Weitere Einzelheiten zur Einrichtung von Braze Mobile Remote Commands und eine Übersicht über die unterstützten Methoden finden Sie in der Tealium-Entwicklerdokumentation:
- [Remote Command](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#json-template)
- [Remote-Command-Tag](https://docs.tealium.com/client-side-tags/braze-mobile-remote-command-tag/)

{% alert important %}
Braze Mobile Remote Commands unterstützen nicht alle Braze-Methoden und Messaging-Kanäle (z. B. Content Cards). Um eine Braze-Methode zu verwenden, die nicht durch einen entsprechenden Remote Command abgebildet wird, müssen Sie die Methode direkt aufrufen, indem Sie Ihrer Codebasis nativen Braze-Code hinzufügen.
{% endalert%}

### Braze Web SDK Tag

Verwenden Sie den Braze Web SDK Tag, um das Braze Web SDK auf Ihrer Website einzusetzen. [Tealium iQ Tag-Management](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) erlaubt es Kund:innen, Braze als Tag innerhalb des Tealium-Dashboards hinzuzufügen, um die Besucheraktivitäten zu verfolgen. Tags werden in der Regel von Marketern verwendet, um die Wirksamkeit von Online-Werbung, E-Mail-Marketing und Website-Personalisierung zu verstehen.

1. Navigieren Sie in Tealium zu **iQ > Tags > + Add Tag > Braze Web SDK**.
2. Geben Sie im Dialogfeld Tag-Konfiguration den API-Schlüssel (Ihren Braze-App-Bezeichner-Schlüssel), die Basis-URL (den Braze-SDK-Endpunkt) und die [Code-Version des Braze Web SDK](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) ein. Sie können auch die Protokollierung aktivieren, um Informationen zu Debugging-Zwecken in der Web-Konsole zu protokollieren.
3. Wählen Sie im Dialogfeld [Load Rules](https://docs.tealium.com/iq-tag-management/load-rules/about/) die Option „Load on All Pages“ oder wählen Sie **Create Rule**, um festzulegen, wann und wo eine Instanz dieses Tags auf Ihrer Website geladen werden soll.
4. Im Dialogfeld **[Data Mappings](https://docs.tealium.com/iq-tag-management/data-mappings/about/)** wählen Sie **Create Mappings**, um Tealium-Daten auf Braze abzubilden. Die Zielvariablen für den Braze Web SDK Tag sind im Tab **Data Mapping** für den Tag integriert. In den [folgenden Tabellen](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) sind die verfügbaren Zielkategorien aufgeführt und die einzelnen Zielnamen beschrieben.
5. Wählen Sie **Finish**.

### Ressourcen für Side-by-side-Integrationen {#side-by-side-integrations-resources}

- iOS Remote Command: [Tealium-Dokumentation](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Tealium GitHub Repository](https://github.com/Tealium/tealium-ios-braze-remote-command)
- Android Remote Command: [Tealium-Dokumentation](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Tealium GitHub Repository](https://github.com/Tealium/tealium-android-braze-remote-command)
- Web SDK Tag: [Tealium-Dokumentation](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)

## Server-zu-Server-Integration {#server-to-server-integration}

Diese Integration leitet Daten von Tealium an die Braze REST API weiter.

Die Server-zu-Server-Integration unterstützt keine Braze-UI-Features wie In-App-Nachrichten, Content Cards oder Push-Benachrichtigungen. Es gibt auch automatisch erfasste Daten (z. B. Felder auf Geräteebene), die mit dieser Methode nicht verfügbar sind.

Wenn Sie diese Daten und Features nutzen möchten, sollten Sie unsere [Side-by-side]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium#side-by-side-sdk-integration)-SDK-Integration in Betracht ziehen.

### 1. Schritt: Eine Quelle einrichten {#step-1-set-up-a-source}

Tealium setzt voraus, dass Sie zunächst eine gültige Datenquelle für Ihren Konnektor einrichten, aus der er schöpfen kann.
1. Navigieren Sie in der Seitenleiste von Tealium unter **Server-Side** zu **Sources > Data Sources > + Add Data Source**.
2. Suchen Sie die gewünschte Plattform in den verfügbaren Kategorien und benennen Sie Ihre Quelle – dies ist ein Pflichtfeld.<br>![Tealium-Dialog „Datenquelle hinzufügen“ mit Plattformauswahl und Feld für den Quellnamen.]({% image_buster /assets/img/tealium/data_source.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. Wählen Sie aus den Optionen für **Event Specifications** die [Event-Spezifikationen](https://docs.tealium.com/server-side/event-specifications/about/) aus, die Sie hinzufügen möchten. Event-Spezifikationen helfen Ihnen, die Event-Namen und die erforderlichen Attribute für das Tracking in Ihrer Installation zu identifizieren. Diese Spezifikationen werden auf eingehende Events angewendet.<br>![Tealium-Optionen für Event-Spezifikationen einer Datenquelle.]({% image_buster /assets/img/tealium/event_specs.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>Nehmen Sie sich etwas Zeit, um darüber nachzudenken, welche Daten für Sie am wertvollsten sind und welche Spezifikationen für Ihren Anwendungsfall am geeignetsten erscheinen. [Angepasste Event-Spezifikationen](https://docs.tealium.com/iq-tag-management/events/about/) sind ebenfalls verfügbar. <br>
4. Der nächste Dialog führt Sie zum Schritt **Get Code**. Der hier bereitgestellte Basiscode und der Code für das Event-Tracking dienen Ihnen als Installationsanleitung. Laden Sie die bereitgestellte PDF-Datei herunter, wenn Sie diese Anweisungen an Ihr Team weitergeben möchten. Wählen Sie **Save & Continue**, wenn Sie fertig sind.<br>
5. Sie können nun Ihre gespeicherte Quelle einsehen und Event-Spezifikationen hinzufügen oder entfernen. <br>![Gespeicherte Tealium-Datenquelle mit Event-Spezifikationen und Verbindungsdetails.]({% image_buster /assets/img/tealium/braze_connection.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>In der Detailansicht der Datenquelle können Sie die folgenden Aktionen durchführen:
- Anzeigen und Kopieren des Datenquellenschlüssels
- Installationsanleitung ansehen
- Zurück zur Seite **Get Code**
- Hinzufügen oder Entfernen von Event-Spezifikationen
- Navigieren, um Live-Events in Bezug auf eine Event-Spezifikation anzuzeigen
- Und mehr...<br>
6. Zum Schluss wählen Sie oben auf der Seite **Save / Publish** aus. Wenn Sie Ihre Quelle nicht veröffentlichen, können Sie sie bei der Konfiguration Ihres Braze-Konnektors nicht finden.

Unter [Data Sources](https://docs.tealium.com/server-side/data-sources/about-data-sources/) finden Sie weitere Anweisungen zum Einrichten und Bearbeiten Ihrer Datenquelle.

### 2. Schritt: Einen Event-Konnektor erstellen {#step-2-create-an-event-connector}

Ein Konnektor ist eine Integration zwischen Tealium und einem anderen Anbieter, die zur Übertragung von Daten verwendet wird. Diese Konnektoren enthalten Aktionen, die die unterstützten APIs des Partners repräsentieren.

1. Navigieren Sie in der Seitenleiste von Tealium unter **Server-Side** zu **EventStream > Event Connectors**.
2. Wählen Sie den blauen Button **+ Add Connector**, um den Marktplatz der Konnektoren zu durchsuchen. In dem neu erscheinenden Dialogfeld verwenden Sie die Spotlight-Suche, um den **Braze**-Konnektor zu finden.
3. Um diesen Konnektor hinzuzufügen, klicken Sie auf die **Braze**-Konnektor-Kachel. Wenn Sie darauf klicken, können Sie die Verbindungsübersicht und eine Liste der erforderlichen Informationen, der unterstützten Aktionen und der Konfigurationsanweisungen anzeigen. Die Konfiguration umfasst drei Schritte: Quelle, Konfiguration und Aktion.

#### Quelle {#source}

Nachdem Sie die Quelle konfiguriert haben, gehen Sie zurück zur Braze-Konnektor-Seite unter **EventStream** > **Event Connectors** > **+ Add Connector** > **Braze**.

Wählen Sie dann die Datenquelle aus, die Sie gerade erstellt haben, und wählen Sie unter **Event Feed** die Option **All Events** oder eine bestimmte Event-Spezifikation – den empfohlenen Pfad, um nur geänderte Werte an Braze zu senden. Wählen Sie **Continue**.

#### Konfiguration {#configuration}

Wählen Sie dann unten auf der Seite **Add Connector** aus. Benennen Sie Ihren Konnektor und geben Sie hier Ihren Braze-API-Endpunkt und den Braze-REST-API-Schlüssel an.

![Braze-Konnektor-Konfiguration mit Feldern für API-Endpunkt und REST-API-Schlüssel.]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Wenn Sie bereits einen Konnektor erstellt haben, können Sie optional einen vorhandenen Konnektor aus der Liste der verfügbaren Konnektoren verwenden und ihn mit dem Bleistiftsymbol an Ihre Bedürfnisse anpassen oder mit dem Papierkorbsymbol löschen.

#### Aktion {#action}

Benennen Sie als Nächstes Ihre Konnektor-Aktion und wählen Sie einen Aktionstyp aus, der Daten gemäß der von Ihnen konfigurierten Abbildung sendet. Hier bilden Sie Braze-Attribute, Events und Käufe auf Tealium-Attribut-, Event- und Kaufnamen ab.

{% alert important %}
Nicht alle angebotenen Felder sind erforderlich.

![Tealium-Konnektor-Aktion mit eingeklappten optionalen Feldern.]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Nutzer:in tracken – Batch und Non-Batch %}

Mit dieser Aktion können Sie Nutzer-, Event- und Kaufattribute in einer einzigen Aktion tracken.

| Parameter | Beschreibung |
| ---------- | ----------- |
| Nutzer-ID | Verwenden Sie dieses Feld, um das Tealium-Nutzer-ID-Feld auf das entsprechende Braze-Feld abzubilden. Bilden Sie ein oder mehrere Nutzer-ID-Attribute ab. Wenn mehrere IDs angegeben werden, wird der erste nicht leere Wert in der folgenden Reihenfolge ausgewählt: Externe ID, Braze ID, Alias-Name und Alias-Label.<br><br>- Externe ID und Braze ID sollten beim Import von Push-Tokens nicht angegeben werden.<br>- Wenn Sie einen Nutzer-Alias angeben, sollten der Alias-Name und das Alias-Label festgelegt werden. <br><br>Weitere Informationen finden Sie unter dem Braze-[Endpunkt `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). |
| Nutzerattribute | Verwenden Sie die vorhandenen Feldnamen der Braze-Nutzerprofile, um die Werte der Nutzerprofile im Braze-Dashboard zu aktualisieren, oder fügen Sie den Nutzerprofilen Ihre eigenen angepassten Daten für die [Nutzerattribute]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens) hinzu.<br><br>- Standardmäßig werden neue Nutzer:innen angelegt, wenn noch keine vorhanden sind.<br>- Wenn Sie **Update Existing Only** auf `true` setzen, werden nur vorhandene Nutzer:innen aktualisiert und keine neuen Nutzer:innen angelegt.<br>- Wenn ein Tealium-Attribut leer ist, wird es in Null umgewandelt und aus dem Braze-Nutzerprofil entfernt. Anreicherungen sollten verwendet werden, wenn keine Nullwerte an Braze gesendet werden sollen, um ein Nutzerattribut zu entfernen. |
| Nutzerattribute ändern | Verwenden Sie dieses Feld, um bestimmte Nutzerattribute zu erhöhen oder zu verringern.<br><br>- Integer-Attribute können um positive oder negative ganze Zahlen inkrementiert werden.<br>- Array-Attribute können durch Hinzufügen oder Entfernen von Werten in bestehenden Arrays geändert werden. |
| Event | Ein Event stellt ein einzelnes Vorkommen eines angepassten Events durch eine:n bestimmte:n Nutzer:in zu einem bestimmten Zeitpunkt dar. Verwenden Sie dieses Feld zum Tracking und zur Abbildung von Event-Attributen, wie sie im Braze-[Event-Objekt]({{site.baseurl}}/api/objects_filters/event_object) enthalten sind. <br><br>- Das Event-Attribut `Name` ist für jedes zugeordnete Event erforderlich.<br>- Das Event-Attribut `Time` wird automatisch auf „jetzt“ gesetzt, wenn es nicht explizit abgebildet wird. <br>- Standardmäßig werden neue Events erstellt, wenn noch keines vorhanden ist. Wenn Sie `Update Existing Only` auf `true` setzen, werden nur bestehende Events aktualisiert und es wird kein neues Event erstellt.<br>- Bilden Sie Array-Typ-Attribute ab, um mehrere Events hinzuzufügen. Array-Typ-Attribute müssen gleich lang sein.<br>- Einzelwert-Attribute können verwendet und auf jedes Event angewendet werden. |
| Event-Template | Stellen Sie Event-Templates zur Verfügung, auf die in den Body-Daten referenziert werden kann. Templates können verwendet werden, um Daten zu transformieren, bevor sie an Braze gesendet werden. Weitere Informationen finden Sie in der [Anleitung für Templates](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) von Tealium. |
| Event-Template-Variable | Stellen Sie Event-Template-Variablen als Dateneingabe bereit. Lesen Sie den [Leitfaden für Template-Variablen](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) von Tealium, um mehr zu erfahren. |
| Kauf | Verwenden Sie dieses Feld, um Nutzer-Kaufattribute zu verfolgen und abzubilden, wie sie im Braze-[Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object) enthalten sind.<br><br>- Die Kaufattribute `Product ID`, `Currency` und `Price` sind für jeden zugeordneten Kauf erforderlich.<br>- Das Kaufattribut `Time` wird automatisch auf „jetzt“ gesetzt, wenn es nicht explizit abgebildet wird.<br>- Standardmäßig werden neue Käufe angelegt, wenn noch keine vorhanden sind. Wenn Sie `Update Existing Only` auf `true` setzen, werden nur bestehende Käufe aktualisiert und es wird kein neuer Kauf angelegt.<br>- Bilden Sie Array-Typ-Attribute ab, um mehrere Kaufartikel hinzuzufügen. Array-Typ-Attribute müssen gleich lang sein.<br>- Einzelwert-Attribute können verwendet werden und gelten dann für jeden Artikel.|
| Kauf-Template | Templates können verwendet werden, um Daten zu transformieren, bevor sie an Braze gesendet werden.<br>- Definieren Sie ein Kauf-Template, wenn Sie Unterstützung für verschachtelte Objekte benötigen.<br>- Wenn ein Kauf-Template definiert wird, wird die Konfiguration, die im Abschnitt „Käufe“ Ihrer Aktion eingerichtet wurde, ignoriert.<br>- Weitere Informationen finden Sie in der [Anleitung für Templates](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) von Tealium.|
| Kauf-Template-Variable | Stellen Sie Produkt-Template-Variablen als Dateneingabe bereit. Lesen Sie den [Leitfaden für Template-Variablen](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) von Tealium, um mehr zu erfahren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aktion" }

![Tealium-Konnektor-Aktion „Nutzer:in tracken“ mit Abbildung von Nutzerattributen, Events und Käufen.]({% image_buster /assets/img/tealium/track_user_example.png %})

{% endtab %}
{% tab Nutzer:in löschen – Non-Batch %}

Diese Aktion erlaubt es Ihnen, Nutzer:innen aus dem Braze-Dashboard zu löschen.

| Parameter | Beschreibung |
| ---------- | ----------- |
| Nutzer-ID | Verwenden Sie dieses Feld, um das Tealium-Nutzer-ID-Feld auf das entsprechende Braze-Feld abzubilden. <br><br>- Bilden Sie ein oder mehrere Nutzer-ID-Attribute ab. Wenn mehrere IDs angegeben werden, wird der erste nicht leere Wert in der folgenden Reihenfolge ausgewählt: Externe ID, Braze ID, Alias-Name und Alias-Label.<br>- Wenn Sie einen Nutzer-Alias angeben, sollten sowohl Alias-Name als auch Alias-Label festgelegt werden.<br><br>Weitere Informationen finden Sie unter dem Braze-[Endpunkt `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aktion" }

![Tealium-Konnektor-Aktion „Nutzer:in löschen“ mit Nutzer-ID-Abbildung.]({% image_buster /assets/img/tealium/track_user_delete.png %})

Wenn Sie die von Ihnen gewählten Optionen ändern möchten, wählen Sie **Back** zum Bearbeiten oder **Finish** zum Abschließen.

{% endtab %}
{% endtabs %}

Wählen Sie **Continue**.

Ihr Konnektor wird nun in der Liste der Konnektoren auf Ihrer Tealium-Startseite angezeigt. <br>![Tealium-Startseite mit einer Liste konfigurierter Konnektoren, einschließlich Braze.]({% image_buster /assets/img/tealium/summary_list.png %}){: style="max-width:80%;"}

Stellen Sie sicher, dass Sie **Save / Publish** für Ihren Konnektor auswählen, wenn Sie fertig sind. Die von Ihnen konfigurierten Aktionen werden nun ausgelöst, wenn die Trigger-Verbindungen erfüllt sind.

### 3. Schritt: Testen Sie Ihren Tealium-Konnektor {#step-3-test-your-tealium-connector}

Nachdem Ihr Konnektor betriebsbereit ist, sollten Sie ihn testen, um sicherzustellen, dass er ordnungsgemäß funktioniert. Der einfachste Weg, dies zu testen, ist die Verwendung des Tealium **Trace Tools**. Um Trace nutzen zu können, müssen Sie die Tealium Tools Browser-Erweiterung hinzugefügt haben.

1. Um einen neuen Trace zu starten, wählen Sie **Trace** in der Seitenleiste unter **Server-Side**-Optionen. Wählen Sie **Start** und erfassen Sie die Trace-ID.
2. Öffnen Sie die Browser-Erweiterung und geben Sie die Trace-ID in AudienceStream Trace ein.
3. Prüfen Sie das Realtime-Protokoll.
4. Suchen Sie nach der Aktion, die Sie validieren möchten, indem Sie den Eintrag **Actions Triggered** auswählen und erweitern.
5. Suchen Sie nach der Aktion, die Sie validieren möchten, und sehen Sie sich den Protokollstatus an.

Ausführlichere Anweisungen zur Implementierung des Trace-Tools von Tealium finden Sie in der [Trace-Dokumentation](https://docs.tealium.com/server-side/connectors/trace/about/) von Tealium.

## Demo zur Integration {#integration-demo}

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1mP84vVWifzNMN7eMYNORNy0y-WZurzBs/view?usp=sharing" title="Demo zur Tealium-Integration" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Mögliche Mehrkosten für Datenpunkte {#potential-data-point-overages}

Bei der Integration von Braze über Tealium gibt es drei Hauptwege, wie Sie versehentlich unnötige Datenpunkte protokollieren können:

### Doppelte Daten senden – nur Braze-Deltas von Attributen senden {#sending-duplicate-data-only-send-braze-deltas-of-attributes}

Tealium sendet keine Braze-Deltas von Nutzerattributen. Wenn Sie zum Beispiel eine EventStream-Aktion haben, die den Vornamen, die E-Mail und die Handynummer eines Nutzers bzw. einer Nutzerin trackt, sendet Tealium alle drei Attribute an Braze, sobald die Aktion getriggert wird. Tealium wird nicht danach suchen, was sich geändert hat oder aktualisiert wurde, und nur diese Informationen senden.

**Lösung**: <br>Sie können in Ihrem Backend überprüfen, ob sich ein Attribut geändert hat oder nicht, und wenn ja, die entsprechenden Methoden von Tealium aufrufen, um das Nutzerprofil zu aktualisieren. **Das tun Nutzer:innen, die Braze direkt integrieren, normalerweise auch.** <br>**ODER**<br> Wenn Sie keine eigene Version eines Nutzerprofils in Ihrem Backend speichern und nicht feststellen können, ob sich Attribute ändern oder nicht, können Sie AudienceStream und
[Anreicherungen erstellen](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/), um Nutzerattribute nur zu senden, wenn sich die Werte geändert haben. Siehe die Dokumentation von Tealium zu den [Anreicherungsregeln](https://docs.tealium.com/server-side-connectors/braze-connector/).

### Senden von irrelevanten Daten oder unnötiges Überschreiben von Daten {#sending-irrelevant-data-or-needlessly-overwriting-data}

Wenn Sie mehrere EventStreams haben, die auf denselben Event-Feed zielen, werden **alle für diesen Konnektor aktivierten Aktionen** automatisch ausgelöst, sobald eine einzelne Aktion getriggert wird. Dies könnte auch dazu führen, dass Daten in Braze überschrieben werden und unnötige Datenpunkte protokolliert werden.

**Lösung**: <br>Richten Sie eine separate Event-Spezifikation oder einen Feed ein, um jede Aktion zu tracken. <br>**ODER**<br> Deaktivieren Sie Aktionen (oder Konnektoren), die Sie nicht auslösen möchten, mit den Umschaltern im Tealium-Dashboard.

### Braze zu früh initialisieren {#initializing-braze-too-early}

Wenn Sie Tealium mit dem Braze Web SDK Tag integrieren, können Sie einen dramatischen Anstieg Ihrer MAU verzeichnen. **Wenn Braze beim Laden der Seite initialisiert wird, erstellt Braze jedes Mal ein anonymes Profil, wenn ein:e Webnutzer:in zum ersten Mal auf die Website navigiert.** Dazu gehört auch Bot-Traffic, der Ihre Zahl aktiver Nutzer:innen aufblähen kann. Manche möchten das Nutzerverhalten nur dann tracken, wenn die Nutzer:innen eine Aktion abgeschlossen haben, wie z. B. „Angemeldet“ oder „Video angesehen“, um ihre MAU-Zahl zu senken.

**Lösung**: <br>Richten Sie [Load Rules](https://docs.tealium.com/iq-tag-management/load-rules/about/) ein, um genau zu bestimmen, wann und wo ein Tag auf Ihrer Website geladen wird. Ausführlichere Anleitungen zum Filtern von Bot-Traffic und zur bedingten Initialisierung des SDK finden Sie unter [Bot-Traffic filtern]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_bot-filtering).