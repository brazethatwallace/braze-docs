---
page_order: 2.2
nav_title: Content Cards
article_title: Content Cards en el SDK de Braze
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Content Cards {#content-cards}

> Obtén información sobre las Content Cards para el SDK de Braze, incluidos los diferentes modelos de datos y las propiedades específicas de las tarjetas disponibles para tu aplicación.

{% multi_lang_include banners/content_card_alert.md %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/content_cards.md %}
{% endsdktab %}

{% sdktab android %}
## Requisitos previos {#prerequisites}

Antes de poder usar las Content Cards de Braze, debes integrar el [SDK de Braze para Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) en tu aplicación. Sin embargo, no se requiere configuración adicional.

## Fragmentos de Google {#google-fragments}

En Android, la fuente de Content Cards se implementa como un [fragmento](https://developer.android.com/guide/components/fragments.html) disponible en el proyecto de interfaz de usuario de Braze para Android. La clase [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) actualiza automáticamente y muestra el contenido de las Content Cards y registra análisis de uso. Las tarjetas que pueden aparecer en las `ContentCards` de un usuario se crean en el panel de Braze.

Para aprender cómo añadir un fragmento a una actividad, consulta la [documentación de fragmentos de Google](https://developer.android.com/guide/fragments#Adding).

## Tipos de tarjetas y propiedades {#card-types-and-properties}

El modelo de datos de Content Cards está disponible en el SDK de Android y ofrece los siguientes tipos únicos de Content Cards. Cada tipo comparte un modelo base, lo que les permite heredar propiedades comunes del modelo base, además de tener sus propias propiedades únicas. Para la documentación de referencia completa, consulta [`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

### Modelo de tarjeta base {#base-card-for-android}

El modelo de [tarjeta base](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) proporciona el comportamiento fundamental para todas las tarjetas.

| Propiedad | Descripción |
|---|---|
| `getId()` | Devuelve el ID de la tarjeta establecido por Braze. |
| `getViewed()` | Devuelve un booleano que indica si la tarjeta ha sido leída o no por el usuario. |
| `getExtras()` | Devuelve un mapa de extras clave-valor para esta tarjeta. |
| `getCreated()` | Devuelve la marca de tiempo unix del momento de creación de la tarjeta en Braze. |
| `isPinned` | Devuelve un booleano que indica si la tarjeta está fijada. |
| `getOpenUriInWebView()` | Devuelve un booleano que indica si las URI de esta tarjeta deben abrirse <br> en el WebView de Braze o no. |
| `getExpiredAt()` | Obtiene la fecha de expiración de la tarjeta. |
| `isRemoved()` | Devuelve un booleano que indica si el usuario final ha descartado esta tarjeta. |
| `isDismissibleByUser()` | Devuelve un booleano que indica si la tarjeta puede ser descartada por el usuario. |
| `isClicked()` | Devuelve un booleano que indica el estado de clic de esta tarjeta. |
| `isDismissed` | Devuelve un booleano que indica si la tarjeta ha sido descartada. Establécelo en `true` para marcar la tarjeta como descartada. Si una tarjeta ya está marcada como descartada, no se puede marcar como descartada de nuevo. |
| `isControl()` | Devuelve un booleano que indica si esta tarjeta es una tarjeta de control y no debe renderizarse. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modelo de tarjeta base #base-card-for-android" }

### Solo imagen {#banner-image-card-for-android}

Las [tarjetas de solo imagen](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) son imágenes a tamaño completo sobre las que se puede hacer clic.

| Propiedad | Descripción |
|---|---|
| `getImageUrl()` | Devuelve la URL de la imagen de la tarjeta. |
| `getUrl()` | Devuelve la URL que se abre después de hacer clic en la tarjeta. Puede ser una URL HTTP(s) o una URL de protocolo. |
| `getDomain()` | Devuelve el texto del enlace para la URL de la propiedad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solo imagen #banner-image-card-for-android" }

### Imagen con subtítulo {#captioned-image-card-for-android}

Las [tarjetas de imagen con subtítulo](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) son imágenes a tamaño completo sobre las que se puede hacer clic, con texto descriptivo acompañante.

| Propiedad | Descripción |
|---|---|
| `getImageUrl()` | Devuelve la URL de la imagen de la tarjeta. |
| `getTitle()` | Devuelve el texto del título de la tarjeta. |
| `getDescription()` | Devuelve el texto del cuerpo de la tarjeta. |
| `getUrl()` | Devuelve la URL que se abre después de hacer clic en la tarjeta. Puede ser una URL HTTP(s) o una URL de protocolo. |
| `getDomain()` | Devuelve el texto del enlace para la URL de la propiedad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Imagen con subtítulo #captioned-image-card-for-android" }

### Clásica {#text-Announcement-card-for-android}

Una tarjeta clásica sin imagen incluida da como resultado una [tarjeta de anuncio de texto](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). Si se incluye una imagen, recibes una [tarjeta de noticias breves](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

| Propiedad | Descripción |
|---|---|
| `getTitle()` | Devuelve el texto del título de la tarjeta. |
| `getDescription()` | Devuelve el texto del cuerpo de la tarjeta. |
| `getUrl()` | Devuelve la URL que se abre después de hacer clic en la tarjeta. Puede ser una URL HTTP(s) o una URL de protocolo. |
| `getDomain()` | Devuelve el texto del enlace para la URL de la propiedad. |
| `getImageUrl()` | Devuelve la URL de la imagen de la tarjeta; aplica solo a la tarjeta clásica de noticias breves. |
| `isDismissed` | Devuelve un booleano que indica si la tarjeta ha sido descartada. Establécelo en `true` para marcar la tarjeta como descartada. Si una tarjeta ya está marcada como descartada, no se puede marcar como descartada de nuevo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Clásica #text-Announcement-card-for-android" }

## Métodos de tarjeta {#card-methods}

Todos los objetos del modelo de datos [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) ofrecen los siguientes métodos de análisis para registrar eventos de usuario en los servidores de Braze.

| Método | Descripción |
|---|---|
| `logImpression()` | Registra manualmente una impresión en Braze para una tarjeta en particular. |
| `logClick()` | Registra manualmente un clic en Braze para una tarjeta en particular. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métodos de tarjeta" }

{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/content_cards.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/content_cards.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/content_cards.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/content_cards.md %}
{% endsdktab %}

{% sdktab tvos %}
## Requisitos previos

Antes de poder usar Content Cards, integra el [SDK Swift de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) en tu aplicación. Luego completa los pasos para configurar tu aplicación tvOS.

{% alert important %}
Implementa tu propia interfaz personalizada, ya que las Content Cards son compatibles a través de una interfaz headless usando el SDK Swift, que no incluye ninguna interfaz ni vistas predeterminadas para tvOS.
{% endalert %}

## Configurar tu aplicación tvOS {#setting-up-your-tvos-app}

### Paso 1: Crear una nueva aplicación iOS {#step-1-create-a-new-ios-app}

En Braze, selecciona **Configuración** > **Configuración de la aplicación** y luego selecciona **Añadir aplicación**. Introduce un nombre para tu aplicación tvOS, selecciona **iOS**&#8212;_no tvOS_&#8212;y luego selecciona **Añadir aplicación**.

![Diálogo de añadir aplicación en Braze con la plataforma iOS seleccionada para registrar una aplicación tvOS.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
Si seleccionas la casilla **tvOS**, no podrás personalizar las Content Cards para tvOS.
{% endalert %}

### Paso 2: Obtener la clave de API de tu aplicación {#step-2-get-your-apps-api-key}

En la configuración de tu aplicación, selecciona tu nueva aplicación tvOS y toma nota de la clave de API de tu aplicación. Usa esta clave para configurar tu aplicación en Xcode.

![Configuración de la aplicación para una aplicación tvOS mostrando la clave de API utilizada para la integración del SDK.]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### Paso 3: Integrar BrazeKit {#step-3-integrate-brazekit}

Usa la clave de API de tu aplicación para integrar el [SDK Swift de Braze](https://github.com/braze-inc/braze-swift-sdk) en tu proyecto tvOS en Xcode. Solo necesitas integrar BrazeKit del SDK Swift de Braze.

### Paso 4: Crear tu interfaz personalizada {#step-4-create-your-custom-ui}

Dado que Braze no proporciona una interfaz predeterminada para Content Cards en tvOS, personalízala tú mismo. Para un recorrido completo, consulta nuestro tutorial paso a paso: [Personalizar Content Cards para tvOS](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/). Para un proyecto de ejemplo, consulta los [ejemplos del SDK Swift de Braze](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui).

{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/content_cards.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/content_cards.md %}
{% endsdktab %}
{% endsdktabs %}