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

Lokalise ofrece dos opciones de integración para Braze:

- **Integración multilingüe (recomendada)**: Utiliza la [API de composición multilingüe]({{site.baseurl}}/api/endpoints/translations/) de Braze para proporcionar una sincronización bidireccional directa entre Lokalise y Braze. Esta integración funciona con variantes de mensajes localizados para Campaigns, Canvas y plantillas de correo electrónico, y es compatible con flujos de trabajo previos y posteriores al lanzamiento para push, correo electrónico e In-App Messages.
- **Integración de contenido conectado (heredada)**: Utiliza el contenido conectado de Braze para insertar contenido traducido en función de la configuración de idioma del usuario.

Este artículo cubre la configuración de ambas integraciones.

## Integración multilingüe (recomendada) {#multi-language-integration-recommended}

La integración multilingüe utiliza la API de composición multilingüe de Braze para proporcionar una forma optimizada y automatizada de gestionar contenido multilingüe de Braze dentro de Lokalise.

### Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Lokalise | Se necesita una cuenta Lokalise para beneficiarse de esta asociación. |
| Proyecto de traducción de Lokalise | Crea un proyecto de Lokalise con el tipo **Marketing and support** y elige **Braze** como **Content integration**. |
| Configuración multilingüe de Braze | La [asistencia en varios idiomas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/) debe estar habilitada en tu espacio de trabajo de Braze. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos para leer y actualizar Campaigns, Canvas y plantillas de correo electrónico. Puedes crear una en el dashboard de Braze desde **Settings** > **API Keys**. |
| Región del servidor de Braze | Tu [región del servidor de Braze]({{site.baseurl}}/api/basics/#endpoints) (por ejemplo, US-01, EU-01). Puedes encontrarla en el dashboard de Braze. |
| Etiquetas de traducción en el contenido de Braze | Los mensajes deben usar [etiquetas de traducción]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) para identificar el contenido traducible. Envuelve cada bloque traducible en etiquetas {% raw %}`{% translation ID %}...{% endtranslation %}`{% endraw %} con un ID único. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

### Configuración y uso {#setup-and-usage}

