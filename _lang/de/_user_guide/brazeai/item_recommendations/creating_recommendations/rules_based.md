---
nav_title: Regelbasierte Empfehlungen
article_title: Regelbasierte Artikelempfehlungen erstellen
description: "Dieser Referenzartikel beschreibt, wie Sie eine regelbasierte Artikelempfehlung für Artikel in einem Katalog erstellen."
page_order: 2
---

# Regelbasierte Artikelempfehlungen erstellen {#create-rules-based-item-recommendations}

> Erfahren Sie, wie Sie ein regelbasiertes Empfehlungssystem aus Artikeln in Ihrem Katalog erstellen.

## Über regelbasierte Artikelempfehlungen {#about-rules-based-item-recommendations}

Ein regelbasiertes Empfehlungssystem verwendet Nutzerdaten und Produktinformationen, um Nutzer:innen relevante Artikel in Nachrichten vorzuschlagen. Es verwendet [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) und entweder Braze-[Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs) oder [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), um Inhalte auf Grundlage von Nutzerverhalten und Attributen dynamisch zu personalisieren.

{% alert important %}
Regelbasierte Empfehlungen basieren auf einer festen Logik, die Sie manuell festlegen müssen. Das bedeutet, dass sich Ihre Empfehlungen nicht an die Kaufhistorie und den Geschmack einer Nutzerin oder eines Nutzers anpassen, sofern Sie die Logik nicht aktualisieren.<br><br>Um personalisierte KI-Empfehlungen zu erstellen, die sich automatisch an den Verlauf von Nutzer:innen anpassen, sehen Sie sich [KI-Artikelempfehlungen]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai) an.
{% endalert %}

## Optionen des Empfehlungssystems {#recommendation-engine-options}

Bei der Entscheidung, welches Empfehlungssystem zu Ihren verfügbaren Ressourcen und Anwendungsfällen passt, orientieren Sie sich an dieser Tabelle:

<table aria-label="Optionen des Empfehlungssystems" style="text-align: center;">
  <caption>Optionen des Empfehlungssystems</caption>
  <thead>
    <tr>
      <th>Empfehlungssystem</th>
      <th>Keine Datenpunkte protokolliert</th>
      <th>No-Code-Lösung</th>
      <th>Kein fortgeschrittenes Liquid</th>
      <th>Aktualisiert automatisch den Produkt-Feed</th>
      <th>Generiert mit der Braze-UI</th>
      <th>Kein Daten-Hosting und keine Fehlerbehebung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Kataloge CSV</strong></td>
      <td>&#10004;</td>
      <td>Ja, wenn Sie vorgeneriertes Liquid verwenden.</td>
      <td>&#10004;</td>
      <td>Ja, wenn die Empfehlungen <strong>nicht</strong> häufig aktualisiert werden.</td>
      <td>&#10004;</td>
      <td>&#10004;</td>
    </tr>
    <tr>
      <td><strong>Kataloge API</strong></td>
      <td>&#10004;</td>
      <td></td>
      <td>&#10004;</td>
      <td>Ja, wenn die Empfehlungen stündlich aktualisiert werden.</td>
      <td>&#10004;</td>
      <td>&#10004;</td>
    </tr>
    <tr>
      <td><strong>Connected-Content</strong></td>
      <td>&#10004;</td>
      <td></td>
      <td></td>
      <td>&#10004;<br>(Empfehlungen werden in Realtime aktualisiert)</td>
      <td>Ja, wenn sie außerhalb von Braze erstellt wurden.</td>
      <td></td>
    </tr>
    <tr>
      <td><strong>Liquid</strong></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>&#10004;</td>
      <td>&#10004;</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="Optionen des Empfehlungssystems" }

## Erstellen eines Empfehlungssystems {#creating-a-recommendation-engine}

Erstellen Sie Ihr Empfehlungssystem entweder mit einem Katalog oder mit Connected-Content:

{% tabs local %}
{% tab using a catalog %}
So erstellen Sie Ihr Empfehlungssystem mithilfe eines Katalogs:

1. [Erstellen Sie einen Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs/create) mit Produkten.
2. Fügen Sie für jedes Produkt eine Liste empfohlener Produkte als String hinzu, der durch ein Trennzeichen (z. B. ein Pipe-Zeichen `|`) getrennt ist, in einer Spalte mit dem Namen „product_recommendations“.
3. Übergeben Sie dem Katalog die Produkt-ID, für die Sie Empfehlungen finden möchten.
4. Rufen Sie den Wert `product_recommendations` für diesen Katalogartikel ab und teilen Sie ihn mit einem Liquid-Split-Filter am Trennzeichen auf.
5. Geben Sie eine oder mehrere dieser IDs an den Katalog zurück, um die weiteren Produktdetails abzurufen.

### Beispiel {#example}

Nehmen wir an, Sie haben eine App für gesunde Ernährung und möchten eine Content-Card-Kampagne erstellen, die verschiedene Rezepte versendet, je nachdem, wie lange Nutzer:innen bereits bei Ihrer App registriert sind. Erstellen Sie zunächst einen Katalog und laden Sie ihn über eine CSV-Datei hoch, die die folgenden Informationen enthält:

