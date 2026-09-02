---
nav_title: Convercus
article_title: Convercus
description: "Este artigo de referência descreve a parceria entre a Braze e a Convercus, uma plataforma de fidelidade e cupons que enriquece a Braze com dados de fidelidade em tempo real e permite que Campaigns da Braze disparem ações de fidelidade na Convercus."
page_type: partner
search_tag: Partner
---

# Convercus

> A [Convercus](https://www.convercus.com/en) é uma plataforma SaaS de fidelidade e cupons que ajuda marcas e varejistas a aumentar a frequência de compra, o valor do carrinho e as taxas de recompra por meio de programas de fidelidade omnicanal e campanhas de cupons personalizadas.

_Essa integração é mantida pela Convercus._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Convercus é bidirecional: os dados de fidelidade fluem para a Braze em tempo real como atributos personalizados, eventos personalizados e compras, e os Canvas e Campaigns da Braze podem disparar ações de fidelidade na Convercus por meio de webhooks. Use o nível do membro sincronizado, o saldo de pontos, as compras e a atividade de cupons em Segments, Liquid e Connected Content. A partir das jornadas da Braze, você também pode atribuir cupons, registrar, acumular e resgatar transações de pontos e atualizar as preferências de inscrição de e-mail na Convercus.

A Convercus hospeda a integração, então você não precisa instalar infraestrutura adicional. Enquanto a maioria dos conectores de fidelidade só envia dados em uma direção, a Convercus fecha o ciclo: reaja na Braze a um evento de fidelidade, execute uma ação na Convercus e meça o resultado de volta na Braze.

## Casos de uso {#use-cases}

* **Celebração de subida de nível:** Quando um membro sobe de nível de fidelidade no Convercus, dispare um Canvas personalizado na Braze com uma mensagem de boas-vindas, um benefício exclusivo do nível e o novo nível e saldo de pontos do membro.
* **Bônus de aniversário e marcos:** A partir de uma jornada na Braze, registre pontos de bônus no Convercus no aniversário ou data comemorativa de um membro e envie uma mensagem de celebração confirmando o novo saldo.
* **Recuperação de membros inativos:** Para membros inativos, faça a Braze atribuir um cupom personalizado no Convercus por meio de um webhook e entregue-o por e-mail, push e mensagens no app.
* **Saldo de pontos em tempo real nas mensagens:** Use Connected Content para buscar o saldo de pontos em tempo real de um membro na Braze via Liquid, alimentando cadências como "faltam X pontos para sua próxima recompensa".

## Pré-requisitos {#prerequisites}

Antes de começar, você precisa do seguinte:

| Pré-requisito | Descrição |
| --- | --- |
| Uma conta Convercus | Um programa Convercus ativo. Entre em contato com o gerente de conta da Convercus se você ainda não for cliente. |
| Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com a permissão `users.track`. Crie essa chave no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Um endpoint REST or transferir estado representacional da Braze | [A URL do seu endpoint REST or transferir estado representacional]({{site.baseurl}}/api/basics#endpoints). Seu endpoint depende da URL da Braze para a sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

Você precisa de um identificador de usuário consistente entre os sistemas: o valor usado como `external_id` (ou o tipo de identificador escolhido) na Braze deve corresponder ao identificador de membro correspondente no Convercus. Caso contrário, os eventos não serão atribuídos ao perfil correto.

## Integração {#integration}

### Etapa 1: Configurar a Braze no Convercus Selfservice {#step-1-configure-braze-in-convercus-selfservice}

No Convercus Selfservice (a interface administrativa voltada ao cliente — abra usando a URL fornecida pelo seu gerente de conta Convercus), abra o programa que você deseja conectar à Braze e use o **cartão de integração Braze** para:

1. Configurar a conexão com a Braze preenchendo o formulário de integração:

   | Campo | Descrição |
   | --- | --- |
   | `apiKey` | Sua chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze (com a permissão `users.track`). |
   | `apiEndpoint` | Seu endpoint REST or transferir estado representacional da Braze, por exemplo `https://rest.iad-01.braze.com`. |
   | Tipo de identificador | `external_id` ou `user_alias`. Determina como os membros do Convercus são associados aos perfis de usuário na Braze. |
   | `defaultOptins` | Seleção múltipla dos canais de aceitação do programa (de `membershipOptins`). Usado como padrão para o webhook de inscrição de e-mail quando a solicitação omite `optins`. A configuração da Braze é considerada incompleta até que pelo menos um seja selecionado. |
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 1: Configurar a Braze no Convercus Selfservice" }

2. Criar uma chave de API or interface de programação do aplicativo (API) para chamadas de entrada. Crie uma credencial `X-Convercus-Key` por programa. A chave bruta é exibida uma única vez na criação, com o prefixo `cvc_` (formato: `cvc_<base64url>`). Armazene-a na Braze ao configurar os webhooks de Campaigns e os blocos de Connected Content na Etapa 2. As chaves podem ser revogadas a qualquer momento pelo mesmo cartão; a revogação entra em vigor imediatamente.

Após salvar a conexão com a Braze, o Convercus começa imediatamente a transmitir os eventos de fidelidade daquele programa para a Braze. Nenhuma configuração adicional de infraestrutura é necessária.

{% alert note %}
Cada programa do Convercus é configurado de forma independente. Um único tenant do Convercus pode conectar programas diferentes a espaços de trabalho distintos da Braze, cada um com sua própria chave de API or interface de programação do aplicativo (API).
{% endalert %}

### Etapa 2: Configurar webhooks na Braze {#step-2-configure-webhooks-in-braze}

Para disparar ações do Convercus a partir de um Canvas ou Campaign, crie ações de webhook na Braze que chamem o serviço de integração do Convercus. Todas as solicitações devem incluir os seguintes cabeçalhos:

- `X-Convercus-Key: cvc_…` - a chave de API or interface de programação do aplicativo (API) gerada na Etapa 1.
- `Content-Type: application/json`

Todos os endpoints estão sob a URL base `<SERVICE_HOST>/v1/programs/{programId}`. Substitua `<SERVICE_HOST>` pelo host fornecido pelo seu gerente de conta Convercus e `{programId}` pelo ID do seu programa Convercus.

| Ação | Endpoint |
| --- | --- |
| Atribuir um cupom a um membro | `POST /campaigns/{couponId}/assign` — retorna `{ "couponCode": "..." }`. |
| Atribuir um cupom a vários membros | `POST /campaigns/{couponId}/assign/batch` — até 500 membros em uma única chamada; o corpo aceita `valid_from` / `valid_to` opcionais. Retorna `{ "batchId": "..." }`. |
| Registrar crédito / débito de pontos | `POST /members/{accountId}/bookings` — cria um `EARNBOOKING` ou `BURNBOOKING` na conta de um membro. Retorna `{ "bookingId": "..." }`. |
| Sincronizar preferências de inscrição de e-mail | `POST /subscriptions/email` — define as aceitações do membro como `allowed` ou `declined`. Os canais de aceitação são resolvidos na ordem: `optins` da solicitação > `defaultOptins`. Retorna `200` (tudo OK), `207` (parcial — veja `succeeded` / `failed`) ou `400` (aceitações desconhecidas ou nenhuma configurada). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Configurar webhooks na Braze" }

Exemplo — atribuir um cupom a um membro:

{% raw %}
```text
POST <SERVICE_HOST>/v1/programs/{programId}/campaigns/{couponId}/assign
X-Convercus-Key: cvc_…
Content-Type: application/json

{
  "account_id": "{{custom_attribute.${convercus_account_id}}}",
  "braze_campaign_id": "{{campaign.${api_id}}}"
}
```
{% endraw %}

As outras ações seguem o mesmo padrão, alterando apenas o endpoint e o corpo. Por exemplo, um registro de pontos envia para `/members/{accountId}/bookings` com `booking_type` (`EARNBOOKING` ou `BURNBOOKING`), `booking_type_code`, `points` e `reason`; o webhook de inscrição de e-mail envia para `/subscriptions/email` com `account_id` e `status` (`allowed` ou `declined`).

#### Respostas de erro e tentativas de reenvio {#error-responses-and-retries}

| Status | Significado |
| --- | --- |
| `200` | Sucesso. |
| `207` | Multi-Status — apenas para o webhook de inscrição de e-mail, quando algumas associações foram atualizadas e outras falharam. |
| `400` | O corpo da solicitação falhou na validação. |
| `401` | `X-Convercus-Key` está ausente ou é inválido. |
| `5xx` | A chamada upstream ao Convercus falhou. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Respostas de erro e tentativas de reenvio" }

{% alert warning %}
Respostas 5xx não são seguras para reenvio sem confirmação de sucesso — essas operações não são idempotentes, e tentativas de reenvio podem duplicar a atribuição de cupons ou duplicar créditos de pontos. Desative o reenvio automático da Braze em erros 5xx para esses webhooks, ou configure uma contagem máxima de tentativas muito baixa.
{% endalert %}

### Etapa 3: Verificar os dados na Braze {#step-3-verify-data-in-braze}

1. Dispare um evento de fidelidade no Convercus — por exemplo, uma mudança de nível de status, uma transação de pontos ou um resgate de cupom.
2. Abra o usuário correspondente na Braze e confirme que o atributo personalizado, evento personalizado ou compra esperados aparecem no perfil. Os usuários são associados por `external_id` (ou pelo tipo de identificador escolhido na Etapa 1).
3. Para verificar a direção oposta, faça um envio de teste na Braze que chame um dos webhooks da Etapa 2 e confirme a ação no Convercus (cupom atribuído, pontos registrados ou inscrição atualizada).

## Usando o Convercus com a Braze {#use-convercus-with-braze}

### Etapa 1: Personalize mensagens com dados de fidelidade sincronizados {#step-1-personalize-messages-with-synced-loyalty-data}

Após a integração estar ativa, os eventos do Convercus chegam em cada perfil de usuário na Braze por meio do endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) e podem ser usados como qualquer outro dado nativo:

1. Use atributos personalizados de fidelidade (por exemplo, `convercus_status_level`, `convercus_balance`) em **Segments** para segmentar portadores de nível, membros com saldo alto ou usuários rebaixados recentemente.
2. Use eventos personalizados (por exemplo, `convercus_status_level_changed`, eventos de cupom e associação) como **etapas de disparo** no Canvas ou como filtros em Campaigns de reengajamento.
3. Faça referência a qualquer um desses campos em **Liquid** para personalização nas mensagens (linhas de assunto, corpo do texto, títulos de push).
4. Use eventos `purchase` transmitidos do Convercus para impulsionar jornadas orientadas a produtos (reposição, upsell de categoria, solicitações de avaliação pós-compra).

#### Atributos personalizados {#custom-attributes}

| Atributo | Descrição |
| --- | --- |
| `convercus_account_id` | O ID de conta Convercus do membro — único dentro de um programa Convercus / espaço de trabalho da Braze. |
| `convercus_user_id` | O ID de usuário Convercus que identifica a pessoa subjacente em vários programas Convercus. |
| `convercus_partner_id` | Identificador do parceiro Convercus (lojista/marca) por meio do qual o membro se inscreveu. Útil para segmentação em programas de coalizão. |
| `convercus_member_role` | O papel do membro dentro do programa de fidelidade. |
| `convercus_status_level` | O nível ou status atual do membro. |
| `convercus_balance` | Objeto com os valores atuais de `points`, `lockedPoints` e `statusPoints` do membro. |
| `email_subscribe` | Estado de inscrição de e-mail derivado das aceitações do Convercus (`opted_in`, `subscribed` ou `unsubscribed`). |
| `push_subscribe` | Estado de inscrição de push derivado dos eventos de token por push do Convercus (`opted_in` ou `unsubscribed`). |
| Campos de perfil padrão | `email`, `phone`, `first_name`, `last_name`, `dob`, `gender`, `home_city`, `country`. |
| Propriedades personalizadas do usuário | Quaisquer propriedades personalizadas definidas no objeto de usuário do Convercus são encaminhadas como atributos personalizados da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados" }

{% alert note %}
Dentro de um espaço de trabalho da Braze, os membros são identificados de forma única pelo `convercus_account_id`. O `convercus_user_id` identifica a pessoa subjacente em vários programas Convercus e é fornecido para análise de dados entre programas; para segmentação dentro da Braze, use `convercus_account_id`.
{% endalert %}

**Mapeamento de `email_subscribe`**

| Estado no Convercus | `email_subscribe` na Braze |
| --- | --- |
| Entrada `allowedOptins` para `email consent` ou `newsletter` | `opted_in` |
| Entrada `declinedOptIns` para esses canais (e nenhuma entrada permitida) | `unsubscribed` |
| Sem registro em nenhum dos casos | `subscribed` (padrão neutro da Braze) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados" }

#### Eventos personalizados {#custom-events}

| Evento | Disparado quando |
| --- | --- |
| `convercus_account_created` | Uma nova conta é criada no Convercus. |
| `convercus_membership_added` | Uma conta existente se associa a um programa de fidelidade. |
| `convercus_membership_created` | Uma nova associação é criada. |
| `convercus_membership_changed` | Os dados de uma associação mudam. |
| `convercus_membership_optins_changed` | As preferências de aceitação de um membro mudam. |
| `convercus_membership_terminated` | Uma associação é encerrada. |
| `convercus_status_level_changed` | O nível ou status de um membro muda. |
| `convercus_balance_changed` | O saldo de pontos de um membro muda. |
| `convercus_account_transaction` | Uma transação de fidelidade é processada. |
| `convercus_coupon_assigned` | Um cupom é atribuído ao membro. |
| `convercus_coupon_redeemed` | O membro resgata um cupom. |
| `convercus_user_logged_in` | O membro faz login em uma superfície do Convercus. |
| `convercus_user_logged_out` | O membro faz logout. |
| `convercus_user_created` | Um novo usuário é criado. |
| `convercus_user_changed` | Os dados de perfil de um usuário mudam. |
| `convercus_push_token_created` | Um token por push é registrado para o membro. |
| `convercus_push_token_deleted` | Um token por push é removido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos personalizados" }

#### Compras {#purchases}

As transações do Convercus do tipo `EARNTRANSACTION` (pontos ganhos a partir de gastos do cliente) são reportadas à Braze como [compras]({{site.baseurl}}/api/objects_filters/purchase_object) e contabilizadas na análise de receita, segmentação RFM e recursos preditivos da Braze — usando o ID da transação como identificador do produto e o valor e a moeda da transação como preço e moeda.

Transações do tipo `PAYWITHPOINTSTRANSACTION` (queima de pontos) **não** são reportadas como compras — elas fluem como o evento personalizado `convercus_account_transaction` para que permaneçam disponíveis para segmentação. Estornos e cancelamentos de transações de ganho são reportados como compras com preço negativo, mantendo a receita da Braze alinhada com o Convercus.

### Etapa 2: Busque dados de fidelidade em tempo real com Connected Content {#step-2-fetch-live-loyalty-data-with-connected-content}

Para valores que precisam estar atualizados no momento do envio — saldo de pontos atual, cupons ativos, nível mais recente — chame o Convercus a partir da Braze usando [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) em vez de depender do atributo sincronizado mais recente. Ambos os endpoints ficam sob a mesma URL base dos webhooks e exigem o cabeçalho `X-Convercus-Key`.

| Dados | Endpoint | Retorna |
| --- | --- | --- |
| Perfil do membro | `GET /members/{accountId}/profile` | `member_id`, `first_name`, `last_name`, `email`, `tier_name`, `tier_id`, `points_balance`, `enrollment_date`. |
| Cupons do membro | `GET /members/{accountId}/coupons` | Lista de cupons ativos e resgatáveis (status, valor, janela de validade, título, descrição). Adicione `?lang=<code>` (por exemplo, `?lang=de`) para localizar `title`/`description`; o padrão é `en`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 2: Busque dados de fidelidade em tempo real com Connected Content" }

Os endpoints de Connected Content sempre retornam HTTP 200 em falhas esperadas, para que os templates Liquid possam ramificar com base no campo `error`:

| Resposta | Significado |
| --- | --- |
| `200` + carga útil | Sucesso. |
| `200 { "error": "member_not_found" }` | A conta não existe neste programa. |
| `200 { "error": "internal_error" }` | Falha upstream ou inesperada. |
| `401` | `X-Convercus-Key` está ausente ou inválido (trate no momento da integração, não no Liquid). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Busque dados de fidelidade em tempo real com Connected Content" }

Exemplo — renderizar o status de fidelidade de um membro (nível, pontos e ofertas ativas):

{% raw %}
```liquid
{% connected_content
  https://<SERVICE_HOST>/v1/programs/{programId}/members/{{custom_attribute.${convercus_account_id}}}/profile
  :headers { "X-Convercus-Key": "cvc_…" }
  :content_type application/json
  :cache_max_age 300
  :retry
  :save member
%}

{% connected_content
  https://<SERVICE_HOST>/v1/programs/{programId}/members/{{custom_attribute.${convercus_account_id}}}/coupons?lang=en
  :headers { "X-Convercus-Key": "cvc_…" }
  :content_type application/json
  :cache_max_age 0
  :retry
  :save coupon_data
%}

{% unless member.error %}
  <h2>Your Loyalty Status</h2>
  <p>Hi {{member.first_name}}, you're a <strong>{{member.tier_name}}</strong> member.</p>
  <p>Points balance: <strong>{{member.points_balance}}</strong></p>

  {% if coupon_data.coupons.size > 0 %}
    <h3>Your Active Offers</h3>
    {% for coupon in coupon_data.coupons %}
      <p><strong>{{coupon.title}}</strong> — valid until {{coupon.valid_to}}</p>
    {% endfor %}
  {% endif %}
{% endunless %}
```
{% endraw %}

Sempre envolva o Connected Content em condicionais (verifique `member.error` e `coupons` vazio) para que uma falha temporária de consulta nunca envie uma mensagem quebrada. Armazene em cache o perfil (`cache_max_age 300`), mas não os cupons (`cache_max_age 0`), já que o status dos cupons pode mudar entre os envios.

## Considerações {#considerations}

- **Latência:** Os eventos do Convercus para a Braze são propagados por meio do Kafka e chegam à Braze em segundos sob carga normal.
- **Limites de frequência da Braze:** A integração faz novas tentativas automaticamente em respostas `429`, respeitando o header `x-ratelimit-retry-after` da Braze com backoff exponencial.
- **Cache de Connected Content:** A Braze armazena em cache as respostas de Connected Content por vários minutos por padrão. Para valores que precisam ser exatos no momento do envio (como saldo de pontos), reduza ou ignore a janela de cache na chamada de Connected Content.
- **Uma configuração por programa:** Cada programa de fidelidade é mapeado para um único espaço de trabalho da Braze. Para conectar um segundo espaço de trabalho, configure-o em um programa separado.
- **Observabilidade:** As estatísticas de chamadas de API or interface de programação do aplicativo (API) por programa e o histórico de erros (em ambas as direções) são retidos por 90 dias e estão disponíveis no cartão de integração da Braze no Selfservice.

## Solução de problemas {#troubleshooting}

- **Os eventos não aparecem na Braze:** verifique se o valor usado como identificador (selecionado na Etapa 1) corresponde ao `external_id` (ou tipo de identificador escolhido) do usuário na Braze. Identificadores incompatíveis fazem com que os eventos sejam atribuídos ao perfil errado ou descartados.
- **O webhook retorna `401`:** o cabeçalho `X-Convercus-Key` está ausente ou a chave de API or interface de programação do aplicativo (API) `cvc_…` foi revogada. Regenere a chave no Selfservice e atualize a ação do webhook na Braze.
- **O webhook retorna `400`:** a requisição está sem `Content-Type: application/json`, ou a carga útil não corresponde ao esquema documentado. Para o webhook de inscrição de e-mail, um `400` também significa que as aceitações solicitadas são desconhecidas pelo programa ou nenhuma está configurada.
- **Depuração mais detalhada:** consulte as estatísticas de chamadas de API or interface de programação do aplicativo (API) por programa e o histórico de erros no cartão de integração da Braze no Selfservice, ou entre em contato com seu representante Convercus.