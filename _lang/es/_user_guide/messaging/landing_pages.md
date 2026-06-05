---
nav_title: Páginas de inicio
article_title: Páginas de inicio
page_order: 8
guide_top_header: "Páginas de inicio"
description: "Este artículo contiene recursos sobre cómo crear y personalizar páginas de inicio de Braze."
alias: /landing_pages/
---

# Acerca de las páginas de inicio {#about-landing-pages}

> Las páginas de inicio de Braze son páginas web independientes que pueden impulsar tu estrategia de adquisición e interacción de usuarios.

Utiliza las páginas de inicio para hacer crecer tu audiencia, capturar datos de usuario, promocionar ofertas especiales y apoyar campañas multicanal. Para una referencia de los bloques de arrastrar y soltar de las páginas de inicio, consulta [Bloques de editor (páginas de inicio)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=landing%20pages).

{% alert note %}
La disponibilidad de páginas de inicio y dominios personalizados depende de tu paquete de Braze. Ponte en contacto con tu director de cuentas o administrador del éxito del cliente para empezar.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## Requisitos previos {#prerequisites}

Antes de poder acceder, crear y publicar páginas de inicio, necesitas [permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#list-of-permissions) de administrador o todos los permisos siguientes:

- View Landing Pages
- Edit Landing Page Drafts
- Publish Landing Pages

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Niveles de plan {#plan-tiers}

El número de páginas de inicio publicadas, dominios personalizados y características que puedes usar depende de tu tipo de plan: gratuito o de pago (incremental).

| Característica | Nivel gratuito | Nivel de pago (incremental) |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Páginas de inicio publicadas | Cinco por empresa | 20 adicionales |
| Dominios personalizados | Uno por empresa | Cinco adicionales |
| [Personalización con Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages/) | No disponible | Disponible |
| Campos de formulario prerrellenados | No disponible | Disponible |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Niveles de plan" }

## Añadir Google Tag Manager a una página de inicio {#adding-google-tag-manager-to-a-landing-page}

Para añadir Google Tag Manager a tus páginas de inicio, agrega un bloque de **Custom Code** a tu página de inicio en el editor de arrastrar y soltar, y luego inserta el código de Tag Manager en el bloque. Asegúrate de añadir una capa de datos antes del código de Tag Manager, como en este ejemplo:

```
<script>
window.dataLayer = window.dataLayer || [];
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');</script>
<!-- End Google Tag Manager -->
```

Para más detalles sobre la implementación de Google Tag Manager, consulta la [documentación de Google](https://developers.google.com/tag-platform/tag-manager/datalayer#installation).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuál es el tamaño máximo para las páginas de inicio? {#whats-the-maximum-size-for-landing-pages}

El tamaño del cuerpo de la página de inicio puede ser de hasta 500 KB.

### ¿Pueden las páginas de inicio gestionar escenarios de alto tráfico? {#can-landing-pages-handle-high-traffic-scenarios}

Sí, las páginas de inicio no personalizadas pueden gestionar escenarios de alto tráfico de forma eficaz. Cuando se solicita por primera vez una página de inicio no personalizada, Braze la almacena en caché a través de Cloudflare. Esto significa que todas las solicitudes posteriores del mismo enlace se sirven desde la caché, por lo que el rendimiento no se degrada en solicitudes de alto volumen. Esta caché dura 24 horas, y las vistas de páginas en caché no cuentan para los límites de velocidad.

Para páginas de inicio personalizadas (que usan personalización con Liquid), los límites de velocidad se aplican a las solicitudes no almacenadas en caché. Para mantener un rendimiento óptimo, consulta [Consideraciones de personalización]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages/#personalization-considerations).

### ¿Hay algún requisito técnico para publicar una página de inicio? {#are-there-any-technical-requirements-to-publish-a-landing-page}

No, no hay ningún requisito técnico.

### ¿Hay un editor HTML para las páginas de inicio? {#is-there-an-html-editor-for-landing-pages}

Sí. Usa el bloque **Custom Code** en el editor de arrastrar y soltar para añadir o editar HTML.

### ¿Puedo crear un webhook dentro de una página de inicio? {#can-i-create-a-webhook-inside-a-landing-page}

No, pero el evento **Submitted a Landing Page form** puede actuar como desencadenante para Canvas o campañas de webhook:

- **Canvas:** Usa el evento **Submitted a Landing Page form** como desencadenante de entrada de Canvas y añade un paso de webhook.
- **Campaign:** Usa el evento **Submitted a Landing Page form** para desencadenar en función del envío del formulario.

Cuando la página no se envía a través de un canal de Braze (por ejemplo, a través de un sitio web o un anuncio), puede crearse un nuevo perfil de usuario al enviar el formulario, incluso si esa persona ya existe en Braze. Para gestionar esto, configura un Canvas desencadenado por **Submitted a Landing Page form** y añade un paso de webhook de Braze a Braze que llame al punto de conexión [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) para fusionar el nuevo perfil con el existente.

Cuando usas la etiqueta de Liquid `landing_page_url` para compartir la página, los envíos de formularios se vinculan automáticamente al perfil de usuario existente. Después puedes hacer referencia a los atributos de usuario enviados en la página de inicio a través de Liquid para la creación de plantillas posteriores.