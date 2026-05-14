---
nav_title: Algolia
article_title: Algolia
description: "Aprende a usar Algolia con Contenido conectado de Braze para entregar dinámicamente resultados de búsqueda personalizados y recomendaciones de productos en tus mensajes de Braze."
alias: /partners/algolia/
page_type: partner
search_tag: Partner
---

# Algolia

> [Algolia](https://www.algolia.com/) es una plataforma de búsqueda y descubrimiento que ayuda a los desarrolladores a crear experiencias de búsqueda rápidas, relevantes y escalables. Con un potente enfoque API-first, Algolia combina algoritmos de clasificación avanzados con información impulsada por IA para una búsqueda fluida en el sitio, navegación y descubrimiento de contenido personalizado.

La integración de Algolia y Braze utiliza [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) para rellenar resultados de búsqueda y recomendaciones de productos impulsados por Algolia en tus mensajes de Braze. Al consultar la API de Algolia en el momento del envío, puedes entregar contenido personalizado que dirige a los usuarios a páginas de detalle de producto o páginas de inicio de alta conversión.

## Casos de uso {#use-cases}

- **Promocionar productos en tendencia:** Extrae automáticamente productos en tendencia o de alto rendimiento de Algolia en los mensajes de Braze para promocionar artículos de alto interés y aumentar la interacción.
- **Personalizar campañas con inteligencia de búsqueda:** Personaliza las Campaigns de Braze utilizando la inteligencia de búsqueda y navegación de Algolia para entregar productos o categorías alineados con los intereses de cada usuario.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|-------------|-------------|
| Cuenta de Algolia | Se requiere una cuenta de Algolia para aprovechar esta integración. |
| Credenciales de API de Algolia | Tu clave de API de Algolia y tu ID de aplicación. |
| Índice de productos de Algolia | Un índice de Algolia poblado con los datos de tus productos. Esto es necesario para usar las API de búsqueda o recomendaciones. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración {#integration}

### Paso 1: Configura tu solicitud de API de Algolia {#step-1-set-up-your-algolia-api-request}

Para más información sobre formatos de solicitud, estructuras de respuesta y uso, consulta la documentación de la [API de búsqueda de Algolia](https://www.algolia.com/doc/rest-api/search) y la [API de recomendaciones de Algolia](https://www.algolia.com/doc/rest-api/recommend). Si necesitas ayuda con la configuración, ponte en contacto con el equipo de Algolia.

{% tabs local %}
{% tab Search API %}

#### Ejemplo de solicitud de Search API {#example-search-api-request}

```
POST https://{ALGOLIA_APP_ID}-dsn.algolia.net/1/indexes/{INDEX_NAME}/query
Content-Type: application/json
X-Algolia-API-Key: {ALGOLIA_API_KEY}
X-Algolia-Application-Id: {ALGOLIA_APP_ID}
```

#### Ejemplo de carga útil de consulta {#example-query-payload}

```json
{
  "query": "",
  "hitsPerPage": 4,
  "filters": "category_page_id:'this week's offers'",
  "attributesToRetrieve": ["name", "price", "image", "url"]
}
```

En este ejemplo, la consulta recupera los cuatro primeros resultados de una página que utiliza un filtro de categoría basado en un atributo llamado `category_page_id`. El parámetro `attributesToRetrieve` limita la respuesta para mantener la carga útil en un tamaño manejable.

**Ejemplo de caso de uso:** Para destacar resultados de búsqueda de `https://www.yoursite.com/weekly-offers` en una Campaign de ofertas semanales de Braze, consulta el índice de Algolia correspondiente y aplica filtros para recuperar los mejores resultados de esa página.

{% alert tip %}
Recupera campos adicionales usando `attributesToRetrieve` para mejorar la personalización, como valoraciones, reseñas o descuentos.
{% endalert %}

{% endtab %}
{% tab Recommend API %}

#### Ejemplo de solicitud de Recommend API {#example-recommend-api-request}

```
POST https://{ALGOLIA_APP_ID}.algolia.net/1/indexes/*/recommendations
Content-Type: application/json
X-Algolia-API-Key: {ALGOLIA_API_KEY}
X-Algolia-Application-Id: {ALGOLIA_APP_ID}
```

#### Ejemplo de carga útil de consulta

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

La Recommend API admite múltiples modelos, incluyendo **Frequently Bought Together**, **Related Products**, **Trending Items**, **Trending Facet Values** y **Looking Similar**. Este ejemplo utiliza el modelo **Trending Items**.

{% alert important %}
Si tus recomendaciones dependen de atributos específicos del usuario u objectIDs, ten en cuenta los límites de velocidad definidos en tu contrato de Algolia. Consulta la sección [Consideraciones](#considerations) para conocer las mejores prácticas.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 2: Implementa Contenido conectado de Braze {#step-2-implement-braze-connected-content}

Usa la característica de Contenido conectado de Braze para realizar llamadas a la API de los puntos de conexión de Algolia e inyectar dinámicamente la respuesta en un mensaje. Para más información sobre configuración, formato de solicitudes y mejores prácticas, consulta [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/).

{% tabs local %}
{% tab Search API %}

#### Ejemplo de solicitud de búsqueda con Contenido conectado {#example-connected-content-search-request}

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

#### Ejemplo de solicitud de recomendaciones con Contenido conectado {#example-connected-content-recommend-request}

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

### Paso 3: Da formato a los resultados de búsqueda en los mensajes de Braze {#step-3-format-search-results-in-braze-messages}

Después de obtener los resultados de Algolia, usa Liquid para analizar la respuesta de la API y renderizar dinámicamente los resultados dentro de tu mensaje.

{% tabs local %}
{% tab Search API %}

#### Ejemplo de plantilla Liquid de correo electrónico para Search API {#example-liquid-email-template-for-search-api}

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

Esto genera una lista de productos a partir de los resultados de Search API dentro del cuerpo del mensaje. Cada enlace de producto dirige a los usuarios a una página de detalle de producto (PDP) o a una página de inicio específica de la Campaign.

{% endtab %}
{% tab Recommend API %}

#### Ejemplo de plantilla Liquid de correo electrónico para Recommend API {#example-liquid-email-template-for-recommend-api}

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

Esto genera una lista de productos recomendados a partir de los resultados de Recommend API dentro del cuerpo del mensaje. Cada enlace de producto dirige a los usuarios a una página de detalle de producto (PDP) o a una página de inicio específica de la Campaign.

{% endtab %}
{% endtabs %}

## Consideraciones {#considerations}

### Evitar consultas únicas {#avoiding-unique-queries}

Ten en cuenta los límites de velocidad de Algolia definidos en tu contrato. Evita realizar consultas específicas por usuario, ya que pueden exceder rápidamente tus solicitudes asignadas. Para personalizar los resultados, apunta a un segmento en lugar de un ID de usuario individual, o filtra por categoría o marca en lugar de un objectID específico. Usa atributos de Braze para personalizar aún más las recomendaciones.

### Almacenar en caché los resultados de Contenido conectado {#caching-connected-content-results}

Almacena en caché los resultados de Contenido conectado usando `cache_max_age` para minimizar las solicitudes de API a Algolia y mejorar el rendimiento. Para más información, consulta [Almacenamiento en caché de respuestas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/).