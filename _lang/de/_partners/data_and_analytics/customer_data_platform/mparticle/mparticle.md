---
nav_title: mParticle von Rokt
article_title: mParticle von Rokt
alias: /partners/mparticle/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und mParticle, einer Customer Data Platform, die Informationen zwischen Quellen in Ihrem Marketing Stack sammelt und weiterleitet."
page_type: partner
search_tag: Partner

---

# mParticle von Rokt {#mparticle-by-rokt}

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> Mit der Customer Data Platform von mParticle können Sie mehr aus Ihren Daten machen. Anspruchsvolle Marketer nutzen mParticle zur Orchestrierung von Daten in ihrem gesamten Growth Stack, um in den entscheidenden Momenten der Customer Journey zu überzeugen.

Die Integration von Braze und mParticle erlaubt es Ihnen, den Informationsfluss zwischen den beiden Systemen nahtlos zu steuern:
- Synchronisieren Sie mParticle-Zielgruppen mit Braze für die Segmentierung von Campaigns und Canvas.
- Teilen Sie Daten zwischen den beiden Plattformen. Dies kann über die mParticle-Kit-Integration und die Server-zu-Server-Integration erfolgen.
- [Senden Sie Braze-Nutzerinteraktionen über Currents an mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents) und machen Sie sie im gesamten Growth Stack nutzbar.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| mParticle-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [mParticle-Konto](https://app.mparticle.com/login). |
| Braze-Instanz | Ihre Braze-Instanz finden Sie auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics#endpoints) (z. B. `US-01` oder `US-02`). |
| Braze-App-Bezeichner-Schlüssel | Ihr App-Bezeichner-Schlüssel. <br><br>Diesen finden Sie im Braze-Dashboard unter **Einstellungen verwalten** > **API-Schlüssel**. |
| Workspace-Representational State Transfer-API-Schlüssel | (Server-zu-Server) Ein Braze-Representational State Transfer-API-Schlüssel<br><br>Dieser kann im Braze-Dashboard unter **Entwicklungskonsole** > **API-Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### Zielgruppen {#audiences}

Nutzen Sie die Partnerschaft von Braze und mParticle, um Ihre Integration zu konfigurieren und mParticle-Zielgruppen direkt in Braze für Retargeting zu importieren – so entsteht ein vollständiger Datenkreislauf zwischen den beiden Systemen.

Jede Integration, die Sie einrichten, wird Datenpunkte protokollieren. Bei Fragen zu den Details der Braze-Datenpunkte kann Ihr Braze Account Manager:in diese beantworten.

#### Weiterleitung von Zielgruppen {#forwarding-audiences}

mParticle bietet drei Möglichkeiten, Kohorten-Mitgliedschaftsattribute zu setzen, gesteuert durch die Konfigurationseinstellung „[Segmente senden als](#send_settings)“. In den folgenden Abschnitten wird die Verarbeitung jeder Option beschrieben:

- [Einzelnes String-Attribut](#string)
- [Einzelnes Array-Attribut](#array)
- [Ein Attribut pro Segment](#per-segment)
- [Sowohl einzelnes Array-Attribut als auch einzelnes String-Attribut](#both-1)
- [Sowohl einzelnes Array-Attribut als auch ein Attribut pro Segment](#both-2)
- [Sowohl einzelnes String-Attribut als auch ein Attribut pro Segment](#both-3)
- [Einzelnes Array-Attribut, einzelnes String-Attribut und ein Attribut pro Segment](#multi)

##### Einzelnes String-Attribut {#string}

mParticle erstellt ein einzelnes angepasstes Attribut namens `SegmentMembership`. Der Wert dieses Attributs ist ein String aus kommaseparierten mParticle-Zielgruppen-IDs, die dem Nutzer bzw. der Nutzerin zugeordnet sind. Diese Zielgruppen-IDs finden Sie im mParticle-Dashboard unter **Audiences**.

Wenn beispielsweise eine mParticle-Zielgruppe „Ibiza dreamers“ die Zielgruppen-ID „11036“ hat, können Sie diese Nutzer:innen mit dem Filter `SegmentMembership` — `matches regex` — `11036` segmentieren.

Obwohl dies die Standardoption in mParticle ist, entscheiden sich die meisten Unternehmensnutzer:innen für [einzelne Array-Attribute](#array), da diese beim Erstellen von Segmenten in Braze ein besseres Filtererlebnis bieten.

{% alert important %}
Diese Lösung wird nicht empfohlen, wenn Sie mehr als einige wenige Zielgruppen haben, da angepasste Attribute bis zu 255 Zeichen lang sein können. Sie können mit dieser Methode also nicht Dutzende oder Hunderte von Zielgruppen in einem Kundenprofil or Nutzerprofil speichern. Wenn Sie eine große Anzahl von Kohorten pro Nutzer:in haben, empfehlen wir dringend die Konfiguration „Ein Attribut pro Segment“.
{% endalert %}

![mParticle-Segmentmitgliedschaft]({% image_buster /assets/img_archive/mparticle1.png %})

##### Einzelnes Array-Attribut {#array}

mParticle erstellt in Braze für jede:n Nutzer:in ein einzelnes angepasstes Array-Attribut namens `SegmentMembershipArray`. Der Wert dieses Attributs ist ein Array aus mParticle-Zielgruppen-IDs, die dem Nutzer bzw. der Nutzerin zugeordnet sind.

Wenn ein:e Nutzer:in beispielsweise Mitglied von drei mParticle-Zielgruppen mit den Zielgruppen-IDs „13053“, „13052“ und „13051“ ist, können Sie Nutzer:innen, die einer dieser Zielgruppen angehören, mit dem Filter `SegmentMembershipArray` — `includes value` — `13051` segmentieren.

{% alert note %}
Braze-Array-Attribute haben eine standardmäßige Maximallänge von 500. Wenn Nutzer:innen Mitglied von mehr als 500 Zielgruppen sind, kürzt Braze deren Mitgliedschaftsinformationen. Wenden Sie sich für eine Lösung an Ihren Braze Account Manager:in, um den Schwellenwert für die maximale Array-Länge zu erhöhen.
{% endalert %}

##### Ein Attribut pro Segment {#per-segment}

mParticle erstellt für jede Zielgruppe, der ein:e Nutzer:in angehört, ein boolesches angepasstes Attribut. Wenn beispielsweise eine mParticle-Zielgruppe „Possible Parisians“ heißt, können Sie diese Nutzer:innen mit dem Filter `In Possible Parisians` — `equals` — `true` segmentieren.

![Angepasstes mParticle-Attribut]({% image_buster /assets/img_archive/mparticle2.png %})

##### Sowohl einzelnes Array-Attribut als auch einzelnes String-Attribut {#both-1}

mParticle sendet Attribute wie sowohl für das einzelne Array-Attribut als auch für das einzelne String-Attribut beschrieben.

##### Sowohl einzelnes Array-Attribut als auch ein Attribut pro Segment {#both-2}

mParticle sendet Attribute wie sowohl für das einzelne Array-Attribut als auch für ein Attribut pro Segment beschrieben.

##### Sowohl einzelnes String-Attribut als auch ein Attribut pro Segment {#both-3}

mParticle sendet Attribute wie sowohl für das einzelne String-Attribut als auch für ein Attribut pro Segment beschrieben.

##### Einzelnes Array-Attribut, einzelnes String-Attribut und ein Attribut pro Segment {#multi}

mParticle sendet Attribute wie für das einzelne Array-Attribut, das einzelne String-Attribut und ein Attribut pro Segment beschrieben.

#### Schritt 1: Erstellen Sie eine Zielgruppe in mParticle {#send_settings}

So erstellen Sie eine Zielgruppe in mParticle:

1. Navigieren Sie zu **Audiences** > **Single Workspace** > **+ New Audience**.
2. Um Braze als Ausgabe für Ihre Zielgruppe zu verbinden, müssen Sie die folgenden Felder angeben:

| Feldname | Beschreibung |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API key | Zu finden im Braze-Dashboard unter **Settings** > **API Keys**. |
| API key operating system | Wählen Sie aus, welchem Betriebssystem Ihr Braze-API-Schlüssel entspricht. Diese Auswahl begrenzt die Arten von Push-Token / Textbaustein, die bei einem Zielgruppen-Update or aktualisieren weitergeleitet werden. |
| Send segments as | Die Methode zum Senden von Zielgruppen an Braze. Weitere Details finden Sie im Abschnitt [Weiterleitung von Zielgruppen](#forwarding-audiences). |
| Workspace Representational State Transfer API key | Braze-Representational State Transfer-API-Schlüssel mit vollständigen Berechtigungen. Dieser kann im Braze-Dashboard unter **Settings** > **API Keys** erstellt werden. |
| External identity type | Der mParticle-Nutzeridentitätstyp, der als externe ID an Braze weitergeleitet wird. Wir empfehlen, den Standardwert „Customer ID“ beizubehalten. |
| Email identity type | Der mParticle-Nutzeridentitätstyp, der als E-Mail an Braze weitergeleitet wird. |
| Braze instance | Geben Sie an, an welchen Cluster Ihre Braze-Daten weitergeleitet werden sollen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 1: Erstellen Sie eine Zielgruppe in mParticle" }

{:start="3"}
3. Abschließend **speichern** Sie Ihre Zielgruppe.

Innerhalb weniger Minuten sollten Sie sehen, dass Zielgruppen mit Braze synchronisiert werden. Die Zielgruppenmitgliedschaft wird nur für Nutzer:innen mit `external_ids` aktualisiert (also nicht für anonyme Nutzer:innen). Weitere Informationen zum Erstellen von Braze-mParticle-Zielgruppen finden Sie in der mParticle-Dokumentation zu den [Konfigurationseinstellungen](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### Schritt 2: Segmentieren Sie Nutzer:innen in Braze {#step-2-segment-users-in-braze}

Um in Braze ein Segment dieser Nutzer:innen zu erstellen, navigieren Sie zu **Segments** unter **Engagement** und benennen Sie Ihr Segment. Im Folgenden finden Sie zwei Beispiele für Segmente, abhängig von der Option, die Sie für **Send segments as** ausgewählt haben. Weitere Details zu jeder Option finden Sie unter [Weiterleitung von Zielgruppen](#forwarding-audiences).

- **Einzelnes Array-Attribut:** Wählen Sie `SegmentMembershipArray` als Ihren Filter. Verwenden Sie dann die Option „includes value“ und geben Sie Ihre gewünschte Zielgruppen-ID ein. ![mParticle-Segmentfilter „SegmentMembershipArray“ eingestellt auf „includes value“ und Zielgruppen-ID.]({% image_buster /assets/img_archive/mparticle5.png %})<br><br>
- **Ein Attribut pro Segment:** Wählen Sie Ihr angepasstes Attribut als Filter. Verwenden Sie dann die Option „equals“ und wählen Sie die entsprechende Logik. ![mParticle-Segmentfilter „in possible parisians“ eingestellt auf „equals“ und „true“.]({% image_buster /assets/img_archive/mparticle3.png %})

Nach dem Speichern können Sie dieses Segment bei der Erstellung von Canvas oder Campaigns im Schritt zur Nutzer-Zielgruppenauswahl referenzieren.

#### Deaktivieren und Löschen von Verbindungen {#deactivating-and-deleting-connections}

Da mParticle Segmente in Braze nicht direkt verwaltet, werden Segmente nicht gelöscht, wenn die entsprechende mParticle-Zielgruppenverbindung gelöscht oder deaktiviert wird. In diesem Fall aktualisiert mParticle die Zielgruppen-Nutzerattribute in Braze nicht, um die Zielgruppe von jedem Nutzer bzw. jeder Nutzerin zu entfernen.

Um die Zielgruppe vor dem Löschen von einem Braze-Nutzer bzw. einer Braze-Nutzerin zu entfernen, passen Sie die Zielgruppenfilter an, um die Zielgruppengröße auf 0 zu setzen, bevor Sie eine Zielgruppe löschen. Nachdem die Zielgruppenberechnung abgeschlossen ist und 0 Nutzer:innen zurückgibt, löschen Sie die Zielgruppe. Dann wird die Zielgruppenmitgliedschaft in Braze für die Einzelattribut-Option auf `false` aktualisiert oder die Zielgruppen-ID aus dem Array-Format entfernt.

## Daten-Mapping {#data-mapping}

Daten können über die [Embedded-Kit-Integration](#embedded-kit-integration) mit Braze verknüpft werden, wenn Sie Ihre mobilen und Web-Apps über mParticle mit Braze verbinden möchten. Sie können auch die [Server-zu-Server-API-Integration](#server-api-integration) verwenden, um serverseitige Daten an Braze weiterzuleiten.

Unabhängig davon, welchen Ansatz Sie wählen, müssen Sie Braze als Ausgabe einrichten:

### Braze-Ausgabeeinstellungen konfigurieren {#configure-your-braze-output-settings}

Navigieren Sie in mParticle zu **Setup > Outputs > Add Outputs** und wählen Sie **Braze** aus, um die Braze-Kit-Konfiguration zu öffnen. Klicken Sie nach Abschluss auf **Save**.

| Einstellungsname | Beschreibung |
| ------------ | ----------- |
| Braze-App-Identifikationsschlüssel | Ihren Braze-App-Identifikationsschlüssel finden Sie im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. Beachten Sie, dass sich die API-Schlüssel je nach Plattform (iOS, Android und Internet) unterscheiden. |
| Externer Identitätstyp | Der mParticle-Nutzeridentitätstyp, der als externe ID an Braze weitergeleitet wird. Wir empfehlen, den Standardwert „Customer ID“ beizubehalten. |
| E-Mail-Identitätstyp | Der mParticle-Nutzeridentitätstyp, der als E-Mail an Braze weitergeleitet wird. Wir empfehlen, den Standardwert „Email“ beizubehalten. |
| Braze-Instanz | Das Cluster, an das Ihre Braze-Daten weitergeleitet werden; dies sollte dasselbe Cluster sein, auf dem sich Ihr Dashboard befindet. |
| Event-Stream-Weiterleitung aktivieren | (Server-zu-Server) Wenn aktiviert, werden alle Events in Realtime weitergeleitet. Andernfalls werden alle Events gesammelt weitergeleitet. Wenn Sie die Event-Stream-Weiterleitung aktivieren, stellen Sie sicher, dass die an Braze übergebenen Daten die [Rate-Limits]({{site.baseurl}}/api/api_limits) einhalten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze-Ausgabeeinstellungen konfigurieren" }

![mParticle-Braze-Ausgabeeinstellungen mit App-Identifikator, Identitäts-Mapping und Instanz-Feldern.]({% image_buster /assets/img_archive/configure_settings.png %})

### Embedded-Kit-Integration {#embedded-kit-integration}

Über die Embedded-Kit-Integration werden die mParticle- und Braze-SDKs in Ihrer Anwendung vorhanden sein. Im Gegensatz zu einer direkten Braze-Integration übernimmt mParticle jedoch den Aufruf der meisten Braze-SDK or Software-Development-Kit-Methoden für Sie. Die mParticle-Methoden, die Sie zum Tracking von Nutzerdaten verwenden, werden automatisch den Braze-SDK or Software-Development-Kit-Methoden zugeordnet.

Diese Zuordnungen des mParticle-SDKs für [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) und [Internet](https://github.com/mparticle-integrations/mparticle-javascript-integration-braze) sind Open Source und auf der [GitHub-Seite von mParticle](https://github.com/mparticle-integrations) zu finden.

Die Embedded-Kit-SDK or Software-Development-Kit-Integration ermöglicht es Ihnen, unsere vollständige Feature-Suite zu nutzen (Push, In-App-Nachrichten und alle relevanten Nachrichtenanalysen).

{% alert note %}
Für Content Cards und angepasste In-App-Nachricht-Integrationen rufen Sie die Braze-SDK or Software-Development-Kit-Methoden direkt auf.
{% endalert %}

#### Schritt 1: mParticle-SDKs integrieren {#step-1-integrate-the-mparticle-sdks}

Integrieren Sie die entsprechenden mParticle-SDKs in Ihre App basierend auf Ihren Plattformanforderungen:

* [mParticle für Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle für iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle für Internet](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### Schritt 2: mParticle-Braze-Event-Kit-Integration abschließen {#step-2-complete-mparticles-braze-event-kit-integration}

Obwohl das Braze-SDK or Software-Development-Kit für diese mParticle-Integration nicht direkt in Ihre Website oder App eingebunden werden muss, muss das folgende mParticle-Appboy-Kit installiert werden, um Daten von Ihrer App an Braze weiterzuleiten.

Die [Braze-Event-Kit-Integrationsanleitung](https://docs.mparticle.com/integrations/braze/event/#kit-integration) von mParticle führt Sie durch die angepassten mParticle- und Braze-Ausrichtungsanweisungen basierend auf Ihren Messaging-Anforderungen (Push, Standort-Tracking usw.).

#### Schritt 3: Verbindungseinstellungen für Ihre Braze-Ausgabe {#step-3-connections-settings-for-your-braze-output}

Navigieren Sie in mParticle zu **Connections** > **Connect** > **[Gewünschte Plattform]** > **Connect Output**, um Braze als Ausgabe hinzuzufügen. Klicken Sie dann auf **Save**.

![mParticle-Event-Kit-Verbindungseinrichtung für Braze-Ausgabe.]({% image_buster /assets/img_archive/mParticle_event_config.png %})

Nicht alle Verbindungseinstellungen gelten für alle Plattformen und Integrationstypen. Eine Aufschlüsselung der Verbindungseinstellungen und der Plattformen, für die sie gelten, finden Sie in der [Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

### Server-API-Integration {#server-api-integration}

Dies ist eine Erweiterung zur Weiterleitung Ihrer Backend-Daten an Braze, wenn Sie die serverseitigen SDKs von mParticle verwenden (zum Beispiel Ruby, Python usw.). Um diese Server-zu-Server-Integration mit Braze einzurichten, folgen Sie der [Dokumentation von mParticle](https://docs.mparticle.com/guides/platform-guide/connections/).

{% alert important %}
Die Server-zu-Server-Integration unterstützt keine Braze-UI-Features wie In-App-Nachrichten, Content Cards oder Push-Benachrichtigungen. Es gibt auch automatisch erfasste Daten, wie gerätebezogene Felder, die über diese Methode nicht verfügbar sind.

Ziehen Sie eine Side-by-side-Integration in Betracht, wenn Sie diese Features nutzen möchten.

Damit serverseitige Daten an Braze weitergeleitet werden, müssen sie eine `external_id` enthalten; anonyme Nutzer:innen werden nicht weitergeleitet.
{% endalert %}

#### Verbindungseinstellungen für Ihre Braze-Ausgabe {#connections-settings-for-your-braze-output}

Navigieren Sie in mParticle zu **Connections > Connect > [Gewünschte Plattform] > Connect Output**, um Braze als Ausgabe hinzuzufügen. Klicken Sie nach Abschluss auf **Save**.

![mParticle-Verbindungsbildschirm zum Hinzufügen von Braze als Ausgabe auf einer Plattform.]({% image_buster /assets/img_archive/mParticle_connections.png %})

Nicht alle Verbindungseinstellungen gelten für alle Plattformen und Integrationstypen. Eine Aufschlüsselung der Verbindungseinstellungen und der Plattformen, für die sie gelten, finden Sie in der [Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

Bevor Sie „Enriched User Attributes“ oder „Enriched User Identities“ aktivieren, empfehlen wir, den Abschnitt [Mögliche Datenpunkt-Mehrkosten](#potential-data-point-overages) zu lesen, um sicherzustellen, dass Sie die Auswirkungen dieser Einstellungen auf die Datenpunkt-Nutzung kennen.

### Details zum Daten-Mapping {#data-mapping-details}

#### Datentypen {#data-types}
Nicht alle Datentypen werden auf beiden Plattformen unterstützt.
- [Angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events) unterstützen String-, numerische, boolesche oder Datumsobjekte. Arrays oder verschachtelte Objekte werden nicht unterstützt.
- [Angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) unterstützen String-, numerische, boolesche Werte, Datumsobjekte und Arrays, jedoch keine Objekte oder verschachtelten Objekte.

{% alert note %}
Braze unterstützt keine Zeitstempel vor dem Jahr 0 oder nach dem Jahr 3000 in angepassten Attributen vom Typ `Time`. Braze nimmt diese Werte auf, wenn sie von mParticle gesendet werden, speichert den Wert jedoch als String.
{% endalert %}

#### Daten-Mapping

| mParticle-Datentyp | Braze-Datentyp | Beschreibung |
| ------------------- | --------------- | ----------- |
| Nutzerattribute (reserviert) | Standardattribut | Zum Beispiel wird der reservierte Nutzerattribut-Schlüssel `$FirstName` von mParticle dem Standardattributfeld `first_name` in Braze zugeordnet. |
| Nutzerattribute (sonstige) | Angepasstes Attribut | Alle an mParticle übergebenen Nutzerattribute, die außerhalb der reservierten Nutzerattribut-Schlüssel liegen, werden in Braze als angepasstes Attribut protokolliert.<br><br>Nutzerattribute unterstützen String-, numerische, boolesche Werte, Datumswerte und Arrays, jedoch keine Objekte oder verschachtelten Objekte. |
| Angepasstes Event | Angepasstes Event | Angepasste mParticle-Events werden von Braze als angepasstes Event erkannt. Event-Attribute werden als angepasste Event-Eigenschaften weitergeleitet.<br><br>Event-Attribute, die als Event-Eigenschaften an Braze übergeben werden, unterstützen String-, numerische, boolesche oder Datumsobjekte, jedoch keine Arrays oder verschachtelten Objekte. |
| Kauf-Commerce-Event | Kauf-Event | Kauf-Commerce-Events werden Braze-Kauf-Events zugeordnet.<br><br>Schalten Sie den Einstellungswert für „Bundle Commerce Event Data“ um, um Käufe auf Bestell- oder Produktebene zu protokollieren. Wenn beispielsweise `false`, würde ein einzelnes eingehendes Event mit zwei eindeutigen Produkten, Aktionen oder Impressionen zu mindestens zwei ausgehenden Braze-Events führen. Bei `true` würde ein einzelnes ausgehendes Event mit einem verschachtelten Produkt-, Aktions- bzw. Impressions-Array entstehen.<br><br>Weitere Informationen zu den zusätzlichen Commerce-Feldern, die protokolliert werden, finden Sie in der [Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/event/#purchase-events).<br><br>Wenn „Bundle Commerce Event Data“ auf `false` gesetzt ist, unterstützen Produktattribute, die als Kauf-Event-Eigenschaften an Braze übergeben werden, String-, numerische, boolesche oder Datumsobjekte, jedoch keine Arrays oder verschachtelten Objekte. |
| Alle anderen Commerce-Events | Angepasstes Event | Alle anderen Commerce-Events werden angepassten Events zugeordnet.<br><br>Schalten Sie den Einstellungswert für „Bundle Commerce Event Data“ um, um Käufe auf Bestell- oder Produktebene zu protokollieren. Wenn beispielsweise `false`, würde ein einzelnes eingehendes Event mit zwei eindeutigen Produkten, Aktionen oder Impressionen zu mindestens zwei ausgehenden Braze-Events führen. Bei `true` würde ein einzelnes ausgehendes Event mit einem verschachtelten Produkt-, Aktions- bzw. Impressions-Array entstehen.<br><br>Zusätzlich zu bestimmten Standard-Commerce-Werten werden Produktattribute als Braze-Event-Eigenschaften protokolliert. Weitere Informationen zu den zusätzlichen Commerce-Feldern, die protokolliert werden, finden Sie in der [Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events).<br><br>Wenn „Bundle Commerce Event Data“ auf `false` gesetzt ist, unterstützen Produktattribute, die als Event-Eigenschaften an Braze übergeben werden, String-, numerische, boolesche oder Datumsobjekte, jedoch keine Arrays oder verschachtelten Objekte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Daten-Mapping" }

#### Nutzeridentitäts-Mapping {#user-identity-mapping}
Für jede mParticle-Ausgabe können Sie den externen Identitätstyp auswählen, der als `external_id` an Braze gesendet wird. Der Standardwert ist die Customer ID, Sie können jedoch auch eine andere ID wie `MPID` zuordnen, um sie als `external_id` an Braze zu senden. Beachten Sie, dass die Wahl eines anderen Bezeichners als der Customer ID beeinflussen kann, wie Daten in Braze gesendet werden.

Zum Beispiel hat die Zuordnung von MPID zu Ihrer Braze-`external_id` folgende Auswirkungen:
- Aufgrund der Art und Weise, wie MPID zugewiesen wird, erhalten alle Nutzer:innen beim Sitzungsstart eine `external_id`.
- Die Currents-Einrichtung erfordert möglicherweise ein zusätzliches Mapping aufgrund unterschiedlicher Datentypen zwischen MPID und `external_id`.

### Weiterleitung von Löschanfragen (Betroffenenanfragen) {#forwarding-erasure-requests-data-subject-requests}

Leiten Sie Löschanfragen an Braze weiter, indem Sie eine Betroffenenanfrage-Ausgabe für Braze konfigurieren. Um Löschanfragen an Braze weiterzuleiten, folgen Sie der [Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/forwarding-dsr/).

## Mögliche Datenpunkt-Mehrkosten {#potential-data-point-overages}

### Angereicherte Nutzer:innen-Attribute {#enriched-user-attributes}

#### Angereicherte Nutzer:innen-Attribute/-Identitäten aktivieren (nur Server-zu-Server) {#enriched}

In den mParticle-Verbindungseinstellungen empfiehlt Braze, **Include Enriched User Attributes** zu deaktivieren. Wenn diese Option aktiviert ist, leitet mParticle bei jedem protokollierten Event alle verfügbaren Nutzer:innen-Attribute (wie Standardattribute, angepasste Attribute und berechnete Attribute) aus dem bestehenden Profil an Braze weiter. Dies führt zu einem hohen Datenpunktverbrauch, da mParticle bei jedem Aufruf dieselben unveränderten Attribute an Braze sendet.

Wenn beispielsweise ein:e Nutzer:in während der ersten Sitzung Vorname, Nachname und Telefonnummer hinzufügt und sich später für einen Newsletter anmeldet, wobei dieselben Informationen und eine E-Mail-Adresse übermittelt werden und ein Newsletter-Anmelde-Event ausgelöst wird:
- Bei aktivierter Option (Standard) fallen fünf Datenpunkte an. (Anmelde-Event, E-Mail-Adresse, Vorname, Nachname und Telefonnummer)
- Bei deaktivierter Option fallen zwei Datenpunkte an (Anmelde-Event und E-Mail-Adresse)

{% alert note %}
Das Deaktivieren dieser Einstellung prüft nicht auf geänderte Daten. Es verhindert jedoch, dass die Integration alle Nutzer:innen-Attribute im Profil sendet, die nicht im ursprünglichen eingehenden Batch empfangen oder explizit als Attribut für das Event festgelegt wurden. Es ist wichtig, weiterhin sicherzustellen, dass nur Deltas an Braze übergeben werden.
{% endalert %}

#### Überlegungen beim Deaktivieren angereicherter Nutzer:innen-Attribute {#considerations-of-turning-off-enriched-user-attributes}

Es gibt einige Punkte, die beim Deaktivieren von **Include Enriched User Attributes** zu beachten sind:
1. Die Server-zu-Server-Integration nutzt die mParticle Events API, um Events an Braze zu senden. Jede Anfrage wird durch ein Event ausgelöst. Wenn ein Nutzer:innen-Attribut geändert wird, z. B. durch Aktualisierung einer E-Mail-Adresse, aber nicht mit einem bestimmten Event verknüpft ist (beispielsweise ein angepasstes Profilaktualisierungs-Event), wird der neue Wert nur als „angereichertes Attribut“ im Payload des nächsten vom/von der Nutzer:in ausgelösten Events an eine Ausgabe wie Braze übergeben. Wenn **Include Enriched User Attributes** deaktiviert ist, wird dieser neue Attributwert, der keinem bestimmten Event zugeordnet ist, nicht an Braze übergeben.
  - Um dieses Problem zu lösen, empfehlen wir, ein separates Event „user attribute updated“ zu erstellen, das nur die spezifischen aktualisierten Nutzer:innen-Attribute an Braze sendet. Beachten Sie, dass bei diesem Ansatz zwar ein zusätzlicher Datenpunkt für das Event „user attribute updated“ anfällt, der Datenpunktverbrauch aber deutlich geringer ist als das Senden aller Nutzer:innen-Attribute bei jedem Aufruf mit aktiviertem Feature.
2. Berechnete Attribute werden als angereichertes Nutzer:innen-Attribut an Braze übergeben. Wenn „Enriched User Attributes“ deaktiviert ist, werden diese nicht mehr an Braze weitergeleitet. Um berechnete Attribute bei deaktivierter Option „Enriched User Attributes“ an Braze zu übermitteln, kann ein [Calculated-Attribute-Feed](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed) helfen, ohne alle Attribute zu übertragen. Der Feed löst eine nachgelagerte Aktualisierung an Braze aus, wenn sich ein berechnetes Attribut ändert.

## Fehlerbehebung {#troubleshooting}

### Fehlerbehebung bei iOS-Push-Benachrichtigungen mit dem Braze-Event-Kit {#troubleshooting-ios-push-notifications-with-the-braze-event-kit}

Wenn Push-Benachrichtigungen bei Verwendung des Braze-Event-Kits (Embedded-Kit-Integration) unter iOS nicht funktionieren, überprüfen Sie Folgendes:
1. **Push-Token / Textbaustein-Weiterleitung:** Bestätigen Sie, dass mParticle Push-Token / Textbaustein an Braze weiterleitet. Überprüfen Sie in Ihrem mParticle-Dashboard, dass bei der Braze-Kit-Verbindung Push aktiviert ist und dass die korrekte Apple-Push-Berechtigung im Braze-Dashboard konfiguriert ist.
2. **Kit-Initialisierungsreihenfolge:** Das Braze-Kit muss initialisiert werden, bevor Ihre App Push-Berechtigungen anfordert. Wenn Push-Berechtigungen angefordert werden, bevor das Kit aktiv ist, wird der Push-Token / Textbaustein möglicherweise nicht an Braze weitergeleitet. Stellen Sie sicher, dass das mParticle SDK or Software-Development-Kit frühzeitig im App-Lebenszyklus gestartet wird.
3. **Method Swizzling:** Das mParticle Apple Kit verwendet Method Swizzling, um Push-Token / Textbaustein automatisch weiterzuleiten und Push-Benachrichtigungs-Events zu verarbeiten. Wenn Sie Swizzling deaktiviert haben oder ein anderes SDK or Software-Development-Kit Konflikte verursacht, erreichen die Push-Token / Textbaustein Braze möglicherweise nicht. Überprüfen Sie, dass Swizzling in Ihrer mParticle-Konfiguration aktiviert ist.
4. **Manuelle Token / Textbaustein-Verarbeitung:** Wenn Sie Push-Token / Textbaustein manuell verwalten (z. B. durch Implementierung von `application:didRegisterForRemoteNotificationsWithDeviceToken:`), stellen Sie sicher, dass Sie den Token / Textbaustein an mParticle übergeben, indem Sie ihn der Push-Benachrichtigungs-Token / Textbaustein-Eigenschaft zuweisen, zum Beispiel: `MParticle.sharedInstance().pushNotificationToken = deviceToken`. Das Kit leitet ihn dann an Braze weiter.
5. **Umgebungsdiskrepanz:** Bestätigen Sie, dass die APNs-Berechtigungsumgebung (Entwicklung vs. Produktion) mit dem Build Ihrer App übereinstimmt. Weitere Details finden Sie unter [Fehlerbehebung bei iOS-Push]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift).
6. **Zeitpunkt der Kit-Initialisierung:** Wenn Sie in `didFinishLaunchingWithOptions` auf die Braze-Instanz zugreifen, ist das mParticle-Kit möglicherweise noch nicht bereit, wenn eine Push-Benachrichtigung eintrifft. Initialisieren Sie die Push-Verarbeitung in [`userNotificationCenter(_:didReceive:withCompletionHandler:)`]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) (oder dem entsprechenden Benachrichtigungsantwort-Delegate), damit das Braze-Kit aktiv ist, wenn Nutzer:innen eine Benachrichtigung öffnen.

### Unnötige oder doppelte Daten an Braze senden {#sending-unnecessary-or-duplicate-data-to-braze}
Braze zählt jedes Mal einen Datenpunkt, wenn ein Attribut an Braze übergeben wird, auch wenn sich der Wert nicht geändert hat. Aus diesem Grund empfiehlt Braze, nur die Daten weiterzuleiten, auf die innerhalb von Braze reagiert werden muss, und sicherzustellen, dass nur Deltas von Attributen übergeben werden.

### Events werden in Braze nicht angezeigt {#events-are-not-appearing-in-braze}

Wenn mParticle-Events oder -Attribute in Braze fehlen, liegt das Problem häufig an einer Fehlkonfiguration in Ihrer mParticle-Verbindung oder im Event-Mapping – nicht an einem Braze-Ausfall. Überprüfen Sie Folgendes:

- **Verbindungsausgabe:** Bestätigen Sie, dass Braze als Ausgabe für die betreffende Verbindung aktiviert ist und dass die korrekte Braze-Instanz, der App-Bezeichner und der Representational State Transfer-API-Schlüssel konfiguriert sind.
- **Identity-Mapping:** Server-zu-Server- und Zielgruppen-Synchronisierungen erfordern eine `external_id`. Anonyme Nutzer:innen werden nicht weitergeleitet.
- **Event-Mapping:** Überprüfen Sie, ob Events an die Braze-Ausgabe geleitet werden und ob nicht unterstützte Datentypen (verschachtelte Objekte, Arrays in Event-Eigenschaften) verworfen werden.

Wenn die Konfiguration korrekt aussieht, aber Daten trotzdem nicht ankommen, wenden Sie sich an den [mParticle-Support](https://support.mparticle.com/), um die Zustellungsprotokolle auf deren Seite zu überprüfen.