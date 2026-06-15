---
nav_title: Kubit
article_title: Kubit
description: "Este artículo de referencia describe la asociación entre Braze y Kubit, una plataforma de análisis de autoservicio sin código que ofrece información instantánea sobre los productos, lo que te permite importar cohortes de usuarios de Kubit y dirigirlas a la mensajería de Braze."
alias: /partners/kubit/
page_type: partner
search_tag: Partner

---

# Kubit

> [Kubit](https://kubit.ai/) es una plataforma de análisis de autoservicio sin código que ofrece información instantánea sobre los productos.

La integración de Braze y Kubit te permite [importar cohortes de usuarios de Kubit]({{site.baseurl}}/partners/data_and_analytics/cohort_import/kubit/) y dirigirlas a la mensajería de Braze. Además, mediante el [uso compartido de datos seguros de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/), puedes integrar los datos sin procesar de campañas e impresiones de Braze con los análisis de productos de Kubit para medir el impacto de estas campañas en tiempo real. Este enfoque proporciona información sobre el ciclo de vida completo de tus usuarios sin requerir ningún esfuerzo de ingeniería.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de empresa Kubit | Se necesita una cuenta de empresa Kubit para aprovechar esta asociación. |
| Coincidencia de ID de usuario | Los datos de tus clientes en Kubit y Braze deben tener ID de usuario coincidentes en las dos plataformas. Esto incluye también los UUID anónimos. Visita nuestra [documentación]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android) para leer cómo Braze establece los ID de usuario. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Análisis de datos de Braze en Kubit {#analyzing-braze-data-in-kubit}

Aprovecha el [uso compartido de datos seguros de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) para compartir con Kubit los datos sin procesar de tus campañas e impresiones de Braze e incorporarlos a los análisis de autoservicio de Kubit, lo que te proporcionará una visión completa del ciclo de vida de los usuarios.

A modo de referencia, aquí están todos los [campos de Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2) disponibles para incorporarse en los análisis de Kubit. Los detalles de este paso son muy específicos de cada cliente y requieren configuraciones especiales. Habla con tu director de cuentas de Kubit o con [support@kubit.ai](support@kubit.ai) para obtener más información.