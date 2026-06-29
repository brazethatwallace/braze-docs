---
nav_title: OneLogin
article_title: OneLogin
page_order: 4
page_type: tutorial
description: "Este artículo te mostrará cómo configurar Braze para utilizar OneLogin para el inicio de sesión único."

---

# OneLogin

> [OneLogin](https://www.onelogin.com/) es una plataforma de identidad en la nube que proporciona una solución integral para gestionar las identidades de los usuarios. OneLogin se integra con aplicaciones en la nube y locales mediante SAML 2.0, para el inicio de sesión único (SSO), el aprovisionamiento de usuarios, la autenticación multifactor, etc.

## Requisitos {#requirements}

Tras la configuración, se te pedirá que proporciones una URL de inicio de sesión y una URL de Assertion Consumer Service (ACS).

| Requisito | Detalles |
|---|---|
| Dominio de Braze | Necesitarás tu dominio de Braze para configurar Braze en OneLogin. Si tu instancia es `US-01`, deberás introducir la URL de tu dashboard en el dashboard de OneLogin. <br><br> Por ejemplo, si la URL de tu dashboard es `https://dashboard-01.braze.com`, tienes que introducir `dashboard-01.braze.com`.  |
| Clave de API RelayState | Para habilitar el inicio de sesión de IdP, ve a **Configuración** > **Claves de API** y crea una clave de API con permisos `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Inicio de sesión iniciado por IdP en OneLogin {#idp-initiated-login-within-onelogin}

### Paso 1: Configurar la aplicación Braze {#step-1-configure-the-braze-app}

1. Inicia sesión en [OneLogin](https://app.onelogin.com/login). Haz clic en **Administration**.![Página de administración de OneLogin.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Ve a **Apps** > **Add Apps** en la barra de navegación superior. Busca "Braze" y selecciona la aplicación Braze.![Resultados de búsqueda de Braze en OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Guarda la aplicación Braze en tu empresa.![Guarda la aplicación Braze en tu empresa.]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. Una vez guardada, ve a **Configuration** y añade tu **Braze Domain** y la clave de API **RelayState**.![Pestaña de configuración de OneLogin para la aplicación Braze.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze espera las aserciones SAML en un [formato específico]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#configure-your-identity-provider). En **Parameters**, los atributos compatibles con Braze deberían estar preconfigurados. Verifica que sean correctos.![Parámetros SAML de Braze en OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Copia el **Certificate** y el **SAML 2.0 Endpoint (HTTP)** necesarios para configurar el dashboard de Braze desde la pestaña **SSO**.![Certificados a copiar desde la pestaña SSO de la aplicación Braze en OneLogin.]({% image_buster /assets/img/onelogin_6.jpg %})

### Paso 2: Configurar OneLogin en Braze {#step-2-configure-onelogin-within-braze}

Una vez que hayas configurado Braze en tu OneLogin, te proporcionarán una URL de destino (`SAML 2.0 Endpoint (HTTP)`) y un certificado `x.509` que introducirás en tu cuenta de Braze.

Después de que tu director de cuentas haya habilitado SAML SSO para tu cuenta, ve a **Configuración** > **Configuración de administrador** > **Configuración de seguridad** y activa la sección SAML SSO a **ON**.

En esta página, introduce lo siguiente:

| Requisito | Detalles |
|---|---|
| `SAML Name` | Aparecerá como el texto del botón en la pantalla de inicio de sesión. Normalmente es el nombre de tu proveedor de identidad, como "OneLogin". |
| `Target URL` | Es la URL `SAML 2.0 Endpoint (HTTP)` proporcionada por OneLogin.|
| `Certificate` | El certificado `x.509` codificado en PEM proporcionado por tu OneLogin. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Configurar OneLogin en Braze" }

![Configuración de SAML SSO con el interruptor seleccionado.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Si quieres que los usuarios de tu cuenta de Braze solo inicien sesión con SAML SSO, puedes [restringir la autenticación de inicio de sesión único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) desde la página de **Configuración de empresa**.
{% endalert %}