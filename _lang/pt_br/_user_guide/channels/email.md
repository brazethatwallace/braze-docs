---
nav_title: E-mail
article_title: E-mail
page_order: 3
page_type: landing
description: "Crie campanhas de e-mail personalizadas na Braze com o editor de arrastar e soltar, editor de HTML, gerenciamento de inscrições e muito mais."
channel:
  - email
search_rank: 2
---

# E-mail {#email}

> Com o e-mail na Braze, você cria mensagens de e-mail personalizadas em Campaigns ou Canvas que alcançam os usuários fora do seu app ou site. Este hub aborda configuração de e-mail, editores de arrastar e soltar e HTML, gerenciamento de inscrições, modelos e testes para que você lance programas de e-mail em conformidade e alinhados à sua marca. Use modelos de e-mail da Braze ou HTML personalizado para combinar com a voz e o layout da sua marca. Comece pela [Configuração de e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup) se estiver configurando um novo domínio de envio. Para ver exemplos de campanhas de e-mail, consulte os [estudos de caso](https://www.braze.com/customers/) da Braze.

## Pré-requisitos {#prerequisites}

Antes de enviar e-mails com a Braze, você precisa configurar seus IPs dedicados, domínios, autenticação de e-mail e aquecimento de IP. Para um passo a passo completo, consulte [Configuração de e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup).

## Personalize seus e-mails {#customize-your-emails}

Você pode personalizar o envio de mensagens por e-mail de diversas maneiras, incluindo:

- [Modelos de e-mail da Braze]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template)
- [Modelos de HTML personalizados]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template)
- [Blocos do editor (e-mail)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email)
- [Inscrições de usuários]({{site.baseurl}}/user_guide/channels/email/subscriptions)
- [Grupos de inscrições]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)

## Teste seus e-mails {#test-your-emails}

[Grupos de teste]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups) enviam automaticamente cópias das suas Campaigns de e-mail para usuários internos, permitindo realizar verificações de controle de qualidade. Os e-mails de teste incluem `[SEED]` no início da linha de assunto para facilitar a identificação.

## Casos de uso {#use-cases}

| Caso de uso | Explicação |
| --- | --- |
| Reengajamento | Alcance usuários fora do seu app, incluindo aqueles que não instalaram o app. |
| Integração | Integre e incentive novos usuários a ativar notificações por push ou compartilhar o app em redes sociais. |
| Mensagens ricas | Permita mensagens HTML ricas e dinâmicas. |
| Conteúdo multimídia | Facilidade na inserção de conteúdo multimídia que engaja os usuários, como vídeos e imagens. |
| Newsletters | Envie newsletters mensais ou semanais de forma prática para manter o engajamento dos usuários. |
| Transações | Notifique os usuários sobre compras recentes e entregue informações importantes sobre produtos e envio com [e-mails de transação]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email).
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

## Serviços de e-mail {#email-services}

Se você precisar de suporte adicional para o seu programa de e-mail, a Braze oferece serviços recorrentes e pontuais com custo adicional. Para saber mais, entre em contato com o gerente da sua conta na Braze.

### Serviços de entregabilidade de e-mail {#email-deliverability-services}

A Braze oferece dois níveis de suporte recorrente para e-mail:
1. Deluxe
2. Standard

Esses serviços podem incluir:

- Auditoria das práticas históricas e atuais de envio de e-mail, com revisão de estratégias de direcionamento, cadência e envio de mensagens
- Configuração de lista de permissões e plano personalizado de aquecimento de IP criado por um especialista em entregabilidade de e-mail
  - Chamadas regulares de acompanhamento durante o primeiro mês (três vezes por semana para Deluxe e uma vez por semana para Standard)
- Chamadas regulares com o especialista em entregabilidade (duas vezes por mês para Deluxe e mensalmente para Standard) para fornecer:
  - Monitoramento do desempenho de entregabilidade por domínio
  - Recomendações para melhorar o desempenho e os resultados do programa de e-mail utilizando dados e melhores práticas estabelecidas
- Atenuar e remediar a triagem de crise para eventos que levam a problemas como inclusão em lista de bloqueio de entregabilidade

## Perguntas frequentes {#frequently-asked-questions}

### Como configuro o envio de e-mail na Braze? {#how-do-i-set-up-email-sending-in-braze}

Configure IPs dedicados, domínios, autenticação e aquecimento de IP antes do seu primeiro envio. Consulte [Configuração de e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup) para ver a lista completa.

### Qual é a diferença entre inscrições de usuário e grupos de inscrições? {#what-is-the-difference-between-user-subscriptions-and-subscription-groups}

As inscrições de usuário controlam o status global de aceitação para um canal (por exemplo, inscrito ou cancelou inscrição de e-mail). Os grupos de inscrições permitem que os usuários escolham categorias específicas de mensagens dentro desse canal. Consulte [Inscrições de usuário]({{site.baseurl}}/user_guide/channels/email/subscriptions) e [Grupos de inscrições]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

### Como posso testar um e-mail antes de enviar uma campanha? {#how-can-i-test-an-email-before-i-send-a-campaign}

Use [grupos de teste]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups) para enviar cópias de prévia a revisores internos e confirmar a renderização em diferentes clientes de e-mail.

## Próximas etapas {#next-steps}

{% article_tiles %}
- name: Configuração de e-mail
  link: /docs/user_guide/channels/email/email_setup
- name: Criar um e-mail com o editor de arrastar e soltar
  link: /docs/user_guide/channels/email/drag_and_drop
- name: Criar um e-mail com o editor de HTML
  link: /docs/user_guide/channels/email/html_editor
{% endarticle_tiles %}