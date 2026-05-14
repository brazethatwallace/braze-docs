---
nav_title: Acceder a tu cuenta
article_title: Acceder a tu cuenta
page_order: 0
page_type: reference
description: "Este artículo explica cómo obtener tu cuenta de Braze, cómo iniciar sesión una vez que se te haya concedido acceso y cómo solucionar problemas de acceso y rendimiento del dashboard."

---

# Acceder a tu cuenta {#access-your-account}

> Este artículo explica cómo obtener tu cuenta de Braze, cómo iniciar sesión una vez que se te haya concedido acceso y cómo solucionar problemas de acceso y rendimiento del dashboard.

Si eres el primer usuario de Braze de tu empresa e inicias sesión por primera vez, recibirás un correo electrónico de bienvenida de `@alerts.braze.com` pidiéndote que confirmes tu correo electrónico e inicies sesión el primer día de tu contrato.

Después de confirmar tu cuenta, puedes añadir usuarios adicionales desde la página [Usuarios de la empresa]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/) de tu dashboard. Todos los usuarios recibirán un correo electrónico pidiéndoles que confirmen su cuenta después de haber sido añadidos.

Si no eres el primer usuario en la cuenta de Braze de tu empresa, ponte en contacto con el administrador de la cuenta de Braze de tu empresa y pídele que cree tu cuenta. Entonces recibirás un correo electrónico de bienvenida de `@alerts.braze.com` pidiéndote que confirmes tu correo electrónico e inicies sesión.

## Iniciar sesión {#logging-in}

Ya sea tu primera vez iniciando sesión o la centésima, así es como accedes a tu dashboard. Si eres el primer usuario de tu empresa, sigue las indicaciones de la sección anterior. De lo contrario, puedes iniciar sesión después de que el administrador de Braze de tu empresa cree tu cuenta.

Puedes iniciar sesión desde el sitio principal de [Braze.com](https://www.braze.com), o usar la URL de tu dashboard que corresponde a tu [instancia de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/) específica. Para tu comodidad, Braze ofrece varias opciones de inicio de sesión único (SSO), como:

* [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/)
    * [Aprovisionamiento justo a tiempo de SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning/)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso/)
* [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta/)
* [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin/)

Después de iniciar sesión en Braze con SSO, ya no podrás usar tu contraseña para iniciar sesión en el dashboard. Ambas direcciones de correo electrónico dirigirán los correos al mismo buzón de entrada, pero Braze las reconocerá como cuentas separadas cuando inicies sesión. Borrar las cookies cerrará tu sesión, por lo que se perderá el trabajo no guardado.

## Navegadores compatibles {#supported-browsers}

El dashboard de Braze es compatible con los siguientes navegadores:
- Chrome (versión 87 o posterior)
- Firefox (versión 85 o posterior)
- Safari (versión 15.4 o posterior)
- Edge (versión 87 o posterior)

Si tu dashboard de Braze muestra un error inesperado y la herramienta de consola de tu navegador muestra el error `ReferenceError: structuredClone is not defined`, tu navegador está desactualizado. Si este error sigue ocurriendo, desinstala y reinstala tu navegador.

## Acceder a múltiples dashboards de Braze {#accessing-multiple-braze-dashboards}

Braze no te permite registrar la misma dirección de correo electrónico para múltiples usuarios del dashboard en el mismo clúster (por ejemplo, si tienes dos dashboards en US-01). Puedes usar el mismo correo electrónico para crear cuentas en diferentes clústeres (por ejemplo, si tienes un dashboard en US-01 y otro en US-05). Si necesitas acceder a múltiples dashboards de Braze en el mismo clúster, puedes hacer lo siguiente:

### Usar alias de correo electrónico {#use-email-aliases}

Si tu proveedor de correo electrónico es Gmail, puedes crear alias añadiendo un signo `+` seguido de cualquier texto a tu dirección de correo electrónico. Por ejemplo:
- **Correo electrónico original:** `rocky@gmail.com`
- **Correo electrónico alias:** `rocky+1@gmail.com`

Ambas direcciones de correo electrónico dirigen los correos al mismo buzón de entrada, pero Braze las reconoce como cuentas separadas cuando inicias sesión.

### Crear alias separados con otros proveedores {#create-separate-aliases-with-other-providers}

Si tu proveedor de correo electrónico no admite alias con `+`, puedes crear alias separados, como configurar `rocky@braze.com` para que reenvíe a `rocky.lotito@braze.com`. Esto permite que múltiples direcciones se canalicen al mismo buzón de entrada mientras Braze las reconoce como correos electrónicos diferentes.

### Usar desarrolladores multiempresa {#use-multi-company-developers}

