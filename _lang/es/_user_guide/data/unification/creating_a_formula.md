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

## Ejemplos {#use-cases}

Las fórmulas, especialmente cuando se combinan con eventos personalizados, pueden ayudarte a comprender los comportamientos de los usuarios dentro de tu aplicación. Las fórmulas también pueden ofrecer información más profunda sobre los patrones de compra de los Segments, incluso si tu empresa utiliza medios contratados junto con Braze, como Google Ads o televisión.

Los siguientes son algunos ejemplos de los tipos de patrones de comportamiento que se pueden detectar usando fórmulas:

- **Aplicaciones de transporte compartido:** Si tienes un evento personalizado para cuando el usuario cancela un viaje, puedes configurar una función de Viajes cancelados / usuarios activos diarios para averiguar si ciertos Segments de usuarios tienden a cancelar más viajes que otros.
- **Aplicaciones de comercio electrónico:** Al configurar una función de compras de un ID de producto determinado / MAU, puedes comparar la popularidad de un producto promocionado recientemente entre Segments, incluso si todas las promociones no pudieron rastrearse usando Braze.
- **Aplicaciones de medios que usan anuncios:** Si la experiencia de los usuarios se interrumpe con anuncios entre clips de video o audio, registrar las salidas a mitad de anuncio como un evento personalizado y calcular la proporción de salidas a mitad de anuncio / usuarios activos diarios puede ayudar a encontrar los mejores Segments a los que dirigir una Campaign de suscripciones premium sin anuncios.

## Creación de fórmulas {#creating-formulas}

Se puede acceder a las fórmulas en las páginas [Inicio]({{site.baseurl}}/user_guide/analytics/dashboards/home), [Informe de ingresos]({{site.baseurl}}/user_guide/analytics/reports/revenue_report) e [Informe de eventos personalizados]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) del panel. En **Inicio** e **Informe de ingresos**, abre el gráfico **Rendimiento a lo largo del tiempo**, establece **Estadísticas para** en **Fórmulas de KPI** y selecciona al menos una fórmula. En la página **Informe de eventos personalizados**, abre **Filtros**, selecciona una o más opciones de **Fórmula de KPI** y selecciona **Aplicar**.

![Ver estadísticas de fórmulas de KPI en el panel de Braze]({% image_buster /assets/img_archive/kpi_forms.png %})

Para crear una nueva fórmula:

1. Ve al panel correspondiente (**Inicio**, **Informe de ingresos** o **Informe de eventos personalizados**).
2. Selecciona **Administrar fórmulas de KPI**.
3. Introduce un nombre para tu fórmula.
4. Selecciona los numeradores y denominadores relevantes.
5. Selecciona **Guardar**.

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

### Panel de resumen {#overview-dashboard}

| Numeradores | Denominadores |
| --- | --- |
| DAU | MAU |
| Sesiones | DAU |
| | Tamaño del Segment |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Panel de resumen" }

### Panel de ingresos {#revenue-dashboard}

| Numeradores | Denominadores |
| --- | --- |
| Compras (todas) | DAU |
| Compras seleccionadas (como una tarjeta de regalo o un ID de producto) | MAU |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Panel de ingresos" }

### Panel de eventos personalizados {#custom-event-dashboard}

| Numeradores | Denominadores |
| --- | --- |
| Recuento de eventos personalizados | MAU |
|  | DAU |
|  | Tamaño del Segment (solo se pueden usar Segments que tengan habilitado el [seguimiento de análisis]({{site.baseurl}}/viewing_and_understanding_segment_data)) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Panel de eventos personalizados" }