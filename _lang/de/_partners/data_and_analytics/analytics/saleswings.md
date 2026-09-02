---
nav_title: SalesWings
article_title: SalesWings
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und SalesWings. SalesWings ist eine Lösung für Vertriebs- und Marketingoperationen für Braze, die Sie bei der Qualifizierung von Leads und Konten unterstützt und Insights und Warnmeldungen für den Vertrieb innerhalb von CRM-Systemen wie Salesforce sowie B2B-Attribution-Berichte liefert. Sie können die Interessen und das Engagement innerhalb von Braze für die Personalisierung in Canvas und die Segmentierung nutzen. Ähnlich wie Digioh bietet auch SalesWings eine Möglichkeit, Leads über eine Website zu generieren."
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) ist eine B2B-SaaS-Lösung für Vertriebs- und Marketingoperationen, die die Lead- und Account-Qualifizierung durch ganzheitliche Lead-Bewertung und -Einstufung unterstützt und Insights und Warnmeldungen für den Vertrieb sowie B2B-Attribution-Berichte liefert, zusammen mit einer engen Salesforce-CRM-Integration. Ein Add-on für das Website-Engagement, ähnlich wie Digioh, ermöglicht es Ihnen, auf der Website Leads zu generieren. Sie können die Interessen und das Engagement innerhalb von Braze für die Personalisierung in Canvas und die Segmentierung nutzen.

_Diese Integration wird von SalesWings gepflegt._

## Über die Integration {#about-the-integration}

SalesWings erlaubt es Marketingteams und Marketing-Operations-Manager:in:innen, Leads und Accounts für ihre Vertriebsteams zu qualifizieren, was für die Ausrichtung von Vertrieb und Marketing und die operative Effizienz unerlässlich ist. Darüber hinaus kann SalesWings zusammen mit Braze den Vertriebsmitarbeitern die vollständige Customer Journey eines Leads und eines Kontos sowie Daten über das Engagement der Braze-Campaigns anzeigen, was es Ihnen erlaubt, die Qualifikationsraten von Leads durch fundiertere Gespräche zu erhöhen. SalesWings identifiziert Bedürfnisse und Interessen zusammen mit anderen Signalen und erlaubt so die automatisierte Übergabe qualifizierter Käufer:innen an Vertriebsteams innerhalb Ihres CRM. Sie können die ermittelten Bedürfnisse, Interessen und die Verkaufsbereitschaft als Braze-Nutzerattribute zur Personalisierung und Segmentierung verwenden.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| SalesWings-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [SalesWings-Konto](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs). |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit `users.export.ids`-Berechtigungen (und `users.track`, wenn Sie das SalesWings-Insights-Push-Feature verwenden). <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-REST-Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Segment.com-Konto (optional) | Wenn Sie Segment.com nutzen, können Sie alle Daten zum Lead-Engagement und -Profil sowie Identifizierungs-Events über Segment.com für das Lead-Profiling senden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

{% tabs %}
{% tab Lead and Account Scoring %}

SalesWings bietet Braze-Kund:innen [eine flexible Möglichkeit, Leads, Kontakte und Konten mit hochmodernen Lead-Scoring-](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs) und Lead-Grading-Funktionen zu qualifizieren. Alle Ihre Daten zur Lead-Qualifizierung werden nativ an Salesforce CRM und andere Systeme gepusht, in denen Sie Leads, Kontakte, Accounts und Opportunities verwalten und darüber berichten möchten.

![Beispiel für ein einfaches Click-not-Code-Lead-Scoring-Modell in SalesWings]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_Beispiel für ein einfaches Klick, der-not-Code-Lead-Scoring-Modell in SalesWings_
{% endtab %}
{% tab Sales and Marketing Alignment %}
SalesWings erlaubt Marketingteams das Tracking, die Qualifizierung und die Übergabe marketingqualifizierter Leads an Ihre Vertriebsteams. Alle SalesWings-Daten werden nativ an Salesforce gepusht und können genutzt werden, um bestehende Prozesse zu optimieren oder neue Prozesse über Listen, Berichte, Abläufe und mehr zu erstellen.

