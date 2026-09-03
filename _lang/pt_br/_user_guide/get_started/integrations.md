---
nav_title: Integração
article_title: Visão geral da integração
page_order: 8
page_type: reference
description: "Este artigo de referência aborda brevemente as etapas de integração exigidas de seus engenheiros ou desenvolvedores."
---

# Integração {#integration}

> A integração com a Braze é um processo que vale a pena. Mas você é inteligente. Você está **aqui**. É claro que você já sabe disso. Mas o que você provavelmente não sabe é que você e seus desenvolvedores estão prestes a embarcar em uma jornada juntos que requer conhecimento técnico, planejamento estratégico e comunicação consistente que ajudará na coordenação entre os dois.

{% alert note %}
Note que o conteúdo deste artigo não se aplica a e-mails. Confira na seção de [configuração de e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup).
{% endalert %}

## O lado técnico do processo de integração {#the-technical-side-of-the-integration-process}

Você pode estar pensando: "Meus desenvolvedores são mágicos! Eles podem fazer qualquer coisa, então geralmente eu só deixo com eles!" E provavelmente são e provavelmente podem! Mas não há motivo para você não saber o que eles estão fazendo nos bastidores. Na verdade, ajudaria todo o processo se você soubesse quando intervir com informações e o que procurar quando eles perguntam: "Pode me enviar a chave de API e o endpoint de API?"

Então, o que eles estão fazendo quando integram a Braze com seu app ou site? Que bom que você perguntou!

### Etapa 1: Eles implementam o SDK da Braze {#step-1-they-implement-the-braze-sdk}

O SDK da Braze (SDK) é como enviamos e recebemos informações do seu app ou site. Seus engenheiros estão, essencialmente, conectando nossos apps. Para fazer isso, eles precisam de algumas informações importantes:

* Suas [chaves de API]({{site.baseurl}}/api/basics)
* Seu [endpoint de SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)
  * A Braze não fornece mais endpoints personalizados, então use os endpoints de SDK predefinidos. Se você recebeu um endpoint personalizado pré-existente, aqui você encontra as etapas de configuração envolvidas para integração com [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration#step-5-optional-custom-endpoint-setup), [iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift) e [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#initializing-the-sdk).

Você pode fornecer essas informações diretamente a eles ou pode dar acesso à Braze criando uma conta para eles.

{% alert warning %}
Garanta que você e seus desenvolvedores não alterem de forma desconhecida ou não intencional as credenciais da empresa na Braze, pois isso pode causar problemas durante o processo de implementação ou bloquear o acesso de um ou mais de vocês às suas contas.
{% endalert %}

### Etapa 2: Eles implementam os canais de envio de mensagens desejados {#step-2-they-implement-your-desired-messaging-channels}

A Braze tem muitas opções para entrar em contato com seus usuários, e cada uma requer sua própria configuração ou ajuste para funcionar da maneira que você deseja. É aqui que a comunicação com seus engenheiros se torna essencial.

Informe seus desenvolvedores sobre quais canais você deseja usar para garantir que a implementação seja feita de forma eficiente e na ordem correta.

| Canal | Detalhes |
|---|---|
| In-App Messages | Requer implementação do SDK, bem como etapas específicas do canal. |
| Push | Requer implementação do SDK para fornecer o tratamento adequado de credenciais de mensagens e tokens por push. |
| E-mail | Este é um processo completamente diferente. Confira a seção [Configuração de e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup) para mais detalhes sobre a integração. |
| Content Cards | Para começar com [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards), entre em contato com seu CSM da Braze. |
| SMS e MMS | Confira a seção [Configuração de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending) para mais detalhes sobre a integração. |
| Webhooks | Requer implementação do SDK, bem como etapas específicas do canal. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Eles implementam os canais de envio de mensagens desejados" }

{% alert tip %}
Você pode usar a Braze para criar campanhas de mensagens acessíveis em cada canal. Trabalhe com seus desenvolvedores para garantir que você atenda aos padrões de acessibilidade na sua implementação.
{% endalert %}

### Etapa 3: Eles configuram seus dados {#step-3-they-set-up-your-data}

A Braze não faz apenas uma coisa. Não se trata apenas de enviar e-mails ou enviar push. Trata-se de criar jornadas do cliente personalizadas que são únicas para cada usuário e cliente. As jornadas do cliente são baseadas nas ações deles dentro do seu app ou site, e você decide quais são essas ações! A próxima tarefa dos seus desenvolvedores é garantir que as ações realizadas dentro do seu app ou site sejam capturadas pela Braze.

Então, o que você precisa fazer para fornecer essas informações a eles?

1. Trabalhe com sua equipe de marketing para definir campanhas, objetivos, atributos e eventos que você precisa acompanhar. Defina esses casos de uso e compartilhe com suas equipes.
2. Defina seus requisitos de dados personalizados ([atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events), etc.).
3. A partir daí, discuta como esses dados devem ser rastreados (disparados pelo SDK, etc.).
4. Defina quantos [espaços de trabalho]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces) você precisa. Seus engenheiros precisarão saber como [testar e configurar]({{site.baseurl}}/user_guide/get_started/workspaces) esses espaços de trabalho.

Depois de reunir todas essas informações, compartilhe com seu engenheiro. Ele usará essas informações para implementar seus [dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data). Talvez você até precise [importar alguns usuários]({{site.baseurl}}/user_guide/audience/manage_audience/import_users). Você também deve ficar atento às [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).

### Etapa 4: Eles personalizam com base no que você deseja {#step-4-they-customize-based-on-what-you-want}

Se você quiser recursos como disparo via API e Connected Content, discuta isso tanto com seu contato na Braze quanto com seus desenvolvedores para garantir que você consiga trazer dados que existem fora do seu app e da Braze para suas mensagens.

### Etapa 5: Vocês realizam QA juntos na implementação {#step-5-you-both-perform-qa-on-your-implementation}

Trabalhe junto com seu engenheiro para garantir que tudo esteja funcionando. Envie [mensagens de teste]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages), use nossos [apps de teste para Android]({{site.baseurl}}/developer_guide/references?tab=android) e [apps de teste para iOS]({{site.baseurl}}/developer_guide/references?tab=swift), e verifique cada item antes de começar a enviar!

Temos até instruções específicas para [testar sua integração Android ou FireOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android) e testar [push para iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing).

## Após a implementação {#after-implementation}

Lembre-se de que a linha de chegada da implementação não é também o sinal verde para enviar um milhão de mensagens de uma só vez. Enviar um milhão de pushes pode quebrar seu app se todos os clientes clicarem no mesmo link simultaneamente. Recomendamos discutir qual é a capacidade da sua configuração interna para lidar com solicitações da Braze antes de clicar no botão **Enviar**. Depois, você pode definir seu [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting) com base nisso.

![Logo da comunidade Braze Firebrands]({% image_buster /assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Depois de se sentir confortável usando a Braze, considere se tornar um Braze Firebrand! Com o Braze Firebrands, nossa comunidade de engajamento do cliente, estamos construindo uma comunidade de pessoas inovadoras que usam a Braze para modernizar sua experiência do cliente e marketing. Quer saber mais? [Participe agora](https://brazefirebrands.splashthat.com/).