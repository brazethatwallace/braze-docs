---
nav_title: "Atribución de último contacto"
permalink: /last-touch_attribution_metrics/
hidden: true
---

# Métricas de atribución de último contacto {#last-touch-attribution-metrics}

> Añade métricas de atribución de último contacto a tus informes en el Generador de informes.

{% alert note %}
Las métricas de atribución de último contacto están en acceso anticipado. Si te interesa participar en el acceso anticipado, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

La atribución de último contacto (LTA) es un modelo de atribución de conversión que otorga todo el crédito de una conversión al último mensaje con el que un usuario interactuó antes de convertir. A diferencia de las ventanas de conversión a nivel de Campaign, la LTA utiliza ventanas de atribución estándar del sector para cada canal:

| Canal | Ventana de atribución |
| --- | --- |
| Correo electrónico | 30 días |
| SMS | 7 días |
| WhatsApp | 7 días |
| Push | 7 días |
| Mensaje dentro de la aplicación | 3 días |
| Content Cards | 3 días |
| Webhook | excluido de este modelo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Si una conversión ocurre fuera de la ventana de atribución de un canal, no se contabiliza en este modelo.
{% endalert %}

## Beneficios {#benefits}

La atribución de último contacto ofrece ventajas clave sobre el seguimiento de conversiones estándar:

* Te permite atribuir conversiones a puntos de intervención específicos, lo que te da la capacidad de entender qué canales (no solo Campaigns o Canvas) están generando resultados.
* El crédito se otorga exclusivamente al último mensaje con el que se interactuó, por lo que cada conversión se cuenta una sola vez, eliminando conversiones superpuestas entre Campaigns o Canvas con eventos de conversión y audiencias compartidos.

## Añadir métricas de atribución de último contacto a tu informe {#add-last-touch-attribution-metrics-to-your-report}

1. Ve a **Generador de informes**, en **Analytics**.
2. Selecciona **Crear informe** > **Crear informe personalizado**.
3. En el desplegable **Filas**, selecciona sobre qué quieres crear un informe.
4. (Opcional) Selecciona **Añadir desglose** y luego elige un área para profundizar en tus informes.
5. En **Columnas**, selecciona **Personalizar métricas**.
6. En **Conversiones**, selecciona **Last Touch Attribution** y luego selecciona **Seleccionar todo**.

{% alert note %}
Las métricas de ingresos y compras no están disponibles.
{% endalert %}

![El panel Personalizar métricas con las métricas de atribución de último contacto.]({% image_buster /assets/unlisted_docs/img/report_builder_2/lta_report_builder.png %})

{: start="7" }
7. Sigue los pasos 7-9 en la página del [Generador de informes](https://www.braze.com/docs/user_guide/analytics/reporting/report_builder).

{% alert note %}
Envía comentarios a tu administrador del éxito del cliente o proporciónalos después de seleccionar el botón **Enviar comentarios**.
{% endalert %}