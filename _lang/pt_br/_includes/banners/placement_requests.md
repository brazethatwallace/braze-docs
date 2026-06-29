Quando você [cria posicionamentos no seu app ou site]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), seu app envia uma solicitação para a Braze buscar mensagens de Banner para cada posicionamento.

- Você pode solicitar até **10 posicionamentos por solicitação de atualização**.
- Para cada posicionamento, a Braze retorna o **Banner de maior prioridade** que o usuário é elegível para receber.
- Se mais de 10 posicionamentos forem solicitados em uma atualização, apenas os primeiros 10 são retornados; os demais são descartados.

Por exemplo, um app pode solicitar três posicionamentos em uma solicitação de atualização: `homepage_promo`, `cart_abandonment` e `seasonal_offer`. Cada solicitação retorna o Banner mais relevante para aquele posicionamento.

#### Limite de taxa para solicitações de atualização {#rate-limiting-for-refresh-requests}

Se você estiver em versões mais antigas do SDK (antes do Swift 13.1.0, Android 38.0.0, Web 6.1.0, React Native 17.0.0 e Flutter 15.0.0), apenas uma solicitação de atualização é permitida por sessão de usuário.

Se você estiver em versões mínimas mais novas do SDK (Swift 13.1.0+, Android 38.0.0+, Web 6.1.0+, React Native 17.0.0+ e Flutter 15.0.0+), as solicitações de atualização são controladas por um algoritmo de token bucket para evitar polling excessivo:

- Cada sessão de usuário começa com cinco tokens de atualização.
- Os tokens são reabastecidos a uma taxa de um token a cada 180 segundos (3 minutos).

Cada chamada explícita para `requestBannersRefresh` consome um token. A atualização automática que ocorre no início de uma nova sessão ou quando `changeUser` é chamado não consome um token, pois essa atualização é uma publicação do último Banner em cache para aquele usuário. Se você tentar uma atualização quando não houver tokens disponíveis, o SDK não faz a solicitação e registra um erro até que um token seja reabastecido. Isso é importante para atualizações durante a sessão e atualizações acionadas por eventos. Para implementar atualizações dinâmicas (por exemplo, após um usuário completar uma ação na mesma página), chame o método de atualização após o evento personalizado ser registrado, mas observe a postergação necessária para a Braze ingerir e processar o evento antes que o usuário se qualifique para uma Campaign de Banner diferente.