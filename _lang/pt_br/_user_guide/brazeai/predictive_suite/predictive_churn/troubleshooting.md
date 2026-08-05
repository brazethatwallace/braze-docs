---
nav_title: Solução de problemas
article_title: Solução de problemas do Predictive Churn
description: "Diagnostique erros de treinamento e de público do Predictive Churn usando um índice de sintomas e requisitos de dados."
page_order: 3

---

# Solução de problemas do Predictive Churn {#troubleshoot-predictive-churn}

> Use esta página para resolver erros de treinamento e de público do Predictive Churn. Para análise de dados e qualidade do modelo, consulte [Análise de dados do Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics).

O Predictive Churn (e qualquer modelo de machine learning) é tão bom quanto os dados disponíveis para o modelo. Também depende de um volume suficiente de usuários no espaço de trabalho.

## Comece aqui: identifique seu sintoma {#start-here-match-your-symptom}

Encontre a mensagem de erro, alerta ou resultado que você vê ao compilar uma previsão na seção que explica como corrigir.

| Sintoma | Acesse |
| --- | --- |
| Erro "Not enough data to train" | [Dados insuficientes para treinar](#not-enough-data-to-train) |
| Alerta "Not enough past non-churners" | [Público da previsão muito pequeno](#problems-with-prediction-audience-size) |
| O público da previsão excede o limite de tamanho | [Público da previsão muito grande](#prediction-audience-size-is-too-big) |
| Qualidade da previsão abaixo de 40% | [A previsão tem qualidade baixa](#prediction-has-poor-quality) |
| Incerteza sobre se seus dados se encaixam no modelo | [Considerações sobre dados](#data-considerations) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sintoma de Predictive Churn" }

## Caminho de investigação padrão {#standard-investigation-path}

Use este fluxo de trabalho quando a compilação de uma previsão falhar ou quando você estiver bloqueado por requisitos de dados ou público. Comece pela etapa 1.

1. Confirme se o Predictive Churn está ativado para sua empresa e se o espaço de trabalho tem usuários ativos mensais (MAU) suficientes — normalmente 300.000 MAU em um único espaço de trabalho.
2. Revise sua definição de churn. Filtros muito restritivos reduzem o número de usuários desistentes disponíveis para treinamento.
3. Revise a definição do público da previsão. Um número muito baixo de não desistentes históricos impede o treinamento do modelo.
4. Confirme se eventos personalizados (não apenas atributos personalizados) capturam as ações de alto valor que indicam risco de churn.
5. Se os erros persistirem após ampliar as definições, entre em contato com o [suporte da Braze]({{site.baseurl}}/braze_support).

## Dados insuficientes para treinar {#not-enough-data-to-train}

**Sintoma:** Você vê um erro "Not enough data to train" ao compilar uma previsão.

Esse erro aparece quando sua definição de churn é muito restritiva e retorna poucos usuários desistentes.

Para corrigir, altere o número de dias, as ações que definem o churn para capturar mais usuários, ou ambos. Certifique-se de que está usando os filtros `AND/OR` corretamente para não criar definições excessivamente restritivas.

{% alert important %}
Embora o Predictive Churn esteja ativado no nível da empresa, alguns espaços de trabalho podem não ter usuários suficientes para compilar previsões. Normalmente, são necessários 300.000 usuários ativos mensais (MAU) em um único espaço de trabalho.
{% endalert %}

## Problemas com o tamanho do público da previsão {#problems-with-prediction-audience-size}

**Sintoma:** Você vê a mensagem "Not enough past non-churners to reliably build the Prediction."

![Requisitos de dados da previsão mostrando 31 usuários desistentes anteriores (atende ao requisito) e 0 usuários não desistentes anteriores (abaixo do mínimo). Uma mensagem de alerta indica que não há usuários não desistentes suficientes para compilar a previsão.]({% image_buster /assets/img/churn/audience_size_error.png %})

Ao criar o público da sua previsão para ajustar o tipo de uso contra o qual você deseja que seu modelo seja treinado, você pode encontrar essa mensagem informando que o público da previsão tem poucos usuários.

Se a definição do público da sua previsão for muito restritiva, talvez você não tenha um grupo grande o suficiente de usuários históricos e ativos para trabalhar. Para corrigir isso, altere o número de dias e o tipo de atributos usados nessa definição, mude as ações que definem o churn, ou ambos.

Se o público da sua previsão continuar sendo um problema mesmo após alterar suas definições, talvez você tenha poucos usuários para dar suporte a esse recurso opcional. Tente compilar uma previsão sem as camadas e filtros adicionais.

## O tamanho do público da previsão é muito grande {#prediction-audience-size-is-too-big}

**Sintoma:** A definição do público da sua previsão excede o tamanho máximo permitido.

A definição do público de uma previsão não pode exceder 100 milhões de usuários. Se você vir uma mensagem informando que seu público é muito grande, adicione mais camadas ao seu público ou altere o período de tempo no qual ele se baseia.

## A previsão tem qualidade baixa {#prediction-has-poor-quality}

**Sintoma:** A [qualidade da previsão]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics) é de 39% ou menos.

![Captura de tela relacionada a uma previsão com qualidade baixa.]({% image_buster /assets/img/churn/churn3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Se o seu modelo tem uma qualidade de previsão de 40% ou mais, você está em uma ótima posição. Porém, se a qualidade da previsão cair para 39% ou menos, pode ser necessário editar as definições de churn e de público da previsão para que sejam mais específicas ou tenham janelas de tempo diferentes.

Se você não conseguir atender ao requisito de tamanho de público ao criar as definições da sua previsão e, ao mesmo tempo, alcançar uma qualidade de previsão superior a 40%, isso provavelmente significa que os dados enviados à Braze não são ideais para esse caso de uso, que não há usuários suficientes para compilar um modelo ou que o ciclo de vida do seu produto é mais longo do que a janela de retrospectiva atual de 60 dias suporta.

## Considerações sobre os dados {#data-considerations}

Veja a seguir as perguntas que você deve fazer a si mesmo ao configurar o Predictive Churn. Os modelos de machine learning são tão bons quanto os dados que os treinam, portanto, ter boas práticas de higiene de dados e entender o que entra no modelo fará uma grande diferença.

- Quais ações de alto valor levam à retenção e à fidelidade?
- Você configurou eventos personalizados que mapeiam essas ações específicas? O Predictive Churn funciona com eventos personalizados em vez de atributos personalizados.
- Você está pensando em períodos dentro dos quais definirá o churn? Você pode definir churn como algo que acontece em até 60 dias.
- Você já considerou as épocas do ano que levam a comportamentos atípicos dos usuários, como os feriados? As rápidas mudanças no comportamento do consumidor afetarão suas previsões.