---
nav_title: Salesforce Sales Cloud
article_title: Leads mit Salesforce Sales Cloud verwalten
page_order: 3
page_type: reference
description: "Erfahren Sie, wie Sie mit Braze-Webhooks über den Salesforce-Endpunkt sobjects/Lead Leads in Salesforce Sales Cloud erstellen und aktualisieren können."
---

# Leads mit Salesforce Sales Cloud verwalten {#manage-leads-with-salesforce-sales-cloud}

> [Salesforce](https://www.salesforce.com/) ist eine der weltweit führenden cloudbasierten geschäftskunden-Relationship-Management-Plattformen (CRM), die Unternehmen bei der Verwaltung ihres gesamten Vertriebsprozesses unterstützt – einschließlich Lead-Generierung, Opportunity-Tracking und Konto-Management.<br><br>Auf dieser Seite erfahren Sie, wie Sie mit Braze-Webhooks über eine von der Community eingereichte Integration Leads in Salesforce Sales Cloud erstellen und aktualisieren können.

{% alert important %}
Dies ist eine von der Community eingereichte Integration, die nicht direkt von Braze unterstützt wird. Nur offizielle, von Braze bereitgestellte Webhook-Templates werden von Braze unterstützt.
{% endalert %}

## Funktionsweise {#how-it-works}

Die Integration von Braze und Salesforce Sales Cloud verwendet Braze-Webhooks zum Erstellen und Aktualisieren von Leads in Salesforce Sales Cloud über den Salesforce-Endpunkt [sobjects/Lead](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.html).

Braze bietet derzeit zwei Integrationen für Salesforce Sales Cloud für die folgenden Anwendungsfälle an:
1. [Erstellen eines Leads in Salesforce Sales Cloud](#creating-lead)
2. [Aktualisieren eines Leads in Salesforce Sales Cloud](#updating-lead)

{% alert note %}
Diese Integration dient ausschließlich dazu, Salesforce von Braze aus zu aktualisieren – als Teil Ihrer Bemühungen zur Lead-Akquisition und -Pflege. Um Daten von Salesforce zurück nach Braze zu synchronisieren, sehen Sie sich das [B2B-Datenmodell]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models) an oder wenden Sie sich an einen unserer [Technologie-Partner]({{site.baseurl}}/partners/home).
{% endalert %}

## Voraussetzungen {#prerequisites}

Bevor Sie mit dieser Integration fortfahren können, muss der Salesforce-Support Ihnen die Möglichkeit geben, verbundene Apps zu erstellen. Sie können dies anfordern, indem Sie eine [Salesforce-Supportanfrage](https://help.salesforce.com/s/articleView?id=005167035&type=1) einreichen.

Nachdem der Salesforce-Support Ihnen die Möglichkeit gewährt hat, eine verbundene App in Salesforce Sales Cloud zu erstellen, befolgen Sie die Schritte in der Salesforce-Dokumentation: [Configure a Connected App for the OAuth 2.0 Client Credentials Flow](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5).

Wenn Sie die erforderlichen OAuth-Einstellungen für die verbundene App konfigurieren, behalten Sie alle OAuth-Einstellungen mit ihren Standardwerten und -auswahlen bei, mit Ausnahme der folgenden:
1. Wählen Sie **Enable for device flow** aus. Sie können die **Callback URL** leer lassen, da sie standardmäßig auf einen Platzhalter gesetzt wird.
2. Fügen Sie für die ausgewählten **OAuth Scopes** den Eintrag **Manage user data via APIs (api)** hinzu.
3. Wählen Sie **Enable Client Credentials Flow** aus.

## Erstellen eines Leads in Salesforce Sales Cloud {#creating-lead}

Als geschäftskunden-Engagement-Plattform kann Braze neue Leads auf Basis von Nutzer:innen-Flows generieren, z. B. beim Ausfüllen eines Formulars auf einer Landing-Page. In diesem Fall können Sie einen Braze Salesforce Sales Cloud Webhook verwenden, um einen entsprechenden Lead in Salesforce zu erstellen.

### Schritt 1: `client_id` und `client_secret` erfassen {#step-1-collect-your-client_id-and-client_secret}

1. Gehen Sie in Salesforce zu **Platform Tools** > **Apps** > **App Manager**.
2. Suchen Sie Ihre neu erstellte Braze-App und wählen Sie **View**.
3. Wählen Sie unter **Consumer Key and Secret** die Option **Manage Consumer Details**.
4. Notieren Sie sich auf der angezeigten Seite Ihren **Consumer Key** und Ihr **Consumer Secret**. Der **Consumer Key** ist Ihre `client_id` und das **Consumer Secret** ist Ihr `client_secret`.

### Schritt 2: Webhook-Template einrichten {#step-2-set-up-your-webhook-template}

Verwenden Sie Templates, um diesen Webhook schnell auf der gesamten Braze-Plattform wiederzuverwenden.

1. Gehen Sie in Braze zu **Templates**, wählen Sie **Webhook Templates** und dann **+ Create Webhook Template**.
2. Geben Sie einen Namen für das Template an, z. B. „Salesforce Sales Cloud > Lead erstellen“.
3. Geben Sie auf dem Tab **Verfassen** die folgenden Details ein:

#### Webhook verfassen {#compose-webhook}

| Feld | Details |
| --- | --- |
| Webhook-URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/`{% endraw %} |
| HTTP-Methode | `POST` |
| Anfragetext | JSON-Schlüssel/Wert-Paare |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook verfassen" }

#### Schlüssel/Wert-Paare für Body-Eigenschaften {#body-property-key-values}

Wählen Sie **+ Add New Body Property** für jedes Schlüssel/Wert-Paar, das Sie von Braze nach Salesforce übertragen möchten. Sie können beliebige Felder zuordnen – die folgende Tabelle ist nur ein Beispiel.

| Schlüssel | Wert |
| --- | --- |
| firstName | {% raw %}`{{${first_name}}}`{% endraw %} |
| lastName | {% raw %}`{{${last_name}}}`{% endraw %} |
| email | {% raw %}`{{${email_address}}}`{% endraw %} |
| company | {% raw %}`{{custom_attribute.${company}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schlüssel/Wert-Paare für Body-Eigenschaften" }

#### Anfrage-Header {#request-headers}

Wählen Sie **+ Add New Header** für jeden der folgenden Anfrage-Header.

| Schlüssel | Wert |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anfrage-Header" }

{: start="4" }
4. Wählen Sie **Save Template**.

![Ein ausgefülltes Webhook-Template zum Erstellen eines Leads.]({% image_buster /assets/img/b2b/create_lead_webhook.png %}){: style="max-width:70%;"}

## Aktualisieren eines Leads in Salesforce Sales Cloud {#updating-lead}

Um einen Braze Salesforce Sales Cloud Webhook einzurichten, der Leads in Salesforce aktualisiert, benötigen Sie einen gemeinsamen Bezeichner zwischen Salesforce Sales Cloud und Braze. Im folgenden Beispiel wird die Salesforce `lead_id` als Braze `external_id` verwendet, aber Sie können dies auch mit einem `user_alias` erreichen. Weitere Informationen finden Sie unter [B2B-Daten]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models).

Dieses Beispiel zeigt konkret, wie Sie die Lead-Stufe eines Leads auf „MQL“ (Marketing Qualified Lead) aktualisieren, nachdem ein Lead einen bestimmten Schwellenwert überschritten hat. Dies ist ein zentraler Bestandteil unseres Anwendungsfalls [B2B-Lead-Scoring-Workflow]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring).

### Schritt 1: `client_id` und `client_secret` erfassen

1. Gehen Sie in Salesforce zu **Platform Tools** > **Apps** > **App Manager**.
2. Suchen Sie Ihre neu erstellte Braze-App und wählen Sie **View**.
3. Wählen Sie unter **Consumer Key and Secret** die Option **Manage Consumer Details**.
4. Notieren Sie sich auf der angezeigten Seite Ihren **Consumer Key** und Ihr **Consumer Secret**.
    - Der **Consumer Key** ist Ihre `client_id` und das **Consumer Secret** ist Ihr `client_secret`.

### Schritt 2: Webhook-Template einrichten

1. Gehen Sie in Braze zu **Templates**, wählen Sie **Webhook Templates** und dann **+ Create Webhook Template**.
2. Geben Sie einen Namen für das Template an, z. B. „Salesforce Sales Cloud > Lead auf MQL aktualisieren“.
3. Geben Sie auf dem Tab **Verfassen** die folgenden Details ein:

#### Webhook verfassen

| Feld | Details |
| --- | --- |
| Webhook-URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} |
| HTTP-Methode | `PATCH` |
| Anfragetext | JSON-Schlüssel/Wert-Paare |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook verfassen" }

#### Schlüssel/Wert-Paare für Body-Eigenschaften

Wählen Sie **+ Add New Body Property** für das folgende Schlüssel/Wert-Paar. Beachten Sie, dass `Lead_Stage__c` ein Beispielname ist. Das angepasste Feld, das Sie für das Tracking von MQLs in Salesforce verwenden, kann einen anderen Namen haben – stellen Sie sicher, dass die Namen übereinstimmen.

| Schlüssel | Wert |
| --- | --- |
| `Lead_Stage__c` | `MQL` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schlüssel/Wert-Paare für Body-Eigenschaften" }

#### Anfrage-Header

Wählen Sie **+ Add New Header** für jeden der folgenden Anfrage-Header.

| Schlüssel | Wert |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anfrage-Header" }

{: start="4"}
4. Wählen Sie **Save Template**.

![Ein ausgefülltes Webhook-Template zum Aktualisieren eines Leads.]({% image_buster /assets/img/b2b/update_lead_webhook.png %}){: style="max-width:70%;"}

## Verwendung dieser Webhooks in einem operativen Workflow {#using-these-webhooks-in-an-operational-workflow}

Sie können Ihre Templates schnell zu Ihren operativen Workflows in Braze hinzufügen, z. B.:

1. Als Teil einer [Campaign für neue Leads](#new-lead), die einen Lead in Salesforce erstellt
2. Als Teil eines [Lead-Scoring-Canvas](#lead-scoring), der Nutzer:innen, die Ihren MQL-Schwellenwert überschritten haben, auf „MQL“ aktualisiert und Salesforce Sales Cloud mit denselben Informationen aktualisiert

### Campaign für neue Leads {#new-lead}

Um einen Lead in Salesforce zu erstellen, wenn Nutzer:innen ihre E-Mail-Adresse angeben, können Sie eine Campaign erstellen, die das Webhook-Template „Update Lead“ verwendet und getriggert wird, wenn Nutzer:innen ihre E-Mail-Adresse hinzufügen (z. B. ein Webformular ausfüllen).

![Schritt 2 der Erstellung einer aktionsbasierten Campaign mit der Aktion „Eine E-Mail-Adresse hinzufügen“ als Trigger.]({% image_buster /assets/img/b2b/salesforce_create_campaign.png %}){: style="max-width:70%;"}

### Lead-Scoring-Canvas für das Überschreiten des Marketing-Qualified-Lead-(MQL)-Schwellenwerts {#lead-scoring}

Dieser Webhook wird im Anwendungsfall [Lead-Scoring]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring#lead-handoff) behandelt, aber Sie können auch direkt innerhalb des Lead-Scoring-Canvas nach MQLs suchen und Salesforce aktualisieren (anstatt eine separate Webhook-Campaign zu erstellen):

Fügen Sie Ihrer Nutzeraktualisierung einen weiteren Schritt hinzu, um zu prüfen, ob Nutzer:innen den von Ihnen definierten MQL-Schwellenwert überschritten haben. Wenn ja, aktualisieren Sie den Status auf „MQL“ und aktualisieren dann Salesforce mit demselben „MQL“-Status über dieses Webhook-Template. Salesforce kümmert sich um den Rest, indem es diesen Lead anhand Ihrer definierten Lead-Routing-Regeln an die entsprechenden Vertriebsteams weiterleitet.

#### Canvas-Schritt hinzufügen, um Nutzer:innen zu prüfen, die den MQL-Schwellenwert überschritten haben {#adding-canvas-step-to-check-for-users-who-passed-the-mql-threshold}

1. Fügen Sie einen **Zielgruppenpfad**-Schritt mit zwei Gruppen hinzu: „MQL-Schwellenwert“ und „Alle anderen“.
2. Suchen Sie in der Gruppe „MQL-Schwellenwert“ nach Nutzer:innen, die derzeit nicht den Status „MQL“ haben (z. B. `lead_stage` gleich „Lead“), aber einen Lead-Score haben, der über dem von Ihnen definierten Schwellenwert liegt (z. B. `lead_score` größer als 50). Wenn ja, gehen sie zum nächsten Schritt über; wenn nicht, verlassen sie den Flow.

![Die Zielgruppenpfad-Gruppe „MQL Threshold“ mit Filtern für `lead_stage` gleich „Lead“ und `lead_score` mehr als „50“.]({% image_buster /assets/img/b2b/salesforce_check_mql.png %}){: style="max-width:70%;"}

{: start="3" }
3. Fügen Sie einen **Nutzeraktualisierung**-Schritt hinzu, der den Wert des Attributs `lead_stage` auf „MQL“ aktualisiert.

![Der Nutzeraktualisierung-Schritt „Update to MQL“, der das Attribut `lead_stage` auf den Wert „MQL“ aktualisiert.]({% image_buster /assets/img/b2b/salesforce_update_mql.png %}){: style="max-width:70%;"}

{: start="4" }
4. Fügen Sie einen Webhook-Schritt hinzu, der Salesforce mit der neuen MQL-Stufe aktualisiert.

![Der Webhook-Schritt „Update Salesforce“ mit ausgefüllten Details.]({% image_buster /assets/img/b2b/salesforce_webhook.png %}){: style="max-width:70%;"}

Jetzt aktualisiert Ihr Canvas-Flow Nutzer:innen, die Ihren MQL-Schwellenwert überschritten haben!

![Ein Canvas-Nutzeraktualisierung-Schritt, der prüft, ob Nutzer:innen den MQL-Schwellenwert überschreiten, und bei Überschreitung Salesforce aktualisiert.]({% image_buster /assets/img/b2b/salesforce_canvas.png %}){: style="max-width:50%;"}

## Fehlerbehebung {#troubleshooting}

Diese Workflows bieten nur begrenzte Debugging-Möglichkeiten innerhalb von Salesforce. Wir empfehlen daher, das Braze [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) zu Rate zu ziehen, um herauszufinden, warum ein Webhook fehlgeschlagen ist und ob Fehler aufgetreten sind.

Ein Fehler, der durch eine ungültige URL für den Abruf des OAuth-Tokens verursacht wird, wird beispielsweise als `https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL` angezeigt.

![Ein Fehler-Antworttext, der besagt, dass die URL keine gültige URL ist.]({% image_buster /assets/img/b2b/error_message_invalid_url.png %})