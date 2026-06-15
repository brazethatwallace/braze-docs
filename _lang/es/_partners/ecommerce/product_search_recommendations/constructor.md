---
nav_title: Constructor
article_title: Constructor
description: "Este artículo de referencia describe la asociación entre Braze y Constructor. Esta asociación te permite aprovechar el Descubrimiento de productos fuera del sitio de Constructor para generar y entregar dinámicamente recomendaciones personalizadas de productos en mensajes de Braze."
alias: /partners/constructor/
page_type: partner
search_tag: Partner
---

# Constructor

> [Constructor](https://constructor.com/) es una plataforma de búsqueda y descubrimiento de productos que utiliza IA y aprendizaje automático para entregar experiencias personalizadas de búsqueda, recomendación y navegación para sitios web de comercio electrónico y comercio minorista.

Con la integración de Braze y Constructor, puedes utilizar el Descubrimiento de productos fuera del sitio de Constructor para generar y entregar dinámicamente recomendaciones de productos personalizadas en mensajes de Braze.

## Casos de uso {#use-cases}

- **Carrito abandonado y seguimiento posterior al pedido**: genera recomendaciones de productos dinámicas basadas en el comportamiento del usuario y el contenido del carrito para enviar recordatorios personalizados de carritos abandonados o sugerencias posteriores al pedido.
- **Recomendaciones de productos similares para artículos del carrito abandonado**: sugiere productos similares a los artículos que quedaron en el carrito de un usuario para mantener su interacción y ofrecerle alternativas.
- **Recordatorios de artículos vistos recientemente**: notifica a los usuarios sobre artículos que vieron recientemente pero que aún no han comprado, animándolos a completar su compra.
- **Campaigns de promoción**: entrega mensajes promocionales personalizados con recomendaciones de productos seleccionadas y adaptadas a las preferencias del usuario para ventas de temporada u ofertas especiales.
- **Sugerencias de productos visualmente similares**: recomienda artículos visualmente similares a los que un usuario vio recientemente, ayudándolo a descubrir opciones relacionadas que podría preferir.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|-------------|-------------|
| Cuenta de Constructor | Se necesita una cuenta de Constructor con su servicio de Descubrimiento fuera del sitio habilitado para aprovechar esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Trabaja con tu equipo de incorporación de Constructor para completar el proceso de integración. Asegúrate de que los datos de comportamiento de tu sitio web u otros orígenes de datos relevantes estén disponibles para habilitar las recomendaciones de productos personalizadas. Tu equipo de incorporación de Constructor también te ayudará a configurar los fragmentos de código HTML necesarios para su uso en mensajes de Braze.

## URL de la API de Descubrimiento fuera del sitio de Constructor {#constructors-offsite-discovery-api-url}

Puedes utilizar la URL de la API de Descubrimiento fuera del sitio de Constructor para mostrar imágenes de productos y dirigir a los usuarios a la página de detalles del producto correspondiente. A continuación encontrarás un desglose de la estructura del punto de conexión y un ejemplo de cómo utilizarlo:

### Ejemplo {#example}

```html
<a href="https://offsite-discovery.cnstrc.com/v1/product/url?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]" target="_blank">
  <img
    src="https://offsite-discovery.cnstrc.com/v1/product/image?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]"
    width="200"
    border="0"
    alt="Shop Now"
  />
</a>
```

### Parámetros {#parameters}

| Parámetros | Descripción |
|-------------|-------------|
| `position` | Se refiere a la clasificación del artículo recomendado específico dentro de la lista sugerida (por ejemplo, `position = 2`). <br>![Clasificación de la posición del artículo.]({% image_buster /assets/img/constructor/constructor_position.png %}) |
| `ui` | Representa el identificador del usuario, crucial para personalizar los resultados de las recomendaciones. Configura el parámetro `ui` como el `external_id` del cliente en Braze. Si se omite, Constructor devolverá recomendaciones generales en lugar de específicas del usuario. |
| `pod_id` | Identificador del pod que contiene la estrategia y las reglas de búsqueda y merchandising para las recomendaciones (por ejemplo, un pod con una estrategia de más vendidos genera recomendaciones personalizadas de más vendidos). |
| `key` | La clave de índice de Constructor para este cliente. |
| `style_id` | Determina qué imágenes se muestran para la tarjeta de producto. Por ejemplo, diferentes `style_ids` muestran imágenes únicas de tarjetas de producto. |
| `campaign_id` | ID único para la campaña de correo electrónico. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Parámetros" }

### Entradas opcionales {#optional-inputs}

| Entrada | Descripción |
|-------------|-------------|
| `item_id` | Representa el artículo semilla. Necesario para estrategias basadas en artículo-artículo, como alternativas, complementarios y paquetes. Por ejemplo, el primer artículo en un correo electrónico es el artículo semilla, y los artículos siguientes son alternativas. |
| `num_results` | Número de productos que se añadirán al correo electrónico. El valor predeterminado es 10, hasta 100. Por ejemplo, `num_results = 3` significa que se añaden tres recomendaciones. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entradas opcionales" }