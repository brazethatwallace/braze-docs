---
nav_title: Píxel de apertura y seguimiento de clics
article_title: Píxel de apertura y seguimiento de clics en correos electrónicos
page_order: 9
page_type: reference
description: "Este artículo de referencia explica cómo implementar el píxel de apertura y el seguimiento de clics."

---

# Píxel de apertura y seguimiento de clics en correos electrónicos

> El [seguimiento de píxel de apertura]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#changing-location-of-tracking-pixel) y el seguimiento de clics se pueden activar o desactivar para cada perfil de usuario. Esta flexibilidad te ayuda a cumplir con las leyes de privacidad regionales, en las que un perfil de usuario individual podría indicar que ya no desea ser rastreado.

## Activar el píxel de apertura o el seguimiento de clics

Al importar o actualizar un perfil de usuario a través de la [API]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields), [CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/#csv) o [Ingesta de datos de Cloud (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/), hay dos campos disponibles que puedes modificar:

- `email_open_tracking_disabled`: Acepta `true` o `false`. Establécelo en `false` para añadir el píxel de seguimiento de apertura a todos los correos electrónicos futuros enviados a este usuario. Disponible solo para SparkPost y SendGrid.
- `email_click_tracking_disabled`: Acepta `true` o `false`. Establécelo en `false` para añadir el seguimiento de clics a todos los enlaces dentro de un correo electrónico futuro enviado a este usuario. Disponible solo para SparkPost y SendGrid.

Como referencia, esta información se refleja en el perfil de usuario en la **Configuración de contacto** de correo electrónico, ubicada en la pestaña **Interacción**.

![Campos de píxel de seguimiento de apertura y clics en correo electrónico en la pestaña Interacción del perfil de un usuario]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}