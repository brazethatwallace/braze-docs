---
nav_title: Diseña tu agente
article_title: Diseña tu agente
page_order: 3
description: "Aprende a diseñar un agente Go de BrazeAI Decisioning Studio, incluyendo la definición de la audiencia, las dimensiones y las limitaciones específicas de Go."
---

# Diseña tu agente {#design-your-agent}

> Este artículo explica cómo diseñar tu agente de Decisioning Studio Go, incluyendo cómo definir tu audiencia, seleccionar dimensiones y comprender las capacidades y limitaciones específicas de Go.

Para conocer los conceptos básicos sobre los agentes de toma de decisiones, incluidas las métricas de éxito, las dimensiones, los bancos de acciones y las restricciones, consulta [Diseño de agentes de toma de decisiones]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/design_agents/).

## Funciones de Go frente a Pro {#go-versus-pro-capabilities}

Decisioning Studio Go es una plataforma de autoservicio con capacidades optimizadas en comparación con Decisioning Studio Pro. Comprender estas diferencias te ayuda a diseñar un agente eficaz dentro del ámbito de Go.

| Capacidad | Decisioning Studio Go | Decisioning Studio Pro |
|-----------|----------------------|------------------------|
| **Métrica de éxito** | Solo clics | Cualquier métrica empresarial (ingresos, conversiones o ARPU) |
| **Dimensiones** | Banco de acciones limitado | Dimensiones ilimitadas |
| **CEP compatibles** | Braze, SFMC | Cualquier CEP (nativo y personalizado) |
| **Datos del cliente** | Solo interacción | Todos los datos 1P |
| **Configuración** | Autoservicio | Soporte de servicios de toma de decisiones con IA |
| **Grupos experimentales** | Go + Control aleatorio + BAU opcional | Totalmente personalizable |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Funciones de Go frente a Pro" }

## Diseña tu agente Go {#design-your-go-agent}

Al diseñar un agente de Decisioning Studio Go, tomarás decisiones en las siguientes áreas:

### Paso 1: Define tu audiencia {#step-1-define-your-audience}

Tu audiencia es el conjunto de clientes con los que interactuará el agente. En Go, las audiencias se definen en tu CEP:

{% tabs %}
{% tab Braze %}

**Definición de audiencia en Braze:**

1. Crea un segmento en Braze que defina los clientes a los que quieres que se dirija el agente.
2. Al configurar tu experimentador en el portal de Decisioning Studio Go, selecciona este segmento como tu audiencia objetivo.

{% alert tip %}
Considera la posibilidad de crear un segmento específico para tu experimentador de Decisioning Studio Go con el fin de mantener tus pruebas aisladas y medibles.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

**Definición de audiencia en SFMC:**

1. Configura una extensión de datos que contenga tu audiencia objetivo.
2. Asegúrate de que esta extensión de datos se actualice diariamente con los datos más recientes de los clientes.
3. Haz referencia a esta extensión de datos en el portal de Decisioning Studio Go al configurar tu experimentador.

{% endtab %}
{% endtabs %}

### Paso 2: Selecciona tus dimensiones {#step-2-select-your-dimensions}

Las dimensiones son las «palancas» que el agente puede accionar para personalizar la experiencia del cliente. Entre ellas se incluyen dimensiones creativas, como la línea del asunto y la imagen principal, así como dimensiones relacionadas con el tipo de envío, como la frecuencia de los correos electrónicos o la hora del día.

{% alert note %}
Las dimensiones específicas disponibles dependen de tu CEP y de cómo estén configuradas tus campañas. Trabaja con las plantillas y el contenido que has configurado en tu CEP.
{% endalert %}

### Paso 3: Configura tu banco de acciones {#step-3-configure-your-action-bank}

El banco de acciones define las opciones específicas entre las que el agente puede elegir para cada dimensión. Por ejemplo:

- **Plantillas de correo electrónico:** selecciona las plantillas que el agente puede utilizar (estas deben configurarse primero en tu CEP).
- **Líneas del asunto:** define las variantes de la línea del asunto que el agente puede probar.
- **Horarios de envío:** especifica las franjas horarias entre las que el agente puede elegir.

### Paso 4: Configura los grupos experimentales {#step-4-set-up-experiment-groups}

Decisioning Studio Go crea automáticamente grupos experimentales para medir el rendimiento:

| Grupo | Descripción |
|-------|-------------|
| **Decisioning Studio Go** | Clientes que reciben recomendaciones optimizadas por IA |
| **Control aleatorio** | Clientes que reciben opciones seleccionadas al azar (comparación con la línea de base) |
| **Business as Usual (opcional)** | Clientes que reciben tu campaña actual (si se compara con el rendimiento actual) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 4: Configura los grupos experimentales" }

{% alert important %}
Para realizar una comparación precisa, asegúrate de que ningún cliente pueda pertenecer a más de un grupo experimental y de que los clientes se asignen aleatoriamente a los grupos sin sesgos.
{% endalert %}

## Limitaciones a tener en cuenta {#limitations-to-consider}

Al diseñar tu agente Go, ten en cuenta estas limitaciones:

- **Solo clics:** Go optimiza las tasas de click-through. Si necesitas optimizar los ingresos, las conversiones u otras métricas empresariales, considera Decisioning Studio Pro.
- **Dimensiones limitadas:** Go admite un conjunto predefinido de dimensiones. Para dimensiones personalizadas o personalizaciones complejas, considera Decisioning Studio Pro.
- **Soporte limitado de CEP:** Go solo se integra con Braze y Salesforce Marketing Cloud. Para otras plataformas, considera Decisioning Studio Pro.

## Buenas prácticas {#best-practices}

- **Empieza con un alcance reducido:** utiliza dos o tres plantillas o variantes de línea del asunto. Esto le da al agente suficientes opciones para aprender, al tiempo que mantiene el experimento bajo control.
- **Dale tiempo:** el agente necesita datos suficientes para aprender. Espera al menos entre 2 y 4 semanas antes de sacar conclusiones sobre el rendimiento.
- **Mantén la variedad en los contenidos:** asegúrate de que tus opciones sean significativamente diferentes. Probar variaciones menores puede no aportar información significativa.
- **Supervisa regularmente:** consulta el portal de Decisioning Studio Go para supervisar el progreso del experimento y las métricas de interacción.

## Próximos pasos {#next-steps}

Una vez que hayas diseñado tu agente y lo hayas configurado en el portal de Decisioning Studio Go, estarás listo para lanzarlo:

- [Lanza tu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/launch_your_agent/)