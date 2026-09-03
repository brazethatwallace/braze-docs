---
nav_title: Aprovisionamiento SAML justo a tiempo
article_title: Aprovisionamiento SAML justo a tiempo
page_order: 1
page_type: tutorial
description: "Este artículo te guiará sobre cómo configurar el aprovisionamiento SAML justo a tiempo para permitir que los nuevos usuarios de la empresa creen una cuenta de Braze en su primer inicio de sesión."

---

# Aprovisionamiento SAML justo a tiempo {#saml-just-in-time-provisioning}

> El aprovisionamiento justo a tiempo funciona con [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup) para permitir que los nuevos usuarios de la empresa creen una cuenta de Braze en su primer inicio de sesión. Esto elimina la necesidad de que los administradores creen manualmente una cuenta para un nuevo usuario de la empresa, elijan sus permisos, lo asignen a un espacio de trabajo y esperen a que active su cuenta.

Como medida de seguridad, el aprovisionamiento SAML justo a tiempo (JITP) solo funciona para usuarios con dominios de correo electrónico que ya existen en tu empresa. JITP solo es posible para dominios en los que ya existe al menos un desarrollador confirmado y sin suplantación de identidad en la empresa.

Por ejemplo, supongamos que la cuenta `jon.smith@decorumsoft.com` puede usar JITP para iniciar sesión en Decorumsoft. La cuenta `jane.smith@decorumsoft.com` tiene el mismo dominio y también se le puede permitir el aprovisionamiento. Sin embargo, si intentas usar JITP con `jon.smith@decorumsoft.eu`, el aprovisionamiento no se permitirá porque no existe una cuenta `decorumsoft.eu` dentro del panel de Braze de Decorumsoft.

Para hacer una excepción para una empresa, ponte en contacto con [Soporte]({{site.baseurl}}/braze_support).

## Requisitos previos {#prerequisites}

SAML JITP requiere que SAML SSO esté configurado e integrado. No es compatible con Google SSO y solo es compatible con flujos de trabajo de inicio de sesión iniciados por el proveedor de identidad (IdP-initiated).

| Requisito | Detalles |
|---|---|
| SAML SSO | Configurado y probado antes de habilitar JITP. Consulta [Configuración de SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup). |
| Inicio de sesión iniciado por IdP | Los usuarios deben iniciar sesión a través del portal de tu IdP en el primer inicio de sesión. El inicio de sesión iniciado por SP por sí solo no aprovisiona nuevos usuarios. |
| Dominio de correo electrónico | El dominio de correo electrónico del usuario ya debe existir en tu empresa (al menos un desarrollador confirmado, sin suplantación de identidad, con ese dominio). |
| Habilitación de la empresa | Braze debe habilitar la característica `saml_jit_provisioning` para tu empresa antes de que aparezca el interruptor **Aprovisionamiento automático de usuarios**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos de JITP" }

{% alert important %}
El aprovisionamiento justo a tiempo de SAML debe ser habilitado para tu empresa por Braze. Ponte en contacto con tu director de cuentas o con [soporte de Braze]({{site.baseurl}}/braze_support) si el interruptor **Aprovisionamiento automático de usuarios** no está disponible.
{% endalert %}

## Cómo funciona JITP {#how-jitp-works}

Cuando JITP está habilitado y un nuevo usuario inicia sesión a través de tu IdP por primera vez:

1. Braze valida la aserción SAML y comprueba que el dominio de correo electrónico del usuario está permitido para JITP.
2. Braze crea una cuenta de usuario en el panel utilizando el correo electrónico de la aserción SAML.
3. Braze asigna el espacio de trabajo y el conjunto de permisos predeterminados configurados en **Configuración de seguridad**.
4. El usuario puede acceder a Braze de inmediato sin necesidad de una invitación o paso de activación por separado.

JITP no actualiza los permisos de los usuarios existentes. Solo crea cuentas para usuarios que aún no existen en tu empresa.

## Configuración del aprovisionamiento justo a tiempo (JITP) de SAML {#setting-up-saml-just-in-time-provisioning-jitp}

Pide a un administrador de Braze que haga lo siguiente:

1. Ve a **Configuración** > **Configuración de la empresa** > **Configuración de administrador** > **Configuración de seguridad**.
2. En la sección **SAML SSO**, activa la opción **Aprovisionamiento automático de usuarios**.
3. Selecciona un espacio de trabajo predeterminado para añadir un nuevo usuario de la empresa.
4. Selecciona el conjunto de permisos predeterminado que se asignará a ese nuevo usuario de la empresa. Para aprender a crear un conjunto de permisos, consulta [Configuración de permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

{% alert note %}
Si tu empresa utiliza permisos granulares, revisa el conjunto de permisos predeterminado después de la migración para confirmar que los nuevos usuarios JITP reciben el acceso previsto.
{% endalert %}

{: start="5"}
5. Selecciona **Guardar cambios**.
6. En la configuración de tu proveedor de SSO, añade a todos los usuarios que necesiten acceso a Braze en el directorio de tu proveedor de SSO.
7. Indica a los usuarios que accedan a Braze a través del portal de tu IdP para su primer inicio de sesión. Después, el botón de inicio de sesión único de SAML se mostrará para futuros inicios de sesión.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cómo desactivo SAML JITP? {#how-do-i-disable-saml-jitp}

Después de configurar JITP, debes [contactar con soporte]({{site.baseurl}}/braze_support) para que lo desactiven.

### ¿Puede JITP asignar diferentes permisos por usuario? {#can-jitp-assign-different-permissions-per-user}

No. Todos los usuarios creados por JITP reciben el espacio de trabajo y el conjunto de permisos predeterminados configurados en **Configuración de seguridad**. Para asignar un acceso diferente, crea los usuarios manualmente o utiliza el [aprovisionamiento automatizado de usuarios con SCIM]({{site.baseurl}}/scim/automated_user_provisioning).

### ¿Funciona JITP con el inicio de sesión iniciado por SP? {#does-jitp-work-with-sp-initiated-login}

No. JITP solo se ejecuta durante el inicio de sesión iniciado por IdP, cuando un usuario accede desde el portal de tu proveedor de identidad.

## Solución de problemas {#troubleshooting}

### El usuario no fue aprovisionado en el primer inicio de sesión con SSO {#user-was-not-provisioned-on-first-sso-sign-in}

Comprueba lo siguiente:

- JITP está habilitado y guardado en **Configuración de seguridad**.
- El usuario inició sesión a través del portal del IdP (iniciado por el IdP), no solo desde la página de inicio de sesión de Braze.
- El dominio de correo electrónico del usuario ya existe en tu empresa.
- La aserción SAML incluye un atributo `email` válido que coincide con la dirección con la que el usuario inicia sesión.

### El botón de inicio de sesión único no aparece con Microsoft Entra ID {#single-sign-on-button-doesnt-appear-with-microsoft-entra-id}

El campo **Sign-On URL** en el formulario **Basic SAML Configuration** de Microsoft Entra para Braze puede provocar que los usuarios solo vean una opción de contraseña, y no un botón de SSO, con el inicio de sesión iniciado por el IdP. Para evitar este problema, deja el campo **Sign-On URL** en blanco al configurar Braze en tu centro de administración de Microsoft Entra.