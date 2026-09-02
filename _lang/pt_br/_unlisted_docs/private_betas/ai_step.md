---
nav_title: Etapa de IA
article_title: Etapa de IA
permalink: /ai_step/
description: "Este artigo de referência aborda a etapa de IA do Canvas."
tool:
  - Canvas
hidden: true
---

# Etapa de IA {#ai-step}

> A etapa de IA no Canvas utiliza o ChatGPT para automatizar o marketing personalizado, interpretando entradas geradas pelo usuário (como feedback de pesquisas), determinando a resposta apropriada e disparando mensagens — tudo dentro da Braze. O ChatGPT é desenvolvido pela OpenAI, um provedor terceirizado.

{% alert note %}
A etapa de IA está disponível atualmente como recurso beta. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar deste teste beta.
{% endalert %}

## Criando uma etapa de IA {#create-ai-step}

1. Adicione uma nova etapa ao seu Canvas e selecione **AI Step**. <br><br>![Etapa de IA no construtor de Canvas][1]{: style="max-width: 30%;"}<br><br>
2. Crie um prompt que diga à IA como responder a diversas ações do usuário. As respostas podem incluir a atualização de um atributo personalizado ou o envio de uma mensagem. Esse prompt pode usar Liquid para atribuir diferentes saídas de resposta com base em diferentes atributos ou entradas do usuário. <br><br>Para atribuir saídas que possam ser usadas para personalizar mensagens futuras dentro do mesmo Canvas, crie um prompt que salve variáveis com nomes específicos (por exemplo, "message" e "sentiment score"). <br><br> ![Exemplo de prompt de IA usado nas configurações da etapa de IA para enviar uma mensagem personalizada com base em uma pontuação de sentimento gerada. Este exemplo está descrito na seção "Respostas de sentimento do cliente".][2] <br><br>
3. Use a guia **Pré-visualização** para testar o que a IA pode gerar para usuários específicos.<br><br> ![A guia Pré-visualização das configurações da etapa de IA mostrando uma mensagem personalizada gerada por IA para três parâmetros: nome Cameron, nome do produto shoes e o texto "decent but my shoe lace already broke"][3]

## Referenciando a saída da IA usando Liquid {#referencing-ai-output-using-liquid}

Referencie a saída da IA em etapas posteriores inserindo a lógica Liquid `{% raw %}{{ai_step_output.${key_name}}}{% endraw %}`. Você pode definir o `key_name` dentro do prompt na etapa de IA.

Por exemplo, se você usar as variáveis "message" e "sentiment score", pode usar `{% raw %}{{ai_step_output.${message}}}{% endraw %}` para personalizar uma mensagem subsequente nesse mesmo Canvas.

Você também pode registrar a saída de qualquer etapa de IA como um atributo personalizado usando a etapa do Canvas de Atualização de usuário, onde você lê a saída da etapa de IA (por exemplo, `{% raw %}{{ai_step_output.${sentiment_score}}}{% endraw %}`). Se a saída não for armazenada como um atributo personalizado, ela não poderá ser usada em nenhum outro lugar além das etapas subsequentes do mesmo Canvas.

### Usando etapas de Contexto {#using-context-steps}

Você pode aproveitar as [etapas de Contexto do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) para referenciar facilmente as saídas posteriormente no seu Canvas.

A seguir, um exemplo de etapa de Contexto que você pode configurar após sua etapa de IA. Neste exemplo, uma etapa de IA anterior contém as saídas da etapa de IA para pontuação de sentimento e mensagem, e esta etapa de Contexto cria as variáveis `sentiment_score` e `message`, que podem ser usadas em etapas subsequentes.

![Etapa de Contexto com duas variáveis: "sentiment_score" e "message".][6]

Você também pode criar uma etapa de Jornadas do público que envia os usuários por caminhos diferentes com base no valor de suas variáveis de contexto. Neste exemplo, você pode segmentar os usuários de forma diferente dependendo da pontuação de sentimento deles. Você também pode usar Liquid para incorporar a variável de mensagem no corpo de um e-mail inserindo a variável usando {% raw %}`{{context.${message}}}`{% endraw %}.

