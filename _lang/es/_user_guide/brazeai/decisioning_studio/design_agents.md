---
nav_title: Diseñar agentes de toma de decisiones
article_title: Diseñar agentes de toma de decisiones
page_order: 1
page_type: reference
description: "Este artículo de referencia cubre conceptos clave y mejores prácticas para diseñar y configurar tu agente de toma de decisiones."
---

# Diseñar agentes de toma de decisiones {#design-decisioning-agents}

> Este artículo de referencia cubre conceptos clave y mejores prácticas para diseñar y configurar tu agente de toma de decisiones.

## Acerca de los agentes de toma de decisiones {#about-decisioning-agents}

Diseñar tu agente de toma de decisiones es el primer paso para configurar Decisioning Studio. Para que el agente de toma de decisiones pueda tomar decisiones, necesitas definir qué resultado quieres maximizar y qué acciones puede realizar el agente para lograrlo.

### Conceptos clave {#key-concepts}

Los siguientes términos se utilizan a lo largo de la guía de Decisioning Studio.

| Término | Definición |
| --- | --- |
| **Agente de toma de decisiones** | Un agente de toma de decisiones es una configuración personalizada de BrazeAI Decisioning Studio™ diseñada a medida para cumplir un objetivo de negocio específico. Se define por la métrica de éxito, las dimensiones y las opciones que elijas. |
| **Métrica de éxito** | La métrica de negocio específica que deseas optimizar, como ingresos, conversiones o ingresos promedio por usuario (ARPU). Esta es la métrica que el agente de toma de decisiones intentará maximizar a través de sus acciones. |
| **Dimensiones** | Las dimensiones pueden entenderse como los *tipos de palancas* que el agente de toma de decisiones puede accionar para maximizar la métrica de éxito. Las dimensiones típicas incluyen oferta, línea del asunto, creatividad, canal o momento de envío. |
| **Banco de acciones** | El banco de acciones define las *opciones específicas* a las que el agente de toma de decisiones tiene acceso para cada "palanca" de dimensión. Por ejemplo, para una dimensión de canal, defines los canales específicos a los que el agente de toma de decisiones tiene acceso. Para una dimensión de oferta, defines las ofertas específicas que el agente de toma de decisiones puede probar. |
| **Restricciones** | En general, el agente de toma de decisiones podría tomar cualquier combinación de acciones que pongas en el banco de acciones. Sin embargo, también puedes definir restricciones para limitar las acciones del agente de toma de decisiones y respetar reglas de negocio críticas. Por ejemplo, esto podría ser evitar que se seleccione una oferta específica para clientes en una geografía no elegible, o establecer un presupuesto máximo para que el agente de toma de decisiones gaste. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conceptos clave" }

![Resumen de alto nivel de un agente de toma de decisiones]({% image_buster /assets/img/decisioning_studio/decisioning_studio_high_level_agent.png %})

{% alert important %}
El agente de toma de decisiones solo puede realizar acciones que *tú* configures y agregues al banco de acciones. Esto significa que todas las acciones posibles están definidas por las combinaciones de lo que pongas en el banco de acciones.
{% endalert %}

## Cómo diseñar tu agente de toma de decisiones {#how-to-design-your-decisioning-agent}

Al configurar un agente de toma de decisiones, necesitarás pensar en cuatro elementos principales de diseño:

### El "objetivo": define tu métrica de éxito {#the-goal-define-your-success-metric}

*¿Qué resultado quieres que el agente maximice?*

Tu métrica de éxito es el resultado de negocio para el que el agente optimizará. Esto debe alinearse directamente con tus objetivos de negocio, no métricas intermedias como clics o aperturas, sino resultados de negocio reales como ingresos, conversiones, ARPU o LTV del cliente.

### El "quién": selecciona tu audiencia {#the-who-select-your-audience}

*¿A quién involucrará el agente de toma de decisiones?*

Define la audiencia a la que tu agente atenderá. Esto podría ser todos los clientes, un segmento específico (como miembros de un programa de fidelización), o clientes en una etapa particular de su ciclo de vida (como compradores recientes o suscriptores en riesgo).

### El "qué": configura tu banco de acciones {#the-what-configure-your-action-bank}

*¿De qué opciones puede elegir el agente para impulsar el resultado?*

El banco de acciones define todas las palancas que el agente puede accionar: las dimensiones (como canal, oferta, momento y frecuencia) y las opciones específicas dentro de cada dimensión. El agente experimenta con diferentes combinaciones de estas opciones para encontrar lo que funciona mejor para cada cliente.

### El "cómo": configura tus restricciones {#the-how-configure-your-constraints}

*¿Qué reglas debe seguir el agente?*

Las restricciones son las reglas que el agente debe seguir. Esto podría ser evitar que se seleccione una oferta específica para clientes en una geografía no elegible, o establecer un presupuesto máximo para que el agente de toma de decisiones gaste.

## Mejores prácticas y ejemplos {#best-practices-and-examples}

