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

Utiliza las páginas de inicio para hacer crecer tu audiencia, capturar datos de usuario, promocionar ofertas especiales y apoyar campañas multicanal. Para una referencia de los bloques de arrastrar y soltar de las páginas de inicio, consulta [Bloques de editor (páginas de inicio)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).

{% alert note %}
La disponibilidad de páginas de inicio y dominios personalizados depende de tu paquete de Braze. Ponte en contacto con tu director de cuentas o CSM or administrador de éxito de cliente or administrador de éxito de cliente para empezar.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## Requisitos previos {#prerequisites}

Antes de poder acceder, crear y publicar páginas de inicio, necesitas [permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) de administrador o todos los permisos siguientes:

- Ver páginas de inicio
- Editar borradores de páginas de inicio
- Publicar páginas de inicio

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Niveles de plan {#plan-tiers}

El número de páginas de inicio publicadas, dominios personalizados y características que puedes utilizar depende de tu tipo de plan: gratuito o pro (incremental).

| Característica                                                                                                   | Nivel gratuito     | Nivel pro (incremental)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Páginas de inicio publicadas                                                                 | Cinco por empresa | 20 adicionales |
| Dominios personalizados          | Uno por empresa | Cinco adicionales |
| [Personalización con Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages) | No disponible | Disponible |
| Campos de formulario prerrellenados | No disponible | Disponible |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Niveles de plan" }

## Límites de velocidad {#rate-limits}

Braze aplica un límite de velocidad de 500 solicitudes cada tres segundos (aproximadamente 167 solicitudes por segundo) por espacio de trabajo para páginas de destino no almacenadas en caché. Este límite ayuda a mantener el rendimiento y la fiabilidad del sistema durante periodos de alto tráfico.

Las visualizaciones de páginas de destino almacenadas en caché no cuentan para este límite. Para saber cómo afecta el almacenamiento en caché al tráfico, consulta [¿Pueden las páginas de destino manejar escenarios de alto tráfico?](#can-landing-pages-handle-high-traffic-scenarios).

## Añadir Google Tag Administrador a una página de destino {#adding-google-tag-manager-to-a-landing-page}

Para añadir Google Tag Administrador a tus páginas de destino, añade un bloque de **Custom Code** a tu página de destino en el editor de arrastrar y soltar, luego inserta el código de Tag Administrador en el bloque. Asegúrate de añadir una capa de datos antes del código de Tag Administrador, como en este ejemplo:

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

Para más información sobre la implementación de Google Tag Administrador, consulta la [documentación de Google](https://developers.google.com/tag-platform/tag-manager/datalayer#installation).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuál es el tamaño máximo de las páginas de inicio? {#whats-the-maximum-size-for-landing-pages}

El tamaño del cuerpo de la página de inicio puede ser de hasta 500 KB.

### ¿Pueden las páginas de inicio gestionar escenarios de alto tráfico? {#can-landing-pages-handle-high-traffic-scenarios}

Sí. Las páginas de inicio no personalizadas gestionan eficazmente los escenarios de alto tráfico. Cuando se solicita una página de inicio por primera vez, Braze la almacena en caché a través de Cloudflare. Las solicitudes posteriores del mismo enlace se sirven desde la caché, lo que ayuda durante los períodos de alto tráfico. Esta caché dura 24 horas, y las vistas de páginas en caché no cuentan para los [límites de velocidad](#rate-limits).

Las páginas de inicio personalizadas utilizan una caché de Cloudflare más corta y generan más solicitudes no almacenadas en caché a Braze. Esas solicitudes no almacenadas en caché están sujetas al límite de velocidad por espacio de trabajo descrito en [Límites de velocidad](#rate-limits).

Para conocer los límites de tamaño y otras recomendaciones de rendimiento para páginas personalizadas, consulta [Consideraciones de personalización]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#personalization-considerations).

### ¿Existen requisitos técnicos para publicar una página de inicio? {#are-there-any-technical-requirements-to-publish-a-landing-page}

No, no hay ningún requisito técnico.

### ¿Hay un editor HTML para las páginas de inicio? {#is-there-an-html-editor-for-landing-pages}

Sí. Utiliza el bloque **Custom Code** en el editor de arrastrar y soltar para añadir o editar HTML. Para interactuar con el SDK or kit de desarrollo de software de Braze desde tu código personalizado, consulta [Puente JavaScript para páginas de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge). Para conectar una interfaz completamente personalizada a un formulario de página de inicio, consulta [Crear bloques de formulario personalizados]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks).

### ¿Puedo usar iframes en las páginas de inicio? {#can-i-use-iframes-on-landing-pages}

Sí. Añade un bloque **Custom Code** en el editor de arrastrar y soltar e incluye un elemento iframe con la URL del contenido que deseas incrustar.

Si el sitio web incrustado restringe el uso de marcos mediante `frame-ancestors` en su Política de seguridad de contenido (CSP) o `X-Frame-Options`, es posible que la página no se cargue en el iframe. Braze no puede anular esa configuración; el sitio incrustado debe estar configurado para permitir el dominio de tu página de inicio.

### ¿Puedo crear un webhook dentro de una página de inicio? {#can-i-create-a-webhook-inside-a-landing-page}

No, pero el evento **Submitted a Landing Page form** puede actuar como desencadenante para Canvas o Campaigns de webhook:

- **Canvas:** Usa el evento **Submitted a Landing Page form** como desencadenante de entrada de Canvas y añade un paso de webhook.
- **Campaign:** Usa el evento **Submitted a Landing Page form** para desencadenar con base en el envío del formulario.

Cuando la página no se envía a través de un canal de Braze (como a través de un sitio web o un anuncio), es posible que se cree un nuevo perfil de usuario al enviar el formulario, incluso si esa persona ya existe en Braze. Para gestionar esto, configura un Canvas desencadenado por **Submitted a Landing Page form** y añade un paso de webhook de Braze a Braze que llame al endpoint [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) para fusionar el nuevo perfil con el existente.

Cuando usas la etiqueta de Liquid `landing_page_url` para compartir la página, los envíos de formularios se vinculan automáticamente al perfil de usuario existente. Luego puedes hacer referencia a los atributos de usuario enviados en la página de inicio a través de Liquid para la creación de plantillas posteriores.