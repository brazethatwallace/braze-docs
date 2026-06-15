---
nav_title: Conceitos básicos de campanhas
article_title: Conceitos básicos de campanhas
page_order: 0
page_type: reference
description: "Este artigo de referência aborda os conceitos básicos de campanhas, cobrindo diversas perguntas que você deve se fazer ao configurar suas primeiras campanhas."
tool: Campaigns

---

# Conceitos básicos de campanhas {#campaigns-basics}

> Este artigo de referência aborda os conceitos básicos de campanhas, cobrindo diversas perguntas que você deve se fazer ao configurar suas primeiras campanhas.

## Entendendo a estrutura de uma campanha {#understanding-campaign-structure}

Antes de entrar nos detalhes mais específicos da configuração de campanhas, vamos identificar os pontos-chave para entender como as campanhas funcionam nos diferentes canais de envio de mensagens.

Campanhas são uma etapa de mensagem única para se conectar com seus usuários por meio de canais, mais comumente chamados de canais de envio de mensagens. Esses canais incluem Content Cards, e-mail, mensagens no app, push, SMS e MMS, e webhooks. Ao entender onde seus clientes estão, você pode aproveitar os canais de envio de mensagens mais adequados para se comunicar.

## Construindo a jornada do cliente {#building-the-customer-journey}

Como as campanhas podem ser criadas de formas diferentes dependendo do canal de envio de mensagens, você pode usar os cinco "Ws" da visualização para ajudar a identificar e conceituar suas estratégias e metas de engajamento com o cliente.

### O "o quê": nomeie sua campanha {#the-what-name-your-campaign}

*O que você está tentando ajudar o usuário a fazer ou entender?*

Nunca subestime o poder do nome. A Braze foi criada para colaboração, então este é um excelente momento para alinhar como você vai comunicar os objetivos com sua equipe. Para saber mais sobre jornadas do cliente, confira nosso curso do Braze Learning [Mapping User Lifecycles](https://learning.braze.com/mapping-customer-lifecycles)!

### O "quando": crie condições de início {#the-when-create-starting-conditions}

*Quando um cliente vai encontrar essa campanha?*

Os usuários podem entrar na sua campanha de três formas: em uma data e hora definidas (agendado), quando realizam uma ação específica (baseado em ação) ou quando fazem algo que dispara uma chamada de API (disparado por API).

A entrega agendada envolve ajustar suas campanhas para envio em um horário específico e, opcionalmente, com uma cadência definida. Campanhas baseadas em ação respondem a comportamentos específicos do cliente em tempo real. Isso pode incluir fazer uma compra ou interagir com outra campanha. Campanhas disparadas por API podem ser configuradas para determinar ações-chave do cliente na sua plataforma que, quando realizadas, disparam uma chamada de API para a Braze e enviam suas campanhas.

### O "quem": selecione um público de entrada {#the-who-select-an-entry-audience}

*Quem você está tentando alcançar?*

Você pode usar [segmentos]({{site.baseurl}}/user_guide/audience/segments/) predefinidos para direcionar usuários com base em suas características e ações demográficas, comportamentais ou técnicas. Adicione mais filtros ao criar sua campanha para refinar ainda mais seu segmento. Apenas os usuários que correspondem a esses critérios de público-alvo podem entrar na jornada. Confira esta tabela para um resumo rápido dos tipos de filtro disponíveis.

| Filtro | Descrição |
|---|---|
| Dados personalizados | Segmente usuários com base em eventos e atributos que você define. Pode usar recursos específicos do seu produto. |
| Atividade do usuário | Segmente clientes com base em suas ações e compras. |
| Redirecionamento | Segmente clientes que receberam, visualizaram ou interagiram com campanhas anteriores. |
| Atividade de marketing | Segmente clientes com base em comportamentos universais, como último engajamento ou campanhas recebidas. |
| Atributos do usuário | Segmente clientes por seus atributos e características constantes. |
| Atribuição da instalação | Segmente clientes pela primeira origem, grupo de anúncios, campanha ou anúncio. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### O "por quê": identifique eventos de conversão {#the-why-identify-conversion-events}

*Por que você está criando essa campanha?*

É sempre importante ter um objetivo definido em mente, e as campanhas ajudam você a entender como está o seu desempenho em relação a KPIs como engajamento de sessão, compras e eventos personalizados. Selecionar pelo menos um [evento de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) vai permitir que você entenda o desempenho da sua campanha.

### O "onde": encontre meu público {#the-where-find-my-audience}

*Onde posso alcançar meu público da melhor forma?*

É aqui que determinamos quais canais de envio de mensagens fazem mais sentido para a jornada do seu usuário. O ideal é alcançar seus usuários onde eles são mais ativos.

### O "como": construa a experiência {#the-how-build-the-experience}

*Como construo minha campanha depois de identificar os cinco Ws?*

Considere configurar variantes e testes A/B à medida que você se torna mais experiente na criação de campanhas. As campanhas suportam até oito variantes com um grupo de controle. Use a análise de dados da sua campanha para tomar decisões informadas ao construí-la, ajustando desde o público segmentado até o conteúdo real da mensagem.