La característica de desarrolladores multiempresa permite compartir una única cuenta de usuario entre múltiples empresas. Los usuarios pueden alternar entre diferentes dashboards de empresa desde su menú de perfil de usuario.

Si tienes SSO y quieres configurar desarrolladores multiempresa, necesitas habilitar un ID de entidad SAML personalizado configurando una integración SAML SSO personalizada. Sigue los pasos en [Inicio de sesión iniciado por el proveedor de servicios (SP)]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/), pero aplica estos cambios:
- Cambia el **Entity ID** a `braze_dashboard_<companyID>` para cada integración de dashboard.
- Ponte en contacto con tu administrador del éxito del cliente o director de cuentas para habilitar el feature flipper `saml_sso_custom_entity_id` para cada dashboard.

### Consideraciones para el inicio de sesión único (SSO) {#considerations-for-single-sign-on-sso}

Si usas inicio de sesión único (SSO), ten en cuenta que tener múltiples direcciones de correo electrónico diferentes podría generar complicaciones. Confirma que tu configuración de SSO esté correctamente establecida para evitar problemas de acceso.

## Solución de problemas {#troubleshooting}

### Restablecer tu contraseña {#resetting-your-password}

Para restablecer tu contraseña, selecciona el enlace **Forgot your password?** en la página de inicio de sesión del dashboard. Se te pedirá que introduzcas tu correo electrónico para recibir un enlace para restablecer tu contraseña.