| Feld | Beschreibung |
|-----|-----------|
| **id** | Eine eindeutige Zahl, die mit der Anzahl der Tage seit der Registrierung bei Ihrer App korreliert. Zum Beispiel entspricht `3` drei Tagen. |
| **type** | Die Rezeptkategorie, wie `comfort`, `fresh` und andere. |
| **title** | Der Titel der Content-Card, die für jede ID verschickt wird, z. B. „Bereiten Sie diese Woche das Mittagessen vor“ oder „Lassen Sie uns Tacos machen“. |
| **link** | Der Link zum Rezeptartikel. |
| **image_url** | Das Bild, das dem Rezept entspricht. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Beispiel" }

Nachdem der Katalog in Braze hochgeladen wurde, bestätigen Sie die Richtigkeit der importierten Informationen, indem Sie Ihren Katalog auf der Katalogseite auswählen und den Tab **Vorschau** öffnen. Eine ausgewählte Anzahl von Artikeln wird in der Vorschau angezeigt und kann zufällig angeordnet sein, aber das hat keinen Einfluss auf die Ausgabe des Empfehlungssystems.

Erstellen Sie mit dem vorhandenen Katalog eine [Content-Card-Kampagne]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card). Geben Sie im Nachrichten-Editor die Liquid-Logik ein, um zu bestimmen, welche Nutzer:innen die Campaign erhalten sollen und welches Rezept und welches Bild angezeigt werden soll. In diesem Anwendungsfall ruft Braze das `start_date` (oder Registrierungsdatum) der Nutzerin oder des Nutzers ab und vergleicht es mit dem aktuellen Datum. Die Differenz in Tagen bestimmt, welche Content-Card gesendet wird.

{% subtabs local %}
{% subtab title %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].title }}
```
{% endraw %}
{% endsubtab %}

{% subtab message %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{% if items[0].title != blank %}
{{ items[0].body }}
{% else %}
{% abort_message('no card for today') %}
{% endif %}
```
{% endraw %}
{% endsubtab %}

{% subtab image %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].image_url }}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}

Zum Beispiel:

![Ein Beispiel für einen Nachrichten-Editor aus einer Content-Card-Kampagne.]({% image_buster /assets/img/recs/content_card_preview.png %})

Geben Sie im Abschnitt **On click behavior** die Liquid-Logik ein, wohin Nutzer:innen weitergeleitet werden sollen, wenn sie auf iOS-, Android- und Internet-Geräten auf die Content-Card klicken.

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].link }}
```
{% endraw %}

Zum Beispiel:

![Ein Beispiel für einen Klick-Verhaltensblock im Nachrichten-Editor.]({% image_buster /assets/img/recs/on_click_behavior.png %}){: style="max-width:60%;"}<br><br>

Gehen Sie zum Tab **Test** und wählen Sie **Custom user** unter **Preview message as user**. Geben Sie ein Datum in das Feld **Custom attribute** ein, um eine Vorschau der Content-Card zu erhalten, die an Nutzer:innen gesendet wird, die sich an diesem Datum registriert haben. <br><br>

![Ein Beispiel für ein angepasstes Attribut mit dem Namen „start_date“.]({% image_buster /assets/img/recs/custom_attributes_test.png %})
{% endtab %}

{% tab using Connected Content %}
Um Ihr Empfehlungssystem mit Connected-Content zu erstellen, erstellen Sie zunächst einen neuen Endpunkt mit einer der folgenden Methoden:

| Option | Beschreibung |
|------|-----------|
| **Tabellenkalkulation konvertieren** | Konvertieren Sie eine Tabellenkalkulation in einen JSON-API-Endpunkt, indem Sie einen Dienst wie SheetDP verwenden, und notieren Sie sich die API-URL, die dadurch erzeugt wird. |
| **Einen angepassten Endpunkt erstellen** | Erstellen, hosten und pflegen Sie einen speziell entwickelten internen Endpunkt. |
| **Ein Drittanbieter-System verwenden** | Verwenden Sie ein Empfehlungssystem eines Drittanbieters, z. B. eines unserer [Technologie-Partner]({{site.baseurl}}/partners/message_personalization), darunter [Amazon Personalise]({{site.baseurl}}/partners/amazon_personalize), [Certona]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/certona), [Dynamic Yield]({{site.baseurl}}/partners/dynamic_yield) und andere. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Beispiel" }

Verwenden Sie als Nächstes Liquid in Ihrer Nachricht, die Ihren Endpunkt aufruft, um einen angepassten Attributwert mit dem Profil von Nutzer:innen abzugleichen und die entsprechende Empfehlung abzurufen.

{% raw %}
```liquid
{% connected_content YOUR_API_URL :save items %}

{% assign recommended_item_ids_from_user_profile = custom_attribute.${RECOMMENDED_ITEM_IDS} | split: ';' %}

