---
nav_title: Contentsquare
article_title: Contentsquare
description: "Este artículo de referencia describe la asociación entre Braze y Contentsquare, una plataforma de análisis de la experiencia digital que te permite mejorar la relevancia y las tasas de conversión de tus campañas orientando los mensajes en función de la experiencia digital de tus clientes."
alias: /partners/contentsquare/
page_type: partner
search_tag: Partner

---

# Contentsquare

> [Contentsquare](https://contentsquare.com/) es una plataforma de análisis de la experiencia digital que permite una comprensión sin precedentes de la experiencia del cliente.

_Esta integración es mantenida por Contentsquare._

## Sobre la integración {#about-the-integration}

La integración de Braze y Contentsquare te permite enviar señales en directo (fraude, señales de frustración, etc.) como eventos personalizados en Braze. Aprovecha la información sobre la experiencia de Contentsquare para mejorar la relevancia y las tasas de conversión de tus campañas orientando los mensajes en función de la experiencia digital y el lenguaje corporal de tus clientes.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Contentsquare | Se requiere una cuenta de Contentsquare para aprovechar esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos `users.track`. Para crear una nueva clave en el panel de Braze, ve a **Settings** > **API Keys**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({% image_buster /assets/img/contentsquare_custom_events.png %}). Tu punto de conexión dependerá de la URL de Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

Algunos casos de uso habituales de Braze y Contentsquare incluyen:
- Hiperpersonalizar mensajes basados en la intención del cliente haciendo aflorar los datos de la experiencia del cliente en Braze.
- Reorientar a los clientes en función de su comportamiento digital, sus dudas, su frustración y su intención.
- Identificar malas experiencias dentro de Contentsquare y recuperar a los clientes con mensajes específicos y ofertas de retención.
- Recuperar a los clientes en riesgo enviándoles mensajes más relevantes y empáticos en el momento y lugar adecuados.

## Integración {#integration}

Para integrar Contentsquare en Braze, debes solicitar la instalación de una integración "Live Signals" desde el catálogo de integraciones de Contentsquare:

1. En Contentsquare, haz clic en **Console** en el menú **Settings**. Esto te redirigirá al proyecto en el que estás trabajando actualmente.
2. En la página **Projects**, ve a la pestaña **Integrations** y haz clic en el botón **+ Add integration**.
3. En el catálogo de integraciones, localiza la integración **Live Signals** y haz clic en **Add**. El equipo de Contentsquare se pondrá en contacto contigo para configurar el fragmento de código para enviar señales en vivo a Braze.
4. Contentsquare procesará ahora tu integración. El texto del indicador se actualizará una vez finalizada la integración.

Para más información, consulta [Solicitar una integración de Contentsquare](https://uxanalyser.zendesk.com/hc/en-gb/articles/4405613239186).

## Uso de esta integración {#using-this-integration}

Una vez completada la integración, los eventos personalizados de Contentsquare estarán disponibles para ser utilizados en tus Campaigns y Canvas. Puedes comprobar qué eventos se envían a Braze desde **Data Settings** > **Custom Events**.

![Datos de señales en vivo de Contentsquare en la pestaña de eventos personalizados de Braze]({% image_buster /assets/img/contentsquare_custom_events.png %})