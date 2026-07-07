{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Flux de cartes {#card-feeds}

Le SDK Braze comprend un flux de cartes par défaut. Pour afficher le flux de cartes par défaut, vous pouvez utiliser la méthode `launchContentCards()`. Cette méthode gère l'ensemble du suivi analytique, des rejets et du rendu des Content Cards d'un utilisateur.

## Content Cards

Vous pouvez utiliser ces méthodes supplémentaires pour créer un flux de Content Cards personnalisé dans votre application :

| Méthode | Description |
|---|---|
| `requestContentCardsRefresh()` | Envoie une requête en arrière-plan pour demander les dernières Content Cards au serveur du SDK Braze. |
| `getContentCardsFromServer(successCallback, errorCallback)` | Récupère les Content Cards du SDK Braze. Cette fonction demande les dernières Content Cards au serveur et renvoie la liste des cartes une fois l'opération terminée. |
| `getContentCardsFromCache(successCallback, errorCallback)` | Récupère les Content Cards du SDK Braze. Cette fonction renvoie la dernière liste de cartes depuis le cache local, qui a été mis à jour lors de la dernière actualisation. |
| `logContentCardClicked(cardId)` | Enregistre un clic pour l'ID de carte de contenu donné. |
| `logContentCardImpression(cardId)` | Enregistre une impression pour l'ID de carte de contenu donné. |
| `logContentCardDismissed(cardId)` | Enregistre un rejet pour l'ID de carte de contenu donné. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Cards" }