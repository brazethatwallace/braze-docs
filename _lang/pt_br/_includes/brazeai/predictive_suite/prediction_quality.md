Para medir a precisão do seu modelo, a métrica de _Qualidade da Previsão_ mostrará quão eficaz esse modelo específico de machine learning parece ser quando testado em dados históricos. A Braze extrai os dados de acordo com os grupos que você especificou na página de criação do modelo. O modelo é treinado em um conjunto de dados (o conjunto de "treinamento") e, em seguida, testado em um conjunto de dados novo e separado (o conjunto de "teste").

A previsão será treinada novamente a cada duas semanas e atualizada juntamente com a métrica _Qualidade da Previsão_ para manter suas previsões atualizadas com os padrões mais recentes de comportamento do usuário. Além disso, sempre que isso ocorrer, as duas últimas semanas de previsões serão testadas em relação aos resultados reais dos usuários. A _Qualidade da Previsão_ será então calculada com base nesses resultados reais (em vez de estimativas). Trata-se de um backtest automático (ou seja, testar um modelo preditivo em dados históricos) para garantir que a previsão seja precisa em cenários do mundo real. A última vez em que esse retreinamento e backtesting ocorreram será exibida na página **Predictions** e na página de análise de dados de uma previsão individual. Mesmo uma previsão prévia realizará esse backtest uma vez após sua criação. Dessa forma, você pode ter certeza da precisão da sua previsão personalizada, mesmo com a versão gratuita do recurso.

{% details Exemplo de qualidade da previsão %}

Por exemplo, se 20% dos seus usuários costumam ter churn em média, e você escolhe um subconjunto aleatório de 20% dos seus usuários e os rotula como "com churn" aleatoriamente (sejam eles realmente com churn ou não), você espera identificar corretamente apenas 20% dos usuários com churn reais. Isso é uma suposição aleatória. Se o modelo tivesse apenas esse desempenho, o lift seria 1 para esse caso.

Se o modelo, por outro lado, permitisse o envio de mensagens para 20% dos usuários e, ao fazê-lo, capturasse todos os "verdadeiros" usuários com churn e mais ninguém, o lift seria de 100% / 20% = 5. Se você traçar essa razão para cada proporção dos usuários com churn mais prováveis para quem poderia enviar mensagens, obterá a [curva de lift](https://en.wikipedia.org/wiki/Lift_(data_mining)).

Outra maneira de pensar na qualidade do lift (e também na _Qualidade da Previsão_) é a distância entre a suposição aleatória (0%) e a perfeição (100%) da curva de lift da previsão na identificação de usuários com churn no conjunto de teste. Para consultar o artigo original sobre qualidade de lift, veja [Measuring lift quality in database marketing](https://dl.acm.org/doi/10.1145/380995.381018).

{% enddetails %}

### Como é medido {#how-its-measured}

Nossa medida de _Qualidade da Previsão_ é a [qualidade de lift](https://dl.acm.org/doi/10.1145/380995.381018). De modo geral, "lift" refere-se ao aumento da proporção ou porcentagem de um resultado bem-sucedido, como uma conversão. Nesse caso, o resultado bem-sucedido é a identificação correta de um usuário que teria churn. A qualidade do lift é o lift médio que a previsão fornece em todos os tamanhos possíveis de público para o envio de mensagens ao conjunto de teste. Essa abordagem mede o quanto o modelo é melhor do que a suposição aleatória. Com essa medida, 0% significa que o modelo não é melhor do que adivinhar aleatoriamente quem vai ter churn, e 100% indica conhecimento perfeito de quem vai ter churn.

### Faixas recomendadas {#recommended-ranges}

Veja o que recomendamos para as diversas faixas de _Qualidade da Previsão_:

| Faixa de qualidade da previsão (%) | Recomendação |
| ---------------------- | -------------- |
| 60 - 100 | Excelente. Precisão exemplar. É improvável que a alteração das definições de público traga benefícios adicionais. |
| 40 - 60 | Bom. Este modelo produzirá previsões precisas, mas pode valer a pena testar outras configurações de público para obter resultados ainda melhores. |
| 20 - 40 | Razoável. Este modelo pode proporcionar precisão e valor, mas experimente diferentes definições de público para ver se o desempenho melhora. |
| 0 - 20 | Fraco. Recomendamos alterar suas definições de público e tentar novamente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Recommended ranges" }