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
Para saber mais sobre o que são webhooks e como você pode usá-los na Braze, confira [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks/) antes de prosseguir.
{% endalert %}

## Etapa 1: Escolha onde criar sua mensagem {#step-1-choose-where-to-build-your-message}

Não tem certeza se sua mensagem deve ser enviada usando uma Campaign ou um Canvas? Campaigns são melhores para campanhas de mensagens únicas e direcionadas, enquanto Canvas são melhores para jornadas de usuário com várias etapas.

{% tabs %}
{% tab Campaign %}

**Etapas:**

1. Acesse **Messaging** > **Campaigns** e selecione **Create Campaign**.
2. Selecione **Webhook** ou, para campanhas direcionadas a múltiplos canais, selecione **Multichannel**.
3. Dê à sua campanha um nome claro e significativo.
4. (Opcional) Adicione uma descrição para descrever como essa campanha será usada.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) e [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) conforme necessário.
   * Tags facilitam encontrar suas campanhas e criar relatórios a partir delas. Por exemplo, ao usar o [Criador de relatórios]({{site.baseurl}}/user_guide/analytics/reports/report_builder/), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes modelos de webhook para cada uma das variantes adicionadas. Para saber mais sobre esse tópico, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% alert tip %}
Se todas as mensagens da sua campanha forem semelhantes ou tiverem o mesmo conteúdo, redija sua mensagem antes de adicionar variantes adicionais. Em seguida, escolha **Copy from Variant** no menu suspenso **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Etapas:**

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) usando o criador de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa no construtor de Canvas. Dê à sua etapa um nome claro e significativo.
3. Escolha um [agendamento de etapa]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#schedule-your-canvas-step) e especifique uma postergação conforme necessário.
4. Filtre seu público para esta etapa conforme necessário. Você pode refinar ainda mais os destinatários desta etapa especificando segmentos e adicionando filtros adicionais. As opções de público serão verificadas após a postergação, no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento de avanço]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#advancement-behavior).
6. Escolha quaisquer outros canais de envio de mensagens que você gostaria de combinar com sua mensagem.

{% endtab %}
{% endtabs %}

## Etapa 2: Crie seu webhook {#step-2-build-your-webhook}

Você pode optar por criar um webhook do zero, usar um modelo existente ou usar um dos nossos modelos disponíveis. Em seguida, crie seu webhook na guia **Compose** do editor.

A guia **Compose** consiste nos seguintes campos:

- Idioma
- URL do webhook
- Método HTTP
- Corpo da solicitação

![A guia "Compose" com um exemplo de modelo de webhook.]({% image_buster /assets/img_archive/webhook_compose.png %})

#### Idioma {#internationalization}

A [internacionalização]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/#campaigns-in-multiple-languages) é suportada na URL e no corpo da solicitação. Para internacionalizar sua mensagem, selecione **Add languages** e preencha os campos obrigatórios.

Recomendamos selecionar seus idiomas antes de escrever seu conteúdo para que você possa preencher seu texto onde ele pertence no Liquid. Para nossa lista completa de idiomas disponíveis que você pode usar, consulte [Idiomas suportados]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

Se você estiver adicionando texto em um idioma escrito da direita para a esquerda, observe que a aparência final das mensagens da direita para a esquerda depende em grande parte de como os prestadores de serviço as renderizam. Para práticas recomendadas sobre como criar mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/).

#### URL do webhook {#webhook-url}

A URL do webhook, ou URL HTTP, especifica seu endpoint. O endpoint é o local para onde você enviará as informações que está capturando no webhook.

Se você deseja enviar informações a um fornecedor, o fornecedor deve fornecer essa URL na documentação da API dele. Se você está enviando informações para seus próprios sistemas, verifique com sua equipe de desenvolvimento ou engenharia para confirmar que está usando a URL correta.

A Braze permite apenas URLs que se comunicam por portas padrão `80` (HTTP) e `443` (HTTPS).

##### Usando Liquid {#using-liquid}

