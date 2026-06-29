---
page_order: 1.3
nav_title: Depuración
article_title: Depuración del SDK de Braze
description: "Aprende a utilizar el Depurador de SDK de Braze, para que puedas solucionar los problemas de tus canales con SDK, sin habilitar manualmente el registro detallado en tu aplicación."
---

# Depuración del SDK de Braze {#debugging-the-braze-sdk}

> Aprende a utilizar el depurador integrado del SDK de Braze, para que puedas solucionar problemas de tus canales con SDK, sin necesidad de habilitar el registro detallado en tu aplicación.

{% alert tip %}
Para una investigación más profunda, también puedes [habilitar el registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/) para capturar la salida detallada del SDK y [aprender a leer los registros detallados]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs/) de canales específicos.
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar el Depurador de SDK de Braze, necesitarás los permisos "View PII" y "View User Profiles (PII Redacted)". Para descargar los registros de tus sesiones de depuración, también necesitarás el permiso "Export User Data". Además, tu SDK de Braze debe cumplir o apuntar a las siguientes versiones mínimas:

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

Para recopilar registros del depurador cuando `Braze.configuration.logger.level` es `.disabled`, usa Swift SDK 11.9.0 o posterior. Para más información, consulta el [registro de cambios de Swift]({{site.baseurl}}/developer_guide/changelogs/#swift_fixed-12).

## Depuración del SDK de Braze

{% alert tip %}
Para habilitar la depuración del SDK Web de Braze, puedes [utilizar un parámetro de URL]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#logging).
{% endalert %}

### Paso 1: Cierra tu aplicación {#step-1-close-your-app}

Antes de iniciar la sesión de depuración, cierra la aplicación que esté experimentando problemas. Puedes relanzar la aplicación al inicio de tu sesión.

### Paso 2: Crea una sesión de depuración {#step-2-create-a-debugging-session}

En Braze, ve a **Configuración** y, en **Configuración y pruebas**, selecciona **Depurador de SDK**.

![La sección "Configuración y pruebas" con "Depurador de SDK" resaltado.]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})

Selecciona **Crear sesión de depuración**.

![La página "Depurador de SDK".]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})

### Paso 3: Selecciona un usuario {#step-3-select-a-user}

Busca a un usuario utilizando su dirección de correo electrónico, `external_id`, alias de usuario o token de notificaciones push. Cuando estés listo para iniciar la sesión, selecciona **Seleccionar usuario**.

![La página de depuración para el usuario seleccionado.]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %}){: style="max-width:85%;"}

### Paso 4: Vuelve a lanzar la aplicación {#step-4-relaunch-the-app}

Primero, inicia la aplicación y confirma que tu dispositivo está emparejado. Si el emparejamiento se realiza correctamente, relanza tu aplicación&#8212;así te asegurarás de que los registros de inicialización de la aplicación se capturan por completo.

### Paso 5: Completa los pasos de reproducción {#step-5-complete-the-reproduction-steps}

Tras relanzar tu aplicación, sigue los pasos para reproducir el error.

{% alert tip %}
Cuando reproduzcas el error, asegúrate de seguir los pasos de reproducción lo más fielmente posible, para que puedas crear [registros de calidad](#step-6-export-your-session-logs-optional).
{% endalert %}

### Paso 6: Finaliza tu sesión {#step-6-end-your-session}

Cuando hayas terminado con los pasos de reproducción, selecciona **Finalizar sesión** > **Cerrar**.

![La sesión de depuración muestra el botón "Finalizar sesión".]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %}){: style="max-width:85%;"}

{% alert note %}
Puede tardar unos minutos en generar tus registros, dependiendo de la duración de la sesión y de la conectividad de la red.
{% endalert %}

### Paso 7: Comparte o exporta tu sesión (opcional) {#step-7-share-or-export-your-session-optional}

Después de la sesión, puedes exportar tus registros de sesión como archivo CSV. Además, otras personas pueden utilizar tu **ID de sesión** para buscar tu sesión de depuración, por lo que no necesitas enviarles tus registros directamente.

![La página de depuración con "Exportar registros" y "Copiar ID de sesión" que se muestra después de la sesión.]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})