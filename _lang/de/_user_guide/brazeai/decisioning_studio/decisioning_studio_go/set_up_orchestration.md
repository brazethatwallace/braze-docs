---
nav_title: Orchestrierung einrichten
article_title: Orchestrierung einrichten
page_order: 2
description: "Erfahren Sie, wie Sie BrazeAI Decisioning Studio Go mit Ihrer Customer-Engagement-Plattform verbinden, um personalisierte Kommunikation zu ermöglichen."
toc_headers: h2
---

# Orchestrierung einrichten {#set-up-orchestration}

> BrazeAI Decisioning Studio™ Go muss mit Ihrer Customer-Engagement-Plattform (CEP) verbunden sein, um personalisierte Kommunikation zu orchestrieren. Dieser Artikel erläutert, wie Sie die Integration für jede unterstützte CEP einrichten.

## Unterstützte CEPs {#supported-ceps}

Decisioning Studio Go unterstützt die folgenden Customer-Engagement-Plattformen:

| CEP | Integrationstyp | Wichtigste Features |
|-----|-----------------|--------------|
| **Braze** | Per API getriggerte Campaigns | Native Integration, Realtime-Triggering |
| **Salesforce Marketing Cloud** | Journey Builder mit API-Events | Automatisierung von SQL-Anfragen, Data Extensions |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unterstützte CEPs" }

Wählen Sie unten Ihre CEP aus, um mit der Integration zu beginnen.

{% tabs %}
{% tab Braze %}

## Einrichtung der Braze-Integration {#set-up-braze-integration}

Um Decisioning Studio Go in Braze zu integrieren, erstellen Sie einen API-Schlüssel, konfigurieren eine per API getriggerte Campaign und stellen die erforderlichen Bezeichner im Decisioning Studio Go-Portal bereit.

### 1. Schritt: Einen REST-API-Schlüssel erstellen {#step-1-create-a-rest-api-key}

1. Gehen Sie im Braze-Dashboard zu **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**.
2. Wählen Sie **API-Schlüssel erstellen**.
3. Geben Sie einen Namen für Ihren API-Schlüssel ein. Ein Beispiel ist „DecisioningStudioGoEmail“.
4. Wählen Sie die Berechtigungen anhand der folgenden Kategorien aus:
    - **Nutzerdaten:** Wählen Sie `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Nachrichten:** Wählen Sie `messages.send`
    - **Campaigns:** Wählen Sie alle aufgeführten Berechtigungen
    - **Canvas:** Wählen Sie alle aufgeführten Berechtigungen
    - **Segments:** Wählen Sie alle aufgeführten Berechtigungen
    - **Templates:** Wählen Sie alle aufgeführten Berechtigungen

{: start="5"}
5. Wählen Sie **API-Schlüssel erstellen**.
6. Kopieren Sie den API-Schlüssel und fügen Sie ihn in Ihr BrazeAI Decisioning Studio™ Go-Portal ein.

### 2. Schritt: Ihren E-Mail-Anzeigenamen ermitteln {#step-2-locate-your-email-display-name}

1. Gehen Sie im Braze-Dashboard zu **Einstellungen** > **E-Mail-Präferenzen**.
2. Suchen Sie den Anzeigenamen, der mit BrazeAI Decisioning Studio™ Go verwendet werden soll.
3. Kopieren Sie den **Absender-Anzeigenamen** und fügen Sie ihn als **E-Mail-Anzeigename** in das BrazeAI Decisioning Studio™ Go-Portal ein.
4. Kopieren Sie die zugehörige E-Mail-Adresse und fügen Sie sie als **Absender-E-Mail-Adresse** in Ihr BrazeAI Decisioning Studio™ Go-Portal ein – diese setzt sich aus dem lokalen Teil und der Domain zusammen.

### 3. Schritt: Ihre Braze-URL und App-ID ermitteln {#step-3-find-your-braze-url-and-app-id}

**So finden Sie Ihre Braze-URL:**
1. Gehen Sie zum Braze-Dashboard.
2. In Ihrem Browserfenster beginnt Ihre Braze-URL mit `https://` und endet mit `braze.com`. Ein Beispiel für eine Braze-URL ist `https://dashboard-01.braze.com`.

**So finden Sie Ihre App-ID (API-Schlüssel):**

{% alert note %}
Braze stellt App-IDs (im Braze-Dashboard als API-Schlüssel bezeichnet) zur Verfügung, die Sie für Tracking-Zwecke verwenden können, beispielsweise um Aktivitäten mit einer bestimmten App in Ihrem Workspace zu verknüpfen. Bei Verwendung von App-IDs unterstützt BrazeAI Decisioning Studio™ Go die Zuordnung einer App-ID zu jedem Experimenter.<br><br>Wenn Sie keine App-IDs verwenden, können Sie einen beliebigen String als Platzhalter eingeben.
{% endalert %}