Para maximizar el impacto de tu agente de toma de decisiones, deberías:

- Elegir una métrica de éxito que se alinee estrechamente con tus metas y objetivos de negocio, como ingresos, conversiones o ARPU.
- Enfocarte en las dimensiones, o "palancas" a probar, como oferta, línea del asunto, creatividad, canal o momento de envío, que tengan más probabilidades de tener un impacto significativo en la métrica de éxito.
- Seleccionar las opciones para cada dimensión, como correo electrónico versus SMS, o frecuencia diaria versus semanal, que tengan más probabilidades de tener un impacto significativo en la métrica de éxito.

Algunos ejemplos de agentes de toma de decisiones que podrías construir son:

{% tabs %}
{% tab Agente de compra repetida %}
Podrías construir un agente de compra repetida para aumentar las conversiones de seguimiento después de una venta inicial:

- Define la audiencia y el mensaje en Braze
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando diferentes combinaciones de ofertas de productos, momento del mensaje y frecuencia para cada cliente
- Con el tiempo, BrazeAI<sup>TM</sup> aprende qué funciona mejor para cada cliente
- Orquesta envíos personalizados a través de Braze para maximizar las tasas de recompra
{% endtab %}
{% tab Agente de venta cruzada o upsell %}
Podrías construir un agente de venta cruzada o upsell para maximizar los ingresos promedio por usuario (ARPU) de suscripciones de internet:

- Define la audiencia y el mensaje en Braze
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando diferentes combinaciones de mensajes, momentos de envío, descuentos y ofertas de planes para cada cliente
- BrazeAI<sup>TM</sup> aprende qué clientes son susceptibles a ofertas de salto de nivel y cuáles requieren descuentos u otros incentivos para actualizar
- Orquesta envíos personalizados a través de Braze para maximizar el ARPU
{% endtab %}
{% tab Agente de renovación y retención %}
Podrías construir un agente de renovación y retención para asegurar renovaciones de contratos, maximizando tanto la duración del contrato como el valor presente neto (VPN):

- Define la audiencia y el mensaje en Braze
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando diferentes ofertas de renovación para cada cliente
- BrazeAI<sup>TM</sup> identifica a los clientes que son menos sensibles al precio y necesitan descuentos menos significativos para renovar
- Orquesta envíos personalizados a través de Braze para maximizar las renovaciones de contratos y el VPN
{% endtab %}
{% tab Agente de recuperación %}
Podrías construir un agente de recuperación para aumentar la reactivación animando a suscriptores anteriores a volver a suscribirse:

- Define la audiencia y el mensaje en Braze
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando miles de variables a la vez, incluyendo creatividad, mensaje, canal y cadencia
- BrazeAI<sup>TM</sup> descubre la mejor combinación para cada cliente individual
- Orquesta envíos personalizados a través de Braze para maximizar las tasas de reactivación
{% endtab %}
{% tab Agente de referidos %}
Podrías construir un agente de referidos para maximizar las nuevas cuentas abiertas a través de referidos de tarjetas de crédito empresariales de clientes existentes:

- Define la audiencia y el mensaje en Braze
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando diferentes correos electrónicos, creatividades, momentos de envío y ofertas de tarjetas de crédito para cada cliente
- BrazeAI<sup>TM</sup> determina la combinación ideal para clientes específicos
- Orquesta envíos personalizados a través de Braze para maximizar las conversiones de referidos
{% endtab %}
{% tab Agente de nutrición y conversión de leads %}
Podrías construir un agente de nutrición y conversión de leads para impulsar ingresos incrementales y pagar la cantidad correcta por cada cliente:

- Define la audiencia y el mensaje en Braze
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando diferentes segmentos de clientes, metodología de puja, niveles de puja y creatividad
- BrazeAI<sup>TM</sup> aprovecha datos propios robustos para optimizar el rendimiento de anuncios pagados a medida que cambian las políticas de privacidad
- Orquesta envíos personalizados a través de Braze para maximizar los ingresos mientras optimiza el costo por cliente
{% endtab %}
{% tab Agente de fidelización e interacción %}
Podrías construir un agente de fidelización e interacción para maximizar las compras de nuevos inscritos en un programa de fidelización de clientes:

- Define la audiencia y el mensaje en Braze
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando diferentes ofertas por correo electrónico, momentos de envío y frecuencias para cada cliente
- BrazeAI<sup>TM</sup> aprende qué funciona mejor para cada nuevo inscrito en el programa de fidelización
- Orquesta envíos personalizados a través de Braze para maximizar las tasas de compra y recompra
{% endtab %}
{% endtabs %}

## Próximos pasos {#next-steps}

¿Listo para construir tu propio agente de toma de decisiones? Consulta [Primeros pasos con Decisioning Studio]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/get_started) para obtener una guía que te acompaña a través de la conexión de orígenes de datos, la configuración de la orquestación, el diseño de tu agente y el lanzamiento a producción.