---
nav_title: Algolia
article_title: Algolia
description: "Erfahren Sie, wie Sie Algolia mit Braze Connected-Content nutzen können, um personalisierte Suchergebnisse und Produktempfehlungen dynamisch in Ihren Braze-Nachrichten bereitzustellen."
alias: /partners/algolia/
page_type: partner
search_tag: Partner
---

# Algolia

> [Algolia](https://www.algolia.com/) ist eine Such- und Discovery-Plattform, die Entwickler:innen dabei unterstützt, schnelle, relevante und skalierbare Sucherlebnisse zu erstellen. Mit einem leistungsstarken API-First-Ansatz kombiniert Algolia fortschrittliche Ranking-Algorithmen mit KI or künstliche Intelligenz-gestützten Insights für nahtlose Website-Suche, Navigation und personalisierte Inhaltsentdeckung.

Die Integration von Algolia und Braze nutzt [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), um Algolia-gestützte Suchergebnisse und Produktempfehlungen in Ihren Braze-Nachrichten bereitzustellen. Durch die Abfrage der Algolia-API zum Sendezeitpunkt können Sie personalisierte Inhalte liefern, die Nutzer:innen zu Produktdetail- oder Landing-Pages mit hoher Conversion führen.

## Anwendungsfälle {#use-cases}

- **Trendprodukte bewerben:** Ziehen Sie automatisch trendige oder leistungsstarke Produkte aus Algolia in Braze-Nachrichten, um stark nachgefragte Artikel zu bewerben und das Engagement zu steigern.
- **Campaigns mit Suchintelligenz personalisieren:** Personalisieren Sie Braze Campaigns mithilfe der Such- und Browsing-Intelligenz von Algolia, um Produkte oder Kategorien bereitzustellen, die auf die Interessen der einzelnen Nutzer:innen abgestimmt sind.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|-------------|-------------|
| Algolia-Konto | Ein Algolia-Konto ist erforderlich, um diese Partnerschaft zu nutzen. |
| Algolia-API-Zugangsdaten | Ihr Algolia-API-Schlüssel und Ihre Application-ID. |
| Algolia-Produktindex | Ein Algolia-Index, der mit Ihren Produktdaten befüllt ist. Dies ist erforderlich, um die Search- oder Recommend-APIs zu verwenden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### 1. Schritt: Algolia-API-Anfrage einrichten {#step-1-set-up-your-algolia-api-request}

Weitere Informationen zu Anfrageformaten, Antwortstrukturen und Nutzung finden Sie in der Dokumentation zur [Algolia Search API](https://www.algolia.com/doc/rest-api/search) und [Algolia Recommend API](https://www.algolia.com/doc/rest-api/recommend). Wenn Sie Unterstützung bei der Einrichtung benötigen, kontaktieren Sie das Algolia-Team.

{% tabs local %}
{% tab Search API %}

#### Beispiel einer Search-API-Anfrage {#example-search-api-request}

```
POST https://{ALGOLIA_APP_ID}-dsn.algolia.net/1/indexes/{INDEX_NAME}/query
Content-Type: application/json
X-Algolia-API-Key: {ALGOLIA_API_KEY}
X-Algolia-Application-Id: {ALGOLIA_APP_ID}
```

#### Beispiel eines Abfrage-Payloads {#example-query-payload}

```json
{
  "query": "",
  "hitsPerPage": 4,
  "filters": "category_page_id:'this week's offers'",
  "attributesToRetrieve": ["name", "price", "image", "url"]
}
```

In diesem Beispiel ruft die Abfrage die vier besten Ergebnisse von einer Seite ab, die einen Kategoriefilter basierend auf einem Attribut namens `category_page_id` verwendet. Der Parameter `attributesToRetrieve` begrenzt die Antwort, um den Payload in einer handhabbaren Größe zu halten.

**Beispiel-Anwendungsfall:** Um Suchergebnisse von `https://www.yoursite.com/weekly-offers` in einer wöchentlichen Angebots-Campaign in Braze zu präsentieren, fragen Sie den entsprechenden Algolia-Index ab und wenden Sie Filter an, um die besten Ergebnisse dieser Seite abzurufen.

{% alert tip %}
Rufen Sie zusätzliche Felder über `attributesToRetrieve` ab, um die Personalisierung zu verbessern, z. B. Bewertungen, Rezensionen oder Rabatte.
{% endalert %}

{% endtab %}
{% tab Recommend API %}

#### Beispiel einer Recommend-API-Anfrage {#example-recommend-api-request}

```
POST https://{ALGOLIA_APP_ID}.algolia.net/1/indexes/*/recommendations
Content-Type: application/json
X-Algolia-API-Key: {ALGOLIA_API_KEY}
X-Algolia-Application-Id: {ALGOLIA_APP_ID}
```

#### Beispiel eines Abfrage-Payloads

```json
{
  "requests": [
    {
      "indexName": "prod_ECOM",
      "model": "trending-items",
      "threshold": 40,
      "maxRecommendations": 4
    }
  ]
}
```

Die Recommend API unterstützt mehrere Modelle, darunter **Frequently Bought Together**, **Related Products**, **Trending Items**, **Trending Facet Values** und **Looking Similar**. Dieses Beispiel verwendet das Modell **Trending Items**.

{% alert important %}
Wenn Ihre Empfehlungen auf nutzerspezifischen Attributen oder objectIDs basieren, beachten Sie die in Ihrem Algolia-Vertrag definierten Rate-Limits. Weitere Best Practices finden Sie im Abschnitt [Hinweise](#considerations).
{% endalert %}

{% endtab %}
{% endtabs %}

### 2. Schritt: Braze Connected-Content implementieren {#step-2-implement-braze-connected-content}

Verwenden Sie das Connected-Content-Feature von Braze, um API-Aufrufe an Algolia-Endpunkte zu senden und die Antwort dynamisch in eine Nachricht einzuspeisen. Weitere Informationen zu Konfiguration, Anfrageformatierung und Best Practices finden Sie unter [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/).

{% tabs local %}
{% tab Search API %}

#### Beispiel einer Connected-Content-Suchanfrage {#example-connected-content-search-request}

{% raw %}
```liquid
{% capture request_body %}
{
  "query": "",
  "hitsPerPage": 4,
  "filters": "category_page_id:'this week's offers'",
  "attributesToRetrieve": ["name", "price", "image", "url"]
}
{% endcapture %}

{% connected_content https://{{ALGOLIA_APP_ID}}-dsn.algolia.net/1/indexes/{{INDEX_NAME}}/query
  :method post
  :headers {"X-Algolia-API-Key":"{{ALGOLIA_API_KEY}}", "X-Algolia-Application-Id":"{{ALGOLIA_APP_ID}}", "Content-Type": "application/json"}
  :body {{request_body}}
  :save algolia_search
%}
```
{% endraw %}

{% endtab %}
{% tab Recommend API %}

#### Beispiel einer Connected-Content-Empfehlungsanfrage {#example-connected-content-recommend-request}

{% raw %}
```liquid
{% capture request_body %}
{
  "requests": [
    {
      "indexName": "prod_ECOM",
      "model": "trending-items",
      "threshold": 40,
      "maxRecommendations": 4
    }
  ]
}
{% endcapture %}

{% connected_content https://{{ALGOLIA_APP_ID}}.algolia.net/1/indexes/*/recommendations
  :method post
  :headers {"X-Algolia-Application-Id":"{{ALGOLIA_APP_ID}}", "X-Algolia-API-Key":"{{ALGOLIA_API_KEY}}", "Content-Type": "application/json"}
  :body {{request_body}}
  :save algolia_recommendations
%}
```
{% endraw %}

{% endtab %}
{% endtabs %}

### 3. Schritt: Suchergebnisse in Braze-Nachrichten formatieren {#step-3-format-search-results-in-braze-messages}

Nachdem Sie Ergebnisse von Algolia abgerufen haben, verwenden Sie Liquid, um die API-Antwort zu parsen und die Ergebnisse dynamisch in Ihrer Nachricht darzustellen.

{% tabs local %}
{% tab Search API %}

#### Beispiel eines Liquid-E-Mail-Templates für die Search API {#example-liquid-email-template-for-search-api}

{% raw %}
```liquid
{% for item in algolia_search.hits %}
  <div style="margin-bottom: 10px;">
    <img src="{{ item.image }}" alt="{{ item.name }}" width="100"/>
    <p><strong>{{ item.name }}</strong></p>
    <p>Price: ${{ item.price }}</p>
    <a href="{{ item.url }}">View Product</a>
  </div>
{% endfor %}
```
{% endraw %}

Dies generiert eine Liste von Produkten aus den Search-API-Ergebnissen im Nachrichtentext. Jeder Produktlink leitet Nutzer:innen zu einer Produktdetailseite (PDP) oder einer Campaign-spezifischen Landing-Page weiter.

{% endtab %}
{% tab Recommend API %}

#### Beispiel eines Liquid-E-Mail-Templates für die Recommend API {#example-liquid-email-template-for-recommend-api}

{% raw %}
```liquid
{% for item in algolia_recommendations.hits %}
  <div style="margin-bottom: 10px;">
    <img src="{{ item.image }}" alt="{{ item.name }}" width="100"/>
    <p><strong>{{ item.name }}</strong></p>
    <p>Price: ${{ item.price }}</p>
    <a href="{{ item.url }}">View Product</a>
  </div>
{% endfor %}
```
{% endraw %}

Dies generiert eine Liste empfohlener Produkte aus den Recommend-API-Ergebnissen im Nachrichtentext. Jeder Produktlink leitet Nutzer:innen zu einer Produktdetailseite (PDP) oder einer Campaign-spezifischen Landing-Page weiter.

{% endtab %}
{% endtabs %}

## Hinweise {#considerations}

### Eindeutige Abfragen vermeiden {#avoiding-unique-queries}

Beachten Sie die in Ihrem Vertrag definierten Algolia-Rate-Limits. Vermeiden Sie nutzerspezifische Abfragen, da diese Ihr zugewiesenes Anfragekontingent schnell überschreiten können. Um Ergebnisse zu personalisieren, zielen Sie auf ein Segment statt auf eine einzelne Nutzer-ID ab, oder filtern Sie nach Kategorie oder Marke statt nach einer bestimmten objectID. Verwenden Sie Braze-Attribute, um die Empfehlungen weiter zu personalisieren.

### Connected-Content-Ergebnisse cachen {#caching-connected-content-results}

Cachen Sie Connected-Content-Ergebnisse mit `cache_max_age`, um API-Anfragen an Algolia zu minimieren und die Performance zu verbessern. Weitere Informationen finden Sie unter [Antworten cachen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/).