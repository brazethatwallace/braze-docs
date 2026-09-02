---
nav_title: Nutzer:innen Produkte empfehlen
article_title: Nutzer:innen Produkte empfehlen
page_order: 4
page_type: reference
description: "Dieser Referenzartikel zeigt Ihnen, wie Sie die Braze REST API, Kataloge und Connected-Content nutzen, um Nutzer:innen über verschiedene Messaging-Kanäle personalisierte Produktempfehlungen anzuzeigen."
---

# Nutzer:innen Produkte empfehlen {#recommending-products-to-users}

> Nutzen Sie die Braze REST API zusammen mit [Katalogen]({{site.baseurl}}/user_guide/data/activation/catalogs/create) oder [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), um personalisierte Produktempfehlungen in Ihren Nachrichten anzuzeigen. Mit diesem Ansatz können Sie Ihr eigenes Empfehlungssystem in das Braze-Messaging-Ökosystem einbinden, sodass nicht-technische Nutzer:innen den Inhalt und die Nachrichten rund um jede Empfehlung eigenständig verwalten können.

Mit diesem Ansatz können Sie:

- Produktempfehlungen aus Ihrem Backend über die REST API in Nutzerprofilen speichern.
- Produkt-Metadaten zum Sendezeitpunkt über Kataloge oder Connected-Content abrufen.
- Personalisierte Empfehlungen über jeden Messaging-Kanal anzeigen, einschließlich E-Mail, Push, In-App-Nachrichten und mehr.

## Voraussetzungen {#prerequisites}

Um diese Anleitung abzuschließen, benötigen Sie:

