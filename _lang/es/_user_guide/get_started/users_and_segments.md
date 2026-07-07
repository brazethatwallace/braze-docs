---
nav_title: Usuarios y segmentos
article_title: "Cómo empezar: Usuarios y segmentos"
page_order: 2
page_type: reference
description: "Este artículo ofrece una visión general de los usuarios y los segmentos, destacando su importancia y cómo pueden aprovecharse para captar a tu audiencia."

---

# Cómo empezar: Usuarios y segmentos {#get-started-users-and-segments}

> Comprender a tus usuarios y dirigirte a ellos con eficacia es crucial para enviar campañas de marketing personalizadas y específicas. Este artículo ofrece una visión general de los usuarios y los segmentos, destacando su importancia y cómo puedes aprovecharlos para captar a tu audiencia.

## Usuarios {#users}

En Braze, la información sobre tu audiencia se almacena en perfiles de usuario. Un [perfil de usuario]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) es una colección completa de información y atributos que describen a un consumidor individual. Sirve como repositorio central para almacenar y gestionar datos relacionados con su comportamiento, preferencias y detalles demográficos.

### Partes de un perfil de usuario {#parts-of-a-user-profile}

Al comprender los perfiles de usuario, puedes obtener información sobre tu audiencia e interactuar con ella de forma personalizada y específica. El perfil de un usuario contiene mucha información, pero estas son algunas de las partes clave:

