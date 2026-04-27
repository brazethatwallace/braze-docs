---
nav_title: Junio
page_order: 7
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de junio de 2020."
---
# Junio de 2020 {#june-2020}

## Informes de retención {#retention-reports}

Los informes de retención ofrecen ahora retención por rangos para [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/test_campaigns/retention_reports/) y [Canvas]({{site.baseurl}}/user_guide/analytics/reports/retention_reports/). La retención por rangos mide cuántos usuarios vuelven y realizan un evento de retención seleccionado durante intervalos de tiempo específicos.

## Actualizaciones de la API de seguimiento de usuarios {#user-track-api-updates}

El [punto de conexión `users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) tiene ahora una tasa predeterminada de 50 000 solicitudes de API por minuto para las empresas del dashboard creadas después del 2 de junio de 2020. Las empresas existentes creadas antes de esta fecha y sus espacios de trabajo seguirán pudiendo realizar solicitudes ilimitadas de API al punto de conexión `users/track`.

 Braze está imponiendo este valor predeterminado en nuestro punto de conexión más utilizado de cara al cliente como un paso hacia nuestros objetivos de estabilidad y fiabilidad para nuestra API e infraestructura. El límite impuesto es muy liberal y afectará a muy pocas empresas del dashboard y a sus operaciones habituales. En caso de que necesites aumentar este límite, ponte en contacto con tu administrador del éxito del cliente o con nuestro equipo de soporte para solicitar un aumento.