---
nav_title: Webhooks
article_title: Webhooks
page_order: 9
page_type: landing
alias: /about_webhooks/
description: "Conecte seus sistemas com webhooks na Braze, disparados por eventos personalizados para enviar dados e mensagens programáticas a endpoints externos."
channel:
  - webhooks
search_rank: 3
---

# Webhooks {#webhooks}

> Um webhook é uma mensagem automatizada de um sistema para outro após determinados critérios serem atendidos. Na Braze, esse critério geralmente é o disparo de um evento personalizado. Os webhooks oferecem acesso dinâmico e flexível a dados e funcionalidades programáticas, e permitem que você configure jornadas de clientes que otimizam processos.

## Pré-requisitos {#prerequisites}

A disponibilidade de webhooks depende do seu pacote Braze. Entre em contato com seu gerente de conta ou gerente de sucesso do cliente para começar.

## Casos de uso {#use-cases}

Os webhooks são uma excelente maneira de conectar seus sistemas — afinal, webhooks são como os apps se comunicam. Aqui estão alguns cenários gerais em que os webhooks podem ser particularmente úteis:

- Enviar dados de e para a Braze
- Enviar mensagens aos seus clientes por canais não suportados diretamente pela Braze
- Fazer publicações nas APIs da Braze

Alguns casos de uso mais específicos incluem:

- Criar um [fluxo de trabalho de pontuação de leads]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring) usando webhooks e Canvas para qualificar e encaminhar leads.
- Se um usuário cancelar a inscrição de e-mail, você pode usar um webhook para atualizar seu banco de dados de análise de dados ou CRM com essa mesma informação, garantindo uma visão holística do comportamento desse usuário.
- Enviar [mensagens transacionais]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email) para usuários no Facebook Messenger ou LINE.
- Enviar mala direta aos clientes em resposta à atividade deles no app e na web, usando webhooks para se comunicar com serviços de terceiros como [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob).
- Se um jogador alcançar um determinado nível ou acumular uma certa quantidade de pontos, use webhooks e sua configuração de API existente para enviar uma melhoria de personagem ou moedas diretamente para a conta dele. Se você enviar o webhook como parte de uma campanha de mensagens multicanal, poderá enviar um push ou outra mensagem para informar o jogador sobre a recompensa ao mesmo tempo.
- Se você é uma companhia aérea, pode usar webhooks e sua configuração de API existente para creditar a conta de um cliente com um desconto depois que ele reservar um determinado número de voos.
- Infinitas receitas "Se Isto, Então Aquilo" ([IFTTT](https://ifttt.com/about)) — por exemplo, se um cliente fizer login no app por e-mail, esse endereço pode ser configurado automaticamente no Salesforce.

## Tratamento de erros e limite de frequência de webhook {#webhook-error-handling-and-rate-limiting}

A Braze tenta reenviar webhooks apenas para determinadas respostas HTTP (por exemplo, `408`, `429` e `5XX`). A maioria das outras respostas, incluindo `401 Unauthorized` e outros erros `4XX`, não são reenviadas. Cabeçalhos de resposta como `Retry-After` e `X-Rate-Limit-*` podem influenciar o tempo de espera entre tentativas **quando uma resposta já é elegível para reenvio**; eles não fazem com que a Braze tente reenviar erros que estão fora do conjunto de respostas reenviáveis.

Para ver a tabela completa de códigos de resposta, limites de tentativas e comportamento de timeout, consulte [Códigos de resposta e lógica de reenvio]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#response-codes-and-retry-logic).

Se a maioria das solicitações de webhook para um host específico estiver falhando, a Braze suspende temporariamente todas as tentativas de envio para esse host. O envio é retomado após um período de espera definido, permitindo que seu sistema se recupere.

## Usando webhooks com parceiros da Braze {#utilizing-webhooks}

Existem muitas formas de usar webhooks e, com nossos parceiros de tecnologia (Alloys), você pode usar webhooks para elevar o nível da sua comunicação diretamente com seus clientes e usuários.

Confira:
* [Messenger]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/instant_chat/messenger)
* [Remerge]({{site.baseurl}}/partners/remerge)
* [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob)
* E muitos mais dos nossos [parceiros de tecnologia]({{site.baseurl}}/partners/home)!

## Próximos passos {#next-steps}

{% article_tiles %}
- name: Criar um webhook
  link: /docs/user_guide/channels/webhooks/create_a_webhook
  description: Configure webhooks disparados por eventos personalizados e envie dados para endpoints externos.
- name: Criar um webhook Braze-para-Braze
  link: /docs/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook
  description: Faça chamadas para as APIs da Braze a partir de Campaigns e Canvas.
{% endarticle_tiles %}