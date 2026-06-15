---
nav_title: Crear una fórmula
article_title: Crear una fórmula
page_order: 3
page_type: reference
description: "Este artículo de referencia cubre la creación y gestión de fórmulas, que te ayudan a comprender fácilmente las relaciones complejas que existen en tus datos."
tool: Reports

---
# Crear una fórmula {#create-a-formula}

> Al visualizar los análisis en Braze, puedes combinar varios puntos de datos para obtener información valiosa sobre tus datos de usuario. Esto se conoce como fórmulas. Usa fórmulas para normalizar tus datos de series temporales en función de tu número total de usuarios activos al mes (MAU) y usuarios activos diarios (DAU).

Las fórmulas te ayudan a comprender las relaciones complejas que existen en tus datos. Por ejemplo, puedes comparar cuántos eventos personalizados completaron los usuarios activos diarios que cumplen los requisitos de un segmento concreto frente a la población general (o frente a otro segmento).

## Casos de uso {#use-cases}

Las fórmulas, especialmente cuando se combinan con eventos personalizados, pueden ayudarte a comprender los comportamientos de los usuarios dentro de tu aplicación. Las fórmulas también pueden proporcionar una visión más profunda de los patrones de compra de los segmentos, incluso si tu empresa utiliza medios contratados junto con Braze, como Google Ads o TV.

Los siguientes son algunos ejemplos de los tipos de patrones de comportamiento que pueden detectarse utilizando fórmulas:

- **Aplicaciones de transporte compartido:** Si tienes un evento personalizado para cuando el usuario cancela un viaje, puedes configurar una función para Viajes cancelados / DAU para encontrar si ciertos segmentos de usuarios tienden a cancelar más viajes que otros.
- **Aplicaciones de comercio electrónico:** Al configurar una función para compras de un determinado ID de producto / MAU, puedes comparar la popularidad de un producto promocionado recientemente entre segmentos, incluso si no se han podido rastrear todas las promociones mediante Braze.
- **Aplicaciones multimedia que utilizan anuncios:** Si la experiencia de los usuarios se ve interrumpida por anuncios entre clips de video o audio, registrar las salidas a mitad de anuncio como un evento personalizado y calcular la proporción de salidas a mitad de anuncio / DAU puede ayudar a encontrar los mejores segmentos a los que dirigirse con una Campaign de suscripciones premium sin anuncios.

## Creación de fórmulas {#creating-formulas}

Se puede acceder a las fórmulas en los paneles de estadísticas de las páginas [Inicio]({{site.baseurl}}/user_guide/analytics/dashboards/home/), [Informe de ingresos]({{site.baseurl}}/user_guide/analytics/reports/revenue_report/) e [Informe de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) del dashboard. Para ver este panel, ve al gráfico **Performance Over Time**, cambia el desplegable **Statistics For** a **KPI Formulas** y, a continuación, selecciona al menos una fórmula de KPI para rellenar el gráfico.

![Ver las estadísticas de las fórmulas de KPI en el dashboard de Braze]({% image_buster /assets/img_archive/kpi_forms.png %})

Para crear una nueva fórmula:

1. Ve al dashboard correspondiente (**Home**, **Revenue Report** o **Custom Events Report**).
2. Selecciona **Manage KPI Formulas**.
3. Introduce un nombre para tu fórmula.
4. Selecciona los numeradores y denominadores correspondientes.
5. Selecciona **Save**.

## Numeradores y denominadores disponibles {#available-numerators-and-denominators}

<style>
  div.small_table + table {
    max-width: 50%;
  }
  div.large_table + table {
    max-width: 75%;
  }
table th:nth-child(1),
table th:nth-child(2),
table th:nth-child(3),
table td:nth-child(1),
table td:nth-child(2),
table td:nth-child(3) {
    width:25%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

### Dashboard de resumen {#overview-dashboard}

| Numeradores | Denominadores |
| --- | --- |
| DAU | MAU |
| Sesiones | DAU |
| | Tamaño del segmento |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Overview dashboard" }

### Dashboard de ingresos {#revenue-dashboard}

| Numeradores | Denominadores |
| --- | --- |
| Compras (todas) | DAU |
| Compras específicas (como una tarjeta regalo o un ID de producto) | MAU |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Revenue dashboard" }

### Dashboard de eventos personalizados {#custom-event-dashboard}

| Numeradores | Denominadores |
| --- | --- |
| Recuento de eventos personalizados | MAU |
|  | DAU |
|  | Tamaño del segmento (solo se pueden utilizar los segmentos que tengan habilitado el [seguimiento de análisis]({{site.baseurl}}/viewing_and_understanding_segment_data/)) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom event dashboard" }