---
nav_title: Píxel de apertura y seguimiento de clics
article_title: Píxel de apertura y seguimiento de clics en correos electrónicos
page_order: 9
page_type: reference
description: "Este artículo de referencia explica cómo implementar el píxel de apertura y el seguimiento de clics."

---

# Píxel de apertura y seguimiento de clics en correos electrónicos {#email-open-pixel-and-click-tracking}

> El [seguimiento de píxel de apertura]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement) y el seguimiento de clics se pueden activar o desactivar para cada perfil de usuario. Esta flexibilidad te ayuda a cumplir con las leyes de privacidad regionales, en las que un perfil de usuario individual podría indicar que ya no desea ser rastreado.

## Activar el seguimiento de píxel de apertura o de clics {#turning-on-open-pixel-or-click-tracking}

Al importar o actualizar un perfil de usuario a través de la [API]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields), [CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) o la [ingesta de datos en la nube (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion), hay dos campos disponibles que puedes modificar:

- `email_open_tracking_disabled`: Acepta `true` o `false`. Establécelo en `false` para añadir el píxel de seguimiento de apertura a todos los correos electrónicos futuros enviados a este usuario.
- `email_click_tracking_disabled`: Acepta `true` o `false`. Establécelo en `false` para añadir el seguimiento de clics a todos los enlaces dentro de un correo electrónico futuro enviado a este usuario.

Como referencia, esta información se refleja en el perfil de usuario en la sección de correo electrónico **Configuración de contacto**, ubicada en la pestaña **Engagement**.

![Campos de píxel de seguimiento de apertura y clics de correo electrónico en la pestaña Engagement del perfil de un usuario]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

## Requisitos de los enlaces de seguimiento de clics {#click-tracking-link-requirements}

El seguimiento de clics de Braze solo reescribe los enlaces que utilizan URL con `http://` o `https://`. Los enlaces que utilizan otros esquemas, como `mailto:` o `tel:`, no se rastrean con seguimiento de clics.

Para rastrear clics en números de teléfono o direcciones de correo electrónico, utiliza una URL de redireccionamiento con `https://` que reenvíe al destino `tel:` o `mailto:`.