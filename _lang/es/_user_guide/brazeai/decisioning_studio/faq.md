---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre Decisioning Studio
page_order: 8
page_type: FAQ
description: "Esta página ofrece respuestas a preguntas frecuentes sobre Decisioning Studio."
---

# Preguntas frecuentes {#frequently-asked-questions}

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre Decisioning Studio.

## ¿Qué es un agente de decisión? {#what-is-a-decisioning-agent}

Un agente de decisión es una configuración personalizada para BrazeAI Decisioning Studio™ que se adapta a medida para cumplir un objetivo de negocio específico. Esto viene definido por la métrica de éxito, las dimensiones y las opciones que elijas. El agente de decisión descubre automáticamente la acción óptima para cada cliente con el fin de maximizar la métrica empresarial elegida.

### ¿Qué métricas puedo optimizar? {#what-metrics-can-i-optimize-for}

Puedes optimizar cualquier métrica empresarial que se ajuste a tus objetivos, como los ingresos, las conversiones, los ingresos medios por usuario (ARPU), el LTV del cliente (valor del ciclo de vida del cliente), la ganancia, las renovaciones de contratos o cualquier otro indicador clave de rendimiento empresarial.

### ¿Qué son las dimensiones en Decisioning Studio? {#what-are-dimensions-in-decisioning-studio}

Las dimensiones pueden considerarse como los *tipos de palancas* que el agente de decisión puede accionar para maximizar la métrica de éxito. Las dimensiones típicas incluyen la oferta, la línea del asunto, la creatividad, el canal o la hora de envío.

### ¿Qué es un banco de acciones? {#what-is-an-action-bank}

El banco de acciones define las *opciones específicas* a las que tiene acceso el agente de decisión para cada dimensión «palanca». Por ejemplo, para una dimensión de canal, defines los canales específicos a los que tiene acceso el agente de decisión. Para una dimensión de oferta, defines las ofertas específicas que el agente de decisión puede probar.

### ¿Puede el agente de decisión realizar acciones que no haya configurado? {#can-the-decisioning-agent-take-actions-i-havent-configured}

No. El agente de decisión solo puede realizar las acciones que tú configures y añadas al banco de acciones. Esto significa que todas las acciones posibles se definen mediante las combinaciones de lo que incluyes en el banco de acciones.

### ¿Qué son las restricciones? {#what-are-constraints}

Las restricciones limitan las acciones del agente de decisión para que respete las reglas de negocio fundamentales. Por ejemplo, esto podría consistir en impedir que una oferta específica sea seleccionada para clientes que se encuentren en una zona geográfica no elegible, o en establecer un presupuesto máximo que el agente de decisión puede gastar.

### ¿Cuál es la diferencia entre Decisioning Studio Go y Decisioning Studio Pro? {#what-is-the-difference-between-decisioning-studio-go-and-decisioning-studio-pro}

Decisioning Studio Pro incluye el soporte de los servicios de toma de decisiones con IA del equipo de ciencia de datos de Braze, que te ayudará a diseñar y configurar tu agente para maximizar los resultados de tu negocio. Para obtener más información, consulta [Decisioning Studio Go frente a Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio#decisioning-studio-go-vs-decisioning-studio-pro).