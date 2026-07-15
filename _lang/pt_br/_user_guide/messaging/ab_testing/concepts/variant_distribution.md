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

A distribuição entre variantes nem sempre é uniforme. Toda vez que uma mensagem é enviada em uma campanha multivariante, a Braze seleciona de forma independente uma opção aleatória de acordo com as porcentagens que você definiu e atribui uma variante com base no resultado. É como jogar uma moeda — anomalias são possíveis. Se você jogar uma moeda 100 vezes, provavelmente não vai obter uma divisão exata de 50-50 entre cara e coroa, mesmo tendo apenas duas opções. Você pode obter 52 caras e 48 coroas.

Da mesma forma, se você quiser dividir múltiplas variantes igualmente usando porcentagens com números inteiros, certifique-se de que o número de variantes divida 100 de forma exata. Caso contrário, algumas variantes terão uma porcentagem maior de usuários distribuídos em comparação com outras. Por exemplo, se sua campanha tem sete variantes, não é possível ter uma distribuição uniforme, já que sete não divide 100 igualmente como número inteiro. Nesse caso, você teria duas variantes de 15% e cinco variantes de 14%.

{% alert tip %}
Para distribuir usuários em um Canvas, você pode adicionar uma [etapa de Divisão de decisão]({{site.baseurl}}/decision_split) e separar os usuários com base nos seus [números de bucket aleatórios]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers).
{% endalert %}

## Distribuição de mensagens no app {#in-app-message-distribution}

Ao executar um teste A/B em mensagens no app, sua análise de dados pode parecer mostrar uma distribuição de variantes mais alta entre uma variante e outra, mesmo que elas tenham uma divisão percentual igual. Por exemplo, considere o gráfico a seguir de *Destinatários Únicos* para a Variante A e a Variante C.

![Gráfico de Destinatários Únicos mostrando que a Variante A tem uma contagem consistentemente maior do que a Variante C, apesar de uma divisão percentual igual.]({% image_buster /assets/img/variant_distribution_iam.png %})

A Variante A tem uma contagem consistentemente maior de *Destinatários Únicos* do que a Variante C. Isso não se deve à distribuição de variantes, mas sim à forma como os *Destinatários Únicos* são calculados para mensagens no app. Para mensagens no app, *Destinatários Únicos* são, na verdade, *Impressões Únicas*, que é o número total de pessoas que receberam e visualizaram a mensagem no app. Isso significa que, se um usuário não receber a mensagem por qualquer motivo ou decidir não visualizá-la, ele não será incluído na contagem de *Destinatários Únicos*, e a distribuição de variantes pode parecer distorcida.