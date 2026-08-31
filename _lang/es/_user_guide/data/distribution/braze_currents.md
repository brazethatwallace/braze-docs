---
page_order: 1
nav_title: Currents
article_title: Currents

layout: dev_guide

page_type: landing
description: "Esta página de inicio enumera artículos sobre el producto de datos de Braze llamado Currents. Aquí encontrarás información sobre cómo configurar Currents, los socios disponibles, la semántica de la entrega, glosarios de eventos y mucho más."
tool: currents
search_rank: 9
guide_top_header: "Braze Currents"
guide_top_text: "Comprender el impacto de tu estrategia de interacción es fundamental para orientar la iteración y optimización de tus comunicaciones con los usuarios. Para integrar estrechamente estos valiosos datos de interacción con el resto de tus operaciones y ayudar a amplificar tu inversión en ciencia de datos, la plataforma Braze realiza un seguimiento de una amplia gama de datos de eventos de tu integración para su análisis, reorientación y otros casos de uso en otros lugares dentro de tus propios sistemas. <br> <br>La herramienta Currents es una transmisión de datos en tiempo real de tus eventos de interacción que es la exportación más sólida y granular de la plataforma Braze. Te proporciona datos en un tipo de archivo Avro a uno de nuestros muchos <a href='/docs/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners'>socios de datos</a>, lo que te permite utilizar los datos únicos y valiosos que crea Braze para potenciar tus esfuerzos de inteligencia empresarial (BI) y análisis en otras plataformas de primera clase."

guide_featured_title: "Artículos de sección"
guide_featured_list:
  - name: Configurar Currents
    link: /docs/user_guide/data/distribution/braze_currents/setting_up_currents
    image: /assets/img/braze_icons/building-01.svg
  - name: Glosario de eventos Currents
    link: /docs/user_guide/data/distribution/braze_currents/event_glossary
    image: /assets/img/braze_icons/data.svg
  - name: Casos de uso
    link: /docs/user_guide/data/distribution/braze_currents/use_cases
    image: /assets/img/braze_icons/expand-05.svg
  - name: Preguntas frecuentes
    link: /docs/user_guide/data/distribution/braze_currents/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

## Capacidades de Currents {#currents-capabilities}

Currents te permite:
* Transmitir datos de eventos de Braze a un almacén de datos o a uno de nuestros [partners de análisis]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) para un análisis detallado.
* Transmitir datos de eventos de Braze de forma continua para impulsar herramientas de inteligencia empresarial, algoritmos de aprendizaje automático y mucho más.
* Dirigir datos de eventos de Braze a una variedad de otros sistemas usando [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium), [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment) o [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents).

Hay mucho más que puedes hacer con los datos de eventos a los que se accede mediante Currents. ¡[Braze también usa Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents)!

## Modelo de distribución de datos de Currents {#currents-data-distribution-model}

Currents utiliza pools de derechos de uso para controlar la creación de conectores y el seguimiento opcional de eventos.

- Los **derechos de uso de eventos de interacción** son necesarios para cada conector estándar de Currents que crees.
- Los **derechos de uso de eventos de comportamiento del cliente** son necesarios cuando habilitas **Track Customer Behavior and User Events** en un conector.
- Los **derechos de uso de perfiles y atributos de usuario** son necesarios cuando habilitas **Track user profiles and attributes** en un conector.

Los conectores de prueba de Currents utilizan un límite de prueba independiente y no consumen derechos de uso de conectores estándar.

Si alcanzas algún límite de derechos de uso, consulta [Solución de problemas de configuración de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#troubleshooting) y las [Preguntas frecuentes sobre Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq), o ponte en contacto con tu director de cuentas.

## Cómo acceder a Currents {#how-to-access-currents}

Un conector de Currents ya está incluido en muchos de nuestros paquetes de nivel profesional y empresarial. Si te interesa utilizar Currents, ponte en contacto con tu director de cuentas. Tu director de cuentas y nuestros especialistas en datos pueden ayudarte con la [configuración e integración de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents).

<br><br>