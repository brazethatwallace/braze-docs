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

Si ves "You do not have any remaining Currents integrations" al añadir una nueva integración, las causas más comunes son:

- No se ha adquirido ningún derecho de uso de Currents para este espacio de trabajo.
- El derecho de uso de Currents está disponible en un espacio de trabajo diferente de tu empresa.

Ponte en contacto con tu director de cuentas de Braze para solicitar un derecho de uso o ajustar tu configuración.

## Requisitos {#requirements}

El uso de Currents con cualquiera de nuestros socios requiere los mismos parámetros básicos y metodología de conexión.

Cada socio requiere que Braze tenga permiso para escribirle y enviarle archivos de datos, y Braze solicita la ubicación en la que debe escribir esos archivos, concretamente nombres de contenedor o claves.

Los siguientes requisitos son los básicos y mínimos para integrarse con la mayoría de nuestros socios. Algunos socios exigirán parámetros adicionales, que figuran en la [documentación de sus respectivos socios]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) junto con cualquier matiz asociado a estos requisitos básicos.

| Requisito | Origen | Acceso | Descripción
|---|---|---|---|
| Cuenta con socio | Configura una cuenta con ese socio o ponte en contacto con tu director de cuentas de Braze para obtener sugerencias. | Consulta el sitio web de ese socio o ponte en contacto con él para registrarte. | Braze no enviará datos a un socio si no tienes acceso a esos datos a través de la cuenta de tu empresa.
| Clave de API o token del socio | Normalmente el dashboard del socio. | Cópialo y pégalo en el campo designado de Braze. | Braze tiene un campo designado para ello en la página de integraciones de ese socio. Necesitamos esto para saber dónde enviar tus datos. **Mantén tus claves o tokens de socio actualizados; las credenciales no válidas pueden desactivar tu conector y eliminar eventos.**
| Código/clave de autenticación, clave secreta, archivo de certificación | Ponte en contacto con un representante de tu cuenta con ese socio. También puede existir en el dashboard del socio. | Copia y pega las claves en el campo designado de Braze. Genera y carga archivos `.json` u otros archivos de certificación en el lugar adecuado de Braze. | Braze tiene un campo designado para ello en la página de integraciones de ese socio. Esto proporciona credenciales a Braze y nos autoriza a escribir archivos en tu cuenta de socio. **Es importante que mantengas tus datos de autenticación actualizados; unas credenciales no válidas pueden hacer que se desactive tu conector y que se pierdan eventos.**
| Contenedor, ruta de carpeta | Algunos socios organizan y clasifican los datos por contenedores. Debe encontrarse en el dashboard del socio. | Si es necesario, copia el nombre de contenedor o la ruta del archivo exactamente en el espacio designado en Braze. | Aunque esto es necesario para algunos socios, es importante acertar cuando lo necesites. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Requirements" }

{% alert important %}
Es importante que mantengas actualizadas tus claves de socio, tokens de socio y datos de autenticación; si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **5 días**, los eventos del conector se descartarán y los datos se perderán de forma permanente.
{% endalert %}

## Configuración de Currents {#setting-up-currents}

### Paso 1: Elige a tu socio {#step-1-choose-your-partner}

Braze Currents te permite integrarte a través del almacenamiento de datos utilizando archivos planos o con nuestros socios de análisis del comportamiento y datos de clientes utilizando cargas útiles JSON por lotes a un punto de conexión designado.

Antes de empezar la integración, es mejor decidir qué integración es la más adecuada para tus propósitos. Por ejemplo, si ya utilizas mParticle y Segment y quieres que los datos de Braze fluyan allí, lo mejor sería utilizar una carga útil JSON por lotes. Si prefieres manipular los datos por tu cuenta o tienes un sistema más complejo de análisis de datos, puede que lo mejor sea utilizar el almacenamiento de datos ([¡Braze utiliza este método]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents/)!)

