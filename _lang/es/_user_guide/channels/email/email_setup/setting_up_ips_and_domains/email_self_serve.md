---
nav_title: Autoservicio de correo electrónico
article_title: Autoservicio de correo electrónico
page_order: 0
page_type: tutorial
channel: email
description: "Este artículo práctico cubre cómo configurar dominios de envío y seguimiento con el autoservicio de correo electrónico en Braze."
toc_headers: h2
---

# Autoservicio de correo electrónico {#email-self-serve}

> Esta página cubre cómo configurar dominios de envío y seguimiento en Braze para que tu dominio de remitente y los enlaces de seguimiento compartan el mismo subdominio.

## Requisitos previos {#prerequisites}

Para usar la configuración de autoservicio de correo electrónico, debes cumplir los siguientes requisitos previos:

- Ser un cliente nuevo en proceso de incorporación
- Tener el permiso a nivel de empresa "Edit Domain Settings"
- Tener un pool de IP, direcciones IP y un dominio verificado

## Consideraciones {#considerations}

- Planifica un subdominio de envío de al menos tres niveles. Dado que Braze crea un subdominio bajo tu dominio delegado (como "marketing.example.com"), tu dominio de envío debe tener al menos tres niveles de profundidad (como "e.marketing.example.com").
- El dominio de envío debe ser subordinado a un dominio que poseas. Por ejemplo, si posees "example.com", un subdominio podría ser "mail.example.com", lo que te permite usar la dirección de envío "@mail.example.com".
- Se aplican límites de dominio. El número total de dominios de seguimiento está limitado a 2 multiplicado por el número de dominios verificados en tu contrato. Si necesitas más, contacta a tu director de cuentas.

## Configuración {#setup}

### Paso 1: Agregar un dominio de envío {#step-1-add-a-sending-domain}

Tu subdominio de envío es la dirección desde la cual se envían tus correos electrónicos. Determina la dirección "de" que ven tus destinatarios.

1. En la sección **Domains**, selecciona **Add domain**.
2. Agrega tu dominio de envío en los campos **Mail from** y **Sending domain** para el pool de IP.
    - La dirección **Mail from** (remitente del sobre o ruta de retorno) es la que gestiona los rebotes en segundo plano. Tus destinatarios no ven esto en un correo electrónico. Por ejemplo, podrías usar "bounce" como subdominio, de modo que el correo personalizado de mail from sea "bounce.mail.example.com". Usar este subdominio es una práctica recomendada para la alineación DMARC SPF.
    - El **Sending domain** es el dominio en la dirección de remitente que los destinatarios ven en su buzón de entrada. Por ejemplo, si la dirección de remitente es "hello@e.mail.example.com", entonces "e.mail.example.com" es el dominio de envío.
{: start="3"}
3. Selecciona tu dominio verificado en el menú desplegable.

Los dominios de envío no se pueden cambiar después de ser enviados. Braze crea registros de DNS para verificación y autenticación y los agrega a tu configuración de DNS. Si necesitas eliminar un dominio de envío, contacta al [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) para obtener asistencia.

### Paso 2: Agregar un dominio de seguimiento {#step-2-add-a-tracking-domain}

Un dominio de seguimiento se usa para envolver los enlaces en tus correos electrónicos con fines de seguimiento de clics y marca. Los destinatarios ven esto cuando pasan el cursor sobre los enlaces o hacen clic en ellos en tus correos electrónicos. Debe ser un subdominio de tu dominio de envío o verificado para una delegación de DNS adecuada.

1. Selecciona si estás usando un **Verified domain** o un **Sending domain** como subdominio para tu dominio de seguimiento:
    - Si quieres que la URL de seguimiento coincida con el dominio de envío para consistencia de marca, selecciona **Sending domain**.
    - Si quieres una URL de seguimiento más corta, selecciona **Verified domain**.

{: start="2"}
2. Ingresa tu subdominio de seguimiento. Esto se antepone al subdominio seleccionado previamente.

El siguiente ejemplo muestra cómo se visualiza el dominio de seguimiento en el correo electrónico según tu selección:

|  | Selección | Dominio de seguimiento |
| --- | --- | ---|
| Dominio verificado | mail.example.com | links.mail.example.com |
| Dominio de envío | marketing.mail.example.com | links.marketing.mail.example.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Dominio de seguimiento por selección" }

{: start="3"}
3. Selecciona el subdominio verificado o de envío asociado desde el menú desplegable.
4. Selecciona **Submit**. Puedes ver los dominios de envío y seguimiento con un estado **Pending**.

Los registros de DNS de los dominios de envío pueden tardar de 5 a 10 minutos en propagarse. Cuando tu dominio esté listo para usar, recibirás un correo electrónico de notificación. Los registros de DNS de los dominios de seguimiento pueden tardar hasta 24 horas en propagarse, aunque generalmente toma menos. Es posible que veas que el subdominio de envío queda listo antes que el dominio de seguimiento.

### Paso 3: Seleccionar espacios de trabajo {#step-3-select-workspaces}

Selecciona los espacios de trabajo que deben tener acceso al dominio, luego selecciona **Confirm**. También puedes elegir agregar automáticamente el dominio de envío a nuevos espacios de trabajo cuando se creen.

### Paso 4: Configurar enlaces universales (opcional) {#step-4-set-up-universal-links-optional}

Los enlaces universales permiten que los enlaces en tus mensajes se abran directamente en tu aplicación móvil en lugar de un navegador móvil. Braze puede alojar los archivos de asociación en tus dominios de seguimiento en tu nombre.

{% alert note %}
Los enlaces universales se aplican por dominio de seguimiento. El mismo contenido de archivo se puede compartir entre dominios, pero cada dominio aloja su propia copia.
{% endalert %}

