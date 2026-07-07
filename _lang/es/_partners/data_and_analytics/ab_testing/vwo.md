---
nav_title: VWO
article_title: Integrar VWO con Braze
description: "Aprende a integrar VWO con Braze."
alias: /partners/vwo/
page_type: partner
search_tag: Partner
---

# VWO

> [VWO](https://vwo.com/) es una potente plataforma de experimentación que ayuda a las marcas a mejorar las métricas empresariales clave, habilitando a los equipos para ejecutar programas de optimización de la conversión respaldados por los datos de comportamiento del cliente. Con VWO, puedes unificar los datos de clientes, obtener información sobre su comportamiento, crear hipótesis, realizar pruebas A/B en múltiples plataformas (servidor, Web y móvil), desplegar características, personalizar experiencias y optimizar todo el recorrido del cliente.

Al integrar VWO con Braze, puedes aprovechar los datos de los experimentos de VWO para crear segmentos específicos y entregar campañas personalizadas.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|-----------------|-------------|
| Cuenta VWO | Una cuenta VWO con acceso a los datos de experimentación. |
| Cuenta Braze | Una cuenta Braze activa con el [SDK Web de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) integrado en tu página web. También necesitarás que se habilite la segmentación de propiedades del evento. Para solicitarlo, consulta [Consideraciones](#request-event-property-segmentation). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integración de VWO con Braze {#integrating-vwo-with-braze}

### Paso 1: Habilitar la integración de Braze en VWO {#step-1-enable-the-braze-integration-in-vwo}

1. Inicia sesión en tu cuenta VWO.
2. En el dashboard de VWO, ve a **Configurations > Integrations**. Aquí puedes habilitar las integraciones a nivel de espacio de trabajo, lo que aplica la integración a todas las campañas de prueba futuras de forma predeterminada.

   ![Configuración de la integración VWO]({% image_buster /assets/img/vwo/vwo1_settings.png %})

4. Selecciona la integración de Braze para habilitarla.
5. Opcionalmente, puedes habilitar la integración de Braze para cualquier campaña existente. Para ello, selecciona una campaña, ve a **Configuration > Integrations** y habilita Braze.

   ![Habilitar la integración de Braze]({% image_buster /assets/img/vwo/vwo2_enable_braze.png %})

6. Una vez habilitada la integración, VWO empezará a enviar datos de experimentos a Braze a nivel de campaña.

### Paso 2: Crear un segmento en Braze con propiedades del evento VWO {#step-2-create-a-segment-in-braze-with-vwo-event-properties}

1. En el dashboard de Braze, selecciona **Segments** > **+ Create Segment**.
3. En la ventana **Create Segment**, introduce un nombre para el segmento y, a continuación, selecciona **Create Segment**.
4. En tu segmento recién creado, selecciona **Filters** > **Add Filter** y, a continuación, elige **Custom Event** como tipo de filtro.
6. En el desplegable de filtros, busca **VWO**.
7. Selecciona la propiedad VWO correspondiente y especifica el valor requerido.
8. Si es necesario, configura el número de visitas y el periodo de tiempo. Cuando hayas terminado, selecciona **Save**.

   ![Creación de segmento en Braze]({% image_buster /assets/img/vwo/vwo3_braze_segment.png %})

9. Para ver el número de usuarios que coinciden con tus criterios de segmentación, selecciona **Calculate Exact Statistics**.

   ![Estadísticas del segmento en Braze]({% image_buster /assets/img/vwo/vwo4_braze_segment_calculate_size.png %})

## Flujo de datos {#data-flow}

VWO envía los datos del experimento de la campaña a Braze como un evento personalizado utilizando el siguiente formato:

- **Nombre del evento:** VWO
- **Propiedades del evento:** `vwo_campaign_name`, `vwo_variation_name`

{% alert tip %}
Estas propiedades del evento personalizado también pueden utilizarse para la segmentación y la orientación.
{% endalert %}

## Consideraciones {#considerations}

### Solicitar segmentación de propiedades del evento {#request-event-property-segmentation}

Antes de poder utilizar la segmentación de propiedades del evento, necesitarás habilitarla en Braze. Utiliza la siguiente plantilla para ponerte en contacto con tu CSM de Braze o con el equipo de soporte para obtener acceso.

   <table aria-label="Solicitar segmentación de propiedades del evento">
     <caption>Solicitar segmentación de propiedades del evento</caption>
   <thead>
      <tr>
         <th>Campo</th>
         <th>Detalles</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Asunto</strong></td>
         <td>Request to Enable Event Property Segmentation for VWO Integration</td>
      </tr>
      <tr>
         <td><strong>Cuerpo</strong></td>
         <td>
         Hello Braze Team,<br><br>
         We would like to enable event property segmentation for events sent from our VWO&lt;&gt;Braze integration. Here are the details:<br><br>
         - <strong>Event Name:</strong> VWO<br>
         - <strong>Event Properties:</strong> <code>vwo_campaign_name</code>, <code>vwo_variation_name</code><br><br>
         Please confirm once the properties have been enabled in our account.<br><br>
         Thank you.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Solicitar segmentación de propiedades del evento" }

### Puntos de datos de Braze {#braze-data-points}

El evento personalizado enviado desde VWO a Braze&#8212;incluidas las propiedades del evento habilitadas para la segmentación&#8212;registrará puntos de datos en tu instancia de Braze.

### Consideraciones adicionales

Actualmente, esta integración no admite la sincronización en tiempo real de los datos de las pruebas. Los datos de la prueba pueden tardar hasta 15 minutos en aparecer en Braze.

## Solución de problemas {#troubleshooting}

Si no ves los datos de VWO en Braze:

1. Haz clic con el botón derecho en la página donde se está ejecutando tu campaña de prueba y selecciona **Inspect Element**.
2. En la pestaña **Network**, busca **Braze** para filtrar las llamadas de red de Braze.
3. Las llamadas de red se rellenan a medida que se carga la página. Puedes recargar la página para ver las llamadas de red.
4. Selecciona una llamada de red para ver más detalles.
5. Ve a la sección **Request Payload** en la pestaña **Payload**, donde encontrarás events: que tiene name: **ce**, lo que indica un evento personalizado.
6. Expande 0: y data: para ver n: "VWO" (nombre del evento personalizado) y p: {vwo_campaign_name: "<your vwo campaign name>", vwo_variation_name: "<variation name>"}. Esto indica que VWO está enviando los valores a Braze.

 ![Solución de problemas de Braze]({% image_buster /assets/img/vwo/vwo5_troubleshooting.png %})

Para obtener ayuda adicional, ponte en contacto con tu administrador del éxito del cliente de VWO.