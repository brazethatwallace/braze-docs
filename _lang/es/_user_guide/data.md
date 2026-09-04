---
nav_title: Datos
article_title: "Plataforma de datos de Braze"
page_order: 3
description: "Aprende sobre la plataforma de datos de Braze, incluyendo cómo unificar, activar y distribuir tus datos."
---

# Plataforma de datos de Braze {#braze-data-platform}

> Aprende sobre la plataforma de datos de Braze, incluyendo cómo unificar, activar y distribuir tus datos.

La plataforma de datos de Braze (BDP) es un conjunto completo y componible de capacidades de datos e integraciones de partners que te permite crear experiencias personalizadas para tus clientes. En Braze, pensamos en los datos en términos de tres tareas relacionadas con los datos: [Unificación]({{site.baseurl}}/user_guide/data/unification), [Activación]({{site.baseurl}}/user_guide/data/activation) y [Distribución]({{site.baseurl}}/user_guide/data/distribution).

Al utilizar una combinación de características de la plataforma de datos de Braze, puedes aprovechar tus datos para crear mensajes significativos y dirigidos que respondan a lo que tus clientes hacen en tiempo real.

## Cómo funciona {#how-it-works}

### Unifica tus datos {#unify-your-data}

Los datos de usuario fluyen hacia Braze a través de muchos puntos de entrada. Recopila y consolida datos propios de cualquier fuente usando [APIs]({{site.baseurl}}/api/home) y [SDKs]({{site.baseurl}}/developer_guide/sdk_integration). También puedes usar herramientas de ingesta integradas como [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) para crear una integración directa desde tu almacén de datos o solución de almacenamiento de archivos a Braze, o usar [Data Transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation) para crear y gestionar integraciones de webhooks para transferir datos a Braze.

### Activa tus datos {#activate-your-data}

Limpia, organiza y prepara tus datos para su uso. Esto implica comprender los comportamientos y preferencias de tus clientes en tiempo real con perfiles de usuario y Segments. Consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary) mientras creas mensajes dirigidos, y usa [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs) para enriquecer tus mensajes con datos de productos o contenido. Identifica cómo responden tus clientes a estas experiencias personalizadas.

### Distribuye tus datos {#distribute-your-data}

Transmite y [exporta tus datos]({{site.baseurl}}/user_guide/data/distribution/export_braze_data) a sistemas externos para obtener información y tomar decisiones en el siguiente paso. Usa [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para transmitir datos de eventos de Braze a un almacén de datos y potenciar herramientas de inteligencia empresarial. También puedes ampliar tus capacidades de datos con [integraciones de partners tecnológicos]({{site.baseurl}}/partners/data_and_analytics).

## Infraestructura de datos {#data-infrastructure}

La infraestructura de datos de Braze incluye [centros de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_centers) que ayudan a minimizar la latencia, es decir, el tiempo que tardan los datos en viajar entre el servidor y el usuario. Esta distribución geográfica permite que nuestros servicios sean fiables y escalables. También ofrecemos [cifrado a nivel de campo]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption) para ayudar a proteger los datos sensibles y minimizar la información de identificación personal (PII) compartida en Braze. Para más información sobre uso y facturación, consulta [Puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points).

## Principios fundamentales {#core-principles}

Los datos desempeñan un papel crucial en la mejora de tu estrategia de interacción con los clientes, ya que te permiten crear experiencias personalizadas, comprender el comportamiento del cliente y optimizar las estrategias de mensajería. En Braze, desarrollamos todas las capacidades de datos teniendo en cuenta tres principios fundamentales:

{% details Hacer que tus datos trabajen más %}
- **Flexibles y basados en componentes:** Nuestro objetivo principal es ayudarte a utilizar tus datos de forma más eficaz y completa. Construido con una arquitectura componible, puedes aprovechar las tecnologías que necesitas para que tus datos trabajen más, sin middleware innecesario.
- **Integraciones de partners:** Braze prioriza las integraciones con las mejores tecnologías del ecosistema (y ofrece API) que facilitan el intercambio de datos bidireccional en tiempo real.
- **Arquitectura de procesamiento en flujo:** Puedes desencadenar acciones sobre cualquier punto de datos ingestado en Braze para segmentación, orquestación y personalización.
{% enddetails %}

{% details Mejorar la agilidad de los datos para impulsar el rendimiento %}
- **Construcción flexible de audiencias:** Reduce la dependencia de los equipos técnicos para crear audiencias y entregar una interacción personalizada con los clientes a escala.
- **Velocidad y rendimiento:** Los datos y la información de participación se entregan en tiempo real, lo que respalda una interacción con los clientes iterativa y eficaz, así como una toma de decisiones empresarial más amplia.
{% enddetails %}

{% details Mantener tus datos seguros, protegidos y en conformidad %}
- **Prácticas de seguridad líderes en la industria:** Realizamos auditorías periódicas de terceros, incluidas SOC 2 Tipo 2 e ISO 27001, para cumplir con los más altos estándares de la industria. Mantenemos un programa público de recompensas por errores para abordar de forma proactiva posibles vulnerabilidades y contamos con un equipo de seguridad dedicado comprometido con la protección de tus datos.
- **Cumplimiento normativo de la industria:** Proporcionamos herramientas que promueven el cumplimiento de las regulaciones de protección de datos, incluidos el RGPD y la CCPA.
- **Privacidad de datos:** Puedes gestionar el consentimiento del usuario final, procesar solicitudes y ejecutar los derechos de los consumidores.
{% enddetails %}