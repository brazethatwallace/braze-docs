---
nav_title: DailyPlay
article_title: DailyPlay
description: "Aprende a conectar los juegos de marca y las recompensas de DailyPlay con Braze para sincronizar datos de juego, segmentar audiencias y desencadenar campañas personalizadas."
alias: /partners/dailyplay/
page_type: partner
search_tag: Partner
---

# DailyPlay

> [DailyPlay](https://dailyplay.ai/) es una plataforma de gamificación. Úsala para lanzar juegos de marca personalizados y sistemas de recompensas integrados que profundizan la participación y mejoran la retención.

*Esta integración es mantenida por DailyPlay.*

## Acerca de esta integración {#about-this-integration}

La integración de Braze y DailyPlay te permite implementar y hacer seguimiento de juegos y del rendimiento de recompensas en todos los segmentos de audiencia. Los juegos y sistemas de recompensas de DailyPlay funcionan con el motor de orquestación de Braze para que puedas convertir audiencias pasivas en participantes activos.

Puedes enviar hitos de juego, canjes de recompensas y métricas de participación a Braze para crear segmentos de audiencia y desencadenar mensajería multicanal automatizada basada en el comportamiento dentro del juego. Con esta integración, puedes:

- **Enriquecer perfiles de usuario:** Enviar métricas de juego, puntuaciones y estados de recompensas a los perfiles de usuario en Braze.
- **Desbloquear segmentación avanzada:** Crear segmentos de audiencia basados en el comportamiento dentro del juego, como los mejores puntuadores, ganadores recientes o usuarios a punto de desbloquear una recompensa.
- **Automatizar campañas en tiempo real:** Desencadenar mensajes multicanal personalizados (push, correo electrónico, in-app) basados en interacciones de juego para impulsar la repetición de juego, la fidelización de marca y un mayor valor de duración del ciclo de vida.

## Ejemplos {#use-cases}

- **Volver a captar clientes inactivos:** Envía un enlace a un juego con la posibilidad de ganar un descuento como recompensa para clientes inactivos.
- **Actividad en torno a productos y tendencias:** Crea juegos personalizados que destaquen un nuevo producto o una temporada festiva, tendencia o evento.
- **Implementar juegos segmentados:** Combina la segmentación de Braze con la personalización de DailyPlay para crear contenido de juegos atractivo para diferentes objetivos y resultados.
- **Incorporación y activación:** Incorpora un enlace de juego de rasca y gana o revelación instantánea de DailyPlay en tu serie de bienvenida de Braze para incentivar una primera compra o la finalización del perfil.
- **Retención y fidelización:** Cuando un consumidor alcanza un hito de fidelización o realiza una acción clave rastreada en Braze, desencadena un juego personalizado de DailyPlay que celebre su logro y desbloquee recompensas específicas de su nivel.
- **Prevención de cancelación y recuperación:** Identifica a los usuarios que se están alejando en Braze y, a continuación, entrega un juego de DailyPlay de baja fricción para recaptar su atención y llevarlos de vuelta a tu aplicación o sitio.

## Requisitos previos {#prerequisites}


| Requisito | Descripción |
| --- | --- |
| Cuenta de DailyPlay | Se requiere una cuenta de DailyPlay para utilizar esta integración. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos de `users.track`. Crea esta clave en Braze en **Configuración** > **APIs e identificadores** > **Claves de API**. Para más información, consulta [Claves de API]({{site.baseurl}}/api/api_key). |
| Endpoint REST de Braze | La URL del endpoint REST de [tu instancia de Braze]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crear una conexión {#step-1-create-a-connection}

1. En el [panel de DailyPlay](https://app.dailyplay.ai/connections), ve a la página **Connections** y selecciona **Add Connection**.

![Página de conexiones de DailyPlay que muestra las conexiones activas de Braze y las estadísticas de activadores.]({% image_buster /assets/img/dailyplay/connections_page.png %}){: style="max-width:70%;"}

{: start="2"}
2. En **Provider**, elige **Braze**. Introduce un nombre, tu clave de API REST de Braze, el ID de la aplicación y el endpoint REST, y luego selecciona **Create Connection**.

![Modal de agregar conexión en DailyPlay con Braze seleccionado y campos de credenciales para la clave de API, el ID de la aplicación y el endpoint REST.]({% image_buster /assets/img/dailyplay/add_connection.png %}){: style="max-width:60%;"}

### Paso 2: Crear un stream {#step-2-create-a-stream}

Ve a la página **Streams** y crea un nuevo stream.

1. Añade la conexión de Braze que creaste en el paso 1 al nuevo stream.
2. Configura los eventos desencadenadores a rastrear, como **Stream Access**, **Play Start**, **Play Complete** y **Prize Redemption**.
3. Crea y añade juegos al stream.
4. Copia el código de integración de Braze para el stream.

![Modal de gestión de conexiones en DailyPlay que muestra los eventos desencadenadores de Braze y el código de integración para plantillas de correo electrónico de Braze.]({% image_buster /assets/img/dailyplay/manage_connections.png %}){: style="max-width:70%;"}

### Paso 3: Crear una campaign en Braze {#step-3-create-a-campaign-in-braze}

Pega el código del paso 2 en tu campaign en Braze.

Cuando los usuarios juegan a los juegos en el stream, DailyPlay desencadena un evento y lo envía a Braze a través de tu endpoint REST de Braze.

### Paso 4: Inspeccionar acciones y expandir tu embudo {#step-4-inspect-actions-and-expand-your-funnel}

Los usuarios que completan acciones en los streams de DailyPlay reciben atributos personalizados y eventos personalizados en su perfil de Braze.

Crea una [campaign]({{site.baseurl}}/user_guide/messaging/campaigns) o un [Canvas]({{site.baseurl}}/user_guide/messaging/canvas) con un desencadenador [basado en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) que utilice los eventos personalizados o atributos personalizados de DailyPlay necesarios para tu caso de uso.

## Usar DailyPlay con Braze {#use-dailyplay-with-braze}

Para dirigirte a un Segment de clientes específico, sigue estos pasos después de completar la configuración de la integración.

### Paso 1: Configura tu configuración de DailyPlay {#step-1-set-up-your-dailyplay-configuration}

Sigue los pasos de integración en esta sección para configurar tu conexión con Braze y tu flujo de DailyPlay. Copia el código de integración.

### Paso 2: Crea una Campaign o un Canvas en Braze {#step-2-create-a-braze-campaign-or-canvas}

Crea una Campaign o un Canvas utilizando un desencadenador basado en acciones. Selecciona los eventos personalizados o atributos personalizados de DailyPlay que necesites para tu caso de uso.

Puedes usar [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) para hacer referencia a las propiedades que DailyPlay envía en el texto de tu mensaje.

**Ejemplo de atributo personalizado:**

{% raw %}
```liquid
Your score was {{custom_attribute.${dailyplay}.last_game_score}}
```
{% endraw %}

**Ejemplo de evento personalizado:**

Usa la notación de puntos para hacer referencia a las propiedades del evento desencadenador:

{% raw %}
```liquid
{{event_properties.${dailyplay_play_complete}.properties.score}}
```
{% endraw %}

## Solución de problemas {#troubleshooting}

Para obtener orientación adicional sobre la configuración y preguntas frecuentes, consulta la [documentación de integración de DailyPlay con Braze](https://docs.dailyplay.ai/connections/braze/).