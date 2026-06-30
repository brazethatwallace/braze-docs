---
nav_title: Caso de uso
article_title: "Caso de uso: Impulsione a descoberta de conteúdo após a visualização"
description: "Este exemplo mostra como uma marca fictícia usa as recomendações de itens de IA da Braze para entregar conteúdo personalizado e sugestões de produtos em momentos-chave do cliente."
page_type: tutorial
---

# Caso de uso: Impulsione a descoberta de conteúdo após a visualização {#use-case-drive-content-discovery-after-viewing}

> Este exemplo mostra como uma marca fictícia usa as recomendações de itens de IA da Braze para entregar conteúdo personalizado e sugestões de produtos em momentos-chave do cliente. Saiba como a lógica de recomendação pode melhorar o engajamento, aumentar as conversões e reduzir o esforço manual.

Vamos supor que Camila é uma gerente de CRM na MovieCanon, uma plataforma de streaming com filmes e séries selecionados.

O objetivo de Camila é manter os espectadores engajados após terminarem de assistir algo. Historicamente, as mensagens "Você também pode gostar" da MovieCanon eram baseadas em correspondência ampla de gênero e enviadas em momentos arbitrários — frequentemente horas ou dias após uma sessão. O engajamento era baixo, e sua equipe sabia que poderiam fazer melhor.

Usando [Recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai), Camila configura um sistema para recomendar automaticamente novos títulos com base no histórico de visualização de cada espectador, entregues imediatamente após um usuário terminar um filme ou episódio. É uma maneira mais inteligente e pessoal de ajudar os usuários a descobrir conteúdo que realmente querem assistir a seguir e mantê-los engajados com a plataforma.

![Mensagem no app dizendo "Próximo, só para você. Porque você assistiu 'Nômades do Sol'", com uma imagem, nome do título, descrição e CTA para "Assistir agora" ou "Pular" para a próxima recomendação.]({% image_buster /assets/img/ai_use_cases/recommendation_rendered.png %})

Este tutorial explica como Camila:

- Cria uma mensagem personalizada acionada quando um usuário termina de assistir algo
- Configura recomendações adaptadas às preferências do espectador — automaticamente retiradas do catálogo da MovieCanon e inseridas na mensagem

## Etapa 1: Criar uma recomendação de IA {#step-1-create-a-churn-prediction-model}

Camila começa criando uma recomendação que mostrará títulos relevantes sempre que um usuário terminar de assistir algo. Ela quer que seja dinâmica, para que os usuários recebam sugestões diferentes com base no que assistiram recentemente.

1. No dashboard da Braze, Camila navega até **Recomendação de item de IA**.
2. Ela cria uma nova recomendação e a nomeia de "Sugestões pós-visualização".
3. Para o tipo de recomendação, ela escolhe **IA Personalizada**, para que cada usuário veja recomendações personalizadas com base em comportamentos passados.
4. Ela seleciona **Não recomendar itens com os quais os usuários já interagiram** para que os usuários não recebam recomendações de algo que já assistiram.
5. Ela seleciona o catálogo contendo a biblioteca de conteúdo atual da MovieCanon. Camila não adiciona uma seleção de catálogo, já que ela quer que todos os itens do catálogo sejam elegíveis para recomendação.
6. Camila vincula a recomendação ao evento personalizado `Watched Content`, que rastreia visualizações concluídas, e define o **Nome da propriedade** como o título do conteúdo.
7. Ela cria a recomendação.

## Etapa 2: Configurar uma mensagem no app {#step-2-set-up-an-in-app-message}

Após a recomendação ter terminado o treinamento, Camila constrói um fluxo de envio de mensagens que alcança o usuário no momento certo: imediatamente após terminar um título. A mensagem inclui uma lista de três sugestões personalizadas retiradas diretamente do catálogo.

1. Camila cria uma Campaign de mensagem no app usando o editor de arrastar e soltar.
2. Ela define o gatilho para seu evento personalizado: `Watched Content`.
3. Ela projeta uma mensagem no app de várias páginas com imagens de título, nomes e um CTA "Assistir agora".

![Modal "Adicionar personalização" aberto no editor da Braze, com "Recomendação de item" selecionado como o tipo de personalização.]({% image_buster /assets/img/ai_use_cases/recommendation_add_personalization.png %})

{: start="4"}

4. No corpo da mensagem, Camila usa o [modal Adicionar personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#inserting-pre-formatted-variables) para adicionar variáveis como o nome, descrição e miniatura do título recomendado usando Liquid, que popula dinamicamente o conteúdo do catálogo. Ela insere um atributo personalizado para `Last Watched Movie` para informar aos usuários que esta recomendação é baseada em seu histórico de visualização.

![Editor de mensagem no app com Liquid bruto para inserir campos específicos dos itens do catálogo a partir da recomendação.]({% image_buster /assets/img/ai_use_cases/recommendation_liquid.png %})

{% details Mostrar o Liquid usado na imagem %}

{% raw %}

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].name }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].description }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].thumbnail }}
```

{% endraw %}

{% enddetails %}

{: start="5"}

5. Camila então duplica sua página e incrementa o array Liquid {% raw %} (`{{ items[0]}}` para `{{items[1]}}`) {% endraw %} em cada variável para inserir o próximo item na lista de recomendações.

## Etapa 3: Medir e otimizar {#step-3-measure-and-optimize}

Com a Campaign ativa, Camila monitora taxas de abertura, CTRs e comportamento de visualização subsequente. Ela compara o desempenho com Campaigns de recomendação estáticas anteriores e observa maior engajamento — e mais sessões de conteúdo por usuário.

Ela também planeja testar A/B:

- Tempo (imediato versus 10 minutos após assistir)
- Layout do conteúdo (carrossel versus lista)
- Variações de CTA ("Assistir agora" versus "Adicionar à fila")

Ao combinar envio de mensagens acionado por eventos com Recomendação de item de IA, Camila transforma a descoberta de conteúdo em uma experiência automática e personalizada. A MovieCanon mantém os usuários engajados sem suposições — entregando conteúdo relevante no momento certo para aumentar a profundidade da sessão e reduzir o churn.