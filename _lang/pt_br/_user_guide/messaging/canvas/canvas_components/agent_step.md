---
nav_title: Agente
article_title: Etapa de agente
alias: /agent_step/
page_order: 2
page_type: reference
description: "Este artigo de referência aborda como usar a etapa de agente no Canvas para gerar conteúdo ou tomar decisões inteligentes em tempo real."
tool: Canvas
toc_headers: h2
---

# Etapa de agente  

> A etapa de agente permite adicionar decisões baseadas em IA e geração de conteúdo diretamente no fluxo de trabalho do seu Canvas. Para informações mais gerais, consulte [Agentes da Braze]({{site.baseurl}}/user_guide/brazeai/agents/). 

![Uma etapa de agente na jornada de usuário de um Canvas.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Pré-requisitos

As etapas de agente usam [variáveis de contexto do Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/) para ingerir contexto relevante e gerar uma variável que pode ser utilizada no Canvas.

## Como funciona

Quando um usuário chega a uma etapa de agente em um Canvas, a Braze envia os dados de entrada que você configurou (contexto completo ou campos selecionados) para o agente escolhido. O agente então processa a entrada usando seu modelo e instruções e retorna uma saída. Essa saída é armazenada na variável de saída que você definiu na etapa.

Você pode usar essa variável de três formas principais:

- **Tomada de decisão:** Direcione os usuários por diferentes jornadas do Canvas com base na resposta do agente. Por exemplo, um agente de pontuação de leads pode retornar um número entre 1 e 10. Você pode usar essa pontuação para decidir se continua enviando mensagens ao usuário ou se o remove da jornada.
- **Personalização:** Insira a resposta do agente diretamente em uma mensagem. Por exemplo, um agente pode analisar o feedback de um cliente e gerar um e-mail de acompanhamento empático que faz referência ao comentário do cliente e sugere uma resolução.
- **Processamento de dados de usuários:** Analise e padronize seus dados de usuários e, em seguida, armazene-os no perfil de usuário ou envie-os usando um webhook. Por exemplo, um agente pode retornar uma pontuação de sentimento ou uma atribuição de afinidade de produto. Você pode armazenar esses dados em um perfil de usuário para uso futuro.

## Criando uma etapa de agente

### Etapa 1: Adicionar uma etapa

Arraste e solte o componente **Agent** da barra lateral, ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Agent**.  

### Etapa 2: Escolher o agente  

Selecione o agente que processará os dados nesta etapa. Escolha um agente existente. Para orientações de configuração, consulte [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Etapa 3: Definir a saída do agente {#define-the-output-variable}

As saídas do agente são chamadas de "variáveis de saída" e são armazenadas em uma [variável de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#context-variable-types) para fácil acesso. Para definir a variável de saída, dê um nome à variável.

O tipo de dado da variável de saída é definido no [Console do agente]({{site.baseurl}}/user_guide/brazeai/agents). As saídas do agente podem ser salvas como strings, números, booleanos ou objetos. Isso as torna flexíveis tanto para personalização de texto quanto para lógica condicional no seu Canvas. Veja alguns usos comuns para cada tipo:

| Tipo de dado | Usos comuns |
| --- | --- |
| String | Personalização de mensagens (linhas de assunto, textos, respostas) |
| Número | Pontuação, limites, roteamento em [Jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) |
| Booleano | Ramificação Sim/Não em [Divisões de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) |
| Objeto | Aproveite um ou mais dos tipos de dados acima com uma única chamada de LLM em uma estrutura de dados previsível |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Você pode usar uma variável de saída em todo o Canvas usando a mesma sintaxe de modelo que usaria com uma variável de contexto. Use o filtro de segmento **Context Variable** ou insira as respostas do agente diretamente usando Liquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

Para usar uma propriedade específica de uma variável de saída do tipo objeto, use a notação de ponto para acessar essa propriedade usando Liquid: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Etapa de agente para Body HTML Writer com um tipo de dado de objeto como saída para a variável "agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### Etapa 4: Adicionar contexto adicional (opcional)

Você pode optar por incluir valores de contexto adicionais para a etapa de agente referenciar durante a execução. Você pode inserir qualquer valor com modelo Liquid que normalmente usaria em um Canvas.

{% alert note %}
O agente já recebe automaticamente o contexto configurado na seção **Instructions**. Variáveis Liquid que já foram configuradas lá não precisam ser inseridas novamente aqui.
{% endalert %}

![A opção de adicionar contexto adicional a uma etapa de agente usando Liquid.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### Etapa 5: Testar o agente

Após configurar sua etapa de agente, você pode testar e pré-visualizar a saída desta etapa.

![Pré-visualizar a saída do agente como um usuário aleatório.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Tratamento de erros  

- Se o modelo conectado retornar um erro de limite de taxa, a Braze faz até cinco novas tentativas com backoff exponencial.  
- Se o agente falhar por qualquer outro motivo (como erro de timeout ou chave de API inválida), a variável de saída é definida como `null`.
    - Se um agente atingir seu limite diário de invocações, a variável de saída é definida como `null`. 
- Use [valores padrão de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/) para se proteger contra erros. Por exemplo, no modal **Add Personalization**, você pode inserir um valor padrão de Liquid como {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} ou {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- As respostas são armazenadas em cache para entradas idênticas e podem ser reutilizadas para invocações idênticas repetidas dentro de alguns minutos.
    - Respostas que usam valores em cache ainda contam para o total e as invocações diárias.
- As etapas de agente podem levar tempo para processar um grande lote de usuários. Se você vir usuários que ainda estão pendentes nesta etapa, verifique seus registros para confirmar que as invocações estão acontecendo.

## Análise de dados  

Consulte as métricas a seguir para acompanhar o desempenho das suas etapas de agente:  

| Métrica | Descrição |
| --- | --- |
| _Entered_ | O número de vezes que os usuários entraram na etapa de agente. |
| _Proceeded to Next Step_ | O número de usuários que avançaram para a próxima etapa do fluxo após passar pela etapa de agente. |
| _Exited Canvas_ | O número de usuários que saíram do Canvas após passar pela etapa de agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Perguntas frequentes

### Quando devo usar uma etapa de agente?

De modo geral, recomendamos usar uma etapa de agente quando você deseja alimentar dados contextuais específicos em um LLM e fazer com que ele atribua de forma agêntica uma variável de contexto do Canvas de maneira inteligente, em uma escala impossível para humanos.

Digamos que você está enviando uma mensagem personalizada para recomendar um novo sabor de sorvete a um usuário que anteriormente pediu chocolate e morango. Veja a diferença entre usar uma etapa de agente e a Recomendação de item de IA:

- **Etapa de agente:** Usa LLMs para tomar uma decisão qualitativa sobre o que o usuário pode querer com base nas instruções e nos dados de contexto fornecidos ao agente. Neste exemplo, uma etapa de agente pode recomendar um novo sabor com base na possibilidade de o usuário querer experimentar sabores diferentes.
- **Recomendação de item de IA:** Usa modelos de machine learning para prever os produtos que um usuário tem maior probabilidade de querer com base em eventos passados do usuário, como compras. Neste exemplo, a Recomendação de item de IA sugeriria um sabor (baunilha) com base nos dois pedidos anteriores do usuário (chocolate e morango) e em como esses se comparam aos comportamentos de outros usuários no seu espaço de trabalho.

### Como as etapas de agente usam os dados de entrada?

Uma etapa de agente analisa os dados de contexto que o agente está configurado para usar, bem como qualquer contexto adicional que é [fornecido ao agente](#step-4-add-any-additional-context-optional).

## Artigos relacionados  

- [Visão geral dos agentes da Braze]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Implantar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  
- [Referência para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference/)