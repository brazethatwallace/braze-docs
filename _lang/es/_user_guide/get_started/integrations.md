---
nav_title: Integración
article_title: Visión general de la integración de incorporación
page_order: 8
page_type: reference
description: "Este artículo de referencia cubre brevemente los pasos de integración que deben seguir tus ingenieros o desarrolladores."
---

# Integración {#integration}

> Integrarse con Braze es un proceso que merece la pena. Pero eres inteligente. Estás **aquí**. Está claro que ya lo sabes. Pero lo que probablemente no sabes es que tú y tus desarrolladores están a punto de emprender juntos un viaje que requiere conocimientos técnicos, planificación estratégica y una comunicación coherente que les ayude a coordinarse.

{% alert note %}
Ten en cuenta que el contenido de este artículo no se aplica al correo electrónico. Consulta la sección [Configuración del correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup).
{% endalert %}

## El lado técnico del proceso de integración {#the-technical-side-of-the-integration-process}

Puede que estés pensando: "¡Mis desarrolladores son geniales! Pueden hacer cualquier cosa, así que normalmente los dejo a lo suyo". Y probablemente lo sean y puedan hacerlo. Pero no hay razón por la que no debas saber qué están haciendo entre bastidores. De hecho, ayudaría a todo el proceso si supieras cuándo intervenir con información y qué buscar cuando te digan: "¿Puedes enviarme la clave de API y el punto final de SDK?"

Entonces, ¿qué hacen cuando integran Braze con tu aplicación o sitio? ¡Qué bueno que preguntas!

### Paso 1: Implementan el SDK de Braze {#step-1-they-implement-the-braze-sdk}

El SDK de Braze (kit de desarrollo de software) es la forma en que enviamos y recibimos información de tu aplicación o sitio. Tus ingenieros, en esencia, están conectando nuestras aplicaciones. Para hacer esto, necesitan algunos datos clave:

* Tus [claves de API]({{site.baseurl}}/api/basics)
* Tu [punto final de SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)
  * Braze ya no proporciona endpoints personalizados, así que utiliza los endpoints de SDK predefinidos. Si te han proporcionado un endpoint personalizado preexistente, aquí puedes encontrar los pasos de configuración para la integración con [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration#step-5-optional-custom-endpoint-setup), [iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift) y [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#initializing-the-sdk).

Puedes proporcionarles esta información directamente o darles acceso a Braze creando una cuenta para ellos.

{% alert warning %}
Asegúrate de que ni tú ni tus desarrolladores cambien involuntaria o accidentalmente las credenciales de la empresa en Braze, ya que esto podría causar problemas durante el proceso de implementación o dejar a uno o más de ustedes fuera de sus cuentas.
{% endalert %}

### Paso 2: Implementan los canales de mensajería que deseas {#step-2-they-implement-your-desired-messaging-channels}

Braze tiene muchas opciones para comunicarse con tus usuarios, y cada una requiere su propia configuración o ajuste para funcionar de la manera que deseas. Aquí es donde la comunicación con tus ingenieros se vuelve fundamental.

Asegúrate de indicarles a tus desarrolladores qué canales quieres utilizar para que la implementación se realice de manera eficiente y en el orden adecuado.

| Canal | Detalles |
|---|---|
| In-App Messages | Requiere la implementación del SDK, así como estos pasos específicos del canal. |
| Push | Requiere la implementación del SDK para proporcionar el manejo adecuado de las credenciales de mensajería y los tokens de notificaciones push. |
| Correo electrónico | Este es un proceso completamente diferente. Consulta la sección [Configuración de correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup) para obtener más detalles sobre la integración. |
| Content Cards | Para comenzar con [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards), comunícate con tu administrador de éxito de cliente de Braze. |
| SMS y MMS | Consulta la sección [Configuración de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending) para obtener más detalles sobre la integración. |
| Webhooks | Requiere la implementación del SDK, así como pasos específicos del canal. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Implementan los canales de mensajería que deseas" }

{% alert tip %}
Puedes usar Braze para crear campañas de mensajería accesibles en cada canal. Trabaja con tus desarrolladores para asegurarte de cumplir con los estándares de accesibilidad en tu implementación.
{% endalert %}

### Paso 3: Configuran tus datos {#step-3-they-set-up-your-data}

Braze no es un producto de un solo truco. No se trata solo de enviar correos electrónicos o notificaciones push. Se trata de crear recorridos del cliente personalizados que sean únicos para cada usuario y cliente. Los recorridos del cliente se basan en sus acciones dentro de tu aplicación o sitio, ¡y tú defines cuáles son! La siguiente tarea de tus desarrolladores es asegurarse de que las acciones realizadas dentro de tu aplicación o sitio sean capturadas por Braze.

Entonces, ¿qué necesitas hacer para proporcionarles esta información?

1. Trabaja con tu equipo de marketing para definir las Campaigns, los objetivos, los atributos y los eventos que necesitas rastrear. Define esos ejemplos y compártelos con tus equipos.
2. Define tus requisitos de datos personalizados ([atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events), etc.).
3. A partir de ahí, discute cómo deben rastrearse esos datos (desencadenados a través del SDK, etc.).
4. Define cuántos [espacios de trabajo]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces) necesitas. Tus ingenieros necesitarán saber cómo [probar y configurar]({{site.baseurl}}/user_guide/get_started/workspaces) estos espacios de trabajo.

Una vez que recopiles toda esta información, compártela con tu ingeniero. Ellos tomarán esa información e implementarán tus [datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data). Puede que incluso necesites [importar algunos usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/import_users). También deberías conocer las [convenciones de nomenclatura de eventos]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).

### Paso 4: Personalizan en función de lo que deseas {#step-4-they-customize-based-on-what-you-want}

Si quieres cosas como el lanzamiento activado por API y contenido conectado, discútelo tanto con tu contacto de Braze como con tus desarrolladores para asegurarte de que podrás obtener datos que viven fuera de tu aplicación y Braze en tus mensajes.

### Paso 5: Ambos realizan el control de calidad de tu implementación {#step-5-you-both-perform-qa-on-your-implementation}

Trabaja junto con tu ingeniero para asegurarte de que todo funciona correctamente. Envía [mensajes de prueba]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages), usa nuestras [aplicaciones de prueba para Android]({{site.baseurl}}/developer_guide/references?tab=android) y [aplicaciones de prueba para iOS]({{site.baseurl}}/developer_guide/references?tab=swift), ¡revisa cada punto antes de empezar a enviar!

Incluso tenemos instrucciones específicas para [probar tu integración de Android o FireOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android) y probar las [notificaciones push para iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing).

## Después de la implementación {#after-implementation}

Ten en cuenta que la línea de meta de la implementación no es también la luz verde para enviar un millón de mensajes a la vez. Enviar un millón de notificaciones push podría hacer fallar tu aplicación si todos los clientes hacen clic en el mismo enlace simultáneamente. Te recomendamos que analices cuál es la capacidad de tu configuración interna para gestionar solicitudes de Braze antes de hacer clic en el botón **Send**. Después, puedes establecer tu [límite de velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting) en función de eso.

![Logotipo de la comunidad Braze Firebrands]({% image_buster /assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Cuando te sientas cómodo usando Braze, ¡considera convertirte en un Braze Firebrand! Con Braze Firebrands, nuestra comunidad de interacción con los clientes, estamos construyendo una comunidad de personas innovadoras que usan Braze para modernizar su experiencia del cliente y su marketing. ¿Te interesa saber más? [Únete ahora](https://brazefirebrands.splashthat.com/).