![Beispiel dafür, wie das SalesWings-Lead-Scoring eine Liste von Leads oder Kontakten nativ in Salesforce priorisiert]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_Beispiel dafür, wie das SalesWings-Lead-Scoring eine Liste von Leads oder Kontakten nativ in Salesforce priorisiert_

![Beispiel dafür, wie das SalesWings-Lead-Scoring eine Liste von Accounts nativ in Salesforce priorisiert]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_Beispiel dafür, wie das SalesWings-Lead-Scoring eine Liste von Accounts nativ in Salesforce priorisiert_
{% endtab %}
{% tab Lead and Account Grading %}
SalesWings erlaubt es Braze-Kund:innen, Leads und Konten auf der Grundlage von Profildaten (typischerweise CRM-Daten) zu qualifizieren. Dies wird auch als „Lead Grading“, „Fit Scoring“ oder „Firmographic Scoring“ bezeichnet. Braze-Kund:innen können Attributdaten direkt an SalesWings senden, und SalesWings kann alle Daten und Datensätze von Salesforce-CRM-Standard- oder angepassten Objekten für eine ganzheitliche Profilbewertung lesen.
{% endtab %}
{% tab Sales Insights for Sales Reps %}
Mit SalesWings können Sie Ihren Vertriebsmitarbeitern Insights über ihre Leads, Kontakte und Konten zeigen (Alternative zu Marketo Sales Insights). Im Wesentlichen können Sie alle Daten aus Braze und dem Web-Engagement für Ihr Vertriebsteam sichtbar machen. Die Insights sind nativ in Salesforce CRM eingebettet und können per Push an andere CRMs oder Systeme oder über eine Braze-E-Mail als „Verkaufsalarm“ übermittelt werden.

![Beispiel einer Insights-Ansicht für Vertriebsmitarbeiter in Salesforce (auch für andere CRM-Systeme verfügbar)]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Beispiel einer Insights-Ansicht für Vertriebsmitarbeiter in Salesforce (auch für andere CRM-Systeme verfügbar)_
{% endtab %}
{% tab Sales Alerts %}
SalesWings bietet native E-Mail- und Slack-Benachrichtigungen, und Sie können Berichtsabonnements in Salesforce einrichten, auf die Ihr Vertriebsteam zugreifen kann, um tägliche, wöchentliche und monatliche E-Mail-Berichte zu erhalten. Darüber hinaus können Sie über eine Zapier-Integration zusätzliche Workflows auf der Grundlage von SalesWings-Daten zur Lead-Qualifizierung erstellen.

![Beispiel einer Verkaufsmeldung über einen Slack-Kanal]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Beispiel einer Verkaufsmeldung über einen Slack-Kanal_
{% endtab %}
{% tab Reporting in Salesforce CRM %}
Durch die native SalesWings-Integration mit Salesforce können Sie automatisierte Berichte mit Leads, Kontakten, Konten und Opportunities auf der Grundlage von Web-Engagement-Daten und jeglichem Braze-Campaign-Engagement mit einer nativen Braze-Currents-Integration erstellen. So können Sie z. B. eine Liste von Hot Leads an ein Vertriebsteam weiterleiten, in der alle Personen aufgeführt sind, die auf eine bestimmte E-Mail-Campaign geklickt oder eine bestimmte Aktion in Ihrer App oder auf Ihrer Website ausgeführt haben.

![Beispiel-Dashboard, das mit dem Braze-E-Mail- und Marketing-Engagement in Salesforce verknüpft ist und die Auswirkungen der Braze-Campaigns auf die Vertriebsergebnisse und -erfolge untersucht]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Beispiel-Dashboard, das mit dem Braze-E-Mail- und Marketing-Engagement in Salesforce verknüpft ist und die Auswirkungen der Braze-Campaigns auf die Vertriebsergebnisse und -erfolge untersucht_
{% endtab %}
{% endtabs %}

