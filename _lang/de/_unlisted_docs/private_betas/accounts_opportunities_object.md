---
nav_title: Konto-Objekte
article_title: Konto-Objekte
page_type: reference
permalink: /account_object/
hidden: true
description: "Erfahren Sie, wie Sie Konto-Objekte verwenden, um Segmente von Nutzer:innen basierend auf ihrer Kontozugehörigkeit zu erstellen und dann personalisierte Nachrichten mit Liquid-Tags zu versenden."
---

# Konto-Objekte {#account-objects}

> Erfahren Sie, wie Sie Konto-Objekte verwenden, um Segmente von Nutzer:innen basierend auf ihrer Kontozugehörigkeit zu erstellen und dann personalisierte Nachrichten mit Liquid-Tags zu versenden.

Um Kontodaten zu importieren, verwenden Sie eine [CSV-Datei](#using-a-csv-file) oder die Braze API. Mit der Braze API können Sie [mehrere Konten erstellen](#create-multiple-accounts), [ein einzelnes Konto erstellen](#create-one-account), [mehrere Konten löschen](#delete-multiple-accounts) und [ein einzelnes Konto löschen](#delete-one-account).

| Zielgruppe | Wie Sie diesen Artikel nutzen |
|----------|----------------------------|
| Marketer | Importieren Sie Nutzer:innen- und Kontodaten per CSV, erstellen Sie Segmente basierend auf Kontoattributen und personalisieren Sie Nachrichten mit Kontoinformationen in Braze. |
| Entwickler:innen | Verwenden Sie die Braze REST API, um Kontodatensätze programmatisch zu erstellen, zu aktualisieren und zu löschen und Braze mit Ihren Daten synchron zu halten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Konto-Objekte befinden sich derzeit in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager, wenn Sie an der Teilnahme an dieser Beta interessiert sind.
{% endalert %}

## So funktioniert es {#how-it-works}

Account-Objekte sind angepasste Datenstrukturen, die das Unternehmen einer Nutzerin oder eines Nutzers repräsentieren. Sie sind mit Nutzerprofilen verknüpft, sodass Sie B2B-Segmente erstellen und Nachrichten personalisieren können. Verwenden Sie Account-Felder wie Firmenname, Branche, Rolle oder Deal-Status mit Braze-Katalogen, Segmentierungsfiltern und Liquid-Tags.

Sie können beispielsweise Nutzer:innen ansprechen, die im Gesundheitswesen tätig sind, und personalisierte Nachrichten an Ärzt:innen und Krankenhausadministrator:innen senden, um Ihre Nachricht noch relevanter zu gestalten.

Um Account-Objekte zu verwenden, importieren Sie drei Arten von Daten in Braze:

- **Nutzerdaten:** Individuelle Nutzerprofile, die zur Identifizierung jeder Person in Braze verwendet werden (zum Beispiel über `external_id`, E-Mail, Telefon oder Nutzer-Alias). Importieren Sie Nutzerdaten per CSV.
- **Nutzer-Account-Beziehungsdaten:** Die Beziehung zwischen einer Nutzerin oder einem Nutzer und einem Account, einschließlich des Unternehmens, dem sie angehören, und der Rolle, die sie in diesem Account haben. Importieren Sie diese Beziehungsdaten per CSV.
- **Account-Daten:** Die Unternehmensdatensätze selbst, wie Firmenname, Branche, Jahresumsatz und andere firmografische Details. Dies sind die Datensätze, auf die Sie in Segmenten und Nachrichten abzielen und gegen die Sie personalisieren. Importieren Sie Account-Daten per CSV oder über die Braze REST API.

Alle drei Datentypen müssen importiert werden, damit Account-Objekte funktionieren. Nutzerdaten identifizieren Personen in Braze, Nutzer-Account-Beziehungsdaten verknüpfen diese Nutzer:innen mit bestimmten Accounts und Rollen, und Account-Daten liefern die Attribute auf Unternehmensebene, die für Segmentierung und Personalisierung verwendet werden.

## Voraussetzungen {#prerequisites}

Bevor Sie dieses Feature nutzen können, müssen bereits Nutzer:innen in Braze vorhanden sein.

## Daten in Braze importieren {#import-data-to-braze}

Um Account-Objekte in Ihren Nachrichten zu verwenden, sollten Ihre Nutzerdaten bereits in Braze vorhanden sein. Führen Sie anschließend zwei Importe durch: Importieren Sie zunächst die Nutzer-Account-Beziehungsdaten, um Account-Zuordnungen und Rollen festzulegen (derzeit nur per CSV). Importieren Sie dann die Account-Daten mit den Unternehmensdetails, die für Segmentierung und Personalisierung verwendet werden (per CSV oder über die Braze REST API).

### Schritt 1: Nutzer-Account-Beziehungsdaten importieren {#step-1-import-user-account-relationship-data}

Importieren Sie zunächst Ihre Nutzer-Account-Beziehungsdaten als CSV-Datei mit den folgenden Feldern in Braze. So kann Braze bestehende Nutzer:innen den richtigen Accounts und Rollen zuordnen.

<style>
table td {
    word-break: break-word;
}
</style>

| Feldname         | Feldtyp    | Erforderlich | Beschreibung                                                                                           |
|------------------|------------|----------|-------------------------------------------------------------------------------------------------------|
| `account_id`       | String     | Ja      | Der Account, zu dem die Nutzer:in gehört. Entspricht dem Feld `id` des Account-Objekts (CRM-ID). |
| `external_id`      | String     | Ja      | Die [externe ID](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles) der Nutzer:in in Braze. |
| `user_alias_name`  | String     | Nein*      | Der [Alias-Name](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle#user-aliases) der Nutzer:in in Braze. |
| `user_alias_label` | String     | Nein*      | Das [Alias-Label](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle/#what-happens-when-you-identify-anonymous-users) der Nutzer:in in Braze. |
| `email`            | String     | Nein*     | Die E-Mail-Adresse der Nutzer:in. |
| `phone`            | String     | Nein*      | Die Telefonnummer der Nutzer:in. |
| `user_role`             | String     | Nein       | Die Rolle der Nutzer:in im Account, z. B. „Verzeichnis“ oder „Mitarbeiter:in“. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
<sup>Eines der Felder `external_id`, `email`, `phone` oder `user_alias` ist erforderlich, um eine Nutzer:in zu identifizieren.</sup>

#### CSV-Datei verwenden {#using-a-csv-file}

Laden Sie Ihre CSV-Datei mit den Nutzer-Account-Beziehungen in Braze hoch:

1. Gehen Sie zu **Data Settings** > **Accounts**.
2. Wählen Sie **Update data**.
3. Wählen Sie unter **CSV upload** die Option **Users** und laden Sie Ihre Datei in Braze hoch.

![Das Dropdown „Upload data“ auf der Seite „Accounts“ in Braze.]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/update_account_data_csv.png %})

### Schritt 2: Account-Daten importieren {#step-2-import-account-data}

Accounts sind Unternehmen, denen Ihre Nutzer:innen angehören. Importieren Sie Ihre Account-Daten als CSV-Datei mit den folgenden Feldern in Braze. Beachten Sie, dass jedem Account eine ID und ein Name zugewiesen werden muss.

<style>
table td {
    word-break: break-word;
}
</style>

| Feldname                      | Feldtyp    | Erforderlich | Beschreibung                                                                        |
|-----------------------------|------------|----------|------------------------------------------------------------------------------------|
| `id`                          | String     | Ja      | Die ID des Accounts in Ihrer CRM-Plattform (Customer Relationship Management). |
| `name`                        | String     | Ja      | Der Name des Accounts.                                                                |
| `type`                        | String     | Nein       | Der Typ des Accounts, z. B. Kund:in, Partner oder Reseller.                                                                                   |
| `annual_revenue`              | String     | Nein       | Jahresumsatz des Accounts.                                                      |
| `industry`                    | String     | Nein       | Branche, in der der Account tätig ist.                                             |
| `number_of_employees`         | String     | Nein       | Anzahl der Mitarbeitenden, unterstützt Bereiche.                                           |
| `address`                     | String     | Nein       | Straßenadresse des Accounts.                                                      |
| `city`                        | String     | Nein       | Ort, an dem sich der Account befindet.                                                  |
| `state`                       | String     | Nein       | Bundesland/Staat, in dem sich der Account befindet.                                                 |
| `postal_code`                 | String     | Nein       | Postleitzahl der Account-Adresse.                                              |
| `country`                     | String     | Nein       | Land, in dem sich der Account befindet.                                               |
| `notes`                       | String     | Nein       | Zusätzliche Anmerkungen zum Account.                                                 |
| `website`                     | String     | Nein       | Website-URL des Accounts.                                                        |
| `main_phone`                  | String     | Nein       | Haupttelefonnummer des Accounts.                                                  |
| `created_date`                | Time       | Nein       | Datum, an dem der Account erstellt wurde.                                                  |
| `account_owner_email_address` | String     | Nein       | Interne:r Account-Inhaber:in (z. B. „Tom aus dem Vertrieb von Unternehmen A betreut Unternehmen B“).      |
| `parent_account_id`           | String     | Nein       | ID des übergeordneten Accounts, falls zutreffend (z. B. Verknüpfung mit der ID eines Mutterunternehmens). |
| `sic_code`                    | String     | Nein       | Branchenklassifizierungscode (SIC-Code).                                              |
| Benutzerdefinierte Felder                 | N/A        | Nein       | Benutzerdefinierte Felder, die von Ihnen definiert und verwaltet werden.                                                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
{% alert note %}
Obwohl einige Felder optional sind, sollten Sie sie nach Möglichkeit angeben, da es sich um reservierte Feldnamen handelt, die dazu beitragen, Ihre Daten organisiert zu halten.
{% endalert %}

Importieren Sie anschließend Ihre Account-Daten in Braze, indem Sie eine CSV-Datei hochladen oder die Braze REST API verwenden. Sie können diese Daten unter **Data Settings** einsehen. Eine Bearbeitung im Browser-Editor ist nicht möglich.

#### CSV-Datei verwenden

So importieren Sie Ihre Daten per CSV:

1. Gehen Sie zu **Data Settings** > **Accounts**.
2. Wählen Sie **Update data**.
3. Wählen Sie unter **CSV upload** die Option **Account Data** und laden Sie Ihre Datei in Braze hoch.

![Das Dropdown „Upload data“ auf der Seite „Accounts“ in Braze.]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/update_account_data_csv.png %})

