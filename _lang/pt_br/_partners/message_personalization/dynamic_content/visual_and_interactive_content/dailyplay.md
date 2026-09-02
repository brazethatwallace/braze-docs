---
nav_title: DailyPlay
article_title: DailyPlay
description: "Saiba como conectar jogos de marca e recompensas do DailyPlay à Braze para sincronizar dados de gameplay, segmentar públicos e disparar campanhas personalizadas."
alias: /partners/dailyplay/
page_type: partner
search_tag: Partner
---

# DailyPlay

> O [DailyPlay](https://dailyplay.ai/) é uma plataforma de gamificação. Use-o para lançar jogos personalizados de marca e sistemas de recompensas integrados que aprofundam o engajamento e melhoram a retenção.

*Essa integração é mantida pelo DailyPlay.*

## Sobre esta integração {#about-this-integration}

A integração entre a Braze e a DailyPlay permite implantar e acompanhar o desempenho de jogos e recompensas em diferentes Segments de público. Os jogos e sistemas de recompensas da DailyPlay funcionam com o motor de orquestração da Braze para que você possa transformar públicos passivos em participantes ativos.

Você pode enviar marcos de jogabilidade, resgates de recompensas e métricas de engajamento para a Braze para criar Segments de público e disparar envio de mensagens automatizado e integrado entre canais com base no comportamento dentro do jogo. Com esta integração, você pode:

- **Enriquecer perfis de usuário:** Enviar métricas de jogabilidade, pontuações e status de recompensas para perfis de usuário na Braze.
- **Desbloquear segmentação avançada:** Criar Segments de público com base no comportamento dentro do jogo, como melhores pontuadores, vencedores recentes ou usuários prestes a desbloquear uma recompensa.
- **Automatizar campanhas em tempo real:** Disparar mensagens personalizadas integradas entre canais (push, e-mail, mensagens no app) com base em interações no jogo para impulsionar jogabilidade recorrente, fidelidade à marca e maior valor do tempo de vida.

## Casos de uso {#use-cases}

- **Reengajar clientes inativos:** Envie um link para um jogo com chance de ganhar um desconto como recompensa para clientes inativos.
- **Atividade em torno de produtos e tendências:** Crie jogos personalizados que destaquem um novo produto ou uma temporada de festas, tendência ou evento.
- **Implementar jogos direcionados:** Combine a segmentação e o direcionamento da Braze com a personalização do DailyPlay para criar conteúdo de jogo envolvente para diferentes objetivos e resultados.
- **Integração e ativação:** Incorpore um link de jogo DailyPlay do tipo raspadinha ou revelação instantânea na sua série de boas-vindas da Braze para incentivar uma primeira compra ou o preenchimento do perfil.
- **Retenção e fidelidade:** Quando um consumidor atinge um marco de fidelidade ou realiza uma ação-chave rastreada na Braze, dispare um jogo DailyPlay personalizado que celebre sua conquista e desbloqueie recompensas específicas do nível.
- **Prevenção de churn e recuperação:** Identifique usuários que estão se afastando na Braze e, em seguida, entregue um jogo DailyPlay de baixo atrito para recapturar a atenção deles e trazê-los de volta ao seu app ou site.

## Pré-requisitos {#prerequisites}


| Requisito | Descrição |
| --- | --- |
| Conta DailyPlay | Uma conta DailyPlay é necessária para usar esta integração. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões de `users.track`. Crie essa chave na Braze em **Configurações** > **APIs e identificadores** > **Chaves de API**. Para saber mais, consulte [Chaves de API]({{site.baseurl}}/api/basics). |
| Endpoint REST da Braze | A URL do endpoint REST para [sua instância da Braze]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Criar uma conexão {#step-1-create-a-connection}

1. No [dashboard do DailyPlay](https://app.dailyplay.ai/connections), acesse a página **Connections** e selecione **Add Connection**.

![Página de conexões do DailyPlay listando conexões ativas da Braze e estatísticas de disparos.]({% image_buster /assets/img/dailyplay/connections_page.png %}){: style="max-width:70%;"}

{: start="2"}
2. Em **Provider**, escolha **Braze**. Insira um nome, sua chave da API REST da Braze, o App ID e o REST endpoint. Em seguida, selecione **Create Connection**.

![Modal de adição de conexão do DailyPlay com Braze selecionado e campos de credenciais para chave de API, App ID e REST endpoint.]({% image_buster /assets/img/dailyplay/add_connection.png %}){: style="max-width:60%;"}

### Etapa 2: Criar um stream {#step-2-create-a-stream}

Acesse a página **Streams** e crie um novo stream.

1. Adicione a conexão da Braze que você criou na etapa 1 ao novo stream.
2. Configure os eventos-gatilho a serem rastreados, como **Stream Access**, **Play Start**, **Play Complete** e **Prize Redemption**.
3. Crie e adicione jogos ao stream.
4. Copie o código de integração da Braze para o stream.

![Modal de gerenciamento de conexões do DailyPlay mostrando eventos-gatilho da Braze e o código de incorporação para modelos de e-mail da Braze.]({% image_buster /assets/img/dailyplay/manage_connections.png %}){: style="max-width:70%;"}

### Etapa 3: Criar uma campanha na Braze {#step-3-create-a-campaign-in-braze}

Cole o código da etapa 2 na sua campanha na Braze.

Quando os usuários jogam nos streams, o DailyPlay dispara um evento e o envia para a Braze por meio do seu REST endpoint da Braze.

### Etapa 4: Inspecionar ações e expandir seu funil {#step-4-inspect-actions-and-expand-your-funnel}

Os usuários que completam ações nos streams do DailyPlay recebem atributos personalizados e eventos personalizados em seu perfil na Braze.

Crie uma [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) ou um [Canvas]({{site.baseurl}}/user_guide/messaging/canvas) com um disparo [baseado em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) que utilize os eventos personalizados ou atributos personalizados do DailyPlay necessários para o seu caso de uso.

## Use a DailyPlay com a Braze {#use-dailyplay-with-braze}

Para engajar um segmento específico de clientes, siga estas etapas após concluir a configuração da integração.

### Etapa 1: Configurar a DailyPlay {#step-1-set-up-your-dailyplay-configuration}

Siga as etapas de integração nesta seção para configurar a conexão com a Braze e o stream da DailyPlay. Copie o código de integração.

### Etapa 2: Criar uma Campaign ou Canvas na Braze {#step-2-create-a-braze-campaign-or-canvas}

Crie uma Campaign ou Canvas usando um disparo baseado em ação. Selecione os eventos personalizados ou atributos personalizados da DailyPlay necessários para o seu caso de uso.

Você pode usar [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) para referenciar propriedades que a DailyPlay envia no texto da sua mensagem.

**Exemplo de atributo personalizado:**

{% raw %}
```liquid
Your score was {{custom_attribute.${dailyplay}.last_game_score}}
```
{% endraw %}

**Exemplo de evento personalizado:**

Use a notação de ponto para referenciar propriedades no evento-gatilho:

{% raw %}
```liquid
{{event_properties.${dailyplay_play_complete}.properties.score}}
```
{% endraw %}

## Solução de problemas {#troubleshooting}

Para orientações adicionais de configuração e perguntas frequentes, consulte a [documentação de integração DailyPlay com a Braze](https://docs.dailyplay.ai/connections/braze/).