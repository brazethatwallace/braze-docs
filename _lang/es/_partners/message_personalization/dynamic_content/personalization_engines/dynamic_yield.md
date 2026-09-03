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

## Acerca de la integración {#about-the-integration}

La asociación entre Braze y Dynamic Yield te permite utilizar el motor de recomendaciones y segmentación de Dynamic Yield para crear bloques de experiencia que pueden integrarse en los mensajes de Braze. Los bloques de experiencia pueden estar compuestos por:
{% multi_lang_include partners/message_personalization/dynamic_yield_experience_blocks.md %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Dynamic Yield | Se requiere una cuenta de [Dynamic Yield](https://adm.dynamicyield.com/users/sign_in#/r/dashboard) para aprovechar esta integración. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crear un bloque de experiencia {#step-1-create-an-experience-block}

Para crear un bloque de experiencia en Dynamic Yield, navega a **Email > Experience Emails > Create New**.

A continuación, selecciona **Create Experience Block** para diseñar un bloque de contenido dinámico o recomendaciones para incrustar dentro de una plantilla de correo electrónico de Braze.<br>![Página de Experience Emails de Dynamic Yield con Create Experience Block seleccionado.]({% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %})

### Paso 2: Redactar tu mensaje {#step-2-draft-your-messaging}

La siguiente imagen muestra un correo electrónico desde cero en el creador.<br>![Creador de correo electrónico de Dynamic Yield con un diseño de correo electrónico de experiencia en borrador.]({% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %})

1. Introduce un nombre de Campaign, nota y etiquetas para la Campaign en el área del encabezado.<br><br>
2. Inserta un bloque de experiencia. Estos bloques incluyen:
  - [Recomendaciones](#configure-a-recommendations-block): Un widget que ofrece a los usuarios recomendaciones totalmente personalizadas.
  - [Contenido dinámico](#configure-a-dynamic-content-block): Dirige diferentes promociones y mensajes a diferentes audiencias.<br><br>
3. Actualiza la configuración:
  - Usa los parámetros de URL para rastrear clics dentro de tu software de análisis (opcional). Añade parámetros a las visualizaciones predeterminadas según sea necesario.
  - Selecciona una ventana de atributos, ya sea de siete días (predeterminado) o de un día.<br><br>
4. Guarda y sal. Puedes volver a editar todos los elementos de tu correo electrónico en cualquier momento antes de que se genere el código. Después de que se genere el código, puedes editar cualquier cosa que [no afecte al código](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH).

### Configurar un bloque de recomendaciones {#configure-a-recommendations-block}

El bloque de recomendaciones te permite establecer algoritmos y filtrado para obtener contenido personalizado de los usuarios que se propaga cuando se abre el correo electrónico.

1. Arrastra un bloque de recomendaciones desde el panel de edición al cuerpo de tu correo electrónico.<br><br>
2. Selecciona el algoritmo deseado (popularidad, afinidad del usuario, similitud y más). Dependiendo del algoritmo seleccionado, se muestran opciones adicionales:
  - Si tu recomendación se basa en popularidad, puedes mezclar los resultados para evitar servir la misma recomendación en diferentes correos electrónicos que el lector abra.
  - Otros algoritmos, como similitud, dependen del contexto para servir recomendaciones, lo que requiere que selecciones elementos a incluir. Estos elementos se pueden añadir en el creador o [añadir una etiqueta de combinación al código de incrustación](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced) para hacerlo dinámico, por ejemplo, para añadir artículos similares en correos electrónicos de confirmación de envío. <br><br>
3. Puedes excluir productos que el usuario ya haya comprado para evitar recomendar estos productos.<br><br>
4. Puedes añadir una [regla de filtro personalizada](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD) para fijar productos específicos a espacios, o incluir y excluir productos por propiedades de producto. Por ejemplo, no mostrar productos que cuesten menos de $5 o solo productos de la categoría de pantalones cortos.<br><br>
5. Por último, configura el diseño del bloque de recomendaciones. Para hacerlo, selecciona una plantilla de elemento, establece el número de elementos a mostrar y en cuántas filas.

### Configurar un bloque de contenido dinámico {#configure-a-dynamic-content-block}
Usa el contenido dinámico para dirigir diferentes promociones y mensajes a diferentes usuarios. La segmentación puede basarse en afinidad o audiencia. Dynamic Yield determina qué experiencia personalizada servir cuando se abre el correo electrónico.

1. Arrastra un bloque de contenido dinámico desde el panel de edición al cuerpo de tu correo electrónico.<br><br>
2. Selecciona una plantilla para la primera variación. Ahora puedes definir variables de diseño y contenido. Guarda la variación cuando esté completa. <br>![Editor de plantillas de variación de contenido dinámico de Dynamic Yield.]({% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %})<br><br>
3. Establece la audiencia en el panel de contenido dinámico.<br>![Configuración de segmentación de audiencia de Dynamic Yield para una variación de contenido dinámico.]({% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %})<br><br>
4. Añade otra variación para dirigirte a otra audiencia específica o a todos los usuarios. Repite según sea necesario.<br><br>
5. Establece las prioridades para tus variaciones usando las flechas arriba y abajo. <br><br>
6. Las prioridades determinan qué variación se sirve cuando un usuario es elegible para más de una experiencia.

### Paso 3: Integrar tu correo electrónico con Braze {#step-3-integrate-your-email-with-braze}

Esta integración te permite añadir widgets de recomendaciones personalizadas y contenido dinámico impulsado por Dynamic Yield en tus Campaigns de correo electrónico de Braze. Incrustar estas Campaigns en Campaigns de Braze se hace con un simple código de incrustación que pegas en el editor de correo electrónico de Braze.

1. Haz clic en el icono de integración ESP en la página de lista de Experience Email.<br><br>
2. Introduce el token relevante de Braze que inserta el CUID y el ID de correo electrónico del usuario.<br>![Modal de integración ESP de Dynamic Yield con campos de token de usuario de Braze.]({% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %})

Cuando estés satisfecho con tu correo electrónico, el siguiente paso es generar el código para incrustar en Braze.
1. En **Experience Emails**, haz clic en **Generate Code**.<br><br>
2. A continuación, haz clic en **Copy to Clipboard**.<br>![Panel de código de incrustación generado de Dynamic Yield con la acción Copiar al portapapeles.]({% image_buster /assets/img/dynamic_yield/dynamic_yield.png %})<br><br>
3. Pega el código en tu Campaign de correo electrónico de Braze y luego continúa diseñando, probando y publicando tu Campaign de correo electrónico.