Para obtener instrucciones detalladas sobre cómo conectar la integración multilingüe de Braze en Lokalise, importar contenido, traducir y exportar traducciones de vuelta a Braze, consulta la [documentación de integración de Braze de Lokalise](https://docs.lokalise.com/en/articles/13654162-braze).

La integración es compatible con:
- Sincronización bidireccional directa entre Lokalise y Braze (sin manejo manual de archivos)
- Variantes de mensajes localizados para Campaigns, Canvas y plantillas de correo electrónico
- Flujos de trabajo de traducción previos y posteriores al lanzamiento

{% alert note %}
Solo el contenido configurado para uso multilingüe en Braze y envuelto en etiquetas de traducción está disponible para importar a Lokalise. Los códigos de idioma deben coincidir exactamente en Braze y Lokalise para que las traducciones se sincronicen correctamente.
{% endalert %}

## Integración de contenido conectado (heredada) {#connected-content-integration-legacy}

La integración heredada utiliza el contenido conectado de Braze para insertar contenido traducido en función de la configuración de idioma del usuario.

### Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Lokalise | Se necesita una cuenta Lokalise para beneficiarse de esta asociación. |
| Proyecto de traducción de Lokalise | Crea un proyecto de Lokalise con el tipo de proyecto **Software Localization**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

### Crear un nuevo proyecto Lokalise {#create-a-new-lokalise-project}

Para crear un nuevo proyecto de traducción, inicia sesión en Lokalise y selecciona **New Project**. A continuación, asigna un nombre a tu proyecto, elige un **Base Language** (el idioma desde el que vas a traducir), añade uno o varios **Target Languages** y elige el tipo de proyecto **Software Localization**. Cuando estés listo, haz clic en **Proceed**.

### Integración {#integration}

En Lokalise, crearás una clave de traducción para cada una de las variables de contenido conectado que definas en Braze. Cuando las traducciones estén listas, puedes generar un archivo JSON por idioma y publicarlo en las URL que servirán tu contenido conectado.

#### Paso 1: Configurar los idiomas de usuario {#step-1-configure-user-languages}

Si aún no lo has hecho, abre el dashboard de Braze y ve a **Users > User Import**. Aquí puedes importar tus usuarios. Cuando prepares un archivo CSV para importarlo, asegúrate de incluir una columna de idioma con los idiomas de los usuarios. Este campo de idioma se utilizará más adelante cuando se muestren las traducciones.

{% alert important %}
Los códigos de idioma utilizados deben coincidir tanto en Braze como en Lokalise.
{% endalert %}

#### Paso 2: Preparar tus traducciones en Lokalise {#step-2-prepare-your-translations-on-lokalise}

A continuación, para preparar tus traducciones en Lokalise, tendrás que crear manualmente las claves de traducción con el mismo nombre que utilizas en las variables de contenido conectado de Braze.

Por ejemplo, vamos a crear una clave de traducción sencilla, `description`:
1. Abre tu proyecto Lokalise, haz clic en **Add Key** e introduce "description" en el campo **Key**.
2. Escribe "Demo description" en el campo **Base Language Value**.
3. Añade "Web" en el desplegable **Platforms**.
4. Cuando estés listo, haz clic en **Save**.

![]({% image_buster /assets/img/lokalise/1_add_key.png %}){: style="max-width:60%"}

Tu clave de traducción debería aparecer en el editor de proyectos:

![]({% image_buster /assets/img/lokalise/2_translation_key_added.png %}){: style="max-width:90%"}

##### Problemas conocidos {#known-issues}

- Tus claves deben estar asignadas a la plataforma **Web**.
- Evita utilizar claves que contengan puntos (`.`) o la cadena `_on`. Por ejemplo, utiliza `this_is_the_key` en lugar de `this.is.the.key`, y utiliza `join_us_instagram` en lugar de `join_us_on_instagram`.

#### Paso 3: Configurar la aplicación Braze en Lokalise {#step-3-configure-the-braze-app-on-lokalise}

Abre tu proyecto Lokalise y haz clic en **Apps**. Aquí, busca e instala la aplicación Braze. Verás la siguiente pantalla:

![Configuración de Braze en Lokalise con el ID del proyecto y la URL de los archivos de traducción.]({% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %})

En la **Translation File URL**, Lokalise publica un archivo JSON que contiene todas las traducciones de tus claves en el proyecto. Obtendrás tantas URL de archivos de traducción como idiomas de destino tengas en tu proyecto. Por eso las URL de los archivos de traducción resultantes tienen dos partes:

1. La primera parte de la ruta URL es común a todos los idiomas.
2. El nombre del archivo JSON al final de la URL se basa en el código de idioma.

La URL del archivo de traducción es la URL que necesitarás al configurar una Campaign de Braze. Puedes actualizar el contenido del archivo JSON haciendo clic en **Refresh**. Ten en cuenta que la URL seguirá siendo la misma, y no tendrás que cambiar tu llamada a contenido conectado en Braze.

##### URL de prueba {#test-url}

Para probar esta URL, cópiala y sustituye {% raw %}`{{${language}}}`{% endraw %} por un código de idioma (por ejemplo, `en`) y abre esta URL en tu navegador. Verás un archivo JSON con tus claves y traducciones:

![]({% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %})

#### Paso 4: Uso de traducciones en la Campaign de Braze {#step-4-use-translations-in-braze-campaign}

##### Insertar llamada de contenido conectado {#insert-connected-content-call}

Cuando estés listo, vuelve a Braze y abre una Campaign existente o crea una nueva. Crearemos una nueva Campaign de correo electrónico con contenido de muestra para este ejemplo. Haz clic en **Edit Email Body**.

Para insertar tus traducciones, tienes que añadir la solicitud de contenido conectado en el HTML, ya sea en la parte superior del documento o justo antes del primer lugar donde se necesite una traducción. Esto puede hacerse insertando el siguiente marcado:

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

Sustituye la URL `https://exports.live.lokalise.cloud/...` por la URL del archivo de traducción obtenida en el paso anterior.

{% raw %}

- `{{${language}}}` significa "inserta el idioma del usuario en esta posición". También puedes codificar directamente el código de tu idioma, por ejemplo, `en.json`.
  - Para asegurarte de que se recupera el archivo JSON traducido adecuado para cada usuario, debes colocar el atributo de perfil `{{${language}}}` u otro atributo personalizado similar que contenga el idioma del usuario al final de la URL de los archivos de traducción (por ejemplo, `/{{${language}}}.json`). Los valores contenidos en estos atributos deben coincidir con el prefijo de cada uno de los archivos JSON traducidos. Esto garantizará que se devuelva el archivo de traducción correcto para cada usuario.
- `:save translations` guardará el contenido JSON en la variable translations.

##### Mostrar traducciones {#display-translations}

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

Braze almacena en caché el contenido traducido, que puede tardar unos minutos en actualizarse. Si estás probando tus Campaigns y necesitas ver los resultados de las traducciones de inmediato, puedes utilizar el parámetro `:cache_max_age` como se explica en este artículo de referencia.