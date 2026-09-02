---
nav_title: Depurador de Connected Content
article_title: Depurador de Connected Content
page_order: 3.5
description: "Este artigo de referência aborda como usar o Depurador de Connected Content para solucionar problemas antes de lançar sua mensagem."
---

# Depurador de Connected Content {#connected-content-debugger}

> Use o Depurador de Connected Content para visualizar a solicitação e a resposta em tempo real de cada chamada de Connected Content, para que você possa verificar seu endpoint, cabeçalhos e Liquid tags antes de lançar uma Campaign ou um Canvas.

## Sobre o depurador {#about-the-debugger}

O Connected Content permite enriquecer mensagens com dados em tempo real, fazendo uma chamada HTTP a uma API or interface de programação do aplicativo (API) externa no momento da renderização e inserindo a resposta na sua mensagem com Liquid. Como essa chamada acontece fora da Braze, pode ser difícil ver exatamente qual solicitação a Braze enviou, o que o endpoint retornou ou por que uma chamada falhou, antes que uma Campaign ou Canvas esteja ativa.

O Depurador de Connected Content ajuda a solucionar esses problemas antes do lançamento. Ele mostra a solicitação e a resposta em tempo real para cada chamada de Connected Content na sua mensagem, na seção **Prévia e Teste**. Dessa forma, você pode confirmar que seu endpoint, cabeçalhos e Liquid tags estão configurados corretamente, tudo dentro do dashboard da Braze.

### Áreas compatíveis {#supported-areas}

O Depurador de Connected Content está disponível para as seguintes áreas:

- Etapas de Contexto do Canvas
- Content Cards
- E-mail
    - Inclui modelos
    - Exclui rodapés e páginas de inscrição
- In-App Messages
- Notificações por push
- SMS/MMS/RCS
- Webhooks
    - Inclui modelos
- WhatsApp

{% alert note %}
O depurador está disponível para a maioria dos canais, mas ainda não para KakaoTalk, LINE, Banners ou superfícies de composição não específicas de canal (como Content Blocks e a etapa de Atualização de Usuário do Canvas). Se você não vir o depurador, o debug de Connected Content pode ainda não ser compatível com esse recurso.
{% endalert %}

## Usar o depurador {#use-the-debugger}

Cada vez que você executa uma prévia, a Braze renderiza automaticamente os resultados da chamada de Connected Content na guia **prévia**. Para usar o depurador:

1. Configure sua mensagem com a tag {% raw %}`{% connected_content %}`{% endraw %}.
2. Acesse a seção **prévia & Test**. Se sua mensagem incluir uma tag de Connected Content, você pode ver um resumo com o número de chamadas de Connected Content e os status de sucesso e erro.

![Seção de Connected Content na seção de teste.]({% image_buster /assets/img/connected_content/debugger1.png %})

{:start="3"}
3. Selecione **View details** para abrir o depurador ao lado da sua prévia. O painel exibe uma tabela com a URL e o resultado de cada chamada de Connected Content.

![Chamadas de Connected Content com três URLs para revisar.]({% image_buster /assets/img/connected_content/debugger3.png %})

{:start="4"}
4. Ao lado de cada URL e resultado, selecione **View** para visualizar os cabeçalhos de solicitação e resposta, a carga útil, o método, a duração e as informações de cache.

![Chamada de Connected Content com detalhes de solicitação e resposta.]({% image_buster /assets/img/connected_content/debugger4.png %})

{:start="5"}
5. Revise os resultados, ajuste sua tag, cabeçalhos ou endpoint conforme necessário. Em seguida, gere uma nova prévia para confirmar a correção.

Se o seu modelo contiver mais de uma tag {% raw %}`{% connected_content %}`{% endraw %}, o depurador lista todas as chamadas realizadas. Para canais que renderizam vários corpos de mensagem a partir de um modelo (por exemplo, e-mail, que renderiza corpos HTML, texto simples e AMP separadamente, ou Quick Push, que renderiza corpos separados específicos por dispositivo), o depurador mostra todas as chamadas de Connected Content feitas em todos os corpos, não apenas o que você está visualizando no momento.

## Entenda a saída de depuração {#understand-the-debug-output}

Cada chamada de Connected Content aparece com suas próprias guias **Response** e **Request**. A guia **Response** é exibida por padrão, pois geralmente é o primeiro indicador para confirmar se uma chamada foi bem-sucedida.

### Detalhes da URL {#url-details}