1. Gehen Sie im Braze-Dashboard zu **Einstellungen** > **App-Einstellungen**.
2. Navigieren Sie zu der App, die Sie tracken möchten.
3. Kopieren Sie den **API-Schlüssel** und fügen Sie ihn in Ihr BrazeAI Decisioning Studio™ Go-Portal ein.

### 4. Schritt: Eine per API getriggerte Campaign erstellen {#step-4-create-an-api-triggered-campaign}

1. Gehen Sie im Braze-Dashboard zu **Messaging** > **Campaigns**.
2. Wählen Sie **Kampagne erstellen**.
3. Wählen Sie als Campaign-Typ **API-Kampagne**.
4. Geben Sie einen Namen für Ihre Campaign ein. Ein Beispiel ist „Decisioning Studio Go Email“.

![Eine API-Kampagne mit dem Namen „Decisioning Studio Go Email“.]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5. Wählen Sie als Messaging-Kanal **E-Mail**.

![Option zum Auswählen Ihres Messaging-Kanals für die API-Kampagne.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6. Aktivieren Sie unter **Zusätzliche Optionen** das Kontrollkästchen **Nutzer:innen erlauben, erneut für die Campaign in Frage zu kommen**.
7. Geben Sie als Zeit für die erneute Berechtigung **1** ein und wählen Sie **Stunden** aus dem Dropdown-Menü.

![Wiederwahlberechtigung für die ausgewählte API-Kampagne.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8. Wählen Sie **Campaign speichern**.

### 5. Schritt: Ihre Campaign- und Nachrichten-IDs kopieren {#step-5-copy-your-campaign-and-message-ids}

1. Kopieren Sie in Ihrer API-Kampagne die **Campaign-ID**. Gehen Sie dann zum BrazeAI Decisioning Studio™ Go-Portal und fügen Sie die **Campaign-ID** ein.

![Ein Beispiel für eine Nachrichtenvarianten-ID zum Kopieren und Einfügen.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2. Kopieren Sie die **Nachrichtenvarianten-ID**. Gehen Sie dann zum BrazeAI Decisioning Studio™ Go-Portal und fügen Sie die **Nachrichtenvarianten-ID** ein.

### 6. Schritt: Eine Testnutzer:in-ID ermitteln {#step-6-locate-a-test-user-id}

Um Ihre Integration zu testen, benötigen Sie eine Nutzer-ID:

Wenn Ihr Workspace [Verschlüsselung auf Bezeichner-Feldebene]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption/) verwendet, muss jede neue Testnutzer:in, die Sie über den `/users/track`-Endpunkt erstellen, die E-Mail-Anforderungen für verschlüsselte Workspaces erfüllen. Senden Sie das Feld `email` als Base64-kodierten HMAC-SHA256-Hash des kleingeschriebenen E-Mail-Werts und `email_encrypted` als den mit Ihren konfigurierten PII-Verschlüsselungsschlüsseln verschlüsselten E-Mail-Wert.

1. Gehen Sie im Braze-Dashboard zu **Zielgruppe** > **Nutzer:innen suchen**.
2. Suchen Sie die Nutzer:in anhand der externen Nutzer-ID, des Nutzer-Alias, der E-Mail-Adresse, der Telefonnummer oder des Push-Tokens.
3. Kopieren Sie die Nutzer-ID, um sie in Ihrer Einrichtung zu referenzieren.

![Beispiel für ein Nutzerprofil, das durch Suche anhand der ID gefunden wurde.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Einrichtung der SFMC-Integration {#set-up-sfmc-integration}

Um Decisioning Studio Go in Salesforce Marketing Cloud zu integrieren, richten Sie ein App-Paket ein, erstellen eine Automatisierung für Datenabfragen und bauen eine Journey zur Verarbeitung getriggerter Sendungen auf.

### Teil 1: Ein SFMC-App-Paket einrichten {#part-1-set-up-an-sfmc-app-package}

1. Gehen Sie zu Ihrer Marketing Cloud-Startseite.
2. Öffnen Sie das Menü in der globalen Kopfzeile und wählen Sie **Setup**.
3. Navigieren Sie im Seitenmenü unter **Platform Tools** zu **Apps** und wählen Sie **Installed Packages**.
4. Wählen Sie **New**, um ein App-Paket zu erstellen.
5. Geben Sie dem App-Paket einen Namen und eine Beschreibung.

![Ein App-Paket mit dem Namen „Experimenter 1 - Test 5“.]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6. Wählen Sie **Add Component**.
7. Wählen Sie als **Component Type** die Option **API Integration**. Wählen Sie dann **Next**.
8. Wählen Sie als **Integration Type** die Option **Server-to-server**. Wählen Sie dann **Next**.
9. Wählen Sie ausschließlich die folgenden empfohlenen Berechtigungsbereiche für Ihr App-Paket:
    - Channels > Email > Read, Write, Send
    - Channels > OTT > Read
    - Channels > Push > Read
    - Channels > SMS > Read
    - Channels > Social > Read
    - Channels > Web > Read
    - Assets > Documents and Images > Read, Write
    - Assets > Saved Content > Read, Write
    - Automation > Automations > Read, Write, Execute
    - Automation > Journeys > Read, Write, Execute, Activate/Stop/Pause/Send/Schedule
    - Contacts > Audiences > Read
    - Contacts > List and Subscribers > Read, Write
    - Cross Cloud Platform > Market Audience > View
    - Cross Cloud Platform > Market Audience Member > View
    - Cross Cloud Platform > Marketing Cloud Connect > Read
    - Data > Data Extensions > Read, Write
    - Data > File Locations > Read
    - Data > Tracking Events > Read, Write
    - Event notifications > Callbacks > Read
    - Event notifications > Subscriptions > Read

{% details Bild der empfohlenen Berechtigungsbereiche anzeigen %}

![Die empfohlenen Berechtigungsbereiche für das Salesforce Marketing Cloud-App-Paket.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10. Wählen Sie **Save**.
11. Kopieren Sie die folgenden Felder und fügen Sie sie in das BrazeAI Decisioning Studio™ Go-Portal ein: **Client Id**, **Client Secret**, **Authentication Base URI**, **REST Base URI**, **SOAP Base URI**.

### Teil 2: Eine Automatisierung für Datenabfragen einrichten {#part-2-set-up-a-data-query-automation}

#### 1. Schritt: Eine neue Automatisierung erstellen {#step-1-create-a-new-automation}

1. Gehen Sie von Ihrer Salesforce Marketing Cloud-Startseite zu **Journey Builder** und wählen Sie **Automation Studio**.

![Option „Automation Studio“ in der Journey Builder-Navigation.]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2. Wählen Sie **New Automation**.
3. Ziehen Sie einen **Schedule**-Knoten per Drag-and-Drop als **Starting Source**.

![„Schedule“ als Startquelle einer Journey.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4. Wählen Sie im **Schedule**-Knoten die Option **Configure**.
5. Legen Sie Folgendes für den Zeitplan fest:
    - **Start Date:** Der morgige Kalendertag
    - **Time:** **12:00 AM**
    - **Time Zone:** **(GMT-05:00) Eastern (US & Canada)**
6. Wählen Sie für **Repeat** die Option **Daily**.
7. Stellen Sie den Zeitplan so ein, dass er niemals endet.
8. Wählen Sie **Done**, um den Zeitplan zu speichern.

![Ein Beispielzeitplan für den 25. Januar 2024 um 12 Uhr ET, der sich täglich wiederholt.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### 2. Schritt: Ihre SQL-Anfragen erstellen {#step-2-create-your-sql-queries}

Erstellen Sie als Nächstes zwei SQL-Anfragen: eine Abonnent:innen-Abfrage und eine Engagement-Abfrage. Diese Abfragen ermöglichen es BrazeAI Decisioning Studio™ Go, Daten abzurufen, um die Zielgruppe zu befüllen und Engagement-Events zu erfassen.

**Abonnent:innen-Abfrage:**

1. Ziehen Sie eine **SQL Query** per Drag-and-Drop auf die Arbeitsfläche.
2. Wählen Sie **Choose**.
3. Wählen Sie **Create New Query Activity**.
4. Geben Sie der Abfrage einen Namen und einen externen Schlüssel. Wir empfehlen, den vorgeschlagenen Namen und externen Schlüssel für die Abonnent:innen-Abfrage zu verwenden, die in Ihrem BrazeAI Decisioning Studio™ Go-Portal angegeben sind.

![Ein Beispiel „OFE_Subscribers_query_Test5“ und der externe Schlüssel.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5. Wählen Sie **Next**.
6. Suchen Sie in Ihrem BrazeAI Decisioning Studio™ Go-Portal die Systemdaten-SQL-Abfrage unter **Subscriber Query Resources**.
7. Kopieren Sie die Abfrage in das Textfeld und wählen Sie **Next**.

![Eine Beispielabfrage im Abschnitt „SQL Query“.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8. Suchen Sie in Ihrem BrazeAI Decisioning Studio™ Go-Portal im Abschnitt **Resources to use** den externen Schlüssel der Ziel-Data-Extension. Fügen Sie ihn dann in die Suchleiste ein.

![Ein externer Schlüssel, der in die Suchleiste eingefügt wurde.]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9. Wählen Sie die Data Extension aus, die mit dem gesuchten externen Schlüssel übereinstimmt. Der Name der Ziel-Data-Extension wird ebenfalls in Ihrem BrazeAI Decisioning Studio™ Go-Portal zur Gegenprüfung angegeben. Die **Data Extension** für die Abonnent:innen-Abfrage sollte mit dem Suffix `BASE_AUDIENCE_DATA` enden.

![Der Name der Data Extension, der mit dem externen Beispielschlüssel übereinstimmt.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10. Wählen Sie **Overwrite** und dann **Next**.

**Engagement-Abfrage:**

1. Ziehen Sie eine **SQL Query** per Drag-and-Drop auf die Arbeitsfläche.

![„SQL Query“ als Aktivität in der Journey hinzugefügt.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2. Wählen Sie **Choose**.
3. Wählen Sie **Create New Query Activity**.
4. Geben Sie der Abfrage einen Namen und einen externen Schlüssel. Wir empfehlen, den vorgeschlagenen Namen und externen Schlüssel für die Engagement-Abfrage zu verwenden, die in Ihrem BrazeAI Decisioning Studio™ Go-Portal bereitgestellt werden.

![Ein Beispiel „OFE_Engagement_query“ und der externe Schlüssel.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5. Wählen Sie **Next**.
6. Suchen Sie in Ihrem BrazeAI Decisioning Studio™ Go-Portal die Systemdaten-SQL-Abfrage unter **Engagement Query Resources**.
7. Kopieren Sie die Abfrage in das Textfeld und wählen Sie **Next**.

![Eine Beispielabfrage im Abschnitt „SQL Query“.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8. Suchen und wählen Sie die Ziel-Data-Extension für die Engagement-Abfrage aus, die in Ihrem BrazeAI Decisioning Studio™ Go-Portal angegeben ist.

{% alert tip %}
Der Name der Ziel-Data-Extension wird ebenfalls in Ihrem BrazeAI Decisioning Studio™ Go-Portal zur Gegenprüfung angegeben. Stellen Sie sicher, dass Sie die richtige Data Extension für die Engagement-Abfrage betrachten. Die **Data Extension** für die Engagement-Abfrage sollte mit dem Suffix ENGAGEMENT_DATA enden.
{% endalert %}

{: start="9"}
9. Wählen Sie **Overwrite** und dann **Next**.

![Der Name der Data Extension, der mit dem externen Beispielschlüssel übereinstimmt.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### 3. Schritt: Die Automatisierung ausführen {#step-3-run-the-automation}

1. Geben Sie der Automatisierung einen Namen und wählen Sie **Save**.

![Eine Beispielautomatisierung „OFE_Experimenter_Test5_Automation“.]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2. Wählen Sie dann **Run Once**, um zu bestätigen, dass alles wie erwartet funktioniert.
3. Wählen Sie beide Abfragen aus und wählen Sie **Run**.

![Eine Automatisierung „OFE_Experimenter_Test5_Automation“ mit einer Liste ausgewählter SQL-Abfrageaktivitäten zur Ausführung.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4. Wählen Sie **Run Now**.

![Eine ausgewählte SQL-Abfrageaktivität.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Nun können Sie überprüfen, ob die Automatisierung erfolgreich ausgeführt wird. Kontaktieren Sie den Braze-Support für weitere Unterstützung, wenn Ihre Automatisierung nicht wie erwartet funktioniert.

### Teil 3: Ihre SFMC-Journey erstellen {#part-3-create-your-sfmc-journey}

#### 1. Schritt: Die Journey einrichten {#step-1-set-up-the-journey}

1. Gehen Sie in Salesforce Marketing Cloud zu **Journey Builder** > **Journey Builder**.
2. Wählen Sie **Create New Journey**.
3. Wählen Sie als Journey-Typ **Multi-Step Journey** und dann **Create**.

![Eine API-Event-Eingangsquelle, die mit einem Decision-Split-Knoten und mehreren E-Mail-Knoten verbunden ist.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### 2. Schritt: Die Journey aufbauen {#step-2-build-the-journey}

**Eingangsquelle erstellen:**

1. Ziehen Sie als Eingangsquelle **API Event** in den Journey Builder.

![„API Event“ als Eingangsquelle ausgewählt.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2. Wählen Sie im **API Event** die Option **Create an event**.

![Die Option „Create an event“ im API Event.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3. Wählen Sie **Select Data Extension**. Suchen und wählen Sie die Data Extension aus, in die BrazeAI Decisioning Studio™ Go Empfehlungen schreiben wird.
4. Wählen Sie **Summary**, um Ihre Änderungen zu speichern.
5. Wählen Sie **Done**, um das API-Event zu speichern.

![Zusammenfassung des API-Events.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**Einen Decision-Split hinzufügen:**

1. Ziehen Sie einen **Decision-Split** per Drag-and-Drop hinter das **API Entry Event**.
2. Wählen Sie in den **Decision-Split**-Details für den ersten Pfad die Option **Edit**.

![Decision-Split-Details mit dem Button „Edit“.]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3. Aktualisieren Sie den **Decision-Split**, um die von der Empfehlungs-Data-Extension übergebene Template-ID zu verwenden. Suchen Sie das entsprechende Feld unter **Journey Data**.

![Der Abschnitt „Journey Data“ in Pfad 1 des Decision-Splits.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4. Wählen Sie Ihr Eingangsevent aus und suchen Sie das gewünschte Template-ID-Feld. Ziehen Sie es dann in den Arbeitsbereich.

![Die einzufügende E-Mail-Template-ID.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5. Geben Sie die Template-ID Ihres ersten E-Mail-Templates ein und wählen Sie **Done**.
6. Wählen Sie **Summary**, um diesen Pfad zu speichern.
7. Fügen Sie für jedes Ihrer E-Mail-Templates einen Pfad hinzu und wiederholen Sie die Schritte 4–6, um die Filterkriterien so festzulegen, dass die Template-ID mit dem ID-Wert jedes Templates übereinstimmt.
8. Wählen Sie **Done**, um den **Decision-Split**-Knoten zu speichern.

![Zwei Pfade in einem Decision-Split für jede E-Mail-Template-ID.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**Eine E-Mail für jeden Decision-Split hinzufügen:**

1. Ziehen Sie einen **Email**-Knoten in jeden Pfad des **Decision-Splits**.
2. Wählen Sie **Email** und dann das entsprechende Template, das in jeden Pfad gehört (d. h. das Template, dessen ID-Wert mit der Logik in Ihrem Decision-Split übereinstimmt).

![Ein E-Mail-Knoten, der zur Journey hinzugefügt wurde.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### 3. Schritt: Die Journey aktivieren {#step-3-activate-the-journey}

Nachdem Sie Ihre Journey eingerichtet haben, aktivieren Sie sie und teilen Sie dem BrazeAI Decisioning Studio™ Go-Team die folgenden Details mit:

* Journey-ID
* Journey-Name
* API-Event-Definitionsschlüssel
* Externer Schlüssel der Empfehlungs-Data-Extension

{% alert note %}
Das BrazeAI Decisioning Studio™ Go-Portal zeigt Ihnen die SFMC-Automatisierung, die bereitgestellt wurde, um einmal täglich die Abonnent:innen- und Engagement-Daten zu exportieren. Wenn Sie diese Automatisierung in SFMC öffnen, stellen Sie sicher, dass Sie die Pause aufheben und sie wieder auf „Live“ setzen.
{% endalert %}

1. Kopieren Sie im BrazeAI Decisioning Studio™ Go-Portal den **Journey-Namen**.
2. Fügen Sie dann im Salesforce Marketing Cloud Journey Builder den Journey-Namen in die Suchleiste ein.
3. Wählen Sie den Journey-Namen aus. Beachten Sie, dass sich die Journey derzeit im Entwurfsstatus befindet.
4. Wählen Sie **Validate**.

![Die fertige Journey zur Aktivierung.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5. Überprüfen Sie die Validierungsergebnisse und wählen Sie **Activate**.

![Empfehlungen im Abschnitt „Validation Rules“.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6. Wählen Sie in der Zusammenfassung **Activate Journey** erneut **Activate**.

![Zusammenfassung der Journey.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

Geschafft! Sie können nun Sendungen über BrazeAI Decisioning Studio™ Go triggern.

{% endtab %}
{% endtabs %}

## Nächste Schritte {#next-steps}

Nachdem Sie die Orchestrierung eingerichtet haben, fahren Sie mit der Gestaltung Ihres Agenten fort:

- [Agenten konzipieren]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)