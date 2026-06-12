---
nav_title: Datenmodelle
article_title: Ein B2B-Datenmodell erstellen
page_order: 0
page_type: reference
description: "Erfahren Sie, wie Sie mit den Daten-Tools von Braze B2B-Modelle erstellen können."
---

# Ein B2B-Datenmodell erstellen {#create-a-b2b-data-model}

> Dieser Anwendungsfall zeigt, wie Sie mit den Daten-Tools von Braze ein effektives und effizientes B2B-Datenmodell erstellen können, das Ihnen beim Targeting, Triggern, Personalisieren und Versenden von Nachrichten an Ihre Geschäftsnutzer:innen hilft.

{% alert note %}
Diese Empfehlungen können sich im Laufe der Zeit ändern, wenn Braze seine B2B-Funktionen weiterentwickelt.
{% endalert %}

Bevor wir uns damit befassen, wie Sie Ihr B2B-Datenmodell einrichten können, sollten Sie einige Konzepte und Begriffe kennen.

Es gibt vier primäre B2B-Objekte, die Sie für die Durchführung von B2B-Kampagnen benötigen.

| Objekt | Beschreibung |
| --- | --- |
| Leads | Ein Datensatz von Interessent:innen, die Interesse an einem Produkt oder einer Dienstleistung gezeigt haben, aber noch nicht als Opportunity qualifiziert wurden. |
| Kontakte | In der Regel Personen, die qualifiziert und von einem Lead in einen Kontakt umgewandelt wurden, um eine Opportunity zu verfolgen. |
| Opportunities | Ein Datensatz, der die Details eines potenziellen Verkaufs oder eines laufenden Geschäfts verfolgt.
| Konten | Ein Datensatz über eine Organisation, die eine qualifizierte Interessent:in, eine bestehende Kund:in, ein Partner oder ein Wettbewerber mit einer Beziehung von ähnlicher Bedeutung ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ein B2B-Datenmodell erstellen" }

In Braze werden diese vier Objekte kombiniert und auf zwei Objekte reduziert: Nutzerprofile und Geschäftsobjekte.

| Braze-B2B-Objekt | Beschreibung | Ursprüngliche B2B-Objekte  |
| --- | --- | --- |
| Nutzerprofile | Diese werden direkt den Leads und Kontakten in Ihrem Vertriebs-CRM-System zugeordnet. Da Leads von Braze erfasst werden, werden sie automatisch als Leads in Ihrem Vertriebs-CRM-System angelegt. Wenn sie in Kontakte umgewandelt werden, werden die Kontakt-IDs und -details zurück zu Braze synchronisiert. | Leads<br> Kontakte |
| Geschäftsobjekte | Diese lassen sich auf alle Nicht-Nutzer-Objekte in Ihrem Vertriebs-CRM-System abbilden. Dazu gehören Ihre vertriebsspezifischen Objekte, wie z. B. Kontoobjekte und Opportunity-Objekte. | Konten<br> Opportunities |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ein B2B-Datenmodell erstellen" }

## 1. Schritt: Erstellen Sie Ihre Geschäftsobjekte in Braze {#step-1-create-your-business-objects-in-braze}

Geschäftsobjekte sind alle nicht nutzerzentrierten Datensätze. Im B2B-Kontext gehören dazu Ihre Konto- und Opportunity-Daten sowie alle anderen relevanten, nicht nutzerzentrierten Datensätze, die Ihr Unternehmen verfolgt.

Es gibt zwei Methoden zur Erstellung und Verwaltung Ihrer Geschäftsobjekte in Braze: Kataloge und verbundene Quellen.

| Methode | Beschreibung |
| --- | --- |
| [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs/) | Dies sind unabhängige Datenobjekte (ergänzende Datenobjekte) zum primären Nutzerprofil in Braze. In einem B2B-Kontext würden Sie wahrscheinlich Kataloge für Ihre Konten und Opportunities haben. |
| [Verbundene Quellen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/) | Diese ermöglichen es Braze, Ihr Data Warehouse direkt abzufragen. Wahrscheinlich synchronisieren Sie Ihre Lead-, Kontakt-, Opportunity- und Konto-Objekte bereits regelmäßig mit Ihrem Data Warehouse, sodass Sie die Braze-Segmentierung direkt auf dieses Warehouse verweisen und es in einer Zero-Copy-Umgebung aktivieren können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="1. Schritt: Erstellen Sie Ihre Geschäftsobjekte in Braze" }

{% tabs %}
{% tab Catalogs %}

### Option 1: Verwenden Sie Kataloge für Konten und Opportunities {#option-1-use-catalogs-for-accounts-and-opportunities}

