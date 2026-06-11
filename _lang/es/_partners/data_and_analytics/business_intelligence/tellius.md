---
nav_title: Tellius
article_title: Tellius
alias: /partners/tellius/
description: "Este artículo de referencia describe la asociación entre Braze y Tellius, una plataforma de inteligencia de decisiones y análisis aumentado, que te permite aprovechar los datos, sin depender de ingenieros de BI, para crear dashboards y generar información para tomar mejores decisiones de marketing."
page_type: partner
search_tag: Partner

---

# Tellius

> [Tellius](https://www.tellius.com/), una plataforma de inteligencia para la toma de decisiones y análisis aumentado, te permite responder preguntas sobre tus datos mediante búsquedas en lenguaje natural y profundizar para entender el "por qué" con información guiada basada en IA.

La integración de Braze y Tellius permite a los usuarios aprovechar los datos, sin depender de ingenieros de BI, para crear dashboards y generar información que les permita tomar mejores decisiones de marketing. Esta integración requiere que los datos de Braze se almacenen en Snowflake, donde Tellius puede conectarse directamente y ejecutar consultas con integración en modo en vivo.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Tellius | Se necesita una cuenta Tellius para aprovechar esta asociación. Puedes empezar tu recorrido con Tellius con una [prueba gratuita](https://www.tellius.com/free-trial/)|
| Programa de uso compartido de datos de Snowflake | Si ya eres cliente de Snowflake, ponte en contacto con tu representante de Braze sobre el programa de uso compartido de datos de Snowflake para transferir tus datos de Braze a tu instancia de Snowflake.|
| Cuenta Snowflake Reader | Si no eres cliente de Snowflake, ponte en contacto con tu representante de Braze para que te proporcionen una cuenta de Snowflake Reader que te permita acceder a tus datos de Braze.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Obtener acceso a Braze a través de Snowflake {#step-1-obtain-access-to-braze-through-snowflake}

Braze almacena datos granulares de los clientes en Snowflake. Puedes aprovechar tus datos de Braze para generar información a través del programa de uso compartido de datos de Braze con Snowflake u obteniendo una cuenta de Snowflake Reader.

Sigue la [integración de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) para configurarlo.

### Paso 2: Conectar Tellius a los datos de Braze en Snowflake {#step-2-connect-tellius-to-braze-data-in-snowflake}

Conecta Tellius a los datos de Braze en Snowflake mediante uno de los siguientes métodos:

- Acceso directo: para cargar datos en Tellius, sigue los pasos para [cargar conjuntos de datos](https://help.tellius.com/article/jn6o59d5gk-load-datasets).
- Acceso OAuth: para el acceso OAuth a Snowflake, sigue los pasos para la [autenticación OAuth](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake).

### Paso 3: Crear una Business View en Tellius a partir de los datos cargados {#step-3-create-business-view-in-tellius-from-loaded-data}

Para empezar a utilizar la búsqueda en lenguaje natural y la información automatizada, crea una [Business View](https://help.tellius.com/article/hy9yvh5tom-create-business-view) y selecciona conjuntos de datos de tu conexión con Snowflake.

### Paso 4: Saca el máximo partido a tus datos con Tellius {#step-4-get-the-most-value-out-of-your-data-using-tellius}

En Tellius hay una interfaz guiada que te acompaña por las características de la plataforma. Si tienes más preguntas o necesitas guías adicionales, consulta su [base de conocimientos](https://help.tellius.com/) completa.