---
nav_title: Correlação de conversão
article_title: Correlação de conversão
alias: /conversion_correlation/
page_order: 3

page_type: reference
description: "Este artigo de referência explica a análise de correlação de conversão na página de análise de dados da campanha."
tool: 
  - Reports
  
---

# Correlação de conversão

> A análise de correlação de conversão na página **Análise de dados da campanha** oferece insights sobre quais atributos e comportamentos dos usuários ajudam ou prejudicam os resultados definidos para as campanhas. 

## Visão geral

Para cada campanha, a Braze verifica uma lista de atributos e comportamentos dos usuários e calcula se eles estão estatisticamente associados a aumentos ou diminuições em cada um dos [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) escolhidos para a campanha. Também calculamos o quanto mais ou menos provável é que usuários com determinado atributo ou comportamento convertam e, se for significativo, exibimos essa informação no lado correspondente da tabela. Os usuários com cada atributo ou comportamento de interesse são comparados com as taxas do público total da campanha. Comportamentos e atributos que não apresentam correlação significativa com a conversão não são exibidos na tabela.

Para executar uma análise de correlação de conversão, selecione o evento de conversão desejado no menu suspenso.

![Painel de correlação de conversão mostrando um exemplo com "Selecionar um evento de conversão" definido como "Evento de conversão primária - A" com a configuração do evento como "Realizou compra em 12 horas (Qualquer produto)".]({% image_buster /assets/img/convcorr.png %})

## O que é verificado?

Verificamos os seguintes atributos tratando-os como variáveis categóricas. Em outras palavras, um usuário possui ou não cada valor possível desses atributos, e testamos se eles afetam a taxa de conversão.

-  País
-  Idioma
-  Gênero

Também verificamos se os seguintes fatores afetam a taxa de conversão:

- Realização de qualquer evento personalizado
- Campanhas e Canvas recebidos nos últimos 30 dias (exceto a campanha sendo avaliada no momento)

Por fim, verificamos diversas variáveis comportamentais que podem assumir múltiplos valores. Dividimos as seguintes variáveis em quatro grupos ou quartis e, em seguida, medimos a associação de estar naquele quartil com aumentos ou diminuições na conversão:

- Idade
- Total de dólares gastos
- Número de sessões

## Quando posso verificar essa análise?

Essa análise fica disponível pelo menos 24 horas após o início do envio de uma campanha e considera apenas os envios realizados nos últimos 30 dias. Se nenhum comportamento ou atributo apresentar correlação significativa com qualquer um dos eventos de conversão da campanha, o menu suspenso será desativado e uma mensagem será exibida informando essa situação.

## Como a Braze verifica a significância

Verificamos a significância estatística usando o [intervalo de confiança de Wilson](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval). Determinamos, com 95% de confiança, a taxa na qual o público total da campanha converteu. Isso é chamado de taxa base. 

Em seguida, para cada uma das variáveis, também calculamos, com 95% de confiança, a taxa na qual os usuários com aquele atributo ou comportamento específico converteram. Ao dividir essa taxa pela taxa base, conseguimos medir a razão. Se for muito maior que 1, os usuários com aquele atributo ou comportamento têm mais probabilidade de converter. Se for muito menor, eles têm menos probabilidade. Exibimos o valor da razão na tabela. O valor só é exibido se estiver suficientemente distante de 1 para ser significativo no nível de 95% de confiança.