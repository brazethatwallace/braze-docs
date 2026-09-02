---
nav_title: Casos de uso
article_title: "Caso de uso: Decisioning Studio"
description: "Este ejemplo muestra cómo una marca ficticia utiliza BrazeAI Decisioning Studio y un agente de toma de decisiones para entregar contenido personalizado y sugerencias de productos en momentos clave para los clientes."
---

# Caso de uso: recuperar clientes inactivos con un agente de toma de decisiones enfocado en ingresos {#use-case-win-back-lapsed-customers-with-a-revenue-focused-decisioning-agent}

> Este ejemplo muestra cómo una marca ficticia utiliza BrazeAI Decisioning Studio™ y un agente de toma de decisiones para dirigir a cada cliente hacia una decisión óptima del banco de acciones, personalizar la mensajería para la recuperación y optimizar los ingresos. Conecta el diseño del agente, la audiencia y los experimentos, la orquestación a través de Braze y el aprendizaje posterior al lanzamiento.

Supongamos que Poppy es administradora de CRM en Kitchenerie, una marca ficticia de comercio minorista en línea especializada en artículos de cocina.

Muchos clientes solo exploran las colecciones de temporada una o dos veces antes de abandonar la página. Los programas de recuperación anteriores utilizaban recorridos fijos y pruebas A/B manuales, que eran útiles para probar textos, pero no para aprender qué combinación de oferta, canal, cadencia y momento maximiza los ingresos por compra de cada cliente. La prioridad de la dirección es clara: recuperar a la mayor cantidad posible de compradores inactivos y aumentar los ingresos sin sobrepasar las restricciones de descuentos o frecuencia.

Este recorrido describe cómo Poppy:

- Define a los clientes inactivos o en riesgo como la audiencia del agente, mientras estructura grupos de experimento para una comparación justa
- Permite que el agente elija las mejores acciones permitidas de un banco de acciones completo para que la mensajería se mantenga personalizada a escala
- Configura la orquestación para que las decisiones fluyan hacia Braze como plataforma de interacción con los clientes
- Lanza el agente, permitiéndole aprender de forma autónoma qué impulsa los ingresos de recuperación

## Paso 1: Definir las métricas de éxito y a quién se dirige el agente {#step-1-define-success-metrics-and-who-the-agent-targets}

Poppy confirma la métrica de éxito que el agente debe maximizar: los ingresos por recompras entre los clientes que han dejado de comprar.

Define quién entra en el programa: un segmento de Braze de compradores inactivos o usuarios inactivos de alto valor. Ahora, Poppy solo necesita compartir qué segmento debe dirigir el agente con el equipo de AI Decisioning Services. La integración para extraer los datos de ese segmento ocurre en segundo plano sin que Poppy necesite configurar una integración.

## Paso 2: Crear el banco de acciones y las restricciones {#step-2-build-the-action-bank-and-constraints}

Poppy mapea las dimensiones que importan para las estrategias de recuperación:

- Oferta: envío gratuito, porcentaje de descuento o paquete de artículos
- Canal: correo electrónico, push o SMS
- Hora de envío o cadencia
- Creatividad: ilustraciones pequeñas o textos enfocados en utilidad

Para cada dimensión, enumera opciones concretas en el banco de acciones, las únicas acciones que el agente puede tomar (todo lo demás queda fuera de los límites por diseño). El agente entonces experimenta con las combinaciones permitidas para descubrir qué funciona para cada cliente mientras optimiza la métrica de éxito elegida.

## Paso 3: Preparar los datos y conectar la orquestación a Braze {#step-3-prepare-data-and-connect-orchestration-to-braze}

Siguiendo [Conectar tus datos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/connect_data_sources/), Poppy se asegura de que señales enriquecidas de primera mano (incluyendo historial de compras, afinidad de categoría, comportamiento de navegación e interacción) alimenten al agente para que cada decisión se base en comportamiento real.

Para la orquestación, utiliza la ruta nativa de Braze: Decisioning Studio decide qué enviar y cuándo; Braze lo entrega. Planifica plantillas base (Campaigns activadas por API) por canal con campos dinámicos para ofertas y creatividad, y configura la reelegibilidad.

## Paso 4: Lanzar, monitorear y optimizar para ingresos {#step-4-launch-monitor-and-optimize-for-revenue}

Tras la revisión de configuración con AI Decisioning Services, Poppy lanza el agente. El agente comienza a recomendar acciones por usuario y a orquestar envíos a través de Braze para mejorar con el tiempo.

Al combinar una métrica de éxito enfocada en ingresos con un agente de toma de decisiones que prueba continuamente las acciones permitidas, Kitchenerie pasa de envíos masivos de recuperación estáticos a decisiones 1:1 que se adaptan por cliente, con el objetivo de recuperar más clientes y aumentar los ingresos mientras se mantiene dentro de las reglas de negocio que Poppy definió.