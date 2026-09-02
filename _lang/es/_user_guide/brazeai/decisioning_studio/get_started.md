---
nav_title: Comenzar
article_title: Cómo empezar con Decisioning Studio
layout: dev_guide
guide_top_header: "Cómo empezar con Decisioning Studio"
guide_top_text: ""
page_order: 0
search_rank: 2
page_type: landing
description: "Esta sección ofrece una introducción a Decisioning Studio y cómo puedes usarlo para diseñar y desplegar agentes de toma de decisiones que optimicen cualquier métrica de negocio."

guide_featured_title: "Artículos de la sección"
guide_featured_list:
  - name: Diseña tu agente
    link: /docs/user_guide/brazeai/decisioning_studio/design_agents
    image: /assets/img/braze_icons/settings-01.svg
  - name: Prepara tus datos
    link: /docs/user_guide/brazeai/decisioning_studio/prepare_data
    image: /assets/img/braze_icons/database-01.svg
  - name: Define tu audiencia
    link: /docs/user_guide/brazeai/decisioning_studio/audience
    image: /assets/img/braze_icons/users-01.svg
  - name: Configura la orquestación
    link: /docs/user_guide/brazeai/decisioning_studio/orchestration_setup
    image: /assets/img/braze_icons/dataflow-04.svg

guide_menu_title: "Recursos adicionales"
guide_menu_list:
  - name: Acerca de Decisioning Studio
    link: /docs/user_guide/brazeai/decisioning_studio
    image: /assets/img/braze_icons/info-circle.svg
  - name: Preguntas frecuentes sobre Decisioning Studio
    link: /docs/user_guide/brazeai/decisioning_studio/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

BrazeAI Decisioning Studio™ te permite diseñar y desplegar agentes de toma de decisiones que optimizan cualquier métrica de negocio.

Esta referencia ofrece un resumen de los pasos necesarios para configurar Decisioning Studio, incluyendo el diseño de tu agente, la configuración y conexión de orígenes de datos, la configuración de la orquestación y la evaluación del rendimiento.

## Decisiones clave de diseño {#key-design-decisions}

Trabaja con el equipo de AI Decisioning Services para tomar las siguientes decisiones:

| Decisión | Descripción | Ejemplos |
|----------|-------------|----------|
| **Métrica de éxito** | El resultado de negocio que el agente maximiza al personalizar la interacción con los clientes. | Ingresos, LTV or valor de duración del ciclo de vida, ARPU, conversiones, retención |
| **Audiencia** | Los clientes para quienes el agente de Decisioning Studio toma decisiones de interacción. | Todos los clientes, miembros de fidelización, suscriptores en riesgo |
| **Grupos de experimento** | ¿Cómo deben estructurarse los ensayos controlados aleatorizados de Decisioning Studio? | Decisioning Studio, control aleatorio, BAU, exclusión |
| **Dimensiones** | Las decisiones de interacción que el agente personaliza para cada cliente. | Hora del día, línea del asunto, frecuencia, ofertas, canal |
| **Opciones** | Las variantes específicas que el agente puede seleccionar dentro de cada dimensión. | Plantillas específicas, ofertas, ventanas de tiempo |
| **Restricciones** | Las reglas de negocio y los límites que restringen las decisiones del agente. | Restricciones geográficas, límites de presupuesto, reglas de elegibilidad |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Decisiones clave de diseño" }

Cada una de estas decisiones tiene implicaciones en cuánto incremento adicional puede generar el agente y con qué rapidez. Nuestro equipo de AI Decisioning Services trabaja contigo para diseñar un agente que genere el máximo valor respetando todas tus reglas de negocio.

![Diagrama que muestra cómo las métricas de éxito, la audiencia, los grupos de experimento, las dimensiones, las opciones y las restricciones alimentan el diseño de un agente de Decisioning Studio]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Capacidades de Decisioning Studio {#decisioning-studio-capabilities}

| Capacidad | Detalles |
|-----------|----------|
| **Cualquier métrica de éxito** | Optimiza para ingresos, conversiones, ARPU, LTV or valor de duración del ciclo de vida o cualquier indicador clave de rendimiento de negocio |
| **Dimensiones ilimitadas** | Personaliza a través de oferta, canal, momento, frecuencia, creatividad y más |
| **Cualquier CEP** | Integraciones nativas con Braze, Salesforce Marketing Cloud o integraciones personalizadas para cualquier plataforma |
| **AI Decisioning Services** | Soporte dedicado del equipo de ciencia de datos de Braze |
| **Diseño avanzado de experimentos** | Grupos de tratamiento y exclusiones totalmente personalizables |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Capacidades de Decisioning Studio" }

## Mejores prácticas {#best-practices}

Algunas mejores prácticas para diseñar agentes de Decisioning Studio:

- **Maximiza la riqueza de datos:** cuanta más información tengan los agentes sobre tus clientes, mejor será su rendimiento.
- **Diversifica las acciones:** cuanto más diverso sea el conjunto de acciones que el agente puede realizar, más podrá personalizar su estrategia para cada usuario.
- **Minimiza las restricciones:** cuantas menos restricciones tengan tus agentes, mejor. Las restricciones deben diseñarse para respetar las reglas de negocio y, al mismo tiempo, liberar la experimentación dirigida por el agente tanto como sea posible.