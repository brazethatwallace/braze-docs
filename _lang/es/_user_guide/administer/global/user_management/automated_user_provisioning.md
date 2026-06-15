---
nav_title: Aprovisionamiento automático de usuarios
article_title: Aprovisionamiento automático de usuarios
page_order: 3
page_type: reference
description: "Este artículo de referencia explica qué información debes proporcionar para el aprovisionamiento automatizado de usuarios y cómo y dónde utilizar el token generado del Sistema para la gestión de identidades entre dominios (SCIM)."
alias: /scim/automated_user_provisioning/

---

# Aprovisionamiento automático de usuarios {#automated-user-provisioning}

> El aprovisionamiento automático de usuarios te permite crear y administrar usuarios de Braze a través de una API en lugar de hacerlo manualmente en el dashboard. Braze lo admite mediante el Sistema para la gestión de identidades entre dominios (SCIM). Este artículo te explica qué información debes proporcionar, cómo generar tu token SCIM y dónde encontrar tu punto de conexión de la API SCIM.

## Acceso a la configuración de aprovisionamiento SCIM {#accessing-scim-provisioning-settings}

1. En el panel de Braze, ve a **Settings** > **Admin Settings** > **SCIM Provisioning** y, a continuación, selecciona **Configure SCIM integration**.
2. En el paso **Braze configuration**, selecciona un método de aprovisionamiento y proporciona la configuración de acceso.

![Una página para configurar la integración SCIM con secciones para seleccionar un método de aprovisionamiento y proporcionar la configuración de acceso.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3. En el paso **IdP configuration**, sigue los pasos indicados en la plataforma para el método de aprovisionamiento seleccionado.

{% tabs %}
{% tab Okta - Braze app %}

{% multi_lang_include early_access_beta_alert.md feature='The Okta integration' %}

Utiliza la opción **Okta - Braze app** si has configurado la aplicación Braze para SAML SSO en Okta. Si configuraste una aplicación personalizada para SSO, sigue las instrucciones en la pestaña [Okta - Integración de aplicación personalizada]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning/?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning).

## Paso 1: Configurar el aprovisionamiento SCIM {#step-1-set-up-scim-provisioning}

### Paso 1.1: Habilitar SCIM {#step-11-enable-scim}

