{% if include.alert == 'Web push private browsing' %}

{% alert important %}
Las ventanas de navegación privada no admiten notificaciones push web.
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
Añadir una dirección BCC a tu Campaign o Canvas hace que se dupliquen los correos electrónicos facturables para la Campaign o el componente de Canvas, ya que Braze envía un mensaje a tu usuario y otro a tu dirección BCC.
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
La configuración de prioridad de visualización de notificaciones ya no se utiliza en dispositivos con Android O o versiones posteriores. En estos dispositivos, configura la prioridad a través de [la configuración del canal de notificaciones](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
No envíes correos transaccionales legalmente requeridos a las pasarelas SMS, ya que es muy probable que esos correos electrónicos no se entreguen.
<br><br>
Aunque los correos electrónicos que envías utilizando un número de teléfono y el dominio de la pasarela del proveedor (conocido como MM3) pueden hacer que el correo electrónico se reciba como un mensaje SMS (de texto), algunos de nuestros proveedores de correo electrónico no admiten este comportamiento. Por ejemplo, si envías un correo electrónico a un número de teléfono de T-Mobile (como "9999999999@tmomail.net"), tu mensaje SMS se enviará a quien posea ese número de teléfono en la red de T-Mobile.
<br><br>
Ten en cuenta que, aunque estos correos electrónicos no se entreguen a la pasarela de SMS, seguirán contando para tu facturación por correo electrónico. Para evitar enviar correos electrónicos a pasarelas no admitidas, revisa la [lista de nombres de dominio de pasarelas no admitidas](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads).
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
Para mayor seguridad, te recomendamos añadir nuestra característica de [autenticación SDK]({{site.baseurl}}/developer_guide/authentication) para evitar la suplantación de identidad de usuarios.
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
Hay ciertos navegadores, como las aplicaciones Naver para Android e iOS, que no son compatibles con el centro de preferencias de Braze. Si prevés que algunos de tus usuarios utilizan estos navegadores, considera proporcionarles métodos alternativos para gestionar sus preferencias de correo electrónico.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
El evento de compra heredado está entrando en modo de mantenimiento. Los clientes existentes de Braze pueden seguir utilizando los eventos de compra heredados. Seguirán funcionando como se espera, pero las nuevas funcionalidades se desarrollarán sobre los eventos recomendados de comercio electrónico en adelante. Braze proporcionará un aviso previo con suficiente antelación antes de que se establezca cualquier fecha de fin de vida. Los nuevos clientes de Braze deben utilizar los [eventos recomendados de comercio electrónico]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events), ya que los eventos de compra heredados no estarán disponibles.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
El evento de compra heredado entrará en un estado obsoleto (modo de mantenimiento). Los eventos de compra seguirán funcionando como se espera, pero no se desarrollarán nuevas funcionalidades netas sobre ellos, en favor de los [eventos recomendados de comercio electrónico]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events). Cuando esto ocurra, los filtros de segmento ya no aparecerán en el comportamiento de compra.<br><br> Si actualmente utilizas eventos de compra, recibirás un aviso previo sobre los planes de eliminación gradual. Por ahora, puedes seguir utilizando los eventos de compra hasta la fecha oficial de obsolescencia. Para más información, consulta el [resumen de eventos recomendados]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events).
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
Los archivos de exportación almacenados en los contenedores de S3 se eliminan automáticamente una vez que caduca el enlace de descarga (cuatro horas después del envío del correo electrónico de exportación, a menos que se indique lo contrario).
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
La integración con Shopify admite webhooks de creación y actualización de clientes de Shopify, que se encuentran en la configuración de datos. Cuando se crea o actualiza un perfil de usuario en Shopify, se creará o actualizará el perfil de usuario correspondiente en Braze. <br><br>Estas acciones no desencadenan eventos personalizados en Braze y se utilizan únicamente para [sincronizar los datos de usuario de Shopify con Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#how-the-integration-works). Los datos sincronizados incluyen [atributos personalizados]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#supported-shopify-custom-attributes), [atributos estándar]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#supported-shopify-standard-attributes) y, si están habilitados en tu configuración, [estados de grupos de suscripción]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins).
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
Las propiedades de entrada de Canvas forman parte de las variables de contexto de Canvas. Esto significa que `canvas_entry_properties` se referencia como `context`. Cada variable `context` incluye un nombre, un tipo de datos y un valor que puede incluir Liquid. Actualmente, `canvas_entry_properties` es compatible con versiones anteriores. Para más detalles, consulta [Contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#how-it-works) y [Objeto de contexto de Canvas]({{site.baseurl}}/api/objects_filters/context_object).
{% endalert %}

{% endif %}

{% if include.alert == 'Braze Agents' %}

{% alert important %}
Este partner aparece en tu página de **Partners tecnológicos** solo si tienes habilitados los [agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents). Para obtener ayuda para empezar, ponte en contacto con tu administrador de éxito de cliente.
{% endalert %}

{% endif %}

{% if include.alert == 'time filter types' %}

{% alert important %}
**Elegir entre los tipos de filtro «Día del año» y «Hora»**: al filtrar variables de contexto que contienen fechas, elige el tipo de comparación correcto en función de si la fecha se repite cada año. Usa «Día del año» solo cuando el año no esté incluido en el valor que produce la variable de contexto.

- **Usa «Día del año»** cuando la fecha se repita cada año (por ejemplo, cumpleaños, aniversarios o fiestas como Navidad). Este tipo de comparación calcula en función del día del año (1-365/366), ignorando el componente del año.
- **Usa «Hora»** cuando la fecha sea una fecha absoluta que no se repita (por ejemplo, fechas de finalización de contratos, fechas de citas o fechas de renovación de suscripciones). Este tipo de comparación calcula basándose en la marca de tiempo completa, incluido el año.

El uso de «Día del año» para fechas absolutas puede producir resultados incorrectos o inesperados, ya que el cálculo ignora el componente del año. Por ejemplo, si comparas la fecha de vencimiento de un contrato futuro en abril para determinar si está dentro de los 63 días, el uso de «Día del año» puede hacer que las fechas coincidan incorrectamente, ya que solo compara los números de los días (119 frente a 359) sin tener en cuenta que, en realidad, quedan 188 días para abril.
{% endalert %}

{% endif %}

{% if include.alert == 'granular permissions ea' %}

{% alert important %}
Los permisos granulares se encuentran en fase de acceso anticipado. Cuando se planifique la migración para tu empresa, los administradores de Braze recibirán correos electrónicos y banners en el panel notificándoles la [migración de permisos granulares]({{site.baseurl}}/granular_permissions_migration).
{% endalert %}

{% endif %}

{% if include.alert == 'WhatsApp audio and documents' %}

{% alert note %}
La [biblioteca de medios de Braze]({{site.baseurl}}/media_library) solo admite imágenes y video. Los archivos de audio y los documentos deben referenciarse a través de una URL alojada.
{% endalert %}

{% endif %}

{% if include.alert == 'Meta MP4 video issue' %}

{% alert important %}
Meta tiene un problema conocido que puede impedir que algunos videos MP4 se reproduzcan en dispositivos Android debido a configuraciones específicas de codificación o contenedor. Hasta que haya una solución permanente disponible, reformatear el archivo MP4 resuelve el problema para la mayoría de los remitentes. Prueba todos los videos en dispositivos Android para confirmar la capacidad de entrega correcta. <br><br>Puedes reformatear el archivo MP4 utilizando una herramienta web, como [CloudConvert](https://cloudconvert.com/mp4-converter). Carga tu archivo MP4 en la herramienta, conviértelo a MP4 de nuevo y luego descarga el archivo convertido.
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify cart token alias' %}

{% alert important %}
Para esta integración, el alias de usuario debe utilizar el siguiente formato para que Braze pueda asociar los webhooks con el perfil de usuario correcto:<br><br>
- `alias_label`: `shopify_cart_${cartToken}`
- `alias_name`: `shopify_cart_token`
{% endalert %}

{% endif %}

{% if include.alert == 'network dependency' %}

{% alert important %}
Content Cards, los mensajes dentro de la aplicación, los banners y los conmutadores de características dependen de la conectividad del dispositivo para sincronizarse con los servidores de Braze. Dado que las condiciones de la red pueden variar, existe la posibilidad de que el contenido o las actualizaciones no se sincronicen, muestren o eliminen de inmediato (por ejemplo, si un usuario está sin conexión). Recomendamos evitar estos canales para actualizaciones críticas y urgentes.
{% endalert %}

{% endif %}

{% if include.alert == 'dynamic image URL' %}

{% alert important %}
Si estás cargando imágenes con [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) o [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), asegúrate de que la URL de tu imagen comience con `https://`. Usar `http://` provocará que tu aplicación se bloquee.
{% endalert %}

{% endif %}