![Inicio de sesión del dashboard con el mensaje "Forgot your password?".]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Borrar la caché y las cookies de tu navegador {#clearing-your-browser-cache-and-cookies}

Si tienes problemas con el rendimiento del dashboard, como que tu dashboard o la lista de rendimiento de segmentos no se carguen, intenta borrar la caché y las cookies de tu navegador siguiendo los pasos para tu navegador correspondiente.

{% alert important %}
Borrar las cookies cierra tu sesión, por lo que se perderá el trabajo no guardado.
{% endalert %}

- [Borrar caché y cookies en Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Borrar cookies en Safari en Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Borrar cookies y datos de sitios en Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Eliminar todas las cookies en Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Si borrar la caché y las cookies de tu navegador no resuelve tus problemas, ponte en contacto con [Soporte]({{site.baseurl}}/support_contact/).

### Error "Aw, Snap!" en Google Chrome {#aw-snap-error-in-google-chrome}

Si Google Chrome muestra un error "Aw, Snap!", Chrome tiene problemas para cargar la página del dashboard de Braze. Para conocer los pasos de solución de problemas, consulta [Obtener ayuda con mensajes de error comunes en Chrome](https://support.google.com/chrome/answer/95669?co=GENIE.Platform%3DDesktop&hl=en).

### "Please Refresh Page" o "Unexpected Error" al navegar por el dashboard {#please-refresh-page-or-unexpected-error-while-navigating-the-dashboard}

Este error puede aparecer cuando un usuario de la empresa no pertenece a ningún espacio de trabajo. Para solucionarlo:

1. Ve a la página [Usuarios de la empresa]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/).
2. Comprueba si el usuario ha sido añadido a un espacio de trabajo.
3. Si no forma parte de ningún espacio de trabajo, añádelo y asigna los permisos correspondientes.
4. Pide al usuario que actualice su dashboard.
5. Si el problema persiste, ponte en contacto con [Soporte]({{site.baseurl}}/support_contact/).

### Acceder al editor de arrastrar y soltar {#accessing-the-drag-and-drop-editor}

Para la mayoría de los usuarios de la empresa, el editor de arrastrar y soltar debería cargarse. Sin embargo, si estás usando una VPN o estás detrás de un firewall, es posible que necesites añadir un dominio a la lista de permitidos. Ponte en contacto con tu administrador de TI para verificar que `*.bz-rndr.com` esté en la lista de permitidos.

El editor puede experimentar problemas de carga debido a lo siguiente:

- **Error transitorio:** Son fallos temporales que pueden afectar la conectividad, la comunicación o la transferencia de datos. Afortunadamente, suelen resolverse por sí solos sin requerir una intervención significativa, ya que a menudo son causados por condiciones de corta duración y no indican problemas sistémicos.
- **Error grave:** Puede involucrar un problema subyacente de infraestructura o producto. Puedes consultar nuestra [página de estado del sistema de Braze](https://braze.statuspage.io/) ya que probablemente estemos al tanto de la situación y trabajando activamente para resolverla.

{% alert important %}
Si sigues experimentando problemas, [abre un ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support/). Antes de hacerlo, verifica que tu administrador de TI haya confirmado que `*.bz-rndr.com` esté en la lista de permitidos de tu lado.
{% endalert %}

### Acceder a Braze Learning {#accessing-braze-learning}

Si tienes problemas para iniciar sesión en Braze Learning y te encuentras atrapado en un bucle que te redirige al dashboard, sigue estos pasos:

1. Si tienes múltiples cuentas de Braze, iniciar sesión con la cuenta incorrecta dos veces te envía al dashboard de Braze. Confirma que estás iniciando sesión en la cuenta correcta.
2. Si tienes un bloqueador de anuncios, confirma que esté desactivado. Puede bloquear las cookies necesarias para la funcionalidad de inicio de sesión único.
3. Ve a **Company Settings** > **Security Settings** y verifica que el inicio de sesión único (SSO) esté activado.
4. Confirma que tu perfil de usuario del dashboard incluya tanto un nombre como un apellido. No tener un apellido puede interrumpir el proceso de inicio de sesión.
5. Accede a Braze Learning desde tu dashboard yendo a **Support** > **Braze Learning**.
6. Si sigues experimentando problemas, considera volver a crear tu cuenta. Los usuarios que accedieron a Braze Learning durante la fase de prueba gratuita pueden tener dificultades para acceder ahora.

### Problemas con la autenticación de dos factores (2FA) {#two-factor-authentication-2fa-issues}

Si un usuario tiene problemas con la autenticación de dos factores (2FA) y no puede acceder al dashboard de Braze, puede deberse a varias razones. Lo más común es que ya no tenga acceso al número de teléfono registrado o al dispositivo donde está instalada la aplicación Authy.

Un administrador debe restablecer la 2FA para el usuario afectado haciendo lo siguiente:

1. Ve a **Manage Users**.
2. Selecciona **Edit User** para el usuario que tiene problemas con la 2FA.
3. Elige la opción para restablecer la 2FA.
4. Confirma el restablecimiento de la 2FA cuando se te solicite.
5. Si el restablecimiento no resuelve el problema de inmediato, borra tus cookies y caché.

Braze no puede restablecer la 2FA en nombre de los usuarios por razones de seguridad, por lo que si el administrador no puede restablecer la 2FA, crea un ticket de soporte.

#### Consideraciones {#considerations}

- Si la 2FA se aplica a nivel de empresa: después del restablecimiento, Braze solicita al usuario que configure su 2FA de nuevo la próxima vez que inicie sesión.
- Si la 2FA no se aplica a nivel de empresa: el usuario inicia sesión en el dashboard sin necesidad de configurar la 2FA de nuevo. Si desea habilitar la 2FA, puede hacerlo en Configuración de cuenta.

{% alert note %}
Este proceso de restablecimiento también se aplica a los usuarios que han sido bloqueados de su cuenta por solicitar demasiados tokens en la última hora.
{% endalert %}

### Bloqueado de la cuenta {#locked-out-of-account}

Si estás bloqueado de tu cuenta de Braze, puedes volver a acceder siguiendo los pasos a continuación.

Puedes identificar qué tipo de bloqueo estás experimentando por el mensaje de error que recibes:

- [Veo un error sobre mi contraseña.](#password-error)
- [No veo un error, pero Braze aún no me deja entrar.](#instance-error)
- [Veo un error sobre la suspensión de la cuenta.](#account-suspension)

#### Error de contraseña {#password-error}

La seguridad de tu cuenta es importante para nosotros, por lo que se requieren contraseñas para iniciar sesión en tu cuenta de Braze.
- Verifica que estás iniciando sesión en la [instancia correcta del dashboard de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/). Consulta con tu administrador de cuenta o director de cuentas de Braze para asegurarte.
- Tu contraseña puede haber expirado, por lo que necesitas [restablecerla](#resetting-your-password).
- Si usas un servicio de [inicio de sesión único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/), consulta con tu administrador de cuenta que la configuración se haya completado correctamente.
- Si tu empresa está en varias instancias de Braze, es posible que estés usando el correo electrónico incorrecto para iniciar sesión.

En caso de duda, siempre puedes [restablecer tu contraseña](#resetting-your-password).

#### Error de instancia {#instance-error}

Si estás usando la misma máquina que usas habitualmente para iniciar sesión, Braze debería detectar automáticamente la instancia correcta. Sin embargo, si no lo hace o estás iniciando sesión por primera vez, considera lo siguiente:

- Verifica que estás iniciando sesión en la [instancia correcta del dashboard de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/). Consulta con tu administrador de cuenta o director de cuentas de Braze para asegurarte.
- Si tu empresa está en varias instancias de Braze, es posible que estés usando el correo electrónico incorrecto para iniciar sesión.

#### Suspensión de cuenta {#account-suspension}

Esto no ocurre muy a menudo, pero Braze se toma muy en serio la suspensión y eliminación de cuentas. Si encuentras este error, ponte en contacto con el administrador de Braze de tu empresa, tu director de cuentas de Braze o [Soporte][support].

### El dashboard de Braze no carga o no funciona como se espera {#braze-dashboard-wont-load-or-work-as-expected}

Primero, prueba si el dashboard carga en un navegador diferente. Si el problema no persiste en un navegador diferente, intenta lo siguiente:

- **Reinicia el dashboard:** Cierra sesión, cierra tu navegador y luego intenta iniciar sesión en tu dashboard.
- **Actualiza tu navegador local:** [Borra tus cookies y la caché del navegador](#clearing-your-browser-cache-and-cookies) y luego intenta iniciar sesión en tu dashboard de nuevo.
- **Usa complementos o herramientas de terceros compatibles:** Los bloqueadores de anuncios o el software de seguridad pueden impedir que el dashboard de Braze se cargue. Prueba esto desactivando un bloqueador de anuncios y luego iniciando sesión en tu dashboard de Braze.
        - También puedes revisar los registros de la consola de tu navegador. Los errores relacionados con `ERR_BLOCKED_BY_CLIENT` pueden indicar que el contenido está siendo bloqueado por un bloqueador de anuncios.
- **Verifica la calidad de tu conexión:** La calidad de tu conexión puede ser deficiente. Intenta iniciar sesión en tu dashboard de Braze desde un dispositivo diferente.
- **Confirma que estás accediendo al clúster correcto:** Asegúrate de que estás iniciando sesión en el clúster asignado a tu empresa. Por ejemplo, puede que estés asignado a US-03, pero estés iniciando sesión en US-01.
- **Actualiza tu navegador:** Actualiza tu navegador a la última versión de [navegador compatible](#supported-browsers) y luego intenta iniciar sesión en tu dashboard.

Si el problema ocurre en todos los navegadores, intenta lo siguiente:

- **Verifica tu conexión de red:** Intenta desactivar tu VPN, si es posible, o desactiva y vuelve a activar tu conexión de red.
- **Reinicia tu dispositivo:** Intenta iniciar sesión en tu dashboard de Braze después de reiniciar tu dispositivo.

Si has resuelto los problemas anteriores y tu dashboard aún no carga o no funciona como se espera, ponte en contacto con [Soporte]({{site.baseurl}}/braze_support/).

### El usuario no pertenece a ningún espacio de trabajo {#the-user-belongs-to-no-workspace}

Verifica esto yendo a **Settings** > **Company Users** y comprobando los permisos a nivel de espacio de trabajo del usuario. Añade los espacios de trabajo necesarios a **Workspaces**.

### Solución de problemas como usuario nuevo {#troubleshooting-as-a-new-user}

Si eres un nuevo usuario de Braze y tienes problemas para iniciar sesión o acceder a tu cuenta por primera vez, sigue estos pasos para resolver problemas comunes:

#### Nunca recibí el correo electrónico de bienvenida {#i-never-received-the-welcome-email}

- Revisa tu carpeta de correo no deseado: confirma que el correo electrónico de activación de la cuenta no fue filtrado a tu carpeta de correo no deseado.
- Verifica tu dirección de correo electrónico: pide a tu administrador que compruebe la dirección de correo electrónico asociada a tu nueva cuenta de Braze para confirmar que es correcta.
- Políticas de TI: confirma con tu equipo de TI que no haya políticas que puedan impedir la recepción del correo electrónico de activación.

#### Recibí el correo electrónico, pero estoy atascado configurando la autenticación de dos factores (2FA) {#i-received-the-email-but-im-stuck-setting-up-two-factor-authentication-2fa}

- Restablecer la 2FA: si tienes problemas para configurar la 2FA, tu administrador puede restablecer la 2FA para tu cuenta de usuario en la configuración.
- Volver a añadir al usuario: si los problemas persisten, el administrador puede eliminar tu cuenta de usuario del dashboard y volver a añadirte. Esto permite la creación del usuario con los mismos datos.

Si los problemas continúan después de estos pasos, ponte en contacto con [Soporte]({{site.baseurl}}/braze_support/) para obtener más ayuda.

## Próximos pasos {#next-steps}

Después de acceder a tu cuenta, explora estos recursos:

- [El dashboard de Braze]({{site.baseurl}}/user_guide/administer/personal/the_braze_dashboard/) para aprender a navegar por las características y herramientas clave.
- [Configuración de idioma]({{site.baseurl}}/user_guide/administer/personal/language_settings/) para establecer tu idioma preferido del dashboard.