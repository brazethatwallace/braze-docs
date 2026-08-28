---
nav_title: Chord
article_title: Chord
description: "Conecta la plataforma de datos de los clientes (CDP) de Chord a Braze para reenviar eventos de comercio electrónico y actualizaciones de identidad para mensajería, segmentación y journeys."
alias: /partners/chord/
page_type: partner
search_tag: Partner
---

# Chord

> [Chord](https://www.chord.co/) proporciona una plataforma de datos de los clientes que captura y estandariza eventos de tu tienda de comercio electrónico. Cuando conectas Chord a Braze, la actividad de compra, los eventos de comportamiento y las actualizaciones de identidad fluyen hacia Braze para que puedas desencadenar Campaigns y mantener los perfiles actualizados sin tener que construir esas canalizaciones tú mismo.

_Esta integración es mantenida por Chord._

Para más información sobre la configuración, las opciones de conexión y las listas de campos, consulta la [integración de Chord con Braze](https://docs.chord.co/braze#chord-x-braze-integration).

## Acerca de la integración {#about-the-integration}

Chord actúa como la capa de datos entre tu tienda y Braze. Después de conectar Braze como un destino en el CDP de Chord, Chord mapea los eventos de su plan de seguimiento a Braze. Usa esos datos en Segments, Canvas y personalización de mensajes para reflejar lo que tus consumidores están haciendo en tu sitio.

## Requisitos previos {#prerequisites}

Antes de conectar Chord y Braze, confirma que tienes lo siguiente:

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Chord | Se requiere una cuenta de Chord para usar esta integración. |
| Credenciales de API de Braze | Las credenciales que necesitas dependen de tu [modo de conexión](#connection-modes). El modo en la nube usa una clave de API REST de Braze. El modo de dispositivo usa la clave de API del canal Web para el SDK de Braze, que es diferente de tu clave de API REST. |
| Endpoint REST de Braze | Chord envía datos del lado del servidor a los endpoints [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) y [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify). Tu URL base sigue tu instancia de Braze, por ejemplo, `https://rest.iad-01.braze.com`. Para más información, consulta [Endpoints de la REST API de Braze]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Modos de conexión {#connection-modes}

Chord admite el modo en la nube (llamadas de servidor a servidor a través de las REST API de Braze) y el modo de dispositivo (Chord inicializa el SDK Web de Braze y reenvía las llamadas mapeadas). Elige el modo que se ajuste a si necesitas todas las funciones del SDK Web (por ejemplo, mensajes dentro de la aplicación) o solo el reenvío de eventos del lado del servidor.

### Modo en la nube {#cloud-mode}

1. En la plataforma de datos de Chord, abre el CDP y ve a **Destinos**.
2. Selecciona **Añadir** junto a destinos, elige **Braze** del catálogo y, a continuación, introduce un nombre de destino y tu clave de API REST de Braze.
3. Crea el destino para finalizar la conexión.

Crea la clave de API REST en el panel de Braze desde **Configuración** > **Claves de API**. Si utilizas la navegación antigua, ve a **Consola para desarrolladores** > **Configuración de API**. A menos que Chord documente requisitos diferentes para tu espacio de trabajo, la clave necesita los permisos `users.track` y `users.identify`. Para más información, consulta [Claves de API]({{site.baseurl}}/api/api_key).

### Modo de dispositivo {#device-mode}

1. En la plataforma de datos de Chord, abre el CDP y ve a **Destinos**.
2. Selecciona **Añadir** junto a destinos, elige **Braze (device mode)** del catálogo y, a continuación, introduce un nombre de destino y tu clave de API del canal Web.
3. Crea el destino para finalizar la conexión.

Usa la clave de API del canal Web desde **Configuración** > **Configuración de la aplicación** > **Web** > **Clave de API** en el panel de Braze. No uses tu clave de API REST para el modo de dispositivo.

### Configuración del modo de dispositivo {#device-mode-configuration}

En la configuración de destinos de Chord, configura lo siguiente:

- **Versión del SDK Web de Braze:** Chord ofrece versiones seleccionables del SDK en el CDP; confirma el rango disponible en la documentación de Chord.
- **Punto final de SDK:** Debe coincidir con tu instancia de Braze. Para más información, consulta [Endpoints de API y SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints).
- **Opciones de eventos y SDK:** Por ejemplo, qué comportamientos de seguimiento o identificación enviar, manejo de eventos de página, comportamiento de mensajes dentro de la aplicación, temporización de la inicialización del SDK y configuración relacionada con el consentimiento.

## Mapeado de eventos (modo de dispositivo) {#event-mapping-device-mode}

Cuando usas el modo de dispositivo, Chord mapea los eventos a Braze como se muestra en esta tabla:

| Chord | Braze |
| ----- | ----- |
| Pedido completado | `logPurchase` |
| Otros eventos `track` | `logCustomEvent` |
| Identify | Actualizaciones de usuario (por ejemplo, atributos a través del objeto de usuario del SDK) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Solo se reenvían los eventos incluidos en tu plan de seguimiento de Chord y configurados para el destino de Braze.

## Uso de la integración {#using-the-integration}

### Paso 1: Confirma los eventos en Braze {#step-1-confirm-events-in-braze}

Después de que los datos comiencen a fluir, abre los perfiles de usuario o tus herramientas de eventos en Braze para confirmar que los eventos y atributos llegan como esperas.

### Paso 2: Crea audiencias y recorridos {#step-2-build-audiences-and-journeys}

Usa los eventos y atributos sincronizados en [Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) y Campaigns para segmentar a los consumidores en función del comportamiento en tienda.

## Ejemplos {#use-cases}

- **Mensajería posterior a la compra:** Desencadena confirmaciones, ventas cruzadas o solicitudes de reseñas cuando Chord recibe pedidos completados.
- **Enriquecimiento de perfiles:** Mantén los atributos de Braze alineados con los datos más recientes del perfil del consumidor de Chord para una segmentación más precisa.
- **Reorientación por comportamiento:** Vuelve a captar consumidores que no han comprado o convertido recientemente utilizando eventos de comportamiento de Chord.

## Consideraciones {#considerations}

{% alert important %}
Si otra herramienta ya envía los mismos eventos a Braze, coordínate con los responsables de esa integración antes de conectar Braze a través de la CDP de Chord. Ejecutar destinos en paralelo puede crear eventos duplicados en sentido descendente.
{% endalert %}

## Solución de problemas {#troubleshooting}

Si los eventos no aparecen en Braze:

1. En el CDP de Chord, confirma que los eventos en vivo están llegando desde tus fuentes.
2. Verifica que el destino de Braze utiliza la clave de API, la versión del SDK (modo de dispositivo) y el endpoint REST o del SDK correctos para tu instancia.
3. Confirma que el destino está asociado a la fuente esperada en Chord.
4. En Chord, revisa los registros del destino de API o los registros de funciones para verificar llamadas exitosas a `/users/track` y `/users/identify`, y luego comprueba de nuevo en Braze.

Para conocer las ubicaciones de los registros específicos de Chord y los pasos en la interfaz, consulta [Integración de Chord con Braze](https://docs.chord.co/braze#chord-x-braze-integration).