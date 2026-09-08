---
nav_title: Criar um webhook
article_title: Criar um webhook
page_order: 1
channel:
  - webhooks
description: "Este artigo de referência aborda como criar e configurar uma campanha de webhook."
search_rank: 2
---

# Criar uma campanha de webhook {#create-a-webhook-campaign}

> Criar uma campanha de webhook ou incluir um webhook em uma campanha multicanal permite acionar ações fora do app, fornecendo informações em tempo real a outros sistemas e aplicativos.

Você pode usar webhooks para enviar informações a sistemas como Salesforce ou Marketo, ou aos seus sistemas de backend. Por exemplo, você pode querer creditar as contas dos seus clientes com uma promoção depois que eles realizarem um evento personalizado um determinado número de vezes.

{% alert tip %}
Para saber mais sobre o que são webhooks e como você pode usá-los na Braze, confira [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks) antes de prosseguir.
{% endalert %}

## Etapa 1: Escolha onde criar sua mensagem {#step-1-choose-where-to-build-your-message}

Não tem certeza se sua mensagem deve ser enviada usando uma Campaign ou um Canvas? Campaigns são melhores para campanhas de mensagens únicas e direcionadas, enquanto Canvas são melhores para jornadas de usuários com várias etapas.

{% tabs %}
{% tab Campaign %}

**Etapas:**

1. Acesse **Envio de mensagens** > **Campaigns** e selecione **Criar Campaign**.
2. Selecione **Webhook** ou, para campanhas direcionadas a vários canais, selecione **Multicanal**.
3. Dê à sua campanha um nome claro e significativo.
4. (Opcional) Adicione uma descrição para descrever como essa campanha será usada.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) conforme necessário.
   * Tags facilitam a localização de suas campanhas e a criação de relatórios. Por exemplo, ao usar o [Construtor de Relatórios]({{site.baseurl}}/user_guide/analytics/reports/report_builder), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher modelos de webhook diferentes para cada uma das variantes adicionadas. Para saber mais sobre esse tópico, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Se todas as mensagens da sua campanha forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Em seguida, você pode escolher **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Etapas:**

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

## Etapa 2: Crie seu webhook {#step-2-build-your-webhook}

Você pode optar por criar um webhook do zero, usar um modelo existente ou utilizar um dos nossos modelos disponíveis. Em seguida, crie seu webhook na guia **Criador** do editor.

A guia **Criador** é composta pelos seguintes campos:

- Idioma
- URL do webhook
- Método HTTP
- Corpo da solicitação

![A guia "Criador" com um exemplo de modelo de webhook.]({% image_buster /assets/img_archive/webhook_compose.png %})

### Idioma {#internationalization}

A [internacionalização]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) é compatível com a URL e o corpo da solicitação. Para internacionalizar sua mensagem, selecione **Adicionar idiomas** e preencha os campos obrigatórios.

Recomendamos selecionar seus idiomas antes de escrever o conteúdo para que você possa preencher o texto nos campos adequados no Liquid. Para ver a lista completa de idiomas disponíveis, consulte [Idiomas compatíveis]({{site.baseurl}}/developer_guide/localization?tab=android).

Se você estiver adicionando texto em um idioma escrito da direita para a esquerda, note que a aparência final das mensagens da direita para a esquerda depende muito de como os provedores de serviço as renderizam. Para conhecer as práticas recomendadas na criação de mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### URL do webhook {#webhook-url}

A URL do webhook, ou URL HTTP, especifica seu endpoint. O endpoint é o local para onde você enviará as informações capturadas pelo webhook.

Se você quiser enviar informações para um fornecedor, o fornecedor deve fornecer essa URL na documentação da API. Se estiver enviando informações para seus próprios sistemas, confirme com sua equipe de desenvolvimento ou engenharia se a URL utilizada está correta.

A Braze permite apenas URLs que se comunicam pelas portas padrão `80` (HTTP) e `443` (HTTPS).

#### Uso do Liquid {#using-liquid}

Você pode personalizar as URLs do seu webhook usando [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid). Em alguns casos, determinados endpoints podem exigir que você identifique um usuário ou forneça informações específicas do usuário como parte da URL. Ao usar o Liquid, certifique-se de incluir um [valor padrão]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web) para cada informação específica do usuário utilizada na URL.

### Método HTTP {#http-method}

O método HTTP que você deve usar varia de acordo com o endpoint para o qual está enviando informações. Na maioria dos casos, você usará POST.

| Método HTTP | Descrição |
| ----------- | ----------- |
| POST | Grava novas informações no servidor de destino. Este é o método mais comum usado no envio de dados. |
| GET | Recupera informações existentes, em vez de gravar novas. Por definição, uma solicitação GET não aceita corpo de solicitação. |
| PUT | Atualiza informações no endpoint, substituindo quaisquer informações existentes pelo conteúdo do corpo da solicitação. |
| DELETE | Exclui o recurso na URL HTTP. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Método HTTP" }

### Corpo da solicitação {#request-body}

O corpo da solicitação contém as informações que serão enviadas para a URL que você especificou. Você pode criar o corpo da sua solicitação de webhook usando pares de chave-valor JSON ou texto bruto.

#### Pares de chave-valor JSON {#json-key-value-pairs}

Os pares de chave-valor JSON permitem escrever facilmente uma solicitação para um endpoint que espera um formato JSON. Esse recurso só pode ser usado com endpoints que esperam uma solicitação JSON. Por exemplo, se sua chave for `message_body`, o valor correspondente pode ser `Your order just arrived!`. Depois de inserir o par de chave-valor, o criador configurará sua solicitação na sintaxe JSON, e uma prévia da solicitação JSON será preenchida automaticamente.

![Corpo da solicitação configurado com pares de chave-valor JSON.]({% image_buster /assets/img/webhook_json_1.png %})

Você pode personalizar seus pares de chave-valor usando Liquid, incluindo qualquer atributo do usuário, [atributo personalizado]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift) ou [propriedade de evento]({{site.baseurl}}/user_guide/data/activation/events/custom_events) na sua solicitação. Por exemplo, você pode incluir o nome e o e-mail de um cliente na solicitação. Certifique-se de incluir um [valor padrão]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web) para cada atributo.

#### Texto bruto {#raw-text}

A opção de texto bruto oferece flexibilidade para escrever uma solicitação para um endpoint que espera um corpo em qualquer formato. Por exemplo, você pode usar essa opção para escrever uma solicitação para um endpoint que espera o formato XML.

Tanto a [personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) quanto a [internacionalização]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) usando Liquid são compatíveis com texto bruto.

![Um exemplo de corpo de solicitação com texto bruto usando Liquid.]({% image_buster /assets/img_archive/webhook_rawtext.png %})

Se você definir o [cabeçalho da solicitação](#request-headers-optional) `Content-Type` como `application/x-www-form-url-encoded`, o corpo da solicitação deve ser formatado como uma string codificada por URL. Por exemplo:

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![Corpo da solicitação com string codificada por URL.]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## Etapa 3: Definir configurações adicionais {#step-3-configure-additional-settings}

### Cabeçalhos da solicitação (opcional) {#request-headers-optional}

Alguns endpoints podem exigir a inclusão de cabeçalhos na sua solicitação. Na seção **Compose** do criador, você pode adicionar quantos cabeçalhos forem necessários.

![Exemplos de cabeçalhos de solicitação para a chave "Authorization" e a chave "Content-Type".]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

Os cabeçalhos de solicitação mais comuns são especificações de [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) (que descrevem o tipo de dados esperado no corpo da mensagem, como XML ou JSON) e cabeçalhos de [`Authorization`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization), que contêm suas credenciais junto ao seu fornecedor ou sistema.

{% alert note %}
Os nomes dos cabeçalhos HTTP não diferenciam maiúsculas de minúsculas, conforme a [RFC 7230, seção 3.2 ("Each header field consists of a case-insensitive field name")](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2). Se o endpoint receptor ou quaisquer serviços intermediários (como CDNs) transformarem a capitalização do cabeçalho, isso não afetará o processamento — `Content-Type`, `content-type` e `CONTENT-TYPE` são todos tratados de forma idêntica.
{% endalert %}

As especificações de tipo de conteúdo devem usar a chave `Content-Type`. Os valores mais comuns são `application/json` ou `application/x-www-form-urlencoded`.

Os cabeçalhos de autorização devem usar a chave `Authorization`. Os valores mais comuns são {% raw %} `Bearer {{YOUR_TOKEN}}` ou `Basic {{YOUR_TOKEN}}` {% endraw %}, em que `YOUR_TOKEN` são as credenciais fornecidas pelo seu fornecedor ou sistema.

## Etapa 4: Envie uma mensagem de teste {#step-4-test-send-your-message}

Antes de ativar sua campanha, a Braze recomenda que você teste o webhook para garantir que a solicitação esteja formatada corretamente.

Para isso, alterne para a guia **Teste** e envie um webhook de teste. Você pode testar o webhook como um usuário aleatório, um usuário específico (inserindo o endereço de e-mail ou o ID de usuário externo) ou um usuário personalizado com os atributos de sua escolha.

Após enviar o webhook de teste, uma caixa de diálogo será exibida com a mensagem de resposta. Se a solicitação do webhook não for bem-sucedida, consulte a mensagem de erro para obter ajuda na solução de problemas do seu webhook. O exemplo a seguir detalha a resposta de um webhook com uma URL de webhook inválida.

```http
404 Not Found

{
  "error": {
    "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
    "status_code": 404
  }
}

```

Para saber mais, consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=webhook).

## Etapa 5: Crie o restante da sua campanha ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Em seguida, crie o restante da sua campanha. Consulte as seções a seguir para obter mais detalhes sobre como usar nossas ferramentas para criar webhooks.

### Escolha o cronograma de entrega ou o disparo {#choose-delivery-schedule-or-trigger}

Os webhooks podem ser entregues com base em um horário agendado, em uma ação ou em um disparo de API. Para saber mais, consulte [Agendamento da sua campanha]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Para a entrega baseada em ação, você também pode definir a duração da campanha e o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

Nesta etapa, você também pode especificar controles de entrega, como permitir que os usuários se tornem [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) para receber a campanha ou ativar regras de [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping).

### Escolha os usuários a serem direcionados {#choose-users-to-target}

Em seguida, você deve [direcionar os usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) escolhendo segmentos ou filtros para refinar seu público. Nesta etapa, você seleciona o público mais amplo a partir dos seus segmentos e, se desejar, refina esse segmento ainda mais com nossos filtros. Você recebe automaticamente uma prévia de como é a população aproximada desse segmento. Lembre-se de que a composição exata do segmento é sempre calculada antes do envio da mensagem.

{% multi_lang_include audience/target_audiences.md %}

### Escolha os eventos de conversão {#choose-conversion-events}