### Fehlerbehebung bei CSV-Importen {#troubleshooting-csv-imports}

#### Leere Zeilen bei CSV-Importen von Account-Objekten {#empty-rows-in-account-objects-csv-imports}

Wenn Sie Account-Objekt-Daten importieren und auf der Seite **Accounts** leere Zeilen sehen, prüfen Sie, ob Account-Feldwerte Kommas enthalten.

Bei CSV-Importen von Account-Objekten können Kommas in Werten als Trennzeichen interpretiert werden. Dies kann dazu führen, dass Werte falsch geparst werden und leere Zeilen im Dashboard erscheinen.

Um dieses Problem zu beheben, entfernen Sie Kommas aus der ursprünglichen CSV-Datei und laden Sie sie erneut hoch. Ändern Sie beispielsweise `"$5,000,000"` in `"$5000000"` oder `"$5 million"`, bevor Sie die Datei erneut hochladen.

## Braze API verwenden {#using-the-braze-api}

APIs (Application Programming Interfaces) ermöglichen es verschiedenen Softwaresystemen, programmatisch zu kommunizieren. Wenn Sie mit der Braze API interagieren, senden Sie HTTP-Anfragen an bestimmte Endpunkte. Endpunkte sind strukturierte URLs, die Anweisungen entgegennehmen und Antworten zurückgeben. Die HTTP-Methode teilt Braze mit, welche Aktion ausgeführt werden soll, und der Anfragekörper enthält die Daten.

