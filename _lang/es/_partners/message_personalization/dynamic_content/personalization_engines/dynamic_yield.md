---
nav_title: Dynamic Yield
article_title: Dynamic Yield
description: "Este artículo de referencia describe la asociación entre Braze y Dynamic Yield. Esta asociación te permite utilizar el motor de recomendación y segmentación de Dynamic Yield para crear bloques de experiencia que pueden incrustarse en los mensajes de Braze."
alias: /partners/dynamic_yield/
page_type: partner
search_tag: Partner

---

# Dynamic Yield

> [Dynamic Yield](https://www.dynamicyield.com/), una empresa de Mastercard, ayuda a las empresas de todos los sectores a entregar experiencias del cliente digitales personalizadas, optimizadas y sincronizadas. Con el [Experience OS](http://www.dynamicyield.com/experience-os) de Dynamic Yield, los especialistas en marketing, administradores de productos, desarrolladores y equipos digitales pueden adaptar algorítmicamente los contenidos, los productos y las ofertas a cada cliente para acelerar los ingresos y la fidelización de los clientes.

_Esta integración es mantenida por Dynamic Yield._

## Sobre la integración {#about-the-integration}

La asociación entre Braze y Dynamic Yield te permite utilizar el motor de recomendación y segmentación de Dynamic Yield para crear bloques de experiencia que pueden incrustarse en los mensajes de Braze. Los bloques de experiencia pueden ser de:
- **Bloques de recomendaciones**: Establecen algoritmos y filtros para obtener contenido personalizado de los usuarios que se propaga cuando se abre el correo electrónico.
- **Bloques de contenido dinámico**: Dirigen diferentes promociones y mensajes a diferentes usuarios. La orientación puede basarse en la afinidad o en la audiencia. Dynamic Yield determina qué experiencia personalizada servir cuando se abre el correo electrónico.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Dynamic Yield | Se necesita una cuenta de [Dynamic Yield](https://adm.dynamicyield.com/users/sign_in#/r/dashboard) para beneficiarse de esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crea un bloque de experiencia {#step-1-create-an-experience-block}

Para crear un bloque de experiencia en Dynamic Yield, ve a **Email > Experience Emails > Create New**.

A continuación, selecciona **Create Experience Block** para diseñar un bloque de contenido dinámico o de recomendaciones para incrustar dentro de una plantilla de correo electrónico de Braze.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %})

### Paso 2: Redacta tu mensaje {#step-2-draft-your-messaging}

La siguiente imagen muestra un correo electrónico desde cero en el constructor.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %})

1. Introduce un nombre de campaña, una nota y etiquetas para la campaña en el área de encabezamiento.<br><br>
2. Inserta un bloque de experiencia. Estos bloques incluyen:
  - [Recomendaciones](#configure-a-recommendations-block): Un widget que ofrece a los usuarios recomendaciones totalmente personalizadas.
  - [Contenido dinámico](#configure-a-dynamic-content-block): Dirige diferentes promociones y mensajes a diferentes audiencias.<br><br>
3. Actualiza la configuración:
  - Utiliza los parámetros de la URL para hacer un seguimiento de los clics en tu software de análisis (opcional). Añade parámetros a las visualizaciones predeterminadas según sea necesario.
  - Selecciona una ventana de atributo, siete días (predeterminado) o un día.<br><br>
4. Guarda y sal. Puedes volver a editar todos los elementos de tu correo electrónico en cualquier momento antes de que se genere el código. Una vez generado el código, puedes editar cualquier cosa que [no afecte al código](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH).

### Configurar un bloque de recomendaciones {#configure-a-recommendations-block}

El bloque de recomendaciones te permite establecer algoritmos y filtros para obtener contenido personalizado de los usuarios que se propaga cuando se abre el correo electrónico.

1. Arrastra un bloque de recomendaciones del panel de edición al cuerpo de tu correo electrónico.<br><br>
2. Selecciona el algoritmo que desees (popularidad, afinidad con el usuario, similitud, etc.). Según el algoritmo seleccionado, se muestran opciones adicionales:
  - Si tu recomendación se basa en la popularidad, puedes barajar los resultados para evitar servir la misma recomendación desde diferentes correos electrónicos que el espectador abra.
  - Otros algoritmos, como el de similitud, se basan en el contexto para ofrecer recomendaciones que requieren que selecciones los elementos a incluir. Estos elementos pueden añadirse en el constructor o [añadir una etiqueta merge al código incrustado](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced) para hacerlo dinámico, por ejemplo, para añadir elementos similares en los correos electrónicos de confirmación de envío. <br><br>
3. Puedes excluir productos que el usuario ya haya comprado para evitar recomendarle estos productos.<br><br>
4. Puedes añadir una [regla de filtro personalizada](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD) para fijar productos concretos a las ranuras, o incluir y excluir productos por sus propiedades. Por ejemplo, no muestres productos que cuesten menos de 5 $ o solo productos de la categoría de pantalones cortos.<br><br>
5. Por último, configura el diseño del bloque de recomendación. Para ello, selecciona una plantilla de elementos, establece el número de elementos que quieres mostrar y en cuántas filas.

### Configurar un bloque de contenido dinámico {#configure-a-dynamic-content-block}
Utiliza el contenido dinámico para dirigir diferentes promociones y mensajes a diferentes usuarios. La orientación puede basarse en la afinidad o en la audiencia. Dynamic Yield determina qué experiencia personalizada servir cuando se abre el correo electrónico.

1. Arrastra un bloque de contenido dinámico desde el panel de edición al cuerpo de tu correo electrónico.<br><br>
2. Selecciona una plantilla para la primera variación. Ahora puedes definir variables de diseño y contenido. Guarda la variación cuando la hayas completado. <br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %})<br><br>
3. Configura la audiencia en el panel de contenido dinámico.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %})<br><br>
4. Añade otra variación para dirigirte a otra audiencia específica o a todos los usuarios. Repítelo según sea necesario.<br><br>
5. Establece las prioridades de tus variaciones utilizando las flechas arriba y abajo. <br><br>
6. Las prioridades determinan qué variación se sirve cuando un usuario es elegible para más de una experiencia.

### Paso 3: Integra tu correo electrónico con Braze {#step-3-integrate-your-email-with-braze}

Esta integración te permite añadir widgets de recomendación personalizados y contenido dinámico impulsado por Dynamic Yield en tus campañas de correo electrónico de Braze. Incrustar estas campañas en campañas de Braze se hace con un simple código de incrustación que pegas en el editor de correo electrónico de Braze.

1. Haz clic en el icono de integración ESP en la página de la lista de correos electrónicos de experiencia.<br><br>
2. Introduce el token correspondiente de Braze que inserta el CUID y el ID de correo electrónico del usuario.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %})

Cuando estés satisfecho con tu correo electrónico, el siguiente paso es generar el código para incrustarlo en Braze.
1. En **Experience Emails**, haz clic en **Generate Code**.<br><br>
2. A continuación, haz clic en **Copy to Clipboard**.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield.png %})<br><br>
3. Pega el código en tu campaña de correo electrónico de Braze, y luego continúa diseñando, probando y publicando tu campaña de correo electrónico.