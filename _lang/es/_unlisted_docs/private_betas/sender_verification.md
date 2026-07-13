---
nav_title: "Verificación del remitente"
article_title: "Verificación del remitente"
permalink: /sender_verification/
description: "Este artículo explica cómo configurar la verificación del remitente y delegar tus propios subdominios a Braze."
hidden: true
---

# Verificación del remitente {#sender-verification}

> Esta página explica cómo delegar tus propios subdominios a Braze. Usa la verificación del remitente para configurar y delegar el control de un subdominio de envío dedicado a Braze, lo que permite una mayor consistencia de marca con tu dominio de remitente y los enlaces de seguimiento bajo el mismo subdominio.

{% alert important %}
Esta característica está en beta y solo está disponible para equipos internos de Braze.
{% endalert %}

## Cómo funciona la verificación del remitente {#how-sender-verification-works}

La delegación de dominio es una opción de configuración de DNS que te permite delegar el control de un subdominio de envío específico a Braze. Por ejemplo, si usas "marketing.example.com" como tu subdominio, Braze administra los registros de DNS necesarios para las funciones de mensajería, como el correo electrónico.

### Beneficios {#benefits}

Usar la verificación del remitente ayuda a simplificar la configuración y el mantenimiento. Braze crea y actualiza lo necesario, lo que significa que hay menos oportunidades de errores en la configuración de DNS.

### Consideraciones {#considerations}

- Elige un subdominio dedicado.
- Después de completar la delegación de dominio, Braze administra tus registros de DNS para el subdominio delegado.
- Si tienes múltiples marcas o espacios de trabajo de Braze, puedes seleccionar un subdominio delegado por marca.
- Hay un límite de 50 dominios de envío y 50 dominios de seguimiento para la verificación del remitente. Si necesitas agregar más, comunícate con el equipo de soporte de Braze.

## Paso 1: Completar los requisitos previos {#step-1-complete-prerequisites}

En el dashboard de Braze, ve a **Configuración** > **Verificación del remitente** en **Configuración de empresa** y trabaja con tu administrador de incorporación para completar los siguientes requisitos previos:

- Agregar un pool de IP
- Agregar direcciones IP
- Agregar un dominio delegado y verificar el registro NS

## Paso 2: Agregar tu subdominio de envío {#step-2-add-your-sending-subdomain}

1. En la sección **Dominios de envío**, selecciona **Agregar dominio de envío**.
2. Ingresa los campos **Mail from** y **Dominio de envío** con tu subdominio de envío para el pool de IP. Un ejemplo es "marketing.mail.example.com".
3. Selecciona tu dominio delegado en el menú desplegable.
4. Luego, selecciona **Enviar**.

![Formulario que muestra campos para la dirección Mail from y el dominio de envío, con un menú desplegable de dominio delegado y un botón Enviar.]({% image_buster /assets/unlisted_docs/img/sender_verification/sending_subdomain.png %}){: style="max-width:85%;"}

Los registros de DNS tardan entre 5 y 10 minutos en propagarse. Una vez completado, recibirás un correo electrónico de notificación indicando que tu dominio está listo para usar.

{% alert important %}
Los dominios no se pueden cambiar después de enviarlos. Braze crea registros de DNS para la verificación y autenticación, y los agrega a tu configuración de DNS.
{% endalert %}

## Paso 3: Agregar tu subdominio de seguimiento {#step-3-add-your-tracking-subdomain}

Después de crear un subdominio y verificarlo:

1. Selecciona **Agregar dominio de seguimiento**.
2. Ingresa el subdominio de seguimiento. Por ejemplo, si tu subdominio de seguimiento es "click", tu subdominio sería: "click.marketing.mail.example.com".
3. Selecciona el dominio de envío asociado en el menú desplegable.
4. Luego, selecciona **Enviar**.

![Un ejemplo de dominio de seguimiento a agregar.]({% image_buster /assets/unlisted_docs/img/sender_verification/tracking_domain.png %}){: style="max-width:85%;"}

Estos registros de DNS pueden tardar hasta 24 horas en propagarse, pero generalmente toma menos tiempo. Una vez completado, recibirás un correo electrónico de notificación indicando que tu dominio está listo para usar.

{% alert important %}
El dominio de seguimiento debe ser un subdominio del dominio de envío para una delegación de DNS adecuada.
{% endalert %}

## Paso 4: Seleccionar los espacios de trabajo {#step-4-select-the-workspaces}

A continuación, selecciona los espacios de trabajo que deben tener acceso al dominio y selecciona **Confirmar**. Opcionalmente, puedes agregar automáticamente un dominio de envío a los nuevos espacios de trabajo cuando se creen.

![Cuadro de diálogo que muestra casillas de selección de espacios de trabajo con la opción de agregar automáticamente el dominio de envío a nuevos espacios de trabajo y un botón Confirmar.]({% image_buster /assets/unlisted_docs/img/sender_verification/select_workspaces_domain.png %}){: style="max-width:85%;"}

## Paso 5: Probar el envío de correo electrónico {#step-5-test-your-email-sending}

Cuando los dominios de envío y seguimiento tengan el estado **Listo para usar**, puedes probar el envío de correo electrónico haciendo lo siguiente:

1. En tu espacio de trabajo, ve a **Configuración** > **Configuración del correo electrónico**.
2. Verifica que el nuevo dominio de envío aparezca en la sección **Dirección de nombre para mostrar**.
3. Agrega la dirección de correo electrónico usando el nuevo dominio (como "marketing@marketing.mail.example.com").
4. Selecciona **Guardar**.
5. A continuación, crea una Campaign de correo electrónico de prueba y envíate un correo electrónico para confirmar lo siguiente:
   - Tu correo electrónico se entregó correctamente.
   - La dirección del remitente es correcta.
   - El enlace de seguimiento de clics usa el dominio de seguimiento.
   - Los encabezados de tu correo electrónico se muestran correctamente.