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

## El aspecto técnico del proceso de integración {#the-technical-side-of-the-integration-process}

Puede que pienses: "¡Mis desarrolladores son mágicos! Pueden hacer cualquier cosa, así que suelo dejarlos hacer lo suyo". Y es probable que lo sean y que puedan lograrlo. Pero no hay razón para que no sepas lo que hacen entre bastidores. De hecho, ayudaría a todo el proceso si supieras cuándo intervenir con información y qué buscar cuando te digan: "¿Puedes enviarme la clave de API y el punto final de la API?".

Entonces, ¿qué hacen cuando integran Braze con tu aplicación o sitio web? ¡Me alegro de que preguntes!

### Paso 1: Implementan el SDK de Braze {#step-1-they-implement-the-braze-sdk}

El SDK (kit de desarrollo de software) de Braze es la manera en que enviamos y obtenemos información desde y hacia tu aplicación o sitio web. Tus ingenieros son, esencialmente, los que unen nuestras aplicaciones. Para ello, necesitan algunos datos clave:

* Tus [claves de API]({{site.baseurl}}/api/api_key)
* Tu [punto final de SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)
  * Braze ya no proporciona puntos finales personalizados, así que utiliza los puntos finales de SDK predefinidos. Si se te ha proporcionado un punto final personalizado preexistente, aquí puedes encontrar los pasos de configuración necesarios para la integración de [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration#step-5-optional-custom-endpoint-setup), [iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift) y [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#initializing-the-sdk).

Puedes darles esta información directamente o darles acceso a Braze creándoles una cuenta.

{% alert warning %}
Asegúrate de que tú y tus desarrolladores no cambien las credenciales de la empresa en Braze sin saberlo o sin querer, ya que esto podría causar problemas durante el proceso de implementación o bloquear a uno o más de ustedes fuera de sus cuentas.
{% endalert %}

### Paso 2: Implementan los canales de mensajería que desees {#step-2-they-implement-your-desired-messaging-channels}

Braze tiene muchas opciones para ponerte en contacto con tus usuarios, y cada una requiere su propia configuración o ajuste para que funcione como deseas. Aquí es donde la comunicación con tus ingenieros resulta fundamental.

Asegúrate de indicar a tus desarrolladores qué canales deseas utilizar para garantizar que la implementación se realice de forma eficaz y en el orden adecuado.

| Canal | Detalles |
|---|---|
| Mensajes dentro de la aplicación | Requiere la implementación del SDK, así como estos pasos específicos del canal. |
| Push | Requiere la implementación del SDK para proporcionar una gestión adecuada de las credenciales de mensajería y los tokens de notificaciones push. |
| Correo electrónico | Se trata de un proceso totalmente distinto. Consulta la sección [Configuración del correo electrónico]({{site.baseurl}}/user_guide/channels/email/email_setup) para obtener más detalles sobre la integración. |
| Content Cards | Para empezar a utilizar [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards), ponte en contacto con tu administrador de éxito de cliente de Braze. |
| SMS y MMS | Consulta la sección [Configuración de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending) para obtener más detalles sobre la integración. |
| Webhooks | Requiere la implementación del SDK, así como pasos específicos del canal. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Implementan los canales de mensajería que desees" }

{% alert tip %}
Puedes utilizar Braze para crear campañas de mensajería accesibles en cada canal. Trabaja con tus desarrolladores para asegurarte de que cumples las normas de accesibilidad en tu implementación.
{% endalert %}

### Paso 3: Configuran tus datos {#step-3-they-set-up-your-data}

Braze no se limita a una sola habilidad. No se trata solo de enviar correos electrónicos o de enviar push. Se trata de crear recorridos del cliente personalizados que sean únicos para cada usuario y cliente. Los recorridos de los clientes se basan en sus acciones dentro de tu aplicación o sitio web, ¡y tú defines cuáles son! La siguiente tarea de tus desarrolladores es asegurarse de que las acciones realizadas en tu aplicación o sitio sean recogidas por Braze.

Entonces, ¿qué necesitas hacer para darles esta información?

1. Colabora con tu equipo de marketing para definir las campañas, los objetivos, los atributos y los eventos que necesitas controlar. Define esos ejemplos y compártelos con tus equipos.
2. Define tus requisitos de datos personalizados ([atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events), etc.).
3. A partir de ahí, discute cómo deberían rastrearse esos datos (desencadenados a través del SDK, etc.).
4. Define cuántos [espacios de trabajo]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces) necesitas. Tus ingenieros necesitarán saber cómo [probar y configurar]({{site.baseurl}}/user_guide/get_started/workspaces) estos espacios de trabajo.

Una vez que descubras toda esta información, compártela con tu ingeniero. Tomarán esa información e implementarán tus [datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data). Puede que incluso necesites [importar algunos usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/import_users). También debes conocer las [convenciones de nomenclatura de los eventos]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).

### Paso 4: Personalizan en función de lo que quieras {#step-4-they-customize-based-on-what-you-want}

Si quieres cosas como el lanzamiento desencadenado por API y el contenido conectado, discútelo tanto con tu contacto de Braze como con tus desarrolladores para asegurarte de que podrás incorporar a tus mensajes datos que viven fuera de tu aplicación y de Braze.

### Paso 5: Ambos realizan el control de calidad de tu implementación {#step-5-you-both-perform-qa-on-your-implementation}

Colabora con tu ingeniero para asegurarte de que todo funciona correctamente. Envía [mensajes de prueba]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages), utiliza nuestras [aplicaciones de prueba para Android]({{site.baseurl}}/developer_guide/references?tab=android) y [aplicaciones de prueba para iOS]({{site.baseurl}}/developer_guide/references?tab=swift), ¡comprueba todas las casillas antes de empezar a enviar!

Incluso tenemos instrucciones específicas para [probar tu integración con Android o FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/test_your_basic_integration#test-your-basic-integration) y para probar [el push en iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing).

## Después de la implementación {#after-implementation}

Ten en cuenta que la línea de meta de la implementación no es también la luz verde para enviar un millón de mensajes a la vez. Enviar un millón de push podría romper tu aplicación si todos los clientes hacen clic simultáneamente en el mismo enlace. Antes de hacer clic en el botón **Enviar**, te recomendamos que analices la capacidad de tu configuración interna para gestionar solicitudes de Braze. Luego, puedes establecer tu [límite de velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting) en función de eso.

![Logotipo de la comunidad Braze Firebrands]({% image_buster /assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Cuando te sientas cómodo utilizando Braze, ¡considera la posibilidad de convertirte en un Braze Firebrand! Con Braze Firebrands, nuestra comunidad de interacción con los clientes, estamos construyendo una comunidad de personas influyentes que utilizan Braze para modernizar su experiencia del cliente y su marketing. ¿Quieres saber más? [Únete ahora](https://brazefirebrands.splashthat.com/).