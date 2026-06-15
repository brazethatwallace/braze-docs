---
nav_title: Nexla
article_title: Nexla
description: "Este artículo de referencia describe la asociación entre Braze y Nexla, una plataforma unificada de operaciones de datos que permite a los usuarios de Braze Currents extraer, transformar y cargar datos de «data lakes» a otras ubicaciones en un formato personalizado."
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# Nexla

> [Nexla](https://www.nexla.com) es líder en operaciones unificadas de datos y un Gartner Cool Vendor 2021. La plataforma Nexla proporciona herramientas para crear flujos de datos escalables, ofreciendo operaciones de datos gobernadas, colaboración y agilidad para los equipos empresariales y de datos. Los equipos que trabajan con datos obtienen una experiencia unificada sin código/con código bajo para integrar, transformar, aprovisionar y supervisar datos para cualquier caso de uso.

La integración de Braze y Nexla permite a los clientes que utilizan [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/) aprovechar Nexla para extraer, transformar y cargar datos de «data lakes» a otras ubicaciones en un formato personalizado, haciendo que los datos sean fácilmente accesibles en todo tu ecosistema.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta Nexla | Se necesita una [cuenta Nexla](https://www.nexla.com/get-demo) para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel de Braze desde **Configuración** > **Claves de API**. |
| Punto de conexión REST de Braze  | La URL de tu punto de conexión REST. Tu punto de conexión dependerá de la [URL de Braze de tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

Los datos como producto de Nexla, [Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information), permiten trabajar con datos de cualquier formato sin necesidad de gestionar metadatos. Cuando configures flujos de datos hacia o desde Braze con Nexla, en cuestión de minutos dispondrás de herramientas sin código. Una vez establecido el flujo de datos a un destino, Nexla supervisa el flujo y se adapta a cualquier cantidad de datos.

## Integración {#integration}

### Paso 1: Crear una cuenta Nexla {#step-1-create-a-nexla-account}

Si aún no tienes una cuenta Nexla, visita el [sitio web](https://www.nexla.com) de Nexla para solicitar una demostración y una prueba gratuitas. A continuación, conéctate a [www.dataops.nexla.io](https://www.dataops.nexla.io) e inicia sesión con tus nuevas credenciales.

### Paso 2: Añade tu fuente {#step-2-add-your-source}

#### Si Braze es tu origen de datos {#if-braze-is-your-data-source}
1. En la plataforma Nexla, ve a **Flows** > **Create a New Flow** en la barra de herramientas de la izquierda.
2. Haz clic en **Create New Source**, selecciona el conector de Braze y haz clic en **Next**.
3. Selecciona **Add a New Credential**, asigna un nombre a la credencial, añade tu clave de API de Braze y el punto de conexión REST, y haz clic en **Save**.
4. Por último, selecciona tus datos y haz clic en **Save**.

Nexla buscará en el origen los datos disponibles y generará un [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) para transformarlo o enviarlo a un destino.

#### Si Braze es tu destino {#if-braze-is-your-destination}

Visita la documentación de Nexla sobre la [conexión de fuentes a Nexla](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source).

### Paso 3: Transformar (opcional) {#step-3-transform-optional}

Si quieres realizar [transformaciones](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations) personalizadas en tus datos o utilizar los conectores prediseñados de Nexla, haz clic en el botón **Transform** del conjunto de datos para acceder al Transform Builder. En la [documentación de Nexla](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data) encontrarás orientación sobre el uso del Transform Builder.

### Paso 4: Enviar a destino {#step-4-send-to-destination}

Para enviar datos a un destino, haz clic en la flecha **Send to Destination** del conjunto de datos y selecciona cualquiera de los conectores de destino de Nexla o Braze si tenías un origen diferente. Introduce tus credenciales, configura las opciones de destino y haz clic en **Save**. Los datos empezarán a fluir instantáneamente en el formato que hayas especificado hacia el destino que elijas.

## Uso de esta integración {#using-this-integration}

Una vez configurado el flujo, no hace falta nada más. Nexla gestionará cualquier cambio en los datos de origen, escalará a cualquier dato nuevo y te notificará cualquier cambio de esquema o error para su triaje. Si quieres hacer cambios en las transformaciones, el origen o el destino, puedes hacer clic en estas opciones y realizar el cambio, y Nexla actualizará el flujo al instante.