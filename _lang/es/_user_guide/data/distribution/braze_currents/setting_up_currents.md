---
nav_title: Configurar Currents
article_title: Configurar Currents
page_order: 1
page_type: tutorial
description: "Este artículo explica el proceso de integración y configuración de Braze Currents."
tool: Currents
search_rank: 8
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"}Configurar Currents {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcurrents-the-basics-2-stylefloatrightwidth120pxborder0-classnoimgborderset-up-currents}

> Esta página resume y describe el proceso genérico de integración y configuración de Braze Currents.

{% alert important %}
Currents está incluido en determinados paquetes de Braze. Ponte en contacto con tu representante de Braze si tienes alguna pregunta o deseas obtener acceso.
{% endalert %}

## Solución de problemas {#troubleshooting}

### No se puede añadir una nueva integración de Currents {#cannot-add-a-new-currents-integration}

Si ves "You do not have any remaining Currents integrations" al añadir una nueva integración, o si el botón para añadir un nuevo conector de Currents aparece atenuado, las causas más comunes son:

- No se ha adquirido un derecho de uso de Currents para este espacio de trabajo.
- El derecho de uso de Currents está disponible en un espacio de trabajo diferente de tu empresa.

Para resolver esto, comprueba otros espacios de trabajo dentro de tu empresa. Es posible que un espacio de trabajo diferente muestre un derecho de uso de Currents disponible. Si necesitas solicitar un derecho de uso o ajustar tu configuración, ponte en contacto con tu director de cuentas de Braze.

## Requisitos {#requirements}

Utilizar Currents con cualquiera de nuestros socios requiere los mismos parámetros básicos y la misma metodología de conexión.

Cada socio requiere que Braze tenga permiso para escribir y enviar archivos de datos, y Braze solicita la ubicación donde debe escribir esos archivos, específicamente nombres de contenedor o claves.

Los siguientes requisitos son los requisitos básicos y mínimos para integrarse con la mayoría de nuestros socios. Algunos socios requerirán parámetros adicionales, que se enumeran en su respectiva [documentación del partner]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) junto con cualquier particularidad asociada a estos requisitos básicos.

| Requisito | Origen | Acceso | Descripción
|---|---|---|---|
| Cuenta con el socio | Gestiona una cuenta con ese socio o contacta con tu director de cuentas de Braze para obtener sugerencias. | Consulta el sitio del socio o contacta con él para suscribirte. | Braze no enviará datos a un socio si no tienes acceso a esos datos a través de la cuenta de tu empresa.
| Clave de API o token del socio | Normalmente en el panel del socio. | Cópiala y pégala en el campo designado de Braze. | Braze tiene un campo designado para esto en la página de integraciones de ese socio. Lo necesitamos para mapear dónde enviamos tus datos. **Mantén tus claves o tokens del socio actualizados; unas credenciales no válidas pueden desactivar tu conector y provocar la pérdida de eventos.**
| Código/clave de autenticación, clave secreta, archivo de certificación | Contacta con un representante de tu cuenta con ese socio. También puede encontrarse en el panel del socio. | Copia y pega las claves en el campo designado de Braze. Genera y sube archivos `.json` u otros archivos de certificación en el lugar apropiado en Braze. | Braze tiene un campo designado para esto en la página de integraciones de ese socio. Esto proporciona a Braze las credenciales y nos autoriza a escribir archivos en tu cuenta del socio. **Es importante mantener tus datos de autenticación actualizados; unas credenciales no válidas pueden provocar la desactivación de tu conector y la pérdida de eventos.**
| Contenedor, ruta de carpeta | Algunos socios organizan y clasifican los datos por contenedores. Esto debería encontrarse en el panel del socio. | Si es necesario, copia el nombre del contenedor o la ruta del archivo exactamente en el espacio designado en Braze. | Aunque esto solo es necesario para algunos socios, es importante hacerlo correctamente cuando lo necesites. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Requisitos" }

{% alert important %}
Es importante mantener tus claves del socio, tokens del socio y datos de autenticación actualizados; si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **5 días**, los eventos del conector se descartarán y los datos se perderán permanentemente.
{% endalert %}

## Configuración de Currents {#setting-up-currents}

### Paso 1: Elige tu partner {#step-1-choose-your-partner}

Braze Currents te permite integrarte a través de almacenamiento de datos utilizando archivos planos o con nuestros socios de análisis del comportamiento y datos de clientes mediante cargas útiles JSON por lotes a un endpoint designado.

