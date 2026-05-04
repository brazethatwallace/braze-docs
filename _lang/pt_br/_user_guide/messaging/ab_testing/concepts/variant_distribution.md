---
nav_title: Distribuição de variantes
article_title: Distribuição de variantes
page_order: 1
page_type: reference
description: "Este artigo de referência explica como a Braze distribui os usuários entre variantes em testes A/B e multivariantes."
tool:
  - Campaign
  - Canvas
---

# Distribuição de variantes {#variant-distribution}

> Quando você configura um teste A/B ou multivariante, cada envio atribui usuários às variantes de forma independente, com base nas porcentagens que você configurar. Como a atribuição é aleatória, a distribuição real pode não corresponder exatamente às suas porcentagens — especialmente com amostras menores.

## Como funciona {#how-it-works}

Toda vez que uma mensagem é enviada em uma campanha multivariante, o sistema seleciona de forma independente uma opção aleatória de acordo com as porcentagens que você definiu e atribui uma variante com base no resultado. É como jogar uma moeda — anomalias são possíveis. Se você já jogou uma moeda 100 vezes, sabe que provavelmente não vai obter uma divisão exata de 50-50 entre cara e coroa todas as vezes, mesmo tendo apenas duas opções. Você pode obter 52 caras e 48 coroas.

Se você tem múltiplas variantes que deseja dividir igualmente, certifique-se de que o número de variantes seja um múltiplo de 100. Caso contrário, algumas variantes terão uma porcentagem maior de usuários distribuídos em comparação com outras. Por exemplo, se sua campanha tem 7 variantes, não é possível ter uma distribuição uniforme, já que 7 não divide 100 igualmente como número inteiro. Nesse caso, você teria 2 variantes de 15% e 5 variantes de 14%.

## Distribuição de mensagens no app {#in-app-message-distribution}

Ao executar um teste A/B em mensagens no app, sua análise de dados pode parecer mostrar uma distribuição de variantes mais alta entre uma variante e outra, mesmo que elas tenham uma divisão percentual igual. Por exemplo, considere o gráfico a seguir de *Destinatários Únicos* para a Variante A e a Variante C.

![Gráfico de Destinatários Únicos mostrando que a Variante A tem uma contagem consistentemente maior do que a Variante C, apesar de uma divisão percentual igual.]({% image_buster /assets/img/variant_distribution_iam.png %})

A Variante A tem uma contagem consistentemente maior de *Destinatários Únicos* do que a Variante C. Isso não se deve à distribuição de variantes, mas sim à forma como os *Destinatários Únicos* são calculados para mensagens no app. Para mensagens no app, *Destinatários Únicos* são, na verdade, *Impressões Únicas*, que é o número total de pessoas que receberam e visualizaram a mensagem no app. Isso significa que, se um usuário não receber a mensagem por qualquer motivo ou decidir não visualizá-la, ele não será incluído na contagem de *Destinatários Únicos*, e a distribuição de variantes pode parecer distorcida.