---
nav_title: Konten
article_title: Kontoobjekte
page_order: 7
page_type: reference
description: "Verwenden Sie Kontoobjekte, um Nutzer:innen zu segmentieren, Nachrichten mit Kontodaten zu personalisieren und Kontodatensätze zu verwalten."
---

# Kontoobjekte {#account-objects}

> Verwenden Sie Kontoobjekte, um Messaging mit Kontodaten zu segmentieren und zu personalisieren.

{% alert important %}
Konten befindet sich im Early Access. Diese Anweisungen können sich ändern, während das Feature weiterentwickelt wird.
{% endalert %}

Mit Kontoobjekten können Sie:

- Segmente mit Kontokriterien erstellen
- Nachrichten mit Kontoattributen über Liquid personalisieren
- Kontodatensätze an einem Ort verwalten

Kontoobjekte sind Datenmodelle auf Workspace-Ebene, die mit Nutzerprofilen verknüpft sind. Ein Kontodatensatz ist ein bestimmtes Konto und die zugehörigen Felddaten.
Verwenden Sie Kontoobjekte, wenn Kontokontext, wie z. B. Unternehmensattribute, Ihnen beim Targeting und der Personalisierung von Messaging hilft.
Sie können auch Kontohierarchien modellieren (z. B. übergeordnete und untergeordnete Konten) und ein Nutzerprofil mit mehreren Konten verknüpfen.

## Warum Kontoobjekte verwenden? {#why-use-account-objects}

Einige Anwendungsfälle erfordern Kontext auf Kontoebene, selbst wenn Ihre Campaigns und Canvases an einzelne Nutzer:innen gesendet werden.

Mit Kontoobjekten können Sie Kontodaten einmal speichern und sie für Segmentierung und Personalisierung in Braze wiederverwenden.

So können Sie:

- Nach Kontoattributen segmentieren
- Nachrichten mit gemeinsamem Kontokontext personalisieren (z. B. Firmenname oder Branche)
- Beziehungen zwischen Konten modellieren und ein Nutzerprofil mit mehreren Konten verknüpfen

Dieser Ansatz ersetzt das Duplizieren derselben Kontoattribute über viele Nutzerprofile hinweg.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen:

- Ihr Workspace muss für den Early Access von Accounts freigeschaltet sein. Wenden Sie sich an Ihr Braze-Kontoteam.
- Sie müssen bereits Nutzer:innen in Braze haben.
- Nachdem Accounts aktiviert wurde, erscheint es unter **Data Settings** > **Accounts**. Wenn Sie Accounts zum ersten Mal verwenden, folgen Sie den Initialisierungsanweisungen auf dem Bildschirm.

## Kontodatenmodell {#account-data-model}

Jedes Konto erfordert eine externe ID (`id`) und einen Namen (`name`).

Die Kontofelder in diesem Abschnitt definieren das Schema des Kontoobjekts. Diese Felder gelten für jeden einzelnen Kontodatensatz, den Sie in Braze speichern.

Braze enthält standardmäßig Kontoobjekte mit Standardfeldern. Sie können angepasste Felder je nach Anwendungsfall hinzufügen und entfernen.

| Feldname | Feldtyp | Erforderlich | Beschreibung |
| --- | --- | --- | --- |
| `id` | String | Ja | Ihre System-ID für das Konto (z. B. CRM-ID). Muss in Ihrem Workspace eindeutig sein. |
| `name` | String | Ja | Kontoname. |
| `type` | String | Nein | Kontotyp, z. B. Kund:in, Partner oder Reseller. |
| `annual_revenue` | Zahl | Nein | Jahresumsatz des Kontos. |
| `industry` | String | Nein | Branche des Kontos. |
| `number_of_employees` | Zahl | Nein | Anzahl der Mitarbeitenden. |
| `address` | String | Nein | Straßenadresse. |
| `city` | String | Nein | Ort. |
| `state` | String | Nein | Bundesland oder Provinz. |
| `postal_code` | String | Nein | Postleitzahl. |
| `country` | String | Nein | Land. |
| `notes` | String | Nein | Zusätzliche Notizen. |
| `website` | String | Nein | Website-URL. |
| `main_phone` | String | Nein | Primäre Telefonnummer. |
| `created_date` | Zeitstempel | Nein | Zeitstempel der Kontoerstellung. |
| `sic_code` | String | Nein | Standard Industry Classification Code. |
| Angepasste Felder | angepasst | Nein | Felder, die Sie definieren und verwalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Felder des Kontodatenmodells" }

## Optionen für die Datenintegration {#data-integration-options}

