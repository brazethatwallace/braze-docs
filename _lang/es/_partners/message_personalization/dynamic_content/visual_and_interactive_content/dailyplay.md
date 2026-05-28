---
nav_title: DailyPlay
article_title: DailyPlay
description: "Aprende a conectar los juegos de marca y las recompensas de DailyPlay con Braze para sincronizar datos de juego, segmentar audiencias y desencadenar campañas personalizadas."
alias: /partners/dailyplay/
page_type: partner
search_tag: Partner
---

# DailyPlay

> [DailyPlay](https://dailyplay.ai/) es una plataforma de gamificación. Úsala para lanzar juegos de marca personalizados y sistemas de recompensas integrados que profundizan la interacción y mejoran la retención.

*Esta integración es mantenida por DailyPlay.*

## Acerca de esta integración {#about-this-integration}

La integración de Braze y DailyPlay te permite desplegar y rastrear juegos y el rendimiento de recompensas en distintos segmentos de audiencia. Los juegos y sistemas de recompensas de DailyPlay funcionan con el motor de orquestación de Braze para que puedas convertir audiencias pasivas en participantes activos.

Puedes enviar hitos de juego, canjes de recompensas y métricas de interacción a Braze para crear segmentos de audiencia y desencadenar mensajería automatizada de canales cruzados basada en el comportamiento dentro del juego. Con esta integración, puedes:

- **Enriquecer perfiles de usuario:** Pasar métricas de juego, puntuaciones y estados de recompensas a los perfiles de usuario en Braze.
- **Desbloquear segmentación avanzada:** Crear segmentos de audiencia basados en el comportamiento dentro del juego, como los mejores puntuadores, ganadores recientes o usuarios cerca de desbloquear una recompensa.
- **Automatizar campañas en tiempo real:** Desencadenar mensajes personalizados de canales cruzados (push, correo electrónico, dentro de la aplicación) basados en interacciones de juego para impulsar la repetición de juego, la fidelización de marca y un mayor valor de duración del ciclo de vida.

## Casos de uso {#use-cases}

- **Reactivar clientes inactivos:** Envía un enlace a un juego con la posibilidad de ganar una recompensa de descuento para clientes inactivos.
- **Actividad en torno a productos y tendencias:** Crea juegos personalizados que muestren un nuevo producto o una temporada festiva, tendencia o evento.
- **Desplegar juegos dirigidos:** Combina la segmentación y la orientación de Braze con la personalización de DailyPlay para crear contenido de juego atractivo para diferentes objetivos y resultados.
- **Incorporación y activación:** Inserta un enlace de juego de rasca y gana o revelación instantánea de DailyPlay en tu serie de bienvenida de Braze para incentivar una primera compra o la completación del perfil.
- **Retención y fidelización:** Cuando un consumidor alcanza un hito de fidelización o realiza una acción clave rastreada en Braze, desencadena un juego personalizado de DailyPlay que celebre su logro y desbloquee recompensas específicas de nivel.
- **Prevención de abandono y recuperación:** Identifica a los usuarios que se están alejando en Braze, luego entrega un juego de DailyPlay de baja fricción para recaptar su atención y llevarlos de vuelta a tu aplicación o sitio.

## Requisitos previos {#prerequisites}


| Requisito | Descripción |
| --- | --- |
| Cuenta de DailyPlay | Se requiere una cuenta de DailyPlay para usar esta integración. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos de `users.track`. Crea esta clave en Braze en **Settings** > **APIs and Identifiers** > **API Keys**. Para más información, consulta [Claves de API]({{site.baseurl}}/api/api_key/). |
| Punto de conexión REST de Braze | La URL del punto de conexión REST para [tu instancia de Braze]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integración {#integration}

### Paso 1: Crear una conexión {#step-1-create-a-connection}

1. En el [dashboard de DailyPlay](https://app.dailyplay.ai/connections), ve a la página **Connections** y selecciona **Add Connection**.

![Página de conexiones de DailyPlay que muestra las conexiones activas de Braze y las estadísticas de desencadenadores.]({% image_buster /assets/img/dailyplay/connections_page.png %}){: style="max-width:70%;"}

{: start="2"}
2. En **Provider**, elige **Braze**. Ingresa un nombre, tu clave de API REST de Braze, el ID de la aplicación y el punto de conexión REST, luego selecciona **Create Connection**.

![Modal de agregar conexión de DailyPlay con Braze seleccionado y campos de credenciales para clave de API, ID de aplicación y punto de conexión REST.]({% image_buster /assets/img/dailyplay/add_connection.png %}){: style="max-width:60%;"}

### Paso 2: Crear un stream {#step-2-create-a-stream}

Ve a la página **Streams** y crea un nuevo stream.

1. Agrega la conexión de Braze que creaste en el paso 1 al nuevo stream.
2. Configura los eventos desencadenadores a rastrear, como **Stream Access**, **Play Start**, **Play Complete** y **Prize Redemption**.
3. Crea y agrega juegos al stream.
4. Copia el código de integración de Braze para el stream.

![Modal de administración de conexiones de DailyPlay que muestra los eventos desencadenadores de Braze y el código de inserción para plantillas de correo electrónico de Braze.]({% image_buster /assets/img/dailyplay/manage_connections.png %}){: style="max-width:70%;"}

### Paso 3: Crear una campaña en Braze {#step-3-create-a-campaign-in-braze}

Pega el código del paso 2 en tu campaña en Braze.

Cuando los usuarios juegan en el stream, DailyPlay desencadena un evento y lo envía a Braze a través de tu punto de conexión REST de Braze.

### Paso 4: Inspeccionar acciones y expandir tu embudo {#step-4-inspect-actions-and-expand-your-funnel}

Los usuarios que completan acciones en los streams de DailyPlay reciben atributos personalizados y eventos personalizados en su perfil de Braze.

Crea una [campaña]({{site.baseurl}}/user_guide/messaging/campaigns/) o un [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/) con un desencadenador [basado en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/) que utilice los eventos personalizados o atributos personalizados de DailyPlay requeridos para tu caso de uso.

## Usar DailyPlay con Braze {#use-dailyplay-with-braze}

Para interactuar con un segmento de clientes específico, sigue estos pasos después de completar la configuración de la integración.

### Paso 1: Configurar tu configuración de DailyPlay {#step-1-set-up-your-dailyplay-configuration}

Sigue los pasos de integración anteriores para configurar tu conexión de Braze y el stream de DailyPlay. Copia el código de integración.

### Paso 2: Crear una campaña o Canvas en Braze {#step-2-create-a-braze-campaign-or-canvas}

Crea una campaña o Canvas usando un desencadenador basado en acciones. Selecciona los eventos personalizados o atributos personalizados de DailyPlay requeridos para tu caso de uso.

Puedes usar [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) para hacer referencia a las propiedades que DailyPlay envía en el texto de tu mensaje.

**Ejemplo de atributo personalizado:**

{% raw %}
```liquid
Your score was {{custom_attribute.${dailyplay}.last_game_score}}
```
{% endraw %}

**Ejemplo de evento personalizado:**

Usa la notación de punto para hacer referencia a las propiedades del evento desencadenador:

{% raw %}
```liquid
{{event_properties.${dailyplay_play_complete}.properties.score}}
```
{% endraw %}

## Solución de problemas {#troubleshooting}

Para orientación adicional sobre la configuración y preguntas frecuentes, consulta la [documentación de integración de DailyPlay con Braze](https://docs.dailyplay.ai/connections/braze/).