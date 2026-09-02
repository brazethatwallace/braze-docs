---
nav_title: Wunderkind
article_title: Wunderkind (Signals)
description: "Este artigo de referência aborda a integração do Wunderkind Signals com a Braze, incluindo sinais comportamentais que disparam jornadas no Canvas, configuração com a API or interface de programação do aplicativo (API) de entrada do Canvas, a carga útil de contexto do Canvas na entrega disparada por API or interface de programação do aplicativo (API) e relatórios."
alias: /partners/wunderkind/
page_type: partner
search_tag: Partner

---

# Wunderkind (Signals)

> [Wunderkind](https://www.wunderkind.co) é uma plataforma de desempenho para eCommerce que usa tecnologia proprietária de identidade para reconhecer visitantes anônimos de sites e resolvê-los em endereços de e-mail acionáveis. Em média, a Wunderkind aumenta a identificação de 3 a 5% do tráfego do site para 40 a 60%, permitindo que as marcas disparem mensagens personalizadas, um a um, em escala por meio do provedor de serviços de e-mail existente.

*Esta integração é mantida pela Wunderkind. Para suporte, acesse [support.wunderkind.co](https://support.wunderkind.co).*

## Sobre a integração {#about-the-integration}

A integração Wunderkind Signals permite que sinais comportamentais de alta intenção — como abandono de carrinho, abandono de produto e quedas de preço — disparem jornadas Canvas em tempo real na Braze. O Wunderkind identifica usuários anônimos no seu website, resolve a identidade deles para um endereço de e-mail válido para entrega e envia uma carga útil de sinal estruturada para a Braze por meio da API or interface de programação do aplicativo (API) de entrada do Canvas, iniciando seus fluxos de e-mail pré-configurados automaticamente.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Wunderkind | É necessária uma conta Wunderkind com Signals ativado. Entre em contato com seu representante Wunderkind para confirmar a elegibilidade. |
| Conta Braze | É necessária uma conta da Braze com acesso ao Canvas. A equipe da Wunderkind precisa receber um acesso na sua conta. Para todos os detalhes, consulte [Conceder acesso da Wunderkind à sua conta Braze](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account). |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Você cria uma chave de API or interface de programação do aplicativo (API) dedicada com permissões específicas durante a configuração (consulte a [Etapa 1](#step-1-create-a-braze-api-key-for-wunderkind)). |
| Identificação do usuário | A Wunderkind normalmente resolve um consumidor na Braze usando `user_alias` com `alias_label: "wknd_email_id"` (frequentemente com o e-mail como `alias_name`). Cada destinatário de [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) deve incluir exatamente um entre `external_user_id`, `user_alias`, `braze_id` ou `email` ([objeto recipients]({{site.baseurl}}/api/objects_filters/recipient_object)); se você usar `email`, inclua [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers). Ao usar `user_alias`, o perfil já deve existir na Braze antes do disparo. Crie ou atualize usuários e aliases primeiro com [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ou [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify). Para saber mais, consulte [Limitações](#limitations). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Como funciona {#how-it-works}

Quando a Wunderkind identifica um usuário anônimo com alta intenção e resolve a identidade dele, ela envia uma carga útil de sinal para a Braze usando o endpoint `/canvas/trigger/send`, disparando a jornada Canvas relevante para esse usuário em tempo real.

Para uma visão geral técnica completa, consulte o [Portal do Desenvolvedor Wunderkind](https://developer.wunderkind.co/docs/integration-overview).

## Integração {#integration}

### Etapa 1: Criar uma chave de API or interface de programação do aplicativo (API) da Braze para o Wunderkind {#step-1-create-a-braze-api-key-for-wunderkind}

No dashboard da Braze:

1. Acesse **Configurações** > **Chaves de API or interface de programação do aplicativo (API)** e clique em **Criar nova chave de API or interface de programação do aplicativo (API)**.
2. Dê à chave um nome descritivo (por exemplo, `Wunderkind Signals`).
3. Conceda as permissões listadas em [Conceder ao Wunderkind acesso à sua conta da Braze](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account).
4. Copie a chave de API or interface de programação do aplicativo (API) para inseri-la na plataforma Wunderkind na próxima seção.

{% alert note %}
Para o Wunderkind Signals, as solicitações da [REST or transferir estado representacional API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics) da Braze são autenticadas com uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional, e não com tokens OAuth. Crie uma chave de API or interface de programação do aplicativo (API) dedicada no dashboard e forneça essa chave ao Wunderkind.
{% endalert %}

### Etapa 2: Conectar a Braze à plataforma Wunderkind {#step-2-connect-braze-to-the-wunderkind-platform}

1. Faça login na plataforma Wunderkind e acesse o **Integrations Hub**.
2. Selecione o bloco **Braze** e depois selecione **Connect**.
3. Insira sua chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze e selecione seu cluster.
4. Selecione **Save**.

### Etapa 3: Revisar os novos ativos da Braze {#step-3-review-new-braze-assets}

Após a ativação, o Wunderkind provisiona novos ativos de implementação no seu espaço de trabalho da Braze com base na estratégia alinhada com o seu representante Wunderkind:

| Tipo de ativo | Método de criação do Wunderkind |
| ---------- | -------------------------- |
| Content Blocks | Automático |
| Canvas disparados por API or interface de programação do aplicativo (API) | Serviço gerenciado |
| Tags, atributos personalizados, modelos de link | Serviço gerenciado |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Revisar os novos ativos da Braze" }

### Etapa 4: Concluir a configuração do Canvas {#step-4-complete-canvas-setup}

Para cada Canvas do Signals, crie seus modelos de e-mail usando o editor de arrastar e soltar ou HTML da Braze.

- O Wunderkind preenche os dados de produto e sessão no objeto `context` de cada destinatário em `/canvas/trigger/send` no momento do envio.
- Para instruções detalhadas sobre como usar Liquid com essa carga útil nos seus modelos, consulte [Complete Canvas setup](https://support.wunderkind.co/hc/en-us/articles/47155403143963-Complete-Canvas-Setup) na Central de Ajuda do Wunderkind.

### Etapa 5: Revisar a elegibilidade do Canvas {#step-5-review-canvas-eligibility}

Para cada Canvas do Signals, acesse as configurações de **Target Audience** para revisar o público de entrada padrão e os critérios de saída do Wunderkind.

- Para garantir que você não está enviando mensagens com frequência excessiva aos seus usuários, consulte [Limite de frequência centrado no usuário]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#user-centric-rate-limiting).
- Ajuste as configurações para impedir que os usuários continuem recebendo mensagens do Canvas após realizarem uma compra. Por exemplo, adicione a exceção **Make Purchase**.
- Alguns Canvas do Signals são pré-configurados com filtros de atributos personalizados para que os usuários recebam a mensagem com a maior intenção possível.
- Consulte [Review Canvas eligibility](https://support.wunderkind.co/hc/en-us/articles/47156586245787-Review-Canvas-Eligibility) na Central de Ajuda do Wunderkind para detalhes sobre elegibilidade e prioridade do Canvas.

### Etapa 6: Testar e lançar {#step-6-test-and-launch}

O Wunderkind realiza um QA de ponta a ponta antes da entrada em produção:

- Confirmar que os sinais estão sendo entregues aos Canvas IDs corretos sem erros de API or interface de programação do aplicativo (API).
- Verificar se os campos `context` (nome do produto, imagem, URL) estão sendo preenchidos corretamente nos modelos de e-mail renderizados.
- Consulte [Test and launch Signals for Braze](https://support.wunderkind.co/hc/en-us/articles/47156667414171-Test-and-Launch-Signals-for-Braze) na Central de Ajuda do Wunderkind para instruções sobre como pré-visualizar modelos com produtos simulados do Wunderkind.

Quando o QA for aprovado, seu gerente de implementação do Wunderkind coordena o lançamento em produção com a sua equipe.

## Carga útil de contexto do Canvas {#canvas-context-payload}

O Wunderkind suporta seis tipos de sinal. Cada um entrega um conjunto distinto de chaves e valores dentro do objeto [`context`]({{site.baseurl}}/api/objects_filters/context_object) para aquele destinatário em `/canvas/trigger/send` (consulte [Enviar mensagens do Canvas usando entrega disparada por API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)). O campo `WkPurpose` identifica o tipo de sinal dentro dessa carga útil.

### Campos comuns (todos os tipos de Canvas) {#canvas-types-table}

| Propriedade | Tipo | Descrição |
| -------- | ---- | ----------- |
| `Origin` | String | Sempre `"wunderkind"` |
| `DataOnly` | String | Sempre `"Y"` — indica que o Wunderkind está atuando apenas como camada de dados; a Braze executa o envio |
| `UserType` | String | `"prospect"` ou `"customer"` |
| `WkChannel` | String | Sempre `"email"` para esta integração |
| `WkPurpose` | String | Identificador do tipo de sinal (consulte os valores por Canvas nesta seção) |
| `WKCouponCode` | String | Código do cupom, se aplicável (string vazia se não utilizado) |
| `WKCouponPurpose` | String | Descrição da oferta do cupom (string vazia se não utilizado) |
| `Items` | Array | Array de objetos de produto (consulte os campos de produto nesta seção) |
| `WkOpen` | String | Pixel de rastreamento disponível para fins de relatório |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos comuns (todos os tipos de Canvas)" }

### Campos de item de produto {#product-item-fields}

| Propriedade | Tipo | Descrição |
| -------- | ---- | ----------- |
| `WkCopy` | String | Nome do produto |
| `WkId` | String | ID do produto |
| `WkImageUrl` | String | URL da imagem do produto |
| `WkUrl` | String | URL da página de detalhes do produto |
| `WkPrice` | String | Preço original (apenas Canvas de queda de preço) |
| `WKSalePrice` | String | Preço promocional (apenas Canvas de queda de preço) |
| `WkQuantity` | String | Unidades restantes (apenas Canvas de estoque baixo) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos de item de produto" }

### Campos específicos do Canvas e valores de `WkPurpose` {#canvas-specific-fields-and-wkpurpose-values}

| Tipo de Canvas | Valor de `WkPurpose` | Campos adicionais |
| ----------- | ----------------- | ------------------- |
| Abandono de carrinho | `"cart abandonment"` | `WkCartReplenUrl` — URL para reabastecer o carrinho |
| Abandono de produto | `"product abandonment"` | — |
| Recapitulação de categoria | `"category recap"` | `WkCategoryUrl` — URL da categoria navegada |
| De volta ao estoque | `"back in stock"` | — |
| Queda de preço | `"price drop"` | `WkPrice`, `WKSalePrice` em cada item |
| Estoque baixo | `"low stock"` | `WkQuantity` em cada item |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos específicos do Canvas e valores de WkPurpose" }

### Exemplos de cargas úteis {#example-payloads}

Cada objeto em `recipients` deve incluir exatamente um entre `external_user_id`, `user_alias`, `braze_id` ou `email`. Para saber mais, consulte o [Objeto de destinatários]({{site.baseurl}}/api/objects_filters/recipient_object).

{% alert note %}
Cada exemplo usa **um** identificador de destinatário da Braze. Os seis primeiros usam apenas `user_alias`; o último usa `email` com [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers) apenas. O JSON de exemplo omite a chave `WkChannel` dentro de `context` para que as ferramentas de revisão não confundam seu valor (`"email"`) com o campo `email` de destinatário da Braze. Em produção, inclua `"WkChannel": "email"` em `context` conforme documentado na [tabela de campos comuns (todos os tipos de Canvas)](#canvas-types-table).
{% endalert %}

Os exemplos a seguir usam `user_alias` com `wknd_email_id`, correspondendo à forma como o Wunderkind resolve identidades.

{% details Exemplo de carga útil de abandono de carrinho %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/cart",
        "WkPurpose": "cart abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCartReplenUrl": "https://example.com/cart/replenish",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Exemplo de carga útil de abandono de produto %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Exemplo de carga útil de recapitulação de categoria %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/category",
        "WkPurpose": "category recap",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCategoryUrl": "https://example.com/category",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Exemplo de carga útil de volta ao estoque %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "back in stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Exemplo de carga útil de queda de preço %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "price drop",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkPrice": "49.99",
            "WKSalePrice": "39.99"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Exemplo de carga útil de estoque baixo %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "low stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkQuantity": "1"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Exemplo com identificador de e-mail (alternativo) %}
Se você disparar o Canvas com o campo `email` da Braze em vez de `user_alias`, o destinatário deve incluir apenas `email` e `prioritization` (consulte [Enviar mensagens do Canvas usando entrega disparada por API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)). O objeto `context` é igual aos outros exemplos.

```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "email": "user@example.com",
      "prioritization": ["unidentified", "most_recently_updated"],
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

### Exemplo de uso de Liquid {#example-liquid-usage}

Quando o Wunderkind chama `/canvas/trigger/send`, as chaves e valores que você passa no objeto `context` de cada destinatário se tornam dados de entrada do Canvas. Nas etapas de mensagem, referencie-os com o namespace Liquid `context`. Um exemplo é {% raw %}`{{context.${WkPurpose}}}`{% endraw %}, conforme descrito em [Objeto de contexto do Canvas]({{site.baseurl}}/api/objects_filters/context_object) e [Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step). Nenhuma configuração adicional é necessária além de usar a sintaxe Liquid correta.

Não aninhe tags de saída da Braze dentro da condição da tag `for`. Atribua o array `Items` de `context` a uma variável primeiro e depois faça o loop, conforme descrito em [Usando Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid#use-a-filter-result-in-a-for-loop). A linha `assign` usa o formato de entrada do Canvas da Braze {% raw %}`{{context.${Items}}}`{% endraw %} (consulte [Tags de personalização suportadas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags#summary-of-supported-tags)).

{% raw %}
```liquid
{% assign wk_items = {{context.${Items}}} %}
{% for item in wk_items %}
  <tr>
    <td>
      <a href="{{ item.WkUrl }}">
        <img src="{{ item.WkImageUrl }}" />
        <p>{{ item.WkCopy }}</p>
      </a>
    </td>
  </tr>
{% endfor %}
```
{% endraw %}

---

## Relatórios {#reporting}

A Wunderkind ingere dados de desempenho da Braze usando o **Braze Currents**, que transmite eventos brutos para o Google Cloud Storage. A Wunderkind então normaliza e agrega esses eventos em relação ao sinal de origem para relatórios de atribuição 1:1.

As seguintes métricas estarão disponíveis em breve no dashboard de relatórios da Wunderkind:

| Métrica | Fonte |
| ------ | ------ |
| Envios entregues | Braze Currents |
| Aberturas de e-mail | Braze Currents |
| Cliques | Braze Currents |
| Conversões | Braze Currents (evento definido na configuração) |
| Cancelamentos de inscrição | Braze Currents |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Relatórios" }

## Limitações {#limitations}

- **Sem sincronização de supressão/opt-out.** A supressão deve ser gerenciada nativamente na Braze. Nota: Para clientes existentes da Wunderkind que estão migrando para o Braze Signals, a Wunderkind trabalha com sua equipe para preservar sua configuração atual.
- **Somente canal de e-mail.** O SMS não é suportado atualmente por meio desta integração.
- **O perfil de usuário deve existir antes do disparo do Canvas.** [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) com um destinatário `user_alias` resolve apenas perfis da Braze **existentes** que já possuem esse alias. Você não pode usar `send_to_existing_only` com aliases, e o disparo do Canvas não cria um perfil completamente novo apenas a partir do alias. O usuário deve ser criado ou atualizado e o alias `wknd_email_id` deve ser definido primeiro (por exemplo, usando [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ou [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)). A Wunderkind pode aguardar brevemente após esse upsert para que a Braze termine o processamento antes de disparar o trigger.
- **E-mail como identificador.** Se o disparo do Canvas identifica o destinatário com `email` em vez de `user_alias`, inclua [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers) nesse objeto de destinatário, conforme exigido pela Braze.

## Recursos adicionais {#additional-resources}

- [Central de ajuda Wunderkind — Visão geral do Signals for Braze](https://support.wunderkind.co/hc/en-us/articles/47156898436891-Signals-for-Braze-Overview)
- [Portal do desenvolvedor Wunderkind — Visão geral da integração](https://developer.wunderkind.co/docs/integration-overview)
- [Enviar mensagens do Canvas usando entrega disparada por API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [Objeto de contexto do Canvas]({{site.baseurl}}/api/objects_filters/context_object)
- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)