- **Identificador de usuario:** Cada perfil de usuario se identifica de forma única mediante un ID de usuario, denominado `external_id`. Este identificador permite a Braze rastrear y asociar los datos de los usuarios a través de diferentes canales y dispositivos, proporcionando una visión unificada de las interacciones de cada usuario con tu marca. [Los perfiles de usuario anónimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) (usuarios que visitan tu sitio web o aplicación sin iniciar sesión) no tienen un `external_id`, pero se les pueden asignar [alias de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#assigning-user-aliases) como identificador alternativo.
- [Atributos](#attributes)**:** Son datos específicos sobre el usuario, como su nombre, edad, ubicación o cualquier otra información demográfica. Puedes utilizar estos atributos para segmentar tu audiencia y personalizar tus mensajes.
- [Eventos](#events)**:** Son acciones que realiza el usuario, como hacer una compra, hacer clic en un enlace o abrir una aplicación. Braze realiza un seguimiento de estos eventos para ayudarte a comprender el comportamiento y la interacción del usuario. De forma similar a los atributos, también puedes utilizar los eventos para segmentar y personalizar.
- **Compras:** Esta sección registra el historial de compras del usuario. Es crucial para comprender los hábitos de compra y las preferencias del usuario.
- **Dispositivos:** Esta sección enumera los dispositivos que el usuario ha utilizado para interactuar con tu marca. Puede incluir dispositivos móviles, navegadores web y dispositivos conectados (como wearables y Smart TV).
- **Interacción:** Esta sección contiene información sobre las interacciones del usuario con los mensajes que le envías, a qué segmentos pertenece, estado de suscripción y más.
- **Historial de mensajes:** Es un registro de todos los mensajes que se han enviado al usuario desde el canal de mensajería correspondiente (como correo electrónico o push).

{% alert tip %}
Los SDK de la plataforma Braze recopilan automáticamente 27 atributos y eventos diferentes. Utilizando estos eventos y atributos estándar, puedes crear segmentos tan pronto como integres el SDK.
{% endalert %}

### Atributos {#attributes}

Los atributos son características o propiedades específicas asociadas a un usuario. Estos atributos te ayudan a segmentar y dirigirte a los usuarios en función de sus rasgos e intereses únicos. Existen dos tipos de atributos en Braze: atributos estándar y atributos personalizados.

#### Atributos estándar {#standard-attributes}

Los atributos estándar son atributos predefinidos que puedes rastrear con Braze tras integrar el SDK en tu aplicación. Se trata de información común sobre los usuarios que la mayoría de las aplicaciones consideran útil, como datos demográficos y datos de dispositivo. Algunos ejemplos son:

- Nombre
- Apellido
- Correo electrónico
- Género
- Fecha de nacimiento
- País
- Ciudad
- Última aplicación usada
- Idioma
- Zona horaria

#### Atributos personalizados {#custom-attributes}

[Los atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) son atributos que defines en función de tus necesidades empresariales específicas. Te permiten realizar un seguimiento de la información exclusiva de tu aplicación o negocio.

Por ejemplo, una aplicación de streaming de música podría rastrear atributos personalizados como:

- Género favorito
- Número de canciones reproducidas
- Suscriptor Premium (Sí/No)
- Artista favorito

Por otro lado, una aplicación de comercio minorista podría rastrear atributos personalizados como:

- Talla de ropa preferida
- Marca favorita
- Número de compras
- Miembro del programa de fidelización (Sí/No)

Los atributos personalizados te ofrecen la flexibilidad necesaria para recopilar y analizar los datos más relevantes para tu empresa. Sin embargo, requieren una configuración adicional.

Tanto los atributos estándar como los personalizados pueden utilizarse para segmentar tu audiencia y personalizar tus mensajes de marketing. Por ejemplo, podrías enviar una oferta especial a los usuarios de una determinada ciudad (atributo estándar) que hayan realizado más de 10 compras (atributo personalizado).

### Eventos {#events}

Los eventos representan acciones o comportamientos específicos realizados por los usuarios dentro de tu aplicación o sitio web. Ejemplos de eventos pueden ser lanzamientos de aplicaciones, compras, visualizaciones de contenido o cualquier otra acción. Mediante el seguimiento y el análisis de estos eventos, puedes obtener información sobre el comportamiento de los usuarios y los patrones de interacción.

#### Eventos estándar {#standard-events}

[Los eventos estándar]({{site.baseurl}}/user_guide/data/activation/events#standard-events) son eventos predefinidos que Braze rastrea automáticamente después de integrar el SDK en tu aplicación o sitio. Algunos ejemplos de eventos estándar son:

- **Inicio de sesión:** Este evento se activa cuando un usuario abre la aplicación.
- **Fin de sesión:** Este evento se activa cuando un usuario cierra la aplicación.
- **Compra:** Este evento se activa cuando un usuario realiza una compra dentro de la aplicación.
- **Clic en notificación push:** Este evento se activa cuando un usuario hace clic en una notificación push.

#### Eventos personalizados {#custom-events}

[Los eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) son eventos que defines en función de las acciones específicas que deseas rastrear dentro de tu aplicación o sitio. Por ejemplo, una aplicación de streaming de música podría rastrear eventos personalizados como:

- Canción reproducida
- Lista de reproducción creada
- Anuncio omitido

Por otro lado, una aplicación de fitness podría realizar un seguimiento de eventos personalizados como:

- Entrenamiento iniciado
- Entrenamiento completado
- Récord personal establecido

Los eventos personalizados te ofrecen la flexibilidad necesaria para realizar un seguimiento de las acciones más relevantes para tu aplicación y tu negocio. Sin embargo, al igual que los atributos personalizados, requieren una configuración adicional.

### Puntos de datos {#data-points}

Braze utiliza puntos de datos para ayudarte a definir la información más impactante para tu negocio. Los puntos de datos son una parte crucial del funcionamiento de Braze y se utilizan para la facturación, la fijación de precios y, lo que es más importante, la personalización y optimización de tus campañas de marketing.

Los puntos de datos se consumen cuando se actualizan los datos del perfil de un usuario o cuando este realiza acciones específicas. Estas acciones pueden incluir el inicio de una sesión, la finalización de una sesión, el registro de un evento personalizado o la realización de una compra. Es importante tener en cuenta que no todos los datos recopilados por Braze cuentan como puntos de datos. Por ejemplo, los datos y eventos recopilados de forma predeterminada por los servicios de Braze, como los tokens de notificaciones push, la información del dispositivo y todos los eventos de seguimiento de interacción en campañas, como las aperturas de correos electrónicos y los clics en notificaciones push, no se contabilizan como puntos de datos.

Al considerar cuidadosamente qué información rastrear como puntos de datos, estás apuntando a los datos de mayor impacto para la experiencia de tus usuarios. Tu director de cuentas de Braze te ayudará a recomendar las mejores prácticas de datos que se adapten a tus necesidades.

Visita nuestro artículo dedicado para saber más sobre [los puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points).

## Segments {#segments}

[La segmentación]({{site.baseurl}}/user_guide/audience/segments) te permite dirigirte a los usuarios en función de sus características y acciones demográficas, de comportamiento, sociales o técnicas (es decir, atributos y eventos). El uso creativo e inteligente de la segmentación y la automatización de la mensajería te permite mover fácilmente a tus usuarios a través de su recorrido en el ciclo de vida del cliente.

Consejos para trabajar con segmentos:

- Los segmentos en Braze son dinámicos: los usuarios siempre entran y salen de los segmentos, ya que no siempre se ajustan a los criterios. Los usuarios que se ajusten a los criterios de un segmento en el momento del envío serán los destinatarios de esa campaña o Canvas.
    - Si deseas que tu segmento sea estático, puedes utilizar extensiones de segmento. Las extensiones de segmento (con [la regeneración desactivada]({{site.baseurl}}/user_guide/audience/segments/segment_extension#extension-regeneration)) representan a tu audiencia como una única instantánea en el tiempo.
- No estás limitado a utilizar un filtro a la vez. Crea segmentos granulares finamente ajustados superponiendo varios filtros.
- Puedes utilizar las acciones o inacciones de tus usuarios para saber cómo llegar a ellos allí donde quieren interactuar contigo. Estas acciones pueden ser eventos personalizados, interacción con una campaña o Canvas existente, o incluso un mensaje específico dentro de un Canvas.

### Caso de uso {#use-case}

Supongamos que tienes una tienda de ropa en línea y has configurado un flujo de mensajería para enviar una serie de correos electrónicos a los usuarios que han añadido un artículo a su carrito pero no han completado la compra. Este flujo de carritos abandonados podría incluir un correo electrónico de recordatorio inicial, un correo electrónico de seguimiento ofreciendo un descuento y un correo electrónico de recordatorio final.

![Captura de pantalla relacionada con el caso de uso.]({% image_buster /assets/img/getting_started/segment_example.png %}){: style="max-width:70%" }

Podrías crear un segmento de usuarios que han desencadenado el evento personalizado "Artículo añadido al carrito" pero no han desencadenado el evento personalizado "Compra completada". A continuación, dentro de este segmento, podrías identificar a los usuarios que han abierto el correo electrónico de recordatorio inicial (interacción con un mensaje específico) pero que no han realizado una compra.

![Podrías crear un segmento de usuarios que han desencadenado el evento personalizado "Artículo añadido al carrito" pero no han desencadenado el evento personalizado "Compra completada". A continuación, dentro de este segmento, podrías identificar a los usuarios que han abierto el correo electrónico de recordatorio inicial (interacción con un mensaje específico) pero que no han realizado una compra.]({% image_buster /assets/img/getting_started/segment_example_breakdown.png %})

Este segmento podría ser objeto de una campaña más agresiva para intentar convertir a estos usuarios en compradores. Por ejemplo, podrías enviarles una oferta especial o una recomendación personalizada basada en los artículos de su carrito.

Este es solo un ejemplo de cómo puedes utilizar las acciones e inacciones de los usuarios, los eventos personalizados y los datos de interacción para crear segmentos y adaptar tus estrategias de marketing en Braze.