![Uma etapa de Jornadas do público com um grupo de público chamado "Group 1" com o filtro "sentiment_score is more than 80".][7]

## Métricas da etapa de IA {#ai-step-metrics}

As etapas de IA possuem as seguintes métricas no nível da etapa:

| Métrica | Descrição |
| _Avançou para a próxima etapa_ | Número de usuários que avançaram para a(s) etapa(s) seguinte(s) no Canvas |
| _Saiu do Canvas_ | Número de usuários que saíram do Canvas se a etapa de IA foi a última etapa |
| _Saída gerada com sucesso_ | Número de usuários para os quais a etapa de IA gerou a saída com sucesso |
| _Falha na geração da saída_ | Número de usuários para os quais a etapa de IA falhou ao gerar a saída; nesse caso, os usuários ainda avançarão para as etapas subsequentes |
{: .reset-td-br_1 .reset-td-br-2 role="presentation" }

### Entendendo as saídas da etapa de IA {#understanding-your-ai-step-outputs}

Existem alguns cenários em que a Braze descartará a saída da etapa de IA e enviará o cliente para a próxima etapa:

- Se a saída exceder 1.024 caracteres
- Se a saída não estiver em JSON
- Se o prompt não atender aos requisitos de [moderação](https://platform.openai.com/docs/guides/moderation/overview) da OpenAI, que sinaliza conteúdo inadequado gerado pelo usuário

## Casos de uso da etapa de IA {#ai-step-use-cases}

### Respostas de sentimento do cliente {#customer-sentiment-responses}

Conforme demonstrado pelo exemplo em [Criando uma etapa de IA](#create-ai-step), você pode pedir à IA para enviar mensagens de acompanhamento com base em pontuações de sentimento geradas a partir do feedback dos clientes.

- **Pontuações de sentimento positivas:** Dispare uma notificação por push pedindo aos usuários que deixem uma avaliação
- **Pontuações de sentimento médias:** Dispare um e-mail perguntando aos usuários se gostariam de ajuda adicional
- **Pontuações de sentimento baixas:** Dispare um webhook que notifica o help desk do usuário para que um representante de suporte possa elaborar um acompanhamento mais detalhado

#### Exemplo de prompt de IA {#example-ai-prompt}

Este exemplo foi usado em [Criando uma etapa de IA](#create-ai-step).

A customer has purchased "`{% raw %}{{canvas_entry_properties.${product_name}}}{% endraw %}`", and given the product feedback: "`{% raw %}{{canvas_entry_properties.${text}}}{% endraw %}`". Create a sentiment score as an integer between 0 to 100. Then create a personalized message. This should return two variables, "message" and "sentiment score."

### Acompanhamento de pesquisas {#survey-follow-ups}

Se você executar uma pesquisa no app ou no navegador com uma seção de resposta livre, pode usar etapas de IA para analisar as respostas livres e fazer o acompanhamento adequado.

Por exemplo, se um varejista de maquiagem tiver uma pesquisa perguntando "Quais produtos você gostaria de indicar para os prêmios de beleza deste ano?", ele poderia usar um prompt que identifica e atribui um atributo para os tipos de produtos e marcas favoritos do usuário, e então personalizar o conteúdo futuro com base nesses dados.

#### Exemplo de prompt de IA

Identify the user's favorite brand using their response. Then create a message that thanks users for filling out the survey and mentions how Beauty Experts also love their favorite brand. This should return two variables, "message" and "favorite brand."

![Guia Pré-visualização das configurações da etapa de IA mostrando uma mensagem personalizada gerada por IA para o parâmetro de resposta da pesquisa "I love Beauty Brand face creams", que agradece ao usuário por preencher a pesquisa e recomenda um creme facial.][4]

### Recomendações baseadas em comportamento {#behavior-driven-recommendations}

Os clientes podem pedir à IA para analisar comportamentos dos usuários e enviar mensagens de recomendação.

Por exemplo, você pode criar um prompt para analisar as 50 compras mais recentes dos usuários e definir a categoria mais comprada como um novo atributo personalizado. Então, você pode enviar recomendações personalizadas por e-mail para a categoria favorita de cada usuário.

#### Exemplo de prompt de IA

A customer has purchased the following products: "`{% raw %}{{custom_attribute.${Products Purchased}}}{% endraw %}`". Identify the user's most purchased product category. This should return a new variable for "most purchased category."

![Guia Pré-visualização das configurações da etapa de IA mostrando a variável gerada por IA "book" para o parâmetro de categoria mais comprada.][5]

## Limites de taxa {#rate-limits}

Há um limite de 10 solicitações por minuto (RPM) por empresa. Isso significa que, para qualquer etapa de IA, até 10 usuários podem receber essa etapa durante qualquer minuto, e quaisquer usuários além dos 10 avançarão automaticamente para a próxima etapa. Quando o próximo minuto começar, os usuários podem novamente receber a etapa de IA, mas os usuários anteriores que acionaram o limite de taxa não serão reprocessados.

## Limitações da etapa de IA {#ai-step-limitations}

- Este recurso utiliza o GPT-3.5.
- Este recurso usa a chave de API or interface de programação do aplicativo (API) da Braze para a OpenAI. Você não pode usar sua própria chave de API or interface de programação do aplicativo (API) da OpenAI.
- Há um limite de 5 solicitações por minuto (RPM) por espaço de trabalho e 10 RPM por empresa.
- Este recurso não é compatível com HIPAA, e os clientes não devem enviar nenhuma informação de identificação pessoal (IPI) ou informação de saúde protegida (PHI).

## Como meus dados são usados e enviados para a OpenAI? {#how-is-my-data-used-and-sent-to-openai}

Para gerar saídas de IA por meio dos recursos de BrazeAI que a Braze identifica como utilizando a OpenAI ("Saída"), a Braze enviará seu prompt, como conteúdo de mensagem, sentimento do usuário final, diretrizes da marca, dados de campanhas anteriores ou qualquer outra entrada, conforme aplicável ("Entrada"), para a [OpenAI](https://openai.com/). Se dados pessoais forem enviados à OpenAI quando você estiver usando a integração ChatGPT da Braze com a etapa de IA, a OpenAI atuará como subprocessadora da Braze, conforme estabelecido no DPA entre você e a Braze. Se você estiver integrando seu próprio modelo de linguagem de grande escala (LLM) com a etapa de IA, qualquer provedor desse LLM será considerado um provedor terceirizado, e o processamento de quaisquer dados pessoais estará sujeito aos termos entre você e esse provedor terceirizado. Conforme os [compromissos de privacidade da plataforma de API or interface de programação do aplicativo (API) da OpenAI](https://openai.com/enterprise-privacy/), os dados enviados à API or interface de programação do aplicativo (API) da OpenAI por meio da Braze não são usados para treinar ou melhorar os modelos da OpenAI e serão excluídos após 30 dias pela OpenAI de seus sistemas. Entre você e a Braze, a Saída é sua propriedade intelectual. A Braze não reivindicará nenhum direito autoral sobre essa Saída. A Braze não oferece nenhuma garantia de qualquer tipo em relação a conteúdo gerado por IA em geral, incluindo a Saída.

[1]: {% image_buster /assets/unlisted_docs/img/ai_step1.png %}
[2]: {% image_buster /assets/unlisted_docs/img/ai_step2.png %}
[3]: {% image_buster /assets/unlisted_docs/img/ai_step3.png %}
[4]: {% image_buster /assets/unlisted_docs/img/ai_step4.png %}
[5]: {% image_buster /assets/unlisted_docs/img/ai_step5.png %}
[6]: {% image_buster /assets/unlisted_docs/img/ai_step6.png %}
[7]: {% image_buster /assets/unlisted_docs/img/ai_step7.png %}