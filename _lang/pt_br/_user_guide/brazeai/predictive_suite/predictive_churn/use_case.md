---
nav_title: Caso de uso
article_title: "Caso de uso: Reduza o churn com conteúdo oportuno"
description: "Este exemplo mostra como uma marca fictícia usa o Predictive Churn para reduzir proativamente a perda de usuários."
page_type: tutorial
---

# Caso de uso: Reduza o churn com o reengajamento oportuno de conteúdo {#use-case-reduce-churn-with-timely-content-re-engagement}

> Este exemplo mostra como uma marca fictícia usa o Predictive Churn para reduzir proativamente a perda de usuários. Em vez de esperar que o churn aconteça, faça a previsão de quais usuários estão em risco e envie mensagens personalizadas enquanto eles ainda estão ativos.

Vamos supor que Camila é gerente de CRM na MovieCanon, uma plataforma de streaming para filmes independentes, documentários e séries internacionais.

A equipe de Camila identificou uma tendência preocupante: os usuários se inscrevem, assistem a um ou dois filmes e depois desaparecem. Historicamente, eles tentaram enviar um e-mail genérico dizendo "Sentimos sua falta" uma semana depois, mas com uma taxa de conversão de apenas 3%, isso foi muito pouco e muito tarde. A maioria dos usuários não volta a se engajar, e o churn se torna inevitável.

Camila quer mudar isso. Em vez de reagir ao churn depois que ele acontece, ela usa o Predictive Churn para identificar usuários que provavelmente ficarão inativos nos próximos 14 dias — dando à sua equipe a oportunidade de reengajar as pessoas enquanto elas ainda estão ativas.

Este tutorial mostra como Camila:

- Cria um modelo de previsão de churn com base no comportamento do usuário
- Segmenta os usuários por nível de risco
- Cria uma Campaign de reengajamento personalizada para aqueles que estão em maior risco
- Avalia o impacto usando a análise de dados da Campaign

## Etapa 1: Crie um modelo de previsão de churn {#step-1-create-a-churn-prediction-model}

Camila começa modelando o resultado que deseja evitar: usuários se tornando inativos. Para a MovieCanon, churn significa não iniciar uma transmissão dentro de 14 dias — então esse é o comportamento que ela deseja prever.

1. No dashboard da Braze, Camila acessa **Analytics** > **Predictive Churn**.
2. Ela cria uma nova previsão de churn e a nomeia "Risco de churn em duas semanas".
3. Para definir o churn, ela seleciona `do not` e o evento personalizado `stream_started`, que indica engajamento ativo.
4. Ela define a janela de previsão para 14 dias — o que significa que o modelo identificará usuários que provavelmente ficarão 14 dias sem iniciar uma nova transmissão.

![Definição de churn mostrando o churn definido como um usuário que não realizou o evento personalizado "stream_started" nos últimos 14 dias.]({% image_buster /assets/img/ai_use_cases/churn_definition.png %})

{:start="5"}
5. Ela seleciona uma população de previsão que inclui todos os usuários que dispararam eventos relevantes nos últimos 30 dias — fornecendo ao modelo comportamento recente suficiente para aprender.
6. Ela define a programação de atualização da previsão para semanalmente, para que as pontuações permaneçam atualizadas.
7. Ela seleciona **Criar previsão**.

O modelo então inicia o treinamento, analisando comportamentos como sessões recentes, frequência de visualização e interações com o conteúdo para revelar padrões que preveem o abandono. Uma hora depois, Camila recebe um e-mail informando que sua previsão concluiu o treinamento, então ela a abre na Braze e verifica a pontuação de [qualidade da previsão]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics#prediction_quality). Está classificada como "Boa", o que significa que as previsões do modelo provavelmente são precisas e confiáveis. Confiante no desempenho do modelo, ela segue em frente.

## Etapa 2: Segmente os usuários por risco de churn {#step-2-segment-users-by-churn-risk}

