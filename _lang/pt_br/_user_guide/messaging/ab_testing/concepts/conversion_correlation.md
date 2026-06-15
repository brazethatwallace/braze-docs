---
nav_title: Correlação de conversão
article_title: Correlação da conversão
alias: /conversion_correlation/
page_order: 3

page_type: reference
description: "Este artigo de referência explica a análise de correlação de conversão na página do Campaign Analytics."
tool:
  - Reports

---

# Correlação de conversão {#conversion-correlation}

> A análise de correlação de conversão na página **Análise de dados da campanha** oferece insight sobre quais atributos e comportamentos do usuário ajudam ou prejudicam os resultados definidos para as campanhas.

## Visão geral {#overview}

Para cada campanha, a Braze verifica uma lista de atributos e comportamentos do usuário e calcula se os usuários estão associados de forma estatisticamente significativa a aumentos ou reduções em cada um dos [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) que você escolheu para a campanha. Também calculamos a probabilidade maior ou menor de conversão dos usuários com determinado atributo ou comportamento e, se for significativo, exibimos isso no lado correspondente da tabela. Os usuários com cada atributo ou comportamento de interesse são comparados com as taxas de todo o público da campanha como um todo. Os comportamentos e atributos que não têm correlação significativa com a conversão não são mostrados na tabela.

Para executar uma análise de correlação de conversão, selecione o evento de conversão de interesse no menu suspenso.

![Painel Conversion Correlation (Correlação de conversão) que mostra um exemplo com "Select a conversion event" (Selecionar um evento de conversão) definido como "Primary Conversion Event - A" (Evento de conversão primária - A) com a configuração do evento como "Made Purchase within 12 hours (Any product)" (Realizou compra em 12 horas (Qualquer produto)).]({% image_buster /assets/img/convcorr.png %})

## O que é verificado? {#what-is-checked}

Verificamos os seguintes atributos tratando-os como variáveis categóricas. Em outras palavras, um usuário possui ou não cada valor possível desses atributos, e testamos se eles afetam a taxa de conversão.

-  País
-  Idioma
-  Gênero

Também verificamos se os seguintes fatores afetam a taxa de conversão:

- Realização de qualquer evento personalizado
- Campaigns e Canvas recebidos nos últimos 30 dias (exceto a campanha sendo avaliada no momento)

Por fim, verificamos diversas variáveis comportamentais que podem assumir múltiplos valores. Dividimos as seguintes variáveis em quatro grupos ou quartis e, em seguida, medimos a associação de estar naquele quartil com aumentos ou reduções na conversão:

- Idade
- Total de dólares gastos
- Número de sessões

## Quando posso verificar essa análise? {#when-can-i-check-this-analysis}

Essa análise fica disponível pelo menos 24 horas após o início do envio de uma campanha e considera apenas os envios realizados nos últimos 30 dias. Se nenhum comportamento ou atributo apresentar correlação significativa com qualquer um dos eventos de conversão da campanha, o menu suspenso será desativado e uma mensagem será exibida informando essa situação.

## Como a Braze verifica a significância {#how-braze-checks-for-significance}

Verificamos a significância estatística usando o [intervalo de confiança de Wilson](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval). Determinamos, com 95% de confiança, a taxa na qual o público total da campanha converteu. Isso é chamado de taxa base.

Em seguida, para cada uma das variáveis, também calculamos, com 95% de confiança, a taxa na qual os usuários com aquele atributo ou comportamento específico converteram. Ao dividir essa taxa pela taxa base, conseguimos medir a razão. Se for muito maior que 1, os usuários com aquele atributo ou comportamento têm mais probabilidade de converter. Se for muito menor, eles têm menos probabilidade. Exibimos o valor da razão na tabela. O valor só é exibido se estiver suficientemente distante de 1 para ser significativo no nível de 95% de confiança.