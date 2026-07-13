---
nav_title: Lemnisk
article_title: Integrar Lemnisk con Braze
description: "Este artículo de referencia detalla la asociación entre Braze y Lemnisk, una plataforma de datos de clientes basada en IA y dirigida a la automatización del marketing, que te permite transmitir datos de usuario recopilados en Lemnisk desde varias fuentes a Braze para activarlos en varios canales y destinos utilizando las herramientas de Braze."
alias: /partners/lemnisk/
page_type: partner
search_tag: Partner

---

# Lemnisk

> [Lemnisk](https://www.lemnisk.co/) es una solución de automatización del marketing y una plataforma de datos de clientes (CDP) impulsada por IA que habilita la captura, unificación y activación en tiempo real de datos de clientes procedentes de fuentes diversas y aisladas. Entrega fácilmente estos datos unificados a través de varias plataformas MarTech y empresariales, al tiempo que ofrece análisis sólidos y en tiempo real para hacer un seguimiento de cada etapa del ciclo de vida de los datos de los clientes.

_Esta integración está mantenida por Lemnisk._

## Sobre la integración {#about-the-integration}

La integración de Lemnisk y Braze permite a las marcas y empresas liberar todo el potencial de Braze actuando como una capa de inteligencia dirigida por CDP que unifica los datos de usuario en todas las plataformas en tiempo real, y enviando la información y los comportamientos del usuario recopilados a Braze en tiempo real. Lemnisk entrega perfiles de cliente enriquecidos directamente en Braze, combinando señales de comportamiento y atributos personales que te permiten personalizar tu mensajería con un contexto más profundo.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuentas Lemnisk | Se necesita una cuenta [Lemnisk](https://www.lemnisk.co/) para beneficiarse de esta asociación. |
| API externa en Lemnisk | Ponte en contacto con tu CSM de Lemnisk para habilitar la **API externa** para tu cuenta. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permiso `users.track`. <br><br> Puede crearse en el panel de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST de Braze | La URL de tu punto de conexión REST. Tu punto de conexión dependerá de la [URL de Braze de tu cuenta]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/#api-and-sdk-endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración de Lemnisk {#integrating-lemnisk}

### Paso 1: Crear una API externa de Braze {#create-a-braze-external-api}

En Lemnisk, ve al canal API externa. Selecciona **Add New External API**. Ahora configuraremos el punto de conexión [Track Users]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) como una API externa.

![Inicio del proceso de creación de la API externa en Lemnisk]({% image_buster /assets/img/lemnisk/open_external_api.png %})

En **Basic Details**, introduce un nombre, una descripción, un canal y un identificador de canal.

![Introducción de los detalles básicos de configuración para una nueva API externa en Lemnisk]({% image_buster /assets/img/lemnisk/ext_api_basic_details.png %})

En **External API details**, introduce los detalles relevantes de tu punto de conexión `users.track`. Puedes definir varios campos a nivel de interacción utilizando {% raw %}`{{}}`{% endraw %}, lo que te permite establecer valores diferentes para distintas campañas.

![Completar el punto de conexión de la API externa y los detalles de la carga útil]({% image_buster /assets/img/lemnisk/ext_api_ext_api_details.png %})

Para finalizar la configuración de Track Users, selecciona **Save**. Se te redirigirá automáticamente a la página **Test API**.

### Paso 2: Probar la configuración {#step-2-test-the-configuration}

En la página **Test API**, introduce algunos valores de prueba para los parámetros de la API en tu vista de árbol JSON y, a continuación, selecciona **Test Configuration**.

Si tus credenciales y las definiciones de la API son correctas, Braze devolverá una respuesta satisfactoria.

![Prueba de la configuración de una API externa con una carga útil de muestra y una respuesta satisfactoria]({% image_buster /assets/img/lemnisk/test_ext_api.png %})

A continuación, comprueba que tus eventos se envían a Braze correctamente. En el panel de Braze, ve a **Audience** > **Search Users** y, a continuación, introduce uno de los identificadores de tu configuración de API externa (como una dirección de correo electrónico de usuario). Si todo funciona correctamente, aparecerá en la lista el perfil que recibió tu desencadenador de API de prueba.

![Vista del perfil de un usuario y un resumen de su actividad en Braze]({% image_buster /assets/img/lemnisk/braze_cov.png %})

### Paso 3: Desencadenar eventos de usuario en Braze {#step-3-trigger-user-events-in-braze}

1. En Lemnisk, crea un nuevo segmento. Por ejemplo, puedes crear un segmento que envíe información a Braze en cuanto los usuarios envíen un formulario de captación de clientes potenciales.
2. En tu nuevo segmento, ve a **External API** > **Add Engagement**.
3. En **Engagement Creation**, introduce los datos básicos y selecciona la configuración [que creaste anteriormente](#create-a-braze-external-api).
4. En **Configure Parameters**, encontrarás las entradas de los parámetros de Braze que hayas decidido exponer a nivel de interacción. En el siguiente ejemplo, se muestran _Name of the User_, _Product ID_ y _Event Time_.
    ![Creación de una interacción para enviar datos de usuario a Braze]({% image_buster /assets/img/lemnisk/create_an_engagement.png %})
5. Introduce las variables de personalización pertinentes para los parámetros elegidos y, a continuación, selecciona **Save**.
6. Cuando hayas terminado, activa la interacción.