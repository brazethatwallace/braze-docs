---
nav_title: Entrega optimizada
article_title: Mensajes de WhatsApp con entrega optimizada
page_order: 1
description: "Este artículo de referencia cubre los pasos necesarios para crear un mensaje de WhatsApp con entrega optimizada."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Mensajes de WhatsApp con entrega optimizada {#whatsapp-messages-with-optimized-delivery}

> Mejora la capacidad de entrega y la interacción llegando a más usuarios adecuados en WhatsApp con una entrega dinámica basada en la interacción.

Los mensajes de WhatsApp con entrega optimizada se envían utilizando la [Marketing Messages API for WhatsApp](https://developers.facebook.com/docs/whatsapp/marketing-messages-api-for-whatsapp) (MM API for WhatsApp) de Meta, que ofrece una entrega dinámica basada en la interacción. Esto significa que tus mensajes de alta interacción (por ejemplo, aquellos con más probabilidades de ser leídos y de recibir clics) pueden llegar a más usuarios que probablemente interactúen con ellos. WhatsApp considera que tus mensajes son de alta interacción si son esperados, relevantes y oportunos, y por lo tanto más propensos a ser leídos y a recibir clics.

Las marcas pueden esperar una capacidad de entrega igual o mayor con MM API for WhatsApp, en comparación con Cloud API. En India, los mensajes de marketing de alta interacción registraron hasta un 9 % más de mensajes entregados en comparación con Cloud API, según Meta. Ten en cuenta que MM API for WhatsApp aún no garantiza una capacidad de entrega del 100 %.

## Disponibilidad regional {#regional-availability}

La disponibilidad y las capacidades de optimización de la entrega optimizada dependen de la región del número de teléfono de la empresa y del usuario. Para obtener más información, consulta [Disponibilidad geográfica de características](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features).

## Configuración de la entrega optimizada {#setting-up-optimized-delivery}

1. En Braze, ve a **Partner Integrations** > **Technology Partners** > **WhatsApp**.
2. En la sección **Optimize your sending with optimized delivery**, selecciona **Upgrade setting** para activar el [flujo de trabajo de registro integrado]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup).

![La sección de integración de mensajería de WhatsApp con una opción para optimizar el envío con entrega optimizada.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3. Una vez habilitada la entrega optimizada, los detalles de tu cuenta en **WhatsApp Business Account Management** mostrarán el estado de la entrega optimizada.

![Sección de administración de cuenta de WhatsApp Business con un grupo de suscripción listado que tiene un estado de número activo.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

Alternativamente, puedes habilitar la entrega optimizada directamente en tu administrador de WhatsApp y luego comenzar a enviar en Braze.

### Solución de problemas de configuración {#troubleshooting-your-setup}

- **Error general:** Si algo sale mal durante la actualización, se mostrará este banner de error y se te aconsejará [contactar con Soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).
- **Error de no elegible:** Si estás restringido por Meta, se mostrará este banner de error: "At least one WhatsApp Business Account is restricted by Meta. Accounts must be in good standing to upgrade." Este no se puede descartar hasta que se resuelva el problema.

## Uso de la entrega optimizada en Campaigns y Canvas {#using-optimized-delivery-in-campaigns-and-canvases}

La entrega optimizada debe usarse para **mensajes de marketing**. Braze eliminará automáticamente la opción de entrega optimizada para **mensajes de utilidad, autenticación, servicio y respuesta**, que deben seguir enviándose a través de la API en la nube, que es la configuración predeterminada.

### Selección del método de entrega {#selecting-the-delivery-method}

1. En el creador de WhatsApp de Braze para una Campaign o un paso de mensaje de Canvas, ve a la pestaña **Settings**.
2. En la sección **Delivery method**, la casilla de verificación de **Optimized Delivery (Recommended)** estará marcada de forma predeterminada si tu cuenta de WhatsApp Business (WABA) está habilitada. Si no deseas usar la entrega optimizada para ese mensaje específico, desmarca la casilla.
- Si seleccionas la entrega optimizada pero no está disponible, el mensaje recurrirá automáticamente al método de API en la nube.

![Creador de mensajes con una pestaña de vista previa que tiene una casilla de verificación para seleccionar la entrega optimizada.]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})

### Reorientar usuarios en otros canales de Braze {#retargeting-users-on-other-braze-channels}

Dado que la API de MM para WhatsApp no ofrece un 100 % de capacidad de entrega, es importante entender cómo reorientar a los usuarios que pueden no haber recibido tu mensaje en otros canales.

Para reorientar usuarios, recomendamos crear un segmento de usuarios que no recibieron un mensaje específico. Para hacerlo, filtra por el código de error `131049`, que indica que un mensaje de plantilla de marketing no se envió debido a la aplicación del límite de plantilla de marketing por usuario de WhatsApp. Puedes hacerlo usando Braze Currents o extensiones de segmento SQL:

- **Braze Currents:** Exporta los eventos de error en mensajes usando Braze Currents. Luego puedes usar estos datos para actualizar un atributo personalizado en el perfil de usuario (como `whatsapp_failed_last_msg: true`), que puedes usar como filtro para tu Campaign de reorientación.
- **Extensiones de segmento SQL:** Si tienes acceso a esta característica, puedes usar SQL para consultar los registros de errores en mensajes y crear un segmento de esos usuarios, y luego segmentar ese segmento en un canal diferente.