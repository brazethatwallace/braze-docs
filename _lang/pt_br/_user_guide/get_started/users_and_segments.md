---
nav_title: Usuários e segmentos
article_title: "Primeiros passos: Usuários e segmentos"
page_order: 2
page_type: reference
description: "Este artigo fornece uma visão geral dos usuários e segmentos, destacando sua importância e como eles podem ser usados para engajar seu público."
---

# Primeiros passos: Usuários e segmentos {#get-started-users-and-segments}

> Compreender seus usuários e direcioná-los de forma eficaz é crucial para enviar campanhas de marketing personalizadas e direcionadas. Este artigo fornece uma visão geral dos usuários e segmentos, destacando sua importância e como você pode alavancá-los para engajar seu público.

## Usuários {#users}

Na Braze, as informações sobre seu público são armazenadas em perfis de usuário. Um [perfil de usuário]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) é uma coleção abrangente de informações e atributos que descrevem um consumidor individual. Ele serve como um repositório central para armazenar e gerenciar dados relacionados ao comportamento, preferências e detalhes demográficos desse consumidor.

### Partes de um perfil de usuário {#parts-of-a-user-profile}

Ao compreender os perfis de usuário, você pode obter insights sobre seu público e interagir com ele de forma personalizada e direcionada. O perfil de um usuário contém muitas informações, mas aqui estão algumas das partes principais:

- **Identificador do usuário:** Cada perfil de usuário é identificado de forma única por um ID de usuário, chamado de `external_id`. Esse identificador permite que a Braze rastreie e associe dados do usuário em diferentes canais e dispositivos, fornecendo uma visão unificada das interações de cada usuário com sua marca. [Perfis de usuário anônimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) (usuários que visitam seu website ou app sem fazer login) não possuem um `external_id`, mas podem receber [aliases de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#assigning-user-aliases) como um identificador alternativo.
- [Atributos](#attributes)**:** São informações específicas sobre o usuário, como nome, idade, local ou qualquer outra informação demográfica. Você pode usar esses atributos para segmentar seu público e personalizar suas mensagens.
- [Eventos](#events)**:** São ações que o usuário realiza, como fazer uma compra, clicar em um link ou abrir um app. A Braze rastreia esses eventos para ajudar você a entender o comportamento e o engajamento do usuário. Assim como os atributos, você também pode usar eventos para segmentar e personalizar.
- **Compras:** Esta seção registra o histórico de compras do usuário. É essencial para entender os hábitos e preferências de compra do usuário.
- **Dispositivos:** Esta seção lista os dispositivos que o usuário utilizou para interagir com sua marca. Pode incluir dispositivos móveis, navegadores web e dispositivos conectados (como wearables e Smart TVs).
- **Engajamento:** Esta seção contém informações sobre as interações do usuário com as mensagens que você envia, a quais Segments ele pertence, status de inscrição e mais.
- **Histórico de mensagens:** É um registro de todas as mensagens enviadas ao usuário pelo respectivo canal de envio de mensagens (como e-mail ou push).

{% alert tip %}
Os SDKs da plataforma Braze coletam automaticamente 27 atributos e eventos diferentes. Usando esses eventos e atributos padrão, você pode criar Segments assim que integrar o SDK or kit de desenvolvimento de software.
{% endalert %}

### Atributos {#attributes}

Atributos são características ou propriedades específicas associadas a um usuário. Esses atributos ajudam você a segmentar e direcionar usuários com base em suas características e interesses únicos. Existem dois tipos de atributos na Braze: atributos padrão e atributos personalizados.

#### Atributos padrão {#standard-attributes}

Atributos padrão são atributos predefinidos que você pode rastrear com a Braze após integrar o SDK or kit de desenvolvimento de software ao seu app. São informações comuns de usuário que a maioria dos apps consideraria úteis, como dados demográficos e dados do dispositivo. Exemplos incluem:

- Nome
- Sobrenome
- E-mail
- Gênero
- Data de nascimento
- País
- Cidade
- Último app usado
- Idioma
- Fuso horário

#### Atributos personalizados {#custom-attributes}

[Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) são atributos que você define com base nas necessidades específicas do seu negócio. Eles permitem rastrear informações únicas do seu app ou negócio.

Por exemplo, um app de streaming de música pode rastrear atributos personalizados como:

- Gênero musical favorito
- Número de músicas reproduzidas
- Assinante premium (Sim/Não)
- Artista favorito

Um app de varejo, por outro lado, pode rastrear atributos personalizados como:

- Tamanho de roupa preferido
- Marca favorita
- Número de compras
- Membro do programa de fidelidade (Sim/Não)

Os atributos personalizados oferecem flexibilidade para coletar e analisar os dados mais relevantes para o seu negócio. No entanto, eles exigem configuração adicional.

Tanto atributos padrão quanto personalizados podem ser usados para segmentar seu público e personalizar suas mensagens de marketing. Por exemplo, você pode enviar uma oferta especial para usuários em uma determinada cidade (atributo padrão) que fizeram mais de 10 compras (atributo personalizado).

### Eventos {#events}

Eventos representam ações ou comportamentos específicos realizados pelos usuários dentro do seu app ou website. Exemplos de eventos podem incluir abertura do app, compras, visualizações de conteúdo ou qualquer outra ação. Ao rastrear e analisar esses eventos, você pode obter insights sobre o comportamento e os padrões de engajamento dos usuários.

#### Eventos padrão {#standard-events}

[Eventos padrão]({{site.baseurl}}/user_guide/data/activation/events) são eventos predefinidos que a Braze rastreia automaticamente após o SDK or kit de desenvolvimento de software ser integrado ao seu app ou site. Alguns exemplos de eventos padrão incluem:

- **Início de sessão:** Este evento é disparado quando um usuário abre o app.
- **Fim de sessão:** Este evento é disparado quando um usuário fecha o app.
- **Compra:** Este evento é disparado quando um usuário faz uma compra dentro do app.
- **Clique em notificação por push:** Este evento é disparado quando um usuário clica em uma notificação por push.

#### Eventos personalizados {#custom-events}

[Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) são eventos que você define com base nas ações específicas que deseja rastrear no seu app ou site. Por exemplo, um app de streaming de música pode rastrear eventos personalizados como:

- Música reproduzida
- Playlist criada
- Anúncio ignorado

Um app de fitness, por outro lado, pode rastrear eventos personalizados como:

- Treino iniciado
- Treino concluído
- Recorde pessoal registrado

Os eventos personalizados oferecem flexibilidade para rastrear as ações mais relevantes para o seu app e negócio. No entanto, assim como os atributos personalizados, eles exigem configuração adicional.

### Pontos de dados {#data-points}

A Braze usa pontos de dados para ajudar você a definir as informações mais impactantes para o seu negócio. Os pontos de dados são uma parte essencial do funcionamento da Braze e são usados para faturamento, precificação e, principalmente, para personalizar e otimizar suas Campaigns de marketing.

Os pontos de dados são consumidos quando os dados do perfil de um usuário são atualizados ou quando ele realiza ações específicas. Essas ações podem incluir iniciar uma sessão, encerrar uma sessão, registrar um evento personalizado ou fazer uma compra. É importante observar que nem todos os dados coletados pela Braze contam como pontos de dados. Por exemplo, dados e eventos coletados por padrão pelos serviços da Braze, como tokens por push, informações do dispositivo e todos os eventos de rastreamento de engajamento de Campaign, como aberturas de e-mail e cliques em notificações por push, não são contabilizados como pontos de dados.

Ao considerar cuidadosamente quais informações rastrear como pontos de dados, você está direcionando os dados de maior impacto para a experiência dos seus usuários. Seu gerente de conta da Braze ajudará a recomendar as melhores práticas de dados para atender às suas necessidades.

Visite nosso artigo dedicado para saber mais sobre [pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points).

## Segments {#segments}

A [segmentação]({{site.baseurl}}/user_guide/audience/segments) permite direcionar usuários com base em suas características e ações demográficas, comportamentais, sociais ou técnicas (ou seja, atributos e eventos). O uso criativo e inteligente da segmentação e da automação de envio de mensagens permite que você mova seus usuários de forma fluida ao longo da jornada do ciclo de vida do cliente.

Dicas para trabalhar com segmentos:

- Os Segments na Braze são dinâmicos: os usuários estão sempre entrando e saindo dos segmentos, pois nem sempre atenderão aos critérios. Os usuários que atenderem aos critérios de um Segment or segmento or segmento no momento do envio serão os destinatários daquela Campaign ou Canvas.
    - Se você quiser que seu Segment or segmento or segmento seja estático, pode usar as extensões de Segment or segmento or segmento. As extensões de Segment or segmento or segmento (com a [regeneração desativada]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-4-designate-refresh-settings-optional)) representam seu público como um snapshot único em um determinado momento.
- Você não está limitado a usar um filtro por vez. Crie segmentos refinados e granulares combinando vários filtros uns sobre os outros.
- Você pode usar as ações ou inações dos seus usuários para entender como alcançá-los onde eles querem interagir com você. Essas ações podem ser eventos personalizados, engajamento com uma Campaign ou Canvas existente, ou até mesmo uma mensagem específica dentro de um Canvas.

### Caso de uso {#use-case}

Suponha que você tenha uma loja de roupas online e configurou um fluxo de envio de mensagens para enviar uma série de e-mails para usuários que adicionaram um item ao carrinho, mas não concluíram a compra. Esse fluxo de carrinho abandonado pode incluir um e-mail de lembrete inicial, um e-mail de acompanhamento oferecendo um desconto e um e-mail de lembrete final.

![Captura de tela relacionada ao caso de uso.]({% image_buster /assets/img/getting_started/segment_example.png %}){: style="max-width:70%" }

Você poderia criar um Segment or segmento or segmento de usuários que dispararam o evento personalizado "Adicionou item ao carrinho", mas não dispararam o evento personalizado "Compra concluída". Em seguida, dentro desse Segment or segmento or segmento, você poderia identificar ainda mais os usuários que abriram o e-mail de lembrete inicial (engajamento com uma mensagem específica), mas não realizaram a compra.

![Você poderia criar um segmento de usuários que dispararam o evento personalizado "Adicionou item ao carrinho", mas não dispararam o evento personalizado "Compra concluída". Em seguida, dentro desse segmento, você poderia identificar ainda mais os usuários que abriram o e-mail de lembrete inicial (engajamento com uma mensagem específica), mas não realizaram a compra.]({% image_buster /assets/img/getting_started/segment_example_breakdown.png %})

Esse Segment or segmento or segmento poderia ser direcionado com uma Campaign mais agressiva para tentar converter esses usuários em compradores. Por exemplo, você poderia enviar uma oferta especial ou uma recomendação personalizada com base nos itens do carrinho deles.

Este é apenas um exemplo de como você pode usar as ações e inações dos usuários, eventos personalizados e dados de engajamento para criar segmentos e personalizar suas estratégias de marketing na Braze.