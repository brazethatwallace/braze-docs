---
nav_title: Usuarios y segmentos
article_title: "Cómo empezar: Usuarios y segmentos"
page_order: 2
page_type: reference
description: "Este artículo ofrece un resumen de los usuarios y los segmentos, destacando su importancia y cómo pueden aprovecharse para captar a tu audiencia."
---

# Cómo empezar: Usuarios y segmentos {#get-started-users-and-segments}

> Comprender a tus usuarios y dirigirte a ellos con eficacia es crucial para enviar campañas de marketing personalizadas y específicas. Este artículo ofrece un resumen de los usuarios y los segmentos, destacando su importancia y cómo puedes aprovecharlos para captar a tu audiencia.

## Usuarios {#users}

En Braze, la información sobre tu audiencia se almacena en perfiles de usuario. Un [perfil de usuario]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) es una colección integral de información y atributos que describen a un consumidor individual. Sirve como un repositorio central para almacenar y gestionar datos relacionados con su comportamiento, preferencias y detalles demográficos.

### Partes de un perfil de usuario {#parts-of-a-user-profile}

Al comprender los perfiles de usuario, puedes obtener información sobre tu audiencia e interactuar con ella de forma personalizada y segmentada. El perfil de un usuario contiene mucha información, pero estas son algunas de las partes clave:

