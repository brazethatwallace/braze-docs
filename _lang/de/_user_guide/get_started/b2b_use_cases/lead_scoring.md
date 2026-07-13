---
nav_title: Lead Scoring
article_title: Einen Lead-Scoring-Workflow erstellen
page_order: 1
page_type: reference
description: "Erfahren Sie, wie Sie mit Braze einfaches Lead Scoring, externes Lead Scoring und Lead-Übergaben durchführen können."
---

# Einen Lead-Scoring-Workflow erstellen {#create-a-lead-scoring-workflow}

> Dieser Anwendungsfall zeigt, wie Sie mit Braze die Lead-Bewertungen von Nutzer:innen in Echtzeit aktualisieren und Leads automatisch an Ihre Vertriebsteams übergeben können.

Die Erstellung eines Lead-Scoring-Workflows in Braze umfasst zwei wesentliche Schritte:

1. Erstellen Sie ein Lead-Scoring-Canvas in Braze oder integrieren Sie ein externes Lead-Scoring-Tool:
- [Einfaches Lead Scoring](#simple-lead-scoring)
- [Externes Lead Scoring](#external-lead-scoring)

2. Erstellen Sie eine Webhook-Campaign, um qualifizierte Leads an Ihr Vertriebsteam zu senden:
- [Lead-Übergabe: Marketing Qualified Lead (MQL) an den Vertrieb](#lead-handoff)

## Einfaches Lead Scoring {#simple-lead-scoring}

### 1. Schritt: Ein Canvas erstellen {#step-1-create-a-canvas}

1. Gehen Sie zu **Messaging** > **Canvas** und wählen Sie **Canvas erstellen**. Füllen Sie dann die Canvas-Grundlagen aus.

2. Geben Sie Ihrem Canvas einen aussagekräftigen Namen, z. B. „Lead Scoring Canvas“, und versehen Sie es zur besseren Auffindbarkeit mit einem Tag wie „Lead Management“.<br><br>![1. Schritt der Erstellung eines Canvas mit dem Namen „Lead Scoring Canvas“ und dem Tag „Lead Management“.]({% image_buster /assets/img/b2b/step_1_simple.png %}){: style="max-width:80%;"}

### 2. Schritt: Entry-Kriterien festlegen {#step-2-set-up-your-entry-criteria}

1. Fahren Sie mit dem Schritt **Entry-Zeitplan** fort und wählen Sie einen **aktionsbasierten** Entry-Zeitplan. Dadurch werden Nutzer:innen in das Canvas aufgenommen, wenn sie bestimmte Aktionen ausführen.

2. Fügen Sie unter **Aktionsbasierte Optionen** diese beiden Aktionen hinzu:
    - **Wert des angepassten Attributs ändern** mit dem Namen Ihres Lead-Scoring-Attributs (z. B. `lead score`). Wenn Sie noch kein Lead-Scoring-Attribut erstellt haben, folgen Sie den Schritten unter [Angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes). Dadurch werden Nutzer:innen in das Canvas aufgenommen, sobald sich ihr Lead Score ändert.
    - **E-Mail-Adresse hinzufügen**

![2. Schritt der Erstellung eines Canvas mit dem Entry-Zeitplan „Aktionsbasiert“ und aktionsbasierten Optionen zum Ändern eines angepassten Attributs „lead score“ und zum Hinzufügen einer E-Mail-Adresse.]({% image_buster /assets/img/b2b/step_2_simple.png %}){: style="max-width:80%;"}

### 3. Schritt: Zielgruppe identifizieren {#step-3-identify-your-target-audience}

#### Schritt 3a: Segmente auswählen {#step-3a-select-segments}

Alle Nutzer:innen kommen für die Lead-Bewertung in Frage. Sie können also unternehmensspezifische Regeln hinzufügen, indem Sie auswählen, welche [Segmente]({{site.baseurl}}/user_guide/audience/segments) Sie ansprechen möchten, und zusätzliche [Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) anwenden. Sie können zum Beispiel Mitarbeitende, Nutzer:innen, die bereits Kund:innen sind, und ähnliche ausschließen.

![3. Schritt der Erstellung eines Canvas mit Optionen zur Auswahl von Segmenten und Filtern, um die Entry-Zielgruppe einzugrenzen.]({% image_buster /assets/img/b2b/step_3_simple.png %}){: style="max-width:80%;"}

#### Schritt 3b: Canvas-Wiederzulassung festlegen {#step-3b-set-canvas-re-eligibility}

Nutzer:innen werden dieses Canvas im Laufe ihres Lebenszyklus mit Ihnen viele Male durchlaufen. Stellen Sie also sicher, dass sie so schnell wieder einsteigen können, wie sie beim letzten Mal ausgestiegen sind. Dies lässt sich über die Einstellungen für die Wiederzulassung erreichen.

Gehen Sie unter **Entry Controls** wie folgt vor:
- Wählen Sie **Allow users to re-enter this Canvas**.
- Wählen Sie **Specified Window**.
- Setzen Sie die Wiederzulassung auf „0“ **Sekunden**.

![Abschnitt „Entry Controls“ mit Auswahlmöglichkeiten für „Allow users to re-enter this Canvas“ in einem „Specified Window“ von 0 Sekunden.]({% image_buster /assets/img/b2b/entry_controls_simple.png %}){: style="max-width:80%;"}

#### Schritt 3c: Sendeeinstellungen aktualisieren {#step-3c-update-send-settings}

Angesichts der operativen Natur dieses Canvas und der Tatsache, dass keine Nachrichten an diese Nutzer:innen gesendet werden, müssen Sie sich nicht an den Abo-Status halten.

Wählen Sie unter **Subscription Settings** bei **Send to these users:** die Option **all users including unsubscribed users**.

![4. Schritt der Erstellung eines Canvas zum Einstellen der Optionen für den Nachrichtenversand.]({% image_buster /assets/img/b2b/step_4_simple.png %}){: style="max-width:80%;"}

### 4. Schritt: Canvas erstellen {#step-4-build-your-canvas}

#### Schritt 4a: Einen Aktionspfad hinzufügen {#step-4a-add-an-action-path}

Wählen Sie unter Ihrer Variante <i class="fas fa-plus" aria-label="Hinzufügen"></i> **Hinzufügen** und dann **Aktionspfade**.

![Canvas mit „Aktionspfade“, die im über das Plus-Symbol geöffneten Menü angezeigt werden.]({% image_buster /assets/img/b2b/action_paths_simple.png %}){: style="max-width:60%;"}

#### Schritt 4b: Aktionsgruppen erstellen {#step-4b-create-action-groups}

Jede Aktionsgruppe repräsentiert alle Aktionen, die zur selben Punkte-Erhöhung oder -Verringerung führen. Sie können bis zu acht Aktionsgruppen einrichten. In diesem Szenario richten wir vier Gruppen ein.

Fügen Sie die folgenden Gruppen zu Ihrem Aktionspfad hinzu:

- **Gruppe 1:** Alle Ereignisse, die für eine Erhöhung um 1 Punkt zählen.
- **Gruppe 2:** Alle Ereignisse, die für eine Erhöhung um 5 Punkte zählen.
- **Gruppe 3:** Alle Ereignisse, die für eine Verringerung um 1 Punkt zählen.
- **Alle anderen:** Aktionspfade ermöglichen es Ihnen, ein Zeitfenster zu definieren, in dem abgewartet wird, ob Nutzer:innen eine Aktion ausführen, bevor sie in eine Gruppe „Alle anderen“ eingeordnet werden. Für das Lead Scoring ist dies eine Gelegenheit, die Punktzahl für „Inaktivität“ zu verringern.

![Aktionspfad mit Aktionsgruppen zum Hinzufügen von einem Punkt, fünf Punkten und zehn Punkten; zum Subtrahieren von einem Punkt und zehn Punkten; sowie „Alle anderen“.]({% image_buster /assets/img/b2b/action_paths_selected_simple.png %}){: style="max-width:20%;"}

#### Schritt 4c: Jede Gruppe mit den relevanten Ereignissen konfigurieren {#step-4c-configure-each-group-to-include-the-relevant-events}

Wählen Sie in jeder Aktionsgruppe **Trigger auswählen** und wählen Sie das Ereignis, das die Anzahl der Punkte für die jeweilige Aktionsgruppe hinzufügen wird. Fügen Sie weitere Trigger hinzu, um alle Ereignisse zu berücksichtigen, die den Lead Score um eins erhöhen. Nutzer:innen könnten beispielsweise ihren Punktestand um eins erhöhen, wenn sie eine Sitzung in einer beliebigen App starten oder ein angepasstes Event durchführen (z. B. die Registrierung oder Teilnahme an einem Webinar).

![Aktionsgruppe zum Hinzufügen eines Punktes mit den Triggern „Starting Session in Any App“ und „Performing Custom Event“.]({% image_buster /assets/img/b2b/action_groups_simple.png %}){: style="max-width:80%;"}

#### Schritt 4d: Schritte zur Nutzeraktualisierung hinzufügen {#step-4d-add-user-update-steps}

Fügen Sie jedem Canvas-Pfad, der unterhalb Ihres Aktionspfads erstellt wurde, einen Schritt zur Nutzeraktualisierung hinzu.

![Canvas, das den Aktionspfad mit verzweigten Nutzeraktualisierungspfaden für jede Aktionsgruppe anzeigt.]({% image_buster /assets/img/b2b/user_update_paths_simple.png %}){: style="max-width:80%;"}

{: start="2"}
Führen Sie auf dem Tab **Verfassen** jedes Nutzeraktualisierungsschritts die folgenden Aktionen für die jeweiligen Felder aus:

| Feld | Aktion |
| --- | --- |
| **Attributname** | Wählen Sie das Lead-Score-Attribut aus, das Sie in Schritt 2 ausgewählt haben (`lead score`). |
| **Aktion** | Ändern Sie die Aktion in **Increment By**, wenn der Pfad die Punktzahl erhöht, oder **Decrement By**, wenn der Pfad die Punktzahl verringert. |
| **Increment By** oder **Decrement By** | Geben Sie die Anzahl der Punkte ein, um die der Lead Score erhöht oder verringert werden soll. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 4d: Schritte zur Nutzeraktualisierung hinzufügen" }

### 5. Schritt: Canvas starten {#step-5-launch-your-canvas}

Das war's! Ihr Lead-Scoring-Canvas ist bereit für den Start.

## Externes Lead Scoring {#external-lead-scoring}

Ob Sie einen unserer [Technologie-Partner]({{site.baseurl}}/partners/home), Ihr eigenes internes Lead-Scoring-Modell, maschinelles Lernen oder ein anderes Lead-Scoring-Tool verwenden – wir haben mehrere Optionen für Sie.

### Externe Partner {#external-partners}

Unter [Technologie-Partner]({{site.baseurl}}/partners/home) erfahren Sie mehr über unsere B2B-Partner, die Lead-Scoring-Funktionen anbieten. Ihr Tool ist dort nicht aufgeführt? Sie können die Integration über unseren [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users)-API-Endpunkt durchführen.

### Interne Lead-Scoring-Datenmodelle {#internal-lead-scoring-data-models}

Sie können Braze auf verschiedene Weise mit Ihren internen Datenmodellen, einschließlich Lead-Scoring-Modellen, integrieren. Im Folgenden finden Sie einige gängige Beispiele dafür, wie unsere Kund:innen Braze integriert haben.

#### Integriertes Cloud Data Warehouse {#integrated-cloud-data-warehouse}

{% tabs %}
{% tab Braze als Datenquelle %}

Als Ihr Marketing-Tool enthält Braze äußerst relevante Daten, die das interne Lead-Score-Modell Ihres Teams ergänzen können.

So können beispielsweise Messaging-Engagement-Daten (wie E-Mail-Öffnungen und -Klicks, Landing-Page-Engagement und andere) den Engagement-Grad eines Leads bestimmen. Mit den Streaming-Export-Lösungen von Braze können Sie diese Daten an Ihr Cloud Data Warehouse zurückgeben und als Input für Ihre Lead-Scoring-Modelle verfügbar machen:

- [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)
- [Snowflake Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)

{% endtab %}
{% tab Braze als Ziel %}

Nachdem Ihre internen Teams Ihr Lead-Scoring-Modell erstellt und ausgeführt haben, können Sie diese Daten wieder in Braze einspeisen, um Leads besser zu segmentieren und mit relevanten Nachrichten anzusprechen. Dies können Sie mit der [Braze Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) tun.

Mit der Cloud-Datenaufnahme erstellen Ihre internen Teams eine neue Tabelle oder Ansicht mit Ihren Nutzer-Bezeichnern, den neuesten Lead-Bewertungen und den Zeitstempeln, wann die Bewertungen aktualisiert wurden. Braze übernimmt die Tabelle oder Ansicht und fügt die Lead Scores den Nutzerprofilen hinzu.

{% endtab %}
{% endtabs %}

## Lead-Übergabe: Marketing Qualified Lead (MQL) an den Vertrieb {#lead-handoff}

Unser empfohlener Ansatz für Lead-Übergaben besteht darin, allen Nutzer:innen in Braze einen entsprechenden Lead oder Kontakt zuzuordnen. Diese Leads würden in die Warteschlange Ihres Vertriebsteams gelangen, wenn ihr Lead-Status in ein MQL-Stadium wechselt. Zu diesem Zeitpunkt würde Salesforce einen Lead-Routing- oder Zuweisungsworkflow starten.

Um den Lead-Datensatz in Salesforce mit dem Lead-Status aus Braze zu aktualisieren, empfehlen wir die Verwendung eines getriggerten Webhook-Templates.

### 1. Schritt: Eine Webhook-Campaign erstellen {#step-1-create-a-webhook-campaign}

### 2. Schritt: Webhook konfigurieren {#step-2-configure-your-webhook}

#### Schritt 2a: Webhook verfassen {#step-2a-compose-webhook}

1. Geben Sie Ihrer Webhook-Campaign einen Namen, z. B. „Salesforce > Lead auf MQL aktualisieren“.

2. Geben Sie Ihre Webhook-URL im Format {% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} ein. Die Braze-Nutzer-ID {% raw %}`{{${user_id}}}`{% endraw %} sollte mit Ihrer Salesforce-Kontakt-ID übereinstimmen. Falls nicht, verwenden Sie einen Alias anstelle von {% raw %}`{{${user_id}}}`{% endraw %}.

3. Aktualisieren Sie die **HTTP Method** auf **PATCH**.

4. Konfigurieren Sie Ihren Payload so, dass der Lead-Datensatz in Salesforce nur dann aktualisiert wird, wenn der Lead Score dieses Leads Ihren vordefinierten Schwellenwert überschreitet. Im folgenden Beispiel-Anfragetext wird ein Lead Score von mehr als 100 verwendet.

{% raw %}
```liquid
{% assign threshold = 100%}
{% if custom_attribute.${lead score} > threshold %}
{
"lead_status": "MQL"
}
{% else %}{% abort_message('not at threshold')%}
{% endif %}
```
{% endraw %}

{: start="5"}
5. Fügen Sie die folgenden Header ein:

| Header | Inhalt |
| --- | --- |
| Authorization | {% raw %}`Bearer {{result.access_token}}`{% endraw %}<br><br>Um ein Token abzurufen, [konfigurieren Sie eine Connected App](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5) für den OAuth 2.0 Client-Credentials-Flow und verwenden Sie dann Connected-Content, um den Bearer von Salesforce abzurufen: <br><br>{% raw %}<code>{% connected_content https://[instance].my.salesforce.com/services/oauth2/token <br>:method post <br> :body client_id=[client_id]&client_secret=[client_secret]&grant_type=client_credentials <br>:save result %}{% endraw %} <br> Bearer {% raw %}{{result.access_token}}</code>{% endraw %} |
| Content-Type | application/json |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2a: Webhook verfassen" }

![Webhook, der mit einer Salesforce-Webhook-URL, der HTTP-Methode PATCH, einem Rohtext-Anfragetext und Anfrage-Headern verfasst wird.]({% image_buster /assets/img/b2b/webhook.png %}){: style="max-width:80%;"}

#### Schritt 2b: Webhook-Versand planen {#step-2b-schedule-webhook-sends}

Die Campaign sollte immer dann getriggert werden, wenn sich der Lead Score von Nutzer:innen ändert. Diese Campaign wird für alle Nutzer:innen ausgelöst, deren Punktestand sich ändert, betrifft aber nur diejenigen, die derzeit kein MQL sind und den von Ihnen im vorherigen Schritt festgelegten Schwellenwert überschritten haben.

Wählen Sie im Schritt **Schedule Delivery** Folgendes aus:
- Einen **aktionsbasierten** Zustellungstyp
- Eine Trigger-Aktion von **Change Custom Attribute Value** mit dem Namen Ihres Lead-Scoring-Attributs und einer Aktion mit einem **beliebigen neuen Wert**

#### Schritt 2c: Zielgruppe identifizieren {#step-2c-identify-target-audience}

Fügen Sie im Schritt **Target Audiences** einen Filter ein, der Nutzer:innen ausschließt, deren Lead-Status bereits auf MQL oder darüber hinaus steht, z. B. „`lead_status` `is none of` `MQL`“.

![Webhook-Targeting-Optionen mit dem Filter „lead_status“ ist keiner von „MQL“.]({% image_buster /assets/img/b2b/step_3_webhook.png %}){: style="max-width:80%;"}

### 3. Schritt: Campaign starten {#step-3-launch-campaign}

Wählen Sie **Starten** und beobachten Sie, wie sich Ihr Lead-Status in Salesforce ändert, wenn Ihre Kund:innen den MQL-Lead-Score-Schwellenwert überschreiten.