## Integration

### Schritt 1: SalesWings-Konto und Konfiguration {#step-1-saleswings-account-and-configuration}

[Vereinbaren Sie eine Demo](https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs) mit dem freundlichen SalesWings-Team, um mehr über SalesWings zu erfahren.

### Schritt 2: Behavioral Tracking auf Ihrer Website oder App installieren {#step-2-installing-behavioral-tracking-on-your-website-or-app}

Es gibt mehrere Möglichkeiten, in SalesWings Verhaltensdaten für das Lead- und Account-Scoring, die Identifizierung der Käuferabsicht und für Insights zu sammeln:
* [Setzen Sie das SalesWings-Tracking-JavaScript ein](https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script) auf den Websites und Apps, auf denen Sie Leads verfolgen und identifizieren möchten
* Nehmen Sie Braze-Events zusammen mit Event-Eigenschaften über Braze-Currents in SalesWings auf
* Senden Sie verhaltensbezogene Lead-Aktivitätsdaten (und Lead-Profildaten) über die [SalesWings-Integration mit Segment](https://support.saleswingsapp.com/en/articles/9258905-segment-com-integration)
* Senden Sie Daten direkt von einer Drittanbieter-Lösung an die SalesWings-[API](https://support.saleswingsapp.com/en/articles/6930889-using-saleswings-open-api-to-send-events-to-saleswings)

### Schritt 3: SalesWings mit Braze verbinden {#step-3-connecting-saleswings-to-braze}

Gehen Sie auf die [Seite **SalesWings Integrations**](https://helium.saleswings.pro/integrations) und erweitern Sie den Abschnitt **Braze Integration**.

![Der Abschnitt „Braze Integration“ auf der Seite „SalesWings Settings“.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %})

Kopieren Sie den Wert der Spalte **Identifier** für den neu erstellten Schlüssel und fügen Sie ihn in das Feld **Braze API key** im Abschnitt SalesWings **Braze Integration** ein.

Fügen Sie Ihren Braze-API-Endpunkt hinzu, wie im Artikel [API- und SDK-Endpunkte]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) beschrieben, und geben Sie ihn in das Feld **Braze API endpoint** ein. Kopieren Sie den Wert der Spalte **REST Endpoint** und geben Sie ihn in das Feld **Braze API endpoint** im Abschnitt SalesWings **Braze Integration** ein.

Wählen Sie dann **Save**.

### Schritt 4: SalesWings-Insights-Push zu Braze aktivieren (optional) {#step-4-enable-saleswings-insights-push-to-braze-optional}

Wenn Sie die SalesWings-Insights in Ihren Braze-Nutzerprofilen für die Segmentierung, Personalisierung oder die Orchestrierung der Canvas Journey verfügbar machen möchten, besuchen Sie die [Seite **SalesWings Integrations**](https://helium.saleswings.pro/integrations) und erweitern Sie den Abschnitt **Braze Integration**.

Klicken Sie auf **Start data push** unter **SalesWings-to-Braze insights data push**.

### Schritt 5: Einen angepassten Currents-Export zu SalesWings einrichten (optional) {#step-5-set-up-a-custom-currents-export-to-saleswings-optional}

Wenn Sie [Nutzerverhalten-]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) und [Nachrichten-Engagement-]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)Events für Behavioral Intelligence, Lead- und Account-Scoring, Insights oder Berichte in Ihrem CRM nutzen möchten, gehen Sie auf die [Seite **SalesWings Integrations**](https://helium.saleswings.pro/integrations) und erweitern Sie den Abschnitt **Braze Integration**.

Wählen Sie **Generate** unter **Generate an API Token / Textbaustein to setup a Custom Currents Export**.

[Erstellen Sie dann einen neuen Current]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents) und wählen Sie als Current-Typ **Custom Currents Export** aus.

