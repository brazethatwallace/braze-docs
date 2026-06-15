{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Fuentes de tarjetas {#card-feeds}

El SDK de Braze incluye una fuente de tarjetas predeterminada. Para mostrar la fuente de tarjetas predeterminada, puedes utilizar el método `launchContentCards()`. Este método gestiona todo el seguimiento de análisis, los descartes y la representación de las Content Cards de un usuario.

## Content Cards

Puedes utilizar estos métodos adicionales para crear una fuente personalizada de Content Cards dentro de tu aplicación:

| Método | Descripción |
|---|---|
| `requestContentCardsRefresh()` | Envía una petición en segundo plano para solicitar las últimas Content Cards al servidor del SDK de Braze. |
| `getContentCardsFromServer(successCallback, errorCallback)` | Recupera Content Cards del SDK de Braze. Esto solicitará las últimas Content Cards al servidor y devolverá la lista de tarjetas al finalizar. |
| `getContentCardsFromCache(successCallback, errorCallback)` | Recupera Content Cards del SDK de Braze. Esto devolverá la última lista de tarjetas de la caché local, que se actualizó en la última actualización. |
| `logContentCardClicked(cardId)` | Registra un clic para el ID de tarjeta de contenido dado. |
| `logContentCardImpression(cardId)` | Registra una impresión para el ID de tarjeta de contenido dado. |
| `logContentCardDismissed(cardId)` | Registra un descarte para el ID de tarjeta de contenido dado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Cards" }