Sie können Kontodatensätze verwalten über:

- REST API-Endpunkte für Kontodatensätze
- Bearbeitung im Browser unter **Data Settings** > **Accounts** für einzelne Datensätze

## Erste Schritte {#get-started}

### Schritt 1: Accounts aktivieren {#step-1-enable-accounts}

Accounts wird auf Unternehmensebene aktiviert. Während des Early Access übernimmt Ihr Braze-Kontoteam die einmalige Aktivierung.

Wenn Accounts aktiviert ist, gehen Sie zu **Data Settings** > **Accounts** und schließen Sie den einmaligen Initialisierungsablauf ab, falls Sie dazu aufgefordert werden.

### Schritt 2: Kontodatensätze hinzufügen {#step-2-add-account-records}

Fügen Sie Kontodatensätze über die REST API oder die browserbasierte Bearbeitung hinzu oder aktualisieren Sie sie.

### Schritt 3: Einen berechneten Filter für Kontokriterien erstellen {#step-3-create-a-calculated-filter-for-account-criteria}

Bevor Sie nach Kontodaten segmentieren, erstellen Sie einen berechneten Filter, der Ihre Kontokriterien definiert:

1. Gehen Sie zu **Audience** > **Calculated Filters**.
2. Wählen Sie **Create filter** und dann **Data Object filters** aus.
3. Definieren Sie Ihre Kontokriterien.

Weitere Informationen finden Sie unter [Berechnete Filter]({{site.baseurl}}/user_guide/audience/segments/calculated_filters#create-a-calculated-filter).

### Schritt 4: Den berechneten Filter im Segment Builder verwenden {#step-4-use-the-calculated-filter-in-segment-builder}

Wählen Sie im Segment Builder den von Ihnen erstellten berechneten Filter aus und fügen Sie dann alle zusätzlichen Nutzerattribut-Filter hinzu, die Ihr Campaign- oder Canvas-Targeting unterstützen.

## Kontobasierte Segmente erstellen {#build-account-based-segments}

Sobald Ihre Kontodatensätze und der berechnete Filter bereit sind:

1. Gehen Sie zum [Segment Builder]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
2. Fügen Sie Ihren vorkonfigurierten berechneten Filter für Kontokriterien hinzu.
3. Fügen Sie alle zusätzlichen Nutzerattribut-Filter hinzu.
4. Speichern Sie Ihr Segment.

Zum Beispiel:

- **Berechneter Filter:** Konto `industry` ist genau `healthcare`
- **Nutzerattribut-Filter:** `days_since_last_login` ist kleiner als `30`

## Mit Liquid personalisieren {#personalize-with-liquid}

Verwenden Sie den Liquid-Tag `{% raw %}{% data_object account %}{% endraw %}`, um Kontodaten für den/die Nutzer:in in das Array `data_objects` zu laden.

{% alert note %}
Wenn Sie **Vorschau und Test** verwenden, nutzen Sie ein Segment, das Kontodaten enthält, damit die Personalisierung korrekt aufgelöst werden kann.
{% endalert %}

{% raw %}
```liquid
{% data_object account %}
Hi {{${first_name}}},
We'd love to invite you and your peers at {{ data_objects[0].name }}.
```
{% endraw %}

Um alle zugeordneten Konten zu durchlaufen:

{% raw %}
```liquid
{% data_object account %}
{% for acct in data_objects %}
- {{ acct.name }}
{% endfor %}
```
{% endraw %}

## API-Grundlagen {#api-basics}

Sie können die REST API verwenden, um Kontodatensätze während des Early Access zu verwalten.

Einzelheiten zu den Endpunkten finden Sie unter [Data Objects-Endpunkte]({{site.baseurl}}/api/endpoints/data_objects).

Informationen zur Authentifizierung und den Grundlagen von REST-Endpunkten finden Sie in der [Braze-API-Übersicht]({{site.baseurl}}/api/basics).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann ich benutzerdefinierte Felder zu Konten hinzufügen? {#can-i-add-custom-fields-to-accounts}

Ja. Sie können benutzerdefinierte Kontofelder in Ihrem Workspace definieren und verwalten. Informationen zu den Feldanforderungen finden Sie unter [Kontodatenmodell](#account-data-model).

### Ist Accounts ein kostenpflichtiges Add-on? {#is-accounts-a-paid-add-on}

Nein. Accounts ist kein kostenpflichtiges Add-on und ist in allen Plänen verfügbar. Während des Early Access muss Ihr Braze-Kontoteam es für Ihren Workspace aktivieren.