---
nav_title: "Cuestionario simple"
article_title: Mensaje dentro de la aplicación de cuestionario simple
page_order: 6
page_type: reference
description: "Este artículo de referencia cubre cómo recopilar atributos de usuario, información y preferencias para impulsar tu estrategia de Campaign utilizando los cuestionarios de mensajes dentro de la aplicación."
channel:
  - in-app messages
tool:
  - Templates
---

# Cuestionario simple {#simple-survey}

> Usa la plantilla de mensaje dentro de la aplicación **Simple Survey** para recopilar atributos de usuario, información y preferencias que impulsen tu estrategia de Campaign.

Este tipo de mensaje está disponible en el [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/).

Los casos de uso comunes de cuestionarios incluyen preguntar a los usuarios cómo les gustaría usar tu aplicación, conocer más sobre sus preferencias personales o preguntar sobre su satisfacción con una característica en particular.

![Tres mensajes de cuestionario simple: preferencias de notificación, preferencias dietéticas y un cuestionario de satisfacción del cliente. Las opciones seleccionadas en los cuestionarios corresponden a atributos personalizados que se registrarán para ese usuario.]({% image_buster /assets/img/iam/iam-survey.png %})

## Requisitos del SDK {#supported-sdk-versions}

Este mensaje dentro de la aplicación solo se entregará a dispositivos que admitan [Flex CSS](https://caniuse.com/flexbox), y debe tener al menos las siguientes [versiones del SDK]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Para habilitar los mensajes dentro de la aplicación HTML a través del SDK Web, debes proporcionar la opción de inicialización `allowUserSuppliedJavascript` a Braze.
{% endalert %}

## Crear un cuestionario {#create}

Al crear un [mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/), selecciona **Simple Survey** para tu **Message Type**.

Esta plantilla de cuestionario es compatible tanto con aplicaciones móviles como con navegadores web. Recuerda verificar que tus SDK estén en las [versiones mínimas del SDK](#supported-sdk-versions) requeridas para esta característica.

### Paso 1: Agrega tu pregunta del cuestionario {#step-1-add-your-survey-question}

Para comenzar a construir tu cuestionario, agrega tu pregunta en el campo **Header** del cuestionario. Si lo deseas, puedes agregar un mensaje opcional de **Body** que aparecerá debajo de tu pregunta del cuestionario.

![Pestaña Redactar del editor de cuestionario simple, con campos para un encabezado, cuerpo opcional y texto de ayuda opcional.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:90%"}

{% alert tip %}
¡Estos campos pueden incluir tanto Liquid como emojis, así que sé creativo!
{% endalert %}

### Paso 2: Configura las opciones {#single-multiple-choice}

Puedes agregar hasta 12 opciones en un cuestionario.

Selecciona **Single-choice selection** o **Multiple-choice selection**. El **Helper text** se actualizará automáticamente cuando cambies entre las dos opciones para informar a los usuarios cuántas opciones pueden seleccionar.

Luego, determina si vas a [recopilar atributos personalizados](#custom-attributes) o [registrar solo las respuestas](#no-attributes).

![Menú desplegable de opciones con "Log attributes upon submission" seleccionado.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### Recopilar atributos personalizados {#custom-attributes}

Selecciona **Log attributes upon submission** para recopilar atributos basados en la respuesta del usuario. Puedes usar esta opción para crear nuevos segmentos y Campaigns de reorientación. Por ejemplo, en un [cuestionario de satisfacción](#user-satisfaction), podrías enviar un correo electrónico de seguimiento a todos los usuarios que no estaban contentos.

Para agregar un atributo personalizado a cada opción, selecciona un nombre de atributo personalizado del menú desplegable (o crea uno nuevo), y luego ingresa el valor que se establecerá cuando se envíe esta opción. También puedes crear un nuevo atributo personalizado en tu [página de configuración]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/).

El tipo de datos de tus atributos personalizados importa dependiendo de cómo hayas configurado tu cuestionario.

- **Selección de opción múltiple:** El tipo de datos del atributo personalizado debe ser un array. Si el atributo personalizado está configurado con un tipo de datos diferente, las respuestas no se registrarán.
- **Selección de opción única:** El tipo de datos del atributo personalizado debe ser una cadena. Los atributos personalizados que no sean de tipo cadena no aparecerán en el menú desplegable, y las respuestas no se registrarán.

{% alert important %}
Cuando la recopilación de atributos personalizados está habilitada, las opciones que comparten el mismo nombre de atributo personalizado se combinarán en un array.
{% endalert %}

##### Ejemplo {#example}

Por ejemplo, en un [cuestionario de preferencias de notificación](#notification-preferences), podrías hacer que cada opción sea un atributo booleano (verdadero/falso) para permitir que los usuarios seleccionen los temas que les interesan. Si un usuario marca la opción "Promociones", eso actualizará su [perfil de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/) con el atributo personalizado `Promotions Topic` establecido en `true`. Si deja la opción sin marcar, ese mismo atributo permanecerá sin cambios.

Luego puedes usar el filtro `Custom Attribute` para crear un segmento de usuarios con el atributo personalizado `Promotions Topic` `is` `true` para asegurarte de que solo los usuarios interesados en tus promociones reciban las Campaigns relevantes.

#### Registrar solo las respuestas {#no-attributes}

Alternativamente, puedes elegir **Log responses only (no attributes)**. Cuando se selecciona esta opción, las respuestas del cuestionario se registran como clics de botón, pero los atributos personalizados no se registran en el perfil del usuario. Esto significa que aún puedes ver las métricas de clics para cada opción del cuestionario (consulta [Análisis](#analytics)), pero esa opción no se reflejará en su perfil de usuario.

Estas métricas de clics no están disponibles para reorientación.

### Paso 4: Elige el comportamiento de envío {#step-4-choose-submission-behavior}

Una vez que un usuario envía su respuesta, puedes opcionalmente mostrar una página de confirmación o simplemente cerrar el mensaje.

Una página de confirmación es un excelente lugar para agradecer a los usuarios por su tiempo o proporcionar información adicional. Puedes personalizar la llamada a la acción en esta página para guiar a los usuarios a otra página de tu aplicación o sitio web.

Edita el texto de tu botón y el comportamiento al hacer clic en la sección **Submit Button** en la parte inferior de la pestaña **Survey**:

![Comportamiento al hacer clic configurado como "Submit responses and display confirmation page".]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Si decides agregar una página de confirmación, cambia a la pestaña **Confirmation Page** para personalizar tu mensaje:

![Pestaña Confirmation Page del editor de cuestionario simple. Los campos disponibles son encabezado, cuerpo opcional, texto del botón y comportamiento del botón al hacer clic.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:90%"}

Si deseas guiar a los usuarios a otra página de tu aplicación o sitio web, cambia el **comportamiento al hacer clic** del botón.

### Paso 5: Estiliza tu mensaje (opcional) {#styling}

Puedes personalizar el color de la fuente y el color de acento del mensaje usando el selector de **Color Theme**.

![Pestaña Redactar del editor de cuestionario simple con el selector de Color Theme expandido después de que un usuario ha hecho clic en la paleta de colores.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analizar resultados {#analytics}

Una vez que tu Campaign se haya lanzado, puedes analizar los resultados en tiempo real para ver el desglose de cada opción seleccionada. Si has habilitado la [recopilación de atributos personalizados](#custom-attributes), también podrás crear nuevos segmentos o Campaigns de seguimiento para los usuarios que hayan enviado el cuestionario.

{% alert note %}
Las opciones de cuestionario eliminadas seguirán apareciendo en los análisis, pero no se mostrarán como opción para nuevos usuarios.
{% endalert %}

Puedes encontrar las métricas de rendimiento de tu cuestionario expandiendo el menú desplegable **Results** para una variante específica en la sección **In-App Message Performance** de los análisis. Aquí tienes un desglose de lo que verás:

- **Interacción con el cuestionario** muestra cómo los usuarios interactuaron con el cuestionario en general, incluyendo envíos totales, descartes y clics dentro del cuerpo del mensaje.
- **Resultados del cuestionario** muestran un desglose de cuántos usuarios seleccionaron cada opción de respuesta, junto con el porcentaje del total de envíos que representa cada opción.
- **Métricas de la página de confirmación** (si está habilitada) incluyen cuántos usuarios vieron la pantalla de confirmación, hicieron clic en su botón o la descartaron sin interactuar.

Para las definiciones de las métricas del cuestionario, consulta el [Glosario de métricas de informe]({{site.baseurl}}/user_guide/analytics/metrics_glossary/) y filtra por "In-App Message".

Consulta [Informes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting/) para un desglose de las métricas de tu Campaign.

### Currents {#currents}

Las opciones seleccionadas fluirán automáticamente a Currents, bajo el campo `button_id` de [**In-App Message Click Events**]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe). Cada opción se enviará con su identificador único universal (UUID).

## Casos de uso {#use-cases}

{% tabs %}
{% tab Satisfacción del usuario %}

### Satisfacción del usuario {#user-satisfaction}

**Objetivo:** Medir la satisfacción del cliente y enviar Campaigns de recuperación a los usuarios que dejaron puntuaciones bajas.

Para configurar esto, usa un cuestionario de selección de opción única con cinco opciones que van desde "😡 Muy insatisfecho" hasta "😍 Muy satisfecho". Cada opción está mapeada al atributo personalizado `customer_satisfaction`, con un valor numérico del 1 al 5, donde 1 indica el menos satisfecho y 5 el más satisfecho. Ten en cuenta que estos valores numéricos se almacenan como cadenas, ya que los atributos personalizados de tipo cadena son obligatorios para la selección de opción única.

| Opción | Atributo | Valor |
|---------------------------------------|------------------------|-------|
| 😡 Muy insatisfecho | `customer_satisfaction` | 1 |
| 😟 Insatisfecho | `customer_satisfaction` | 2 |
| 🙂 Ni satisfecho ni insatisfecho | `customer_satisfaction` | 3 |
| 😊 Satisfecho | `customer_satisfaction` | 4 |
| 😍 Muy satisfecho | `customer_satisfaction` | 5 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="User satisfaction" }

Cuando un usuario envía el cuestionario, su valor seleccionado se registra como un atributo personalizado. Luego puedes crear Campaigns de seguimiento usando filtros de audiencia. Por ejemplo, dirige mensajes de recuperación a los usuarios cuyo atributo `customer_satisfaction` sea "1" o "2".

{% endtab %}
{% tab Preferencias de notificación %}

### Preferencias de notificación {#notification-preferences}

**Objetivo:** Permitir que los usuarios opten por tipos específicos de notificaciones.

Para configurar esto, usa un cuestionario de selección de opción múltiple donde cada opción representa un tema de notificación. En lugar de asignar el mismo atributo con diferentes valores, cada opción se mapea a un atributo booleano distinto que refleja el interés del usuario en ese tema. Si un usuario selecciona una opción, el atributo correspondiente se establece en `true`. Si se deja sin seleccionar, el atributo permanece sin cambios.

| Opción | Atributo | Valor |
|--------------------|------------------------|--------|
| Actualizaciones de producto | `wants_product_updates`| `true` |
| Promociones | `wants_promotions` | `true` |
| Invitaciones a eventos | `wants_event_invites` | `true` |
| Cuestionarios y comentarios | `wants_surveys` | `true` |
| Consejos y tutoriales | `wants_tips` | `true` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Notification preferences" }

{% endtab %}
{% tab Identificar objetivos del cliente %}

### Identificar objetivos del cliente {#identify-customer-goals}

**Objetivo:** Identificar las principales razones por las que los usuarios visitan tu aplicación.

Para configurar esto, usa un cuestionario de selección de opción única con cada opción representando un objetivo o intención común. Cada opción está mapeada al atributo personalizado `product_goal` con un valor correspondiente a la intención del usuario seleccionada.

| Opción | Atributo | Valor |
|----------------------------|------------------|-----------|
| Verificar estado | `product_goal` | `status` |
| Actualizar mi cuenta | `product_goal` | `upgrade` |
| Programar una cita | `product_goal` | `schedule`|
| Soporte al cliente | `product_goal` | `support` |
| Solo explorando | `product_goal` | `browse` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Identify customer goals" }

Cuando un usuario envía el cuestionario, el valor seleccionado se registra como un atributo personalizado en su perfil. Luego puedes usar estos datos para personalizar experiencias futuras o segmentar usuarios según su objetivo principal.

{% endtab %}
{% tab Mejorar tasas de conversión %}

### Mejorar tasas de conversión {#improve-conversion-rates}

**Objetivo:** Entender por qué los clientes no están actualizando o comprando.

Para configurar esto, usa un cuestionario de selección de opción única con cada opción representando una barrera común para la actualización. Cada opción está mapeada al atributo personalizado `upgrade_reason` con un valor correspondiente que refleja la selección del usuario.

| Opción | Atributo | Valor |
|---------------------|------------------|-------------|
| Demasiado caro | `upgrade_reason` | `expensive` |
| No es valioso | `upgrade_reason` | `value` |
| Difícil de usar | `upgrade_reason` | `difficult` |
| Uso un competidor | `upgrade_reason` | `competitor`|
| Otra razón | `upgrade_reason` | `other` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Improve conversion rates" }

Cuando un usuario envía el cuestionario, el valor seleccionado se guarda en su perfil. Luego puedes dirigirte a estos usuarios con Campaigns adaptadas a su objeción específica, como ofertas de descuento o mejoras de usabilidad.

{% endtab %}
{% tab Características favoritas %}

### Características favoritas {#favorite-features}

**Objetivo:** Entender qué características disfrutan usar los clientes.

Para configurar esto, usa un cuestionario de selección de opción múltiple donde cada opción representa una característica de tu aplicación. Cada opción está mapeada al atributo personalizado `favorite_features`, y cuando el usuario envía el cuestionario, el atributo se establece como un array de los valores seleccionados.

| Opción | Atributo | Valor |
|-------------------|--------------------|--------------|
| Marcadores | `favorite_features`| `bookmarks` |
| Aplicación móvil | `favorite_features`| `mobile` |
| Compartir publicaciones | `favorite_features`| `sharing` |
| Soporte al cliente | `favorite_features`| `support` |
| Personalización | `favorite_features`| `custom` |
| Precio / Valor | `favorite_features`| `value` |
| Comunidad | `favorite_features`| `community` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Favorite features" }

Dado que este cuestionario usa selección de opción múltiple, el perfil del usuario se actualizará con una lista de todos los valores de características seleccionados.

{% endtab %}
{% endtabs %}