Você pode personalizar suas URLs de webhook usando [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/). Às vezes, certos endpoints podem exigir que você identifique um usuário ou forneça informações específicas do usuário como parte da sua URL. Ao usar Liquid, certifique-se de incluir um [valor padrão]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) para cada informação específica do usuário que você usar na sua URL.

#### Método HTTP {#http-method}

O método HTTP que você deve usar varia dependendo do endpoint para o qual está enviando informações. Na maioria dos casos, você usará POST.

| Método HTTP | Descrição |
| ----------- | ----------- |
| POST | Grava novas informações no servidor receptor. Este é o método mais comum usado ao enviar dados. |
| GET | Recupera informações existentes, em vez de gravar novas informações. Por definição, uma solicitação GET não suporta um corpo de solicitação. |
| PUT | Atualiza informações no endpoint, substituindo quaisquer informações existentes pelo que está no corpo da solicitação. |
| DELETE | Exclui o recurso na URL HTTP. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTTP method" }

#### Corpo da solicitação {#request-body}

O corpo da solicitação é a informação que será enviada para a URL que você especificou. Você pode criar o corpo da sua solicitação de webhook com pares de chave-valor JSON ou texto bruto.

##### Pares de chave-valor JSON {#json-key-value-pairs}

Pares de chave-valor JSON permitem que você escreva facilmente uma solicitação para um endpoint que espera um formato JSON. Você só pode usar isso com um endpoint que espera uma solicitação JSON. Por exemplo, se sua chave for `message_body`, o valor correspondente pode ser `Your order just arrived!`. Depois de inserir seu par de chave-valor, o criador configurará sua solicitação na sintaxe JSON, e uma pré-visualização da sua solicitação JSON será preenchida automaticamente.

![Corpo da solicitação definido como pares de chave-valor JSON.]({% image_buster /assets/img/webhook_json_1.png %})

Você pode personalizar seus pares de chave-valor usando Liquid, incluindo qualquer atributo de usuário, [atributo personalizado]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#additional-notes-and-best-practices) ou [propriedade de evento]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) na sua solicitação. Por exemplo, você pode incluir o nome e o e-mail de um cliente na sua solicitação. Certifique-se de incluir um [valor padrão]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) para cada atributo.

##### Texto bruto {#raw-text}

A opção de texto bruto oferece a flexibilidade de escrever uma solicitação para um endpoint que espera um corpo de qualquer formato. Por exemplo, você pode usar isso para escrever uma solicitação para um endpoint que espera que sua solicitação esteja em formato XML.

Tanto a [personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) quanto a [internacionalização]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/#campaigns-in-multiple-languages) usando Liquid são suportadas em texto bruto.

![Um exemplo de corpo de solicitação com texto bruto usando Liquid.]({% image_buster /assets/img_archive/webhook_rawtext.png %})

Se você definir o [cabeçalho de solicitação](#request-headers-optional) `Content-Type` como `application/x-www-form-url-encoded`, o corpo da solicitação deve ser formatado como uma string codificada em URL. Por exemplo:

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![Corpo da solicitação com string codificada em URL.]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## Etapa 3: Configure definições adicionais {#step-3-configure-additional-settings}

#### Cabeçalhos de solicitação (opcional) {#request-headers-optional}

Certos endpoints podem exigir que você inclua cabeçalhos na sua solicitação. Na seção **Compose** do criador, você pode adicionar quantos cabeçalhos forem necessários.

![Exemplos de cabeçalhos de solicitação para a chave "Authorization" e a chave "Content-type".]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

Cabeçalhos de solicitação comuns são especificações de `Content-Type` (que descrevem que tipo de dados esperar no corpo, como XML ou JSON) e cabeçalhos de autorização que contêm suas credenciais com seu fornecedor ou sistema.

As especificações de tipo de conteúdo devem usar a chave `Content-Type`. Valores comuns são `application/json` ou `application/x-www-form-urlencoded`.

Os cabeçalhos de autorização devem usar a chave `Authorization`. Valores comuns são {% raw %} `Bearer {{YOUR_TOKEN}}` ou `Basic {{YOUR_TOKEN}}` {% endraw %} onde `YOUR_TOKEN` são as credenciais fornecidas pelo seu fornecedor ou sistema.

## Etapa 4: Teste o envio da sua mensagem {#step-4-test-send-your-message}

Antes de colocar sua campanha no ar, a Braze recomenda que você teste o webhook para garantir que a solicitação esteja formatada corretamente.

Para isso, mude para a guia **Test** e envie um webhook de teste. Você pode testar o webhook como um usuário aleatório, um usuário específico (inserindo o endereço de e-mail ou ID de usuário externo) ou um usuário personalizado com atributos de sua escolha.

Após enviar o webhook de teste, uma caixa de diálogo aparecerá com a mensagem de resposta. Se a solicitação do webhook não for bem-sucedida, consulte a mensagem de erro para ajudar na solução de problemas do seu webhook. O exemplo a seguir detalha a resposta de um webhook com uma URL de webhook inválida.

```http
404 Not Found

{
  "error": {
    "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
    "status_code": 404
  }
}

```

Para mais informações, consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=webhook).

