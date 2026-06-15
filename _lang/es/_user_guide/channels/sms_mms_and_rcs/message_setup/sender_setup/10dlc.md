---
nav_title: "A2P 10DLC"
article_title: "A2P 10DLC"
page_order: 2.9
description: "Este artículo cubre A2P 10DLC, por qué el registro 10DLC es necesario para los clientes de códigos largos en EE. UU., información útil sobre costos y rendimiento, y cómo empezar con el registro."
page_type: reference
channel:
  - SMS

---

# Códigos largos de 10 dígitos de aplicación a persona {#application-to-person-10-digit-long-codes}

> A2P 10DLC se refiere a un sistema en Estados Unidos que permite a las empresas enviar mensajes de tipo aplicación a persona (A2P) a través de un número de teléfono estándar de código largo de 10 dígitos (10DLC). Estos códigos largos registrados cuentan con mayor rendimiento, mejor capacidad de entrega y cumplimiento mejorado en comparación con el código largo estándar.

{% alert important %}
Todos los clientes que actualmente tienen y/o usan códigos largos de EE. UU. para enviar mensajes a clientes en EE. UU. deben registrar sus códigos largos para 10DLC; quienes no lo hagan experimentarán un filtrado intenso de todos los mensajes. Este proceso de solicitud toma de 4 a 6 semanas.
{% endalert %}

## Por qué es necesario {#why-its-necessary}

El servicio 10DLC fue creado específicamente para facilitar la mensajería A2P usando códigos largos. Históricamente, los códigos largos estaban destinados a la mensajería de persona a persona (P2P), pero cuando se usaban con fines de marketing, las empresas se veían limitadas por un rendimiento reducido y un filtrado más estricto.

10DLC ayuda a aliviar esos problemas al ofrecer:
- **Mayor rendimiento**: Los números 10DLC admiten un volumen de mensajes más alto que los códigos largos regulares.
- **Mejor capacidad de entrega**: Los números 10DLC están designados para tráfico A2P, por lo que los mensajes enviados con estos números tienen más probabilidades de llegar al destinatario y menos probabilidades de ser filtrados o rechazados por el operador que los mensajes enviados a través de códigos largos locales regulares.
- **Cumplimiento mejorado**: Usar un código largo local para mensajes de texto comerciales va en contra de las directrices de la [CTIA](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf). Los números 10DLC fueron designados para mensajería masiva y permiten a las marcas cumplir con las regulaciones de la industria sin depender de códigos abreviados.
- **Económico**: 10DLC es una excelente opción para empresas que quieren empezar a enviar SMS o enviar SMS en volúmenes pequeños. Para marcas que envían volúmenes de mensajería más grandes, de más de 100,000 mensajes al día, recomendamos usar un código abreviado.

Desde 2019, los operadores han comenzado a adoptar 10DLC para mensajería comercial, con Verizon y AT&T actualmente soportando 10DLC, y esperamos que todos los operadores principales sigan pronto. Si bien puede causar inconvenientes a corto plazo, a largo plazo los clientes disfrutarán de mejores tasas de capacidad de entrega mientras protegen a sus consumidores de mensajes no deseados.

## Lo que necesitas saber {#what-you-need-to-know}

### Acceso {#access}

Registrar códigos largos con A2P 10DLC tomará de 4 a 6 semanas.

### Costos {#costs}

Registrarse con A2P 10DLC puede incluir varios tipos de tarifas:

| Tipo de tarifa | Descripción |
| -------- | ---------- |
| Tarifas de registro | Tarifas nominales aplicadas al registrar tu marca y caso de uso en todas las principales redes de EE. UU. |
| Tarifas de verificación secundaria | Las marcas pueden apelar su [puntuación de confianza de marca](#trust-score) y solicitar un proceso de verificación secundaria para mejorar su rendimiento general; hay una tarifa asociada con este proceso. |
| Tarifas de operador | Tarifas cobradas por los operadores por mensajes SMS y MMS salientes enviados a usuarios después del registro 10DLC. A partir del 1 de octubre de 2021, las tarifas de operador serán más altas para el tráfico no registrado (códigos largos estándar) que para el tráfico registrado (10DLC). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Costos" }

Visita el artículo de Twilio sobre 10DLC para consultar las [estimaciones de tarifas](https://support.twilio.com/hc/en-us/articles/1260803965530-What-pricing-and-fees-are-associated-with-the-A2P-10DLC-service-) actualizadas.

### Rendimiento {#throughput}

El rendimiento de mensajes para tu 10DLC depende de varios factores, incluyendo la puntuación de confianza de marca, los límites diarios de mensajes y tus casos de uso de mensajería.

#### Puntuación de confianza de marca {#trust-score}

El Campaign Registry (TCR) es una agencia de terceros que utiliza un algoritmo de reputación para revisar criterios específicos relacionados con tu empresa y asignar una puntuación de confianza que determina el rendimiento de mensajería para cada marca. Esta puntuación de confianza se asignará cuando un cliente se registre para la mensajería 10DLC en EE. UU. Cuanto mayor sea la puntuación de confianza, mejores mensajes por segundo (MPS) experimentarás.

|     | Puntuación de confianza | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| Alta | 75-100 | 75 MPS | 75 MPS | 75 MPS |
| Media | 50-74 | 40 MPS | 40 MPS | 40 MPS |
| Baja | 1-49 | 4 MPS | 4 MPS | 4 MPS |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Puntuación de confianza de marca" }

{% alert tip %}
Las empresas que figuran en el índice Russell 3000 recibirán un alto rendimiento y una puntuación de confianza de marca alta después del registro y revisión de 10DLC.
{% endalert %}

#### Límites diarios de mensajes {#daily-message-limits}

Los límites diarios van desde 2,000 hasta 200,000 mensajes dependiendo de tu puntuación de confianza de marca y se aplican a todos los códigos largos. Si bien las puntuaciones de confianza de marca altas vienen con un rendimiento de 60 mensajes por segundo, cualquier límite diario de mensajes establecido por el operador seguirá aplicándose. Esto significa que los códigos abreviados serían una mejor opción si los mensajes pico diarios de una marca son superiores al límite diario impuesto.

#### Casos de uso de mensajería {#messaging-use-cases}

El rendimiento también se ve afectado por el tipo de caso de uso de mensajería que elijas. La mayoría de los clientes caerán en el caso de uso de marketing estándar o marketing mixto. Otros casos de uso menos comunes estarán sujetos a diferentes valores de rendimiento.

Dependiendo de tu caso de uso, la puntuación de confianza necesaria para alcanzar el rendimiento máximo variará. Las siguientes tablas enumeran los casos de uso estándar y los rangos comunes de puntuación de confianza por caso de uso. Para casos de uso especiales como servicios de emergencia o caridad, consulta la [documentación de Twilio](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US).

| Casos de uso estándar | Descripción |
| ------------------ | ----------- |
| Marketing | Contenido promocional como ventas y ofertas por tiempo limitado. |
| Mixto | Campaña que cubre múltiples casos de uso, como atención al cliente. |
| Educación superior | Campañas para instituciones de educación superior. |
| Encuestas y votaciones | Encuestas y votaciones no políticas, como cuestionarios de clientes. |
| PSA | Anuncios de servicio público para crear conciencia sobre un tema determinado. |
| Atención al cliente | Soporte, administración de cuentas y otras interacciones con el cliente. |
| Notificaciones de entrega | Estado de los mensajes de entrega. |
| Notificaciones de cuenta | Notificaciones sobre el estado de una cuenta. |
| 2FA | Cualquier autenticación de verificación de cuenta, como OTP. |
| Alertas de seguridad | Notificación de un sistema comprometido. |
| Alertas de fraude | Mensajería sobre actividad potencialmente fraudulenta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso de mensajería" }

{% tabs %}
{% tab Caso de uso declarado %}
Un caso de uso declarado significa que has elegido un caso de uso específico que no es de marketing (por ejemplo, 2FA o notificaciones de cuenta).

| Puntuación de confianza | Rendimiento total hacia las principales redes de EE. UU. | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74	 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Casos de uso de mensajería" }

{% endtab %}
{% tab Caso de uso de marketing mixto %}

Los casos de uso de marketing mixto se pueden registrar para clientes que desean enviar mensajes para múltiples casos de uso desde el mismo conjunto de números o para marketing.

| Puntuación de confianza | Rendimiento total hacia las principales redes de EE. UU. | AT&T | T-Mobile  | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Casos de uso de mensajería" }

{% endtab %}
{% endtabs %}

Visita el artículo de Twilio sobre 10DLC para consultar las [estimaciones de rendimiento](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US) actualizadas.

## Próximos pasos {#next-steps}

Los clientes que aún no se han registrado para 10DLC deben trabajar con su administrador del éxito del cliente para registrar sus códigos largos. **Si los clientes no registran sus códigos largos, a partir del 1 de octubre de 2021, cualquier remitente A2P que use códigos largos experimentará un filtrado intenso de todos los mensajes.** Ponte en contacto con tu administrador del éxito del cliente para comenzar con tu registro 10DLC.