{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Karten-Feeds {#card-feeds}

Das Braze SDK or Software-Development-Kit enthält einen Standard-Karten-Feed. Um den Standard-Karten-Feed anzuzeigen, können Sie die Methode `launchContentCards()` verwenden. Diese Methode verarbeitet das gesamte Analytics-Tracking, Ausblendungen und die Darstellung der Content Cards einer Nutzer:in.

## Content Cards

Mit diesen zusätzlichen Methoden können Sie einen angepassten Content-Card-Feed in Ihrer App erstellen:

| Methode | Beschreibung |
|---|---|
| `requestContentCardsRefresh()` | Sendet eine Anfrage im Hintergrund, um die neuesten Content Cards vom Braze SDK or Software-Development-Kit-Server anzufordern. |
| `getContentCardsFromServer(successCallback, errorCallback)` | Ruft Content Cards aus dem Braze SDK or Software-Development-Kit ab. Diese Funktion fragt die neuesten Content Cards vom Server ab und gibt nach Abschluss die Liste der Karten zurück. |
| `getContentCardsFromCache(successCallback, errorCallback)` | Ruft Content Cards aus dem Braze SDK or Software-Development-Kit ab. Dies gibt die neueste Liste der Karten aus dem lokalen Cache zurück, die beim letzten Refresh aktualisiert wurde. |
| `logContentCardClicked(cardId)` | Protokolliert einen Klick für die angegebene Content-Card-ID. |
| `logContentCardImpression(cardId)` | Protokolliert eine Impression für die angegebene Content-Card-ID. |
| `logContentCardDismissed(cardId)` | Protokolliert eine Ausblendung für die angegebene Content-Card-ID. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Cards" }