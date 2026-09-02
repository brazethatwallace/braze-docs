---
nav_title: Configuración de SAML inicio de sesión único
article_title: Configuración de SAML inicio de sesión único
page_order: 0
page_type: tutorial
toc_headers: h2
description: "Este artículo te guiará sobre cómo habilitar el inicio de sesión único SAML para tu cuenta de Braze."
---

# Inicio de sesión iniciado por el proveedor de servicios (SP) {#service-provider-sp-initiated-login}

> Este artículo te guiará sobre cómo habilitar el inicio de sesión único SAML para tu cuenta de Braze y cómo obtener un rastreo SAML.

## Requisitos {#requirements}

Tras la configuración, se te pedirá que proporciones una URL de inicio de sesión y una URL del servicio de consumidor de aserciones (ACS).

| Requisito | Detalles |
|---|---|
| URL del servicio de consumidor de aserciones (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Para dominios de la Unión Europea, la URL de ACS es `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. <br><br> Para algunos IdP, también puede denominarse URL de respuesta, URL de inicio de sesión, URL de audiencia o URI de audiencia. |
| ID de entidad | `braze_dashboard` de forma predeterminada. Si tu IdP requiere un ID de entidad específico de la empresa, habilita **ID de entidad personalizado** en **Configuración de seguridad** y utiliza `braze_dashboard_<companyID>`. |
| Clave de API de RelayState | Ve a **Configuración** > **Configuración y pruebas** > **API e identificadores**, abre la pestaña **Claves de API** y crea una clave de API con permisos `sso.saml.login`. Introduce la clave de API generada como parámetro `RelayState` en tu IdP. Para ver los pasos detallados, consulta [Configurar tu RelayState](#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Configuración de SAML inicio de sesión único {#setting-up-saml-sso}

### Paso 1: Configura tu proveedor de identidad {#step-1-configure-your-identity-provider}

Configura Braze como proveedor de servicios (SP) en tu proveedor de identidad (IdP) con la siguiente información. Además, configura el mapeado de atributos SAML.

{% alert important %}
Si planeas usar Okta como tu proveedor de identidad, asegúrate de utilizar la integración prediseñada que se encuentra en el [sitio de Okta](https://www.okta.com/integrations/braze/).
{% endalert %}

| Atributo SAML | ¿Obligatorio? | Atributos SAML aceptados |
|---|---|---|
| `email` | Obligatorio | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Opcional | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Opcional | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 1: Configura tu proveedor de identidad" }

{% alert note %}
Braze solo requiere `email` en la aserción SAML.
{% endalert %}

### Paso 2: Configura Braze {#step-2-configure-braze}

Cuando termines de configurar Braze en tu proveedor de identidad, este te proporcionará una URL de destino y un certificado `x.509` para introducir en tu cuenta de Braze.

Después de que tu director de cuentas active SAML inicio de sesión único para tu cuenta, ve a **Configuración** > **Configuración de la empresa** > **Configuración de administrador** > **Configuración de seguridad** y cambia la sección de SAML inicio de sesión único a **ACTIVADO**.

En la misma página, introduce lo siguiente:

| Requisito | Detalles |
|---|---|
| Nombre SAML | Aparecerá como el texto del botón en la pantalla de inicio de sesión.<br>Normalmente es el nombre de tu proveedor de identidad, como "Okta". |
| URL de destino | Se proporciona después de configurar Braze dentro de tu IdP.<br> Algunos IdP hacen referencia a esto como la URL de inicio de sesión único o endpoint SAML 2.0. |
| Certificado | El certificado `x.509` proporcionado por tu proveedor de identidad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Configura Braze" }

### ID de entidad personalizado {#custom-entity-id}

De forma predeterminada, Braze utiliza `braze_dashboard` como ID de entidad (también llamado Audience o Audience URI en algunos IdP). Si tu IdP requiere un ID de entidad específico de la empresa:

1. En **Configuración de seguridad**, activa **ID de entidad personalizado**.
2. Copia el ID de entidad generado (`braze_dashboard_<companyID>`).
3. Pega ese valor en el campo de ID de entidad, Audience o Audience URI de tu IdP.
4. Guarda los cambios tanto en Braze como en tu IdP antes de probar el inicio de sesión.

{% alert important %}
Los usuarios no podrán iniciar sesión hasta que el ID de entidad coincida tanto en Braze como en tu IdP. El ID de entidad personalizado requiere configuración adicional en tu proveedor de identidad.
{% endalert %}

Asegúrate de que tu certificado `x.509` siga este formato al añadirlo al panel:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![Configuración de SAML SSO con el interruptor seleccionado.]({% image_buster /assets/img/samlsso.png %})

### Paso 3: Inicia sesión en Braze {#step-3-sign-into-braze}

Guarda tu configuración de seguridad y cierra sesión. Luego, vuelve a iniciar sesión con tu proveedor de identidad.

## Usar un ID de entidad personalizado {#using-a-custom-entity-id}

De forma predeterminada, cada panel de Braze utiliza el ID de entidad compartido `braze_dashboard`. Un ID de entidad personalizado le da a tu panel un identificador único, de modo que tu proveedor de identidad pueda verificar que las solicitudes de inicio de sesión están destinadas a este panel específico. Esto es útil si estás configurando SAML inicio de sesión único en varias empresas de Braze dentro del mismo proveedor de identidad.

Usar un ID de entidad personalizado es opcional. Si no lo habilitas, tu panel seguirá usando `braze_dashboard`.

{% alert warning %}
La [aplicación preconfigurada de Braze en el marketplace de Okta](https://www.okta.com/integrations/braze/) exige el ID de entidad compartido `braze_dashboard` y no es compatible con un ID de entidad personalizado. Si ya tienes SAML inicio de sesión único configurado con la aplicación de Braze en el marketplace de Okta, activar un ID de entidad personalizado sin actualizar el campo de ID de entidad en Okta a través de una aplicación SAML personalizada interrumpirá el inicio de sesión y puede bloquear a los usuarios del panel. Para usar un ID de entidad personalizado con Okta, configura una aplicación SAML personalizada en su lugar.
{% endalert %}

### Paso 1: Activar el ID de entidad personalizado {#step-1-turn-on-the-custom-entity-id}

Ve a **Configuración** > **Configuración de administrador** > **Configuración de seguridad** y abre la sección de inicio de sesión único SAML. Activa la opción **ID de entidad personalizado**. Braze genera un ID de entidad único para tu panel en el formato `braze_dashboard_<COMPANY_ID>`. Si no ves la opción **ID de entidad personalizado**, contacta a tu director de cuentas de Braze.

### Paso 2: Actualizar tu proveedor de identidad {#step-2-update-your-identity-provider}

Copia el ID de entidad generado y pégalo en el campo de ID de entidad de la aplicación de Braze en tu proveedor de identidad. Según tu proveedor, este campo puede estar etiquetado como **Entity ID**, **Audience** o **Audience URI**.

{% alert important %}
El ID de entidad debe coincidir tanto en Braze como en tu proveedor de identidad. Hasta que ambos lados utilicen el mismo valor, los usuarios no podrán iniciar sesión con SAML inicio de sesión único. Actualiza tu proveedor de identidad antes de guardar esta página para evitar bloquear a los usuarios.
{% endalert %}

### Paso 3: Guardar y probar {#step-3-save-and-test}

Guarda tu configuración de seguridad, cierra sesión y luego vuelve a iniciar sesión a través de tu proveedor de identidad para confirmar que el inicio de sesión funciona con el ID de entidad personalizado.

## Configuración de tu RelayState {#setting-up-your-relaystate}

1. En Braze, ve a **Configuración** > **Configuración y pruebas** > **API e identificadores**.
2. En la pestaña **Claves de API**, selecciona el botón **Crear clave de API**.
3. En el campo **Nombre de la clave de API**, introduce un nombre para tu clave.
4. Despliega el menú **inicio de sesión único** en **Permisos** y marca **inicio de sesión único.saml.login**.
5. Selecciona **Crear clave de API**.
6. En la pestaña **Claves de API**, copia el identificador junto a la clave de API que creaste.
7. Pega la clave de API de RelayState en el campo RelayState de tu proveedor de identidad (también puede aparecer como "Relay State" o "Default Relay State" dependiendo de tu proveedor de identidad).

## Inicio de sesión iniciado por el IdP {#idp-initiated-login}

Algunos proveedores de identidad admiten el inicio de sesión iniciado por el IdP, en el que los usuarios comienzan desde el portal del IdP en lugar de la página de inicio de sesión de Braze. El inicio de sesión iniciado por el IdP requiere una clave de API RelayState válida y una configuración correcta de la URL ACS. Guías de configuración específicas por proveedor:

- [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)
- [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)
- [Microsoft Entra inicio de sesión único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)

{% alert note %}
El inicio de sesión iniciado por el IdP de Microsoft Entra inicio de sesión único requiere dejar el campo **Sign-On URL** en blanco. Consulta [Microsoft Entra inicio de sesión único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso) para obtener más detalles.
{% endalert %}

## Comportamiento del inicio de sesión único {#sso-behavior}

Los miembros que opten por usar inicio de sesión único ya no podrán utilizar su contraseña. Los usuarios que sigan usando su contraseña podrán hacerlo a menos que se lo restrinjan los siguientes ajustes.

## Restricción {#restriction}

Puedes restringir a los miembros de tu organización para que solo inicien sesión con Google inicio de sesión único o SAML inicio de sesión único. Para activar las restricciones, ve a **Configuración** > **Configuración de la empresa** > **Configuración de administrador** > **Configuración de seguridad** y selecciona **Forzar inicio de sesión solo con Google inicio de sesión único** o **Forzar inicio de sesión solo con SAML inicio de sesión único personalizado**.

![Ejemplo de configuración de la sección "Reglas de autenticación" con una longitud mínima de contraseña de 8 caracteres y reutilización de contraseña de 3 veces. Las contraseñas caducarán después de 180 días y los usuarios cerrarán sesión tras 1440 minutos de inactividad.]({% image_buster /assets/img/sso3.png %})

Al activar las restricciones, los usuarios de Braze de tu empresa ya no podrán iniciar sesión con una contraseña, incluso si han iniciado sesión con una contraseña anteriormente.

{% alert important %}
Después de que se aplique el inicio de sesión único, no existe una opción alternativa para iniciar sesión si la autenticación inicio de sesión único falla. Antes de habilitar la aplicación de inicio de sesión único, asegúrate de que la configuración de inicio de sesión único sea correcta, de que todos los certificados estén vigentes y renovados, y de que la configuración de seguridad esté gestionada correctamente para evitar problemas de inicio de sesión.
{% endalert %}

## Cómo obtener una traza SAML {#obtaining-a-saml-trace}

Si experimentas problemas de inicio de sesión relacionados con inicio de sesión único, obtener una traza SAML puede ayudarte a solucionar problemas con tu conexión inicio de sesión único al identificar qué se envía en las solicitudes SAML.

### Requisitos previos {#prerequisites}

Para ejecutar una traza SAML, necesitarás un rastreador SAML. Aquí tienes dos opciones posibles según tu navegador:

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### Paso 1: Abre el rastreador SAML {#step-1-open-the-saml-tracer}

Selecciona el rastreador SAML en la barra de navegación de tu navegador. Asegúrate de que **Pause** no esté seleccionado, ya que esto impedirá que el rastreador SAML capture lo que se envía en las solicitudes SAML. Cuando el rastreador SAML esté abierto, verás que se rellena la traza.

![Rastreador SAML para Google Chrome.]({% image_buster /assets/img/saml_tracer_example.png %})

### Paso 2: Inicia sesión en Braze usando inicio de sesión único {#step-2-sign-into-braze-using-sso}

Ve a tu panel de Braze e intenta iniciar sesión usando inicio de sesión único. Si encuentras un error, abre el rastreador SAML e inténtalo de nuevo. Una traza SAML se ha recopilado correctamente si hay una fila con una URL como `https://dashboard-XX.braze.com/auth/saml/callback` y una etiqueta SAML de color naranja.

### Paso 3: Exporta y envía a Braze {#step-3-export-and-send-to-braze}

Selecciona **Export**. En **Select cookie-filter profile**, selecciona **None**. Luego, selecciona **Export**. Esto generará un archivo JSON que puedes enviar a soporte de Braze para solucionar problemas adicionales.

![Menú de preferencias de exportación de traza SAML con la opción "None" seleccionada.]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## Solución de problemas {#troubleshooting}

### ¿La dirección de correo electrónico del usuario está configurada correctamente? {#is-the-users-email-address-correctly-set-up}

Si recibes el error `ERROR_CODE_SSO_INVALID_EMAIL`, la dirección de correo electrónico del usuario no es válida. Confirma en el rastreo SAML que el campo `saml2:Attribute Name="email"` coincide con la dirección de correo electrónico que el usuario está utilizando para iniciar sesión. Si utilizas Microsoft Entra ID (anteriormente Azure Active Directory), el mapeado de atributos es `email = user.userprincipalname`.

La dirección de correo electrónico distingue entre mayúsculas y minúsculas y debe coincidir exactamente con la que se configuró en Braze, incluida la configurada en tu proveedor de identidad (como Okta, OneLogin, Microsoft Entra ID y otros).

Otros errores que indican que tienes problemas con la dirección de correo electrónico del usuario incluyen:
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`: La dirección de correo electrónico del usuario no se encuentra en el panel.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`: La dirección de correo electrónico del usuario está en blanco o mal configurada.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` o `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH`: La dirección de correo electrónico del usuario no coincide con la utilizada para configurar inicio de sesión único.

### ¿Tienes un certificado SAML válido (certificado x.509)? {#do-you-have-a-valid-saml-certificate-x509-certificate}

Puedes validar tu certificado SAML utilizando [esta herramienta de validación SAML](https://www.samltool.com/validate_response.php). Ten en cuenta que un certificado SAML caducado también es un certificado SAML no válido.

### ¿Cargaste un certificado SAML correcto (certificado x.509)? {#did-you-upload-a-correct-saml-certificate-x509-certificate}

Confirma que el certificado en la sección `ds:X509Certificate` del rastreo SAML coincide con el que cargaste en Braze. Esto no incluye el encabezado `-----BEGIN CERTIFICATE-----` ni el pie `-----END CERTIFICATE-----`.

### ¿Escribiste mal o formateaste incorrectamente tu certificado SAML (certificado x.509)? {#did-you-mistype-or-misformat-your-saml-certificate-x509-certificate}

Confirma que no haya espacios en blanco ni caracteres adicionales en el certificado que enviaste en el panel de Braze.

Cuando ingreses tu certificado en Braze, necesita estar codificado en Privacy Enhanced Mail (PEM) y formateado correctamente (incluyendo el encabezado `-----BEGIN CERTIFICATE-----` y el pie `-----END CERTIFICATE-----`).

A continuación se muestra un ejemplo de certificado con el formato correcto:

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### ¿El token de sesión del usuario es válido? {#is-the-users-session-token-valid}

Pide al usuario afectado que [borre la caché y las cookies de su navegador](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser) y luego intente iniciar sesión con SAML inicio de sesión único de nuevo.

### ¿Configuraste tu RelayState? {#did-you-set-your-relaystate}

Si recibes el error `ERROR_CODE_SSO_INVALID_RELAY_STATE`, tu RelayState podría estar mal configurado o no existir. Si aún no lo has hecho, necesitas configurar tu RelayState en tu sistema de administración de IdP. Para ver los pasos, consulta [Configurar tu RelayState](#setting-up-your-relaystate).

### ¿El inicio de sesión inicio de sesión único exitoso te devuelve a la página de inicio de sesión de Braze? {#does-successful-sso-sign-in-return-you-to-the-braze-login-page}

Esto puede ocurrir cuando el RelayState no está configurado correctamente. Confirma que creaste una clave de API (en **Configuración** > **Configuración y pruebas** > **API e identificadores**) para el inicio de sesión con IdP y que configuraste esa clave de API como el parámetro `RelayState` en tu IdP. El RelayState identifica en qué cuenta de empresa estás iniciando sesión. Para instrucciones paso a paso, consulta [Configurar tu RelayState](#setting-up-your-relaystate).

Si aún no puedes iniciar sesión, [contacta con soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) con un rastreo SAML si es posible. Para obtener ayuda capturando un rastreo, consulta [Obtener un rastreo SAML](#obtaining-a-saml-trace).

### ¿El usuario está atrapado en un bucle de inicio de sesión entre Okta y Braze? {#is-the-user-stuck-in-a-sign-in-loop-between-okta-and-braze}

Si un usuario no puede iniciar sesión porque está atrapado en un ciclo entre el inicio de sesión único de Okta y el panel de Braze, debes ir a Okta y configurar la URL de destino de inicio de sesión único a tu [instancia de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) (por ejemplo, `https://dashboard-07.braze.com`).

Si usas otro IdP, verifica si tu empresa cargó el certificado SAML o x.509 correcto en Braze.

### ¿Estás usando una integración manual? {#are-you-using-a-manual-integration}

Si tu empresa no descargó la aplicación de Braze desde la tienda de aplicaciones de tu IdP, necesitas descargar la integración prediseñada. Por ejemplo, si Okta es tu IdP, descargarías la aplicación de Braze desde su [página de integración](https://www.okta.com/integrations/braze/).

## Google inicio de sesión único

Si tu empresa usa Google inicio de sesión único en lugar de SAML inicio de sesión único personalizado, ponte en contacto con tu director de cuentas de Braze para habilitar Google inicio de sesión único en tu espacio de trabajo. Una vez habilitado, ve a **Configuración** > **Configuración de la empresa** > **Configuración de administrador** > **Configuración de seguridad** y selecciona **Enforce Google inicio de sesión único only login** para requerir la autenticación de Google para todos los usuarios de la empresa.

Cuando se activa la aplicación de Google inicio de sesión único, los usuarios deben iniciar sesión con la autenticación de Google y ya no podrán usar una contraseña de Braze. Cada usuario debe iniciar sesión con la cuenta de Google que coincida con su dirección de correo electrónico del panel de Braze. Si un usuario selecciona una cuenta de Google diferente durante el inicio de sesión, Braze rechaza el intento de autenticación.

### Solución de problemas del inicio de sesión con Google inicio de sesión único {#troubleshooting-google-sso-sign-in}

Si algunos usuarios no pueden iniciar sesión con Google inicio de sesión único, verifica lo siguiente:

- La dirección de correo electrónico de la cuenta de Google del usuario coincide exactamente con su dirección de correo electrónico del panel de Braze.
- El usuario tiene acceso a una cuenta de Google para su dirección de correo electrónico de la empresa.
- El usuario no está suspendido en Braze (**Configuración** > **Usuarios de la empresa**).

## Próximos pasos {#next-steps}

Después de configurar SAML inicio de sesión único, puedes:

- [Exigir inicio de sesión solo con inicio de sesión único]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#single-sign-on-sso-authentication) en tu configuración de seguridad para restringir a los usuarios de iniciar sesión con una contraseña.
- [Configurar el aprovisionamiento justo a tiempo de SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning) para que los nuevos usuarios creen automáticamente cuentas de Braze en su primer inicio de sesión con inicio de sesión único.