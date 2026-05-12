---
nav_title: Elige tus características
article_title: Elige tus características para Decisioning Studio
page_order: 7
page_type: reference
description: "Este artículo de referencia cubre cómo construir características de cliente efectivas para BrazeAI Decisioning Studio, incluyendo tipos de características, directrices generales, construcción de características de comportamiento y la relación entre características y el espacio de acciones."
---

# Elige buenas características {#choose-good-features}

> El modelo de Decisioning Studio utiliza características de cliente como entradas para hacer recomendaciones individualizadas. Las características de alta calidad que están bien alineadas con tu espacio de decisión son una de las palancas más impactantes para mejorar el rendimiento del modelo. Este artículo cubre los tipos de características que puedes proporcionar, cómo construirlas bien y cómo pensar en alinear las características con las acciones entre las que tu agente elegirá.

Si tienes equipos internos de ciencia de datos o ingeniería de datos, están mejor posicionados para construir y seleccionar características, ya que tienen más contexto sobre qué señales en tus datos son significativas.

{% alert note %}
Para los clientes de Braze, las características de cliente se pasan típicamente a Decisioning Studio a través de atributos personalizados en los perfiles de usuario. Para más detalles sobre atributos personalizados frente a eventos personalizados y sus respectivas estrategias de actualización, consulta [Instantáneas frente a flujos de eventos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams/).
{% endalert %}

## Tipos de características de cliente {#types-of-customer-features}

Hay cuatro categorías comunes de características de cliente:

| Tipo de característica | Qué captura | Ejemplos |
|-------------|-----------------|---------|
| **Perfil de usuario** | Datos objetivos sobre el estado del cliente | `age`, `loyalty_tier`, `days_enrolled`, `city`, `acquisition_channel` |
| **Propensión del usuario** | Puntuaciones derivadas de modelos sobre la probabilidad del cliente de hacer algo | `churn_risk_score`, `purchase_intent_score`, `upsell_affinity` |
| **Comportamiento del usuario** | Resúmenes de la actividad del cliente en una ventana de tiempo | `clicks_past_30d`, `purchases_past_7d`, `app_logins_past_14d` |
| **Ambiental** | Señales contextuales externas al cliente | `is_promotional_period`, `is_holiday`, `regional_economic_index` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipos de características de cliente" }

Juntos, estos tipos de características le dan al modelo la información que necesita para identificar segmentos, distinguir entre clientes y adaptar las recomendaciones en consecuencia.

## Directrices generales {#general-guidelines}

Ten en cuenta lo siguiente al seleccionar y construir características:

- **Cobertura:** Las características deben cubrir a todos los clientes en tu audiencia objetivo. Una característica que falta o es nula para una gran parte de tu audiencia le da al modelo menos con qué trabajar para esos clientes.
- **Granularidad:** Todas las características deben estar agregadas a nivel de cliente. Consulta [Usa el ID externo de Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/braze_external_id/) para orientación sobre lo que significa "nivel de cliente" en la práctica.
- **Frescura:** Las características deben actualizarse en un calendario basado en tiempo, no en uno basado en eventos. Consulta [Instantáneas frente a flujos de eventos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams/) para entender por qué esto importa.
- **Validez:** Los valores de las características deben estar dentro de rangos que tengan sentido dada la definición. Una característica para "compras en los últimos 30 días" nunca debería ser negativa.
- **Dispersión:** Evita características que sean cero o nulas para la gran mayoría de los clientes, a menos que haya una razón de negocio clara. Las características dispersas añaden ruido sin añadir señal.
- **Correlación:** Evita incluir características que estén altamente correlacionadas entre sí. Las características redundantes pueden introducir sesgo y ralentizar el entrenamiento sin mejorar las predicciones.

## Construye características de comportamiento {#construct-behavioral-features}

Las características de comportamiento resumen el historial de acciones de un cliente en una ventana de tiempo definida (por ejemplo, "número de compras en los últimos 28 días"). Estas son de las características más valiosas para un sistema de recomendación porque capturan cómo se comporta realmente un cliente, no solo rasgos estáticos de perfil.

### Elige ventanas de tiempo {#choose-time-windows}

La ventana de tiempo adecuada depende de la frecuencia con la que los clientes realizan la acción que estás midiendo:

