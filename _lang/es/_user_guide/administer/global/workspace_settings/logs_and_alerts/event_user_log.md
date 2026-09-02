---
nav_title: Registro de eventos de usuario
article_title: Registro de eventos de usuario
page_order: 1
page_type: reference
description: "Este artículo de referencia cubre el registro de eventos de usuario, que puede ayudarte a depurar o solucionar problemas en tu integración de Braze."

---

# Registro de eventos de usuario {#event-user-log}

> El registro de eventos de usuario puede ayudarte a desglosar, depurar o solucionar problemas en tu integración de Braze. Esta pestaña te ofrece un registro de errores que detalla el tipo de error, con qué aplicación está asociado, cuándo ocurrió y, a menudo, la oportunidad de ver los datos sin procesar asociados.

{% alert tip %}
Además de este artículo, también te recomendamos consultar nuestro [curso de Braze Learning sobre herramientas de control de calidad y depuración](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), que cubre cómo usar el registro de eventos de usuario para realizar tu propia solución de problemas y depuración.
{% endalert %}

Para acceder al registro, ve a **Configuración** > **Configuración y pruebas** > **Registro de eventos de usuario**.

Para encontrar tus registros fácilmente, puedes filtrar según:

* SDK or kit de desarrollo de software o API
* Nombres de aplicaciones
* Período de tiempo
* Usuario

Cada registro se divide en múltiples secciones, que pueden incluir:

* Atributos del dispositivo
* Atributos del usuario
* Eventos
* Eventos de Campaign
* Datos de respuesta

Selecciona el icono **Expandir datos** para mostrar los datos JSON sin procesar de ese registro específico.

![El icono "Expandir datos" junto a un registro específico.]({% image_buster /assets/img_archive/expand_data.png %})

Los registros de eventos de usuario permanecerán en el panel durante 30 días después de ser registrados.

![Registros sin procesar de eventos]({% image_buster /assets/img_archive/rawlogs.png %}){: style="max-width:60%;"}

## Solución de problemas {#troubleshooting}

### Faltan registros del SDK or kit de desarrollo de software para usuarios de prueba {#missing-sdk-logs-for-test-users}

Si has añadido un usuario a un grupo interno, pero no muestra ningún registro del SDK or kit de desarrollo de software en el registro de usuarios del evento, esto puede deberse a una opción de configuración que falta. Para capturar los registros del SDK or kit de desarrollo de software, asegúrate de seleccionar **Registrar eventos de usuario para los miembros del grupo** en la **Configuración del grupo interno** de ese [grupo interno]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups).

### Retraso en las actualizaciones de los registros {#delay-in-logs-updates}

Este retraso suele deberse a la carga normal de procesamiento de la API.

Cuando llamas a métodos del SDK or kit de desarrollo de software, generalmente el SDK or kit de desarrollo de software almacena esos eventos en caché de forma local y los envía al servidor cada 10 segundos. Puede tardar desde un segundo hasta unos minutos para que nuestra cola de procesamiento de trabajos ingiera los eventos, dependiendo de la carga general en ese momento.

Si deseas que los eventos lleguen lo más rápido posible, intenta llamar a la función `requestImmediateDataFlush()`.

### Fallos en las impresiones de mensajes dentro de la aplicación {#in-app-message-impression-failures}

Si un mensaje dentro de la aplicación no se muestra, puedes encontrar el motivo en el registro de usuarios del evento expandiendo los datos JSON sin procesar de la solicitud del SDK or kit de desarrollo de software correspondiente y buscando el campo `error_code` en la respuesta. El `error_code` identifica la razón específica por la que falló la impresión (por ejemplo, un valor de color no válido o un problema de renderizado). Comparte este código de error con el [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) si se necesita una investigación adicional.

### El fin de sesión y el inicio de sesión tienen marcas de tiempo similares (iOS) {#session-end-and-session-start-have-similar-timestamps-ios}

El registro de usuarios del evento muestra la marca de tiempo de cuándo Braze fue notificado de que la sesión terminó, que es milisegundos antes de que comience la siguiente sesión. Braze no puede saber que la sesión ha terminado antes de que la aplicación se vuelva a abrir porque iOS es agresivo al detener la ejecución de hilos cuando la aplicación está en segundo plano, por lo que no se pueden enviar datos a Braze hasta que la aplicación se vuelva a abrir.

Aunque el tiempo de fin de sesión se especifica como segundos antes del inicio de sesión, cuando el evento se envía, la duración de la sesión se envía por separado y es correcta, reflejando el tiempo que la aplicación estuvo abierta. Por lo tanto, este comportamiento no afecta al filtro `Median Session Duration`.

En relación con las sesiones de usuario, puedes usar Braze para monitorear datos como:

- Cuántas sesiones ha tenido un usuario
- Cuándo un usuario inició una sesión por última vez
- Si el usuario inicia una sesión después de recibir una Campaign
- Cuál es la duración mediana de sesión del usuario

Estos comportamientos no se ven afectados por el evento de fin de sesión que se envía en la siguiente sesión.