- **Identificador de usuario:** Cada perfil de usuario se identifica de forma única mediante un ID de usuario, llamado `external_id`. Este identificador permite a Braze rastrear y asociar datos de usuario a través de diferentes canales y dispositivos, proporcionando una vista unificada de las interacciones de cada usuario con tu marca. Los [perfiles de usuario anónimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) (usuarios que visitan tu sitio web o aplicación sin iniciar sesión) no tienen un `external_id`, pero se les pueden asignar [alias de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#assigning-user-aliases) como identificador alternativo.
- [Atributos](#attributes)**:** Son datos específicos sobre el usuario, como su nombre, edad, ubicación o cualquier otra información demográfica. Puedes usar estos atributos para segmentar tu audiencia y personalizar tu mensajería.
- [Eventos](#events)**:** Son acciones que el usuario realiza, como hacer una compra, hacer clic en un enlace o abrir una aplicación. Braze hace seguimiento de estos eventos para ayudarte a entender el comportamiento y la participación del usuario. Al igual que los atributos, también puedes usar eventos para segmentar y personalizar.
- **Compras:** Esta sección registra el historial de compras del usuario. Es fundamental para entender los hábitos de compra y preferencias del usuario.
- **Dispositivos:** Esta sección enumera los dispositivos que el usuario ha utilizado para interactuar con tu marca. Puede incluir dispositivos móviles, navegadores web y dispositivos conectados (como wearables y Smart TV).
- **Participación:** Esta sección contiene información sobre las interacciones del usuario con los mensajes que le envías, a qué Segments pertenece, estado de suscripción y más.
- **Historial de mensajes:** Es un registro de todos los mensajes que se han enviado al usuario desde el respectivo canal de mensajería (como correo electrónico o push).

{% alert tip %}
Los SDK or kit de desarrollo de software de la plataforma Braze recopilan automáticamente 27 atributos y eventos diferentes. Usando estos eventos y atributos estándar, puedes crear Segments tan pronto como integres el SDK or kit de desarrollo de software.
{% endalert %}

### Atributos {#attributes}

Los atributos son características o propiedades específicas asociadas a un usuario. Estos atributos te ayudan a segmentar y dirigirte a usuarios según sus rasgos e intereses únicos. Hay dos tipos de atributos en Braze: atributos estándar y atributos personalizados.

#### Atributos estándar {#standard-attributes}

Los atributos estándar son atributos predefinidos que puedes rastrear con Braze tras integrar el SDK or kit de desarrollo de software en tu aplicación. Son datos comunes de usuario que la mayoría de las aplicaciones encontrarían útiles, como información demográfica y datos de dispositivo. Algunos ejemplos incluyen:

- Nombre
- Apellido
- Correo electrónico
- Género
- Fecha de nacimiento
- País
- Ciudad
- Última aplicación utilizada
- Idioma
- Zona horaria

#### Atributos personalizados {#custom-attributes}

Los [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) son atributos que defines según las necesidades específicas de tu negocio. Te permiten rastrear información que es única para tu aplicación o negocio.

Por ejemplo, una aplicación de streaming de música podría rastrear atributos personalizados como:

- Género musical favorito
- Número de canciones reproducidas
- Suscriptor premium (Sí/No)
- Artista favorito

Una aplicación de comercio minorista, por otro lado, podría rastrear atributos personalizados como:

- Talla de ropa preferida
- Marca favorita
- Número de compras
- Miembro del programa de fidelización (Sí/No)

Los atributos personalizados te dan la flexibilidad de recopilar y analizar los datos más relevantes para tu negocio. Sin embargo, requieren configuración adicional.

Tanto los atributos estándar como los personalizados se pueden usar para segmentar tu audiencia y personalizar tus mensajes de marketing. Por ejemplo, podrías enviar una oferta especial a usuarios en una determinada ciudad (atributo estándar) que hayan realizado más de 10 compras (atributo personalizado).

### Eventos {#events}

Los eventos representan acciones o comportamientos específicos realizados por los usuarios dentro de tu aplicación o sitio web. Algunos ejemplos de eventos pueden incluir inicios de aplicación, compras, visualizaciones de contenido o cualquier otra acción. Al rastrear y analizar estos eventos, puedes obtener información sobre el comportamiento de los usuarios y los patrones de participación.

#### Eventos estándar {#standard-events}

Los [eventos estándar]({{site.baseurl}}/user_guide/data/activation/events) son eventos predefinidos que Braze rastrea automáticamente tras integrar el SDK or kit de desarrollo de software en tu aplicación o sitio. Algunos ejemplos de eventos estándar incluyen:

- **Inicio de sesión:** Este evento se desencadena cuando un usuario abre la aplicación.
- **Fin de sesión:** Este evento se desencadena cuando un usuario cierra la aplicación.
- **Compra:** Este evento se desencadena cuando un usuario realiza una compra dentro de la aplicación.
- **Clic en notificación push:** Este evento se desencadena cuando un usuario hace clic en una notificación push.

#### Eventos personalizados {#custom-events}

Los [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) son eventos que defines según las acciones específicas que deseas rastrear dentro de tu aplicación o sitio. Por ejemplo, una aplicación de streaming de música podría rastrear eventos personalizados como:

- Canción reproducida
- Lista de reproducción creada
- Anuncio omitido

Una aplicación de fitness, por otro lado, podría rastrear eventos personalizados como:

- Entrenamiento iniciado
- Entrenamiento completado
- Récord personal establecido

Los eventos personalizados te dan la flexibilidad de rastrear las acciones más relevantes para tu aplicación y negocio. Sin embargo, al igual que los atributos personalizados, requieren configuración adicional.

### Puntos de datos {#data-points}

Braze utiliza puntos de datos para ayudarte a definir la información más impactante para tu negocio. Los puntos de datos son una parte fundamental del funcionamiento de Braze y se utilizan para facturación, precios y, lo más importante, personalizar y optimizar tus Campaigns de marketing.

Los puntos de datos se consumen cuando se actualizan los datos del perfil de un usuario o cuando este realiza acciones específicas. Estas acciones pueden incluir iniciar una sesión, finalizar una sesión, registrar un evento personalizado o realizar una compra. Es importante tener en cuenta que no todos los datos recopilados por Braze cuentan como puntos de datos. Por ejemplo, los datos y eventos recopilados de forma predeterminada por los servicios de Braze, como los tokens de notificaciones push, la información del dispositivo y todos los eventos de seguimiento de participación en Campaigns, como las aperturas de correo electrónico y los clics en notificaciones push, no se cuentan como puntos de datos.

Al considerar cuidadosamente qué información rastrear como puntos de datos, estás apuntando a los datos de mayor impacto para la experiencia de tus usuarios. Tu director de cuentas de Braze te ayudará a recomendar las mejores prácticas de datos que se ajusten a tus necesidades.

Visita nuestro artículo dedicado para obtener más información sobre los [puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points).

## Segments {#segments}

La [segmentación]({{site.baseurl}}/user_guide/audience/segments) te permite dirigirte a los usuarios en función de sus características y acciones demográficas, de comportamiento, sociales o técnicas (es decir, atributos y eventos). El uso creativo e inteligente de la segmentación y la automatización de la mensajería te permite mover fácilmente a tus usuarios a lo largo de su ciclo de vida del cliente.

Consejos para trabajar con Segments:

- Los Segments en Braze son dinámicos: los usuarios siempre están entrando y saliendo de los Segments, ya que no siempre cumplirán los criterios. Los usuarios que cumplan los criterios de un Segment en el momento del envío serán los destinatarios de esa Campaign o Canvas.
    - Si quieres que tu Segment sea estático, puedes usar las extensiones de segmento. Las extensiones de segmento (con la [regeneración desactivada]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-4-designate-refresh-settings-optional)) representan tu audiencia como una única instantánea en el tiempo.
- No estás limitado a usar un solo filtro a la vez. Crea Segments detallados y granulares combinando múltiples filtros unos sobre otros.
- Puedes usar las acciones o inacciones de tus usuarios para entender cómo llegar a ellos donde quieren interactuar contigo. Estas acciones pueden ser eventos personalizados, la participación con una Campaign o Canvas existente, o incluso un mensaje específico dentro de un Canvas.

### Caso de uso {#use-case}

Supongamos que tienes una tienda de ropa en línea y has configurado un flujo de mensajería para enviar una serie de correos electrónicos a los usuarios que han añadido un artículo a su carrito pero no han completado la compra. Este flujo de carrito abandonado podría incluir un correo electrónico de recordatorio inicial, un correo electrónico de seguimiento ofreciendo un descuento y un correo electrónico de recordatorio final.

![Captura de pantalla relacionada con el caso de uso.]({% image_buster /assets/img/getting_started/segment_example.png %}){: style="max-width:70%" }

Podrías crear un Segment de usuarios que hayan desencadenado el evento personalizado "Added Item to Cart" pero que no hayan desencadenado el evento personalizado "Completed Purchase". Luego, dentro de este Segment, podrías identificar aún más a los usuarios que hayan abierto el correo electrónico de recordatorio inicial (participación con un mensaje específico) pero que no hayan realizado una compra.

![Podrías crear un Segment de usuarios que hayan desencadenado el evento personalizado "Added Item to Cart" pero que no hayan desencadenado el evento personalizado "Completed Purchase". Luego, dentro de este Segment, podrías identificar aún más a los usuarios que hayan abierto el correo electrónico de recordatorio inicial (participación con un mensaje específico) pero que no hayan realizado una compra.]({% image_buster /assets/img/getting_started/segment_example_breakdown.png %})

Este Segment podría ser el objetivo de una Campaign más agresiva para intentar convertir a estos usuarios en compradores. Por ejemplo, podrías enviarles una oferta especial o una recomendación personalizada basada en los artículos de su carrito.

Este es solo un ejemplo de cómo puedes usar las acciones e inacciones de los usuarios, los eventos personalizados y los datos de participación para crear Segments y adaptar tus estrategias de marketing en Braze.