A Braze permite que você rastreie a frequência com que os usuários realizam ações específicas, chamadas [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), após receberem uma campanha. Você tem a opção de permitir uma janela de até 30 dias durante a qual uma conversão será contabilizada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes da sua etapa do Canvas. Para obter detalhes sobre como criar o restante do seu Canvas, incluindo testes multivariantes e [Otimizar com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), consulte [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

{% endtab %}
{% endtabs %}

## Etapa 6: Revisar e implementar {#step-6-review-and-deploy}

Depois de terminar de criar a última parte da sua Campaign ou Canvas, revise os detalhes, teste e envie!

## Informações importantes {#things-to-know}

### Erros, lógica de repetição e tempos limite {#errors-retry-logic-and-timeouts}

Os webhooks dependem dos servidores da Braze fazendo solicitações a um endpoint externo, e erros podem ocorrer ocasionalmente. Os erros mais comuns incluem erros de sintaxe, chaves de API expiradas, limites de frequência e problemas inesperados no lado do servidor. Antes de enviar uma campanha de webhook:

- Teste seu webhook para verificar erros de sintaxe
- Verifique se as variáveis personalizadas possuem valores padrão

Se o envio do webhook falhar, uma mensagem de erro será registrada no [Registro de atividade de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), incluindo detalhes como o horário do erro, o nome do app e informações sobre o erro.

![Erro de webhook com a mensagem "An active access token must be used to query information about the current user".]({% image_buster /assets/img_archive/webhook-error.png %})

Se a mensagem de erro não for clara o suficiente em relação à origem do erro, consulte a documentação do endpoint de API que você está usando. Normalmente, essa documentação fornece uma explicação dos códigos de erro que o endpoint utiliza e suas causas mais comuns.

#### Códigos de resposta e lógica de repetição {#response-codes-and-retry-logic}

Quando a solicitação do webhook é enviada, o servidor receptor retorna um código de resposta indicando o que aconteceu com a solicitação. A tabela a seguir resume as diferentes respostas que o servidor pode enviar, como elas afetam a análise de dados da campanha e se, em caso de erros, a Braze tentará reenviar a campanha:

| Código de resposta | Marcado como recebido? | Tentativas de reenvio? |
|---------------|-----------|----------|
| `20x` (sucesso)  | Sim |   N/A  |
| `30x` (redirecionamento)  | Não | Não |
| `408` (tempo limite da solicitação)  | Não | Sim |
| `429` (limite de frequência excedido)  | Não | Sim |
| `Outros 4XX` (erro do cliente)  | Não | Não |
| `5XX` (erro do servidor)   | Não | Sim |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Códigos de resposta e lógica de repetição" }

{% alert note %}
A Braze tenta reenviar os códigos de status que permitem repetição listados nesta seção por até cinco tentativas no total (a solicitação inicial mais quatro tentativas), com atraso crescente entre elas. Se a Braze não conseguir alcançar seu endpoint, as tentativas podem continuar por até 24 horas.<br><br>Cada solicitação de webhook tem um tempo limite de 120 segundos.
{% endalert %}

Os cabeçalhos de resposta `Retry-After` e de limite de frequência podem afetar o tempo que a Braze aguarda antes de uma tentativa de **reenvio** (por exemplo, após `408`, `429` ou `5XX`). Eles não tornam respostas que não permitem repetição, como `401`, elegíveis para reenvio.

<!-- support-analyzer-phase2:webhook_delivery_failures -->
{% alert note %}
Se os envios de webhook parecem estar ausentes na análise de dados, abra o [Registro de atividade de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) da Campaign ou da etapa do Canvas. A Braze tenta reenviar apenas determinadas respostas (por exemplo, `408`, `429` e `5XX`). A maioria dos outros erros de cliente `4XX`, incluindo `401 Unauthorized`, **não** é reenviada. Para a tabela completa de respostas, consulte [Códigos de resposta e lógica de repetição](#response-codes-and-retry-logic).
{% endalert %}


#### 403 Forbidden e lista de permissões de IP {#403-forbidden-and-ip-allowlisting}

Respostas `403 Forbidden` significam que seu endpoint recebeu a solicitação, mas a recusou. As causas mais comuns incluem autenticação inválida ou ausente, permissões de API insuficientes e regras de rede (como firewall ou firewall de aplicação web) que bloqueiam os endereços IP de saída da Braze.

Se as solicitações de webhook consistentemente retornarem `403` e seus cabeçalhos de autenticação estiverem corretos, adicione os IPs da Braze do seu cluster à lista de permissões no servidor que recebe o webhook. Consulte [Lista de permissões de IP](#ip-allowlisting). As solicitações de Connected Content usam os mesmos IPs de saída; consulte [Lista de permissões de IP para Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting).

Para outras etapas de solução de problemas com `4XX`, consulte [Solução de problemas de solicitações de webhook e Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#4xx-errors).

#### Autenticação e credenciais de Connected Content {#authentication-and-connected-content-credentials}

A solicitação HTTP de saída do webhook não suporta a vinculação de [credenciais de Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types) (`:basic_auth` ou `:auth_credentials`) para autenticação no seu endpoint. Em vez disso, configure a autenticação usando **Cabeçalhos da solicitação** no webhook. Para buscar um token ou segredo no momento do envio, você pode inserir uma tag {% raw %}`{% connected_content %}`{% endraw %} em um campo de cabeçalho ou corpo para que o Liquid a resolva antes do envio do webhook.

#### Modelos de webhook salvos e uso em Campaigns {#saved-webhook-templates-and-campaign-usage}

A Braze não oferece um relatório integrado que liste todas as Campaigns ou etapas do Canvas que referenciam um determinado **modelo de webhook salvo**. Para auditar o uso, revise as etapas de webhook que usam a mesma URL e o mesmo método HTTP, ou entre em contato com o [suporte da Braze]({{site.baseurl}}/support_contact).

#### Solução de problemas e detalhes adicionais de erros {#troubleshooting-and-additional-error-details}

Para explicações detalhadas, etapas de solução de problemas e orientações sobre como resolver erros específicos de webhook, consulte [Solução de problemas de solicitações de webhook e Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content). Você também encontrará mais explicações sobre como nosso sistema de detecção de hosts não saudáveis funciona e como a Braze fornece notificações de erro por meio de e-mails automatizados e registros adicionais no Braze Currents.

### Lista de permissões de IP {#ip-allowlisting}

Quando um webhook é enviado pela Braze, os servidores da Braze fazem solicitações de rede para servidores de clientes ou de terceiros. Com a lista de permissões de IP, você pode verificar se as solicitações de webhook estão vindo da Braze, adicionando uma camada de segurança.

A Braze enviará webhooks a partir dos seguintes IPs. Os IPs listados são adicionados automaticamente e dinamicamente a todas as chaves de API que optaram pela lista de permissões.

{% alert important %}
Se você estiver fazendo um webhook de Braze para Braze e usando a lista de permissões, adicione todos os seguintes IPs à lista, incluindo `127.0.0.1`.
{% endalert %}

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Excluir usuários {#delete-users}

Para excluir um usuário individual ou um Segment de usuários, acesse **Público** > **Gerenciar público** > **Excluir usuários**. O dashboard suporta exclusão em massa de Segments (até 10 milhões de perfis), inclui uma janela de cancelamento de 7 dias e não consome os limites de frequência compartilhados da REST API. Para etapas, limites e permissões, consulte [Excluir usuários]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users).

Para exclusão programática em lotes menores, use o [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) em vez de uma campanha de webhook.