### Paso 2: Abre Currents {#step-2-open-currents}

Para empezar, ve a **Integraciones de socios** > **Currents**. Accederás a la página de gestión de la integración de Currents.

![Página de Currents en el panel de Braze]({% image_buster /assets/img_archive/currents-main-page.png %})

### Paso 3: Añade tu socio {#step-3-add-your-partner}

Añade un socio, a veces llamado "conector de Currents", seleccionando el desplegable en la parte superior de la pantalla.

Cada socio requiere un conjunto diferente de pasos de configuración. Para habilitar cada integración, consulta nuestra lista de [socios disponibles]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) y sigue las instrucciones en sus respectivas páginas.

### Paso 4: Configura tus eventos {#step-4-configure-your-events}

Elige los eventos que deseas pasar a ese socio marcando entre las opciones disponibles. Encontrarás listados de estos eventos en nuestras bibliotecas de [eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) y [eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).

![]({% image_buster /assets/img/current4.png %})

Si lo necesitas, puedes obtener más información sobre nuestros eventos en nuestro artículo sobre [semántica de la entrega de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/).

### Paso 5: Configura las transformaciones de campo {#step-5-set-up-field-transformations}

Puedes utilizar las transformaciones de campo de Currents para eliminar o convertir en hash un campo de cadena.

- **Eliminar:** Sustituye el campo de cadena por `[REDACTED]`. Esto es útil si tu socio rechaza eventos en los que faltan campos o están vacíos.
- **Hash:** Aplica un algoritmo de hash SHA-256 al campo de cadena.

Al seleccionar un campo para una de estas transformaciones, dicha transformación se aplicará a todos los eventos en los que aparezca ese campo. Por ejemplo, si seleccionas `email_address` para el hash, el campo `email_address` se convertirá en hash en los eventos de envío de correo electrónico, apertura de correo electrónico, rebote de correo electrónico y cambio de estado del grupo de suscripción.

![Añadir transformaciones de campo]({% image_buster /assets/img/current3.png %})

### Paso 6: Prueba tu integración {#step-6-test-your-integration}

{% alert important %}
Currents eliminará los eventos con cargas útiles excesivamente grandes, superiores a 900&nbsp;KB.
{% endalert %}

Antes de realizar la prueba, te recomendamos que consultes nuestros [datos de muestra de Currents en GitHub](https://github.com/Appboy/currents-examples). Cuando estés listo para realizar la prueba, elige una de las siguientes opciones:

#### Envío de eventos de prueba {#sending-test-events}

Para probar tu integración, puedes seleccionar **Send Test Events** para enviar un evento de cada uno de los tipos de eventos seleccionados a este Current. Para obtener información detallada sobre cada tipo de evento, consulta nuestras bibliotecas de [eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) y [eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).

![La página de prueba de Currents en el panel de Braze.]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Comprobación de los conectores de prueba de Currents {#testing-currents-connectors}

Los conectores de prueba de Currents son versiones gratuitas de nuestros conectores existentes que pueden utilizarse para probar y ensayar diferentes destinos. Los conectores de prueba de Currents tienen:

- Hasta 10 conectores de prueba de Currents por espacio de trabajo.
- Un máximo acumulado de 1500 eventos por cada periodo fijo de 24 horas, que se restablece a medianoche UTC. Este total de eventos se actualiza cada hora en el dashboard.

Una vez que tus conectores de prueba de Currents alcancen el límite de envío, tu conector no enviará eventos hasta el día siguiente (a medianoche UTC).

Para actualizar tu conector de prueba de Currents, edita la integración en el dashboard y selecciona **Upgrade Test Integration**.

## Actualizar Currents {#updating-currents}

{% multi_lang_include updating_currents.md %}

## Lista de direcciones IP permitidas {#ip-allowlisting}

Braze enviará datos de Currents desde las IP de la lista:

{% multi_lang_include data_centers.md datacenters='ips' %}