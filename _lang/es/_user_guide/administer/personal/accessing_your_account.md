---
nav_title: Acceder a tu cuenta
article_title: Acceder a tu cuenta
page_order: 0
page_type: reference
description: "Este artículo explica cómo obtener tu cuenta de Braze, cómo iniciar sesión una vez que se te haya concedido acceso y cómo solucionar problemas de acceso y rendimiento del panel."
---

# Acceder a tu cuenta {#access-your-account}

> Este artículo explica cómo obtener tu cuenta de Braze, cómo iniciar sesión una vez que se te haya concedido acceso y cómo solucionar problemas de acceso y rendimiento del panel.

Si eres el primer usuario de Braze de tu empresa e inicias sesión por primera vez, recibirás un correo electrónico de bienvenida de `@alerts.braze.com` pidiéndote que confirmes tu correo electrónico e inicies sesión el primer día de tu contrato.

Después de confirmar tu cuenta, puedes añadir usuarios adicionales desde la página [Usuarios de la empresa]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users) de tu panel. Todos los usuarios recibirán un correo electrónico pidiéndoles que confirmen su cuenta después de haber sido añadidos.

Si no eres el primer usuario en la cuenta de Braze de tu empresa, ponte en contacto con el administrador de la cuenta de Braze de tu empresa y pídele que cree tu cuenta. Entonces recibirás un correo electrónico de bienvenida de `@alerts.braze.com` pidiéndote que confirmes tu correo electrónico e inicies sesión.

## Iniciar sesión {#logging-in}

Ya sea la primera vez que inicias sesión o la centésima, aquí te explicamos cómo acceder a tu panel. Si eres el primer usuario de tu empresa, sigue las instrucciones de la sección anterior. De lo contrario, puedes iniciar sesión después de que el administrador de Braze de tu empresa cree tu cuenta.

Puedes iniciar sesión desde el sitio principal de [Braze.com](https://www.braze.com), o usar la URL de tu panel que corresponde a tu [instancia de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) específica. Para tu comodidad, Braze ofrece varias opciones de inicio de sesión único (inicio de sesión único), como:

* [SAML inicio de sesión único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)
    * [Aprovisionamiento just-in-time de SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning)
* [Microsoft Entra inicio de sesión único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)
* [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)
* [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)

Después de iniciar sesión en Braze con inicio de sesión único, ya no puedes usar tu contraseña para iniciar sesión en el panel. Ambas direcciones de correo electrónico dirigen los correos al mismo buzón de entrada, pero Braze las reconoce como cuentas separadas cuando inicias sesión. Borrar las cookies cierra tu sesión, por lo que se pierde el trabajo no guardado.

## Navegadores compatibles {#supported-browsers}

El panel de Braze es compatible con los siguientes navegadores:
- Chrome (versión 87 o posterior)
- Firefox (versión 85 o posterior)
- Safari (versión 15.4 o posterior)
- Edge (versión 87 o posterior)

Si tu panel de Braze muestra un error inesperado y la herramienta de consola de tu navegador muestra el error `ReferenceError: structuredClone is not defined`, tu navegador está desactualizado. Si este error sigue apareciendo, desinstala y vuelve a instalar tu navegador.

## Acceder a varios paneles de Braze {#accessing-multiple-braze-dashboards}

Braze no te permite registrar la misma dirección de correo electrónico en varios usuarios del panel en el mismo clúster (por ejemplo, si tienes dos paneles en US-01). Puedes usar el mismo correo electrónico para crear cuentas en diferentes clústeres (por ejemplo, si tienes un panel en US-01 y otro en US-05). Si necesitas acceder a varios paneles de Braze en el mismo clúster, puedes hacer lo siguiente:

### Usar alias de correo electrónico {#use-email-aliases}

Si tu proveedor de correo electrónico es Gmail, puedes crear alias añadiendo un signo `+` seguido de cualquier texto a tu dirección de correo electrónico. Por ejemplo:
- **Correo electrónico original:** `rocky@gmail.com`
- **Alias de correo electrónico:** `rocky+1@gmail.com`

Ambas direcciones de correo electrónico dirigen los correos a la misma bandeja de entrada, pero Braze las reconoce como cuentas separadas cuando inicias sesión.

### Crear alias separados con otros proveedores {#create-separate-aliases-with-other-providers}

Si tu proveedor de correo electrónico no admite el uso de alias con `+`, puedes crear alias separados, como configurar `rocky@braze.com` para que reenvíe a `rocky.lotito@braze.com`. Esto permite que varias direcciones lleguen al mismo buzón de entrada y al mismo tiempo Braze las reconozca como correos electrónicos diferentes.

### Usar desarrolladores multiempresa {#use-multi-company-developers}

La característica de desarrolladores multiempresa permite compartir una única cuenta de usuario entre varias empresas. Los usuarios del panel pueden alternar entre diferentes paneles de empresa desde su menú de perfil de usuario.

Si tienes inicio de sesión único y quieres configurar desarrolladores multiempresa, necesitas habilitar un ID de entidad SAML personalizado configurando una integración SAML inicio de sesión único personalizada. Sigue los pasos en [Inicio de sesión iniciado por el proveedor de servicios (SP)]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup), pero aplica estos cambios:
- Cambia el **ID de entidad** a `braze_dashboard_<companyID>` para cada integración de panel.
- Contacta a tu CSM or administrador de éxito de cliente or administrador de éxito de cliente o director de cuentas para habilitar el interruptor de características `saml_sso_custom_entity_id` para cada panel.

