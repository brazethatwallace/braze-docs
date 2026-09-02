---
nav_title: OneLogin
article_title: OneLogin
page_order: 4
page_type: tutorial
description: "Este artículo te mostrará cómo configurar Braze para utilizar OneLogin para el inicio de sesión único."

---

# OneLogin

> [OneLogin](https://www.onelogin.com/) es una plataforma de identidad en la nube que proporciona una solución integral para gestionar las identidades de los usuarios. OneLogin se integra con aplicaciones en la nube y locales mediante SAML 2.0, para el inicio de sesión único (inicio de sesión único), el aprovisionamiento de usuarios, la autenticación multifactor, etc.

## Requisitos {#requirements}

Durante la configuración, se te pedirá que proporciones una URL de inicio de sesión y una URL de Assertion Consumer Service (ACS).

| Requisito | Detalles |
|---|---|
| URL de Assertion Consumer Service (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Para dominios de la Unión Europea, la URL de ACS es `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. |
| ID de entidad | `braze_dashboard` de forma predeterminada. Si tu proveedor de identidad requiere un ID de entidad específico de la empresa, habilita **ID de entidad personalizado** en **Configuración de seguridad** y usa `braze_dashboard_<companyID>`. |
| Dominio de Braze | Necesitarás tu dominio de Braze para configurar Braze dentro de OneLogin. Si tu instancia es `US-01`, deberás introducir la URL de tu panel en el panel de OneLogin. <br><br> Por ejemplo, si la URL de tu panel es `https://dashboard-01.braze.com`, debes introducir `dashboard-01.braze.com`.  |
| Clave de API de RelayState | Para habilitar el inicio de sesión del proveedor de identidad, ve a **Configuración** > **Configuración y pruebas** > **API e identificadores**, abre la pestaña **Claves de API** y crea una clave de API con permisos `sso.saml.login`. Para ver los pasos, consulta [Configuración de tu RelayState]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Inicio de sesión iniciado por el IdP dentro de OneLogin {#idp-initiated-login-within-onelogin}

### Paso 1: Configura la aplicación de Braze {#step-1-configure-the-braze-app}

1. Inicia sesión en [OneLogin](https://app.onelogin.com/login). Haz clic en **Administration**.![Página de administración de OneLogin.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Ve a **Apps** > **Add Apps** en la barra de navegación superior. Busca "Braze" y selecciona la aplicación de Braze.![Resultados de búsqueda de Braze en OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Guarda la aplicación de Braze en tu empresa.![Resultados de búsqueda de Braze en OneLogin.]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. Cuando se haya guardado, ve a **Configuration** y añade tu **Braze Domain** y la clave de API de **RelayState**. Si tu IdP requiere un Entity ID específico de la empresa, configura también la **ACS URL** (`https://<SUBDOMAIN>.braze.com/auth/saml/callback`) y el Entity ID desde la [configuración de SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#requirements).![Pestaña de configuración de OneLogin para la aplicación de Braze.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze espera las aserciones SAML en un [formato específico]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#step-1-configure-your-identity-provider). En **Parameters**, los atributos compatibles con Braze deberían estar prellenados. Verifica que sean correctos.![Parámetros SAML de Braze en OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Copia el **Certificate** y el **SAML 2.0 Endpoint (HTTP)** necesarios para configurar el panel de Braze desde la pestaña **SSO**.![Certificados para copiar desde la pestaña SSO de la aplicación de Braze en OneLogin.]({% image_buster /assets/img/onelogin_6.jpg %})

### Paso 2: Configura OneLogin dentro de Braze {#step-2-configure-onelogin-within-braze}

Una vez que hayas configurado Braze dentro de tu OneLogin, te proporcionarán una URL de destino (`SAML 2.0 Endpoint (HTTP)`) y un certificado `x.509` para introducir en tu cuenta de Braze.

Después de que tu director de cuentas haya habilitado SAML inicio de sesión único para tu cuenta, ve a **Configuración** > **Configuración de la empresa** > **Configuración de administrador** > **Configuración de seguridad** y activa la sección de SAML inicio de sesión único a **ON**.

En esta página, introduce lo siguiente:

| Requisito | Detalles |
|---|---|
| `SAML Name` | Aparecerá como el texto del botón en la pantalla de inicio de sesión. Normalmente es el nombre de tu proveedor de identidad, como "OneLogin". |
| `Target URL` | Esta es la URL de `SAML 2.0 Endpoint (HTTP)` proporcionada por OneLogin. |
| `Certificate` | El certificado `x.509` codificado en PEM es proporcionado por tu OneLogin. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Configura OneLogin dentro de Braze" }

Si tu IdP requiere un Entity ID específico de la empresa, activa **Custom Entity ID** en **Configuración de seguridad**, copia el valor generado y pégalo en el campo Entity ID de OneLogin. Consulta [Custom Entity ID]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#custom-entity-id) en el artículo de configuración de SAML inicio de sesión único.

![Configuración de SAML SSO con el interruptor seleccionado.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Si quieres que los usuarios de tu cuenta de Braze solo inicien sesión con SAML inicio de sesión único, puedes [restringir la autenticación de inicio de sesión único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) desde **Configuración** > **Configuración de la empresa** > **Configuración de administrador** > **Configuración de seguridad**.
{% endalert %}

## Próximos pasos {#next-steps}

Después de que el SAML inicio de sesión único de OneLogin esté funcionando:

- [Imponer el inicio de sesión exclusivo mediante SAML inicio de sesión único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) si se debe deshabilitar el inicio de sesión con contraseña.
- [Configurar el aprovisionamiento justo a tiempo de SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning) para crear automáticamente usuarios del panel en el primer inicio de sesión del IdP.
- Usa [Obtener una traza SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#obtaining-a-saml-trace) si los usuarios encuentran errores de inicio de sesión.