Für die Kontoverwaltung verwendet die Braze API diese HTTP-Methoden:

| Methode | Zweck | Verhalten |
|--------|---------|----------|
| `PUT` | Ressourcen erstellen oder aktualisieren | Fügt einen neuen Kontodatensatz hinzu, wenn keiner vorhanden ist. Aktualisiert den bestehenden Datensatz, wenn einer vorhanden ist. `PUT` ist idempotent konzipiert, sodass Sie dieselben Daten mehrfach synchronisieren können, ohne Duplikate zu erzeugen. |
| `DELETE` | Ressourcen entfernen | Entfernt den angegebenen Kontodatensatz und seine Zuordnungen dauerhaft aus Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Die Braze API gibt Ihnen programmatische Kontrolle über Kontodaten im großen Maßstab. Sie können Workflows zur Kontoverwaltung automatisieren, Kontoinformationen direkt aus Ihren Datenquellen synchronisieren und Braze mit Ihrer zentralen Datenquelle abgleichen – ohne manuelle Uploads oder Bearbeitungen. Dies reduziert den operativen Aufwand und sorgt für genaue, aktuelle Kontodaten für Segmentierung und Personalisierung.

Weitere Informationen zu HTTP-Methoden und der Funktionsweise von REST APIs finden Sie in den folgenden Ressourcen:
- [HTTP-Anfragemethoden](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods) auf MDN Web Docs
- [REST API Tutorial](https://restapitutorial.com/)
- [Braze API-Übersicht]({{site.baseurl}}/api/basics)

{% alert note %}
Verwenden Sie einen API-Schlüssel mit Katalog-Berechtigungen, um Anfragen an den Endpunkt `/business/accounts` zu authentifizieren.
{% endalert %}

Dieser Abschnitt behandelt die Verwendung der Braze API für:
- [Mehrere Konten erstellen](#create-multiple-accounts)
- [Ein einzelnes Konto erstellen](#create-one-account)
- [Mehrere Konten löschen](#delete-multiple-accounts)
- [Ein einzelnes Konto löschen](#delete-one-account)

### Mehrere Konten erstellen {#create-multiple-accounts}

Da `PUT` idempotent ist, können Sie dieselbe Anfrage mehrfach senden und Braze aktualisiert bestehende Datensätze, anstatt Duplikate zu erstellen. Dies macht es zu einer zuverlässigen Wahl, um Kontodatensätze in Braze aktuell zu halten.

Das folgende Code-Snippet sendet eine `PUT`-Anfrage an den Endpunkt `/business/accounts`. Das Array `accounts` enthält mehrere Unternehmensobjekte, die jeweils den in [Schritt 2: Kontodaten importieren](#step-2-import-account-data) definierten Kontofeldern zugeordnet sind. Braze verarbeitet jedes Objekt und erstellt oder aktualisiert den entsprechenden Datensatz auf Ihrer Seite **Konten**. Dieser Vorgang ist asynchron. Braze stellt die Anfrage in eine Warteschlange und verarbeitet sie im Hintergrund, was ihn gut für Massenimporte geeignet macht, bei denen keine sofortige Bestätigung erforderlich ist.

Um mehrere Konten zu erstellen, senden Sie eine `PUT`-Anfrage an `/business/accounts`. Wenn ein Konto nicht existiert, fügt Braze einen neuen Eintrag auf der Seite **Konten** hinzu. Jede Anfrage kann bis zu 50 Konten unterstützen. Beachten Sie, dass dieser Vorgang asynchron ist.

Ihre Anfrage sollte ähnlich wie die folgende aussehen:

```plaintext
curl -X PUT https://YOUR_REST_API_URL/business/accounts \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
          "accounts": [
              {
                  "id": "ACC001",
                  "name": "Acme Corporation",
                  "type": "Customer",
                  "annual_revenue": "$5,000,000",
                  "industry": "Manufacturing",
                  "number_of_employees": "150",
                  "address": "123 Industrial Way",
                  "city": "Metropolis",
                  "state": "NY",
                  "postal_code": "10001",
                  "country": "USA",
                  "notes": "Key client in the manufacturing sector",
                  "website": "http://www.acme.com",
                  "main_phone": "+1-212-555-1234",
                  "created_date": "2023-01-15T09:30:00Z",
                  "account_owner_email_address": "owner@example.com",
                  "parent_account_id": "",
                  "sic_code": "2011"
              },
              {
                  "id": "ACC002",
                  "name": "Global Solutions",
                  "type": "Partner",
                  "annual_revenue": "$10,000,000",
                  "industry": "Technology",
                  "number_of_employees": "500",
                  "address": "456 Tech Park",
                  "city": "Silicon Valley",
                  "state": "CA",
                  "postal_code": "94043",
                  "country": "USA",
                  "notes": "Important partner for software solutions",
                  "website": "http://www.globalsolutions.com",
                  "main_phone": "+1-650-555-5678",
                  "created_date": "2023-02-20T14:45:00Z",
                  "account_owner_email_address": "partner@example.com",
                  "parent_account_id": "ACC001",
                  "sic_code": "7372"
              },
              {
                  "id": "ACC003",
                  "name": "Oceanic Ventures",
                  "type": "Customer",
                  "annual_revenue": "$3,200,000",
                  "industry": "Retail",
                  "number_of_employees": "75",
                  "address": "789 Ocean Blvd",
                  "city": "Miami",
                  "state": "FL",
                  "postal_code": "33101",
                  "country": "USA",
                  "notes": "Expanding presence in retail markets",
                  "website": "http://www.oceanicventures.com",
                  "main_phone": "+1-305-555-6789",
                  "created_date": "2023-03-05T08:15:00Z",
                  "account_owner_email_address": "contact@example.com",
                  "parent_account_id": "",
                  "sic_code": "5941"
              }
          ]
      }'
```

### Ein einzelnes Konto erstellen {#create-one-account}

Wie beim Erstellen mehrerer Konten verwendet dieser Vorgang die `PUT`-Methode. Der Unterschied besteht darin, dass die Konto-ID direkt in der Endpunkt-URL statt im Anfragekörper enthalten ist. Dies gibt Ihnen präzise Kontrolle über einen einzelnen Datensatz.

Das folgende Code-Snippet sendet eine `PUT`-Anfrage an `/business/accounts/ACC001`, wobei `ACC001` der eindeutige Bezeichner für das Konto ist. Dieser Vorgang ist synchron. Braze verarbeitet die Anfrage sofort und gibt eine Antwort zurück, sobald sie abgeschlossen ist. Dies eignet sich gut für Realtime-Integrationen. Wenn sich beispielsweise Kontoinformationen in Ihrem System ändern, können Sie dieses Update sofort in Braze für Targeting oder Personalisierung widerspiegeln.

Um ein einzelnes Konto zu erstellen, senden Sie eine `PUT`-Anfrage an `/business/accounts/:account_id`. Wenn das Konto nicht existiert, erstellt Braze einen neuen Kontodatensatz. Dieser Vorgang ist synchron.

Ihre Anfrage sollte ähnlich wie die folgende aussehen:

```plaintext
curl -X PUT https://YOUR_REST_API_URL/business/accounts/ACC001 \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "accounts": [
            {
                "name": "Braze",
                "type": "Customer",
                "annual_revenue": "$5,000,000",
                "industry": "Manufacturing",
                "number_of_employees": "150",
                "address": "123 Industrial Way",
                "city": "Metropolis",
                "state": "NY",
                "postal_code": "10001",
                "country": "USA",
                "notes": "Key client in the manufacturing sector",
                "website": "http://www.acme.com",
                "main_phone": "+1-212-555-1234",
                "created_date": "2023-01-15T09:30:00Z",
                "account_owner_email_address": "owner@example.com",
                "parent_account_id": "",
                "sic_code": "2011"
            }
        ]
      }'
```

### Mehrere Konten löschen {#delete-multiple-accounts}

Die `DELETE`-Methode entfernt Kontodatensätze aus Braze. Im Gegensatz zu `PUT` sind `DELETE`-Anfragen nicht umkehrbar. Sobald ein Konto gelöscht wird, wird die Zuordnung zwischen Nutzer:innen und diesem Konto entfernt.

Das folgende Code-Snippet sendet eine `DELETE`-Anfrage an `/business/accounts` mit einer Liste von Konto-IDs im Anfragekörper. Braze verarbeitet jede ID und entfernt den entsprechenden Kontodatensatz. Dieser Vorgang ist asynchron. Braze stellt die Löschungen in eine Warteschlange und verarbeitet sie im Hintergrund. Verwenden Sie dies für Massenbereinigungsaufgaben, z. B. wenn eine Gruppe von Konten abgewandert ist, konsolidiert wurde oder für die Segmentierung in Braze nicht mehr relevant ist.

Um mehrere Konten zu löschen, senden Sie eine `DELETE`-Anfrage an `/business/accounts` mit einem Anfragekörper, der eine Liste von Konto-IDs enthält. Beachten Sie, dass dieser Vorgang asynchron ist.

Ihre Anfrage sollte ähnlich wie die folgende aussehen:

```plaintext
curl -X DELETE https://YOUR_REST_API_URL/business/accounts \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "accounts": [
      { "id": "ACC001" },
      { "id": "ACC002" },
      { "id": "ACC003" }
    ]
  }'
```

### Ein einzelnes Konto löschen {#delete-one-account}

Wie beim Erstellen eines einzelnen Kontos zielt dieser Vorgang auf ein bestimmtes Konto ab, indem dessen ID direkt in der Endpunkt-URL enthalten ist. Dies gibt Ihnen präzise Kontrolle über einen einzelnen Datensatz, ohne andere zu beeinflussen.

Das folgende Code-Snippet sendet eine `DELETE`-Anfrage an `/business/accounts/ACC001`. Dieser Vorgang ist synchron. Braze verarbeitet die Anfrage sofort und gibt eine Antwort zurück, sobald sie abgeschlossen ist. Verwenden Sie dies, wenn ein einzelnes Konto geschlossen, zusammengeführt oder aus Compliance- oder Datenhygiene-Gründen aus Braze entfernt werden muss.

Um ein einzelnes Konto zu löschen, senden Sie eine `DELETE`-Anfrage an `/business/accounts/:account_id`. Beachten Sie, dass dieser Vorgang synchron ist.

Ihre Anfrage sollte ähnlich wie die folgende aussehen:

```plaintext
curl -X DELETE https://YOUR_REST_API_URL/business/accounts/ACC001 \
  -H "Authorization: Bearer YOUR-REST-API-KEY"
```

## Objekte in Nachrichten verwenden {#using-objects-in-messages}

Nachdem Sie Ihre [Daten in Braze importiert](#importing-data-to-braze) haben, können Sie Account-Objekte verwenden, um ein Segment zu erstellen und personalisierte Nachrichten mithilfe von Liquid an Nutzer:innen zu senden.

### Schritt 1: Segment erstellen {#step-1-build-a-segment}

Erstellen Sie als Nächstes ein Segment, das Nutzerdaten und Account-Daten kombiniert. In diesem Beispiel sprechen Sie Direktor:innen bei Unternehmen im Gesundheitswesen an, um die Registrierung für ein neues Webinar Ihres Gesundheitsförderungsunternehmens zu steigern.

1. Gehen Sie zu **Audience** > **Segments** und wählen Sie **Create Segment** aus.
2. Geben Sie Ihrem Segment einen Namen.
3. Wählen Sie im **Segment Builder** den Filter **Business** aus und richten Sie die folgenden Segmentierungsfilter ein. Wenn Sie fertig sind, wählen Sie **Save** aus.

| Filter                          | Beschreibung                                      |
|---------------------------------|--------------------------------------------------|
| `Role is exactly director`      | Zielt auf Nutzer:innen ab, deren Rolle speziell „Director“ ist |
| `Accounts industry matches regex healthcare` | Findet Nutzer:innen in Accounts mit Branchen, die mit dem Gesundheitswesen zusammenhängen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Um derzeit mehrere Account-Filter zu verwenden, wählen Sie **Add Criteria** aus, anstatt das **OR/AND**-Dropdown zu verwenden.
{% endalert %}

![Segmentierungsfilter, die so eingerichtet sind, dass ein Segment für Nutzer:innen erstellt wird, die Direktor:innen bei Unternehmen im Gesundheitswesen sind.]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/build_segment.png %})

{% alert note %}
Die Segmentierung funktioniert nur für die ersten 1.000 Account-Datensätze, die den Kriterien entsprechen. Sie können bis zu einen Business-Filter pro Segment verwenden, und alle Kriterien müssen in einem Filter enthalten sein.
{% endalert %}

### Schritt 2: Mit Liquid personalisieren {#step-2-use-liquid-to-personalize}

Jetzt können Sie Ihre Nachricht personalisieren, um Nutzer:innen Informationen über Opportunities zu senden. In diesem Beispiel verfassen Sie eine Nachricht an Ihre Direktor:innen und verlinken sie zum Webinar. Sie können auch einen Braze-Katalog verwenden, um branchenspezifische Bilder für die Personalisierung abzurufen.

#### Schritt 2.1: Mit Account-Informationen personalisieren {#step-21-personalize-with-account-information}

Wählen Sie **Business** als Personalisierungstyp aus und dann **Name**, um die Nachricht mit dem Firmennamen der Nutzer:innen zu personalisieren.

Folgendes wird in Ihre Zwischenablage kopiert.

{% raw %}
```javascript
{% business %}
{{ business_accounts[0].name }}
```
{% endraw %}

Braze generiert den {% raw %}`{% business %}`{% endraw %}-Tag, der ein Array namens `business_accounts` erstellt, das Account-Informationen für den zugehörigen Account enthält.

Passen Sie die automatisch generierte Ausgabe an, um Ihre Nachricht zu erstellen.

Im folgenden Beispiel verschieben Sie den Aufruf des {% raw %}`{% business %}`{% endraw %}-Tags an den Anfang der Nachricht und personalisieren mit dem Vornamen der Nutzer:innen. Verwenden Sie den Account-Namen, um die Nachricht zu personalisieren. Die Liquid-Ausgabe bleibt gleich, aber Sie platzieren sie in verschiedenen Teilen der Nachricht.

{% raw %}
```javascript
{% business %}

Hi {{${first_name}}},

We would love to invite you and your peers at {{ business_accounts[0].name }} to join our latest webinar named "Creating Optimal Health Outcomes for Patients".  Click the link below to register.
```
{% endraw %}

Die Ausgabe sieht in etwa wie folgt aus:

{% raw %}
```javascript
Hi John,

We would love to invite you and your peers at Sunshine Health to join our latest webinar named "Creating Optimal Health Outcomes for Patients". Click the link below to register.
```
{% endraw %}

#### Schritt 2.2: Mit Katalogen verbinden {#step-22-connect-with-catalogs}

Personalisieren Sie als Nächstes Ihre Nachricht weiter, indem Sie Braze-Kataloge verwenden, um ein Bild hinzuzufügen und zu speichern, das dem Unternehmen im Gesundheitswesen entspricht.

Für dieses Beispiel nehmen Sie an, dass Sie Folgendes haben:

- Einen eingerichteten Katalog namens `industry_assets`
- Die ID für jeden Katalogeintrag ist der Name einer Branche, die den Branchen in Ihren Accounts entspricht
- Die Bild-URL-Links für ein primäres und ein sekundäres Bild.

Das Folgende ist ein Beispiel für das in dieser Personalisierung verwendete Liquid.
{% raw %}
```javascript
//Make a call to the business tag.  This sets the accounts array and prepares us to pull account data out.
{% business %}

//Assign the user's accounts industry to a variable called industry.  This step isn't required but it makes everything easier to read.
{% assign industry = {{business_accounts[0].industry}} %}

//Make a catalog_items call to the industry_assets catalog and ask for the industry item (in this case, it will ask for "healthcare")
{% catalog_items industry_assets industry %}

// Get the hero image for the "healthcare" industry
{{items[0].hero_image}}
```
{% endraw %}

## Häufig gestellte Fragen (FAQ) {#faq}

### Kann ich benutzerdefinierte Felder hinzufügen? {#can-i-add-custom-fields}

Ja. Sie können benutzerdefinierte Felder zu Konten hinzufügen. Wenn Sie eine eigene Lead-Scoring-Methode haben, können Sie auch ein benutzerdefiniertes Feld in Ihrem Konto-Objekt verwenden, um dies zu verfolgen.

### Kann eine Nutzerin oder ein Nutzer mit mehr als einem Konto verknüpft sein? {#can-a-user-be-associated-with-more-than-one-account}

Nein. Derzeit kann jede Nutzerin und jeder Nutzer nur eine Kontozuordnung haben.

### Kann ein Nutzerprofil mehrere E-Mail-Adressen enthalten? {#can-one-user-profile-contain-multiple-emails}

Nein. Ein Nutzerprofil kann nicht mehr als eine E-Mail-Adresse haben, z. B. eine private und eine geschäftliche E-Mail.