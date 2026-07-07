---
nav_title: Consentimento e coleta de endereços
article_title: Consentimento e coleta de endereços
page_order: 6
page_type: reference
description: "Este artigo de referência aborda as práticas recomendadas para a coleta de consentimento e endereços de e-mail de usuários e define os diferentes estados possíveis de assinantes de usuários."
channel: email

---

# Consentimento e coleta de endereços {#consent-and-address-collection}

> Antes de enviar seus e-mails iniciais, é importante obter primeiro a permissão de seus clientes. É uma cortesia comum e faz maravilhas para suas taxas de abertura!

## Estados do assinante {#subscriber-states}

Há três estados de inscrição de e-mail para um usuário: **opted in**, **subscribed** e **unsubscribed**. Para alterar o estado da inscrição de um usuário, consulte nosso artigo sobre [alteração de inscrições]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-subscriptions) ou use nossas [APIs de inscrição]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status).

| Estado do assinante | Descrição |
|---|---|
| Opted In | Esses clientes clicaram no link em um e-mail de confirmação e aceitaram ativamente receber suas mensagens. |
| Subscribed | Por padrão, os usuários são inscritos para receber e-mails desde que tenham um endereço de e-mail válido armazenado em seu perfil. Os usuários permanecem inscritos até que cancelem a inscrição ou façam opt-in. |
| Unsubscribed | Para ser marcado como cancelado, o cliente deve ter cancelado explicitamente a inscrição em seus e-mails ou marcado um e-mail como spam. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados do assinante" }

## Métodos de coleta de endereços {#address-collection-methods}

Além de obter a permissão dos usuários antes do envio de mensagens, existem vários métodos para coletar esses endereços de e-mail que podem impactar sua entregabilidade.

### Listas de endereços compradas {#purchased-address-lists}

Enviar e-mails para listas compradas ou alugadas é uma violação do seu contrato com a Braze! Se você está comprando e-mails, está enviando mensagens totalmente não solicitadas e colocando em risco sua entregabilidade.

### Co-registro {#co-registration}

Co-registro refere-se a um acordo entre empresas para coletar informações de usuários. Este é um método arriscado de coleta. Ele inscreve os usuários para receber e-mails de terceiros, às vezes sem o conhecimento ou permissão do cliente. Se você optar por esse caminho, certifique-se de ter divulgações claras e a possibilidade de cancelar a inscrição no momento da coleta.

### Opt-in pré-selecionado ou forçado {#pre-selected-or-forced-opt-in}

O opt-in pré-selecionado é um método de registro de e-mail no qual a caixa de inscrição já vem marcada para que os assinantes recebam seu e-mail. Ao deixar a caixa marcada, os assinantes estão fazendo opt-in e dando seu consentimento para receber seu e-mail. Esse método tende a irritar as pessoas (e também é ilegal para e-mails enviados para ou dentro do Canadá). Você pode acabar com uma lista de e-mails de tamanho razoável, mas não pode ter certeza de que esses usuários realmente querem seus e-mails de marketing.

### Opt-in simples {#single-opt-in}

O opt-in simples acontece quando os assinantes se inscrevem por meio de um formulário de inscrição e são imediatamente adicionados à sua lista de e-mails. Com esse método, os usuários realizam uma única etapa para se inscrever, como digitar seu endereço de e-mail em um campo de coleta ou marcar uma caixa como parte de uma transação.

### Opt-in confirmado {#confirmed-opt-in}

O opt-in confirmado ocorre quando um usuário marca uma caixa solicitando comunicação por e-mail e uma mensagem de confirmação é enviada em resposta. Esse método permite que os usuários escolham o tipo e a frequência do conteúdo, melhorando o engajamento.

Para garantir que você está direcionando apenas os usuários mais engajados, você também pode usar o método de opt-in com dupla confirmação. Essa abordagem adiciona uma etapa extra na qual o usuário deve clicar em um botão ou link no e-mail de confirmação para ser incluído na lista de e-mails.