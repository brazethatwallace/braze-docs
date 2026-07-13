---
nav_title: Compatibilidad con visionOS
article_title: Compatibilidad con visionOS
page_order: 7.2
platform:
  - iOS
description: "Este artículo cubre las características compatibles con visionOS."
---

# Compatibilidad con visionOS {#visionos-support}

> A partir de [Braze Swift SDK 8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800), puedes aprovechar Braze con [visionOS](https://developer.apple.com/visionos/), la plataforma de computación espacial de Apple para el Apple Vision Pro. Para ver una aplicación visionOS de ejemplo que utiliza Braze, consulta [Aplicaciones de ejemplo]({{site.baseurl}}/developer_guide/references?tab=swift).

## Características totalmente compatibles {#fully-supported-features}

La mayoría de las características disponibles en iOS también están disponibles en visionOS, entre ellas:

- Análisis (sesiones, eventos personalizados, compras, etc.)
- Mensajería dentro de la aplicación (modelos de datos e interfaz de usuario)
- Content Cards (modelos de datos e interfaz de usuario)
- Notificaciones push (visibles para el usuario con botones de acción y notificaciones silenciosas)
- Conmutadores de características
- Análisis de ubicación

## Características parcialmente compatibles {#partially-supported-features}

Algunas características solo son parcialmente compatibles con visionOS, pero es probable que Apple las aborde en el futuro:

- Notificaciones push enriquecidas
  - Se admiten imágenes.
  - Los GIF y videos muestran la miniatura de vista previa, pero no se pueden reproducir.
  - No se admite la reproducción de audio.
- Push Stories
  - Se puede desplazar y seleccionar la página de Push Stories.
  - No es posible navegar entre páginas de Push Stories utilizando **Next**.

## Características no compatibles {#unsupported-features}

- No se admite la monitorización de geovallas. Apple no ha puesto a disposición de visionOS las API de Core Location para la monitorización de regiones.
- No se admiten las actividades en vivo. Actualmente, ActivityKit solo está disponible en iOS y iPadOS.