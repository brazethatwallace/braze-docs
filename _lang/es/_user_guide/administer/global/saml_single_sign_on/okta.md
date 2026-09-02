---
nav_title: Okta
article_title: Okta
page_order: 3
page_type: tutorial
description: "Este artículo te mostrará cómo configurar Braze para utilizar Okta en el inicio de sesión único."

---

# Okta

> Okta conecta a cualquier persona con cualquier aplicación en cualquier dispositivo. Es un servicio de gestión de identidades de nivel empresarial, creado para la nube, pero compatible con muchas aplicaciones locales. Con Okta, tu equipo de TI puede gestionar el acceso de cualquier empleado a cualquier aplicación o dispositivo.

{% alert note %}
La aplicación preconfigurada de Braze en el marketplace de Okta utiliza el Entity ID compartido `braze_dashboard`. Si necesitas un Entity ID único para este panel (por ejemplo, para conectar varios paneles de Braze a través de Okta), configura una aplicación SAML personalizada en lugar de la aplicación del marketplace y luego sigue los pasos de [Uso de un Entity ID personalizado]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#using-a-custom-entity-id).
{% endalert %}

## Requisitos {#requirements}

| Requisito | Detalles |
| ----------- | ------- |
| Okta activado para tu cuenta | Contacta a tu director de cuentas de Braze para que lo activen en tu cuenta. |
| Privilegios de administrador en Okta | Asegúrate de tener privilegios de administrador antes de configurar Okta. |
| Privilegios de administrador en Braze | Asegúrate de tener privilegios de administrador antes de configurar Okta. |
| Clave de API de RelayState | Para habilitar el inicio de sesión del IdP, ve a **Configuración** > **Claves de API** y crea una clave de API con permisos `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Paso 1: Configurar Braze {#step-1-configure-braze}

### Paso 1a: Navega a Configuración de seguridad en Braze {#step-1a-navigate-to-security-settings-in-braze}

Después de que tu director de cuentas haya habilitado SAML inicio de sesión único para tu cuenta, ve a **Configuración** > **Configuración de administrador** > **Configuración de seguridad** y activa la sección de SAML inicio de sesión único a **ON**.

![SAML SSO de Okta habilitado en la página de Configuración de seguridad.]({% image_buster/assets/img/Okta/okta1.png %})

### Paso 1b: Editar la configuración de SAML inicio de sesión único {#step-1b-edit-saml-sso-settings}

Desde el panel de administración de Okta, Okta te proporciona una URL de destino (URL de inicio de sesión) y un certificado `x.509`, que debes introducir en la página **Configuración de seguridad** de tu cuenta de Braze.

![Captura de pantalla relacionada con el paso 1b: editar la configuración de SAML SSO.]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| Requisito | Detalles |
|---|---|
| `SAML Name` | Aparecerá como el texto del botón en la pantalla de inicio de sesión. Normalmente es el nombre de tu proveedor de identidad, por ejemplo, "Okta". |
| `Target URL` | Esta es la URL de inicio de sesión proporcionada por el panel de administración de Okta. Encuéntrala yendo a **Applications** > tu aplicación > pestaña **General** > **App Embed Link** > **Embed Link**. |
| `Certificate` | El certificado `x.509` codificado en PEM es proporcionado por tu proveedor de identidad. Debes copiarlo y pegarlo en este campo. Recupéralo en Okta yendo a **SAML Signing Certificates** y seleccionando **Actions** > **Download certificate**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 1b: Editar la configuración de SAML inicio de sesión único" }

Selecciona **Save Changes** en la parte inferior de la página cuando hayas terminado.

## Paso 2: Configurar Okta {#step-2-configure-okta}

En Okta, selecciona la pestaña **Sign On** de la aplicación SAML de Braze y haz clic en **Edit**.

A continuación, introduce la clave de API RelayState con el permiso `sso.saml.login` en el campo **Default Relay State**.

![RelayState predeterminado de Okta en la pestaña Sign On.]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

Asegúrate de guardar esta nueva configuración.

{% alert tip %}
Si quieres que los usuarios de tu cuenta de Braze solo inicien sesión con SAML inicio de sesión único, puedes [restringir la autenticación de inicio de sesión único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) desde la página **Configuración de la empresa**.
{% endalert %}

## Paso 3: Iniciar sesión {#step-3-log-in}

¡Ahora deberías poder iniciar sesión en Braze usando Okta!

![Inicio de sesión en el panel de Braze con SAML SSO de Okta habilitado.]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}