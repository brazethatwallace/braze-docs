---
nav_title: Caso de uso de la recopilación
article_title: Caso de uso de la recopilación
page_order: 3
page_type: reference
description: "Este artículo de referencia trata un caso de uso de recopilación de datos de usuario sobre cómo una aplicación de transporte compartido podría decidir qué datos de usuario recopilar."

---

# Caso de uso de la recopilación {#collection-use-case}

> Este artículo trata un caso de uso de recopilación de datos de usuario sobre cómo una aplicación de transporte compartido podría decidir qué datos de usuario recopilar.

Supongamos que una aplicación de taxi o de transporte compartido, llamada StyleRyde, quiere decidir qué datos de usuario recopilar. Las siguientes preguntas y el proceso de lluvia de ideas son un gran modelo a seguir por sus equipos de marketing y desarrollo. Al final de este ejercicio, ambos equipos deberían tener una sólida comprensión de qué eventos y atributos personalizados tiene sentido recopilar para ayudar a cumplir su objetivo.

## Pregunta del caso 1: ¿Cuál es el objetivo? {#case-question-1-what-is-the-goal}

El objetivo de StyleRyde es sencillo: quieren que los usuarios llamen a taxis a través de su aplicación.

## Pregunta del caso 2: ¿Cuáles son los pasos para alcanzar ese objetivo tras la instalación de la aplicación? {#case-question-2-what-are-the-steps-to-reach-that-goal-after-app-installation}

1. StyleRyde necesita que los usuarios inicien el proceso de registro y rellenen sus datos personales.
2. StyleRyde necesita que los usuarios completen y verifiquen el proceso de registro introduciendo un código en la aplicación que reciben a través de SMS.
3. StyleRyde necesita que los usuarios intenten llamar a un taxi.
4. StyleRyde tiene que estar disponible cuando los usuarios llamen a un taxi.

Estas acciones podrían entonces etiquetarse como los siguientes eventos personalizados:

- Inicio del registro
- Registro completado
- Llamadas de taxi con éxito
- Llamadas de taxi fallidas

Una vez implementados los eventos, StyleRyde puede ejecutar Campaigns como las siguientes:

1. Enviar mensajes a los usuarios que iniciaron el registro pero no lo han completado en un plazo determinado.
2. Enviar mensajes de felicitación a los usuarios que hayan completado el registro.
3. Enviar disculpas y crédito promocional a los usuarios que hayan tenido llamadas de taxi fallidas, que no hayan sido seguidas por una llamada de taxi exitosa dentro de un cierto período de tiempo.
4. Enviar promociones a los usuarios con más llamadas de taxi realizadas con éxito para agradecerles su fidelización.

## Pregunta del caso 3: ¿Qué otra información sobre el usuario podríamos recopilar y utilizar para orientar nuestra mensajería? {#case-question-3-what-other-user-information-could-we-collect-and-use-to-inform-our-messaging}

- ¿Los usuarios tienen algún crédito promocional?
- ¿Cuál es la valoración media que los usuarios dan a sus conductores?
- ¿Códigos promocionales únicos para usuarios?

Estas características podrían etiquetarse como los siguientes atributos personalizados:

- Saldo de crédito promocional (tipo decimal)
- Valoración media de los conductores (tipo entero)
- Código promocional único (tipo cadena)

Estos atributos te permiten enviar campañas a usuarios como:

1. Recordar a los usuarios que no han utilizado la aplicación en siete días y tienen crédito promocional en su cuenta que vuelvan a la aplicación y utilicen el crédito.
2. Utilizar nuestras plantillas de mensajes y [funciones de personalización]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/overview/#personalized-messaging) para arrastrar el atributo de código promocional único a los mensajes dirigidos a los usuarios.

{% alert important %}
Braze prohibirá o bloqueará a los usuarios ("usuarios ficticios") con más de 5.000.000 de sesiones y dejará de ingerir sus eventos de SDK porque suelen ser el resultado de una mala integración. Si descubres que esto le ha ocurrido a un usuario legítimo, ponte en contacto con tu director de cuentas de Braze.
{% endalert %}