#### Autenticación de dos factores (2FA) {#two-factor-authentication-2fa}

El funcionamiento de la 2FA para desarrolladores multiempresa depende de tu método de 2FA:

- **Correo electrónico y servicio de mensajes cortos:** Tu configuración de 2FA se copia a todas las cuentas de desarrollador vinculadas. Después de configurar la 2FA por correo electrónico o servicio de mensajes cortos en una cuenta, el mismo método se aplica en todos tus paneles de empresa.
- **Contraseña de un solo uso basada en tiempo (TOTP):** La configuración de TOTP no se sincroniza entre cuentas. Si usas una aplicación de autenticación, debes configurar un código separado para cada panel en el que inicies sesión directamente.

Cuando cambias entre cuentas desde el panel, solo necesitas completar la 2FA una vez: la primera vez que inicias sesión en cualquier cuenta vinculada durante esa sesión.

### Consideraciones para el inicio de sesión único (inicio de sesión único) {#considerations-for-single-sign-on-sso}

Si usas inicio de sesión único (inicio de sesión único), ten en cuenta que tener varias direcciones de correo electrónico diferentes podría generar complicaciones. Confirma que tu configuración de inicio de sesión único esté correctamente establecida para evitar problemas de acceso.

## Solución de problemas {#troubleshooting}

### Restablecer tu contraseña {#resetting-your-password}

Para restablecer tu contraseña, selecciona el enlace **¿Olvidaste tu contraseña?** en la página de inicio de sesión del panel. Se te pedirá que ingreses tu correo electrónico para recibir un enlace y restablecer tu contraseña.


#### No se recibió el correo electrónico de restablecimiento de contraseña {#password-reset-email-not-received}

Si solicitaste un restablecimiento de contraseña pero no has recibido el correo electrónico, prueba los siguientes pasos de solución de problemas:

{% alert note %}
Si tu empresa aplica el [inicio de sesión único (inicio de sesión único)]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup), la página de inicio de sesión puede no mostrar **¿Olvidaste tu contraseña?** ni enviar correos electrónicos de restablecimiento de contraseña, porque el inicio de sesión con contraseña está deshabilitado. Inicia sesión a través del proveedor de identidad de tu organización o contacta a tu administrador de Braze.
{% endalert %}

