---
nav_title: Conceptos básicos de las campañas
article_title: Conceptos básicos de las campañas
page_order: 0
page_type: reference
description: "Este artículo de referencia cubre los conceptos básicos de las campañas, abordando varias preguntas que deberías hacerte al configurar tus primeras campañas."
tool: Campaigns

---

# Conceptos básicos de las campañas {#campaigns-basics}

> Este artículo de referencia cubre los conceptos básicos de las campañas, abordando varias preguntas que deberías hacerte al configurar tus primeras campañas.

## Comprender la estructura de las campañas {#understanding-campaign-structure}

Antes de entrar en los detalles más específicos de la configuración de campañas, identifiquemos los aspectos clave para entender cómo funcionan las campañas en los diferentes canales de mensajería.

Las campañas son un paso de mensaje único para conectar con tus usuarios a través de canales, o más comúnmente conocidos como canales de mensajería. Estos canales de mensajería incluyen Content Cards, correo electrónico, mensajes dentro de la aplicación, push, SMS y MMS, y webhooks. Al comprender dónde se encuentran tus clientes, puedes aprovechar los canales de mensajería adecuados para comunicarte.

## Construir el recorrido del cliente {#building-the-customer-journey}

Dado que las campañas pueden construirse de forma única dependiendo del canal de mensajería, puedes usar estas cinco preguntas de visualización para ayudar a identificar y conceptualizar tus estrategias y objetivos de interacción con los clientes.

### El "qué": nombra tu campaña {#the-what-name-your-campaign}

*¿Qué estás intentando ayudar al usuario a hacer o entender?*

Nunca subestimes el poder del nombre. Braze está diseñado para la colaboración, así que este es un excelente momento para establecer cómo comunicarás los objetivos con tu equipo. Para más información sobre los recorridos del cliente, consulta nuestro curso de Braze Learning [Mapping User Lifecycles](https://learning.braze.com/mapping-customer-lifecycles).

### El "cuándo": crea las condiciones de inicio {#the-when-create-starting-conditions}

*¿Cuándo encontrará un cliente esta campaña?*

Los usuarios pueden entrar en tu campaña de tres formas: en una fecha y hora establecidas (planificada), cuando realizan una acción específica (basada en acciones), o cuando hacen algo que desencadena una llamada a la API (desencadenada por API).

La entrega planificada implica ajustar tus campañas para que se envíen en un momento específico y, opcionalmente, con una cadencia determinada. Las campañas basadas en acciones responden a comportamientos específicos del cliente a medida que ocurren en tiempo real. Esto puede incluir realizar una compra o interactuar con otra campaña. Las campañas desencadenadas por API pueden configurarse para determinar acciones clave del cliente en tu plataforma que, cuando se logran, desencadenarán una llamada a la API de Braze y enviarán tus campañas.

### El "quién": selecciona una audiencia de entrada {#the-who-select-an-entry-audience}

*¿A quién intentas llegar?*

Puedes usar [Segments]({{site.baseurl}}/user_guide/audience/segments) predefinidos para dirigirte a los usuarios según sus características y acciones demográficas, de comportamiento o técnicas. Añade más filtros al crear tu campaña para refinar aún más tu segmento. Solo los usuarios que cumplan con estos criterios de audiencia objetivo pueden entrar en el recorrido. Consulta esta tabla para un resumen rápido de los tipos de filtros disponibles.

| Filtro | Descripción |
|---|---|
| Datos personalizados | Segmenta usuarios según eventos y atributos que tú defines. Puede usar características específicas de tu producto. |
| Actividad del usuario | Segmenta clientes según sus acciones y compras. |
| Reorientación | Segmenta clientes a los que se les han enviado, han recibido o han interactuado con campañas anteriores. |
| Actividad de marketing | Segmenta clientes según comportamientos universales como la última interacción o las campañas recibidas. |
| Atributos del usuario | Segmenta clientes por sus atributos y características constantes. |
| Atribución de instalación | Segmenta clientes por su primera fuente, grupo de anuncios, campaña o anuncio. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="El "quién": selecciona una audiencia de entrada" }

### El "por qué": identifica los eventos de conversión {#the-why-identify-conversion-events}

*¿Por qué estás creando esta campaña?*

Siempre es importante tener un objetivo definido en mente, y las campañas te ayudan a entender tu rendimiento frente a KPI como la interacción en sesiones, las compras y los eventos personalizados. Seleccionar al menos un [evento de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) te dará la capacidad de comprender el rendimiento de tu campaña.

### El "dónde": encuentra a mi audiencia {#the-where-find-my-audience}

*¿Dónde puedo llegar mejor a mi audiencia?*

Aquí es donde determinamos qué canales de mensajería tienen más sentido para el recorrido de tu usuario. Idealmente, querrás llegar a tus usuarios donde estén más activos.

### El "cómo": construye la experiencia {#the-how-build-the-experience}

*¿Cómo construyo mi campaña después de identificar las cinco preguntas?*

Considera configurar variantes y pruebas A/B a medida que te vuelvas más hábil con la creación de campañas. Ten en cuenta que las campañas admiten hasta ocho variantes con un grupo de control. Usa los análisis de tu campaña para tomar decisiones informadas mientras construyes tu campaña, ajustando cualquier cosa, desde tu audiencia segmentada hasta el contenido real de tu mensaje.