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

Para ponerte en contacto con el equipo de soporte de Braze, navega al dashboard de Braze y selecciona **Support**. El menú ofrece dos opciones:

- **Get help with Operator** abre BrazeAI Operator<sup>TM</sup>, que puede solucionar tu problema en el momento utilizando el contexto de tu conversación y la pantalla actual. Si Operator no puede resolver tu problema, puedes pedirle que redacte un ticket de soporte basado en tu conversación. Para más información, consulta [enviar tickets de soporte con BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets).
- **Get help** te lleva directamente al portal de soporte de Braze (si eres un contacto de soporte designado) o a nuestro formulario de soporte estándar, donde puedes enviar y hacer seguimiento de casos. Si no estás seguro de si eres un contacto de soporte de Braze, ponte en contacto con el administrador de Braze de tu empresa, tu gestor de éxito de Braze o el propietario de la cuenta.

![El menú desplegable "Support" mostrando las opciones "Get help with Operator" y "Get help".]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:50%;"}


## Añadir contactos de soporte designados {#adding-designated-support-contacts}

Los contactos de soporte designados pueden acceder a todos los casos de soporte de tu empresa, independientemente de quién los haya enviado. Puedes configurar usuarios como contactos de soporte designados directamente desde la página **Edit user**.

1. Ve a **Configuración** > **Usuarios de la empresa** y busca al usuario por su nombre o dirección de correo electrónico.
2. Selecciona el nombre del usuario o pasa el cursor sobre la fila del nombre del usuario para mostrar un menú.
3. En el menú, selecciona **Editar** para ser redirigido a la página **Editar usuario**.
4. Marca la casilla de verificación **Set this user as a Designated Support Contact for Braze Support Portal**.

### Obtener acceso {#gaining-access}

Después de que un usuario sea designado como contacto de soporte, el portal de soporte de Braze envía a ese usuario un correo electrónico de bienvenida con instrucciones para configurar su acceso.

## Ver casos de tu empresa {#view-cases-from-your-company}

Si eres un contacto de soporte designado, usa las vistas de filtro **My Org's** en el portal de soporte para ver todos los casos enviados por usuarios de tu empresa. Los casos de todos los canales de envío (BrazeAI Operator<sup>TM</sup>, formulario web, correo electrónico o portal) están incluidos en estas vistas.

## Proporcionar capturas de pantalla de la consola para desarrolladores {#provide-developer-console-screenshots}

Al comunicarte con soporte, es posible que necesites acceder a tu consola para desarrolladores para proporcionar información adicional:
- Chrome
  1. Haz clic derecho en la página web y selecciona **Inspect**.
  2. Selecciona la pestaña **Console** en la ventana que se abre.
  3. Toma una captura de pantalla de la pestaña de la consola.<br><br>
- Firefox
  1. Haz clic derecho en la página web y selecciona **Inspect Element**.
  2. Selecciona la pestaña **Console** en la ventana que se abre.
  3. Toma una captura de pantalla de la pestaña de la consola.<br><br>
- Safari
  1. Ve a Safari en la barra de menú en la parte superior de tu pantalla y luego selecciona **Preferences**.
  2. Selecciona **Advanced** y luego marca la casilla de verificación junto a **Show Develop menu in menu bar**. Después puedes cerrar la ventana.
  3. Haz clic derecho en la página web y selecciona **Inspect Element**.
  4. Selecciona la pestaña **Console** en la ventana que se abre.
  5. Toma una captura de pantalla de la pestaña de la consola.

## Mejores prácticas para enviar un caso de soporte {#best-practices-for-submitting-a-support-case}

### Proporciona la mayor cantidad de información posible {#provide-as-much-information-as-possible}

Cuanta más información puedas ofrecer, mejor. Incluye detalles específicos como el espacio de trabajo, la URL de la campaña o el segmento, y cualquier ID externo relevante. Esto puede ayudarnos a solucionar tu problema de manera más eficiente.

### Proporciona una muestra de usuarios {#provide-a-sample-of-users}

Comparte una muestra de usuarios en lugar de todo el segmento afectado. Proporcionar un número menor de usuarios nos ayuda a reducir el alcance y acelerar nuestras investigaciones.

### Adjunta registros de red (registros HAR) {#attach-network-logs-har-logs}

Si te pones en contacto con soporte, será útil que el usuario afectado recopile registros de red (registros HAR) de su navegador mientras ocurre el problema. Esto mostrará las solicitudes de red entre el navegador y el servidor para los componentes individuales de una página web, así como el dashboard de Braze que el usuario está intentando abrir.

Pide al usuario afectado que haga lo siguiente:

1. Abra sus herramientas de desarrollador. Si usa Chrome, esto se puede hacer con el atajo de teclado `option` + `⌘` + `J` (en macOS). Si usa Windows o Linux, esto se puede hacer con el atajo `shift` + `CTRL` + `J`.
2. Seleccione **Network** > **Fetch/XHR** o **XHR**.
3. Capture una grabación de pantalla o captura de pantalla que muestre **Name**, **Status**, **Size** y **Time** de los elementos.<br><br>![La pestaña "Fetch/XHR" en un navegador Chrome.]({% image_buster /assets/img/network_xhr.png %}){: style="max-width:60%;"}

Luego, adjunta la grabación o captura de pantalla del usuario al ticket de soporte. Esta información puede ayudar a la investigación de soporte.

### Aclara el comportamiento esperado frente al real {#clarify-expected-versus-actual-behavior}

Haznos saber qué esperabas y qué sucedió realmente. Esto puede ayudarnos a reducir las posibles causas del problema.

### Adjunta imágenes relevantes {#attach-relevant-images}

Considera adjuntar una captura de pantalla para ilustrar el problema. Proporcionar estas imágenes puede ayudar significativamente a nuestra comprensión del problema y acelerar el proceso de resolución.

### Evalúa el impacto {#assess-the-impact}

Selecciona el nivel de gravedad apropiado para ayudarnos a asignar los recursos adecuados para abordar el problema.

{% alert important %}
Marcar un problema como "Crítico" significa que tu instancia de producción está caída y todo el trabajo dentro de Braze se ha detenido.
{% endalert %}

## Solución de problemas de carga del dashboard {#troubleshooting-dashboard-load-issues}

Si el dashboard de Braze no se carga correctamente, prueba lo siguiente antes de ponerte en contacto con soporte:

1. Abre el dashboard en un navegador diferente o en una ventana de incógnito o privada.
2. [Borra la caché y las cookies de tu navegador]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#clearing-your-browser-cache-and-cookies).
3. Desactiva los bloqueadores de anuncios y las extensiones del navegador, y luego recarga el dashboard.
4. Si usas una VPN, desconéctala e inténtalo de nuevo.

Si la consola para desarrolladores de tu navegador muestra `ERR_BLOCKED_BY_CLIENT`, una extensión o bloqueador de anuncios está bloqueando los recursos del dashboard. Desactiva el bloqueador para la URL de tu dashboard de Braze y recarga la página.

## Solución de problemas de acceso {#troubleshooting-access}

Si recibes un error al iniciar sesión en el portal de soporte de Braze, como `Check your entry`, asegúrate de haber seguido el enlace en tu correo electrónico de bienvenida para establecer una contraseña para el portal. Si ya lo hiciste o anteriormente podías iniciar sesión en el portal, crea un ticket de soporte.