---
nav_title: Puente JavaScript
article_title: Puente JavaScript para páginas de destino
page_order: 5
page_type: reference
description: "Aprende a utilizar el puente JavaScript brazeBridge para registrar eventos, establecer atributos personalizados y desencadenar acciones de Braze desde el bloque de código personalizado de una página de destino."
---

# Puente JavaScript para páginas de destino {#javascript-bridge-for-landing-pages}

> Las páginas de destino admiten un «puente» JavaScript para conectar tu código personalizado (HTML, CSS y JavaScript) con el SDK de Braze.

Accede al puente utilizando `brazeBridge` en un bloque de código personalizado para registrar eventos, establecer atributos personalizados, identificar usuarios y más cuando un visitante interactúa con tu página de destino.

## Cómo funciona {#how-it-works}

Las páginas de destino te permiten añadir HTML, CSS y JavaScript personalizados a un bloque de **código personalizado** para tener mayor control sobre la apariencia, el estilo y el comportamiento de tu página. Los bloques de código personalizado pueden utilizar el [puente JavaScript](#supported-methods) para registrar eventos, establecer atributos personalizados, identificar usuarios y más:
- Registrar eventos personalizados y compras
- Establecer atributos de usuario estándar y personalizados
- Hacer seguimiento de clics y envíos de formularios
- Identificar usuarios

Si reutilizas código de `brazeBridge` de mensajes dentro de la aplicación o banners, debería seguir funcionando en las páginas de destino. Los métodos que no aplican a las páginas de destino se ignoran y registran una advertencia en la consola del navegador en lugar de causar un error. Para más detalles, consulta [Métodos no compatibles en páginas de destino](#methods-not-supported-on-landing-pages).

{% alert important %}
El puente de la página de destino es asíncrono; cada método devuelve una Promise. Esto difiere del [puente de mensajes dentro de la aplicación con HTML personalizado]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge), cuyos métodos devuelven resultados de forma inmediata. Si el siguiente paso de tu script depende de que una llamada al puente finalice —como redirigir la página, enviar un formulario o enviar datos a Braze— utiliza `await` o `.then()` y no asumas que la llamada se completó de forma síncrona.
{% endalert %}

## Disponibilidad del puente {#bridge-availability}

Cuando un visitante abre tu página de destino, `brazeBridge` ya está disponible en el JavaScript de tu **código personalizado**. Llama a los métodos del puente directamente en las páginas de destino: no necesitas esperar un evento de disponibilidad separado como el que usan los mensajes dentro de la aplicación con `ab.BridgeReady`.

Que el objeto del puente esté disponible no significa que el SDK de Braze esté inicializado para ese visitante. El SDK se inicializa para una visita a la página de destino en cualquiera de estos casos:

- El visitante abre la página a través de una [etiqueta de Liquid de página de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) enviada mediante un canal de Braze (correo electrónico, SMS, push, etc.). El SDK se inicializa automáticamente cuando la página se carga.
- El visitante envía el formulario de la página, por ejemplo, haciendo clic en un botón **Enviar** que envía los datos del formulario. Esto incluye las llamadas a `brazeBridge` realizadas dentro de las devoluciones de llamada `registerFormInput` de un [bloque de formulario personalizado]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks), ya que estas se ejecutan como parte del envío del formulario.

Si un visitante abre la página de destino directamente, sin una etiqueta de Liquid de página de destino, y nunca envía el formulario, la página es anónima para Braze y las llamadas a los métodos del puente no tienen efecto.

{% alert note %}
`window.lpBridge` y `window.appboyBridge` hacen referencia al mismo objeto del puente, pero ambos están obsoletos. Utiliza `window.brazeBridge`.
{% endalert %}

## Ejemplo {#example}

Dado que los métodos son asíncronos, utiliza un controlador async y `await` en las llamadas cuando el orden o la finalización sean importantes:

```html
<button id="button">Set Favorite Color</button>
<script>
  document.querySelector("#button").onclick = async function () {
    // Track a click for analytics
    await brazeBridge.logClick("set-favorite-color");
    // Set the user's custom attribute
    await brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    await brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    await brazeBridge.requestImmediateDataFlush();
  };
</script>
```

## Métodos compatibles {#supported-methods}

Los siguientes métodos de `brazeBridge` devuelven una promesa y son compatibles con los bloques de **código personalizado** de las páginas de destino. Utiliza `await` o `.then()` cuando necesites secuenciar tareas o garantizar su finalización.

### Métodos de nivel superior {#top-level-methods}