Após o modelo concluir o treinamento, a Braze atribui a cada usuário elegível uma [pontuação de risco de churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics#churn_score) entre 0 e 100.

Para determinar um limite inicial para o direcionamento, Camila usa o controle deslizante de população de previsão para visualizar quantos usuários se enquadram em cada faixa de pontuação e qual é a precisão da previsão nesse nível. Ela equilibra cobertura e precisão com base nos verdadeiros positivos esperados. Com base nisso, ela decide direcionar para pontuações de risco superiores a 70.

1. Camila navega até Segments na Braze.
2. Ela cria um [segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) usando o [filtro de pontuação de risco de churn]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#churn-risk-score) e seleciona a previsão de churn que criou:
   - **Provável churn:** Pontuação superior a 70

![Filtragem de segment para usuários com pontuação de risco de churn superior a 70.]({% image_buster /assets/img/ai_use_cases/churn_risk_score.png %})

## Etapa 3: Direcione usuários em risco com conteúdo recorrente de reengajamento {#step-3-target-at-risk-users-with-recurring-re-engagement-content}

Com sua previsão e segment prontos, Camila configura uma Campaign recorrente que alcança automaticamente os usuários que se tornam vulneráveis a cada semana.

1. Camila cria uma Campaign recorrente e ativa o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing), para que cada mensagem seja entregue quando cada usuário individual estiver mais propenso a se engajar, em vez de depender de um dia e horário fixos.
2. Ela direciona para o segment "Provável churn" que acabou de criar.
3. Ela define o evento de conversão da Campaign como o evento personalizado `stream_started`, para rastrear quantos usuários realmente retornam para visualizar o conteúdo.
4. Camila escolhe o e-mail como seu canal principal — ele lhe dá espaço para destacar várias opções de conteúdo personalizado em um formato visualmente rico, sem muita pressão. O e-mail inclui:
   - Uma lista de observação personalizada alimentada por [Recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations), selecionada dinamicamente a partir do catálogo da MovieCanon
   - Uma chamada à ação que leva o usuário diretamente para o app.

Isso garante que, a cada semana, a MovieCanon alcance apenas os usuários que precisam de um empurrãozinho — sem excesso de envio de mensagens, sem suposições.

### Exemplo de e-mail {#example-email}

- **Assunto:** Não deixe esses títulos pendentes
- **Cabeçalho:** Sua próxima grande maratona está esperando
- **Corpo:** Não aperta o play há algum tempo? Não se preocupe — selecionamos algumas opções especialmente para você. De thrillers de suspense a documentários premiados, tem algo aqui com o seu nome escrito.
- **CTA:** Ver mais sugestões

## Etapa 4: Meça o desempenho {#step-4-measure-performance}

Após algumas semanas, Camila verifica a [análise de dados da Campaign]({{site.baseurl}}/user_guide/channels/email/reporting) para avaliar o desempenho da estratégia.

Ela vê:

- *Taxa de abertura:* 31%
- *Taxa de cliques:* 15%
- *Taxa de conversão* (transmissão iniciada em 48 horas): 11%

Em comparação com a antiga Campaign "Sentimos sua falta" (onde as taxas de conversão oscilavam em torno de 3%), esse novo fluxo reduz o churn no grupo-alvo em 28%. Ela analisa o [relatório de funil]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports) para identificar onde os usuários abandonam o processo. Embora as taxas de abertura e cliques sejam altas, ela percebe um leve atrito entre o clique e a conversão — o que a leva a considerar testar o texto da CTA ou experimentar um novo layout.

Para entender o impacto a longo prazo, Camila também rastreia o volume de usuários que entram no segment "Provável churn" semana após semana. Isso a ajuda a avaliar a integridade geral do ciclo de vida e a informar a estratégia de retenção em um nível mais amplo. Por fim, ela revisita a página de [análises de previsão]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics) para sua previsão de churn, a fim de comparar os usuários previstos como churners com os reais — uma verificação útil para garantir que o modelo esteja funcionando conforme o esperado.

Com base nesses insights, Camila planeja fazer testes A/B com linhas de assunto, testar diferentes janelas de tempo e experimentar formatos de conteúdo, como recomendações em estilo carrossel em uma mensagem no app.

Com o Predictive Churn, Intelligent Timing e a personalização baseada em IA, a equipe de Camila não está apenas reagindo ao churn — está se antecipando a ele. E a Campaign dela roda discretamente em segundo plano, alcançando as pessoas certas, no momento certo, com conteúdo que realmente lhes interessa.