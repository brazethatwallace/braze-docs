---
nav_title: Stylitics
article_title: Stylitics
description: "Este artículo de referencia describe la asociación entre Braze y Stylitics, una plataforma SaaS basada en la nube que te permite mejorar tus campañas de correo electrónico existentes con contenidos agrupados atractivos y relevantes, creando una experiencia del cliente personalizada."
alias: /partners/stylitics/
page_type: partner
search_tag: Partner

---

# Stylitics

> [Stylitics](https://stylitics.com/) es una plataforma SaaS basada en la nube que permite a los minoristas automatizar y distribuir contenidos visuales a gran escala. Los paquetes de Stylitics inspiran contextualizando los productos, aumentando la confianza en la compra e incrementando la participación, lo que en última instancia conduce a un mayor valor medio de los pedidos y a mejores tasas de conversión.

_Esta integración está mantenida por Stylitics._

## Sobre la integración {#about-the-integration}

Tu integración de Braze y Stylitics te permite mejorar tus campañas de correo electrónico existentes con contenidos agrupados atractivos y relevantes, creando una experiencia del cliente personalizada.

![Ejemplo de contenido agrupado de Stylitics integrado en una experiencia de correo electrónico de Braze.]({% image_buster /assets/img/stylitics.png %}){: style="max-width:60%;"}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Stylitics | Es necesario disponer de una cuenta de [Stylitics](https://stylitics.com/) para beneficiarse de esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Ejemplos {#use-cases}

A continuación se enumeran algunos ejemplos comunes de programas de correo electrónico desencadenados:
- Correos electrónicos de carritos abandonados
- Correos electrónicos de navegación abandonada
- Correos electrónicos de confirmación de envío
- Correos electrónicos posteriores a la compra

## Integración {#integration}

Stylitics proporciona los datos del paquete para esta integración. Tu proveedor de servicios de correo electrónico puede crear o actualizar la plantilla de correo electrónico para incluir los paquetes de Stylitics. Stylitics no puede alterar el diseño ni la maquetación de los correos electrónicos.

1. Integra el paquete en el correo electrónico. El ESP determina la posición y la personalización.
2. El ESP actualiza el código de activación del correo electrónico para incluir el contenido de Stylitics.
3. El ESP probará, previsualizará y lanzará las actualizaciones de la serie desencadenada.

Stylitics solo proporcionará los datos de los paquetes de artículos. Entre tú y tu ESP, dispondrás de los datos de usuario y podrás conectar los datos del paquete de Stylitics para enviarlos a los usuarios.

## Intercambio de datos {#data-exchange}

Los tres enfoques siguientes te permiten incluir paquetes de Stylitics en tus correos electrónicos desencadenados.

### 1. Enfoque API (recomendado) {#1-api-approach-recommended}

Tú o tu ESP pueden realizar una llamada a la API por artículo para rellenar los datos del paquete en tu correo electrónico. Stylitics te recomienda que utilices su API para hacer llamadas, ya que está lista para usarse de inmediato.

{% alert note %}
Si realizas una prueba A/B ejecutada por Stylitics, los parámetros `styliticsCID` y `styliticsoverride` deben añadirse a las URL PDP de los elementos de Stylitics en los que el usuario hace clic en el correo electrónico.
<br><br>
Por ejemplo, {% raw %}`&styliticsoverride=001?styliticsCID=email[clientname]`{% endraw %}
{% endalert %}

### 2. Enfoque de archivo plano {#2-flat-file-approach}

Tú o tu ESP pueden hacer referencia a los datos del paquete de un artículo en un archivo plano para rellenar los datos del paquete en tu correo electrónico. Stylitics puede aplanar los datos de los paquetes en formato CSV, TXT o XML y enviártelos diariamente. También pueden ayudar a ajustar el formato del archivo según las necesidades de tu ESP. Ten en cuenta que se tarda entre 2 y 3 semanas en crear este archivo.

#### Requisitos: {#requirements}
- **Ubicación**: Stylitics puede depositar el archivo en el SFTP de Stylitics para que lo recojas diariamente, o puedes enviarles tus credenciales SFTP para que depositen el archivo.
- **Hora**: Stylitics depositará el archivo diariamente por la mañana. Indícales si necesitas el archivo para una hora concreta.
- **Clave de archivo**: Tú y Stylitics deben ponerse de acuerdo sobre la cadena de datos del artículo que se utilizará como clave en el archivo para que tu ESP pueda hacer referencia a los datos. Se suelen utilizar SKU, `item_group_id` o `item_number`.

### 3. Enfoque de extracción de datos del sitio web {#3-website-data-extraction-approach}

Los proveedores pueden rastrear el front end de tu sitio en busca de contenido de Stylitics e insertar los datos del paquete en los correos electrónicos. No se requiere ningún trabajo adicional por parte de Stylitics.

## Mejores prácticas para plantillas de correo electrónico {#email-template-best-practices}

Tú y tu ESP crearán una plantilla de correo electrónico HTML para insertar los datos y paquetes de Stylitics. Aquí tienes algunas buenas prácticas y recomendaciones.
- Muestra de 2 a 4 paquetes en el correo electrónico para el artículo más caro o el primer artículo a precio completo que el usuario haya comprado o con el que haya interactuado
- Llama a varios `item_numbers` y muestra las primeras respuestas de paquetes
- Ten una opción alternativa si no hay paquetes disponibles para el artículo
	- Oculta la sección donde se encuentran los paquetes de Stylitics
	- Muestra los paquetes del siguiente artículo que el usuario haya visto
- Muestra imágenes de paquetes y una lista de títulos de productos e imágenes en miniatura para garantizar que el usuario tenga un click-through claro

{% alert note %}
El widget JavaScript de Stylitics no puede insertarse en los correos electrónicos, ya que estos no admiten JavaScript.
{% endalert %}

## Análisis {#analytics}

Stylitics proporciona los datos del paquete para este tipo de programa de correo electrónico. Por lo tanto, pedimos un intercambio de datos abierto entre tú, tu ESP y Stylitics. Si es posible, esperamos recibir de ti las siguientes métricas para comprender el impacto y mejorar el programa:
- Correos electrónicos enviados
- Correos electrónicos abiertos
- Vistas e interacciones
- Tasa de clics
- Añadir al carrito
- Compras

## Próximos pasos {#next-steps}

Ponte en contacto con tu director de cuentas de Stylitics para coordinar los próximos pasos y plazos del programa de correo electrónico. Algunos de los próximos pasos incluyen:
- Decidir qué correos electrónicos quieres utilizar
- Conectar Stylitics con tu ESP para discutir el intercambio de datos y decidir entre la opción API o la opción de archivo plano
- Crear maquetas con tu ESP
- Alinearse en los análisis
- Alinearse en el calendario de lanzamiento