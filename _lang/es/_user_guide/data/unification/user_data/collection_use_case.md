---
nav_title: Caso de uso de la recopilación
article_title: Caso de uso de la recopilación
page_order: 3
page_type: reference
description: "Este artículo de referencia trata un caso de uso de recopilación de datos de usuario sobre cómo una aplicación de transporte compartido podría decidir qué datos de usuario recopilar."

---

# Caso de uso de la recopilación {#collection-use-case}

> Este artículo trata un caso de uso de recopilación de datos de usuario sobre cómo una aplicación de transporte compartido podría decidir qué datos de usuario recopilar.

Supongamos que una aplicación de Taxi for Email o de transporte compartido, llamada StyleRyde, quiere decidir qué datos de usuario recopilar. Las siguientes preguntas y el proceso de lluvia de ideas son un gran modelo a seguir por sus equipos de marketing y desarrollo. Al final de este ejercicio, ambos equipos deberían tener una sólida comprensión de qué eventos y atributos personalizados tiene sentido recopilar para ayudar a cumplir su objetivo.

## Pregunta del caso 1: ¿Cuál es el objetivo? {#case-question-1-what-is-the-goal}

El objetivo de StyleRyde es sencillo: quieren que los usuarios soliciten viajes en Taxi for Email a través de su aplicación.

## Pregunta del caso 2: ¿Cuáles son los pasos para alcanzar ese objetivo después de la instalación de la aplicación? {#case-question-2-what-are-the-steps-to-reach-that-goal-after-app-installation}

1. StyleRyde necesita que los usuarios comiencen el proceso de registro y completen su información personal.
2. StyleRyde necesita que los usuarios completen y verifiquen el proceso de registro ingresando un código en la aplicación que reciben a través de SMS.
3. StyleRyde necesita que los usuarios intenten solicitar un Taxi for Email.
4. StyleRyde necesita estar disponible cuando los usuarios solicitan un Taxi for Email.

Estas acciones podrían entonces etiquetarse como los siguientes eventos personalizados:

- Began Registration
- Completed Registration
- Successful Taxi for Email Hails
- Unsuccessful Taxi for Email Hails

Después de implementar los eventos, StyleRyde puede ejecutar Campaigns que incluyan lo siguiente:

1. Enviar un mensaje a los usuarios que iniciaron Began Registration, pero no han completado Completed Registration dentro de un período de tiempo determinado.
2. Enviar mensajes de felicitación a los usuarios que completaron Completed Registration.
3. Enviar disculpas y crédito promocional a los usuarios que tuvieron Unsuccessful Taxi for Email Hails, que no fueron seguidos por un Successful Taxi for Email Hail dentro de un período de tiempo determinado.
4. Enviar promociones a los usuarios más activos con muchos Successful Taxi for Email Hails para agradecerles su fidelización.

## Pregunta del caso 3: ¿Qué otra información de usuario podríamos recopilar y utilizar para orientar nuestra mensajería? {#case-question-3-what-other-user-information-could-we-collect-and-use-to-inform-our-messaging}

- ¿Los usuarios tienen algún crédito promocional?
- ¿Cuál es la calificación promedio que los usuarios dan a sus conductores?
- ¿Los usuarios tienen códigos promocionales únicos?

Estas características podrían etiquetarse como los siguientes atributos personalizados:

- Saldo de crédito promocional (tipo decimal)
- Calificación promedio del conductor (tipo entero)
- Código promocional único (tipo cadena)

Estos atributos te permiten enviar Campaigns a los usuarios, como por ejemplo:

1. Recordar a los usuarios que no han utilizado la aplicación en siete días y que tienen crédito promocional en su cuenta para que vuelvan a la aplicación y lo utilicen.
2. Usar nuestras plantillas de mensajes y [características de personalización]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) para insertar el atributo de código promocional único en la mensajería dirigida a los usuarios.

{% alert important %}
Braze bloquea los perfiles de usuario ("usuarios ficticios") con más de 5 000 000 de sesiones, más de 20 000 nombres de eventos personalizados distintos o más de 20 000 nombres de productos distintos en compras, ya que suelen ser el resultado de una integración incorrecta. Una vez que un perfil es bloqueado, Braze deja de ingerir todos los datos entrantes para ese perfil, tanto de los SDK como de la REST API. Si descubres que esto le ha ocurrido a un usuario legítimo, contacta a tu director de cuentas de Braze.
{% endalert %}