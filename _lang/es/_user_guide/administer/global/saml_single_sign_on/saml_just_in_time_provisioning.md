---
nav_title: Aprovisionamiento SAML justo a tiempo
article_title: Aprovisionamiento SAML justo a tiempo
page_order: 1
page_type: tutorial
description: "Este artículo te guiará sobre cómo configurar el aprovisionamiento SAML justo a tiempo para permitir que los nuevos usuarios de la empresa creen una cuenta de Braze en su primer inicio de sesión."

---

# Aprovisionamiento SAML justo a tiempo

> El aprovisionamiento justo a tiempo funciona con [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/) para permitir que los nuevos usuarios de la empresa creen una cuenta de Braze en su primer inicio de sesión. Esto elimina la necesidad de que los administradores creen manualmente una cuenta para un nuevo usuario de la empresa, elijan sus permisos, lo asignen a un espacio de trabajo y esperen a que active su cuenta.

Como medida de seguridad, el aprovisionamiento SAML justo a tiempo (JITP) solo funciona para usuarios con dominios de correo electrónico que ya existen en tu empresa. JITP solo es posible para dominios en los que ya existe al menos un desarrollador confirmado y sin suplantación de identidad en la empresa.

Por ejemplo, supongamos que la cuenta `jon.smith@decorumsoft.com` puede usar JITP para iniciar sesión en Decorumsoft. La cuenta `jane.smith@decorumsoft.com` tiene el mismo dominio y también se le puede permitir el aprovisionamiento. Sin embargo, si intentas usar JITP con `jon.smith@decorumsoft.eu`, el aprovisionamiento no se permitirá porque no existe una cuenta `decorumsoft.eu` dentro del panel de Braze de Decorumsoft.

Para hacer una excepción para una empresa, ponte en contacto con [Soporte]({{site.baseurl}}/braze_support/).

## Requisitos previos

SAML JITP requiere que SAML SSO esté configurado e integrado. No es compatible con Google SSO y solo es compatible con flujos de trabajo de inicio de sesión iniciados por el proveedor de identidad (IdP-initiated).

## Configuración del aprovisionamiento SAML justo a tiempo (JITP)

Pide a un administrador de Braze que haga lo siguiente:

1. Ve a **Configuración** > **Configuración de administrador** > **Configuración de seguridad**.
2. En la sección **SAML SSO**, activa la opción **Automatic user provisioning**.
3. Selecciona un espacio de trabajo predeterminado para añadir un nuevo usuario de la empresa.
4. Selecciona el conjunto de permisos predeterminado para asignar a ese nuevo usuario de la empresa. Para aprender a crear un conjunto de permisos, consulta [Configuración de permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/).
6. Selecciona **Guardar cambios** en la parte inferior de la página.
7. En la configuración de tu proveedor de SSO, añade a todos los usuarios que necesiten acceso a Braze en el directorio de tu proveedor de SSO.
8. Indica a los usuarios que accedan a Braze a través del portal de tu IdP para su primer inicio de sesión. Después de esto, el botón de inicio de sesión único SAML se mostrará para futuros inicios de sesión.

## Preguntas frecuentes

### ¿Cómo desactivo SAML JITP?

Después de configurar JITP, debes [ponerte en contacto con Soporte]({{site.baseurl}}/braze_support/) para que lo desactiven.

## Solución de problemas

### El botón de inicio de sesión único no aparece con Microsoft Entra ID

El campo **Sign-On URL** en el formulario **Basic SAML Configuration** de Microsoft Entra para Braze puede hacer que los usuarios solo vean una opción de contraseña, no un botón de SSO, con el inicio de sesión iniciado por IdP. Para evitar este problema, deja el campo **Sign-On URL** en blanco al configurar Braze en tu centro de administración de Microsoft Entra.