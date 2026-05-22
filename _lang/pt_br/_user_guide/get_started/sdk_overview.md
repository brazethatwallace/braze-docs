---
nav_title: Visão geral do SDK
article_title: Visão geral do SDK
page_order: 9
page_type: reference
description: "Este artigo de referência aborda os conceitos básicos do SDK da Braze."
---

# Visão geral do SDK {#sdk-overview}

> O SDK da Braze coleta dados de sessão, identifica usuários e registra compras e eventos personalizados por meio do seu site ou app. Você também pode usar o SDK para engajar usuários enviando **In-App Messages** e notificações por push diretamente do dashboard da Braze.

Em resumo, o SDK da Braze:
* Coleta e sincroniza dados de usuários em um perfil de usuário consolidado
* Captura dados de engajamento de marketing e dados personalizados específicos do seu negócio
* Potencializa as notificações por push, as **In-App Messages** e os canais de envio de mensagens do cartão de conteúdo

## O que é um SDK? {#what-is-an-sdk}
Um kit de desenvolvimento de software (SDK) é um conjunto de ferramentas pré-fabricadas — apenas pequenos blocos de código — que podem ser adicionadas a aplicativos digitais para oferecer suporte a novos recursos. O SDK da Braze é usado para enviar e obter informações de e para seu app ou site. Ele foi projetado para oferecer funcionalidades essenciais desde o início: criação de perfis de usuário, registro de eventos personalizados, disparo de notificações por push, etc.

Como essa funcionalidade vem por padrão da Braze, seus desenvolvedores ficam livres para se concentrar no seu negócio principal. Sem um SDK, cada cliente da Braze teria que criar toda a infraestrutura e as ferramentas para processamento de dados, lógica de segmentação, opções de entrega, tratamento de usuários anônimos, análise de Campaigns e muito mais completamente do zero. Isso levaria muito mais tempo e seria muito mais trabalhoso do que a hora ou mais que leva para incorporar nosso SDK.

## Implementação {#implementation}

Para incorporar um SDK no seu app ou site, alguém precisará adicionar o código do SDK à base de código geral que alimenta o aplicativo. Isso significa que a sua equipe de engenharia estará envolvida, essencialmente unindo nossos apps para que as informações e ações fluam entre eles. Mas, embora seus desenvolvedores estejam envolvidos, o SDK foi projetado para ser leve e de fácil integração.

Para economizar seu tempo e garantir uma integração tranquila, recomendamos que você e sua equipe de engenharia configurem seus eventos personalizados, atributos personalizados e o SDK ao mesmo tempo. Saiba mais sobre as etapas que as equipes de marketing e engenharia precisarão pensar juntas lendo nosso [artigo sobre implementação]({{site.baseurl}}/user_guide/get_started/integrations/).

## Agregação de dados {#data-aggregation}

O SDK da Braze captura automaticamente dados em nível de usuário, fornecendo métricas essenciais para seu app e base de usuários. Agrupe apps semelhantes em um único espaço de trabalho (por exemplo, versões iOS e Android juntas) para visualizar os dados coletados em diferentes plataformas e construir um panorama completo da atividade do usuário. Consulte o artigo na [página inicial]({{site.baseurl}}/user_guide/analytics/dashboards/home/) para mais informações.

## Envio de mensagens no app {#in-app-messaging}

Use o SDK para redigir e enviar **In-App Messages** diretamente. Você pode escolher mensagens slideup, modal ou em tela cheia com base na sua estratégia de Campaign. Para detalhes de composição, consulte [Criar **In-App Messages**]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/).

![Push exibido em um navegador da web]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Notificações por push {#push-notifications}

As notificações por push são outra ótima opção para engajar seus usuários e são especialmente úteis para lidar com chamadas à ação sensíveis ao tempo. As notificações por push para dispositivos móveis aparecem nos dispositivos dos usuários, e as notificações por push para a web aparecem mesmo quando o site não está aberto. Para informações específicas sobre o uso de notificações por push, consulte nosso [artigo sobre notificações por push]({{site.baseurl}}/user_guide/channels/push/).

Os usuários do seu site ou app precisam fazer opt-in para receber notificações por push. Veja [preparação de push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/) para mais detalhes.

## Regras de segmentação e entrega {#segmentation-and-delivery-rules}

Por padrão, uma Campaign contendo **In-App Messages** será enviada para todas as versões do app nesse espaço de trabalho. Por exemplo, a mensagem será enviada tanto para usuários da web quanto para usuários de dispositivos móveis. Para enviar **In-App Messages** apenas na web ou em dispositivos móveis, você precisará segmentar sua Campaign de acordo, o que é suportado por padrão por meio do SDK da Braze.

Você pode criar um segmento dos seus usuários da web definindo **Apps e sites direcionados** como **Usuários de apps específicos** e, em seguida, selecionar apenas seu site para os **Apps específicos**.

![Página de detalhes do Segment com o app da web em foco]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

Isso permitirá direcionar os usuários com base em seu comportamento de forma inteligente. Se você quisesse direcionar os usuários da web para incentivá-los a baixar seu app móvel, criaria esse segmento como seu público-alvo. Se quisesse enviar uma Campaign de mensagens que incluísse **In-App Messages** no celular, mas não na web, desmarcaria o ícone do seu site no seu segmento.

## Plataformas suportadas {#supported-platforms}

A Braze fornece SDKs para várias plataformas, como Web, Android e Swift. Para a lista completa, consulte o [Guia do Desenvolvedor da Braze]({{site.baseurl}}/developer_guide/home/).