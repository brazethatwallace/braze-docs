---
nav_title: Inbox Monster
article_title: Inbox Monster
alias: /partners/inbox_monster/
description: "Este artículo de referencia describe la asociación entre Braze e Inbox Monster, una herramienta de marketing por correo electrónico en línea que permite a los clientes de Braze obtener información valiosa sobre la capacidad de entrega y análisis creativos para potenciar el rendimiento del buzón de entrada."
page_type: partner
search_tag: Partner

---

# Inbox Monster

> [Inbox Monster](https://inboxmonster.com/) es una plataforma de señales de buzón de entrada que ayuda a las marcas empresariales a aterrizar cada envío. Es una línea de productos integrada de soluciones de capacidad de entrega, renderización creativa y monitorización de servicio de mensajes cortos, que capacita a los equipos modernos de CRM or administración de las relaciones con el cliente or administración de las relaciones con el cliente (CRM or administración de las relaciones con el cliente) y acaba con los sustos de los envíos.

La integración de Braze e Inbox Monster te permite eliminar las pruebas manuales de listas de semillas, automatizar la creación de señales potentes y procesables de colocación en el buzón de entrada, simplificar el proceso de revisión y aprobación de activos creativos de correo electrónico y obtener información valiosa sobre la capacidad de entrega. También puedes importar fácilmente plantillas de correo electrónico para diagnósticos creativos y vistas previas de dispositivos.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cuenta de la plataforma Inbox Monster | Se requiere una cuenta en la plataforma Inbox Monster para beneficiarse de esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con los siguientes permisos:  <br> - `messages.send` <br>  - `templates.email.create`<br> - `templates.email.update` <br> - `templates.email.info`<br> - `templates.email.list` <br><br> Y con las siguientes IP en la lista blanca: <br> - `3.136.16.19` <br>  - `3.140.233.31`<br> - `18.220.127.138` <br><br> Se puede crear en el panel de Braze desde **Settings** > **APIs and Identifiers** en la pestaña **API Keys** |
| Identificador de la aplicación Braze | Un identificador de aplicación Braze. <br><br>Puedes encontrarlo en el panel de Braze, en **Settings** > **APIs and Identifiers**, en la pestaña **App Identifiers**. |
| Punto de conexión de Braze | [Tu punto de conexión de Braze]({{site.baseurl}}/api/basics/#endpoints) se corresponde con la URL de tu panel de Braze.<br><br> Por ejemplo, si la URL de tu panel es `https://dashboard-03.braze.com`, tu punto de conexión será `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Para integrar Inbox Monster, sigue los pasos de [Integración con Inbox Monster](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_80147afaf3).

## Uso {#usage}

Para saber cómo enviar pruebas programadas de colocación en el buzón de entrada a través de Inbox Monster, consulta [Pruebas programadas de colocación en el buzón de entrada](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_7e74bc474e).