- **Ventanas cortas (7–28 días):** Úsalas para actividades de alta frecuencia como inicios de sesión en la aplicación, aperturas de correo electrónico o visitas al sitio web.
- **Ventanas largas (90–365 días):** Úsalas para actividades poco frecuentes como compras de productos, renovaciones de suscripción o contactos con servicio al cliente.

Un diagnóstico útil: si un gran porcentaje de los valores de tu característica son cero, la ventana de tiempo probablemente es demasiado corta. Amplíala hasta que veas varianza significativa entre clientes.

### Elige agregaciones {#choose-aggregations}

- **Para eventos sin un valor** (algo ocurrió o no): usa agregaciones de **conteo**. Por ejemplo, `email_opens_past_30d`.
- **Para eventos con un valor asociado** (ingresos, duración, cantidad): usa tanto agregaciones de **suma** como de **promedio**. Por ejemplo, `purchase_value_sum_past_90d` y `purchase_value_avg_past_90d`. Estas proporcionan información complementaria sobre el volumen total y la magnitud por evento.

## Alinea las características con el espacio de acciones {#align-features-with-the-action-space}

Decisioning Studio no es un modelo de propensión; es un sistema de clasificación. Su objetivo es identificar, para cada cliente, qué acción de un conjunto definido de opciones tiene más probabilidades de producir el mejor resultado. Esto crea un requisito específico: **las características deben, cuando sea posible, darle al modelo información que le ayude a distinguir entre las opciones disponibles para un cliente dado.**

### Por qué esto importa {#why-this-matters}

Por ejemplo, supón que el espacio de acciones de tu agente es recomendar uno de tres elementos del menú: café, té negro o té de burbujas.

Si tus características describen a los clientes a un nivel alto ("pide bebidas frecuentemente" o "alta interacción por correo electrónico"), el modelo puede segmentar a los clientes en grupos amplios. Pero cuando se trata de clasificar café frente a té de burbujas para un cliente específico, las características amplias no ayudan mucho. Dos clientes pueden verse idénticos en características de alto nivel pero tener preferencias completamente opuestas.

Cuando el modelo encuentra señales contradictorias, como recomendar café a dos clientes aparentemente similares pero solo uno convierte, no puede aprender de manera efectiva. El ruido reduce su capacidad para hacer clasificaciones precisas.

### Construye características que coincidan con el espacio de acciones {#build-features-that-match-the-action-space}

Las características que se mapean a la misma granularidad que tu espacio de acciones le dan al modelo señales de clasificación mucho más fuertes. En el ejemplo del café, una característica como `coffee_orders_past_14d` le dice directamente al modelo si un cliente prefiere café. Una característica como `black_tea_orders_past_14d` hace lo mismo para el té negro. El modelo ahora puede tomar una decisión de clasificación bien informada.

Con características alineadas a las acciones, el modelo también puede detectar saturación y fatiga. Si un cliente tiene un valor alto de `coffee_orders_past_14d` pero no convirtió en una recomendación reciente de café, el modelo aprende que recomendar café de nuevo puede no ser la mejor opción y comienza a probar alternativas.

### Cuando la alineación exacta no está disponible {#when-exact-alignment-isnt-available}

La alineación exacta entre característica y acción es lo ideal, pero a menudo está limitada por la disponibilidad de datos. Dos enfoques pueden ayudar cuando no puedes construir características perfectamente alineadas:

**Resumen de datos:** Si no puedes distinguir entre compras de té negro y té de burbujas, usa una característica agregada `tea_orders_past_14d`. Esto pierde algo de precisión pero aún ayuda al modelo a distinguir a los clientes que prefieren té de los que prefieren café.

**Señales indirectas:** Las características que no están directamente en el espacio de acciones aún pueden ser valiosas si tienen una relación lógica con él. Por ejemplo, `dessert_purchased_past_30d` es un proxy razonable para la preferencia por artículos dulces, que probablemente está correlacionada con la preferencia por té de burbujas. El modelo puede aprender de estas señales indirectas incluso sin una coincidencia directa de características.

El principio subyacente es que la información más relevante y granular siempre ayuda, pero el modelo aún puede aprender de características imperfectas. Comienza con lo que tienes y refina con el tiempo a medida que más datos estén disponibles.