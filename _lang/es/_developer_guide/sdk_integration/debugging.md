---
page_order: 1.3
nav_title: Depuración
article_title: Depuración del SDK or kit de desarrollo de software de Braze
description: "Aprende a utilizar el depurador del SDK or kit de desarrollo de software de Braze, para que puedas solucionar problemas de tus canales con SDK or kit de desarrollo de software, sin habilitar el registro detallado en tu aplicación."
---

# Depuración del SDK or kit de desarrollo de software de Braze {#debugging-the-braze-sdk}

> Aprende a utilizar el depurador integrado del SDK or kit de desarrollo de software de Braze, para que puedas solucionar problemas de tus canales con SDK or kit de desarrollo de software, sin necesidad de habilitar el registro detallado en tu aplicación.

{% alert tip %}
Para una investigación más profunda, también puedes [habilitar el registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) para capturar la salida detallada del SDK or kit de desarrollo de software y [aprender a leer los registros detallados]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs) de canales específicos.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar el depurador del SDK or kit de desarrollo de software de Braze, necesitarás los permisos "View PII" y "View User Profiles (PII Redacted)". Para descargar los registros de tu sesión de depuración, también necesitarás el permiso "Export User Data". Además, tu SDK or kit de desarrollo de software de Braze debe cumplir o apuntar a las siguientes versiones mínimas:

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

Para recopilar registros del depurador cuando `Braze.configuration.logger.level` está en `.disabled`, usa Swift SDK or kit de desarrollo de software 11.9.0 o posterior. Para más información, consulta los [registros de cambios de Swift]({{site.baseurl}}/developer_guide/changelogs#swift_fixed-12).

## Depuración del SDK or kit de desarrollo de software de Braze

{% alert tip %}
Para habilitar la depuración del SDK or kit de desarrollo de software de Braze para Web, puedes [usar un parámetro de URL]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#logging).
{% endalert %}

### Paso 1: Cierra tu aplicación {#step-1-close-your-app}

Antes de iniciar tu sesión de depuración, cierra la aplicación que está experimentando problemas. Puedes volver a abrir la aplicación al inicio de tu sesión.

### Paso 2: Crea una sesión de depuración {#step-2-create-a-debugging-session}

En Braze, ve a **Configuración** y, en **Configuración y pruebas**, selecciona **SDK or kit de desarrollo de software Debugger**.

![La sección "Configuración y pruebas" con "SDK Debugger" resaltado.]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})

Selecciona **Crear sesión de depuración**.

![La página "SDK Debugger".]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})

### Paso 3: Selecciona un usuario {#step-3-select-a-user}

Busca un usuario usando su dirección de correo electrónico, `external_id`, alias de usuario o token de notificaciones push. Cuando estés listo para iniciar tu sesión, selecciona **Seleccionar usuario**.

![La página de depuración para el usuario seleccionado.]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %}){: style="max-width:85%;"}

### Paso 4: Vuelve a abrir la aplicación {#step-4-relaunch-the-app}

Primero, abre la aplicación y confirma que tu dispositivo está emparejado. Si el emparejamiento se realizó correctamente, vuelve a abrir tu aplicación: esto garantizará que los registros de inicialización de la aplicación se capturen completamente.

### Paso 5: Completa los pasos de reproducción {#step-5-complete-the-reproduction-steps}

Después de volver a abrir tu aplicación, sigue los pasos para reproducir el error.

{% alert tip %}
Cuando estés reproduciendo el error, asegúrate de seguir los pasos de reproducción lo más fielmente posible, para que puedas crear [registros de calidad](#step-6-export-your-session-logs-optional).
{% endalert %}

### Paso 6: Finaliza tu sesión {#step-6-end-your-session}

Cuando hayas terminado con los pasos de reproducción, selecciona **Finalizar sesión** > **Cerrar**.

![La sesión de depuración mostrando el botón "Finalizar sesión".]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %}){: style="max-width:85%;"}

{% alert note %}
Puede tardar unos minutos en generar tus registros dependiendo de la duración de tu sesión y la conectividad de red.
{% endalert %}

### Paso 7: Comparte o exporta tu sesión (opcional) {#step-7-share-or-export-your-session-optional}

Después de tu sesión, puedes exportar los registros de tu sesión como un archivo CSV. Además, otros pueden usar tu **ID de sesión** para buscar tu sesión de depuración, de modo que no necesitas enviarles tus registros directamente.

![La página de depuración con "Exportar registros" y "Copiar ID de sesión" mostrados después de la sesión.]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})