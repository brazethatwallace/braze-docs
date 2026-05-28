---
nav_title: Hino Futuro
article_title: Hino Futuro
description: "Este artigo de referência descreve a parceria entre a Braze e a Future Anthem, uma plataforma de IA em tempo real para personalização de apostas esportivas e iGaming."
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# Hino Futuro {#future-anthem}

> A plataforma de IA em tempo real da [Future Anthem](https://www.futureanthem.com/) oferece personalização em esportes, cassino, bingo e loteria. Os clientes da Braze podem enriquecer os perfis de jogadores com atributos específicos do setor, incluindo jogo favorito, time favorito, pontuação de engajamento, recomendação de próxima aposta, próxima aposta esperada e muito mais.
>
> Entregue por meio de experiências em tempo real, públicos dinâmicos e recomendações de conteúdo, cada atributo é construído com base no comportamento ao vivo do jogador, para que os clientes da Braze possam agir no momento certo.

_Essa integração é mantida pela Future Anthem._

{% alert important %}
Este recurso está atualmente em acesso antecipado. Entre em contato com a equipe de sucesso do cliente da Future Anthem para começar.
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Future Anthem | Uma conta da Future Anthem. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissão para o [endpoint `users.track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Você pode criar essa chave no dashboard da Braze em **Settings** > **API Keys**. |
| Endpoint REST da Braze | O [endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) da Braze que corresponde à sua instância, como `rest.iad-01.com`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Casos de uso {#use-cases}

Com essa integração, você pode:

- Identificar jogadores com altas pontuações de engajamento e direcioná-los com ofertas personalizadas, como promoções exclusivas ou recompensas VIP.
- Sugerir jogos semelhantes com base nos jogos que um jogador já gosta.

## Integração {#integration}

A equipe de sucesso do cliente da Future Anthem ajuda você a configurar sua integração. Entre em contato com o seu contato de sucesso do cliente da Future Anthem, e eles ajudarão a identificar os atributos mais relevantes para enviar à Braze.

| Atributos de exemplo na Future Anthem | Atributos de exemplo na Braze |
| ----------------------------------- | --------------------------- |
| ![Dashboard da Future Anthem mostrando atributos de perfil de um jogador.]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %}) | ![Perfil de usuário da Braze mostrando atributos de objeto personalizado sincronizados da Future Anthem.]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integration" }

## Atributos personalizados da Braze {#braze-custom-attributes}

Estes são os atributos personalizados disponíveis na Braze. Para saber mais, consulte [Future Anthem: Primeiros passos](https://knowledge.futureanthem.com/getting-started).

{% tabs local %}
{% tab Bet Recommendations %}

| Subcategoria | Exemplo (JSON) | Tipo de dado |
| ----------- | ---------------- | --------- |
| Preferências do usuário | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}` | Objeto |
| Recomendações de apostas simples | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}` | Objeto |
| Recomendações de apostas acumuladoras (rótulos de eventos) | `{"Bet_1": "Haaland goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}` | Objeto |
| Recomendações de apostas acumuladoras (odds numéricas) | `{"Bet_1": 1.5, "Bet_2": 2}` | Objeto |
| Recomendações de apostas do construtor de apostas | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahawks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}` | Objeto |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}
{% tab Bonus Recommendations %}

| Subcategoria | Exemplo | Tipo de dado |
| ----------- | ------- | --------- |
| NGR (receita líquida de jogos, vitalícia) | 2232 | Número |
| NGR14 (receita líquida de jogos, últimos 14 dias de atividade) | 42 | Número |
| Pontuação de rentabilidade do jogador | 130 | Número |
| Pontuação de engajamento | 0.78 | Número |
| Pontuação de risco de churn | 0.02 | Número |
| Data estimada da próxima aposta | 2024-08-29 | Horário |
| Recomendação de valor de bônus Aposte e Ganhe | 20 | Número |
| Outras recomendações de valor de bônus | 0 | Número |
| CLTV futuro | 3126 | Número |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}
{% tab Game Recommendations %}

| Subcategoria | Exemplo | Tipo de dado |
| ----------- | ------- | --------- |
| Recomendado para você | Fluffy Favourites, Fishin' Frenzy, Big Bass Bonanza, Rainbow Gold, Wild West | Array |
| Jogos favoritos | Fishin' Frenzy | Array |
| Novos jogos recomendados | Sticky Bees, Beware the Deep Megaways, Gold Party, The Flintstones | Array |
| Jogadores como você estão jogando (filtragem colaborativa) | Gold Blitz, Big Bass Splash, Rick and Morty, Book of Dead, Gates of Olympus, Luck O' the Irish | Array |
| Porque você jogou (similaridade de jogo) | Fluffy Favourites 2, Luck O' the Irish Express, Gold Cash, Aztec Treasure Hunt, Stars Bonanza | Array |
| Próximo (sequenciamento de jogo) | Fishin' Frenzy The Big Catch, Big Banker, 9 Masks of Fire, Super Lion, Fishin' Bigger Pots of Gold | Array |
| Jogos populares | Temple of Iris, Fishin' Frenzy, Fishing Reward, Crazy Time, Fluffy Favourites | Array |
| Jogos em alta | Pig Banker, Hyper Gold, Pyramid King, Gold Cash | Array |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}

{% tab Player Cluster %}

| Subcategoria | Exemplo | Tipo de dado |
| ----------- | ------- | --------- |
| Mostra em qual cluster o jogador está | High Value Game Diverse | String |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}

{% tab Player Sustain (risco potencial do jogador) %}

| Subcategoria | Exemplo | Tipo de dado |
| ----------- | ------- | --------- |
| Pontuação de risco | 0.5 | Número |
| Jogador arriscado | True | Booleano |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}
{% endtabs %}