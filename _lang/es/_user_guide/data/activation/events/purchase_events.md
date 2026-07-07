---
nav_title: Eventos de compra
article_title: Eventos de compra
page_order: 3
page_type: reference
description: "Este artículo de referencia describe los eventos y propiedades de compra, su uso, segmentación, dónde ver los análisis relevantes y más."
search_rank: 3
---

# Eventos de compra {#purchase-events}

> Esta página cubre los eventos y propiedades de compra, su uso, segmentación, dónde ver los análisis relevantes y más.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

Los eventos de compra son acciones de compra realizadas por tus usuarios, y se utilizan para registrar las compras dentro de la aplicación y establecer el valor de duración del ciclo de vida (LTV) para cada perfil de usuario. Estos eventos deben ser configurados por tu equipo. El registro de eventos de compra te permite añadir propiedades como la cantidad y el tipo, lo que te ayuda a segmentar aún más a tus usuarios en función de estas propiedades.

## Registro de eventos de compra {#log-purchase-events}

Puedes registrar las compras pasando un [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object) a través del [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), o utilizando una de nuestras bibliotecas SDK que se enumeran a continuación.

{% alert note %}
Las propiedades de eventos de compra utilizan los mismos tipos de datos que las [propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events#expected-format).
{% endalert %}

A continuación se enumeran los métodos utilizados en diversas plataformas para registrar las compras. En estas páginas también encontrarás documentación sobre cómo añadir propiedades y cantidades a tu evento de compra. Puedes segmentar aún más a tus usuarios en función de estas propiedades.

- [Android y FireOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=unity)
- [.NET MAUI (anteriormente Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=roku)

## Ver datos de compra {#view-purchase-data}

Después de haber configurado y comenzado a registrar eventos de compra, puedes ver estos datos de compra en el perfil de un usuario en la [pestaña Resumen]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#overview-tab).

## Usar datos de compra {#use-purchase-data}

Hay varias formas en las que puedes usar los datos de compra en Braze:

- **[Segmentación](#purchase-event-segmentation):** Usa los datos de compra para crear segmentos de usuarios en función de su comportamiento de compra.
- **[Personalización](#personalization):** Usa los datos de compra para personalizar los mensajes a los usuarios.
- **[Mensajes desencadenados](#trigger-messages):** Configura mensajes que se desencadenen en función de eventos de compra.
- **[Análisis](#analytics):** Analiza tus datos de compra para obtener información sobre el comportamiento de los usuarios y la efectividad de tus campañas de marketing.

### Segmentación {#purchase-event-segmentation}

Puedes desencadenar cualquier número o tipo de campañas de seguimiento en función de los eventos de compra registrados. Por ejemplo, puedes crear un segmento de usuarios que realizaron una compra en los últimos 30 días, o un segmento de usuarios que han gastado más de una cantidad determinada.

Los siguientes filtros de segmentación están disponibles al segmentar usuarios:

- Primera compra realizada
- Primera compra en la aplicación
- Último producto comprado
- Dinero gastado
- Producto comprado
- Número total de compras
- X dinero gastado en Y días
- X producto comprado en Y días
- X propiedad de compra en Y días
- X compras en los últimos Y días

Para más detalles sobre cada filtro, consulta el glosario de [filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) y filtra por "Comportamiento de compra".

![Filtrado de usuarios que realizaron exactamente tres compras]({% image_buster /assets/img/purchase_filter_example.gif %}){: style="max-width:80%;"}

{% alert tip %}
Para segmentar por el número de veces que se ha realizado una compra específica, registra esa compra individualmente como un [atributo personalizado incremental]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview#custom-attribute-storage).
{% endalert %}

### Personalización {#personalization}

Como cualquier otro tipo de datos que recopilas de tus usuarios, puedes usar los datos de compra para personalizar tu mensajería a través de Liquid. Por ejemplo, puedes enviar un correo electrónico personalizado a un usuario recomendando productos similares a los que acaba de comprar.

Supongamos que tienes una propiedad de evento de compra llamada `last_purchased_product` que almacena el nombre del último producto que un usuario compró. Puedes usar esta propiedad para personalizar un mensaje de correo electrónico así:

{% raw %}

```liquid
{% if ${last_purchased_product} == "Running Shoes" %}
  We hope you're enjoying your new running shoes! Based on your recent purchase, you might also like these running shorts and water bottles.
{% elsif ${last_purchased_product} == "Yoga Mat" %}
  We hope you're enjoying your new yoga mat! Based on your recent purchase, you might also like these yoga blocks and straps.
{% else %}
  Thank you for your recent purchase! We hope you're enjoying your new item.
{% endif %}
```

{% endraw %}

En este ejemplo, el mensaje se personaliza en función de la propiedad `last_purchased_product`. Si el último producto que el usuario compró fue "Running Shoes", recibe un mensaje recomendando pantalones cortos para correr y botellas de agua. Si el último producto fue "Yoga Mat", recibe un mensaje recomendando bloques y correas de yoga. Si `last_purchased_product` es cualquier otra cosa, recibe un mensaje genérico de agradecimiento.

### Mensajes desencadenados {#trigger-messages}

Un caso de uso común es enviar automáticamente un mensaje, como un correo electrónico, cuando un usuario realiza una compra. Por ejemplo, puedes enviar un mensaje de agradecimiento o un código de descuento para una compra futura.

Para hacerlo, crea una campaña o Canvas basado en acciones, y luego establece la acción desencadenante como **Realizar compra**. También puedes especificar condiciones adicionales para el desencadenante, como el producto comprado o el monto de la compra.

También puedes personalizar tu mensaje desencadenado con Liquid. En el siguiente ejemplo, `${purchase_product_name}` es un atributo personalizado que reemplazarías con el nombre real del atributo que almacena el nombre del producto comprado en tu configuración de Braze.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

### Análisis {#analytics}

Además de hacer seguimiento de las métricas de compra para segmentación, Braze también registra el número de compras de cada producto y los ingresos generados a lo largo del tiempo. Esto puede ser útil para identificar los productos más populares o medir el impacto de una campaña promocional en las ventas.

Puedes encontrar estos datos en la página del [Informe de ingresos]({{site.baseurl}}/user_guide/analytics/reports/revenue_report#revenue-data).

### Cálculos de ingresos {#revenue-calculations}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Cálculos de ingresos">
  <caption>Cálculos de ingresos</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-revenue">Lifetime Revenue</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-value-per-user">Lifetime Value Per User</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#average-daily-revenue">Average Daily Revenue</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-purchases">Daily Purchases</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-revenue-per-user">Daily Revenue Per User</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

#### Conversión de moneda {#currency-conversion}

Cuando los eventos de compra se registran en una moneda distinta al USD, Braze convierte el monto a USD utilizando tasas de cambio de [Open Exchange Rates](http://openexchangerates.org). Estas tasas se actualizan una vez cada 24 horas. Debido a que las tasas de cambio se almacenan en caché, puede haber ligeras diferencias con la tasa de mercado en tiempo real, particularmente para monedas que experimentan fluctuaciones rápidas.

#### Cálculo de ingresos de por vida {#lifetime-revenue-calculation}

Braze utiliza los eventos de compra para calcular los ingresos de por vida (también llamados valor de duración del ciclo de vida o LTV) de un usuario, que es una predicción de la ganancia neta atribuida a toda la relación futura con un cliente. Esto puede ayudarte a tomar decisiones informadas sobre estrategias de adquisición y retención de clientes.

$$\text{Valor promedio de compra} = \frac{\text{Gasto total en dólares}}{\text{Número total de eventos de compra}}$$

Hay dos lugares principales en Braze donde puedes consultar el LTV de tus usuarios:

- Para métricas generales como *Ingresos de por vida* y el *Valor de por vida por usuario* para cada aplicación y sitio, consulta tu [Informe de ingresos]({{site.baseurl}}/user_guide/analytics/reports/revenue_report#revenue-data).
- Para entender los ingresos de por vida de un usuario específico, consulta su [perfil de usuario]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#overview-tab).

##### Impacto de los reembolsos en los ingresos de por vida {#impact-of-refunds-on-lifetime-revenue}

Cuando usas eventos de compra para hacer seguimiento de los datos de compra, debes registrar los reembolsos como un evento de compra de Braze con una propiedad `price` negativa. Este enfoque mantiene un total preciso para los ingresos de por vida.

Sin embargo, ten en cuenta que el reembolso contará como un evento de compra adicional. Consideremos el siguiente ejemplo. Sam realiza su primera compra por $12 pero devuelve parte de la compra por un reembolso de $5. El perfil de Sam registraría:

- 1 compra con un precio de $12
- 1 compra con un precio de -$5
- Ingresos de por vida de $7

Aunque Sam tendría dos eventos de compra en su perfil, en realidad solo realizó una compra. Esto es importante tenerlo en cuenta si tienes segmentos o casos de uso construidos alrededor del número de compras que un usuario ha realizado. Los reembolsos constantes inflarán el conteo de compras en el perfil del usuario.

## Propiedades de eventos de compra {#purchase-properties}

Con las propiedades de eventos de compra, puedes establecer propiedades en las compras que pueden usarse para calificar aún más las condiciones de desencadenamiento, aumentar la personalización en la mensajería y generar análisis más sofisticados a través de la exportación de datos sin procesar. Los tipos de valores de las propiedades (cadena, numérico, booleano, fecha) varían según la plataforma y frecuentemente se asignan como pares clave-valor.

{% alert warning %}
Las siguientes claves están reservadas y no pueden usarse como nombres de propiedades de eventos de compra: `time`, `product_id`, `quantity`, `event_name`, `price` y `currency`. Usar una clave reservada en el objeto `properties` devolverá el error "Invalid 'properties' field".
{% endalert %}

Por ejemplo, si tienes una aplicación de comercio electrónico y quieres enviar un mensaje a un usuario después de realizar una compra, podrías mejorar adicionalmente tu audiencia objetivo y permitir una mayor personalización de la campaña añadiendo una propiedad de evento de compra de `brand_name`.

**Ejemplo de desencadenamiento basado en propiedades de eventos de compra:**

![Configuración de entrega basada en acciones para enviar una campaña a usuarios que compran auriculares con un nombre de marca igual a HeadphoneMart]({% image_buster /assets/img/purchase2.png %}){: style="max-width:80%;margin-left:15px;"}

Consulta el [objeto de propiedades de compra]({{site.baseurl}}/api/objects_filters/purchase_object#purchase-properties-object) para más información.

### Segmentación por propiedades de eventos {#event-property-segmentation}

La segmentación por propiedades de eventos te permite segmentar usuarios basándote no solo en los eventos personalizados realizados, sino también en las propiedades asociadas con esos eventos. Esto añade opciones de filtrado adicionales al segmentar compras y eventos personalizados.

![Filtros de segmentación para propiedades de eventos de compra, mostrando opciones para filtrar usuarios basándose en valores específicos de propiedades de eventos de compra, como filtrar usuarios que compraron un producto con una propiedad determinada dentro de un período de tiempo establecido.]({% image_buster /assets/img/purchase_event_property.png %}){: style="max-width:80%;margin-left:15px;"}

Estos filtros de segmentación incluyen:
- Ha realizado el evento personalizado con propiedad Y con valor V X veces en los últimos Y días
- Ha realizado cualquier compra con propiedad Y con valor V X veces en los últimos Y días
- Añade segmentación de 1 a 30 días en todas las compras, eventos y propiedades dentro de compras y eventos

A diferencia de las [Extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension), los segmentos utilizados se actualizan en tiempo real, admiten una cantidad ilimitada de segmentos, ofrecen un historial retrospectivo de como máximo 30 días y generan puntos de datos. Debido al cargo adicional de puntos de datos, debes contactar a tu administrador del éxito del cliente de Braze para activar las propiedades de eventos en tus eventos personalizados.

Una vez aprobado, se pueden añadir propiedades adicionales en el dashboard en **Configuración de datos** > **Eventos personalizados** seleccionando **Administrar propiedades**. Luego puedes usar estas propiedades de eventos en el paso de segmentación del constructor de campañas o Canvas.

{% include data_activation/segmentable_purchase_properties_keys_note.md %}

### Propiedades de entrada de Canvas y propiedades de eventos {#canvas-entry-properties-and-event-properties}

{% multi_lang_include canvas/entry_event_properties.md %}

### Registrar compras a nivel de pedido {#log-purchases-at-the-order-level}

Para registrar compras a nivel de pedido en lugar de a nivel de producto, usa el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación del objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object#product-id-naming-conventions) para más información.

### Convenciones de nomenclatura de ID de producto {#product-id-naming-conventions}

En Braze, ofrecemos algunas convenciones generales de nomenclatura para el `product_id` del objeto de compra. Al elegir `product_id`, Braze sugiere usar nombres simples como el nombre del producto o la categoría del producto (en lugar de SKU) con la intención de agrupar todos los elementos registrados por este `product_id`.

Esto hace que los productos sean fáciles de identificar para segmentación y desencadenamiento.

## Bloquear eventos de compra {#blocklist-purchase-events}

Ocasionalmente puedes identificar eventos de compra que registran demasiados puntos de datos, ya no son útiles para tu estrategia de marketing o se registraron por error. Para evitar que estos datos se envíen a Braze, puedes bloquear el objeto de datos personalizado mientras tu equipo de ingeniería trabaja en eliminarlo del backend de tu aplicación o sitio web.

En el dashboard de Braze, puedes administrar el bloqueo desde **Configuración de datos** > **Productos**. Consulta [Administrar datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data) para más información.