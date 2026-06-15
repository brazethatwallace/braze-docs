---
nav_title: Mention Me
article_title: Integrar Mention Me con Braze
description: Guía de configuración de la integración de Mention Me
alias: /partners/mention_me/
page_type: partner
search_tag: Partner
---

# Mention Me

> Juntos, [Mention Me](https://www.mention-me.com/) y Braze pueden ser tu puerta de entrada para atraer a clientes premium y fomentar una fidelización inquebrantable a la marca. Al integrar fácilmente datos propios de referidos en Braze, puedes entregar experiencias omnicanal altamente personalizadas dirigidas a los fans de tu marca.

_Esta integración está mantenida por Mention Me._

## Requisitos previos {#prerequisites}

Antes de empezar, necesitarás lo siguiente:

| Requisitos          | Descripción                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Una cuenta de Mention Me   | Se necesita una cuenta de [Mention Me](https://mention-me.com/login) para aprovechar esta asociación.                                                                     |
| Una clave de API REST de Braze  | Una clave de API REST de Braze con permisos `users.track` y `templates.email.create`. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Un punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze de tu instancia.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

* Envía datos de contacto y adhesiones voluntarias de clientes referidos de Mention Me a Braze en tiempo real.
* Utiliza los datos de referidos para crear recordatorios de cupones por correo electrónico.
* Mejora el rendimiento de otros canales de marketing utilizando datos de referidos para segmentar y dirigirte a clientes de alto valor.

## ¿Qué datos se envían desde Mention Me a Braze? {#what-data-is-sent-from-mention-me-to-braze}

Cuando configures esta integración, Mention Me creará automáticamente tus atributos y eventos de cliente, por lo que no necesitas hacerlo de antemano.

Las direcciones de correo electrónico de tus clientes en Braze se utilizarán para vincular eventos y atributos personalizados relevantes. Mention Me enviará eventos y atributos del perfil de contacto de cualquier cliente potencial o existente que desencadene este evento a través de Mention Me, independientemente de su estado de adhesión voluntaria.

Para más detalles, consulta [Atributos y eventos del perfil de contacto](https://help.mention-me.com/hc/en-gb/articles/26677937177501-What-Mention-Me-data-is-sent-to-Braze).

## Integración de Mention Me {#integrating-mention-me}

{% alert tip %}
Para una guía completa paso a paso, consulta [la documentación de configuración de Braze de Mention Me](https://help.mention-me.com/hc/en-gb/articles/26151773368221-How-to-setup-Braze-with-Mention-Me).
{% endalert %}

Para integrar Mention Me con Braze:

1. En Mention Me, ve a la página de [integración de Braze](https://mention-me.com/merchant/~/integrations/braze) y selecciona **Connect**.
2. Selecciona **Create New Authorization**, luego añade la [clave de API que creaste anteriormente](#prerequisites) y selecciona tu instancia de Braze.
3. Elige uno o varios países con los que quieras sincronizar.
4. Cuando hayas terminado, selecciona **Connect**.