| Voraussetzung | Beschreibung |
| --- | --- |
| Braze-REST-API-Schlüssel | Ein Schlüssel mit der Berechtigung `users.track` und, falls Kataloge über die API verwaltet werden, den entsprechenden Katalogberechtigungen. Um einen zu erstellen, navigieren Sie zu **Einstellungen** > **API-Schlüssel**. |
| Braze-Katalog | Ein Katalog, der Ihre Produktmetadaten enthält (z. B. Name, Kategorie, Preis und Bild-URL). Um einen zu erstellen, siehe [Katalog erstellen]({{site.baseurl}}/user_guide/data/activation/catalogs/create). |
| Liquid-Kenntnisse | Mittlere Vertrautheit mit [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) für das Erstellen von Templates mit personalisierten Variablen und die Verwendung von Connected-Content. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Schritt 1: Empfehlungen in Nutzerprofilen speichern {#step-1-store-recommendations-on-user-profiles}

Speichern Sie zunächst die von Ihrem Empfehlungssystem generierten Produktempfehlungen als angepasste Attribute in Braze-Nutzerprofilen. So können Sie bei der Nachrichtenzustellung auf die empfohlenen Produkte der einzelnen Nutzer:innen zugreifen.

1. Legen Sie fest, welche Empfehlungsdaten gespeichert werden sollen, z. B. Produkt-IDs oder bevorzugte Kategorien.
2. Verwenden Sie den Endpunkt [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), um die Empfehlung als angepasstes Attribut im Nutzerprofil zu speichern.

### Beispielanfrage {#example-request}

```http
POST YOUR_REST_ENDPOINT/users/track
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Ersetzen Sie `YOUR_REST_ENDPOINT` durch die [REST-Endpunkt-URL]({{site.baseurl}}/api/basics#endpoints) für Ihren Workspace.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "recommended_product_id": "1001"
    }
  ]
}
```

Verwenden Sie aussagekräftige Attributnamen (wie `recommended_product_id`), damit Sie später in Liquid-Templates leicht darauf verweisen können. Halten Sie die Empfehlungen aktuell, indem Sie sie regelmäßig aktualisieren, sobald Ihr Empfehlungssystem neue Ergebnisse liefert.

## Schritt 2: Produktmetadaten abrufen {#step-2-retrieve-product-metadata}

Nachdem Sie einen Empfehlungsbezeichner in jedem Nutzerprofil gespeichert haben, müssen Sie die vollständigen Produktmetadaten (Name, Preis, Bild usw.) abrufen, um sie in Ihre Nachricht einzubinden. Dafür stehen Ihnen zwei Optionen zur Verfügung:

- **Option A:** [Braze-Kataloge](#option-a-braze-catalogs) — Produktinformationen direkt in Braze speichern, um schnelle, integrierte Abfragen zu ermöglichen.
- **Option B:** [Connected Content](#option-b-connected-content) — Produktinformationen zum Sendezeitpunkt von einer externen API abrufen.

### Option A: Braze-Kataloge {#option-a-braze-catalogs}

Wenn Sie einen [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs/create) mit Ihrem Produktbestand erstellt haben, können Sie Artikel direkt in Ihrer Nachricht per Liquid nachschlagen. Eine vollständige Anleitung finden Sie unter [Kataloge verwenden]({{site.baseurl}}/user_guide/data/activation/catalogs/use).

#### Einen bestimmten Katalogartikel empfehlen {#recommend-a-specific-catalog-item}

{% raw %}
Um ein bestimmtes Produkt anhand seiner ID zu referenzieren, verwenden Sie den Liquid-Tag `catalog_items`. Um beispielsweise das Produkt `1001` aus einem Katalog mit dem Namen `retail_products` zu empfehlen:

```liquid
{% catalog_items retail_products 1001 %}

We have a new item we think you'll like:
Category: {{ items[0].category }}
Name: {{ items[0].name }}
Price: ${{ items[0].price }}
```
{% endraw %}

#### Mehrere Katalogartikel empfehlen {#recommend-multiple-catalog-items}

{% raw %}
Sie können auch mehrere Artikel in einem einzigen Tag referenzieren. Um beispielsweise drei Produkte hervorzuheben:

```liquid
{% catalog_items retail_products 1001 1003 1005 %}

New items added in:
- {{ items[0].category }}
- {{ items[1].category }}
- {{ items[2].category }}

Visit our store to learn more!
```
{% endraw %}

#### Artikel mithilfe der Empfehlung einer Nutzerin oder eines Nutzers als Template verwenden {#template-items-using-a-users-recommendation}

{% raw %}
Kombinieren Sie das angepasste Attribut aus [Schritt 1](#step-1-store-recommendations-on-user-profiles) mit einer Katalogabfrage, um die Empfehlung für jede Nutzerin und jeden Nutzer zu personalisieren:

```liquid
{% catalog_items retail_products {{custom_attribute.${recommended_product_id}}} %}

Hi {{${first_name}}}, check out our pick for you:
{{ items[0].name }} — ${{ items[0].price }}
```
{% endraw %}

### Option B: Connected Content {#option-b-connected-content}

Wenn Ihre Produktmetadaten in einem externen Dienst statt in einem Braze-Katalog gespeichert sind, verwenden Sie [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call), um die Daten zum Sendezeitpunkt abzurufen.

{% raw %}
Wenn Ihre interne API beispielsweise Produktdetails anhand der ID zurückgibt:

```liquid
{% connected_content https://api.yourcompany.com/products/{{custom_attribute.${recommended_product_id}}} :save product %}

Hi {{${first_name}}}, we think you'll love:
{{ product.name }} — ${{ product.price }}
```
{% endraw %}

Weitere Informationen zum Durchführen von API-Aufrufen aus Ihren Nachrichten finden Sie unter [Einen API-Aufruf durchführen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call).

{% alert warning %}
Vermeiden Sie es, Connected Content zu verwenden, um eine große Liste von Produkten abzurufen und diese dann zum Sendezeitpunkt in Liquid zu durchlaufen. Große Antwort-Payloads erhöhen die Sendelatenz und können bei hohem Volumen zu Nachrichten-Timeouts oder Zustellungsfehlern führen. Speichern Sie stattdessen nur die spezifischen Produkt-IDs, die Nutzer:innen benötigen, in ihrem Profil (siehe [Schritt 1](#step-1-store-recommendations-on-user-profiles)) und rufen Sie die Metadaten für diese einzelnen Artikel ab, oder verwenden Sie [Kataloge](#option-a-braze-catalogs), die für schnelle Abfragen optimiert sind.
{% endalert %}

## Schritt 3: Überprüfen Sie Ihre Integration {#step-3-verify-your-integration}

Überprüfen Sie nach Abschluss der Einrichtung Ihre Integration:

1. Verwenden Sie den Endpunkt [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), um eine Testempfehlung in Ihr eigenes Nutzerprofil zu schreiben.
2. Senden Sie eine Testnachricht, die auf das empfohlene Produkt verweist – entweder über Catalogs oder Connected-Content.
3. Bestätigen Sie, dass die Produktdetails in der zugestellten Nachricht korrekt dargestellt werden.
4. Gehen Sie im Braze-Dashboard zur Ergebnisseite der Campaign oder des Canvas und bestätigen Sie, dass der Versand aufgezeichnet wurde.

## Überlegungen {#considerations}

- Halten Sie die Empfehlungsdaten aktuell, indem Sie angepasste Attribute regelmäßig aktualisieren, sobald Ihr Empfehlungssystem neue Ergebnisse liefert.
- Nutzen Sie die [Personalisierungs-Features]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) von Braze, um Nachrichten weiter anzupassen, z. B. durch die Einbindung nutzerspezifischer Daten neben Produktdetails.
- Erwägen Sie die Verwendung von [API-gesteuerter Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery), um Nachrichten über Ihr Backend mithilfe von im Braze-Dashboard definierten Templates zu triggern.