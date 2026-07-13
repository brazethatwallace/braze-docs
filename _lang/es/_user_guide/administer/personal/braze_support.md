---
nav_title: Soporte de Braze
article_title: Soporte de Braze
page_order: 4
description: "Esta página te ayudará a localizar el portal de soporte de Braze para enviar comentarios sobre el producto Braze. Esta página solo será accesible para clientes de Braze."
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"}Soporte de Braze {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomthe-braze-support-portal-stylefloatrightwidth120pxborder0-classnoimgborderbraze-support}

> Aprende a acceder al portal de soporte de Braze, enviar y hacer seguimiento de casos de soporte, y proporcionar la información necesaria para una solución de problemas eficiente.

## Acceder al portal de soporte {#access-the-support-portal}

Para ponerte en contacto con el equipo de soporte de Braze, navega al panel de Braze y selecciona **Support** > **Get help with Operator** > **Contact Support**.

Esto abre BrazeAI Operator<sup>TM</sup> con la opción de enviar un ticket de soporte directamente. Operator puede solucionar tu problema utilizando el contexto de tu conversación y la pantalla actual. Si Operator no puede resolver tu problema, puedes pedirle que redacte un ticket de soporte basado en tu conversación, y luego enviar el ticket en el portal de soporte de Braze (si eres un contacto de soporte designado) o a través de nuestro formulario de soporte estándar.

Para más información, consulta [enviar tickets de soporte con BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets). Si no estás seguro de si eres un contacto de soporte de Braze, ponte en contacto con el administrador de Braze de tu empresa, tu gestor de éxito de Braze o el propietario de la cuenta.

![El menú desplegable "Support" mostrando "Get help with Operator".]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:50%;"}


## Añadir contactos de soporte designados {#adding-designated-support-contacts}

Los contactos de soporte designados pueden acceder a todos los casos de soporte de tu empresa, independientemente de quién los haya enviado. Puedes configurar usuarios como contactos de soporte designados directamente desde la página **Edit user**.

1. Ve a **Configuración** > **Usuarios de la empresa** y busca al usuario por su nombre o dirección de correo electrónico.
2. Selecciona el nombre del usuario o pasa el cursor sobre la fila del nombre del usuario para mostrar un menú.
3. En el menú, selecciona **Edit** para ser redirigido a la página **Edit user**.
4. Marca la casilla de verificación **Set this user as a Designated Support Contact for Braze Support Portal**.

### Obtener acceso {#gaining-access}

Después de que un usuario sea designado como contacto de soporte, el portal de soporte de Braze envía a ese usuario un correo electrónico de bienvenida con instrucciones para configurar su acceso.

## Ver casos de tu empresa {#view-cases-from-your-company}

Si eres un contacto de soporte designado, usa las vistas de filtro **My Org's** en el portal de soporte para ver todos los casos enviados por usuarios de tu empresa. Los casos de todos los canales de envío (BrazeAI Operator<sup>TM</sup>, formulario web, correo electrónico o portal) están incluidos en estas vistas.

## Mejores prácticas para enviar un caso de soporte {#best-practices-for-submitting-a-support-case}

### Proporciona la mayor cantidad de información posible {#provide-as-much-information-as-possible}

Cuanta más información puedas ofrecer, mejor. Incluye detalles específicos como el espacio de trabajo, la URL de la Campaign o el Segment, y cualquier ID externo relevante. Esto puede ayudarnos a solucionar tu problema de manera más eficiente.

### Proporciona una muestra de usuarios {#provide-a-sample-of-users}

Comparte una muestra de usuarios en lugar de todo el segmento afectado. Proporcionar un número menor de usuarios nos ayuda a reducir el alcance y acelerar nuestras investigaciones.

### Aclara el comportamiento esperado frente al real {#clarify-expected-versus-actual-behavior}

Haznos saber qué esperabas y qué sucedió realmente. Esto puede ayudarnos a reducir las posibles causas del problema.

### Adjunta imágenes relevantes {#attach-relevant-images}

Considera adjuntar una captura de pantalla para ilustrar el problema. Proporcionar estas imágenes puede ayudar significativamente a nuestra comprensión del problema y acelerar el proceso de resolución.

### Evalúa el impacto {#assess-the-impact}

Selecciona el nivel de gravedad apropiado para ayudarnos a asignar los recursos adecuados para abordar el problema.

{% alert important %}
Marcar un problema como "Crítico" significa que tu instancia de producción está caída y todo el trabajo dentro de Braze se ha detenido.
{% endalert %}

## Solución de problemas de carga del panel {#troubleshooting-dashboard-load-issues}

Si el panel de Braze no se carga correctamente, prueba lo siguiente antes de ponerte en contacto con soporte:

1. Abre el panel en un navegador diferente o en una ventana de incógnito o privada.
2. [Borra la caché y las cookies de tu navegador]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#clearing-your-browser-cache-and-cookies).
3. Desactiva los bloqueadores de anuncios y las extensiones del navegador, y luego recarga el panel.
4. Si usas una VPN, desconéctala e inténtalo de nuevo.

Si la consola para desarrolladores de tu navegador muestra `ERR_BLOCKED_BY_CLIENT`, una extensión o bloqueador de anuncios está bloqueando los recursos del panel. Desactiva el bloqueador para la URL de tu panel de Braze y recarga la página.

## Solución de problemas de acceso {#troubleshooting-access}

Si recibes un error al iniciar sesión en el portal de soporte de Braze, como `Check your entry`, asegúrate de haber seguido el enlace en tu correo electrónico de bienvenida para establecer una contraseña para el portal. Si ya lo hiciste o anteriormente podías iniciar sesión en el portal, crea un ticket de soporte.