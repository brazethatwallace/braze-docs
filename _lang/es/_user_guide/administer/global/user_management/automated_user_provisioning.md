---
nav_title: Aprovisionamiento automático de usuarios
article_title: Aprovisionamiento automático de usuarios
page_order: 3
page_type: reference
description: "Este artículo de referencia explica qué información debes proporcionar para el aprovisionamiento automatizado de usuarios y cómo y dónde utilizar el token generado del Sistema para la gestión de identidades entre dominios (SCIM)."
alias: /scim/automated_user_provisioning/

---

# Aprovisionamiento automático de usuarios {#automated-user-provisioning}

> El aprovisionamiento automático de usuarios te permite crear y administrar usuarios de Braze a través de una API en lugar de hacerlo manualmente en el panel. Braze lo admite mediante el Sistema para la gestión de identidades entre dominios (SCIM). Este artículo te explica qué información debes proporcionar, cómo generar tu token SCIM y dónde encontrar tu endpoint de la API SCIM.

{% multi_lang_include scim/scim_alerts.md alert='one_integration' %}

## Acceder a la configuración de aprovisionamiento SCIM {#accessing-scim-provisioning-settings}

{% alert important %}
La disponibilidad del aprovisionamiento SCIM depende de tu edición de la plataforma. Si esta característica no está en tu espacio de trabajo, contacta a tu administrador de éxito de cliente para obtener información.
{% endalert %}

1. En el panel de Braze, ve a **Configuración** > **Configuración de la empresa** > **Configuración de administrador** > **Aprovisionamiento SCIM** y selecciona **Configurar integración SCIM**.
2. En el paso **Configuración de Braze**, selecciona un método de aprovisionamiento y proporciona la configuración de acceso.

