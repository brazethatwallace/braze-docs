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

Utiliza las páginas de inicio para hacer crecer tu audiencia, capturar datos de usuario, promocionar ofertas especiales y apoyar campañas multicanal.

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

El número de páginas de inicio publicadas y dominios personalizados que puedes usar depende de tu tipo de plan: gratuito o de pago (incremental).

| Característica                                                                                                   | Nivel gratuito     | Nivel de pago (incremental)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Páginas de inicio publicadas                                                                 | Cinco por empresa | 20 adicionales |
| Dominios personalizados          | Uno por empresa | Cinco adicionales |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

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

### ¿Hay algún requisito técnico para publicar una página de inicio? {#are-there-any-technical-requirements-to-publish-a-landing-page}

No, no hay ningún requisito técnico.

### ¿Hay un editor HTML para las páginas de inicio? {#is-there-an-html-editor-for-landing-pages}

Sí. Usa el bloque **Custom Code** en el editor de arrastrar y soltar para añadir o editar HTML.

### ¿Puedo crear un webhook dentro de una página de inicio? {#can-i-create-a-webhook-inside-a-landing-page}

No, esto no es compatible actualmente.