1. **Verifica tu dirección de correo electrónico:** Pide a un administrador que compruebe que el correo electrónico de tu cuenta coincide en **Configuración** > **Usuarios de la empresa**. El enlace de restablecimiento se envía al correo electrónico registrado en el sistema.
2. **Revisa las carpetas de correo no deseado y basura:** Busca correos electrónicos de `@alerts.braze.com` en tu carpeta de correo no deseado o basura.
3. **Verifica los filtros de correo electrónico de TI:** Confirma con tu equipo de TI que los correos electrónicos de `@alerts.braze.com` no estén siendo bloqueados o filtrados.
4. **Confirma la instancia correcta del panel:** Asegúrate de que estás solicitando el restablecimiento desde la [instancia correcta del panel de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Consulta con el administrador de tu cuenta o tu director de cuentas de Braze si no estás seguro.
5. **Prueba con un navegador diferente:** Algunas extensiones o configuraciones del navegador pueden interferir con el proceso de restablecimiento de contraseña. Intenta usar un navegador diferente o una ventana de incógnito.

Los enlaces de restablecimiento de contraseña expiran dos horas después de que se envía el correo electrónico. Si tu enlace ha expirado, solicita un nuevo restablecimiento desde la página de inicio de sesión.

Si ninguno de estos pasos funciona, un administrador puede eliminar y recrear tu cuenta de usuario como solución alternativa. Para más información, consulta [Gestionar usuarios de la empresa]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users).

{% alert note %}
Eliminar y recrear una cuenta de usuario restablece sus permisos y puede afectar la atribución de activos para Campaigns, Canvas y otro contenido que anteriormente era propiedad de ese usuario.
{% endalert %}

### Borrar la caché y las cookies de tu navegador {#clearing-your-browser-cache-and-cookies}

Si tienes problemas con el rendimiento del panel, como que tu panel o la lista de rendimiento de Segment no se carguen, intenta borrar la caché y las cookies de tu navegador siguiendo los pasos para tu navegador correspondiente.

{% alert important %}
Borrar las cookies cierra tu sesión, por lo que se perderá el trabajo no guardado.
{% endalert %}

