---
nav_title: Flybuy
article_title: Flybuy
alias: /partners/flybuy/
description: "Este artículo de referencia describe la asociación entre Braze y Flybuy, una plataforma de servicios de ubicación, para añadir inteligencia de ubicación a tus operaciones y capacidades de marketing."
page_type: partner
search_tag: Partner

---

# Flybuy

> [Flybuy](https://www.flybuy.com/) de Radius Networks es la plataforma de ubicación omnicanal líder que aprovecha la tecnología impulsada por IA para optimizar la velocidad del servicio en recogida, entrega, autoservicio y servicio en mesa. A través de su línea de productos de marketing integrada, Flybuy también permite a las marcas entregar mensajes hiperdirigidos y basados en el momento, ayudando a impulsar la interacción, aumentar el importe del ticket y apoyar iniciativas de fidelización más amplias.

_Esta integración es mantenida por Flybuy._

## Acerca de la integración {#about-the-integration}

Flybuy entrega eventos enriquecidos de inteligencia de usuario a Braze, lo que permite a las marcas enviar mensajes hiperrelevantes y conscientes de la ubicación con el más alto nivel de personalización. Cuando un usuario genera un evento en Flybuy, se entregan a Braze eventos personalizados con atributos de usuario enriquecidos. Estos eventos y atributos se pueden utilizar para impulsar operaciones omnicanal y desencadenar mensajes basados en proximidad.

## Requisitos previos {#prerequisites}

Lo siguiente es necesario antes de habilitar la integración:

| Requisito | Descripción |
|---|---|
| Cuenta de Flybuy | Una cuenta de Flybuy con al menos un proyecto. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos de `users.track`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Para habilitar la integración, completa los siguientes pasos:

1. En el portal de comerciantes de Flybuy, navega a **Project Info** y haz clic en **Events Engine**.
2. Haz clic en **Add a Destination** y luego selecciona **Braze**.
3. Añade tu clave de API de Braze y punto de conexión, y selecciona los eventos que deseas habilitar.
4. Haz clic en **Finish Setup**.

{% alert important %}
Flybuy mapea `loyalty_id` al `external_id` de Braze para usuarios que han iniciado sesión.
{% endalert %}

## Casos de uso {#use-cases}

- [Recogida](https://www.flybuy.com/flybuypickup)
- [Entrega](https://www.flybuy.com/flybuydelivery)
- [Autoservicio](https://www.flybuy.com/flybuydrivethru)
- [Servicio en mesa](https://www.flybuy.com/flybuytableservice)
- [Check-in móvil y pedidos en hoteles](https://www.flybuy.com/industries/hospitality)
- [Línea de productos de marketing](https://www.flybuy.com/flybuy-marketing-suite)

## Ejemplos de desencadenadores basados en eventos y atributos {#event-and-attribute-based-trigger-examples}

Los eventos personalizados y los atributos personalizados se pueden utilizar para impulsar una variedad de experiencias personalizadas.

### Crear un segmento de audiencia de clientes que tuvieron una mala experiencia de recogida {#build-an-audience-segment-of-customers-who-had-a-bad-pickup-experience}

Por ejemplo, dirígete a cualquier cliente que calificó su experiencia de recogida con menos de 5 estrellas.

![Segmento para mala experiencia de recogida]({% image_buster /assets/img/flybuy/flybuy1.png %})

### Desencadenar una alerta cuando un cliente entra en un área de recogida virtual {#trigger-an-alert-when-a-customer-enters-a-virtual-pickup-area}

Envía un SMS personalizado dirigido a clientes sin una cuenta de fidelización para que descarguen la aplicación y creen una cuenta de fidelización.

![Desencadenar una alerta cuando un cliente entra en un área de recogida virtual]({% image_buster /assets/img/flybuy/flybuy2.png %})

![Mensaje de alerta cuando un cliente entra en un área de recogida virtual]({% image_buster /assets/img/flybuy/flybuy2a.png %})

### Crear un segmento de audiencia de clientes que tuvieron un tiempo de espera prolongado {#build-an-audience-segment-of-customers-who-had-a-long-wait-time}

Por ejemplo, dirígete a cualquier cliente que tuvo un tiempo de espera de más de dos minutos al salir de las instalaciones virtuales de una tienda.

![Crear un segmento de audiencia de clientes que tuvieron un tiempo de espera prolongado]({% image_buster /assets/img/flybuy/flybuy3.png %})

### Desencadenar una alerta de corrección de rumbo cuando un cliente se dirige a la ubicación incorrecta {#trigger-a-course-correction-alert-when-a-customer-is-headed-to-the-wrong-location}

Envía una notificación push a los clientes cuando se dirigen o han llegado a una ubicación diferente de donde realizaron su pedido.

### Entregar ofertas especiales basadas en hitos de viaje {#deliver-special-offers-based-on-trip-milestones}

Por ejemplo, envía una oferta especial cuando un cliente VIP llega a sus ubicaciones favoritas.

### Crear un segmento de audiencia de clientes a los que les faltaban artículos en su pedido {#build-an-audience-segment-of-customers-who-were-missing-items-in-their-order}

Por ejemplo, dirígete a cualquier cliente que comentó que faltaban artículos en su pedido digital.

Para más detalles sobre APIs y SDKs, consulta la [documentación para desarrolladores de Flybuy](https://www.radiusnetworks.com/developers/flybuy/#/).