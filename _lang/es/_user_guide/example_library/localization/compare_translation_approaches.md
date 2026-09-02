---
nav_title: Comparar enfoques de traducción
article_title: Comparar enfoques para gestionar traducciones multilingües
page_order: 1
page_type: reference
description: "Compara Liquid manual, Content Blocks, catálogos, mensajes multilingües, partners de traducción y contenido conectado para elegir cómo Kitchenerie gestiona el texto localizado."
tool:
  - Campaigns
  - Canvas
---

# Comparar enfoques para gestionar traducciones multilingües {#compare-approaches-for-managing-multi-language-translations}

> Evalúa cómo se almacena, actualiza, previsualiza y envía el texto localizado para que puedas elegir un enfoque de localización que se ajuste a tu flujo de trabajo de QA, combinación de canales y frecuencia de actualización.

## Acerca de este ejemplo {#about-this-example}

Kitchenerie, un minorista ficticio de artículos de cocina, envía correos electrónicos, push y mensajes dentro de la aplicación en inglés, francés y alemán. Los equipos de marketing e ingeniería necesitan una forma repetible y escalable de gestionar las traducciones en todas las Campaigns.

Braze admite varios patrones de localización:

- **Liquid condicional manual:** Contenido introducido por idioma en el cuerpo del mensaje
- **Content Blocks:** Bloques reutilizables (con o sin etiquetas de traducción multilingüe)
- **Catálogos:** Filas de traducción estructuradas con clave por configuración regional
- **Mensajes multilingües:** Etiquetas de traducción, cargas de CSV y la API de traducción (acceso anticipado)
- **Partners de traducción:** Smartling, Phrase, Lokalise y otros
- **Contenido conectado:** Cadenas localizadas obtenidas de tu CMS o API en el momento del envío

Este ejemplo compara las ventajas y desventajas para que puedas elegir el enfoque que mejor se adapte a tu flujo de trabajo de QA, combinación de canales, frecuencia de actualización y recursos del equipo. No sustituye la configuración paso a paso de ningún método individual. Para recorridos detallados de cada característica, comienza con [Localización]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) y [Mensajes multilingües]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Consideraciones {#considerations}

- Decide si necesitas vista previa y control de calidad en el panel, flujos de trabajo de traducción profesional, actualizaciones de contenido de alta frecuencia o texto gestionado por un CMS en tiempo real antes de elegir un patrón.
- Los [mensajes en varios idiomas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) son compatibles con correo electrónico, push, banners, mensajes dentro de la aplicación y Content Blocks. Ten en cuenta que servicio de mensajes cortos y WhatsApp utilizan otros patrones de localización. Liquid manual, Content Blocks, catálogos, partners y contenido conectado pueden aplicarse en todos los canales donde esas características sean compatibles.
- Braze no genera traducciones. Tú proporcionas el texto a través del panel, CSV, API, importación de catálogo, flujo de trabajo del partner o CMS externo.
- Liquid manual y Content Blocks con condicionales integrados necesitan convenciones de nomenclatura y procesos de revisión a medida que crecen los idiomas, y los flujos de trabajo de varios idiomas y de partners centralizan las actualizaciones, pero pueden requerir mantenimiento de CSV o API.
- El contenido conectado y algunos flujos de partners dependen de sistemas externos. Si una API o un CMS no está disponible en el momento del envío, el contenido localizado puede no cargarse.
- La superposición es habitual. Por ejemplo, puedes usar etiquetas de varios idiomas para el cuerpo de los correos electrónicos, Content Blocks para pies de página compartidos y catálogos para el texto de productos en el mismo programa.

## Configuración {#setup}

### Paso 1: Captura tus requisitos de localización {#step-1-capture-your-localization-requirements}

| Requisito | Preguntas a responder |
| --- | --- |
| Vista previa y QA | ¿Los especialistas en marketing necesitan previsualizar cada configuración regional en el creador de Braze antes del envío? |
| Escala | ¿Cuántos idiomas y con qué frecuencia cambia el texto? |
| Flujo de trabajo | ¿Necesitas revisión, correcciones y aprobaciones por parte de traductores? |
| Forma de los datos | ¿El texto es contenido de marketing de formato libre o campos de producto estructurados (nombres, precios, URLs)? |
| Automatización | ¿Deben actualizarse las traducciones automáticamente cuando cambia tu CMS? |
| Habilidades del equipo | ¿Tu equipo puede mantener Liquid, cargas de CSV, APIs o integraciones de partners? |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Captura tus requisitos de localización" }

### Paso 2: Compara los enfoques de un vistazo {#step-2-compare-approaches-at-a-glance}

| Dimensión | Liquid manual | Content Blocks | Catálogos | Mensajes multilingües | Partners de traducción | Contenido conectado |
| --- | --- | --- | --- | --- | --- | --- |
| Vista previa en el panel / QA | Sí | Sí | Sí | Sí | Varía según el partner | Limitada: más difícil previsualizar contenido obtenido |
| Predeterminado (sin integración) | Sí | Sí | Parcial: se requiere configuración de catálogo | Sí | No: se requiere configuración del proveedor | No: se requiere API o CMS |
| Cobertura de canales | Todos los canales compatibles | Todos los canales compatibles | Todos los canales compatibles | Correo electrónico, push, banners, mensajes dentro de la aplicación, Content Blocks | Varía según el partner | Todos los canales compatibles |
| Esfuerzo de implementación | Bajo | Bajo–medio | Medio | Bajo | Alto (depende del partner) | Medio |
| Esfuerzo continuo (BAU) | Alto: ediciones por mensaje | Medio: mantenimiento de bloques | Medio: actualizaciones por CSV o API | Medio: cargas de CSV | Medio: gestionado en la plataforma | Bajo: obtenido en el momento del envío |
| Actualizaciones de alta frecuencia | No | Parcial | No | Parcial | Sí | Sí |
| Flujo de traducción profesional | No | No | No | No | Sí | No |
| Datos estructurados / de producto | Limitado | Limitado | Sí: ideal para texto con clave | Limitado | Varía | Sí: a través de fuente externa |
| Riesgo de dependencia externa | Ninguno | Ninguno | Ninguno | Ninguno | Medio | Medio: el envío falla si la fuente no está disponible |
| Más adecuado para | Pocos idiomas, actualizaciones infrecuentes | Componentes compartidos entre mensajes | Muchas configuraciones regionales de cadenas estructuradas | Muchos idiomas con menor esfuerzo de copiar y pegar | Traducción empresarial con aprobaciones | Localización dinámica impulsada por CMS |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="Compara los enfoques de un vistazo" }

