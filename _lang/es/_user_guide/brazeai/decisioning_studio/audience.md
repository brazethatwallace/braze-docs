---
nav_title: Define tu audiencia
article_title: Define tu audiencia
page_order: 3
page_type: reference
description: "Aprende a definir y configurar la audiencia para tu agente de BrazeAI Decisioning Studio, incluidos los grupos de tratamiento y los pasos de configuración específicos de cada plataforma."
---

# Define tu audiencia {#define-your-audience}

> Las audiencias de los casos de uso se definen normalmente en una plataforma de interacción con los clientes (como Braze o Salesforce Marketing Cloud) y luego se envían al agente de Decisioning Studio. A continuación, el agente divide a los clientes en grupos de tratamiento para realizar ensayos controlados aleatorizados.

## Grupos de tratamiento {#treatment-groups}

| Grupo | Descripción |
|-------|-------------|
| **Decisioning Studio** | Clientes que reciben recomendaciones optimizadas por IA |
| **Control aleatorio** | Clientes que reciben opciones seleccionadas aleatoriamente (comparación de referencia) |
| **Business-as-Usual (opcional)** | Clientes que reciben el recorrido de marketing actual (para comparar con el rendimiento existente) |
| **Holdout (opcional)** | Clientes que no reciben comunicaciones (para medir el impacto general de la campaña) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Grupos de tratamiento" }

## Configura tu audiencia {#configure-your-audience}

{% tabs %}
{% tab Braze %}

1. Crea un segmento para la audiencia a la que deseas dirigirte.
2. Proporciona el ID del segmento a tu equipo de AI Decisioning Services.

{% alert note %}
Para Braze, podemos ingerir múltiples segmentos y combinarlos para crear la audiencia. Decisioning Studio puede ingerir un segmento para una campaña comparativa de Business-as-Usual. Todos estos patrones son aceptables.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

1. Configura una extensión de datos (Data Extension) de SFMC para tu audiencia y proporciona el ID de la extensión de datos.
2. Configura un paquete instalado (Installed Package) de SFMC para la integración de API con los permisos apropiados requeridos por Decisioning Studio.
3. Confirma que esta extensión de datos se actualiza diariamente, ya que Decisioning Studio extrae los datos incrementales más recientes disponibles.

Proporciona el ID de la extensión y la clave de API a nuestro equipo de AI Decisioning Services, que te asistirá con los próximos pasos para la ingesta de datos de clientes.

{% endtab %}
{% tab Otras plataformas %}

### Google Cloud Storage

Si la audiencia no está almacenada actualmente en Braze o Salesforce Marketing Cloud, el siguiente mejor paso es configurar una exportación automatizada directamente a un contenedor de Google Cloud Storage (GCS) controlado por Braze.

Para determinar si esto es factible, consulta la documentación de tu plataforma. Por ejemplo, mParticle ofrece una [integración nativa con Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/). Si este es el caso, podemos proporcionar un contenedor de GCS para exportar los datos de audiencia.

### Recursos adicionales {#additional-resources}

- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## Próximos pasos {#next-steps}

Después de definir tu audiencia, procede a configurar la orquestación:

- [Configurar la orquestación]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/orchestration_setup)