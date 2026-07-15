---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre la sincronización de audiencias
alias: /partners/audience_sync_faq/
description: "Este artículo ofrece respuestas a las preguntas más frecuentes sobre la sincronización de audiencias."
page_order: 80
tool:
  - Canvas

---

# Preguntas frecuentes {#frequently-asked-questions}

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre la sincronización de audiencias.

## ¿Cuánto tardan mis audiencias en aparecer en mi panel de partners de Audience Sync? {#how-long-does-it-take-for-my-audiences-to-populate-in-my-audience-sync-partner-dashboard}

El tiempo que se tarda en poblar una audiencia depende del partner concreto. Todas las redes procesarán las solicitudes de Braze e intentarán emparejar a los usuarios. Este proceso suele durar entre 6 y 48 horas.

Puedes consultar el intervalo de tiempo específico en la sección de solución de problemas de la documentación de cada partner de Audience Sync.

## ¿Qué tipo de datos propios puedo utilizar en mi Audience Sync? {#what-type-of-first-party-data-can-i-use-in-my-audience-sync}

Los campos específicos utilizados para cada partner pueden variar en función de los requisitos del partner.

Por ejemplo, cuando configuras una sincronización de audiencia con Facebook, puedes utilizar una amplia variedad de campos de datos propios, como correo electrónico, teléfono, nombre y apellidos, mientras que, con Snapchat, solo puedes seleccionar correo electrónico, teléfono o ID de anunciante móvil.

Es importante tener en cuenta que los campos de usuario que puedes seleccionar para sincronizar se correlacionan con los atributos estándar de Braze y los ID de publicidad móvil. Debes asegurarte de que transmites adecuadamente estos datos a través de nuestros SDK o API.

## ¿Qué ocurre cuando se procesan mis datos para enviarlos a cada partner de Audience Sync? {#what-happens-when-my-data-is-being-processed-to-send-to-each-audience-sync-partner}

Los datos que selecciones para enviar a tu destino de sincronización de audiencias se normalizarán. Cada partner puede tener especificaciones diferentes para la normalización de datos en función de los requisitos de su API, así que revisa el endpoint específico de cada partner para obtener más detalles.

Además, Braze aplicará hash a todos los datos antes de sincronizar a los usuarios con nuestros partners de Audience Sync, garantizando que toda la PII se somete a hash SHA256.

## ¿Por qué puedo seleccionar varios identificadores en un paso para algunos partners, pero solo puedo seleccionar un identificador para otros? {#why-can-i-select-multiple-identifiers-in-one-step-for-some-partners-but-can-only-select-one-identifier-for-others}

Esto lo determinan los métodos de integración del partner y no lo controla Braze. Algunos partners (como Meta) permiten sincronizar varios identificadores, y otros partners (como Google) solo permiten sincronizar un único identificador con un usuario en un momento dado.

## ¿Cómo vuelvo a conectar mi integración? {#how-do-i-reconnect-my-integration}

Si el usuario anterior que conectó la integración ya no está en tu empresa, tendrás que actualizar la integración con el nuevo usuario seleccionando **Cambiar cuenta**. A continuación, selecciona **Confirmar** y conéctate con el nuevo usuario. Recomendamos cambiar de usuario cuando no se estén produciendo sincronizaciones activas, como antes de una entrada programada de usuarios en un Canvas, ya que la sincronización durante una transición del usuario anterior a un nuevo usuario puede interrumpir los Canvas activos.

El usuario que se vuelva a conectar debe tener acceso de lectura y escritura a todas las audiencias para que los usuarios puedan sincronizarse correctamente con los partners. Comprueba que el usuario que está reconectando la integración tiene acceso a las mismas cuentas de anuncios y audiencias. No tendrás que editar ningún paso en Canvas existente.

## ¿Cuáles son los errores más comunes que pueden producirse al crear y gestionar mis sincronizaciones de audiencia? {#what-are-common-errors-that-can-occur-when-creating-and-managing-my-audience-syncs}

| Error | Causa | Solución |
| --- | --- | --- |
| Token no válido | Esto puede ocurrir si has cambiado tu contraseña para iniciar sesión en una red publicitaria específica, o si tus credenciales han caducado. | Ve a la página del partner correspondiente para desconectar y volver a conectar tu cuenta. |
| Tamaño de la audiencia demasiado bajo | Esto puede ocurrir si has creado un paso de sincronización de audiencia que elimine usuarios de tus audiencias. Si el tamaño de tu audiencia se acerca a cero, la red puede marcar que el tamaño de la audiencia es demasiado bajo para servir. | Confirma que estás considerando una estrategia de sincronización de audiencia que añada y elimine usuarios regularmente de forma que no se agote por completo el tamaño de la audiencia. |
| La audiencia no existe | El paso de sincronización de audiencia utiliza una audiencia que no existe. Esto también puede activarse si no tienes el permiso necesario para acceder a la audiencia. | Añade una audiencia activa en tu configuración de sincronización de audiencia o crea una nueva audiencia. |
| Intento de acceso a la cuenta publicitaria | Este error se produce si no tienes permiso para la cuenta publicitaria, para una audiencia que hayas seleccionado o para ambas. | Trabaja con los administradores de tu cuenta publicitaria para obtener el acceso y los permisos adecuados. |
| Configuración no válida | Esto puede ocurrir si no has configurado un destino específico de sincronización de audiencia en Canvas, incluidos los campos de cuenta publicitaria, audiencia o usuario que deben coincidir. | Completa la configuración de cada partner antes del lanzamiento. |
| Condiciones de servicio | Para algunos destinos de sincronización de audiencia, como Facebook, la red publicitaria requiere que aceptes unas condiciones de servicio específicas para utilizar la característica de sincronización de audiencia. Este error se producirá si no has aceptado las condiciones correspondientes. | Confirma que has aceptado las condiciones requeridas de cada partner. Para Facebook en concreto, revisa [la solución de problemas de Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#troubleshooting). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="¿Cuáles son los errores más comunes que pueden producirse al crear y gestionar mis sincronizaciones de audiencia?" }