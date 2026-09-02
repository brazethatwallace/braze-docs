# Creación de agentes de decisión basados en IA {#building-ai-decisioning-agents}

> Aprende a crear un agente para BrazeAI Decisioning Studio™, para que puedas automatizar la experimentación personalizada y optimizar resultados como conversiones, retención o ingresos, sin pruebas A/B manuales.

{% multi_lang_include decisioning_studio/alert_multi_platform_support.md %}

## Acerca de los agentes {#about-agents}

Un agente de decisión de IA es una configuración personalizada del motor de decisión de BrazeAI<sup>TM</sup> diseñada a medida para cumplir un objetivo de negocio específico.

Por ejemplo, podrías crear un agente de compra repetida para aumentar las conversiones de seguimiento después de una venta inicial. Tú defines la audiencia y el mensaje en Braze, mientras que tu agente de decisión ejecuta experimentos diarios y prueba automáticamente diferentes combinaciones de ofertas de productos, tiempos de envío de mensajes y frecuencia para cada cliente. Con el tiempo, BrazeAI<sup>TM</sup> aprende lo que funciona mejor y orquesta envíos personalizados a través de Braze para maximizar las tasas de recompra.

Para crear un buen agente, deberás:

- Elegir una métrica de éxito para que BrazeAI<sup>TM</sup> la optimice, como ingresos, conversiones o ARPU.
- Definir qué dimensiones probar, como oferta, línea del asunto, creatividad, canal o momento de envío.
- Seleccionar las opciones para cada dimensión, como correo electrónico frente a servicio de mensajes cortos, o frecuencia diaria frente a semanal.

![Diagrama de ejemplo de un agente de Decisioning Studio para correos electrónicos de referidos.]({% image_buster /assets/img/offerfit/example_use_cases_referral_email.png %})

## Agentes de ejemplo {#sample-agents}

Aquí tienes algunos ejemplos de agentes que puedes crear con BrazeAI Decisioning Studio™. Tus agentes de toma de decisiones con IA aprenderán de cada interacción con los clientes y aplicarán esas conclusiones a las acciones del día siguiente.

{% multi_lang_include decisioning_studio/sample_agents.md %}

## Creación de un agente {#building-an-agent}

### Requisitos previos {#prerequisites}

Antes de poder crear un agente, necesitarás [integrar BrazeAI Decisioning Studio™]({{site.baseurl}}/developer_guide/decisioning_studio/integration).

### Paso 1: Contacta con AI Expert Services {#step-1-contact-ai-expert-services}

El equipo de AI Expert Services trabajará de cerca contigo para definir el alcance, diseñar y crear tu agente de toma de decisiones. Si aún no lo has hecho, [contáctanos](https://www.braze.com/get-started/) para empezar.

Completarás los siguientes pasos junto con el equipo para crear un agente personalizado que se adapte a tus necesidades.

### Paso 2: Diseña tu agente {#step-2-design-your-agent}

Junto con el equipo de AI Expert Services, definirás:

- un público objetivo,
- la métrica de negocio a optimizar,
- las acciones para el agente de toma de decisiones de BrazeAI<sup>TM</sup>, y
- cualquier dato de clientes propio que el agente deba aprovechar para impulsar tus resultados de negocio.

Con el diseño listo, el equipo trabajará contigo para identificar y completar cualquier requisito de integración adicional.

### Paso 3: Configura tu plataforma de entrega {#step-3-set-up-your-delivery-platform}

A continuación, el equipo de AI Expert Service te ayudará a configurar tu plataforma de interacción con los clientes. Aunque Decisioning Studio funciona mejor con Braze, se admiten otras plataformas&#8212;contacta con tu equipo de AI Expert Service para obtener recursos adicionales.

{% tabs local %}
{% tab Braze %}
Para configurar Braze:

1. Crea una [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) o un [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=api-triggered%20delivery#step-12-determine-your-canvas-entry-schedule). BrazeAI Decisioning Studio™ utilizará este método de entrega para enviar eventos de activación personalizados 1:1 a los usuarios de tu audiencia definida.
2. Asegúrate de no incluir un [grupo de control]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) de Braze, para que BrazeAI<sup>TM</sup> pueda actuar como grupo de control dedicado en su lugar.
3. Dependiendo de tus dimensiones, puedes configurar etiquetas de Liquid en tu contenido creativo para completar dinámicamente tu mensajería con las recomendaciones de BrazeAI<sup>TM</sup>. BrazeAI<sup>TM</sup> pasará contenido específico de cada cliente a las etiquetas de Liquid en tus plantillas utilizando la API de Braze.
{% endtab %}
{% endtabs %}

### Paso 4: Lanza y supervisa {#step-4-launch-and-monitor}

Después de lanzar tu agente, tu equipo de AI Expert Services continuará supervisándolo y ajustándolo según el diseño acordado. También te ayudarán a realizar cualquier ajuste, ampliación o modificación del agente, si es necesario.