### Paso 3: Asocia los escenarios estilo Kitchenerie con un enfoque {#step-3-match-kitchenerie-style-scenarios-to-an-approach}

| Escenario de Kitchenerie | Punto de partida recomendado |
| --- | --- |
| Tres idiomas, pocas Campaigns al mes, equipo de marketing pequeño | Liquid condicional manual o Content Blocks con Liquid |
| Encabezado, pie de página y bloques legales compartidos entre correo electrónico e IAM | Content Blocks, con [traducciones multilingües guardadas en el bloque]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#save-translations-in-content-blocks) cuando las configuraciones regionales escalen |
| Nombres de productos, líneas promocionales y URLs de imágenes organizados por configuración regional | [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs) |
| Correo electrónico y push en ocho o más configuraciones regionales con vista previa en el creador | [Mensajes multilingües]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) |
| TMS central con flujo de trabajo de traductores y aprobaciones | [Partners de localización]({{site.baseurl}}/partners/message_personalization/localization) (por ejemplo, Smartling o Phrase) |
| Texto gestionado en un CMS que se actualiza diariamente | [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Asocia los escenarios estilo Kitchenerie con un enfoque" }

### Paso 4: Implementa el enfoque que seleccionaste {#step-4-implement-the-approach-you-selected}

1. **Liquid condicional manual:** Usa los atributos de perfil `language` o de configuración regional con Liquid `if` / `elsif` / `else`. Consulta [Enfoques alternativos]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#alternative-approaches) y [Lógica condicional]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic).
2. **Content Blocks:** Crea bloques reutilizables; opcionalmente, oculta Liquid condicional dentro de los bloques. Consulta [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) y la pestaña Content Blocks en [Envío de mensajes traducidos]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages).
3. **Catálogos:** Importa filas de traducción (por ejemplo, `id`, `context`, `language`, `body`) y haz referencia a ellas con Liquid `catalog_items`. Consulta la pestaña Catálogos en [Envío de mensajes traducidos]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages).
4. **Mensajes multilingües:** [Añade configuraciones regionales]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings), envuelve el texto en etiquetas de traducción y luego carga un CSV. Si tienes acceso anticipado a los [endpoints de traducción]({{site.baseurl}}/api/endpoints/translations), puedes actualizar las traducciones por API en su lugar. Previsualiza con **Multi-language user** en el creador.
5. **Partners de traducción:** Configura las configuraciones regionales del espacio de trabajo y luego sigue la integración de tu partner (por ejemplo, [Smartling]({{site.baseurl}}/partners/message_personalization/localization/smartling) o [Phrase]({{site.baseurl}}/partners/message_personalization/localization/phrase)).
6. **Contenido conectado:** Llama a tu CMS o API de traducción en el momento del envío. Prueba a fondo; la vista previa puede no reflejar las respuestas de la API en vivo. Consulta [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content).

Para la orquestación de Canvas y Campaigns entre regiones (un recorrido frente a un recorrido por país), consulta [Gestión de traducciones]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#translation-management) en la página de localización.

## Artículos relacionados {#related-articles}

- [Localización]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)
- [Mensajes en varios idiomas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)
- [Configuración de localización]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
- [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Partners de localización]({{site.baseurl}}/partners/message_personalization/localization)
- [Idioma de accesibilidad para mensajes localizados]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility)