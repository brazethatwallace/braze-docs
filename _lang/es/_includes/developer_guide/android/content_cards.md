## Requisitos previos {#prerequisites}

Antes de poder usar las Content Cards de Braze, deberás integrar el [SDK de Braze para Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) en tu aplicación. Sin embargo, no es necesario realizar ninguna configuración adicional.

## Fragmentos de Google {#google-fragments}

En Android, la fuente de Content Cards se implementa como un [fragmento](https://developer.android.com/guide/components/fragments.html) disponible en el proyecto Braze Android UI. La clase [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) actualizará y mostrará automáticamente el contenido de las Content Cards y registrará los análisis de uso. Las tarjetas que pueden aparecer en el `ContentCards` de un usuario se crean en el panel de Braze.

Para aprender a añadir un fragmento a una actividad, consulta [la documentación sobre fragmentos de Google](https://developer.android.com/guide/fragments#Adding).

## Tipos y propiedades de las tarjetas {#card-types-and-properties}

El modelo de datos de Content Cards está disponible en el SDK de Android y ofrece los siguientes tipos de Content Cards únicos. Cada tipo comparte un modelo base, lo que les permite heredar propiedades comunes del modelo base, además de tener sus propias propiedades únicas. Para obtener la documentación de referencia completa, consulta [`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

### Modelo de tarjeta base {#base-card-for-android}

El modelo de [tarjeta base](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) proporciona un comportamiento básico para todas las tarjetas.

| Propiedad | Descripción |
|---|---|
| `getId()` | Devuelve el ID de la tarjeta configurado por Braze. |
| `getViewed()` | Devuelve un booleano que refleja si la tarjeta ha sido leída o no por el usuario. |
| `getExtras()` | Devuelve un mapa de extras clave-valor para esta tarjeta. |
| `getCreated()` | Devuelve la marca de tiempo unix de la hora de creación de la tarjeta desde Braze. |
| `isPinned` | Devuelve un booleano que refleja si la tarjeta está anclada. |
| `getOpenUriInWebView()` | Devuelve un booleano que refleja si las URI de esta tarjeta deben abrirse <br> en el Braze WebView o no. |
| `getExpiredAt()` | Obtiene la fecha de caducidad de la tarjeta. |
| `isRemoved()` | Devuelve un booleano que refleja si el usuario final ha descartado esta tarjeta. |
| `isDismissibleByUser()` | Devuelve un booleano que indica si el usuario puede descartar la tarjeta. |
| `isClicked()` | Devuelve un booleano que refleja el estado de clic de esta tarjeta. |
| `isDismissed` | Devuelve un booleano que indica si la tarjeta ha sido descartada. Establécelo en `true` para marcar la tarjeta como descartada. Si una tarjeta ya está marcada como descartada, no se puede volver a marcar como descartada. |
| `isControl()` | Devuelve un booleano que indica si esta tarjeta es una tarjeta de control y no debe renderizarse. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Base card model #base-card-for-android" }

### Solo imagen {#banner-image-card-for-android}

[Las tarjetas de solo imagen](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) son imágenes a tamaño completo en las que se puede hacer clic.

| Propiedad | Descripción |
|---|---|
| `getImageUrl()` | Devuelve la URL de la imagen de la tarjeta. |
| `getUrl()` | Devuelve la URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP(s) o una URL de protocolo. |
| `getDomain()` | Devuelve el texto del enlace para la URL de la propiedad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image only #banner-image-card-for-android" }

### Imagen con pie de foto {#captioned-image-card-for-android}

[Las tarjetas de imagen con pie de foto](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) son imágenes a tamaño completo en las que se puede hacer clic y que van acompañadas de un texto descriptivo.

| Propiedad | Descripción |
|---|---|
| `getImageUrl()` | Devuelve la URL de la imagen de la tarjeta. |
| `getTitle()` | Devuelve el texto del título de la tarjeta. |
| `getDescription()` | Devuelve el texto del cuerpo de la tarjeta. |
| `getUrl()` | Devuelve la URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP(s) o una URL de protocolo. |
| `getDomain()` | Devuelve el texto del enlace de la URL de la propiedad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Captioned image #captioned-image-card-for-android" }

### Clásica {#text-Announcement-card-for-android}

Una tarjeta clásica sin imagen incluida dará como resultado una [tarjeta de anuncio de texto](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). Si se incluye una imagen, recibirás una [tarjeta de noticias breve](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

| Propiedad | Descripción |
|---|---|
| `getTitle()` | Devuelve el texto del título de la tarjeta. |
| `getDescription()` | Devuelve el texto del cuerpo de la tarjeta. |
| `getUrl()` | Devuelve la URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP(s) o una URL de protocolo. |
| `getDomain()` | Devuelve el texto del enlace de la URL de la propiedad. |
| `getImageUrl()` | Devuelve la URL de la imagen de la tarjeta; solo se aplica a la tarjeta de noticias breve clásica. |
| `isDismissed` | Devuelve un booleano que indica si la tarjeta ha sido descartada. Establécelo en `true` para marcar la tarjeta como descartada. Si una tarjeta ya está marcada como descartada, no se puede volver a marcar como descartada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Classic #text-Announcement-card-for-android" }

## Métodos de tarjeta {#card-methods}

Todos los objetos del modelo de datos [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) ofrecen los siguientes métodos de análisis para registrar eventos de usuario en los servidores de Braze.

| Método | Descripción |
|---|---|
| `logImpression()` | Registra manualmente una impresión en Braze para una tarjeta concreta. |
| `logClick()` | Registra manualmente un clic en Braze para una tarjeta concreta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Card methods" }