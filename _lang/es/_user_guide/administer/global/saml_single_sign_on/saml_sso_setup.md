---
nav_title: Configuración de SAML SSO
article_title: Configuración de SAML SSO
page_order: 0
page_type: tutorial
toc_headers: h2
description: "Este artículo te guiará sobre cómo habilitar el inicio de sesión único SAML para tu cuenta de Braze."

---

# Inicio de sesión iniciado por el proveedor de servicios (SP) {#service-provider-sp-initiated-login}

> Este artículo te guiará sobre cómo habilitar el inicio de sesión único SAML para tu cuenta de Braze y cómo obtener un rastreo SAML.

## Requisitos {#requirements}

Durante la configuración, se te pedirá que proporciones una URL de inicio de sesión y una URL de Assertion Consumer Service (ACS).

| Requisito | Detalles |
|---|---|
| URL de Assertion Consumer Service (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Para dominios de la Unión Europea, la URL de ACS es `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. <br><br> Para algunos IdP, también puede denominarse URL de respuesta, URL de inicio de sesión, URL de audiencia o URI de audiencia. |
| ID de entidad | `braze_dashboard` |
| Clave de API de RelayState | Ve a **Configuración** > **Claves de API** y crea una clave de API con permisos `sso.saml.login`, luego introduce la clave de API generada como parámetro `RelayState` en tu IdP. Para conocer los pasos detallados, consulta [Configurar tu RelayState](#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Configurar SAML SSO {#setting-up-saml-sso}

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

Después de que tu director de cuentas active SAML SSO para tu cuenta, ve a **Configuración** > **Configuración de administrador** > **Configuración de seguridad** y cambia la sección SAML SSO a **ACTIVADO**.

En la misma página, introduce lo siguiente:

| Requisito | Detalles |
|---|---|
| Nombre SAML | Aparecerá como el texto del botón en la pantalla de inicio de sesión.<br>Normalmente es el nombre de tu proveedor de identidad, como "Okta". |
| URL de destino | Se proporciona después de configurar Braze en tu IdP.<br> Algunos IdP lo denominan URL de SSO o punto de conexión SAML 2.0. |
| Certificado | El certificado `x.509` proporcionado por tu proveedor de identidad.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Configura Braze" }

Asegúrate de que tu certificado `x.509` siga este formato cuando lo añadas al dashboard:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![Configuración de SAML SSO con el interruptor seleccionado.]({% image_buster /assets/img/samlsso.png %})

### Paso 3: Inicia sesión en Braze {#step-3-sign-into-braze}

Guarda tu configuración de seguridad y cierra sesión. Luego, vuelve a iniciar sesión con tu proveedor de identidad.

![Pantalla de inicio de sesión del dashboard con SSO habilitado]({% image_buster /assets/img/sso1.png %}){: style="max-width:60%;"}

## Configurar tu RelayState {#setting-up-your-relaystate}

1. En Braze, ve a **Configuración** > **API e identificadores**.
2. En la pestaña **Claves de API**, selecciona el botón **Crear clave de API**.
3. En el campo **Nombre de la clave de API**, introduce un nombre para tu clave.
4. Despliega el menú **SSO** en **Permisos** y marca **sso.saml.login**.<br><br>![La sección "Permisos" con sso.saml.login marcado.]({% image_buster /assets/img/relaystate_troubleshoot.png %}){: style="max-width:70%;"}<br><br>
5. Selecciona **Crear clave de API**.
6. En la pestaña **Claves de API**, copia el identificador junto a la clave de API que creaste.
7. Pega la clave de API de RelayState en el RelayState de tu IdP (también puede aparecer como "Relay State" o "Default Relay State" dependiendo de tu IdP).

## Comportamiento de SSO {#sso-behavior}

Los miembros que opten por usar SSO ya no podrán utilizar su contraseña como lo hacían antes. Los usuarios que continúen usando su contraseña podrán hacerlo a menos que se restrinja mediante la siguiente configuración.

## Restricción {#restriction}

Puedes restringir a los miembros de tu organización para que solo inicien sesión con Google SSO o SAML SSO. Para activar las restricciones, ve a **Configuración de seguridad** y selecciona **Enforce Google SSO only login** o **Enforce custom SAML SSO only login**.

![Ejemplo de configuración de la sección "Reglas de autenticación" con una longitud mínima de contraseña de 8 caracteres y reutilización de contraseña de 3 veces. Las contraseñas caducarán después de 180 días y los usuarios cerrarán sesión después de 1440 minutos de inactividad.]({% image_buster /assets/img/sso3.png %})

Al activar las restricciones, los usuarios de Braze de tu empresa ya no podrán iniciar sesión con una contraseña, incluso si han iniciado sesión con una contraseña anteriormente.

## Obtener un rastreo SAML {#obtaining-a-saml-trace}

Si experimentas problemas de inicio de sesión relacionados con SSO, obtener un rastreo SAML puede ayudarte a solucionar problemas de tu conexión SSO al identificar qué se envía en las solicitudes SAML.

### Requisitos previos {#prerequisites}

Para ejecutar un rastreo SAML, necesitarás un rastreador SAML. Aquí tienes dos opciones posibles según tu navegador:

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### Paso 1: Abre el rastreador SAML {#step-1-open-the-saml-tracer}

Selecciona el rastreador SAML en la barra de navegación de tu navegador. Asegúrate de que **Pause** no esté seleccionado, ya que esto impedirá que el rastreador SAML capture lo que se envía en las solicitudes SAML. Cuando el rastreador SAML esté abierto, verás que se llena el rastreo.

![Rastreador SAML para Google Chrome.]({% image_buster /assets/img/saml_tracer_example.png %})

### Paso 2: Inicia sesión en Braze usando SSO {#step-2-sign-into-braze-using-sso}

Ve a tu dashboard de Braze e intenta iniciar sesión usando SSO. Si encuentras un error, abre el rastreador SAML e inténtalo de nuevo. Un rastreo SAML se ha recopilado correctamente si hay una fila con una URL como `https://dashboard-XX.braze.com/auth/saml/callback` y una etiqueta SAML naranja.

### Paso 3: Exporta y envía a Braze {#step-3-export-and-send-to-braze}

Selecciona **Export**. En **Select cookie-filter profile**, selecciona **None**. Luego, selecciona **Export**. Esto generará un archivo JSON que puedes enviar a soporte de Braze para una solución de problemas más detallada.

![Menú "Export SAML-trace preferences" con la opción "None" seleccionada.]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## Solución de problemas {#troubleshooting}

### ¿La dirección de correo electrónico del usuario está configurada correctamente? {#is-the-users-email-address-correctly-set-up}

Si recibes el error `ERROR_CODE_SSO_INVALID_EMAIL`, la dirección de correo electrónico del usuario no es válida. Confirma en el rastreo SAML que el campo `saml2:Attribute Name="email"` coincida con la dirección de correo electrónico que el usuario está usando para iniciar sesión. Si usas Microsoft Entra ID (anteriormente Azure Active Directory), el mapeado de atributos es `email = user.userprincipalname`.

La dirección de correo electrónico distingue entre mayúsculas y minúsculas y debe coincidir exactamente con la que se configuró en Braze, incluida la configurada en tu proveedor de identidad (como Okta, OneLogin, Microsoft Entra ID y otros).

Otros errores que indican que tienes problemas con la dirección de correo electrónico del usuario incluyen:
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`: La dirección de correo electrónico del usuario no está en el dashboard.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`: La dirección de correo electrónico del usuario está en blanco o mal configurada.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` o `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH`: La dirección de correo electrónico del usuario no coincide con la utilizada para configurar SSO.

### ¿Tienes un certificado SAML válido (certificado x.509)? {#do-you-have-a-valid-saml-certificate-x509-certificate}

Puedes validar tu certificado SAML usando [esta herramienta de validación SAML](https://www.samltool.com/validate_response.php). Ten en cuenta que un certificado SAML caducado también es un certificado SAML no válido.

### ¿Cargaste un certificado SAML correcto (certificado x.509)? {#did-you-upload-a-correct-saml-certificate-x509-certificate}

Confirma que el certificado en la sección `ds:X509Certificate` del rastreo SAML coincida con el que cargaste en Braze. Esto no incluye el encabezado `-----BEGIN CERTIFICATE-----` ni el pie `-----END CERTIFICATE-----`.

### ¿Escribiste mal o formateaste incorrectamente tu certificado SAML (certificado x.509)? {#did-you-mistype-or-misformat-your-saml-certificate-x509-certificate}

Confirma que no haya espacios en blanco ni caracteres adicionales en el certificado que enviaste en el dashboard de Braze.

Cuando introduces tu certificado en Braze, debe estar codificado en Privacy Enhanced Mail (PEM) y formateado correctamente (incluyendo el encabezado `-----BEGIN CERTIFICATE-----` y el pie `-----END CERTIFICATE-----`).

Aquí tienes un ejemplo de certificado formateado correctamente:

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### ¿El token de sesión del usuario es válido? {#is-the-users-session-token-valid}

Pide al usuario afectado que [borre la caché y las cookies de su navegador](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser) y luego intente iniciar sesión con SAML SSO de nuevo.

### ¿Configuraste tu RelayState? {#did-you-set-your-relaystate}

Si recibes el error `ERROR_CODE_SSO_INVALID_RELAY_STATE`, tu RelayState podría estar mal configurado o no existir. Si aún no lo has hecho, necesitas configurar tu RelayState en tu sistema de administración de IdP. Para conocer los pasos, consulta [Configurar tu RelayState](#setting-up-your-relaystate).

### ¿El inicio de sesión SSO exitoso te devuelve a la página de inicio de sesión de Braze? {#does-successful-sso-sign-in-return-you-to-the-braze-login-page}

Esto puede ocurrir cuando RelayState no está configurado correctamente. Confirma que creaste una clave de API (en **Configuración** > **Claves de API**) para el inicio de sesión del IdP y que configuraste esa clave de API como el parámetro `RelayState` en tu IdP. RelayState identifica en qué cuenta de empresa estás iniciando sesión. Para instrucciones paso a paso, consulta [Configurar tu RelayState](#setting-up-your-relaystate).

Si aún no puedes iniciar sesión, [ponte en contacto con soporte de Braze]({{site.baseurl}}/braze_support/) con un rastreo SAML si es posible. Para obtener ayuda capturando un rastreo, consulta [Obtener un rastreo SAML](#obtaining-a-saml-trace).

### ¿El usuario está atrapado en un bucle de inicio de sesión entre Okta y Braze? {#is-the-user-stuck-in-a-sign-in-loop-between-okta-and-braze}

Si un usuario no puede iniciar sesión porque está atrapado en un ciclo entre el SSO de Okta y el dashboard de Braze, necesitas ir a Okta y configurar la URL de destino de SSO a tu [instancia de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/) (por ejemplo, `https://dashboard-07.braze.com`).

Si usas otro IdP, verifica si tu empresa cargó el certificado SAML o x.509 correcto en Braze.

### ¿Estás usando una integración manual? {#are-you-using-a-manual-integration}

Si tu empresa no descargó la aplicación de Braze desde la tienda de aplicaciones de tu IdP, necesitas descargar la integración prediseñada. Por ejemplo, si Okta es tu IdP, descargarías la aplicación de Braze desde su [página de integración](https://www.okta.com/integrations/braze/).

## Google SSO

Si tu empresa usa Google SSO en lugar de SAML SSO personalizado, ponte en contacto con tu director de cuentas de Braze para habilitar Google SSO en tu espacio de trabajo. Una vez habilitado, ve a **Configuración de seguridad** y selecciona **Enforce Google SSO only login** para requerir la autenticación de Google para todos los usuarios de la empresa.

Cuando se activa la aplicación de Google SSO, los usuarios deben iniciar sesión con la autenticación de Google y ya no podrán usar una contraseña de Braze. Cada usuario debe iniciar sesión con la cuenta de Google que coincida con su dirección de correo electrónico del dashboard de Braze. Si un usuario selecciona una cuenta de Google diferente durante el inicio de sesión, Braze rechaza el intento de autenticación.

### Solución de problemas del inicio de sesión con Google SSO {#troubleshooting-google-sso-sign-in}

Si algunos usuarios no pueden iniciar sesión con Google SSO, verifica lo siguiente:

- La dirección de correo electrónico de la cuenta de Google del usuario coincide exactamente con su dirección de correo electrónico del dashboard de Braze.
- El usuario tiene acceso a una cuenta de Google para su dirección de correo electrónico de la empresa.
- El usuario no está suspendido en Braze (**Configuración** > **Usuarios de la empresa**).

## Próximos pasos {#next-steps}

Después de configurar SAML SSO, puedes:

- [Forzar el inicio de sesión solo con SSO]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#restriction) en tu configuración de seguridad para restringir a los usuarios de iniciar sesión con una contraseña.
- [Configurar el aprovisionamiento justo a tiempo de SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning/) para que los nuevos usuarios creen automáticamente cuentas de Braze en su primer inicio de sesión con SSO.