Geben Sie im Abschnitt **Credentials** des Formulars zur Erstellung von Currents das API-Token / Textbaustein ein, das Sie auf der [Seite **SalesWings Integrations**](https://helium.saleswings.pro/integrations) für **Bearer Token / Textbaustein** generiert haben, und `https://helium.saleswings.pro/api/braze/currents/events` für **Endpoint**.

### Schritt 6: SalesWings-Lead- und Account-Scoring für Braze, CRM-Integration und mehr konfigurieren {#step-6-configuring-saleswings-lead-and-account-scoring-for-braze-crm-integration-and-more}

Wenden Sie sich an das SalesWings-Serviceteam, das Sie beim Onboarding über die [Website](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) unterstützt.

## Verwendung dieser Integration {#using-this-integration}

Um Verhaltensdaten und andere Daten mit Leads und Accounts zu verknüpfen, muss SalesWings Nutzer:innen auf Ihrer Website oder App oder durch eine Drittanbieter-Integration identifizieren. Dies kann auf die folgenden Arten geschehen:

- **Formulareinreichungen:** Wenn Nutzer:innen ein Webformular absenden, identifiziert SalesWings automatisch alle Ihre Webformulartypen (wie Anmeldung, Download, Kontakt usw.) und löst die Identität auf, wenn ein Formular abgeschickt wird.
- **URL-Klicks mit einer Braze-ID oder externen ID:** Nutzer:innen klicken auf eine Braze-Marketingaktion, typischerweise E-Mail-Klicks, Banner-Klicks oder ähnliches, was zu einer Seite führt, die Sie mit SalesWings tracken.
- **Braze-Currents-Events (optional):** Wenn der angepasste Currents-Export zu SalesWings konfiguriert ist, erstellt SalesWings für alle Braze-Nutzer:innen mit einer E-Mail ein identifiziertes Profil, deren Events an den Current gesendet werden.
- **E-Mail-Tracking über Gmail- und Outlook-Plugins (optional):** Wenn Sie Ihre Vertriebsmitarbeiter mit E-Mail-Tracking-Plugins ausstatten, können diese das vollständige Website-Tracking der Nutzer:innen triggern, indem sie trackbare Links versenden.
- **Segment.com-Identify-Event (optional):** Als Segment.com-Nutzer:in können Sie die Identität auch über die Segment.com-Integration auflösen.

### Identifizierung von Nutzer:innen anhand von URL-Klicks {#identifying-users-from-url-clicks}

Sie können Nutzer:innen automatisch identifizieren, wenn sie auf eine trackbare URL klicken (z. B. E-Mail-Blasts, Banner mit URLs). Um eine URL verfolgbar zu machen, gibt es zwei Möglichkeiten, Ihre Website-URLs in Ihren E-Mails, Bannern oder SMS zu ändern, indem Sie den Parameter und die ID am Ende Ihrer Links hinzufügen.

1. Anhängen von `?braze_id=` gefolgt von {% raw %}`{{${braze_id}}}`{% endraw %}
  - **Beispiel-Link:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. Anhängen von `?br_user_id=` gefolgt von {% raw %}`{{${user_id}}}`{% endraw %}
  - **Beispiel-Link:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

Die Variable `braze_id` wird auf einen von Braze erzeugten Bezeichner der Nutzer:innen gesetzt und ist immer verfügbar. Die Variable `br_user_id` wird auf den Bezeichner der Nutzer:innen in Ihrem System gesetzt und kann in bestimmten Szenarien fehlen (z. B. bei anonymen Nutzer:innen, die mit dem Braze SDK erstellt wurden). Wenn sowohl `braze_id` als auch `br_user_id` in einem Link verwendet werden, berücksichtigt SalesWings nur den Parameter `braze_id`.

### SalesWings-Insights nach Braze pushen {#pushing-saleswings-insights-to-braze}

Wenn Sie den SalesWings-Insights-Push für Braze aktivieren, aktualisiert SalesWings Ihre Braze-Nutzerprofile mit den folgenden [angepassten Attributen]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types):

