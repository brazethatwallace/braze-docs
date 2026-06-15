---
nav_title: Usuários e segmentos
article_title: "Primeiros passos: Usuários e segmentos"
page_order: 2
page_type: reference
description: "Este artigo fornece uma visão geral dos usuários e segmentos, destacando sua importância e como eles podem ser usados para engajar seu público."

---

# Primeiros passos: Usuários e **Segments** {#get-started-users-and-segments}

> Compreender seus usuários e direcioná-los de forma eficaz é crucial para enviar **Campaigns** de marketing personalizadas e direcionadas. Este artigo fornece uma visão geral dos usuários e **Segments**, destacando sua importância e como você pode aproveitá-los para engajar seu público.

## Usuários {#users}

Na Braze, as informações sobre seu público são armazenadas em perfis de usuário. Um [perfil de usuário]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/) é uma coleção abrangente de informações e atributos que descrevem um consumidor individual. Ele serve como um repositório central para armazenar e gerenciar dados relacionados ao comportamento, preferências e detalhes demográficos do usuário.

### Partes de um perfil de usuário {#parts-of-a-user-profile}

Ao entender os perfis de usuário, você pode obter insights sobre seu público e interagir com ele de maneira personalizada e direcionada. O perfil de um usuário contém muitas informações, mas aqui estão algumas das partes principais:

