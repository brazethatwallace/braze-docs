---
nav_title: Cómo empezar
article_title: Empieza a utilizar Braze Pilot
page_order: 2
page_type: reference
description: "Este artículo de referencia cubre brevemente los pasos de integración que deben seguir tus ingenieros o desarrolladores."
---

# Empieza a utilizar Braze Pilot {#get-started-with-braze-pilot}

> Este artículo explica cómo empezar a utilizar Braze Pilot. Aquí te guiaremos a través del proceso de descarga de la aplicación, inicialización de la conexión con tu panel de Braze y finalización de la configuración.

## Paso 1: Descarga Braze Pilot {#step-1-download-braze-pilot}

Para empezar a utilizar Braze Pilot, primero tendrás que descargar la aplicación desde Apple App Store o Google Play Store. Puedes buscar la aplicación en la tienda de aplicaciones o escanear los códigos QR de la siguiente sección para visitar la página de la aplicación para tu dispositivo.

## Paso 2: Acepta los términos y condiciones {#step-2-accept-the-terms-and-conditions}

A continuación, acepta los términos y condiciones e introduce tu correo electrónico del trabajo en el formulario. Tu correo electrónico se utilizará únicamente para análisis de uso de la aplicación y no se utilizará con fines de marketing.

![Página de bienvenida de Braze Pilot.]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"} ![Opción para introducir tu dirección de correo electrónico del trabajo.]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## Paso 3: Inicializa la conexión con el SDK de Braze {#step-3-initialize-the-connection-with-the-braze-sdk}

Braze Pilot te permite inicializar el SDK de Braze en cualquier panel de Braze. Una vez inicializado el SDK, Pilot comenzará a enviar datos de participación a Braze y te permitirá desencadenar cualquier mensaje lanzado desde ese panel de Braze.

Hay dos métodos para configurar la conexión del SDK en Pilot: códigos QR de demostración y el asistente de configuración.

{% tabs local %}
{% tab Códigos QR de demostración %}

### Método 1: Códigos QR de demostración {#method-1-demo-qr-codes}

Escanea un código QR que incluye todos los detalles necesarios para inicializar el SDK, crear tu perfil de usuario y establecer un vínculo profundo con una simulación de aplicación concreta en Braze Pilot. Los códigos QR de demostración se muestran en el cajón complementario para campañas de demostración específicas en tu prueba gratuita.

| Pilot para Android | Pilot para iOS |
| --- | --- |
| ![Código QR para Android.]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | ![Código QR para iOS.]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Método 1: Códigos QR de demostración" }

{% endtab %}
{% tab Asistente de configuración %}

### Método 2: Asistente de configuración {#method-2-setup-wizard}

Sigue una guía paso a paso para inicializar la conexión con el espacio de trabajo de tu panel desde la página **Configuración de la aplicación** en tu panel de Braze.

![Paso 1 del asistente de configuración de Braze Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Esta conexión es específica del espacio de trabajo. Esto significa que si inicializas la conexión desde el espacio de trabajo de demostración y luego cambias al espacio de trabajo en vivo en tu panel de prueba gratuita, tendrás que reinicializar el SDK desde ese espacio de trabajo para recibir cualquier campaña lanzada allí.

![El menú desplegable del espacio de trabajo en el panel de Braze con «Demo - Braze» seleccionado como espacio de trabajo activo.]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## Paso 4: Permite los permisos push {#step-4-allow-push-permissions}

Por último, se recomienda que permitas que la aplicación te envíe notificaciones push si deseas probar las funciones push a través de la aplicación. Puedes otorgar estos permisos a la aplicación de las siguientes maneras: actualizando la configuración de la aplicación en los ajustes de tu dispositivo o lanzando un mensaje push primer desde Braze a la aplicación.

{% tabs local %}
{% tab Actualizar la configuración de la aplicación %}

Abre la configuración de tu dispositivo y busca Braze Pilot. A continuación, actualiza la configuración para permitir que las notificaciones aparezcan en tu pantalla de bloqueo.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/device_settings.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Lanzar un mensaje push primer %}

Puedes utilizar un mensaje dentro de la aplicación de Braze para solicitar permisos push para la aplicación, tal como lo harías con tus propios consumidores. Para aprender a crear este tipo de mensaje en Braze, consulta [Mensajes push primer dentro de la aplicación]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages#push-primer-in-app-messages).

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Paso 5: Experimenta la mensajería de Braze en Pilot {#step-5-experience-braze-messaging-in-pilot}

¡Ya estás listo para empezar a recibir campañas y Canvas desde tu panel de Braze como usuario de Braze Pilot! Visita cualquiera de las campañas lanzadas en tu espacio de trabajo de demostración para ver una breve demostración de los casos de uso de Braze y, a continuación, dirígete a tu espacio de trabajo en vivo para empezar a enviar las tuyas.

Para obtener más información sobre cómo configurar campañas y Canvas en Braze, consulta [Primeros pasos: Campañas y Canvas]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases).