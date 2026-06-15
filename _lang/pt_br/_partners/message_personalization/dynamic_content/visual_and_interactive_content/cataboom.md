---
nav_title: CataBoom
article_title: CataBoom
description: "Saiba como conectar experiências gamificadas da CataBoom à Braze usando Catapult, Request Unique URLs e Conteúdo conectado."
alias: /partners/cataboom/
page_type: partner
search_tag: Partner
---

# CataBoom

> A [CataBoom](https://www.cataboom.com/) é uma plataforma de gamificação. As marcas a utilizam para criar e lançar experiências digitais interativas, incluindo jogos de girar para ganhar, quizzes e jogos de prêmio instantâneo. Essas experiências aprofundam o engajamento e coletam dados primários.

*Essa integração é mantida pela CataBoom.*

## Sobre esta integração {#about-this-integration}

Use a integração da Braze com a CataBoom para adicionar links de jogos personalizados às suas mensagens. Você pode passar identificadores e atributos de usuários entre campanhas do Catapult e a Braze em tempo real. Depois, você pode alimentar Campaigns personalizadas, gatilhos e jornadas de acompanhamento com esses dados.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisa do seguinte:

| Pré-requisito | Descrição |
| --- | --- |
| Conta Catapult | Uma conta Catapult é necessária para usar esta integração. |
| Chave da API REST da Braze (opcional) | Se você usar webhooks do Catapult, precisará de uma chave da API REST da Braze com as permissões de dados de usuários que seu caso de uso exige. Crie a chave na Braze em **Configurações** > **APIs e identificadores** > **Chaves de API**. |
| Endpoint REST da Braze (opcional) | Se você usar webhooks do Catapult, use a URL do endpoint REST que corresponde à URL da Braze para [sua instância da Braze]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Etapa 1: Crie sua experiência de jogo {#step-1-create-your-game-experience}

Crie sua experiência de jogo na plataforma Catapult. As etapas a seguir mostram uma configuração simples de roleta que usa a API Request Unique URL na página **Link Configuration**. A CataBoom oferece mais de 200 opções de jogos, incluindo mecânicas baseadas em sorte, mecânicas baseadas em habilidade e utilitários como cartões de fidelidade e colete-e-ganhe. Você pode seguir um fluxo semelhante para outros tipos de jogos. Para saber mais sobre a CataBoom e o Catapult, acesse [o site da CataBoom](https://www.cataboom.com).

1. Crie a campanha.

Selecione **New Campaign** no canto superior direito. Insira um nome para a campanha, escolha um slug de URL e selecione a categoria e o tipo do jogo.

![Formulário New Campaign do dashboard da CataBoom com campos de nome da campanha, URL, categoria do jogo e tipo do jogo.]({% image_buster /assets/img/cataboom/new_campaign.png %})

{: start="2"}
2. Ative a API Request Unique URL.

No menu à esquerda, selecione **Link Configuration**.

Na página **Link Configuration**, ative **Request Unique URL API**. Essa opção cria uma URL de sistema para sistema que você pode usar posteriormente na Braze, como em um cartão de conteúdo.

![Página Link Configuration da CataBoom com Request Unique URL API ativada e a URL da API visível.]({% image_buster /assets/img/cataboom/link_configuration.png %})

{: start="3"}
3. Defina o rastreamento de jogadas como Account ID.

No menu à esquerda, selecione **Play Control**.

Na página **Play Control**, em **Play Tracking**, defina **Play Count Tracked By** como **Account ID Parameter**.

Você pode passar um Account ID para cada jogador para rastreamento, limites de jogadas, webhooks e outros comportamentos específicos do jogador. Outros sistemas costumam chamar o Account ID de member ID, player ID, loyalty ID ou um nome semelhante.

![Página Play Control da CataBoom com Play Count Tracked By definido como Account ID Parameter.]({% image_buster /assets/img/cataboom/play_control.png %})

Agora você tem o suficiente configurado para executar um teste na Braze. As etapas opcionais abaixo completam uma configuração típica de jogo completo. O Catapult também oferece muitas outras configurações que você pode usar para personalizar a jogabilidade.

{: start="4"}
4. Adicione seus criativos (opcional).

No menu à esquerda, selecione **Creative**.

Faça upload dos seus ativos. O Catapult oferece controle total de branding para sua experiência de jogo.

![Página Creative da CataBoom com ações de download e upload de gráficos e uma pré-visualização do jogo.]({% image_buster /assets/img/cataboom/creative.png %})

{: start="5"}
5. Configure os prêmios para jogos baseados em sorte (opcional).

No menu à esquerda, selecione **Summary**.

Na página **Summary**, expanda **Prize Options**.

O Catapult suporta prêmios por tempo, prêmios por probabilidade ou ambos. Para configurá-los, use **Timed Prizes and Codes**, **Prize Control and Odds Setup** ou ambos, conforme necessário.

As capturas de tela a seguir mostram **Prize Options** no resumo da campanha e uma configuração simples de probabilidade com 50% de chance de ganhar no nível 1.

![Página Summary da CataBoom com a seção Prize Options expandida.]({% image_buster /assets/img/cataboom/prize_options_summary.png %})

![Página Odds da CataBoom com níveis de prêmio, porcentagens e controles de nível.]({% image_buster /assets/img/cataboom/prize_odds.png %})

## Etapa 2: Crie uma mensagem na Braze {#step-2-create-a-message-in-braze}

Este exemplo mostra como criar um **cartão de conteúdo** que usa a Request Unique URL da página **Link Configuration**.

1. Adicione Conteúdo conectado para a URL de jogada.

No seu cartão de conteúdo, adicione texto e conteúdo dinâmico conforme necessário. Envolva sua Request Unique URL da CataBoom em uma tag de [Conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/). Adicione um parâmetro de consulta `AccountID` que use uma tag de personalização da Braze correspondente ao identificador que você usa no Catapult. O exemplo usa {% raw %}`{{${user_id}}}`{% endraw %}.

Substitua a URL base e os parâmetros de consulta `username` e `password` pelos valores da página **Link Configuration** da sua campanha no Catapult.

{% raw %}
```liquid
{% connected_content https://secure.cataboom.com/dplayurl/YOUR_CAMPAIGN_SLUG?username=YOUR_API_USERNAME&password=YOUR_API_PASSWORD&AccountID={{${user_id}}} :save result %}
```
{% endraw %}

Use o `result` salvo no seu cartão (por exemplo, como a URL do link ou no corpo da mensagem). Siga o formato de resposta da API da CataBoom para sua campanha. Para saber mais sobre parâmetros de consulta e Liquid em URLs, consulte [Fazendo uma chamada de API]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/).

![Criador de cartão de conteúdo da Braze mostrando Conteúdo conectado no campo de mensagem e uma pré-visualização mobile do cartão.]({% image_buster /assets/img/cataboom/braze_content_card.png %})

O Conteúdo conectado solicita um link de jogada único quando o usuário abre o cartão de conteúdo. Você pode adicionar outros parâmetros de consulta para experiências mais personalizadas.