---
nav_title: Registro integrado
article_title: Registro integrado de WhatsApp
page_order: 1
description: "Este artículo de referencia ofrece un recorrido paso a paso del flujo de trabajo de registro integrado de WhatsApp en Braze."
page_type: reference
channel:
  - WhatsApp
---

# Registro integrado de WhatsApp {#whatsapp-embedded-signup}

> Este artículo de referencia ofrece un recorrido paso a paso del flujo de trabajo de registro integrado de WhatsApp en Braze.

Se accede al flujo de trabajo de registro integrado de WhatsApp cuando [integras WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/) por primera vez en tu espacio de trabajo de Braze, y cuando [añades una cuenta de WhatsApp Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/) a una integración de WhatsApp existente.

{% alert note %}
Puedes añadir [múltiples cuentas de WhatsApp Business]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/) a un espacio de trabajo de Braze. Sin embargo, cada cuenta de WhatsApp Business específica solo puede añadirse a un único espacio de trabajo de Braze.
{% endalert %}

## Acceder al flujo de trabajo {#accessing-the-workflow}

Ve a **Integraciones de socios** > **Socios tecnológicos**, luego busca y selecciona **WhatsApp**. Tu siguiente selección depende de tu caso de uso:

- Si estás integrando WhatsApp en tu espacio de trabajo, selecciona **Begin Integration**. <br><br>![Página del socio WhatsApp con un botón para iniciar la integración.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:80%;"}<br><br>
- Si estás añadiendo una cuenta de WhatsApp Business a una integración de WhatsApp existente, selecciona **Add WhatsApp Business Account**. <br><br>![«WhatsApp Messaging Integration» con opciones para añadir una cuenta de WhatsApp Business o un grupo de suscripción y número.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %}){: style="max-width:80%;"}

El flujo de trabajo a partir de aquí es el mismo para ambos casos de uso.

## Flujo de trabajo de registro integrado de WhatsApp {#whatsapp-embedded-signup-workflow}

1. En la ventana de inicio de sesión de Meta (Facebook), selecciona **Login as** o **Continue**. <br><br>![Ventana de inicio de sesión de Meta.]({% image_buster /assets/img/whatsapp/login_screen.png %}){: style="max-width:60%;"}<br><br>
2. Lee los permisos que compartirás con Braze y luego selecciona **Get Started**. <br><br>![Lista de permisos que compartirás con Braze para la integración.]({% image_buster /assets/img/whatsapp/get_started.png %}){: style="max-width:50%;"}<br><br>
3. En esta pantalla, configura lo siguiente y luego selecciona **Next**:
- En el desplegable **Business portfolio**, selecciona tu portafolio de empresa. Esto se conecta a tu cuenta de WhatsApp Business, así que si no ves el portafolio de empresa esperado, verifica tus permisos.
- En el campo **WhatsApp business account**, selecciona **Create a new WhatsApp Business Account**, incluso cuando estés añadiendo otra cuenta de WhatsApp Business a tu espacio de trabajo o cuando esa cuenta ya exista en Meta. Elige esta opción en lugar de seleccionar una cuenta de WhatsApp Business existente del desplegable. <br><br>![Una ventana con campos para introducir la información de tu empresa, incluido el nombre del portafolio de empresa.]({% image_buster /assets/img/whatsapp/business_info.png %}){: style="max-width:50%;"}<br><br>
4. Selecciona lo siguiente en los campos desplegables y luego selecciona **Next**.
- **Choose a WhatsApp Business account**: Crear una cuenta de WhatsApp Business
- **Create or select a WhatsApp Business profile**: Crear un nuevo perfil de WhatsApp Business <br><br>![Campos para especificar si estás eligiendo o creando una cuenta y perfil de WhatsApp Business.]({% image_buster /assets/img/whatsapp/create_select_waba.png %}){: style="max-width:50%;"}<br><br>
5. Proporciona lo siguiente y luego selecciona **Next**.
- Nombre de la cuenta de WhatsApp Business
- Nombre de visualización de WhatsApp Business
- Categoría <br><br>![Campos para proporcionar detalles de la nueva cuenta de WhatsApp Business.]({% image_buster /assets/img/whatsapp/waba_details.png %}){: style="max-width:50%;"}<br><br>
6. Introduce tu número de teléfono y elige **Text message** o **Phone call**. Para un número nuevo, el número debe cumplir con los requisitos de número de teléfono de WhatsApp, incluido no estar registrado en ninguna otra cuenta de WhatsApp. Si estás migrando un número existente (consulta el paso 3) y Meta muestra que el número ya está en uso, continúa más allá de la advertencia para finalizar la migración. <br><br>![Campos para añadir un número de teléfono.]({% image_buster /assets/img/whatsapp/add_phone_number.png %}){: style="max-width:50%;"}<br><br>
7. Introduce tu código de autenticación de dos factores y luego selecciona **Next**. <br><br>![Un campo de entrada para un código de autenticación de dos factores.]({% image_buster /assets/img/whatsapp/two_factor.png %}){: style="max-width:50%;"}<br><br>
8. Revisa los permisos que recibirá tu cuenta de WhatsApp Business y luego selecciona **Continue**. <br><br>![Lista de permisos solicitados por la cuenta de WhatsApp Business.]({% image_buster /assets/img/whatsapp/permissions.png %}){: style="max-width:50%;"}<br><br>
9. ¡Listo! <br><br>![Ventana que indica que estás listo para empezar a enviar mensajes.]({% image_buster /assets/img/whatsapp/finish.png %}){: style="max-width:50%;"}