| Angepasstes Attribut | Typ | Beschreibung |
| ----------- | ----------- | ----------- |
| `sw_favorite` | Boolescher Wert | Ob der Lead in SalesWings oder Salesforce CRM als Favorit markiert wurde |
| `sw_last_active_at` | Datum | Der Zeitpunkt der letzten Aktivität des Leads auf Ihrer Website |
| `sw_lead_link_open` | String | Der Link zum Zugriff auf ein Lead-Profil in SalesWings (ohne ein SalesWings-Dashboard-Konto) |
| `sw_lead_link_protected` | String | Der Link zum Zugriff auf ein Lead-Profil in SalesWings (mit einem SalesWings-Dashboard-Konto) |
| `sw_lead_owner` | String | Der Eigentümer, der für den Lead in SalesWings oder Salesforce CRM festgelegt wurde |
| `sw_lead_score` | Gleitkommazahl | Der Wert des wichtigsten SalesWings-Lead-Scores, der in der SalesWings [Rule Engine](https://helium.saleswings.pro/falcon) konfiguriert wurde |
| `sw_predictive_score` | String | Der Wert des [prädiktiven Scores](https://support.saleswingsapp.com/en/articles/581795-the-predictive-lead-score) von SalesWings, der das Engagement des Leads auf der Grundlage der Anzahl und Aktualität der getrackten Aktivitäten bewertet. Die möglichen Werte sind `HOT`, `WARM`, `NORMAL`, `COLD` oder `FROZEN` |
| `sw_salesforce_record_id` | String | Die ID des Lead- oder Kontaktdatensatzes in Salesforce CRM |
| `sw_salesforce_record_url` | String | Die URL des Lead- oder Kontaktdatensatzes in Salesforce CRM |
| `sw_session_count` | Ganzzahl | Die Anzahl der getrackten Sitzungen auf Ihrer Website für diesen Lead |
| `sw_tags` | String-Array | Die von SalesWings identifizierten Bedürfnisse und Interessen, dargestellt als „Tags“. Die Namen der SalesWings-Tags, die in der SalesWings [Rule Engine](https://helium.saleswings.pro/falcon) konfiguriert sind und für diesen Lead gelten |
| Zusätzliche Lead-Score-Attribute | Gleitkommazahl | Ein angepasstes Attribut für jeden zusätzlichen Lead-Score, der in der SalesWings [Rule Engine](https://helium.saleswings.pro/falcon) konfiguriert wurde. Der Name des Attributs wird vom Namen des SalesWings-Scores abgeleitet. Ein Score mit dem Namen `Likeliness to meet` wird beispielsweise als angepasstes Attribut `sw_likeliness_to_meet` gesendet. Wenn Sie einen Score umbenennen, nachdem das System ihn erstellt hat, setzt SalesWings die Synchronisierung mit dem ursprünglichen Namen des angepassten Attributs fort. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SalesWings-Insights nach Braze pushen" }

Wenn der Push aktiviert ist, beginnt SalesWings sofort damit, angepasste Attribute an Braze zu senden, sobald sich die zugrundeliegenden Datenpunkte in den SalesWings-Lead-Profilen ändern, und synchronisiert nach und nach alle bestehenden Leads, auch wenn sie keine neuen Updates haben.

SalesWings aktualisiert alle Braze-Nutzer:innen mit einer E-Mail, die mit der E-Mail-Adresse des SalesWings-Lead-Profils übereinstimmt. Wenn es in Braze keine passenden Nutzer:innen gibt, legt SalesWings keine neuen an.

### Verwendung von Braze-Currents-Events in Ihrem CRM {#using-braze-currents-events-in-your-crm}

Wenn Sie einen Braze-Current mit SalesWings verbinden, erstellt SalesWings für alle Braze-Nutzer:innen mit einer E-Mail identifizierte Lead-Profile und erfasst unterstützte Braze-Events als Lead-Aktivität. In Ihrem CRM können alle Daten automatisch auf der Kontoebene des Leads aggregiert werden. Die aufgezeichneten Aktivitäten und Daten können mit den Verhaltensdaten, die mit dem SalesWings-Tracking-Skript oder Segment.com erfasst wurden, oder mit anderen Daten, die an die SalesWings-API gesendet werden, kombiniert werden, um die Bedürfnisse und die Verkaufsbereitschaft Ihrer potenziellen Kund:innen für Ihre Lead- und Account-Management-Prozesse zu ermitteln.

Die folgende Tabelle zeigt die von SalesWings unterstützten Braze-Event-Typen und ihre Darstellung im Verlauf der Lead-Aktivitäten und in der Rule Engine von SalesWings:

| Event-Kategorie | Event-Typ | Event-Name in SalesWings |
| ----------- | ----------- | ----------- |
| Canvas-Events | Eintritte | `[Nurturing] Added by marketing team onto the journey $canvas_name` |
| Kundenverhalten-Events | Angepasste Events | `[Custom Event tracked] $name` |
| Kundenverhalten-Events | Erste Sitzung | `[User Action] Today marks the user's first session` |
| Kundenverhalten-Events | Install-Attribution | `[User Action] User installed app from $source` |
| Kundenverhalten-Events | Kauf-Events | `[Purchase] Customer purchased $product_id for $price $currency` |
| Nachrichten-Events | Content-Card-Klick | `[Content Card engagement] Clicked on $campaign_name content card` |
| Nachrichten-Events | E-Mail-Bounce | `[Alerting or negative] Email hard-bounced. This person's email appears to be no longer valid` |
| Nachrichten-Events | E-Mail-Klick | `[Email campaign engagement] Clicked in email $campaign_name on $url` |
| Nachrichten-Events | E-Mail-Zustellung | `[Nurturing] Received email $campaign_name` |
| Nachrichten-Events | E-Mail-Öffnung | `[Email campaign engagement] Opened email $campaign_name` |
| Nachrichten-Events | E-Mail-Abmeldung | `[Subscription status change] Unsubscribed from $campaign_name` |
| Nachrichten-Events | In-App-Nachricht-Klick | `[In-app campaign engagement] Clicked on message $campaign_name` |
| Nachrichten-Events | Push-Öffnung | `[Push notification engagement] Clicked on notification $campaign_name` |
| Nachrichten-Events | Eingehende SMS/MMS empfangen | `[SMS/mobile campaign engagement] We received a message from this person to our internal number $inbound_phone_number: $message_body` |
| Nachrichten-Events | SMS/MMS-Kurzlink-Klick | `[SMS/mobile campaign engagement] Clicked on $short_url` |
| Nachrichten-Events | Eingehende WhatsApp-Nachricht empfangen | `[WhatsApp engagement] We received a message from this person to our WhatsApp number $inbound_phone_number: $message_body` |
| Nachrichten-Events | WhatsApp gelesen | `[WhatsApp engagement] Lead read our message from the $campaign_name campaign` |
| Abos | Globale Abostatus-Änderung | `[Subscription status change] Global marketing subscription setting set to $subscription_status` |
| Abos | Statusänderung der Abo-Gruppe | `[Subscription status change] $subscription_status to/from $campaign_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Verwendung von Braze-Currents-Events in Ihrem CRM" }

Sie können dann die Bedingungen für **Custom Event** > **Event Name** und **Custom Event** > **Event Property** für SalesWings-Tags und -Scores anhand der SalesWings-Event-Namen aus der obigen Tabelle konfigurieren. Die Liste der Event-Eigenschaften, die für Bedingungen zur Verfügung stehen, ist mit einigen häufig verwendeten Einträgen vorausgefüllt. Sie können jederzeit neue Eigenschaften im Abschnitt **Event Property** auf der [Konfigurationsseite der Rule Engine](https://helium.saleswings.pro/falcon) hinzufügen.

![Beispiel für eine Event-Name-Bedingung.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_custom_event_condition.png %})

Für die Konfiguration und weitere Fehlerbehebung wenden Sie sich an das [SalesWings-Serviceteam](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) für Onboarding-Support.