1. En Okta, ve a **Applications** > **Applications** y selecciona **Create App Integration**. Selecciona **SAML 2.0** como método de inicio de sesión.
2. Completa los siguientes datos (que se encuentran en el paso [**IdP configuration**](#accessing-scim-provisioning-settings) de Braze) para crear una aplicación personalizada:
- Logotipo de la aplicación
- URL de inicio de sesión único
- URL de audiencia (ID de entidad del SP)
3. Selecciona **Finish**.
4. Selecciona la pestaña **General**.
5. En la sección **App Settings**, selecciona **Edit**.
6. En el campo **Provisioning**, selecciona **SCIM**.

### Paso 1.2: Desactivar la visibilidad de la aplicación {#step-12-disable-application-visibility}

1. En el campo **Application visibility**, selecciona la casilla **Do not display application icon to user**. Esto evita que los usuarios accedan a SSO a través de la aplicación, que está destinada únicamente a SCIM.
2. Selecciona **Save**.

### Paso 1.3: Configurar la integración SCIM {#step-13-set-up-the-scim-integration}

1. Selecciona la pestaña **Provisioning**.
2. En **Settings** > **Integration** > **SCIM Connection**, selecciona **Edit** y completa los valores de los campos que aparecen en la tabla de la página **Setup SCIM provisioning**.

### Paso 1.4: Probar las credenciales de la API {#step-14-test-the-api-credentials}

Selecciona **Test API Credentials**. Si la integración es correcta, aparecerá un mensaje de verificación y podrás guardar.

### Paso 1.5: Habilitar el aprovisionamiento en la aplicación {#step-15-enable-provisioning-to-the-app}

1. En **Provisioning** > **Settings** > **To App** > **Provisioning to App**, selecciona **Edit**.
2. Habilita lo siguiente:
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. Revisa y configura la sección **Attribute Mapping** con los mapeados que aparecen en la tabla de la página **Setup SCIM provisioning**.

## Paso 2: Asignar usuarios a la aplicación {#step-2-assign-users-to-the-app}

1. Selecciona la pestaña **Assignment**.
2. Selecciona **Assign** y elige una opción.
3. Asigna la aplicación a las personas que deben tener acceso a Braze.
4. Selecciona **Done** cuando hayas completado la asignación.

{% endtab %}
{% tab Okta - Custom app integration %}

{% multi_lang_include early_access_beta_alert.md feature='The Okta integration' %}

Utiliza la opción **Okta - Custom app integration** si configuraste una aplicación personalizada para SSO. Si configuraste la aplicación Braze para SAML SSO en Okta, sigue las instrucciones en la pestaña [Okta - Braze app]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning/?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning).

## Paso 1: Configurar el aprovisionamiento SCIM

### Paso 1.1: Habilitar SCIM

1. En Okta, ve a tu aplicación Braze.
2. Selecciona la pestaña **General**.
3. En la sección **App Settings**, selecciona **Edit**.
4. En el campo **Provisioning**, selecciona **SCIM**.
5. Selecciona **Save**.

### Paso 1.2: Configurar la integración SCIM {#step-12-set-up-scim-integration}

1. Selecciona la pestaña **Provisioning**.
2. En **Settings** > **Integration** > **SCIM Connection**, selecciona **Edit** y completa los valores de los campos que aparecen en la tabla de la página **Setup SCIM provisioning**.
3. Prueba las credenciales de la API seleccionando **Test API Credentials**.
4. Selecciona **Save**.

### Paso 1.3: Habilitar el aprovisionamiento en la aplicación {#step-13-enable-provisioning-to-the-app}

1. En **Provisioning** > **Settings** > **To App** > **Provisioning to App**, selecciona **Edit**.
2. Habilita lo siguiente:
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. Revisa y configura la sección **Attribute Mapping** con los mapeados que aparecen en la tabla de la página **Setup SCIM provisioning**.

## Paso 2: Asignar usuarios a la aplicación

1. Selecciona la pestaña **Assignment**.
2. Selecciona **Assign** y elige una opción.
3. Asigna la aplicación a las personas que deben tener acceso a Braze.
4. Selecciona **Done**.

{% endtab %}
{% tab Entra ID %}

{% multi_lang_include early_access_beta_alert.md feature='The Entra ID integration' %}

## Paso 1: Configurar la aplicación de aprovisionamiento SCIM {#step-1-set-up-scim-provisioning-app}

### Paso 1.1: Iniciar sesión en el centro de administración de Microsoft Entra {#step-11-log-into-microsoft-entra-admin-center}

Inicia sesión en tu centro de administración de Microsoft Entra.

### Paso 1.2: Crear y configurar tu aplicación SCIM {#step-12-create-and-set-up-your-scim-app}

1. En el menú de navegación, ve a **Entra ID** > **Enterprise apps**.
2. Selecciona **New application**.
3. Selecciona **Create your own application**.
4. En el panel, introduce un nombre para tu aplicación.
5. En la sección **What are you looking to do with your application?**, selecciona **Integrate application you don't find in the gallery (Non-gallery)**.
6. Selecciona **Create**.

### Paso 1.3: Configurar la integración SCIM {#step-13-set-up-scim-integration}

1. Ve a la sección **Manage** > **Provisioning** de tu aplicación SCIM.
2. Selecciona **Connect your application** o **New configuration** y completa los valores de los campos que aparecen en la tabla de la página **Setup SCIM provisioning**.

### Paso 1.4: Habilitar el aprovisionamiento en la aplicación {#step-14-enable-provisioning-to-the-app}

1. Ve a la sección **Manage** > **Attribute mapping (Preview)** de tu aplicación SCIM.
2. Selecciona **Provision Microsoft Entra ID Users**.
3. Revisa y configura la sección **Attribute Mapping** para que coincida con los atributos que aparecen en la tabla de la página **Setup SCIM provisioning**.
4. Cierra la página **Attribute Mapping**.

## Paso 2: Asignar usuarios a la aplicación

1. Ve a **Manage** > **Users and Groups**.
2. Selecciona **Add user/group**.
3. Selecciona **None Selected** para asignar usuarios a la aplicación.
4. Selecciona el botón **Select** para confirmar la asignación.

{% endtab %}
{% tab Custom %}

## Paso 1: Configurar los ajustes de SCIM {#step-1-configure-your-scim-settings}

- **Espacio de trabajo predeterminado:** selecciona el espacio de trabajo donde se deben añadir los nuevos usuarios de forma predeterminada. Si no especificas un espacio de trabajo en tu [solicitud a la API SCIM]({{site.baseurl}}/post_create_user_account/), Braze asigna los usuarios a este espacio de trabajo.
- **Origin del servicio:** introduce el dominio de origen de tus solicitudes SCIM. Braze lo utiliza en el encabezado `X-Request-Origin` para verificar de dónde provienen las solicitudes.
- **Lista de IP permitidas (opcional):** puedes restringir las solicitudes SCIM a direcciones IP específicas. Introduce una lista separada por comas o un rango de direcciones IP permitidas. El encabezado `X-Request-Origin` de cada solicitud se utiliza para comprobar la dirección IP de la solicitud con la lista de permitidas.

![Formulario de configuración de aprovisionamiento SCIM con tres campos: espacio de trabajo predeterminado, origin del servicio y lista de IP permitidas opcional. El botón "Generate SCIM Token" está deshabilitado.]({% image_buster /assets/img/scim_unfilled.png %})

## Paso 2: Generar un token SCIM {#step-2-generate-a-scim-token}

Después de completar los campos obligatorios, pulsa **Generate SCIM token** para generar un token SCIM y ver tu punto de conexión de la API SCIM. Asegúrate de copiar el token SCIM antes de salir de la página. **Este token solo aparece una vez.**

![Campos del punto de conexión de la API SCIM y del token SCIM mostrados con valores enmascarados y botones de copiar. Debajo del campo del token hay un botón "Reset Token".]({% image_buster /assets/img/scim.png %})

Braze espera que todas las solicitudes SCIM contengan el token bearer de la API SCIM adjunto mediante un encabezado HTTP `Authorization`.

{% endtab %}
{% endtabs %}