## Etapa 5: Construa o restante da sua campanha ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Em seguida, construa o restante da sua campanha. Consulte as seções a seguir para mais detalhes sobre como usar melhor nossas ferramentas para criar webhooks.

#### Escolha o agendamento de entrega ou gatilho {#choose-delivery-schedule-or-trigger}

Webhooks podem ser entregues com base em um horário agendado, uma ação ou com base em um gatilho de API. Para saber mais, consulte [Agendando sua campanha]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

Para entrega baseada em ação, você também pode definir a duração da campanha e o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/).

Nesta etapa, você também pode especificar controles de entrega, como permitir que os usuários se tornem [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/#campaigns) para receber a campanha, ou habilitar regras de [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping).

#### Escolha os usuários a serem direcionados {#choose-users-to-target}

Em seguida, você deve [direcionar os usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/) escolhendo segmentos ou filtros para restringir seu público. Nesta etapa, você seleciona o público maior dos seus segmentos e restringe ainda mais esse segmento com nossos filtros, se desejar. Você recebe automaticamente uma pré-visualização de como é a população aproximada desse segmento. Tenha em mente que a composição exata do segmento é sempre calculada antes do envio da mensagem.

{% multi_lang_include target_audiences.md %}

#### Escolha eventos de conversão {#choose-conversion-events}

A Braze permite que você acompanhe com que frequência os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você tem a opção de permitir uma janela de até 30 dias durante a qual uma conversão será contabilizada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não o fez, conclua as seções restantes da sua etapa do Canvas. Para mais detalhes sobre como construir o restante do seu Canvas, implementar testes multivariantes e Seleção inteligente, e mais, consulte a etapa [Construa seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) da nossa documentação de Canvas.

{% endtab %}
{% endtabs %}

## Etapa 6: Revise e implante {#step-6-review-and-deploy}

Depois de terminar de construir a última parte da sua campanha ou Canvas, revise seus detalhes, teste e envie!

## O que você precisa saber {#things-to-know}

### Erros, lógica de nova tentativa e timeouts {#errors-retry-logic-and-timeouts}

Webhooks dependem dos servidores da Braze fazendo solicitações a um endpoint externo, e erros podem ocorrer ocasionalmente. Os erros mais comuns incluem erros de sintaxe, chaves de API expiradas, limites de taxa e problemas inesperados no lado do servidor. Antes de enviar uma campanha de webhook:

- Teste seu webhook para erros de sintaxe
- Certifique-se de que variáveis personalizadas tenham valores padrão

Se o seu webhook falhar ao enviar, uma mensagem de erro será registrada no [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) e incluirá detalhes como o timestamp do erro, nome do app e detalhes sobre o erro.

![Erro de webhook com a mensagem "An active access token must be used to query information about the current user".]({% image_buster /assets/img_archive/webhook-error.png %})

Se a mensagem de erro não for clara o suficiente sobre a origem do erro, você deve verificar a documentação do endpoint de API que está usando. Normalmente, ela fornece uma explicação dos códigos de erro que o endpoint usa, bem como o que geralmente os causa.

#### Códigos de resposta e lógica de nova tentativa {#response-codes-and-retry-logic}

Quando a solicitação do webhook é enviada, o servidor receptor retornará um código de resposta indicando o que aconteceu com a solicitação. A tabela a seguir resume as diferentes respostas que o servidor pode enviar, como elas impactam a análise de dados da campanha e se, no caso de erros, a Braze tentará reenviar a campanha:

| Código de resposta | Marcado como recebido? | Novas tentativas? |
|---------------|-----------|----------|
| `20x` (sucesso)  | Sim |   N/A  |
| `30x` (redirecionamento)  | Não | Não |
| `408` (timeout da solicitação)  | Não | Sim |
| `429` (limite de taxa)  | Não | Sim |
| `Outros 4XX` (erro do cliente)  | Não | Não |
| `5XX` (erro do servidor)   | Não | Sim |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Response codes and retry logic" }

{% alert note %}
A Braze tenta novamente os códigos de status acima até cinco vezes em 30 minutos usando backoff exponencial. Se não conseguirmos alcançar seu endpoint, as novas tentativas podem se estender por um período de 24 horas.<br><br>Cada webhook tem um limite de 90 segundos antes de expirar.
{% endalert %}

Os cabeçalhos de resposta `Retry-After` e de limite de taxa podem afetar quanto tempo a Braze espera antes de uma tentativa **que pode ser repetida** (por exemplo, após `408`, `429` ou `5XX`). Eles não tornam respostas que não podem ser repetidas, como `401`, elegíveis para nova tentativa.

#### Autenticação e credenciais de Conteúdo conectado {#authentication-and-connected-content-credentials}

A solicitação HTTP de webhook de saída não suporta a anexação de [credenciais de Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/#authentication-types) (`:basic_auth` ou `:auth_credentials`) para autenticação no seu endpoint. Em vez disso, defina a autenticação usando **Request headers** no webhook. Para buscar um token ou segredo no momento do envio, você pode colocar uma tag {% raw %}`{% connected_content %}`{% endraw %} em um campo de cabeçalho ou corpo para que o Liquid a resolva antes do envio do webhook.

#### Modelos de webhook salvos e uso em campanhas {#saved-webhook-templates-and-campaign-usage}

A Braze não fornece um relatório integrado que liste todas as campanhas ou etapas do Canvas que fazem referência a um determinado **modelo de webhook salvo**. Para auditar o uso, revise as etapas de webhook que usam a mesma URL e método HTTP, ou entre em contato com o [suporte da Braze]({{site.baseurl}}/support_contact/).

#### Solução de problemas e detalhes adicionais de erros {#troubleshooting-and-additional-error-details}

Para explicações detalhadas, etapas de solução de problemas e orientações sobre como resolver erros específicos de webhook, consulte [Solução de problemas de solicitações de webhook e Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content/). Você também encontrará mais explicações sobre como nosso sistema de detecção de hosts não saudáveis funciona e como a Braze fornece notificações de erro por meio de e-mails automatizados e registro adicional no Braze Currents.

### Lista de permissões de IP {#ip-allowlisting}

Quando um webhook é enviado pela Braze, os servidores da Braze fazem solicitações de rede para nossos clientes ou servidores de terceiros. Com a lista de permissões de IP, você pode verificar que as solicitações de webhook estão vindo da Braze, adicionando uma camada de segurança.

A Braze enviará webhooks a partir dos seguintes IPs. Os IPs listados são adicionados automática e dinamicamente a quaisquer chaves de API que tenham optado pela lista de permissões.

{% alert important %}
Se você está fazendo um webhook Braze-para-Braze e usando lista de permissões, você deve incluir todos os IPs a seguir na lista de permissões, incluindo `127.0.0.1`.
{% endalert %}

{% multi_lang_include data_centers.md datacenters='ips' %}