- **Identificador do usuário:** Cada perfil de usuário é identificado de forma única por um ID de usuário, chamado de `external_id`. Esse identificador permite que a Braze rastreie e associe dados de usuários em diferentes canais e dispositivos, fornecendo uma visão unificada das interações de cada usuário com sua marca. Os [perfis de usuários anônimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users/) (usuários que visitam seu site ou app sem fazer login) não têm um `external_id`, mas podem receber [aliases de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users/#assigning-user-aliases) como identificador alternativo.
- [Atributos](#attributes)**:** São informações específicas sobre o usuário, como nome, idade, local ou qualquer outra informação demográfica. Você pode usar esses atributos para segmentar seu público e personalizar seu envio de mensagens.
- [Eventos](#events)**:** São ações que o usuário realiza, como fazer uma compra, clicar em um link ou abrir um app. A Braze rastreia esses eventos para ajudar você a entender o comportamento e o engajamento do usuário. Assim como os atributos, você também pode usar eventos para segmentar e personalizar.
- **Compras:** Esta seção registra o histórico de compras do usuário. É crucial para entender os hábitos e preferências de compra do usuário.
- **Dispositivos:** Esta seção lista os dispositivos que o usuário usou para interagir com sua marca. Pode incluir dispositivos móveis, navegadores web e dispositivos conectados (como wearables e smart TVs).
- **Engajamento:** Esta seção contém informações sobre as interações do usuário com as mensagens que você envia, a quais **Segments** ele pertence, status de inscrição e mais.
- **Histórico de mensagens:** Este é um registro de todas as mensagens que foram enviadas ao usuário pelo respectivo canal de envio de mensagens (como e-mail ou push).

{% alert tip %}
Os SDKs da plataforma Braze coletam automaticamente 27 atributos e eventos diferentes. Usando esses eventos e atributos padrão, você pode criar **Segments** assim que integrar o SDK.
{% endalert %}

### Atributos {#attributes}

Atributos são características ou propriedades específicas associadas a um usuário. Esses atributos ajudam você a segmentar e direcionar os usuários com base em seus traços e interesses únicos. Existem dois tipos de atributos na Braze: atributos padrão e atributos personalizados.

#### Atributos padrão {#standard-attributes}

Os atributos padrão são atributos predefinidos que você pode rastrear com a Braze após integrar o SDK ao seu app. São informações comuns de usuário que a maioria dos apps consideraria úteis, como dados demográficos e de dispositivo. Exemplos incluem:

- Nome
- Sobrenome
- E-mail
- Gênero
- Data de nascimento
- País
- Cidade
- Último uso do app
- Idioma
- Fuso horário

#### Atributos personalizados {#custom-attributes}

[Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) são atributos que você define com base nas suas necessidades específicas de negócios. Eles permitem que você acompanhe informações exclusivas do seu app ou negócio.

Por exemplo, um app de streaming de música pode rastrear atributos personalizados como:

- Gênero favorito
- Número de músicas tocadas
- Assinante premium (Sim/Não)
- Artista favorito

Um app de varejo, por outro lado, pode rastrear atributos personalizados como:

- Tamanho de roupa preferido
- Marca favorita
- Número de compras
- Membro do programa de fidelidade (Sim/Não)

Atributos personalizados oferecem a flexibilidade para coletar e analisar dados que são mais relevantes para o seu negócio. No entanto, eles exigem configuração adicional.

Tanto os atributos padrão quanto os personalizados podem ser usados para segmentar seu público e personalizar suas mensagens de marketing. Por exemplo, você pode enviar uma oferta especial para usuários em uma determinada cidade (atributo padrão) que fizeram mais de 10 compras (atributo personalizado).

### Eventos {#events}

Eventos representam ações ou comportamentos específicos realizados pelos usuários dentro do seu app ou site. Exemplos de eventos podem incluir abertura de app, compras, visualizações de conteúdo ou qualquer outra ação. Ao rastrear e analisar esses eventos, você pode obter insights sobre o comportamento do usuário e padrões de engajamento.

#### Eventos padrão {#standard-events}

[Eventos padrão]({{site.baseurl}}/user_guide/data/activation/events/#standard-events) são eventos predefinidos que a Braze rastreia automaticamente após a integração do SDK no seu app ou site. Alguns exemplos de eventos padrão incluem:

- **Início da sessão:** Este evento é acionado quando um usuário abre o app.
- **Fim da sessão:** Este evento é acionado quando um usuário fecha o app.
- **Compra:** Este evento é acionado quando um usuário faz uma compra dentro do app.
- **Clique em notificação por push:** Este evento é acionado quando um usuário clica em uma notificação por push.

#### Eventos personalizados {#custom-events}

[Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) são eventos que você define com base nas ações específicas que deseja rastrear no seu app ou site. Por exemplo, um app de streaming de música pode rastrear eventos personalizados como:

- Música tocada
- Playlist criada
- Anúncio pulado

Um app de fitness, por outro lado, pode rastrear eventos personalizados como:

- Treino iniciado
- Treino concluído
- Recorde pessoal definido

Eventos personalizados oferecem a flexibilidade para rastrear as ações que são mais relevantes para o seu app e negócio. No entanto, assim como os atributos personalizados, eles exigem configuração adicional.

### Pontos de dados {#data-points}

A Braze usa pontos de dados para ajudar você a definir as informações mais impactantes para o seu negócio. Os pontos de dados são uma parte crucial de como a Braze opera e são usados para faturamento, precificação e, mais importante, personalização e otimização de suas Campaigns de marketing.

Os pontos de dados são consumidos quando os dados do perfil de um usuário são atualizados ou quando ele realiza ações específicas. Essas ações podem incluir iniciar uma sessão, encerrar uma sessão, registrar um evento personalizado ou fazer uma compra. É importante notar que nem todos os dados coletados pela Braze contam como pontos de dados. Por exemplo, dados e eventos coletados por padrão pelos serviços da Braze, como tokens de push, informações do dispositivo e todos os eventos de rastreamento de engajamento de Campaign, como aberturas de e-mail e cliques em notificação por push, não são contados como pontos de dados.

Ao considerar cuidadosamente quais informações rastrear como pontos de dados, você está direcionando os dados de maior impacto para a experiência de seus usuários. Seu gerente de conta da Braze ajudará a recomendar as melhores práticas de dados para atender às suas necessidades.

Acesse nosso artigo dedicado para saber mais sobre [pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points/).

## **Segments** {#segments}

A [segmentação]({{site.baseurl}}/user_guide/audience/segments/) permite que você direcione os usuários com base em suas características e ações demográficas, comportamentais, sociais ou técnicas (ou seja, atributos e eventos). O uso criativo e inteligente da segmentação e automação de envio de mensagens permite que você mova seus usuários de forma contínua ao longo de sua jornada de ciclo de vida do cliente.

Dicas para trabalhar com **Segments**:

- Os **Segments** na Braze são dinâmicos: os usuários estão sempre entrando e saindo dos **Segments**, pois nem sempre se encaixam nos critérios. Os usuários que se enquadram nos critérios de um **Segment** no momento do envio serão os destinatários dessa **Campaign** ou **Canvas**.
    - Se você quiser que seu **Segment** seja estático, você pode usar **Segment Extensions**. **Segment Extensions** (com [regeneração desativada]({{site.baseurl}}/user_guide/audience/segments/segment_extension/#extension-regeneration)) representam seu público como uma única captura no tempo.
- Você não está limitado a usar apenas um filtro por vez. Crie **Segments** granulares e bem ajustados, sobrepondo vários filtros uns sobre os outros.
- Você pode usar as ações ou inações de seus usuários para entender como alcançá-los onde eles desejam interagir com você. Essas ações podem ser eventos personalizados, engajamento com uma **Campaign** ou **Canvas** existente, ou até mesmo uma mensagem específica dentro de um **Canvas**.

### Caso de uso {#use-case}

Suponha que você administre uma loja de roupas online e tenha configurado um fluxo de envio de mensagens para enviar uma série de e-mails aos usuários que adicionaram um item ao carrinho, mas não concluíram a compra. Esse fluxo de carrinho abandonado pode incluir um e-mail de lembrete inicial, um e-mail de acompanhamento oferecendo um desconto e um e-mail de lembrete final.

![]({% image_buster /assets/img/getting_started/segment_example.png %}){: style="max-width:70%" }

Você pode criar um **Segment** de usuários que acionaram o evento personalizado "Adicionou item ao carrinho", mas não acionaram o evento personalizado "Compra concluída". Em seguida, dentro desse **Segment**, você pode identificar ainda mais os usuários que abriram o e-mail de lembrete inicial (engajamento com uma mensagem específica), mas não fizeram uma compra.

![]({% image_buster /assets/img/getting_started/segment_example_breakdown.png %})

Esse **Segment** poderia ser alvo de uma **Campaign** mais agressiva para tentar converter esses usuários em compradores. Por exemplo, você pode enviar a eles uma oferta especial ou uma recomendação personalizada com base nos itens em seu carrinho.

Este é apenas um exemplo de como você pode usar ações e inações de usuários, eventos personalizados e dados de engajamento para criar **Segments** e adaptar suas estratégias de marketing na Braze.