![Una página para configurar la integración SCIM con secciones para seleccionar un método de aprovisionamiento y proporcionar la configuración de acceso.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3. En el paso **Configuración del IdP**, sigue los pasos dentro de la plataforma para el método de aprovisionamiento seleccionado.

{% tabs %}
{% tab Okta - Braze app %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Okta integration' %}

Usa la opción **Okta - Braze app** si configuraste la aplicación de Braze para SAML SSO en Okta. Si configuraste una aplicación personalizada para SSO, sigue las instrucciones en la pestaña [Okta - Custom app integration]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning).

{% multi_lang_include scim/scim_alerts.md alert='idp_integration' idp='Okta' %}

## Paso 1: Configurar el aprovisionamiento SCIM {#step-1-set-up-scim-provisioning}

### Paso 1.1: Habilitar SCIM {#step-11-enable-scim}

1. En Okta, ve a **Applications** > **Applications** y selecciona **Create App Integration**. Selecciona **SAML 2.0** como método de inicio de sesión.
2. Completa los siguientes datos (que se encuentran en el [paso **Configuración del IdP**](#accessing-scim-provisioning-settings)) para crear una aplicación personalizada:
- Logotipo de la aplicación
- URL de inicio de sesión único
- URL de audiencia (ID de entidad SP)
3. Selecciona **Finish**.
4. Selecciona la pestaña **General**.
5. En la sección **App Settings**, selecciona **Edit**.
6. En el campo **Provisioning**, selecciona **SCIM**.

### Paso 1.2: Desactivar la visibilidad de la aplicación {#step-12-disable-application-visibility}

1. En el campo **Application visibility**, selecciona la casilla **Do not display application icon to user**. Esto evita que los usuarios accedan a SSO a través de la aplicación, que está destinada únicamente para SCIM.
2. Selecciona **Save**.

### Paso 1.3: Configurar la integración SCIM {#step-13-set-up-the-scim-integration}

1. Selecciona la pestaña **Provisioning**.
2. En **Settings** > **Integration** > **SCIM Connection**, selecciona **Edit** y completa los valores de los campos que aparecen en la tabla de la página **Setup SCIM provisioning**.

### Paso 1.4: Probar las credenciales de la API {#step-14-test-the-api-credentials}

Selecciona **Test API Credentials**. Si la integración es exitosa, aparece un mensaje de verificación y puedes guardar.

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

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Okta integration' %}

Usa la opción **Okta - Custom app integration** si configuraste una aplicación personalizada para SSO. Si configuraste la aplicación de Braze para SAML SSO en Okta, sigue las instrucciones en la pestaña [Okta - Braze app]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning).

{% multi_lang_include scim/scim_alerts.md alert='idp_integration' idp='Okta' %}

## Paso 1: Configurar el aprovisionamiento SCIM

### Paso 1.1: Habilitar SCIM

1. En Okta, ve a tu aplicación de Braze.
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

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Entra ID integration' %}

{% multi_lang_include scim/scim_alerts.md alert='idp_integration' idp='Entra ID' %}

## Paso 1: Configurar la aplicación de aprovisionamiento SCIM {#step-1-set-up-scim-provisioning-app}

### Paso 1.1: Iniciar sesión en el centro de administración de Microsoft Entra {#step-11-log-into-microsoft-entra-admin-center}

Inicia sesión en tu centro de administración de Microsoft Entra.

### Paso 1.2: Crear y configurar tu aplicación SCIM {#step-12-create-and-set-up-your-scim-app}

1. En el menú de navegación, ve a **Entra ID** > **Enterprise apps**.
2. Selecciona **New application**.
3. Selecciona **Create your own application**.
4. En el panel, ingresa un nombre para tu aplicación.
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

{% alert important %}
El atributo `userName` debe coincidir exactamente con la dirección de correo electrónico del usuario en Braze para que SCIM identifique y gestione correctamente a los usuarios. Los usuarios que fueron aprovisionados manualmente en Braze antes de que se habilitara SCIM no se convertirán automáticamente en usuarios gestionados por el IdP, incluso si se agregan a la aplicación SCIM. Su método de aprovisionamiento permanece manual.
{% endalert %}

## Paso 2: Asignar usuarios a la aplicación

1. Ve a **Manage** > **Users and Groups**.
2. Selecciona **Add user/group**.
3. Selecciona **None Selected** para asignar usuarios a la aplicación.
4. Selecciona el botón **Select** para confirmar la asignación.

{% endtab %}
{% tab Custom %}

## Paso 1: Configurar tus ajustes SCIM {#step-1-configure-your-scim-settings}

- **Espacio de trabajo predeterminado:** Selecciona el espacio de trabajo donde se deben agregar los nuevos usuarios de forma predeterminada. Si no especificas un espacio de trabajo en tu [solicitud de API SCIM]({{site.baseurl}}/post_create_user_account), Braze asigna a los usuarios a este espacio de trabajo.
- **Service Origin:** Ingresa el dominio de origen de tus solicitudes SCIM. Braze lo usa en el encabezado `X-Request-Origin` para verificar de dónde provienen las solicitudes.
- **Lista de IP permitidas (opcional):** Puedes restringir las solicitudes SCIM a direcciones IP específicas. Ingresa una lista separada por comas o un rango de direcciones IP a permitir. El encabezado `X-Request-Origin` en cada solicitud se usa para verificar la dirección IP de la solicitud contra la lista de permitidos.

## Paso 2: Generar un token SCIM {#step-2-generate-a-scim-token}

Después de completar los campos obligatorios, presiona **Generate SCIM token** para generar un token SCIM y ver tu endpoint de API SCIM. Asegúrate de copiar el token SCIM antes de navegar a otra página. **Este token aparece solo una vez.**

![Campos de endpoint de API SCIM y token SCIM mostrados con valores enmascarados y botones de copiar. Debajo del campo del token hay un botón de reinicio de token.]({% image_buster /assets/img/scim.png %})

Braze espera que todas las solicitudes SCIM contengan el token bearer de la API SCIM adjunto a través de un encabezado HTTP `Authorization`.

{% endtab %}
{% endtabs %}