1. Ve a **Configuración** > **Configuración de la empresa** > **Dominios verificados** > **Enlaces universales**.
2. Selecciona **Set up universal links**.
3. Ingresa un nombre para el conjunto de enlaces universales.
4. Activa la configuración de iOS y agrega tu archivo AASA. JSON es el único tipo de archivo aceptado. Braze lee el archivo y muestra el número de IDs de aplicación y componentes encontrados, además de una vista previa del archivo generado.
5. Activa la configuración de Android y agrega tu archivo de Digital Asset Links de la misma manera. Braze muestra los nombres de paquetes, la huella digital del certificado SHA-256 y el número de declaraciones, además de una vista previa.
6. Revisa cada vista previa para confirmar que el contenido se ve correcto, luego selecciona **Next: Select tracking domains**. Solo aparecen los dominios de seguimiento verificados. Un conjunto puede aplicarse a múltiples dominios de seguimiento.
7. Tu conjunto aparece en la página de enlaces universales junto con sus dominios de seguimiento, canales, estado de iOS, estado de Android y fecha de creación. Braze verifica que el archivo AASA esté correctamente alojado para cada dominio e informa el resultado en la columna de estado.

### Paso 5: Probar el envío de correo electrónico {#step-5-test-your-email-sending}

Después de que tanto los dominios de envío como los de seguimiento muestren un estado **Ready for use**, prueba tu configuración:

1. En tu espacio de trabajo, ve a **Configuración** > **Configuración de correo electrónico**.
2. Verifica que el nuevo dominio de envío aparezca en la sección **Display Name Address**.
3. Agrega una dirección de remitente usando el nuevo dominio (por ejemplo, "hello@e.mail.example.com").
4. Selecciona **Save**.
5. Crea una Campaign de correo electrónico de prueba y envíatela a ti mismo. Luego, confirma que:
    - Tu correo electrónico se entregó correctamente.
    - La dirección de remitente es correcta.
    - Los enlaces de seguimiento de clics usan el dominio de seguimiento.
    - Los enlaces universales abren la aplicación o el sitio web según lo esperado en función del dispositivo del destinatario.
    - Los encabezados del correo electrónico se muestran correctamente.

## Próximos pasos {#next-steps}

Después de que tu verificación de remitente esté completa, Braze recomienda el calentamiento de IP para que tus mensajes lleguen a los buzones de entrada de destino a una tasa consistentemente alta. Después de completar esta configuración, consulta con el equipo de incorporación de Braze para confirmar si tus dominios y el [calentamiento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) están funcionando.

## Solución de problemas {#troubleshooting}

### La propagación de DNS está tardando más de lo esperado {#dns-propagation-is-taking-longer-than-expected}

Los registros de dominio de envío generalmente se propagan en 5 a 10 minutos. Los registros de dominio de seguimiento pueden tardar hasta 24 horas dependiendo de la configuración de TTL or tiempo de vida de tu proveedor de DNS. Si la propagación tarda más, confirma primero que los registros NS se agregaron correctamente y luego contacta al soporte de Braze.

### No puedo eliminar un dominio verificado {#im-not-able-to-remove-a-verified-domain}

Los dominios verificados no se pueden eliminar directamente en el panel, ya que esto puede potencialmente interrumpir tu envío si no se revisa adecuadamente. Contacta al soporte de Braze para que te ayuden a eliminar el dominio de tu cuenta.

### Mis enlaces universales no abren la aplicación {#my-universal-links-arent-opening-the-app}

Revisa primero los estados de iOS y Android en la página de enlaces universales. Si un dominio no aloja un archivo válido, abre el conjunto, corrige la configuración y guarda de nuevo. Si los estados se ven bien, asegúrate de estar probando desde un enlace en un correo electrónico en un dispositivo real en lugar de pegar la URL en la barra de direcciones del navegador.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puede Braze gestionar mi certificado SSL sin delegación NS? {#can-braze-manage-my-ssl-certificate-without-ns-delegation}

Los dominios verificados requieren registros NS (servidor de nombres) para la delegación de propiedad de DNS a Braze. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="Braze-hosted SSL certificates without NS delegation" %}

### ¿Puedo delegar un dominio raíz en su lugar? {#can-i-delegate-a-root-domain-instead}

Los dominios verificados están diseñados y recomendados principalmente para su uso con subdominios. No recomendamos delegar el dominio principal de tu marca por motivos de seguridad, ya que pierdes visibilidad y control sobre él. Si deseas delegar un dominio principal, usa un dominio principal que no se utilice en ningún otro lugar además de Braze.

### ¿Por qué mi dominio verificado no puede ser también el dominio de envío? {#why-cant-my-verified-domain-also-be-the-sending-domain}

Braze solo puede crear un subdominio de envío bajo tu dominio verificado, que generalmente es un subdominio del dominio principal (`mail.example.com`). Por lo tanto, la profundidad mínima del dominio de envío en este caso es de tres niveles (`e.mail.example.com`), en lugar de los dos niveles típicos.

### ¿Qué sucede si modifico alguno de mis registros NS después de la configuración? {#what-happens-if-i-modify-any-of-my-ns-records-after-setup}

Los dominios verificados dependen completamente de que los registros NS estén intactos. Si realizas cambios en alguno de tus registros NS, esto puede interrumpir tu envío de correo electrónico y seguimiento.

### ¿Puedo agregar solo una de las cuatro líneas de registros NS, ya que mi comando dig muestra los cuatro registros? {#can-i-add-only-one-of-four-ns-record-lines-since-my-dig-command-shows-all-four-records}

Confirma que los cuatro registros NS estén explícitamente presentes usando el comando `dig` y que el dominio se valide en el panel antes de considerar la configuración como completa.