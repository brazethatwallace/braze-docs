---
nav_title: Transformación de datos
article_title: Transformación de datos
page_order: 2
layout: dev_guide
guide_top_header: "Transformación de datos"
guide_top_text: "Transformación de datos de Braze te permite crear y gestionar integraciones de webhook para automatizar el flujo de datos desde plataformas externas a Braze. Estos datos de usuario recién integrados pueden impulsar casos de uso de marketing aún más sofisticados. Transformación de datos de Braze puede agilizar tu integración de datos, aunque tengas muy poca experiencia en codificación, y puede ayudar a sustituir la dependencia de tu equipo de llamadas manuales a API, herramientas de integración de terceros o incluso plataformas de datos de los clientes."
page_type: landing
description: "Esta página de inicio contiene artículos sobre Transformación de datos de Braze, incluyendo cómo crear una transformación de datos y casos de uso."
alias: /data_transformation/

guide_featured_title: "Artículos de sección"
guide_featured_list:
  - name: Crear una transformación
    link: /docs/user_guide/data/unification/data_transformation/creating_a_transformation
    image: /assets/img/braze_icons/flip-forward.svg
  - name: Casos de uso
    link: /docs/user_guide/data/unification/data_transformation/use_cases
    image: /assets/img/braze_icons/users-01.svg
---

## Cómo funciona {#how-it-works}

Muchas plataformas actuales disponen de "webhooks", o notificaciones de API en tiempo real, para enviar información sobre un nuevo evento o nuevos datos de una plataforma a otra. Transformación de datos proporciona:

* Una dirección URL de Braze para recibir dichos webhooks.
* Capacidades para transformar la carga útil del webhook con código JavaScript para crear solicitudes válidas a varios endpoints de la API de Braze, incluidos `/users/track` o `/catalogs` de Braze. Por ejemplo, para el destino `/users/track`, puedes elegir qué información utilizar del webhook y cómo deseas que se representen los datos en los perfiles de usuario de Braze como atributos de usuario, eventos o compras.
* Registro para realizar el control de calidad, solucionar problemas y supervisar el rendimiento de tus transformaciones.

El resultado final es una integración de webhook que conecta una plataforma fuente de tu elección convirtiendo sus webhooks en actualizaciones de Braze.

{% details Más sobre webhooks %}
Los webhooks son notificaciones en tiempo real enviadas a través de una solicitud HTTP POST a un destino específico. Los webhooks se utilizan a menudo para enviar datos de un punto a otro, en el que el webhook puede pasar datos sobre una acción que se ha producido y quién estaba involucrado en esa acción.

Por ejemplo, una plataforma de cuestionarios puede enviar un webhook a un destino de tu elección cada vez que se reciba una respuesta a un formulario en línea. O bien, una plataforma de atención al cliente puede enviar un webhook a un destino de su elección cada vez que se cree un ticket de atención al cliente.
{% enddetails %}

## Niveles de Transformación de datos {#data-transformation-tiers}

La siguiente tabla describe las diferencias entre la versión gratuita y la versión pro de Transformación de datos.

| Área | Versión gratuita | Transformación de datos Pro |
|----|----|----|
| Transformaciones activas | Hasta 5 por empresa | Hasta 55 por empresa |
| Al mes | 300.000 solicitudes entrantes al mes | 10.300.000 solicitudes entrantes al mes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Niveles de Transformación de datos" }

{% alert important %}
Para solicitar una actualización a Transformación de datos Pro, ponte en contacto con tu director de cuentas de Braze o selecciona el botón **Request Upgrade** en el panel de Braze.
{% endalert %}

### Límites de velocidad {#rate-limits}

El límite de velocidad para las Transformaciones de datos de Braze es de 1.000 solicitudes entrantes por minuto y espacio de trabajo. Si tienes Transformación de datos Pro y necesitas un límite de velocidad superior, ponte en contacto con tu director de cuentas de Braze.

## Preguntas más frecuentes {#frequently-asked-questions}

### ¿Qué se sincroniza con Transformación de datos de Braze? {#what-gets-synced-with-braze-data-transformation}

Cualquier dato que la plataforma externa ponga a disposición en un webhook puede sincronizarse con Braze. Cuanto más envíe una plataforma externa a través de webhooks, más opciones habrá para elegir lo que se sincroniza.

### Soy especialista en marketing. ¿Necesito recursos de desarrollador para utilizar Transformación de datos de Braze? {#im-a-marketer-do-i-need-developer-resources-to-use-braze-data-transformation}

Aunque nos encantaría que los desarrolladores también utilizaran esta característica, no es necesario ser uno de ellos para utilizarla. Los especialistas en marketing también pueden configurar transformaciones con éxito sin recursos de desarrollador.

### ¿Puedo seguir utilizando Transformación de datos de Braze si mi plataforma externa solo proporciona una dirección de correo electrónico o un número de teléfono como identificador? {#can-i-still-use-braze-data-transformation-if-my-external-platform-only-gives-an-email-address-or-phone-number-as-an-identifier}

Sí. Puedes hacer que tus transformaciones actualicen el endpoint `/users/track` con la [dirección de correo electrónico o el número de teléfono como identificador]({{site.baseurl}}/api/endpoints/user_data/post_user_track#update-a-user-profile-by-email-address).

Esto funciona utilizando `email` o `phone` como tu propiedad identificadora en el código de transformación en lugar de `external_id` o `braze_id`. El [código de transformación]({{site.baseurl}}/user_guide/data/unification/data_transformation/use_cases#example-transformation-code) de ejemplo utiliza esta funcionalidad.

{% alert note %}
Los usuarios de acceso temprano de Transformación de datos de Braze que empezaron antes de abril de 2023 pueden estar familiarizados con una función `get_user_by_email` que ayudaba con este caso de uso. Esa función ha quedado obsoleta.
{% endalert %}

### ¿Transformación de datos de Braze registra puntos de datos? {#does-braze-data-transformation-log-data-points}

Sí, en la mayoría de los casos. Transformación de datos de Braze crea, finalmente, una llamada a `/users/track` que escribe los atributos, eventos y compras que desees. Estos registrarán puntos de datos del mismo modo que si la llamada a `/users/track` se realizara de forma independiente. Tienes control sobre cuántos puntos de datos se registran en función de cómo escribas tu transformación.

### ¿Cómo puedo obtener ayuda para configurar mi caso de uso o con mi código de transformación? {#how-can-i-get-help-setting-up-my-use-case-or-with-my-transformation-code}

Ponte en contacto con tu director de cuentas de Braze para obtener más ayuda.