Antes de comenzar tu integración, lo mejor es decidir qué integración se adapta mejor a tus necesidades. Por ejemplo, si ya utilizas mParticle y Segment y te gustaría que los datos de Braze se transmitieran allí, lo mejor sería usar una carga útil JSON por lotes. Si prefieres manipular los datos por tu cuenta o tienes un sistema más complejo de análisis de datos, podría ser mejor usar el almacenamiento de datos ([¡Braze utiliza este método!]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents))

### Paso 2: Abre Currents {#step-2-open-currents}

Para empezar, ve a **Integraciones de socios** > **Currents**. Serás dirigido a la página de gestión de integraciones de Currents.

![Página de Currents en el panel de Braze]({% image_buster /assets/img_archive/currents-main-page.png %})

### Paso 3: Añade tu partner {#step-3-add-your-partner}

Añade un partner, a veces llamado "conector de Currents", seleccionando el menú desplegable en la parte superior de la pantalla.

Cada partner requiere un conjunto diferente de pasos de configuración. Para habilitar cada integración, consulta nuestra lista de [socios disponibles]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) y sigue las instrucciones en sus respectivas páginas.

{% multi_lang_include currents/contact_email_notifications.md %}

### Paso 4: Configura tus eventos {#step-4-configure-your-events}

Elige los eventos que deseas enviar a ese partner marcando las opciones disponibles. Puedes encontrar listados de estos eventos en nuestras bibliotecas de [eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) y [eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

![Página de configuración de Currents con eventos del partner seleccionados para exportación.]({% image_buster /assets/img/current4.png %})

Si lo necesitas, puedes obtener más información sobre nuestros eventos en nuestro artículo de [semántica de la entrega de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics).

### Paso 5: Configura las transformaciones de campos {#step-5-set-up-field-transformations}

Puedes usar las transformaciones de campos de Currents para eliminar o aplicar hash a un campo de cadena.

- **Eliminar:** Reemplaza el campo de cadena con `[REDACTED]`. Esto es útil si tu partner rechaza eventos con campos vacíos o faltantes.
- **Hash:** Aplica un algoritmo de hash SHA-256 al campo de cadena.

Seleccionar un campo para una de estas transformaciones aplicará esa transformación a todos los eventos en los que aparezca ese campo. Por ejemplo, seleccionar `email_address` para hash aplicará hash al campo `email_address` en los eventos de envío de correo electrónico, apertura de correo electrónico, rebote de correo electrónico y cambio de estado del grupo de suscripción.

![Añadir transformaciones de campos]({% image_buster /assets/img/current3.png %})

### Paso 6: Prueba tu integración {#step-6-test-your-integration}

{% alert important %}
Currents descartará eventos con cargas útiles excesivamente grandes de más de 900&nbsp;KB.
{% endalert %}

Antes de probar, considera revisar nuestros [datos de ejemplo de Currents en GitHub](https://github.com/Appboy/currents-examples). Cuando estés listo para probar, elige una opción en la siguiente sección:

#### Envío de eventos de prueba {#sending-test-events}

Para probar tu integración, puedes seleccionar **Send Test Events** para enviar un evento de cada uno de los tipos de eventos seleccionados a este Current. Para obtener información detallada sobre cada tipo de evento, consulta nuestras bibliotecas de [eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) y [eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

![La página "Prueba de Currents" en el panel de Braze.]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Prueba de conectores de Currents {#testing-currents-connectors}

Los conectores de prueba de Currents son versiones gratuitas de nuestros conectores existentes que se pueden usar para probar y experimentar con diferentes destinos. Los Currents de prueba tienen:

- Hasta 10 conectores de prueba de Currents por espacio de trabajo.
- Un máximo agregado de 1500 eventos por período fijo de 24 horas, que se reinicia a medianoche UTC. Este total de eventos se actualiza cada hora en el panel.

Después de que tus conectores de prueba de Currents alcancen el límite de envío, tu conector no enviará eventos hasta el día siguiente (a medianoche UTC).

Para actualizar tu conector de prueba de Currents, edita la integración en el panel y selecciona **Upgrade Test Integration**.

## Actualización de Currents {#updating-currents}

{% multi_lang_include currents/updating_currents.md %}

## Lista de IP permitidas {#ip-allowlisting}

Braze enviará datos de Currents desde las IP indicadas:

{% multi_lang_include administer/data_centers.md datacenters='ips' %}