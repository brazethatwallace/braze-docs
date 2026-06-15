---
nav_title: Braze Go
permalink: "/braze_go/"
hidden: true
noindex: true
hide_toc: true
---

# Braze Go

> Braze Go ofrece acceso simplificado a la plataforma de interacción con los clientes de Braze para ayudar a tus equipos de marketing a empezar en cualquier lugar y llegar a todas partes. Diseñado para la simplicidad y la eficiencia, Braze Go está adaptado para mercados emergentes seleccionados.

{% alert important %}
Braze Go no está disponible en todos los mercados. Si te interesa obtener más información sobre Braze Go, ponte en contacto con tu director de cuentas.
{% endalert %}

Braze Go ofrece toda la misma funcionalidad que Braze, con los siguientes cambios específicos en estas características:

- Puedes tener hasta 30 campañas activas.
- Puedes tener hasta 20 Canvas activos.
- El límite de velocidad predeterminado total de la REST API es de 50 000 por hora, por espacio de trabajo.
    - Para uso fuera de Braze Go, obtén más información sobre los [límites de la REST API]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type).
- La retención de datos de interacción de campañas y Canvas es de 2 meses sin restauración.
    - Para uso fuera de Braze Go, obtén más información sobre la [disponibilidad de datos de interacción de mensajería]({{site.baseurl}}/messaging_interaction_data/).

{% alert note %}
Los datos de interacción de campañas y Canvas son diferentes de los datos de Snowflake y no tienen ningún efecto en absoluto.
{% endalert %}

- Los webhooks de Braze a Braze no son compatibles.
- Los filtros relacionados con etiquetas no son compatibles, específicamente los siguientes filtros:
    - Clicked or Opened Campaign or Canvas with Tag
    - Last Received Message from Campaign or Canvas with Tag
    - Received Campaign or Canvas with Tag
- Braze también puede implementar una política de retención de datos para eventos de perfil de usuario y datos de compra que elimine eventos, compras o ambos con más de 1 año de antigüedad que no se hayan vuelto a realizar en 1 año. Sin embargo, estos datos seguirían estando disponibles en las extensiones de segmento SQL durante 2 años.

Si se actualiza alguna funcionalidad mencionada anteriormente, se reflejará en este artículo y se indicará en nuestras [notas de la versión]({{site.baseurl}}/help/release_notes/#most-recent-braze-release-notes).