| Método | Descripción |
| --- | --- |
| `brazeBridge.changeUser(userId, signature?)` | Identifica al usuario con un ID único. |
| `brazeBridge.logCustomEvent(eventName, eventProperties?)` | Registra un evento personalizado. |
| `brazeBridge.logPurchase(productId, price, currencyCode?, quantity?, purchaseProperties?)` | Registra una compra. |
| `brazeBridge.requestImmediateDataFlush(callback?)` | Envía los datos en cola a los servidores de Braze. |
| `brazeBridge.logClick(trackingId)` | Registra un clic en la página de destino (`lp_c`) para el ID de seguimiento proporcionado. Consulta [Seguimiento de clics](#click-tracking). |
| `brazeBridge.logSubmit()` | Registra un envío de formulario de la página de destino (`lp_fs`). Específico de páginas de destino. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métodos de nivel superior" }

### Métodos de `getUser()` {#getuser-methods}

{% alert note %}
`brazeBridge.getUser()` devuelve un objeto simple de forma síncrona, por lo que no necesitas usar `await` con `getUser()`; los métodos del objeto devuelto (como `getUser().setEmail(email)`) sí devuelven Promises.
{% endalert %}

`getUser()` devuelve un objeto que expone los siguientes métodos de usuario. Cada método devuelve una Promise.

| Método | Descripción |
| --- | --- |
| `getUser().setFirstName(firstName)` | Establece el nombre del usuario. |
| `getUser().setLastName(lastName)` | Establece el apellido del usuario. |
| `getUser().setEmail(email)` | Establece la dirección de correo electrónico del usuario. |
| `getUser().setPhoneNumber(phoneNumber)` | Establece el número de teléfono del usuario. |
| `getUser().setGender(gender: "m" \| "f" \| "o" \| "u" \| "n" \| "p")` | Establece el género del usuario: masculino, femenino, otro, desconocido, no aplica o prefiere no decirlo, respectivamente. |
| `getUser().setDateOfBirth(year, month, day)` | Establece la fecha de nacimiento del usuario. |
| `getUser().setCountry(country)` | Establece el país del usuario. |
| `getUser().setHomeCity(city)` | Establece la ciudad de residencia del usuario. |
| `getUser().setLanguage(language)` | Establece el idioma del usuario. |
| `getUser().setCustomUserAttribute(key, value, merge?)` | Establece un atributo personalizado del usuario. |
| `getUser().addToCustomAttributeArray(key, value)` | Añade un valor a un arreglo de atributos personalizados. |
| `getUser().removeFromCustomAttributeArray(key, value)` | Elimina un valor de un arreglo de atributos personalizados. |
| `getUser().incrementCustomUserAttribute(key, incrementValue?)` | Incrementa un atributo personalizado numérico. |
| `getUser().setCustomLocationAttribute(key, latitude, longitude)` | Establece un atributo de ubicación personalizado. |
| `getUser().addToSubscriptionGroup(subscriptionGroupId)` | Añade al usuario a un grupo de suscripción de correo electrónico o SMS. |
| `getUser().removeFromSubscriptionGroup(subscriptionGroupId)` | Elimina al usuario de un grupo de suscripción de correo electrónico o SMS. |
| `getUser().setEmailNotificationSubscriptionType(type: "opted_in" \| "subscribed" \| "unsubscribed")` | Establece el estado de suscripción a notificaciones por correo electrónico. |
| `getUser().setPushNotificationSubscriptionType(type: "opted_in" \| "subscribed" \| "unsubscribed")` | Establece el estado de suscripción a notificaciones push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métodos de getUser()" }

## Seguimiento de clics {#click-tracking}

Utiliza `brazeBridge.logClick(trackingId)` para hacer seguimiento de los clics en tu página de destino. Cada llamada registra un evento de clic en la página de destino (`lp_c`) etiquetado con el ID de seguimiento que proporcionas:

```html
<a href="#" onclick="brazeBridge.logClick('cta-hero')">Get started</a>
```

{% alert note %}
El seguimiento de clics en páginas de destino difiere de los mensajes dentro de la aplicación, que utilizan `logClick('0')` y `logClick('1')` como IDs convencionales para "Botón 1" y "Botón 2". Las páginas de destino no tienen IDs de botón especiales equivalentes. Cada llamada a `logClick(trackingId)` registra un evento `lp_c` identificado por el ID de seguimiento que proporcionas.
{% endalert %}

## Métodos no compatibles en páginas de destino {#methods-not-supported-on-landing-pages}

Los siguientes métodos funcionan en mensajes dentro de la aplicación y banners, pero no son compatibles con las páginas de destino. Si tu código llama a uno de ellos en una página de destino, Braze ignora la llamada. Tu página sigue funcionando, pero es posible que veas una advertencia en la consola para desarrolladores del navegador.

| Método | Notas |
| --- | --- |
| `brazeBridge.closeMessage()` | No hay una interfaz de mensaje que cerrar en una página de destino. |
| `brazeBridge.requestPushPermission(successCallback?, deniedCallback?)` | El permiso push no se solicita desde una página de destino. |
| `brazeBridge.web.registerAppboyPushMessages(successCallback?, deniedCallback?)` | El registro de notificaciones push web no está disponible en las páginas de destino. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métodos no compatibles en páginas de destino" }

## Contenido relacionado {#related-content}

- [Crear bloques de formulario personalizados]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks) cubre un uso más avanzado de este puente: conectar una interfaz completamente personalizada a un formulario de página de destino.
- [Crear páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)