# Panel de control de uso de mensajes {#message-usage-dashboard}

> El panel de control de uso de mensajes proporciona información de autoservicio sobre el uso de créditos de SMS, RCS y WhatsApp, lo que permite obtener una visión completa del uso histórico y actual en comparación con las asignaciones del contrato. Esta información puede reducir tu confusión y ayudarte a hacer ajustes para evitar riesgos de excedente.

El panel de **Message Usage** está dividido en tres secciones:
- [Resumen del uso de créditos](#credit-usage-overview)
- [SMS/MMS](#smsmms)
- [WhatsApp](#whatsapp)

Accede al panel yendo a **Settings** > **Billing** > **Message Usage**.

## Resumen del uso de créditos {#credits-usage-overview}

**Credits Usage Overview** proporciona un resumen del uso en todos los canales que utilizan créditos. Puedes ver cómo vas con respecto a tu asignación total de créditos y encontrar detalles sobre tu contrato activo y tu periodo de contrato.

Esta página se muestra si tienes un contrato de créditos. Los canales que utilizan créditos se muestran en **Credits contract overview**.

{% alert note %}
Si has comprado WhatsApp pero no tienes un contrato de créditos, seguirás viendo el consumo de créditos de WhatsApp porque así es como se facturan los contratos de WhatsApp antiguos. Esto difiere de los SMS tradicionales, que solo consumen créditos cuando tienes un contrato de créditos.
{% endalert %}

Los datos de **Credits Usage Overview** se limitan al periodo del contrato, que se muestra en **Credits contract overview**. No puedes filtrar por un intervalo de fechas fuera del **Credits period**.

### Uso de créditos durante el contrato {#credits-usage-over-contract}

El gráfico **Credits Usage over Contract** muestra tu uso durante el periodo de tiempo seleccionado. La granularidad de este gráfico depende del marco temporal que hayas seleccionado. Accede a las opciones de exportación seleccionando el menú en la esquina superior derecha del gráfico.

![Panel de resumen del uso de créditos con secciones para el uso de créditos, resumen del contrato de créditos y consumo de créditos durante el contrato.]({% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %}){: style="max-width:70%;"}

## SMS, MMS y RCS {#sms-mms-and-rcs}

**SMS/MMS/RCS Credits Usage** muestra el desglose del uso de los canales SMS, MMS y RCS. Las columnas de la tabla de datos generalmente requieren que hayas adquirido créditos (aunque Braze sigue admitiendo temporalmente los modelos de facturación anteriores), y las columnas **Credit ratio** y **Credits** indican la tasa del país correspondiente y los créditos consumidos. Además, los mosaicos de alto nivel indicarán el consumo total de SMS y, cuando sea pertinente, de MMS durante el intervalo de fechas seleccionado.

Hay filtros disponibles que te permiten filtrar por **Country** o tipo de SMS y RCS.

![Uso de créditos SMS/MMS/RCS con mosaicos para datos de alto nivel y una sección para el consumo por cuenta.]({% image_buster /assets/img/app_settings/sms_credit_consumption2.png %}){: style="max-width:70%;"}

A diferencia de **Credits Usage Overview**, esta sección contiene datos históricos de periodos contractuales anteriores.

{% alert note %}
Es posible seleccionar un intervalo de fechas que contenga tanto el uso sin créditos como el uso con créditos. En este caso, el consumo que se haya producido fuera de los créditos mostrará `—` (nulo) en las columnas **Credit ratio** y **Credits**.
{% endalert %}

![Tabla de uso de créditos SMS/MMS/RCS con valores nulos.]({% image_buster /assets/img/app_settings/sms_table_null3.png %}){: style="max-width:70%;"}

## WhatsApp {#whatsapp}

**WhatsApp Credits Usage** muestra el desglose de uso del canal WhatsApp. Los mosaicos muestran el uso total de créditos de WhatsApp, que puede desglosarse en la sección **Usage by account** aplicando filtros para limitar los resultados de la tabla de datos a un espacio de trabajo concreto.

### Filtros {#filters}

Puedes filtrar tus datos por:
- País
- Cuenta de WhatsApp Business
- Espacio de trabajo de Braze
- Tipo de categoría de conversación
- Región

![Uso de créditos de WhatsApp con un mosaico para el total de créditos consumidos y una tabla de uso por cuenta.]({% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %}){: style="max-width:70%;"}

## Lo que debes saber {#things-to-know}

{% alert important %}
Los datos que se muestran en el panel de **Message Usage** son a nivel de contrato y no se limitan a una empresa o espacio de trabajo individual del dashboard. Estos datos reflejan el uso de todos los espacios de trabajo de tu dashboard, y potencialmente de todos los dashboards (si tienes varios).
{% endalert %}

- Los datos subyacentes se proporcionan con una cadencia diaria, con las tablas de datos actualizadas a las 3 am, 9 am, 12 pm y 6 pm EST. El panel de **Message Usage** puede tardar más de 24 horas en actualizarse.
- Braze sigue la metodología estándar de redondeo: las cifras se redondean a la décima más próxima.

### Selección del intervalo de fechas {#date-range-selection}

El panel de **Message Usage** excluye la fecha final del intervalo seleccionado de los resultados. Por ejemplo, si seleccionas del 1 al 31 de octubre, se excluyen las estadísticas de uso del 31 de octubre. Para incluir el último día del periodo deseado, amplía el intervalo en un día. Por ejemplo, para incluir todo el mes de octubre, selecciona del 1 de octubre al 1 de noviembre.

### Comparación con proveedores externos {#comparing-with-third-party-providers}

Al comparar los datos de uso de mensajes de Braze con los de proveedores externos (como Infobip), ten en cuenta lo siguiente:

- **Segmentos del mensaje frente a mensajes**: Braze cuenta los mensajes SMS por segmentos. Un único mensaje SMS que se divide en varios segmentos (por ejemplo, debido a su longitud) se cuenta como varios segmentos en Braze. Para obtener más información, consulta [las calculadoras de facturación de SMS y RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/).
- **Mensajes basados en créditos frente a mensajes no basados en créditos**: El panel incluye mensajes basados en créditos y no basados en créditos. Es posible que los proveedores externos solo cuenten los mensajes basados en créditos, lo que puede provocar discrepancias en los totales.
- **De entrada frente a saliente**: Asegúrate de que estás comparando los mismos tipos de mensajes. Algunos dashboards de terceros incluyen tanto los mensajes entrantes como los salientes en sus totales, mientras que Braze te permite filtrar por dirección.
- **Alineación del intervalo de fechas**: Dado que el panel excluye la fecha final, las comparaciones diarias pueden ser más precisas que las comparaciones de intervalos de fechas más largos. Si estás comparando datos de un periodo específico, amplía el intervalo de fechas de Braze un día para incluir el último día del periodo de comparación.