---
nav_title: Lanzar tu agente
article_title: Lanzar tu agente
page_order: 5
page_type: reference
description: "Aprende a lanzar tu agente de Decisioning Studio y cerrar el ciclo de toma de decisiones con IA para una optimización de autoaprendizaje."
---

# Lanzar tu agente {#launch-your-agent}

> Después de haber conectado los orígenes de datos, configurado la orquestación y diseñado tu agente, estás listo para lanzarlo. Este artículo cubre la activación de tu agente y el cierre del ciclo de toma de decisiones con IA para que el agente pueda aprender y mejorar continuamente.

## Pasos de lanzamiento {#launch-steps}

Después de completar todos los pasos de configuración con tu equipo de AI Decisioning Services:

1. Revisa la configuración de tu agente para asegurarte de que todos los ajustes sean correctos.
2. Verifica que tus conexiones de datos e integraciones de orquestación estén activas.
3. Trabaja con tu equipo de AI Decisioning Services para activar el agente.

Una vez lanzado, tu agente:
- Comenzará a recibir datos de audiencia y de clientes
- Empezará a hacer recomendaciones personalizadas para cada cliente
- Orquestará acciones a través de tu CEP configurada
- Recopilará datos de retroalimentación para aprender y mejorar con el tiempo

## Cerrar el ciclo de toma de decisiones con IA {#close-the-ai-decisioning-loop}

Una vez lanzado, tu agente necesita datos de retroalimentación para aprender y mejorar. Esto incluye datos de conversiones, datos de interacción y datos de activaciones que le indican al agente qué sucedió después de que se enviaron las decisiones de interacción con los clientes.

Para conocer los requisitos detallados sobre la preparación de estos activos de datos de retroalimentación críticos, consulta [Preparar tus orígenes de datos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/).

{% alert note %}
Si el agente está integrado de forma nativa con la plataforma de interacción con los clientes (como Braze o Salesforce Marketing Cloud), es posible que no sean necesarios pasos de configuración adicionales para los datos de retroalimentación, ya que estos pueden enviarse automáticamente con los datos de clientes.
{% endalert %}

## Monitorear tu agente {#monitor-your-agent}

Después del lanzamiento, trabaja con tu equipo de AI Decisioning Services para monitorear el rendimiento:

- **Métricas de rendimiento:** Realiza un seguimiento de tu métrica de éxito en los grupos de experimento
- **Progreso de aprendizaje:** Observa cómo evolucionan las recomendaciones del agente con el tiempo
- **Información:** Comprende qué dimensiones y opciones están generando resultados para diferentes segmentos de clientes

## Optimización continua {#ongoing-optimization}

Tu equipo de AI Decisioning Services seguirá trabajando contigo para:

- Analizar el rendimiento del agente e identificar oportunidades de optimización
- Ampliar dimensiones u opciones según sea necesario
- Ajustar restricciones en función de cambios en las reglas de negocio
- Escalar agentes exitosos a casos de uso adicionales

{% alert tip %}
El agente aprende y mejora continuamente con el tiempo. Permite tiempo suficiente para que el agente recopile datos y optimice antes de realizar cambios significativos en la configuración.
{% endalert %}