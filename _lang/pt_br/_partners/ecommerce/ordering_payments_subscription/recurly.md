---
nav_title: Recurly
article_title: Recurly
description: "A Recurly é a principal plataforma de gerenciamento e faturamento de assinaturas para marcas diretas ao consumidor que buscam aumentar suas assinaturas e receitas recorrentes."
alias: /partners/recurly/
page_type: partner
search_tag: partner
---

# Recurly

> A [Recurly](https://recurly.com/) é uma plataforma de gerenciamento de assinaturas e faturamento. A plataforma integrada da Recurly simplifica a automação do ciclo de vida da assinatura em escala, permitindo que as equipes gerenciem e otimizem a experiência do assinante&#8212;desde o teste de novos planos, ofertas e promoções até o gerenciamento de métodos de pagamento, integrações e insights.

_Essa integração é mantida pela Recurly._

## Sobre a integração {#about-the-integration}

A integração entre a Recurly e a Braze simplifica o processo de compartilhamento de dados de assinatura com a Braze, permitindo a comunicação direcionada com os clientes.

- Use os eventos do ciclo de vida da assinatura da Recurly (por exemplo, renovações, pausas ou cancelamentos de assinatura) na Braze para disparar campanhas e comunicações personalizadas.
- Aproveite os dados de assinatura da Recurly (por exemplo, planos de assinatura, complementos ou status) para criar e gerenciar usuários da empresa, segmentos e Canvas para executar campanhas e comunicações específicas de coorte.
- Envie dados da Recurly diretamente para a Braze, possibilitando casos de uso adicionais de envio de mensagens e reduzindo os custos indiretos de desenvolvimento.

Consulte a [documentação da Recurly](https://docs.recurly.com/docs/braze-integration) para saber mais sobre como usar a Recurly com a Braze.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Recurly | Para aproveitar essa parceria, é necessário ter um plano de assinatura Elite da [Recurly](https://recurly.com/) com a Feature Flag da Braze ativada. A ativação de faturas de crédito na sua plataforma da Recurly também é necessária.|
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. Como a Recurly usa apenas o endpoint `users.track`, recomendamos o provisionamento de uma chave específica da Recurly somente com essa permissão. |
| Endpoint REST or transferir estado representacional da Braze | [Sua URL de endpoint REST or transferir estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integração {#integration}

Antes de começar, verifique se você tem contas ativas na Braze e na Recurly.

### Conectar a Recurly à Braze {#connect-recurly-to-braze}

1. Na Recurly, acesse **Integrations** > **Braze**. Ao navegar pela primeira vez na página de configuração da integração da Braze na Recurly, a interface solicitará que você conecte os dois sistemas.

2. Forneça as seguintes credenciais:

- **Instance URL:** O endpoint REST or transferir estado representacional da Braze da instância para a qual você está provisionado.
- **API or interface de programação do aplicativo (API) Key (Identifier):** A chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze que a Recurly deve usar ao enviar solicitações à Braze.

Lembre-se de copiar a URL da sua instância da Braze. Por exemplo, sua URL pode ter a seguinte aparência:

```
<https://dashboard-03.braze.com/dashboard/app_usage?locale=en>
```

{:start="3"}
3. Depois de inserir suas credenciais, clique em **Connect**.

## Usando essa integração {#using-this-integration}

### Identificadores suportados {#supported-identifiers}

A Recurly usa o `account_code` de uma conta como `external_id` na Braze. Por isso, o `account_code` das suas contas da Recurly deve corresponder ao `external_id` do seu usuário da Braze.

### Eventos personalizados {#custom-events}

Para um engajamento eficaz do cliente, você deve [configurar eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) na Braze para receber eventos disparados pela Recurly. Inclua cada evento da Recurly para obter uma integração completa dos dados. Esses eventos também podem ser rastreados na [análise de dados da Braze]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics). Uma vez configurados, esses eventos personalizados podem ser usados para segmentar usuários ou personalizar o envio de mensagens.

| Evento personalizado da Braze | Evento da Recurly |
| ----------- | ----------- |
| Recurly New Subscription              | Disparado quando uma assinatura é criada                            |
| Recurly Renewed Subscription          | Disparado quando uma assinatura é renovada                                |
| Recurly Updated Subscription          | Disparado quando os atributos de uma assinatura mudam (mudança de plano, mudança de preço ou mudança de quantidade) |
| Recurly Canceled Subscription         | Disparado quando uma assinatura é cancelada                           |
| Recurly Reactivated Subscription      | Disparado quando uma assinatura cancelada é reativada               |
| Recurly Paused Subscription           | Disparado quando uma assinatura é definida para ser pausada                   |
| Recurly Resumed Subscription          | Disparado quando a pausa de uma assinatura é removida                              |
| Recurly Subscription Expired          | Disparado quando uma assinatura expira                               |
| Recurly Invoice Created               | Disparado quando uma fatura é criada                                |
| Recurly Successful Payment            | Disparado quando uma fatura é cobrada com sucesso                 |
| Recurly Refund Issued                 | Disparado quando um reembolso é emitido                                   |
| Recurly Failed Recurring Payment      | Disparado quando uma fatura falha para uma renovação de assinatura          |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom events" }

### Loteamento e limite de taxa {#batching-and-rate-limiting}

Como a Recurly usa o endpoint `/users/track` da Braze, a integração está sujeita aos limites de taxa padrão da Braze de 50.000 solicitações por minuto.

A Recurly agrupa determinados eventos do ciclo de vida da assinatura em chamadas únicas à API or interface de programação do aplicativo (API) da Braze para reduzir o número de solicitações.

- A Recurly agrupa e envia várias assinaturas criadas ao mesmo tempo em uma única solicitação.
- A Recurly agrupa várias renovações simultâneas de uma conta em uma única solicitação.
- A Recurly envia eventos do ciclo de vida da assinatura do mesmo modelo em uma única solicitação. Por exemplo, uma fatura recém-criada com um pagamento resulta em uma solicitação de API or interface de programação do aplicativo (API) contendo os eventos personalizados `Recurly Invoice Created` e `Recurly Successful Payment`.

Os lotes são enviados à Braze em grupos de até 75 eventos por vez. Por exemplo, se 100 assinaturas fossem criadas de uma vez, a Recurly faria duas solicitações de API or interface de programação do aplicativo (API) para a Braze. Consulte [como agrupar solicitações de rastreamento de usuários em lote]({{site.baseurl}}/api/api_limits/#batch-user-track) para obter detalhes.