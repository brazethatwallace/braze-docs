---
nav_title: Recuperar usuários inativos
article_title: Recuperar usuários inativos
page_order: 1
page_type: tutorial
description: "Este artigo prático aborda a questão dos usuários inativos e como usar campanhas da Braze de forma eficaz para reengajá-los."
tool:
  - Segments
  - Campaigns

---

# Recuperar usuários inativos {#capture-lapsing-users}

> Se o seu público está diminuindo, é essencial tentar reconquistá-lo. Com a Braze, você pode configurar campanhas automatizadas e recorrentes de reengajamento para recuperar usuários inativos. Você pode escolher o período de reengajamento e a recorrência que melhor se adequam ao seu app, mas, para demonstrar, vamos começar com um plano de reengajamento de 14 dias.

Para saber mais sobre direcionamento de usuários, confira nosso [curso do Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuração de campanhas!

## Etapa 1: Segmentar usuários {#step-1-segment-users}

Primeiro, vamos criar um segmento para direcionar usuários que não usaram seu app nas últimas duas semanas, usando os seguintes filtros:

- **Last Used App** há mais de 2 semanas
- **Last Used App** há menos de 3 semanas

![Captura de tela relacionada à etapa 1: segmentar usuários.]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

Dê ao segmento um nome fácil de lembrar, como "Usuários Inativos – 2 Semanas". Como estamos configurando a campanha para ser recorrente semanalmente, queremos garantir que haja pelo menos uma semana de usuários capturados no segmento. Por isso, selecionamos usuários que usaram o app pela última vez entre duas e três semanas atrás.

## Etapa 2: Criar uma campanha {#step-2-create-a-campaign}

Em seguida, clique em **Criar campanha** e escolha o tipo de campanha que enviaremos para esse segmento. Neste exemplo, vamos criar uma nova [campanha de push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message).

![Em seguida, clique em Criar campanha e escolha o tipo de campanha que enviaremos para esse segmento. Neste exemplo, vamos criar uma nova campanha de push.]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

Vamos nomear a campanha como "Mensagem para Usuários Inativos - 2 Semanas" e então criar o conteúdo da nossa mensagem. Neste exemplo, vamos direcionar apenas usuários iOS, mas você pode usar a Braze para notificações por push no Android e iOS.

Quanto mais próximo da última vez que o usuário esteve no app, mais importante é ser oportuno e relevante. Ao enviar uma mensagem para um usuário após duas semanas sem usar o app, é importante destacar conteúdo relevante e ressaltar os benefícios de usar o app.

![Captura de tela relacionada à etapa 2: criar uma campanha.]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

Em seguida, vamos criar uma programação recorrente para enviar nossa mensagem semanal às quintas-feiras às 17h45 usando a [entrega por fuso horário local]({{site.baseurl}}/help/faqs#what-does-local-time-zone-delivery-offer) nas **Opções de agendamento com base em horário**. Recomendamos que você analise o gráfico de sessões para direcionar os usuários logo antes dos períodos de maior uso. Isso garante que você tente reengajar as pessoas quando elas têm mais probabilidade de usar o app. Você pode alterar isso depois e testar sua hipótese inicial.

![Vamos criar uma programação recorrente para enviar nossa mensagem semanal às quintas-feiras às 17h45 usando a entrega por fuso horário local nas Opções de agendamento com base em horário. Recomendamos que você analise o gráfico de sessões para direcionar os usuários logo antes dos períodos de maior uso. Isso garante que você tente reengajar as pessoas quando elas têm mais probabilidade de usar o app. Você pode alterar isso depois e testar sua hipótese inicial.]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## Etapa 3: Lançar a campanha {#step-3-launch-the-campaign}

Agora, você está pronto para enviar a campanha. Confirme as configurações na última página do criador e clique em **Lançar campanha**!