Kataloge sind Datentabellen, die in Braze gehostet und verwaltet werden. Während Konto- und Opportunity-Daten aus dem CRM-System Ihrer Wahl stammen, würden Sie diese in Braze duplizieren, um sie für Marketingzwecke zu verwenden: kontobasierte Segmentierung, kontobasiertes Marketing, Lead-Management und mehr.

Bei dieser Option empfehlen wir, einen Katalog für Ihre Konten und einen für Ihre Opportunities zu erstellen und beide regelmäßig zu aktualisieren, indem Sie Braze-Updates über unsere [Katalog-API]({{site.baseurl}}/api/endpoints/catalogs/) oder [Cloud-Datenaufnahme (CDI) für Kataloge]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/) senden. Stellen Sie bei der Erstellung dieser Kataloge sicher, dass die `id` (erste Spalte) Ihres Katalogs mit der `id` in Ihrem Vertriebs-CRM-System übereinstimmt.

#### Übertragen Sie Ihre CRM-Felder {#map-over-your-crm-fields}

In den nachstehenden Tabellen finden Sie einige Beispiele für Felder, die Sie aus den Konto- und Opportunity-Objekten Ihres CRM übertragen können.

{% subtabs %}
{% subtab Account catalog %}

In diesem Anwendungsfall ist Salesforce das Beispiel-CRM-System. Sie können jedes Feld übertragen, das in den Objekten Ihres CRM enthalten ist.

<table aria-label="CRM-Felder übertragen" border="1">
  <caption>CRM-Felder übertragen</caption>
  <thead>
  <tr>
    <th><b>Braze-Objekt</b></th>
    <th><b>Braze-Feld</b></th>
    <th><b>CRM-Objekt (Salesforce)</b></th>
    <th><b>CRM-Feld (Salesforce)</b></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td rowspan="4">Katalog &gt; Kontokatalog</td>
    <td><code>id</code></td>
    <td><code>account</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>AccountName</code></td>
    <td><code>account</code></td>
    <td><code>Account Name</code></td>
  </tr>
  <tr>
    <td><code>Type</code></td>
    <td><code>account</code></td>
    <td><code>Type</code></td>
  </tr>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>account</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tbody>
</table>

##### Beispieltabelle der zugeordneten Kontofelder {#example-table-of-mapped-account-fields}

![Tabelle mit Salesforce-Konten und den entsprechenden Informationen, wie Rechnungsadresse und Kontoinhaber.]({% image_buster /assets/img/b2b/sf_accounts.png %})

{% endsubtab %}
{% subtab Opportunity catalog %}

In diesem Anwendungsfall ist Salesforce das Beispiel-CRM-System. Sie können jedes Feld übertragen, das in den Objekten Ihres CRM enthalten ist.

<table aria-label="Beispieltabelle der zugeordneten Kontofelder" border="1">
  <caption>Beispieltabelle der zugeordneten Kontofelder</caption>
  <thead>
  <tr>
    <th><b>Braze-Objekt</b></th>
    <th><b>Braze-Feld</b></th>
    <th><b>CRM-Objekt (Salesforce)</b></th>
    <th><b>CRM-Feld (Salesforce)</b></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td rowspan="4">Katalog &gt; Opportunity-Katalog</td>
    <td><code>id</code></td>
    <td><code>opportunity</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>OpportunityName</code></td>
    <td><code>opportunity</code></td>
    <td><code>Opportunity Name</code></td>
  </tr>
  <tr>
    <td><code>Territory</code></td>
    <td><code>opportunity</code></td>
    <td><code>Territory</code></td>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>opportunity</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tr>
  </tbody>
</table>

##### Beispieltabelle der zugeordneten Opportunity-Felder {#example-table-of-mapped-opportunity-fields}