| Campo | Descrição |
| --- | --- |
| URL | A URL totalmente renderizada que a Braze chamou, com quaisquer Liquid tags resolvidas. |
| Method | O método HTTP utilizado (GET ou POST). |
| Status code | O código de status HTTP retornado pelo seu endpoint (por exemplo, `200`, `404`, `500`). Consulte [Solução de problemas de códigos de resposta](#troubleshooting-response-codes) para códigos específicos da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalhes da URL" }

### Guia Response {#response-tab}

| Campo | Descrição |
| --- | --- |
| Duration | Quanto tempo a solicitação levou para ser concluída, em segundos. A duração é exibida apenas para chamadas em tempo real (não armazenadas em cache). |
| Served from cache | Indica se essa resposta foi servida a partir do cache de Connected Content da Braze em vez de uma chamada em tempo real ao seu endpoint (`Yes` ou `No`). Um resultado em cache reflete uma resposta anterior, não necessariamente o estado atual do seu endpoint. |
| Response body | O corpo retornado pelo seu endpoint. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Guia Response" }

### Guia Request {#request-tab}

| Campo | Descrição |
| --- | --- |
| Headers | Cabeçalhos da sua tag de Connected Content (`:headers`, credenciais e opções como `:content_type`). |
| Body | O corpo da solicitação enviado, se houver (solicitações POST). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Guia Request" }

## Quais cabeçalhos de solicitação aparecem no depurador {#which-request-headers-appear-in-the-debugger}

A guia **Request** lista os cabeçalhos da sua tag de Connected Content: `:headers` personalizados, credenciais armazenadas e cabeçalhos definidos por opções da tag, como `:content_type` e `:basic_auth`. A Braze também adiciona cabeçalhos padrão na solicitação de saída para o seu endpoint (por exemplo, `User-Agent` e `Host`). Esses cabeçalhos adicionados pela Braze aparecem no depurador quando você os define em `:headers`.

{% alert note %}
Para enviar um `User-Agent` consistente, defina-o em `:headers`. A Braze usa o seu valor, e o depurador exibe esse cabeçalho.
{% endalert %}

{% multi_lang_include connected_content/outgoing_request_headers.md %}

## Redação de credenciais {#credential-redaction}

Se a sua tag de Connected Content usar `:basic_auth`, cabeçalhos secretos comuns, chaves ou outras [opções de credenciais de autenticação]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types), o depurador oculta esses valores na guia **Request** e os substitui por uma série de asteriscos (*). Isso permite que você confirme que as credenciais foram incluídas na solicitação sem expor os valores em **prévia & Test**.

Falhas de autenticação ainda ficam visíveis mesmo quando as credenciais estão ocultas: se o seu endpoint retornar um `401` ou `403`, esse código de status aparece normalmente na guia **Response**, para que você saiba que sua solicitação foi rejeitada por falha de autenticação, mesmo que a credencial em si esteja oculta.

## Solução de problemas de códigos de resposta {#troubleshooting-response-codes}

### Erros do endpoint versus limites impostos pela Braze {#endpoint-errors-versus-braze-imposed-limits}

Nem todo código de status diferente de `2XX` na guia **Response** vem do seu endpoint. A Braze aplica seus próprios limites nas chamadas de Connected Content, e esses limites podem gerar respostas que parecem semelhantes a um erro de endpoint.

Se você encontrar [códigos de resposta]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#start-here-match-your-symptom) como `408`, `429`, `502`, `503`, `504` ou `599`, o problema geralmente está do lado da Braze na chamada — relacionado à integridade do host, tempo limite ou tamanho da carga útil. Se o seu endpoint retorna respostas grandes de forma consistente, considere reduzir a carga útil da resposta para incluir apenas os campos necessários para a sua mensagem.

### O endpoint retornou um código de status inesperado {#endpoint-returned-an-unexpected-status-code}

Use a guia **Request** para confirmar a URL, os cabeçalhos da sua tag e o corpo da solicitação. Uma causa comum de respostas `4XX` inesperadas é uma Liquid tag dentro da URL, dos cabeçalhos ou do corpo que não foi resolvida da forma esperada. Verifique se todas as referências {% raw %}`{{ }}`{% endraw %} apontam para campos que existem para o usuário ou contexto que você está visualizando.

### A resposta parece desatualizada {#response-looks-stale}

Verifique o campo **Served from cache** na guia **Response**. Se ele mostrar `Yes`, o depurador está exibindo uma resposta armazenada em cache anteriormente, em vez de uma chamada nova. Adicione `:no_cache` à sua tag temporariamente, ou aguarde o cache expirar (conforme `:cache_max_age`), para confirmar o comportamento atual do endpoint.

## Artigos relacionados {#related-articles}

- [Referência de Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Fazer uma chamada de API or interface de programação do aplicativo (API) de Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [Cabeçalhos de solicitação de saída]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#outgoing-request-headers)
- [Solucionar problemas de webhooks e solicitações de Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content)