{% for item_id in recommended_item_ids_from_user_profile %}
  {% assign recommended_item = items | where: "ITEM_ID", ITEM_ID | first %}
  recommended_item.item_name
{% endfor %}
```
{% endraw %}

Ersetzen Sie Folgendes:

| Attribut | Ersetzung |
| --- | --- |
| `YOUR_API_URL` | Ersetzen Sie durch die tatsächliche URL Ihrer API. |
| `RECOMMENDED_ITEM_IDS` | Ersetzen Sie durch den tatsächlichen Namen Ihres angepassten Attributs, das die IDs der empfohlenen Artikel enthält. Dieses Attribut wird als eine durch Semikolon getrennte Zeichenkette von IDs erwartet. |
| `ITEM_ID` | Ersetzen Sie durch den tatsächlichen Namen des Attributs in Ihrer API-Antwort, das der Artikel-ID entspricht. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Beispiel" }

{% alert note %}
Dies ist ein einfaches Beispiel, das Sie je nach Ihren spezifischen Anforderungen und Ihrer Datenstruktur möglicherweise weiter anpassen müssen. Ausführlichere Anleitungen finden Sie in der [Liquid-Dokumentation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) oder wenden Sie sich an eine Entwicklerin oder einen Entwickler.
{% endalert %}

### Beispiel

Nehmen wir an, Sie möchten Restaurantempfehlungen aus der Zomato-Restaurants-Datenbank abrufen und das Ergebnis als lokale Variable namens `restaurants` speichern. Sie können den folgenden Connected-Content-Aufruf tätigen:

{% raw %}
```liquid

{% connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

Nehmen wir als Nächstes an, Sie möchten Restaurantempfehlungen auf Grundlage des Orts und der Essensvorlieben von Nutzer:innen abrufen. Sie können dies tun, indem Sie die angepassten Attribute für den Ort und die Essensart dynamisch am Anfang des Aufrufs einfügen und dann den Wert von `restaurants` der Variablen `city_food.restaurants` zuweisen.

Der Connected-Content-Aufruf würde wie folgt aussehen:

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

Wenn Sie die Antwort so anpassen möchten, dass nur der Name und die Bewertung des Restaurants abgerufen werden, können Sie am Ende des Aufrufs Filter hinzufügen, etwa so:

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0].restaurant.name}}
{{city_food.restaurants[0].restaurant.user_rating.rating_text}}
```
{% endraw %}

Nehmen wir abschließend an, Sie möchten die Restaurantempfehlungen nach Bewertung gruppieren. Gehen Sie wie folgt vor:

1. Verwenden Sie `assign`, um leere Arrays für die Bewertungskategorien „Excellent“, „Very Good“ und „Good“ zu erstellen.
2. Fügen Sie eine `for`-Schleife hinzu, die die Bewertung jedes Restaurants in der Liste untersucht.
- Wenn eine Bewertung „Excellent“ lautet, fügen Sie den Restaurantnamen an den String `excellent_restaurants` an und fügen Sie dann am Ende ein *-Zeichen hinzu, um die einzelnen Restaurantnamen voneinander zu trennen.
- Wenn eine Bewertung „Very Good“ lautet, fügen Sie den Restaurantnamen an den String `very_good_restaurants` an und fügen Sie dann am Ende ein *-Zeichen hinzu.
- Wenn eine Bewertung „Good“ lautet, fügen Sie den Restaurantnamen an den String `good_restaurants` an und fügen Sie dann am Ende ein *-Zeichen hinzu.
3. Begrenzen Sie die Anzahl der zurückgegebenen Restaurantempfehlungen auf vier pro Kategorie.

So würde der endgültige Aufruf aussehen:

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}
{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}
{% assign excellent_restaurants = “” %}
{% assign very_good_resturants = “” %}
{% assign good_restaurants = “” %}
{% for list in restaurants %}
{% if {{list.restaurant.user_rating.rating_text}} == `Excellent` %}
{% assign excellent_restaurants = excellent_restaurants | append: list.restaurant.name | append: `*` %}
{% elsif {{list.restaurant.user_rating.rating_text}} == `Very Good` %}
{% assign very_good_restaurants = very_good_restaurants | append: list.restaurant.name | append: `*` %}
{% elsif {{list.restaurant.user_rating.rating_text}} == `Good` %}
{% assign good_restaurants = good_restaurants | append: list.restaurant.name | append: `*` %}
{% endif %}
{% endfor %}
{% assign excellent_array = excellent_restaurants | split: `*` %}
{% assign very_good_array = very_good_restaurants | split: `*` %}
{% assign good_array = good_restaurants | split: `*` %}

Excellent places
{% for list in excellent_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Very good places
{% for list in very_good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Good places
{% for list in good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}
```
{% endraw %}

Im folgenden Screenshot sehen Sie ein Beispiel dafür, wie die Antwort auf dem Gerät von Nutzer:innen angezeigt wird.

![Darstellung einer Restaurantliste, die durch den endgültigen Beispielaufruf generiert wurde.]({% image_buster /assets/img/recs/sample_response.png %}){: style="max-width:30%;"}
{% endtab %}
{% endtabs %}