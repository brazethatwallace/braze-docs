---
nav_title: B.Layer
article_title: B.Layer
description: "Este artículo de referencia describe la asociación entre Braze y B.Layer, un creador de mensajes dentro de la aplicación, que puedes utilizar para crear mensajes dentro de la aplicación diseñados a medida de forma sencilla, rápida y sin codificación."
alias: /partners/blayer-inapps/
page_type: partner
search_tag: Partner

---

# B.Layer

> [B.Layer](https://blayer.phiture.com) es el creador de mensajes dentro de la aplicación de Phiture que ayuda a los equipos de CRM or administración de las relaciones con el cliente de las aplicaciones móviles a crear mensajes dentro de la aplicación diseñados a medida de forma sencilla, rápida y sin codificación.

_Esta integración está mantenida por B.Layer._

## Sobre la integración {#about-the-integration}

La integración de Braze y B.Layer te permite utilizar el creador de mensajes dentro de la aplicación B.Layer para ayudarte a crear mensajes dentro de la aplicación con tu marca, que pueden exportarse como archivo zip o HTML en línea a Braze. Esta integración no requiere recursos adicionales de desarrollador, lo que te ahorra tiempo y presupuesto.

![Interfaz del creador B.Layer con vista previa de un mensaje dentro de la aplicación con marca.]({% image_buster /assets/img/blayer/blayer2.png %})

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta B.Layer | Se necesita una cuenta [B.Layer](https://blayer.phiture.com) para beneficiarse de esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Ejemplos {#use-cases}

Con B.Layer hay un sinfín de oportunidades para crear y experimentar, incluyendo deslizadores de recomendación de productos, incorporación multipantalla o cuestionarios, NPS, captura de correo electrónico, ofertas especiales y mucho más.

Trabajan con marcas como Lifesum, Blinkist, OnX Hunt y muchas más para ayudarles a mejorar su experiencia de usuario sin recursos adicionales. También estamos entre los finalistas de los premios APS 2022 en la categoría de innovación en aplicaciones.

## Integración {#integration}

### Paso 1: Crea tu mensaje dentro de la aplicación {#step-1-create-your-in-app-message}

#### Definir los colores y tipos de letra de la marca {#set-brand-colors-and-fonts}

En B.Layer, en el menú hamburguesa de la parte superior de la página, haz clic en **Brand assets > add your brand assets**. Aquí puedes asignar el color y las fuentes de tu marca.
Ya está todo listo. Ahora puedes empezar a diseñar tu mensaje dentro de la aplicación.

![Pantalla de activos de marca de B.Layer para configurar colores y fuentes.]({% image_buster /assets/img/blayer/blayer4.png %})

#### Diseña tu mensaje dentro de la aplicación {#design-your-in-app-message}

Para diseñar tu mensaje dentro de la aplicación, selecciona un único mensaje dentro de la aplicación. A continuación, dale estilo a tu mensaje y añade los componentes que necesites. Cada componente puede ajustarse.

![Editor de mensajes de B.Layer con componentes y controles de estilo.]({% image_buster /assets/img/blayer/blayer5.png %})

### Descarga tu mensaje dentro de la aplicación {#download-your-in-app-message}

Una vez que hayas terminado, descarga tu mensaje. Tu mensaje puede descargarse en formato ZIP o HTML en línea.

### Paso 2: Añadir código personalizado de B.Layer {#step-2-add-blayer-custom-code}

En Braze, crea un mensaje dentro de la aplicación de código personalizado. Si tienes un archivo ZIP, arrástralo y suéltalo en la casilla de carga de esta sección. Si tienes un archivo HTML en línea, pega el HTML en línea en la sección HTML.

![Editor de mensajes dentro de la aplicación de código personalizado de Braze con contenido exportado de B.Layer.]({% image_buster /assets/img/blayer/blayer6.png %})

## Seguimiento de botones {#button-tracking}

Con B.Layer, puedes registrar las interacciones con botones o la introducción de texto como un atributo de Braze. Eso se puede hacer dentro del editor. Un ejemplo popular es un cuestionario NPS.

B.Layer utiliza el seguimiento de botones de Braze añadido a los enlaces que introduces (por ejemplo, `?button=0`). De esta forma, puedes ver los clics en los botones en la parte de análisis de tu campaña.