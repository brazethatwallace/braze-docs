---
nav_title: E-mail de transação
article_title: E-mail de transação
page_order: 4
page_type: landing
channel:
  - email
search_rank: 3
description: "Envie e-mails de transação para notificações críticas e urgentes disparadas por chamadas de API na Braze."
---

# E-mail de transação {#transactional-email}

> E-mails de transação são criados especificamente para o envio de mensagens automatizadas e não promocionais, facilitando uma transação acordada entre você e seus clientes. Use campanhas de e-mail de transação na Braze para enviar notificações críticas e urgentes disparadas por chamadas de API, como confirmações de pedido, redefinições de senha e atualizações de envio.

## Pré-requisitos {#prerequisites}

O e-mail de transação está disponível apenas como parte de pacotes selecionados da Braze. Entre em contato com o seu gerente de sucesso do cliente da Braze ou abra um [ticket de suporte]({{site.baseurl}}/braze_support) para mais detalhes.

Antes de começar, certifique-se de que você tem o seguinte:

- [Configuração de e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup) concluída, incluindo configuração de IP e domínio, autenticação e aquecimento de IP
- Uma **chave da API REST da Braze** com a permissão `transactional.send`

## Casos de uso {#use-cases}

O e-mail de transação foi criado para enviar mensagens não promocionais disparadas por serviços. Os casos de uso mais comuns incluem os seguintes:

| Caso de uso | Explicação |
| --- | --- |
| Confirmações de pedido | Confirmar que a compra de um cliente foi recebida e está sendo processada. |
| Redefinições de senha | Entregar links seguros e com prazo de validade para que os clientes redefinam suas credenciais de conta. |
| Notificações de envio | Notificar os clientes quando o pedido foi despachado, incluindo informações de rastreamento e datas estimadas de entrega. |
| Alertas de conta | Enviar notificações críticas relacionadas à conta, como falhas de pagamento, alterações de inscrição ou alertas de segurança. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

## Como o e-mail de transação difere do e-mail de marketing {#how-transactional-email-differs-from-marketing-email}

Os e-mails de transação são enviados por meio de uma [API HTTP transacional]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email) dedicada da Braze, otimizada para velocidade e confiabilidade. Diferentemente dos e-mails de marketing, os e-mails de transação:

- Não exigem que o usuário tenha optado por receber comunicações de marketing
- São disparados por chamadas de API, em vez de disparadores agendados ou baseados em ação
- Oferecem entrega quase em tempo real para conteúdo urgente

## Próximos passos {#next-steps}

- [Criar um e-mail de transação]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email)
- [Rastreamento]({{site.baseurl}}/user_guide/channels/transactional_email/tracking)