![Tabelle mit Salesforce-Opportunities und den entsprechenden Informationen, wie Rechnungsadresse und Kontoinhaber.]({% image_buster /assets/img/b2b/sf_opportunities.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Connected sources %}

### Option 2: Verwenden Sie verbundene Quellen für Konten und Opportunities {#option-2-use-connected-sources-for-accounts-and-opportunities}

Verbundene Quellen sind Datentabellen, die von Ihnen in Ihrem eigenen Data Warehouse gehostet und von Braze über [CDI-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/) abgefragt werden. Im Gegensatz zu Katalogen würden Sie Ihre Geschäftsobjekte (Konten und Opportunities) nicht in Braze duplizieren, sondern in Ihrem Data Warehouse belassen und Ihr Warehouse als Single Source of Truth nutzen.

Wie Sie verbundene Quellen einrichten, erfahren Sie unter [Verbundene Quellen integrieren]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/#integrating-connected-sources).

{% endtab %}
{% endtabs %}

## 2. Schritt: Verknüpfen Sie Ihre Geschäftsobjekte mit Nutzerprofilen {#step-2-relate-your-business-objects-to-user-profiles}

Nutzerprofile sind das primäre Objekt in Braze und ermöglichen den Großteil Ihrer demografischen Segmentierung, Triggerung und Personalisierung. Nutzerprofile umfassen [Standard-Nutzerdaten]({{site.baseurl}}/user_guide/data/unification/user_data/), die von unserem SDK und anderen Quellen erfasst werden, einschließlich [angepasster Daten]({{site.baseurl}}/user_guide/data/activation/), die in Form von Attributen (demografische Daten), Ereignissen (Verhaltensdaten) oder Käufen (Transaktionsdaten) vorliegen.

### Schritt 2.1: Vertriebs-CRM-IDs auf Braze abbilden {#step-21-map-sales-crm-ids-to-braze}

Stellen Sie zunächst sicher, dass Braze und das CRM Ihrer Wahl über einen gemeinsamen Bezeichner verfügen, um Daten auszutauschen. Wir empfehlen, die folgende Tabelle zu verwenden, um die ID-Felder Ihres Vertriebs-CRM auf das Braze-Nutzerobjekt abzubilden. In der folgenden Tabelle ist Salesforce als CRM-System angegeben, aber dies kann mit jedem CRM durchgeführt werden.

#### Braze-Objekt: Nutzer:in {#braze-object-user}

| Braze-Feld | CRM-Objekt (Salesforce) | CRM-Feld (Salesforce) | Zusätzliche Informationen |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | Lead | `id` | - Alias-Label: `salesforce_lead_id` <br>- Alias-Name: `lead_id` |
| `Aliases.salesforce_contact_id` | Kontakt | `id` | - Alias-Label: `salesforce_contact_id` <br>- Alias-Name: `contact_id` |
| `AccountId` | Kontakt | `AccountId` |
| `OpportunityId` (optional, skalar) <br>oder<br> `Opportunities` (optional, Array) | Opportunity | `id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Braze-Objekt: Nutzer:in" }

{% alert note %}
Wir empfehlen die Verwendung von [Aliasen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#user-aliases) anstelle von `external_id`, um Salesforce-Lead- und Kontakt-Bezeichner auf Braze abzubilden. Dies reduziert die Anzahl der erforderlichen Suchvorgänge beim Identifizieren und Umsetzen Ihrer produktgesteuerten Wachstumsinitiativen.
{% endalert %}

Nachdem Sie Ihre IDs synchronisiert haben, müssen Sie Ihre Braze-Nutzerprofile mit Ihren Geschäftsobjekten verknüpfen.

### Schritt 2.2: Erstellen Sie eine Beziehung zwischen Nutzerprofilen und Ihren Geschäftsobjekten {#step-22-create-a-relationship-between-user-profiles-and-your-business-objects}

{% tabs %}
{% tab Catalogs %}

#### Option 1: Bei Verwendung von Katalogen {#option-1-when-using-catalogs}

Da Ihre Opportunity- und Kontodaten nun als Braze-Kataloge erfasst sind, müssen Sie eine Beziehung zwischen diesen Katalogen und den Nutzerprofilen herstellen, an die Sie Nachrichten senden möchten. Derzeit sind dafür zwei Schritte erforderlich:

1. Nehmen Sie das Konto (z. B. `account_id (string)`), die Opportunity-ID (z. B. `opportunity_ids (array)`) oder beides als Attribute in das Nutzerprofil auf.
2. Protokollieren Sie ein Ereignis (z. B. `account_linked`), das die Konto-ID als Ereignis-Eigenschaft enthält.

```json
{
  "attributes" : [
    {
      "external_id" : "user1",
      "accountId" : "001J7000004K7AF",
      "opportunityIds" : [
"0064J000004EU59",
"0064J000004EU5G"
]
    }
  ],
  "events" : [
    {
      "external_id" : "user1",
      "name" : "account_linked",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "account_id": "001J7000004K7AF"
      }
    }
  ]
}
```

{% endtab %}
{% tab Connected sources %}

#### Option 2: Bei Verwendung verbundener Quellen {#option-2-when-using-connected-sources}

Eine der Tabellen Ihrer verbundenen Quelle sollte eine `user_id` enthalten, die mit der in Braze für Ihre Nutzer:innen festgelegten `external_user_id` übereinstimmt. Die oben beschriebene Nutzerprofil-Einrichtung verwendet Ihre Lead- und `contact_ids` als `external_id`, daher sollten Sie sicherstellen, dass Ihre Lead-/Kontakttabellen diese IDs enthalten.

Zusätzlich zur Übereinstimmung der IDs empfehlen wir, grundlegende Daten auf Kontoebene wie `account_id`, `opportunity_id` und sogar gängige firmografische Attribute wie `industry` in die Nutzerprofile zu schreiben, um eine effiziente Segmentierung und Personalisierung zu ermöglichen.

{% endtab %}
{% endtabs %}