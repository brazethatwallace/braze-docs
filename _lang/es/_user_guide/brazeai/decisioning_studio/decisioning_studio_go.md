---
nav_title: Decisioning Studio Go
article_title: BrazeAI Decisioning Studio Go
page_order: 5.5
description: "Aprende a configurar e integrar BrazeAI Decisioning Studio<sup>TM</sup> Go en Braze."
---

# BrazeAI Decisioning Studio™ Go

> Aprende a configurar e integrar BrazeAI Decisioning Studio™ Go en Braze.

## Acerca de Decisioning Studio Go {#about-decisioning-studio-go}

Decisioning Studio Go es un agente de toma de decisiones con IA para programas de correo electrónico recurrentes. En lugar de elegir una única línea del asunto, hora de envío o imagen ganadora para toda la audiencia, el agente selecciona la mejor combinación para cada destinatario en función de su participación pasada.

Tú defines las variantes entre las que el agente puede elegir, como líneas del asunto, CTA, imágenes, días de envío y horas de envío. Para cada usuario de tu segmento, el agente elige la opción con más probabilidades de generar participación, dentro de las restricciones y el calendario que configures.

Esto difiere de las pruebas A/B a nivel de Campaign o de la [selección inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection), que optimizan una única variante para toda la audiencia. Decisioning Studio Go personaliza a nivel individual en cada envío del programa.

### Cómo funciona {#how-it-works}

El agente divide un segmento de Braze en dos grupos: un grupo de Decisioning Studio que recibe contenido de correo electrónico optimizado por IA, y un grupo de control aleatorio (mínimo 5 %) que recibe combinaciones aleatorias de las mismas opciones. El control aleatorio te proporciona una medición continua y comparable del incremento del agente; siempre puedes ver cómo rinde la experiencia personalizada frente al mismo contenido enviado sin personalización.

Para cada usuario del grupo de Decisioning Studio, el agente elige entre las opciones que proporcionaste: qué creativo enviar (incluida la línea del asunto, el CTA y la imagen específicos dentro de él), y cuándo enviarlo (día de la semana y hora del día, respetando las horas tranquilas y la zona horaria local del usuario). [Configura tu agente de Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup) cubre cada uno de estos aspectos en detalle.

A medida que los usuarios interactúan —o no—, el agente aprende. Los informes indican cuándo el agente aún está en su periodo de entrenamiento frente a cuándo está personalizando activamente, para que siempre sepas en qué etapa se encuentra.

### Qué configuras {#what-you-configure}

| Configuración | Descripción |
|---|---|
| **Audiencia** | Un único segmento de Braze como público de entrada. El agente divide automáticamente el segmento entre el grupo de toma de decisiones y el grupo de control aleatorio. |
| **Calendario** | Frecuencia de envío (por ejemplo, una única selección tres veces por semana), días de la semana permitidos, horas tranquilas en la zona horaria local del usuario y cumplimiento de las reglas de limitación de frecuencia a nivel de agente. |
| **Creativos** | Uno o más creativos base creados en el creador de Braze. Dentro de cada creativo base, puedes marcar una línea del asunto, un CTA y una imagen como puntos de personalización mediante etiquetas de Liquid, y luego proporcionar una lista de variantes para cada uno. El agente decide qué creativo base y variante usar para cada destinatario. |
| **Restricciones** | Límites que impiden que el agente envíe el mismo creativo base o la misma línea del asunto a un usuario más de una vez dentro de una ventana que tú defines. |
| **Revisión y lanzamiento** | Una pantalla de validación final muestra cualquier advertencia que debas atender antes de lanzar. El agente pasa de **Draft** a **Live** y comienza a enviar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuración de Decisioning Studio Go" }

### Cuándo usar Decisioning Studio Go {#when-to-use-decisioning-studio-go}

El mejor ajuste son los programas de correo electrónico recurrentes con audiencias estables y contenido con enlaces clicables, como calendarios permanentes (recompensas, lanzamientos de contenido, recordatorios de ciclo de vida), programas evergreen (recuperación, reactivación) y promociones con múltiples correos electrónicos. Estos le dan al agente suficiente volumen y variedad para aprender de forma significativa.

Consulta [Ejemplos para Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples) para obtener orientación detallada por tipo de programa.

### Dónde se ubica Decisioning Studio Go en la línea de productos de Decisioning Studio {#where-decisioning-studio-go-sits-in-the-decisioning-studio-suite}

Decisioning Studio Go es el nivel de entrada de BrazeAI Decisioning Studio. Está diseñado para especialistas en marketing que desean personalización de correo electrónico uno a uno sin la carga de configuración de una implementación completa de Decisioning Studio Pro.

Decisioning Studio Pro añade:
- Optimización para cualquier métrica empresarial (no solo clics)
- Conexión a cualquier origen de datos propios
- Toma de decisiones multicanal
- Patrones de orquestación extendidos
- Soporte dedicado del equipo de Braze AI Decisioning Services

## Próximos pasos {#next-steps}

- [Configura tu agente de Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup): configura audiencia, calendario, creativos y restricciones
- [Revisa ejemplos para Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples) para confirmar que tu programa es un buen candidato
- Consulta las [preguntas frecuentes]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq) para dudas comunes