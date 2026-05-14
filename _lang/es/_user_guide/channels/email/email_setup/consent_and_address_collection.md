---
nav_title: Consentimiento y recogida de direcciones
article_title: Consentimiento y recogida de direcciones
page_order: 6
page_type: reference
description: "Este artículo de referencia cubre las mejores prácticas para recopilar el consentimiento y las direcciones de correo electrónico de los usuarios y define los diferentes estados posibles de suscripción de los usuarios."
channel: email

---

# Consentimiento y recopilación de direcciones {#consent-and-address-collection}

> Antes de enviar tus primeros correos electrónicos, es importante obtener primero el permiso de tus clientes. Es un gesto de cortesía y hace maravillas en tus tasas de apertura.

## Estados del suscriptor {#subscriber-states}

Existen tres estados de suscripción de correo electrónico para un usuario: **adhesión voluntaria**, **suscrito** y **cancelado**. Para cambiar el estado de suscripción de un usuario, consulta nuestro artículo sobre [cambiar suscripciones]({{site.baseurl}}/user_guide/channels/email/subscriptions/#changing-subscriptions) o usa nuestras [API de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

| Estado del suscriptor | Descripción |
|---|---|
| Adhesión voluntaria | Estos clientes han hecho clic en el enlace de un correo electrónico de confirmación y han optado activamente por recibir tus mensajes. |
| Suscrito | De forma predeterminada, los usuarios están suscritos al correo electrónico siempre que tengan una dirección de correo electrónico válida almacenada en su perfil. Los usuarios permanecen suscritos hasta que cancelan la suscripción o se adhieren voluntariamente. |
| Cancelado | Para ser marcado como cancelado, un cliente debe haberse dado de baja explícitamente de tus correos electrónicos o haber marcado un correo electrónico como correo no deseado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados del suscriptor" }

## Métodos de recopilación de direcciones {#address-collection-methods}

Además de obtener el permiso de tus usuarios antes de enviarles mensajes, existen varios métodos para recopilar estas direcciones de correo electrónico que pueden afectar tu capacidad de entrega.

### Listas de direcciones compradas {#purchased-address-lists}

Enviar correos electrónicos a listas compradas o alquiladas viola tu contrato con Braze. Si compras correos electrónicos, estás enviando mensajes totalmente no solicitados y te expones a problemas de capacidad de entrega.

### Corregistro {#co-registration}

El corregistro se refiere a un acuerdo entre empresas para recopilar información de los usuarios. Este es un método de recopilación arriesgado. Suscribe a los usuarios para recibir correos electrónicos de terceros, a veces sin el conocimiento o permiso del cliente. Si optas por esta vía, asegúrate de tener divulgaciones claras y la posibilidad de cancelar la suscripción en el punto de recopilación.

### Adhesión voluntaria preseleccionada o forzada {#pre-selected-or-forced-opt-in}

La adhesión voluntaria preseleccionada es un método de registro de correo electrónico en el que la casilla de registrarse para correo electrónico ya está marcada para que los suscriptores reciban tu correo electrónico. Al dejar la casilla marcada, los suscriptores están optando por recibir y dando su consentimiento para recibir tu correo electrónico. Este método tiende a molestar a las personas (y también es ilegal para correos enviados hacia o dentro de Canadá). Puede que termines con una lista de correo electrónico de tamaño considerable, pero realmente no puedes estar seguro de que estos usuarios quieran tus correos electrónicos de marketing.

### Adhesión voluntaria simple {#single-opt-in}

La adhesión voluntaria simple ocurre cuando los suscriptores se registran a través de un formulario de suscripción y se añaden inmediatamente a tu lista de correo electrónico. Con este método, los usuarios realizan un solo paso para suscribirse, como escribir su dirección de correo electrónico en un campo de recopilación o seleccionar una casilla como parte de una transacción.

### Adhesión voluntaria confirmada {#confirmed-opt-in}

Una adhesión voluntaria confirmada ocurre cuando un usuario marca una casilla solicitando comunicación por correo electrónico y se envía un mensaje de confirmación como respuesta. Este método permite a los usuarios elegir el tipo y la frecuencia del contenido, lo que mejora la interacción.

Para confirmar que te diriges solo a los usuarios más comprometidos, también puedes usar el método de adhesión voluntaria con doble confirmación. Este enfoque añade un paso adicional en el que el usuario debe hacer clic en un botón o enlace en el correo electrónico de confirmación para ser añadido a la lista de correo electrónico.