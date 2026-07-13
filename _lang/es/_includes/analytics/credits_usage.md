# Dashboard de uso de créditos {#credits-usage-dashboard}

> El dashboard de **uso de créditos** proporciona información de autoservicio sobre tu consumo de créditos para una vista integral del uso histórico y actual en comparación con las asignaciones del contrato. Esta información puede reducir tu confusión y ayudarte a realizar ajustes para prevenir riesgos de excedente.

El dashboard de **uso de créditos** se divide en dos secciones:
- [Resumen de uso de créditos](#credits-usage-overview)
- [Pestañas de canales](#credits-features)

Accede al dashboard en **Configuración** > **Facturación** > **Uso de créditos**.

## Resumen de uso de créditos {#credits-usage-overview}

**Message credit usage overview** proporciona un resumen del uso en todos los canales que consumen créditos. Puedes ver cómo avanzas respecto a tu asignación total de créditos y encontrar detalles sobre tu contrato activo y tu período contractual.

Esta página se muestra si tienes un contrato de créditos. Los canales que consumen créditos aparecen en **Credits usage**.

{% alert note %}
Si compraste WhatsApp pero no tienes un contrato de créditos, seguirás viendo el consumo de créditos para WhatsApp porque así se facturan los contratos heredados de WhatsApp. Esto difiere del SMS heredado, que solo consume créditos cuando tienes un contrato de créditos.
{% endalert %}

Los datos generales de uso de créditos están limitados al período del contrato, que se muestra en **Credits contract overview**. No puedes filtrar por un rango de fechas fuera del **Credits period**.


### Uso de créditos durante el contrato {#credits-usage-over-contract}

El gráfico **Message credits usage over contract** muestra tu uso durante el período de tiempo seleccionado. La granularidad de este gráfico depende del marco temporal seleccionado. Consulta las opciones de exportación seleccionando el menú en el menú del gráfico.

![Gráfico de uso de créditos durante el contrato.]({% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %})

## Pestaña de resumen {#overview-tab}

La pestaña **Overview Usage** muestra el uso de créditos en los canales aplicables a tu empresa. Por ejemplo, si no tienes WhatsApp, su pestaña no aparecerá.

### Características de créditos {#credits-features}

Consulta las siguientes pestañas para obtener detalles sobre lo que se muestra para cada característica que consume créditos.

{% tabs %}
{% tab Banners %}

### Banners

**Banners Credits Usage** muestra el uso de créditos de Banners en todas las cuentas. Los mosaicos muestran el total de créditos consumidos y el total de impresiones únicas diarias. La tabla **Usage by account** incluye **Braze workspace**, **Daily unique impressions**, **Credit ratio** y **Credits**. Cuando hay datos disponibles, **Last updated** muestra cuándo se actualizó la tabla.

#### Filtros {#filters}

Puedes filtrar tus datos por:
- Rango de fechas (predeterminado: últimos 30 días)
- Espacio de trabajo de Braze

Usa **Export** para descargar los datos de la tabla.

![Uso de créditos de Banners con mosaicos para créditos e impresiones únicas y una tabla de uso por cuenta.]({% image_buster /assets/img/app_settings/credits_usage_banners.png %})

{% endtab %}
{% tab Content Cards %}

### Content Cards

**Content Cards Credits Usage** muestra el uso de créditos de Content Cards en todas las cuentas. Los mosaicos muestran el total de créditos consumidos y el total de impresiones únicas diarias. La tabla **Usage by account** incluye **Braze workspace**, **Card type**, **Daily Unique Impressions**, **Credit ratio** y **Credits**. Cuando hay datos disponibles, **Last updated** muestra cuándo se actualizó la tabla.

#### Filtros

Puedes filtrar tus datos por:
- Rango de fechas (predeterminado: últimos 30 días)
- Espacio de trabajo de Braze
- Tipo de tarjeta

Usa **Export** para descargar los datos de la tabla.

![Uso de créditos de Content Cards con mosaicos para créditos e impresiones únicas y una tabla de uso por cuenta.]({% image_buster /assets/img/app_settings/credits_usage_content_cards.png %})

{% endtab %}
{% tab Correo electrónico %}

### Correo electrónico {#email}

**Email Credits Usage** muestra el uso de créditos de correo electrónico en todas las cuentas. Los mosaicos muestran el total de créditos consumidos y el total de correos electrónicos enviados. La tabla **Usage by account** incluye **Braze workspace**, **Email sent**, **Credit ratio** y **Credits**. Cuando hay datos disponibles, **Last updated** muestra cuándo se actualizó la tabla.

#### Filtros

Puedes filtrar tus datos por:
- Rango de fechas (predeterminado: últimos 30 días)
- Espacio de trabajo de Braze

Usa **Export** para descargar los datos de la tabla.

![Uso de créditos de correo electrónico con mosaicos para créditos y correos enviados y una tabla de uso por cuenta.]({% image_buster /assets/img/app_settings/credits_usage_email.png %})

{% endtab %}
{% tab KakaoTalk %}

### KakaoTalk

**KakaoTalk Credits Usage** muestra el uso de créditos de KakaoTalk en todas las cuentas. Los mosaicos muestran el total de créditos consumidos y el total de envíos de KakaoTalk. La tabla de la sección **KakaoTalk** incluye **Braze workspace**, **Month**, **Year**, **Company**, **Sends**, **Credit Ratio** y **Credits**. Cuando hay datos disponibles, **Last updated** muestra cuándo se actualizó la tabla.

#### Filtros

Puedes filtrar tus datos por:
- Rango de fechas (predeterminado: últimos 30 días)
- Espacio de trabajo de Braze
- Mes
- Año
- Empresa

Usa **Export** para descargar los datos de la tabla.

![Uso de créditos de KakaoTalk con mosaicos para créditos y envíos de KakaoTalk y una tabla de uso.]({% image_buster /assets/img/app_settings/credits_usage_kakaotalk.png %})

{% endtab %}
{% tab LINE %}

### LINE

**LINE Credits Usage** muestra el uso de créditos de LINE en todas las cuentas. Los mosaicos muestran el total de créditos consumidos y el total de envíos facturables. La tabla de la sección **Line** incluye **Braze workspace**, **Month**, **Year**, **Company**, **Destination**, **Billable sends**, **Credit ratio** y **Credits**. Cuando hay datos disponibles, **Last updated** muestra cuándo se actualizó la tabla.

#### Filtros

Puedes filtrar tus datos por:
- Rango de fechas (predeterminado: últimos 30 días)
- Espacio de trabajo de Braze
- Mes
- Año
- Empresa
- Destino

Usa **Export** para descargar los datos de la tabla.

![Uso de créditos de LINE con mosaicos para créditos y envíos facturables y una tabla de uso detallada.]({% image_buster /assets/img/app_settings/credits_usage_line.png %})

{% endtab %}
{% tab SMS, MMS y RCS %}

### SMS, MMS y RCS {#sms-mms-and-rcs}

**SMS/MMS/RCS Credits Usage** muestra el desglose de uso para el canal de SMS, MMS y RCS. Las columnas **Credit ratio** y **Credits** indican la tasa del país correspondiente y los créditos consumidos. Además, los mosaicos de alto nivel indican el consumo total de SMS y, cuando corresponde, de MMS en el rango de fechas seleccionado.

Hay filtros disponibles que te permiten filtrar por **Country** o tipo de SMS y RCS.

![Uso de créditos de SMS/MMS/RCS con mosaicos para datos de alto nivel y una sección de consumo por cuenta.]({% image_buster /assets/img/app_settings/sms_credit_consumption2.png %})

A diferencia del **resumen de uso de créditos**, esta sección contiene datos históricos de períodos contractuales anteriores.

{% alert note %}
Es posible seleccionar un rango de fechas que contenga tanto uso con créditos como sin créditos. En este caso, el consumo que ocurrió fuera de los créditos mostrará `—` (nulo) en las columnas **Credit ratio** y **Credits**.
{% endalert %}

![Tabla de uso de créditos de SMS/MMS/RCS con valores nulos.]({% image_buster /assets/img/app_settings/sms_table_null3.png %})

{% endtab %}
{% tab Webhooks %}

### Webhooks

**Webhooks Credits Usage** muestra el uso de créditos de webhooks en todas las cuentas. Los mosaicos muestran el total de créditos consumidos y el total de envíos de webhook. La tabla **Usage by account** incluye **Braze workspace**, **Sends**, **Credit ratio** y **Credits**. Cuando hay datos disponibles, **Last updated** muestra cuándo se actualizó la tabla.

#### Filtros

Puedes filtrar tus datos por:
- Rango de fechas (predeterminado: últimos 30 días)
- Espacio de trabajo de Braze

Usa **Export** para descargar los datos de la tabla.

![Uso de créditos de webhooks con mosaicos para créditos y envíos de webhook y una tabla de uso por cuenta.]({% image_buster /assets/img/app_settings/credits_usage_webhooks.png %})

{% endtab %}
{% tab WhatsApp %}

### WhatsApp

**WhatsApp Credits Usage** muestra el desglose de uso para el canal de WhatsApp. Los mosaicos muestran el uso total de créditos de WhatsApp, que se puede desglosar en la sección **Usage by account** aplicando filtros para limitar los resultados de la tabla de datos a un espacio de trabajo específico.

#### Filtros

Puedes filtrar tus datos por:
- País
- Cuenta de WhatsApp Business
- Espacio de trabajo de Braze
- Tipo de categoría de conversación
- Región

![Uso de créditos de WhatsApp con un mosaico para el total de créditos consumidos y una tabla de uso por cuenta.]({% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %})

{% endtab %}
{% tab Ratios de créditos %}

### Ratios de créditos {#credit-ratios}

**Credit Ratios** muestra los ratios de créditos en diferentes canales y destinos. No hay mosaicos de resumen ni control de **Date range** en esta página. La tabla **Credit ratios** incluye **Channel grouping**, **Destination** y **Credit ratio**.

#### Filtros

Puedes filtrar tus datos por:
- Agrupación de canales
- Destino

Usa **Export** para descargar los datos de la tabla.

![Página de ratios de créditos con una tabla de ratios de créditos y filtros de canal y destino.]({% image_buster /assets/img/app_settings/credits_usage_credit_ratios.png %})

{% endtab %}
{% tab Consola de agente %}

### Consola de agente {#agent-console}

**Agent Console Credits Usage** muestra el uso de créditos de la consola de agente en todas las cuentas. Los mosaicos muestran el total de créditos consumidos y el total de invocaciones. La tabla **Usage by account** incluye **Braze workspace**, **Agent name**, **Model owner**, **Total invocations**, **Credit ratio** y **Credits**. Cuando hay datos disponibles, **Last updated** muestra cuándo se actualizó la tabla.

#### Filtros

Puedes filtrar tus datos por:
- Rango de fechas (predeterminado: últimos 30 días)
- Espacio de trabajo de Braze
- Nombre del agente
- Propietario del modelo

Usa **Export** para descargar los datos de la tabla.

![Uso de créditos de la consola de agente con mosaicos para créditos e invocaciones y una tabla de uso por cuenta.]({% image_buster /assets/img/app_settings/credits_usage_agent_console.png %})

{% endtab %}
{% tab Audience Sync %}

### Audience Sync

**Audience Sync Credits Usage** muestra el uso de créditos de Audience Sync en todas las cuentas. Los mosaicos muestran el total de créditos consumidos y el total de sincronizaciones de audiencia. La tabla **Usage by account** incluye **Braze workspace**, **Provider**, **Total syncs**, **Credit ratio** y **Credits**. Cuando hay datos disponibles, **Last updated** muestra cuándo se actualizó la tabla.

#### Filtros

Puedes filtrar tus datos por:
- Rango de fechas (predeterminado: últimos 30 días)
- Espacio de trabajo de Braze
- Proveedor

Usa **Export** para descargar los datos de la tabla.

![Uso de créditos de Audience Sync con mosaicos para créditos y sincronizaciones de audiencia y una tabla de uso por cuenta.]({% image_buster /assets/img/app_settings/credits_usage_audience_sync.png %})

{% endtab %}
{% tab Archivado de mensajes %}

### Archivado de mensajes {#message-archiving}

**Message Archiving Credits Usage** muestra el uso de créditos de archivado de mensajes en todas las cuentas. Los mosaicos muestran el total de créditos consumidos y el total de mensajes archivados. La tabla **Usage by account** incluye **Braze workspace**, **Channel**, **Messages archived**, **Credit ratio** y **Credits**. Cuando hay datos disponibles, **Last updated** muestra cuándo se actualizó la tabla.

#### Filtros

Puedes filtrar tus datos por:
- Rango de fechas (predeterminado: últimos 30 días)
- Espacio de trabajo de Braze
- Canal

Usa **Export** para descargar los datos de la tabla.

![Uso de créditos de archivado de mensajes con mosaicos para créditos y mensajes archivados y una tabla de uso por cuenta.]({% image_buster /assets/img/app_settings/credits_usage_message_archiving.png %})

{% endtab %}
{% endtabs %}

## Cosas que debes saber {#things-to-know}

{% alert important %}
Los datos que se muestran en el dashboard de **uso de créditos** están a nivel de contrato y no están limitados a una empresa o espacio de trabajo individual del panel. Estos datos reflejan el uso de todos los espacios de trabajo dentro de tu panel, y potencialmente de todos los paneles (si tienes varios).
{% endalert %}

- Los datos subyacentes se proporcionan con una cadencia diaria, y las tablas de datos se actualizan a las 3 am, 9 am, 12 pm y 6 pm EST. El dashboard de **uso de créditos** puede tardar más de 24 horas en actualizarse.
- Braze sigue la metodología de redondeo estándar: los números se redondean al décimo más cercano.

### Selección de rango de fechas {#date-range-selection}

El dashboard de **uso de créditos** excluye la fecha final del rango seleccionado de los resultados. Por ejemplo, si seleccionas del 1 al 31 de octubre, las estadísticas de uso del 31 de octubre se excluyen. Para incluir el último día de tu período deseado, extiende el rango un día más. Por ejemplo, para incluir todo octubre, selecciona del 1 de octubre al 1 de noviembre.

### Comparación con proveedores externos {#comparing-with-third-party-providers}

Al comparar los datos de uso de créditos de Braze con proveedores externos (como Infobip), ten en cuenta lo siguiente:

- **Segmentos del mensaje frente a mensajes**: Braze cuenta los mensajes SMS por segmentos. Un solo mensaje SMS que se divide en múltiples segmentos (por ejemplo, debido a su longitud) se cuenta como múltiples segmentos en Braze. Para más información, consulta [Calculadoras de facturación de SMS y RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments).
- **Mensajes basados en créditos frente a no basados en créditos**: El dashboard incluye tanto mensajes basados en créditos como no basados en créditos. Los proveedores externos pueden contar solo los mensajes basados en créditos, lo que puede causar discrepancias en los totales.
- **De entrada frente a de salida**: Asegúrate de que estás comparando los mismos tipos de mensajes. Algunos paneles de proveedores externos incluyen tanto mensajes de entrada como de salida en sus totales, mientras que Braze te permite filtrar por dirección.
- **Alineación del rango de fechas**: Dado que el dashboard excluye la fecha final, las comparaciones día a día pueden alinearse más estrechamente que los rangos de fechas más largos. Si estás comparando datos de un período específico, extiende tu rango de fechas de Braze un día más para incluir el último día de tu período de comparación.