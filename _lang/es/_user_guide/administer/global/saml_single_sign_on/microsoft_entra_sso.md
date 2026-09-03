---
nav_title: SSO de Microsoft Entra
article_title: SSO de Microsoft Entra
page_order: 2
page_type: tutorial
description: "Este artículo te guiará sobre cómo configurar las capacidades de inicio de sesión único de Microsoft Entra con Braze."

---

# SSO de Microsoft Entra {#microsoft-entra-sso}

> [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial) es el servicio de gestión de identidades y acceso basado en la nube de Microsoft, que ayuda a tus empleados a iniciar sesión y acceder a recursos. Puedes usar Entra SSO para controlar el acceso a tus aplicaciones y los recursos de tus aplicaciones, en función de tus requisitos empresariales.

## Requisitos {#requirements}

Durante la configuración, se te pedirá que proporciones una URL del servicio de consumidor de aserciones (ACS).

| Requisito | Detalles |
|---|---|
| URL del servicio de consumidor de aserciones (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> En algunos proveedores de identidad, también se puede denominar URL de respuesta, URL de audiencia o URI de audiencia. |
| ID de entidad | `braze_dashboard` de forma predeterminada. <br><br> Para asignar a este panel un ID de entidad único, habilita un ID de entidad personalizado y usa el valor generado (`braze_dashboard_<COMPANY_ID>`) en su lugar. Para ver los pasos, consulta [Uso de un ID de entidad personalizado]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#using-a-custom-entity-id). |
| Clave de API de RelayState | Para habilitar el inicio de sesión del proveedor de identidad, ve a **Configuración** > **Claves de API** y crea una clave de API con permisos `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Inicio de sesión iniciado por el proveedor de servicios (SP) en Microsoft Entra SSO {#service-provider-sp-initiated-login-within-microsoft-entra-sso}

### Paso 1: Añade Braze desde la galería {#step-1-add-braze-from-the-gallery}

1. En tu centro de administración de Microsoft Entra, ve a **Identity** > **Applications** > **Enterprise Applications** y selecciona **New application**.
2. Busca **Braze** en el cuadro de búsqueda, selecciónalo en el panel de resultados y luego selecciona **Add**.

### Paso 2: Configura Microsoft Entra SSO {#step-2-configure-microsoft-entra-sso}

1. En tu centro de administración de Microsoft Entra, ve a la página de integración de la aplicación Braze y selecciona **Single sign-on**.
2. En la página **Select a single sign-on method**, selecciona **SAML** como tu método.
3. En la página **Set up Single Sign-On with SAML**, selecciona el icono de edición de **Basic SAML Configuration**.
4. Configura la aplicación en modo iniciado por IdP introduciendo una **Reply URL** que combine tu [instancia de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) con el siguiente patrón: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.
5. En la misma sección **Basic SAML Configuration**, deja **Identifier (Entity ID)** configurado como `braze_dashboard` a menos que uses un [Entity ID personalizado]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#using-a-custom-entity-id). En ese caso, introduce el valor generado por tu panel (`braze_dashboard_<COMPANY_ID>`) para que coincida con el valor mostrado en la configuración de seguridad de Braze.
6. Configura el RelayState introduciendo tu clave de API de Relay State generada en el campo **Relay State**.

{% alert important %}
**No** configures el campo **Sign-On URL**. Deja este campo en blanco para evitar problemas con tu SAML SSO iniciado por IdP.
{% endalert %}

{: start="7"}
7. Formatea las aserciones SAML en el formato específico esperado por Braze. Consulta las siguientes pestañas sobre atributos de usuario y declaraciones de usuario para entender cómo deben formatearse estos atributos y valores.

{% tabs %}
{% tab Atributos de usuario %}
Puedes gestionar los valores de estos atributos desde la sección **User Attributes** en la página **Application Integration**.

Usa los siguientes pares de atributos:

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.mail`
- `name` = `user.userprincipalname`
- `email` = `user.userprincipalname`
- `first_name` = `user.givenname`
- `last_name` = `user.surname`
- `Unique User Identifier` = `user.userprincipalname`

{% alert important %}
El campo de correo electrónico debe coincidir con lo configurado para tus usuarios en Braze. En la mayoría de los casos, es el mismo que `user.userprincipalname`; sin embargo, si tienes una configuración diferente, trabaja con tu administrador de sistemas para asegurarte de que estos campos coincidan exactamente.
{% endalert %}

{% endtab %}
{% tab Declaraciones de usuario %}

En la página **Set up Single Sign-On with SAML**, selecciona **Edit** para abrir el diálogo **User Attributes**. Luego, edita las declaraciones de usuario según el formato adecuado.

Usa los siguientes pares de nombres de declaraciones:

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
El campo de correo electrónico debe coincidir con lo configurado para tus usuarios en Braze. En la mayoría de los casos, es el mismo que `user.userprincipalname`; sin embargo, si tienes una configuración diferente, trabaja con tu administrador de sistemas para asegurarte de que estos campos coincidan exactamente.
{% endalert %}

Puedes gestionar estas declaraciones de usuario y sus valores desde la sección **Manage claim**.

{% endtab %}
{% endtabs %}

{: start="8"}
8. Ve a la página **Set up Single Sign-On with SAML**, luego desplázate hasta la sección **SAML Signing Certificate** y descarga el **Certificate (Base64)** apropiado según tus requisitos.
9. Ve a la sección **Set up Braze** y copia las URL apropiadas para usarlas en la [configuración de Braze](#step-3).

### Paso 3: Configura Microsoft Entra SSO dentro de Braze {#step-3}

Después de configurar Braze en el centro de administración de Microsoft Entra, Microsoft Entra proporciona una URL de destino (URL de inicio de sesión) y un certificado **x.509**, que introduces en tu cuenta de Braze.

Después de que tu director de cuentas haya habilitado SAML SSO para tu cuenta, haz lo siguiente:

1. Ve a **Configuración** > **Configuración de la empresa** > **Configuración de administrador** > **Configuración de seguridad** y alterna la sección SAML SSO a **ON**.
2. En la misma página, añade lo siguiente:

| Requisito | Detalles |
|---|---|
| `SAML Name` | Aparecerá como el texto del botón en la pantalla de inicio de sesión. Normalmente es el nombre de tu proveedor de identidad, como "Microsoft Entra". |
| `Target URL` | Esta es la URL de inicio de sesión proporcionada por Microsoft Entra. |
| `Certificate` | El certificado `x.509` codificado en PEM lo proporciona tu proveedor de identidad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Configura Microsoft Entra SSO dentro de Braze #step-3" }

{% alert tip %}
Si quieres que los usuarios de tu cuenta de Braze solo inicien sesión con SAML SSO, puedes [restringir la autenticación de inicio de sesión único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) en la página **Configuración de seguridad** en **Reglas de autenticación**.
{% endalert %}