- [Borrar la caché y las cookies en Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Borrar las cookies en Safari en Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Borrar las cookies y datos de sitios en Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Eliminar todas las cookies en Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Si borrar la caché y las cookies de tu navegador no resuelve tus problemas, contacta a [Soporte]({{site.baseurl}}/support_contact).

### Error "Aw, Snap!" en Google Chrome {#aw-snap-error-in-google-chrome}

Si Google Chrome muestra un error "Aw, Snap!", Chrome tiene problemas para cargar la página del panel de Braze. Para pasos de solución de problemas, consulta [Obtener ayuda con mensajes de error comunes en Chrome](https://support.google.com/chrome/answer/95669?co=GENIE.Platform%3DDesktop&hl=en).

### "Please Refresh Page" o "Unexpected Error" al navegar por el panel {#please-refresh-page-or-unexpected-error-while-navigating-the-dashboard}

Este error puede aparecer cuando un usuario de la empresa no pertenece a ningún espacio de trabajo. Para solucionar problemas:

1. Ve a la página de [Usuarios de la empresa]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users).
2. Comprueba si el usuario ha sido añadido a un espacio de trabajo.
3. Si no forma parte de ningún espacio de trabajo, añádelo y asígnale los permisos apropiados.
4. Pide al usuario que actualice su panel.
5. Si el problema persiste, contacta a [Soporte]({{site.baseurl}}/support_contact).

### Acceder al editor de arrastrar y soltar {#accessing-the-drag-and-drop-editor}

Para la mayoría de los usuarios de la empresa, el editor de arrastrar y soltar debería cargarse. Sin embargo, si estás usando una VPN o estás detrás de un firewall, puede que necesites añadir un dominio a la lista de permitidos. Contacta a tu administrador de TI para comprobar que `*.bz-rndr.com` esté en la lista de permitidos.

El editor puede experimentar problemas de carga debido a lo siguiente:

- **Error transitorio:** Estos son fallos temporales que pueden afectar la conectividad, la comunicación o la transferencia de datos. Afortunadamente, por lo general se resuelven por sí solos sin requerir intervención significativa, ya que suelen ser causados por condiciones de corta duración y no indican problemas sistémicos.
- **Error mayor:** Esto puede involucrar un problema subyacente de infraestructura o producto. Puedes consultar nuestra [página de estado del sistema de Braze](https://braze.statuspage.io/) ya que probablemente estemos al tanto de la situación y trabajando activamente para resolverla.

{% alert important %}
Si sigues experimentando problemas, [abre un ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support). Antes de hacerlo, comprueba que tu administrador de TI haya confirmado que `*.bz-rndr.com` esté en la lista de permitidos en tu red.
{% endalert %}

### Acceder a Braze Learning {#accessing-braze-learning}

Si tienes problemas para iniciar sesión en Braze Learning y te encuentras atrapado en un bucle que te redirige al panel, sigue estos pasos:

1. Si tienes varias cuentas de Braze, iniciar sesión con la cuenta incorrecta dos veces te envía al panel de Braze. Confirma que estás iniciando sesión en la cuenta correcta.
2. Si tienes un bloqueador de anuncios, confirma que esté desactivado. Puede bloquear las cookies necesarias para la funcionalidad de inicio de sesión único.
3. Ve a **Configuración** > **Configuración de la empresa** > **Configuración de administrador** > **Configuración de seguridad** y verifica que el inicio de sesión único (inicio de sesión único) esté activado.
4. Confirma que el perfil de usuario de tu panel incluya tanto un nombre como un apellido. No tener un apellido puede interrumpir el proceso de inicio de sesión.
5. Accede a Braze Learning desde tu panel yendo a **Soporte** > **Braze Learning**.
6. Si sigues experimentando problemas, considera recrear tu cuenta. Los usuarios que accedieron a Braze Learning durante la fase de prueba gratuita pueden tener dificultades para acceder ahora.

### Problemas con la autenticación de dos factores (2FA) {#two-factor-authentication-2fa-issues}

Si un usuario experimenta problemas con la autenticación de dos factores (2FA) y no puede acceder al panel de Braze, puede deberse a varias razones. Lo más común es que ya no tenga acceso al número de teléfono registrado o al dispositivo donde está instalada la aplicación Authy.

Un administrador debería restablecer la 2FA para el usuario afectado haciendo lo siguiente:

1. Ve a **Configuración** > **Gestión de usuarios**.
2. Selecciona el usuario que tiene problemas con la 2FA.
3. En **Autenticación de dos factores**, selecciona **Restablecer**.
4. Confirma el restablecimiento de la 2FA cuando se te solicite.
5. Si el restablecimiento no resuelve el problema de inmediato, borra tus cookies y la caché.

Braze no puede restablecer la 2FA en nombre de los usuarios por razones de seguridad, por lo que si el administrador no puede restablecer la 2FA, crea un ticket de soporte.

#### Consideraciones {#considerations}

- Si la 2FA se aplica a nivel de la empresa: Después del restablecimiento, Braze solicita al usuario que configure su 2FA nuevamente la próxima vez que inicie sesión.
- Si la 2FA no se aplica a nivel de la empresa: El usuario inicia sesión en el panel sin necesidad de configurar la 2FA nuevamente. Si desea habilitar la 2FA, puede hacerlo en la configuración de la cuenta.

{% alert note %}
Este proceso de restablecimiento también se aplica a los usuarios que han sido bloqueados de su cuenta por solicitar demasiados tokens en la última hora.
{% endalert %}

### Bloqueado de la cuenta {#locked-out-of-account}

Si estás bloqueado de tu cuenta de Braze, puedes volver a acceder siguiendo estos pasos.

Puedes identificar el tipo de bloqueo que estás experimentando por el mensaje de error que recibes:

- [Veo un error sobre mi contraseña.](#password-error)
- [No veo un error, pero Braze no me deja entrar.](#instance-error)
- [Veo un error sobre la suspensión de la cuenta.](#account-suspension)

#### Error de contraseña {#password-error}

La seguridad de tu cuenta es importante para nosotros, por lo que se requieren contraseñas para iniciar sesión en tu cuenta de Braze.
- Comprueba que estás iniciando sesión en la [instancia correcta del panel de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Consulta con el administrador de tu cuenta o tu director de cuentas de Braze para estar seguro.
- Tu contraseña puede haber expirado, por lo que necesitas [restablecerla](#resetting-your-password).
- Si usas un servicio de [inicio de sesión único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup), consulta con el administrador de tu cuenta que la configuración se haya completado correctamente.
- Si tu empresa está en varias instancias de Braze, puede que estés usando el correo electrónico incorrecto para iniciar sesión.

En caso de duda, siempre puedes [restablecer tu contraseña](#resetting-your-password).

#### Error de instancia {#instance-error}

Si estás usando la misma máquina que usas habitualmente para iniciar sesión, Braze debería detectar automáticamente la instancia correcta. Sin embargo, si no lo hace o estás iniciando sesión por primera vez, ten en cuenta lo siguiente:

- Comprueba que estás iniciando sesión en la [instancia correcta del panel de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Consulta con el administrador de tu cuenta o tu director de cuentas de Braze para estar seguro.
- Si tu empresa está en varias instancias de Braze, puede que estés usando el correo electrónico incorrecto para iniciar sesión.

#### Suspensión de cuenta {#account-suspension}

Esto no sucede con mucha frecuencia, pero Braze toma la suspensión y eliminación de cuentas muy en serio. Si encuentras un error "Account has been banned" al intentar iniciar sesión, tu cuenta del panel está temporalmente suspendida. Esto puede ocurrir por varias razones.

| Razón | Descripción |
| --- | --- |
| Problemas de pago | La cuenta de Braze de tu empresa puede tener problemas de facturación o pago sin resolver. |
| Violaciones de políticas | La cuenta puede haber violado los términos de servicio o las políticas de uso aceptable de Braze. |
| Preocupaciones de seguridad | Una actividad sospechosa puede haber activado una suspensión automática por razones de seguridad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Razón de la suspensión de cuenta" }

Para resolver este problema, contacta al administrador de Braze de tu empresa, tu director de cuentas de Braze o [Soporte]({{site.baseurl}}/support_contact).

### El panel de Braze no carga o no funciona como se espera {#braze-dashboard-wont-load-or-work-as-expected}

Primero, prueba si el panel carga en un navegador diferente. Si el problema no persiste en un navegador diferente, prueba lo siguiente:

- **Reinicia el panel:** Cierra sesión, cierra tu navegador y luego intenta iniciar sesión en tu panel.
- **Actualiza tu navegador local:** [Borra tus cookies y la caché del navegador](#clearing-your-browser-cache-and-cookies) y luego intenta iniciar sesión en tu panel nuevamente.
- **Usa complementos o herramientas de terceros compatibles:** Los bloqueadores de anuncios o el software de seguridad pueden impedir que el panel de Braze se cargue. Prueba esto deshabilitando un bloqueador de anuncios y luego iniciando sesión en tu panel de Braze.
        - También puedes verificar los registros de la consola de tu navegador. Los errores relacionados con `ERR_BLOCKED_BY_CLIENT` pueden indicar que el contenido está siendo bloqueado por un bloqueador de anuncios.
- **Verifica la calidad de tu conexión:** La calidad de tu conexión puede ser deficiente. Intenta iniciar sesión en tu panel de Braze desde un dispositivo diferente.
- **Confirma que estás accediendo al clúster correcto:** Asegúrate de que estás iniciando sesión en el clúster asignado a tu empresa. Por ejemplo, puede que estés asignado a US-03, pero estés iniciando sesión en US-01.
- **Actualiza tu navegador:** Actualiza tu navegador a la última versión de [navegadores compatibles](#supported-browsers) y luego intenta iniciar sesión en tu panel.

Si el problema ocurre en todos los navegadores, prueba lo siguiente:

- **Verifica tu conexión de red:** Intenta desactivar tu VPN, si es posible, o desactiva y vuelve a activar tu conexión de red.
- **Reinicia tu dispositivo:** Intenta iniciar sesión en tu panel de Braze después de reiniciar tu dispositivo.

Si has resuelto los problemas anteriores y tu panel aún no carga o no funciona como se espera, contacta a [Soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### El usuario no pertenece a ningún espacio de trabajo {#the-user-belongs-to-no-workspace}

Los administradores pueden resolver esto yendo a **Configuración** > **Gestión de usuarios**, verificando los permisos a nivel de espacio de trabajo del usuario y añadiendo los espacios de trabajo necesarios a **Espacios de trabajo**.

### Solución de problemas como usuario nuevo {#troubleshooting-as-a-new-user}

Si eres un usuario nuevo de Braze que tiene problemas para iniciar sesión o acceder a tu cuenta por primera vez, sigue estos pasos para resolver problemas comunes:

#### No recibí el correo electrónico de bienvenida {#i-never-received-the-welcome-email}

- Revisa tu carpeta de correo no deseado: Confirma que el correo electrónico de activación de la cuenta no fue filtrado a tu carpeta de correo no deseado o basura.
- Verifica tu dirección de correo electrónico: Pide a tu administrador que compruebe la dirección de correo electrónico asociada a tu nueva cuenta de Braze para confirmar que sea correcta.
- Políticas de TI: Confirma con tu equipo de TI que no haya políticas establecidas que puedan impedir que se reciba el correo electrónico de activación.

#### Recibí el correo electrónico, pero estoy atascado configurando la autenticación de dos factores (2FA) {#i-received-the-email-but-im-stuck-setting-up-two-factor-authentication-2fa}

Si seleccionas **Iniciar configuración** durante la configuración de 2FA pero nunca recibes un código de verificación (por servicio de mensajes cortos o correo electrónico) o no puedes completar la configuración de la aplicación de autenticación, las extensiones del navegador, la configuración de cookies o las restricciones de red pueden estar interfiriendo. Prueba lo siguiente:

- Desactiva los bloqueadores de anuncios y habilita las cookies de terceros: Los bloqueadores de anuncios o las extensiones de privacidad pueden bloquear el flujo de verificación de 2FA. Desactívalos temporalmente y confirma que las cookies de terceros estén habilitadas en la configuración de tu navegador.
- Prueba con un navegador diferente: Cambia a un navegador diferente para descartar problemas específicos del navegador.
- Cambia de red: Si estás en una red corporativa, las políticas de firewall pueden interferir con la configuración de 2FA. Intenta cambiar a una conexión personal o un punto de acceso móvil.
- Instala una aplicación de autenticación antes de la configuración en el navegador: Descarga e instala una aplicación de autenticación (como Authy, Google Authenticator o LastPass Authenticator) en tu dispositivo móvil antes de seleccionar **Aplicación de autenticación** durante la configuración.
- Elimina perfiles de autenticación obsoletos: Si anteriormente iniciaste la configuración de la aplicación de autenticación pero no se completó, elimina los perfiles obsoletos en tu aplicación y vuelve a escanear el código QR.

Si sigues teniendo problemas después de probar estos pasos:

- Restablecer la 2FA: Tu administrador puede restablecer la 2FA para tu cuenta de usuario en la configuración.
- Volver a añadir al usuario: Si los problemas persisten, el administrador puede eliminar tu cuenta de usuario del panel y volver a añadirte. Esto permite la creación del usuario con los mismos datos.

Si los problemas continúan después de estos pasos, contacta a [Soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) para obtener asistencia adicional.

## Próximos pasos {#next-steps}

Después de acceder a tu cuenta, explora estos recursos:

- [El panel de Braze]({{site.baseurl}}/user_guide/administer/personal/the_braze_dashboard) para aprender a navegar por las características y herramientas clave.
- [Configuración de idioma]({{site.baseurl}}/user_guide/administer/personal/language_settings) para establecer tu idioma preferido del panel.