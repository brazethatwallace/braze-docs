---
nav_title: Decisioning Studio Go
article_title: BrazeAI Decisioning Studio Go
page_order: 5.5
description: "Aprende a configurar e integrar BrazeAI Decisioning Studio<sup>TM</sup> Go en Braze."
---

# BrazeAI Decisioning Studio™ Go

> Aprende a configurar e integrar BrazeAI Decisioning Studio™ Go en Braze.

## Acerca de Decisioning Studio Go {#about-decisioning-studio-go}

Decisioning Studio Go es un agente de decisión con IA para programas de correo electrónico recurrentes. En lugar de elegir una única línea del asunto ganadora, horario de envío o imagen para toda una audiencia, el agente selecciona la mejor combinación para cada destinatario en función de su participación anterior.

Tú defines las variantes entre las que el agente puede elegir, como líneas del asunto, CTAs, imágenes, días de envío y horarios de envío. Para cada usuario en tu Segment, el agente elige la opción con más probabilidades de impulsar la participación, dentro de las restricciones y el calendario que configures.

Esto difiere de las pruebas A/B a nivel de Campaign con [Optimizar con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection), que optimiza las variantes para la audiencia. Decisioning Studio Go personaliza a nivel individual en cada envío del programa.

### Cómo funciona {#how-it-works}

El agente divide un Segment de Braze en dos grupos: un grupo de Decisioning Studio que recibe contenido de correo electrónico optimizado por IA, y un grupo de control aleatorio (mínimo 5%) que recibe combinaciones aleatorias de las mismas opciones. El grupo de control aleatorio te ofrece una medición continua y comparable del incremento del agente; siempre puedes ver cómo rinde la experiencia personalizada frente al mismo contenido enviado sin personalización.

Para cada usuario en el grupo de Decisioning Studio, el agente elige entre las opciones que proporcionaste: qué creativo enviar (incluida la línea del asunto, el CTA y la imagen específicos dentro de él), y cuándo enviarlo (día de la semana y hora del día, respetando las horas tranquilas y la zona horaria local del usuario). [Configura tu agente de Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup) cubre cada uno de estos aspectos en detalle.

A medida que los usuarios interactúan —o no— el agente aprende. Los informes indican cuándo el agente aún está en su período de entrenamiento en comparación con cuando está personalizando activamente, para que siempre sepas en qué etapa se encuentra el agente.

### Qué configuras {#what-you-configure}

| Configuración | Descripción |
|---|---|
| **Audiencia** | Un único Segment de Braze como público de entrada. El agente divide automáticamente el Segment entre el grupo de decisión y el grupo de control aleatorio. |
| **Calendario** | Frecuencia de envío (por ejemplo, una única selección tres veces por semana), días de la semana permitidos, horas tranquilas en la zona horaria local del usuario y adherencia a las reglas de limitación de frecuencia a nivel de agente. |
| **Creativos** | Uno o más creativos base creados en el creador de Braze. Dentro de cada creativo base, puedes marcar una línea del asunto, un CTA y una imagen como puntos de personalización usando etiquetas de Liquid, y luego proporcionar una lista de variantes para cada uno. El agente decide qué creativo base y variante usar para cada destinatario. |
| **Restricciones** | Límites que evitan que el agente envíe el mismo creativo base o la misma línea del asunto a un usuario más de una vez dentro de una ventana que tú defines. |
| **Revisión y lanzamiento** | Una pantalla de validación final muestra cualquier advertencia a la que debas prestar atención antes de lanzar. El agente pasa de **Borrador** a **Activo** y comienza a enviar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuración de Decisioning Studio Go" }

### Cuándo usar Decisioning Studio Go {#when-to-use-decisioning-studio-go}

El mejor ajuste son los programas de correo electrónico recurrentes con audiencias estables y contenido en el que se pueda hacer clic, como calendarios siempre activos (recompensas, lanzamientos de contenido, recordatorios de ciclo de vida), programas perennes (recuperación, reactivación) y promociones con múltiples correos electrónicos. Estos dan al agente suficiente volumen y variedad para aprender de manera significativa.

Consulta [Ejemplos para Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples) para obtener orientación detallada de ajuste por tipo de programa.

### Dónde se ubica Decisioning Studio Go en la línea de productos de Decisioning Studio {#where-decisioning-studio-go-sits-in-the-decisioning-studio-suite}

Decisioning Studio Go es el nivel de entrada de BrazeAI Decisioning Studio. Está diseñado para especialistas en marketing que desean personalización de correo electrónico uno a uno sin la complejidad de configuración de una implementación completa de Decisioning Studio Pro.

Decisioning Studio Pro añade:
- Optimización para cualquier métrica de negocio (no solo clics)
- Conexión a cualquier origen de datos propios
- Decisión multicanal
- Patrones de orquestación extendidos
- Soporte dedicado del equipo de AI Decisioning Services de Braze

## Próximos pasos {#next-steps}

{% article_tiles %}
- name: Configura tu agente de Decisioning Studio Go
  link: /docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup/
- name: Revisa los ejemplos para Decisioning Studio Go
  link: /docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples/
- name: Preguntas frecuentes
  link: /docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq/
{% endarticle_tiles %}