{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Feeds de cartões {#card-feeds}

O SDK or kit de desenvolvimento de software da Braze inclui um feed de cartão padrão. Para mostrar o feed do cartão padrão, você pode usar o método `launchContentCards()`. Esse método lida com todo o rastreamento de análise de dados, descartes e renderização dos Content Cards de um usuário.

## Content Cards

Você pode usar esses métodos adicionais para criar um feed de Content Cards personalizado no seu app:

| Método | Descrição |
|---|---|
| `requestContentCardsRefresh()` | Envia uma solicitação em segundo plano para solicitar os Content Cards mais recentes do servidor do SDK or kit de desenvolvimento de software da Braze. |
| `getContentCardsFromServer(successCallback, errorCallback)` | Recupera os Content Cards do SDK or kit de desenvolvimento de software da Braze. Isso solicitará os Content Cards mais recentes do servidor e retornará a lista de cartões após a conclusão. |
| `getContentCardsFromCache(successCallback, errorCallback)` | Recupera os Content Cards do SDK or kit de desenvolvimento de software da Braze. Isso retornará a lista mais recente de cartões do cache local, que foi atualizada na última atualização. |
| `logContentCardClicked(cardId)` | Registra um clique para o ID do Content Card fornecido. |
| `logContentCardImpression(cardId)` | Registra uma impressão para o ID do Content Card fornecido. |
| `logContentCardDismissed(cardId)` | Registra um descarte para o ID do Content Card fornecido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Cards" }