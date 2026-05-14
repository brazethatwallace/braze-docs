---
nav_title: Lokalise
article_title: Lokalise
description: "Este artículo de referencia describe la asociación entre Braze y Lokalise, un servicio de gestión de traducciones para equipos ágiles."
alias: /partners/lokalise/
page_type: partner
search_tag: Partner

---

# Lokalise

> [Lokalise](https://lokalise.com) es un servicio de administración de traducciones para equipos ágiles.

_Esta integración está mantenida por Lokalise._

## Sobre la integración {#about-the-integration}

La integración de Braze y Lokalise utiliza el Contenido conectado para permitirte insertar fácilmente contenido traducido en tus Campaigns de Braze en función de la configuración de idioma del usuario.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Lokalise | Se necesita una cuenta Lokalise para beneficiarse de esta asociación. |
| Proyecto de traducción de Lokalise | Debe crearse un proyecto de traducción de Lokalise antes de configurar esta integración. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Crear un nuevo proyecto Lokalise {#create-a-new-lokalise-project}

Para crear un nuevo proyecto de traducción, inicia sesión en Lokalise y selecciona **New Project**. A continuación, asigna un nombre a tu proyecto, elige un **Base Language** (el idioma desde el que vas a traducir), añade uno o varios **Target Languages** y elige el tipo de proyecto **Software Localization**. Cuando estés listo, haz clic en **Proceed**.

## Integración {#integration}

En Lokalise, crearás una clave de traducción para cada una de las variables de Contenido conectado que definas en Braze. Cuando las traducciones estén listas, puedes generar un archivo JSON por idioma y publicarlo en las URL que servirán tu Contenido conectado.

### Paso 1: Configurar los idiomas de usuario {#step-1-configuring-user-languages}

Si aún no lo has hecho, abre el dashboard de Braze y ve a **Users > User Import**. Aquí puedes importar tus usuarios. Cuando prepares un archivo CSV para importarlo, asegúrate de incluir una columna de idioma con los idiomas de los usuarios. Este campo de idioma se utilizará más adelante cuando se muestren las traducciones.

{% alert important %}
Los códigos de idioma utilizados deben coincidir tanto en Braze como en Lokalise.
{% endalert %}
### Paso 2: Preparar tus traducciones en Lokalise {#step-2-preparing-your-translations-on-lokalise}

A continuación, para preparar tus traducciones en Lokalise, tendrás que crear manualmente las claves de traducción con el mismo nombre que utilizas en las variables de Contenido conectado de Braze.

Por ejemplo, vamos a crear una clave de traducción sencilla, `description`:
1. Abre tu proyecto Lokalise, haz clic en **Add Key** e introduce "description" en el campo **Key**.
2. Escribe "Demo description" en el campo **Base Language Value**.
3. Añade "Web" en el desplegable **Platforms**.
4. Cuando estés listo, haz clic en **Save**.

![]({% image_buster /assets/img/lokalise/1_add_key.png %}){: style="max-width:60%"}

Tu clave de traducción debería aparecer en el editor de proyectos:

![]({% image_buster /assets/img/lokalise/2_translation_key_added.png %}){: style="max-width:90%"}

#### Problemas conocidos {#known-issues}

- Tus claves deben estar asignadas a la plataforma **Web**.
- Evita utilizar claves que contengan puntos (`.`) o la cadena `_on`. Por ejemplo, utiliza `this_is_the_key` en lugar de `this.is.the.key`, y utiliza `join_us_instagram` en lugar de `join_us_on_instagram`.

### Paso 3: Configurar la aplicación Braze en Lokalise {#step-3-configuring-the-braze-app-on-lokalise}

Abre tu proyecto Lokalise y haz clic en **Apps**. Aquí, busca e instala la aplicación Braze. Verás la siguiente pantalla:

![Configuración de Braze en Lokalise con el ID del proyecto y la URL de los archivos de traducción.]({% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %})

En la **Translation File URL**, Lokalise publica un archivo JSON que contiene todas las traducciones de tus claves en el proyecto. Obtendrás tantas URL de archivos de traducción como idiomas de destino tengas en tu proyecto. Por eso las URL de los archivos de traducción resultantes tienen dos partes:

1. La primera parte de la ruta URL es común a todos los idiomas.
2. El nombre del archivo JSON al final de la URL se basa en el código de idioma.

La URL del archivo de traducción es la URL que necesitarás al configurar una Campaign de Braze. Puedes actualizar el contenido del archivo JSON haciendo clic en **Refresh**. Ten en cuenta que la URL seguirá siendo la misma, y no tendrás que cambiar tu llamada a Contenido conectado en Braze.

### URL de prueba {#test-url}

Para probar esta URL, cópiala y sustituye {% raw %}`{{${language}}}`{% endraw %} por un código de idioma (por ejemplo, `en`) y abre esta URL en tu navegador. Verás un archivo JSON con tus claves y traducciones:

![]({% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %})

### Paso 4: Uso de traducciones en la Campaign de Braze {#step-4-using-translations-in-braze-campaign}

#### Insertar llamada de Contenido conectado {#insert-connected-content-call}

Cuando estés listo, vuelve a Braze y abre una Campaign existente o crea una nueva. Crearemos una nueva Campaign de correo electrónico con contenido de muestra para este ejemplo. Haz clic en **Edit Email Body**.

Para insertar tus traducciones, tienes que añadir la solicitud de Contenido conectado en el HTML, ya sea en la parte superior del documento o justo antes del primer lugar donde se necesite una traducción. Esto puede hacerse insertando el siguiente marcado:

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

Sustituye la URL `https://exports.live.lokalise.cloud/...` por la URL del archivo de traducción obtenida en el paso anterior.

{% raw %}

- `{{${language}}}` significa "inserta el idioma del usuario en esta posición". También puedes codificar directamente el código de tu idioma, por ejemplo, `en.json`.
  - Para asegurarte de que se recupera el archivo JSON traducido adecuado para cada usuario, debes colocar el atributo de perfil `{{${language}}}` u otro atributo personalizado similar que contenga el idioma del usuario al final de la URL de los archivos de traducción (por ejemplo, `/{{${language}}}.json`). Los valores contenidos en estos atributos deben coincidir con el prefijo de cada uno de los archivos JSON traducidos. Esto garantizará que se devuelva el archivo de traducción correcto para cada usuario.
- `:save translations` guardará el contenido JSON en la variable translations.

#### Mostrar traducciones {#display-translations}

Ahora utiliza la variable translations para mostrar las traducciones deseadas por sus claves.

Por ejemplo, para mostrar la clave `description`, utiliza `{{ translations.description }}`.

{% endraw %}
![]({% image_buster /assets/img/lokalise/6_integration_usage_sample.png %})

Por último, guarda la plantilla de correo electrónico y visualízala. Deberías ver que se muestra tu traducción.

## Preguntas más frecuentes {#frequently-asked-questions}

### ¿Qué ocurre si borro accidentalmente una clave de Lokalise? {#what-happens-if-i-accidentally-delete-a-key-from-lokalise}

La cadena correspondiente en Braze ya no tendrá traducción.

### Si tengo una localización `en` pero la sustituyo por `en-US` en Lokalise, ¿Braze la leerá como `en-US`? {#if-i-have-an-en-locale-but-override-it-with-en-us-on-lokalise-will-braze-read-it-as-en-us}

No, los códigos ISO de localización deben coincidir en Braze y Lokalise.

### ¿Podemos utilizar el indicador `:rerender` al conectar contenidos de Lokalise? {#can-we-use-the-rerender-flag-when-connecting-lokalise-content}

Sí, claro. Puedes consultar la documentación de Braze para saber cómo añadir este indicador.

### Después de actualizar el archivo de traducción en Lokalise, ¿por qué no puedo ver ningún cambio en el contenido traducido en Braze? {#after-refreshing-the-translation-file-on-lokalise-why-cant-i-see-any-changes-in-the-translated-content-on-braze}

Braze almacena en caché el contenido traducido, que puede tardar unos minutos en actualizarse. Si estás probando tus Campaigns y necesitas ver los resultados de las traducciones inmediatamente, puedes utilizar el parámetro `:cache_max_age` como se explica en este artículo de referencia.