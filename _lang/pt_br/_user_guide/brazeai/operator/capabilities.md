---
nav_title: Funcionalidades
article_title: O que você pode fazer com o Operator
page_order: 1
page_type: reference
toc_headers: h2
description: "Este artigo de referência aborda as tarefas de IA disponíveis por meio do BrazeAI Operator™ — incluindo redação de textos, Liquid, geração de imagens, código de transformação de dados e revisão de conteúdo."
---

# O que você pode fazer com o Operator {#operator-capabilities}

> As funcionalidades de IA anteriormente disponíveis como assistentes independentes agora estão acessíveis por meio do [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator). Como o Operator está integrado ao dashboard e entende seu espaço de trabalho (suas diretrizes da marca, atributos, Conteúdo conectado e a página em que você está trabalhando), o resultado é mais contextualizado do que o que os assistentes anteriores conseguiam produzir.

Em vez de abrir uma ferramenta diferente para cada tarefa, descreva o que você quer em linguagem natural e o Operator cuida disso no contexto. Você também pode manter o fluxo da conversa — pedindo um tom diferente, uma versão mais curta ou uma tradução — sem precisar recomeçar. O Operator também pode propor e executar alterações diretamente por meio de [cartões de ação]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) que você revisa antes de entrarem em vigor.

## Pré-requisitos {#prerequisites}

O Operator tem as mesmas permissões que você, então certas ações exigem a permissão relevante para aquela área — por exemplo, gerar uma imagem exige *Edit Media Library Assets*. Se você não encontrar um ponto de entrada, verifique suas permissões com o administrador. Para saber mais, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

## O que está disponível por meio do Operator {#whats-available-through-operator}

Todos os pontos de entrada existentes permanecem no lugar, então seus fluxos de trabalho não são afetados. Essas experiências agora são alimentadas pelo Operator. A tabela a seguir mapeia cada assistente independente anterior para onde encontrá-lo agora.

| Assistente anterior | O que fazia | Onde encontrar agora |
| --- | --- | --- |
| AI Copywriter | Gerava textos de marketing a partir de um nome ou descrição de produto | Um novo ícone **Ask Operator** nos criadores de SMS, push, e-mail HTML e Canvas |
| AI Liquid Assistant | Gerava Liquid para personalização | Um novo ícone **Ask Operator** nos criadores de SMS, push, e-mail HTML e Canvas |
| AI Image Generator | Gerava imagens a partir de um prompt de texto para a biblioteca de mídia | Um novo botão **Generate with Operator** na biblioteca de mídia |
| Data Transformations AI Copilot | Gerava código de transformação | O botão **Insert Code** na página de Transformação de dados |
| Revisão de conteúdo | Verificava o conteúdo quanto a ortografia, gramática, tom, linguagem ofensiva e código solto | Botão **Review with Operator** na guia **Test** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="O que está disponível por meio do Operator" }

## Aplicar diretrizes da marca {#apply-brand-guidelines}

O Operator usa as diretrizes da marca configuradas no seu espaço de trabalho para que textos, modelos e imagens gerados correspondam à voz, ao tom e ao estilo da sua marca. Para configurar as diretrizes da marca, acesse **Conteúdo** > **Diretrizes da marca**. Para saber mais, consulte [Diretrizes da marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines). Para detalhes sobre como aplicar diretrizes da marca para uso com o Operator, consulte [Aplicar diretrizes da marca]({{site.baseurl}}/user_guide/brazeai/operator#apply-brand-guidelines).

## Gerar texto {#generate-copy}

Você pode usar o Operator para fazer brainstorming ou gerar textos de qualquer lugar, mas a melhor experiência é usá-lo diretamente no criador de mensagens, onde ele pode trabalhar junto com você na mensagem que está sendo criada. Descreva seu produto ou Campaign, e o Operator retorna um texto que você pode revisar e inserir.

O Operator melhora o copywriter independente de algumas formas:

- Ele aplica suas [diretrizes da marca](#apply-brand-guidelines) automaticamente quando estão configuradas.
- Ele usa [contexto da página]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context), então você não precisa descrever novamente o canal ou a mensagem em que está trabalhando. Como ele reconhece a página, você também pode usá-lo para editar ou refinar uma mensagem existente em vez de gerar uma do zero.
- Ele pode consultar seus [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) e eventos, então você pode pedir que ele personalize recomendações de texto com Liquid real.
- Você pode manter o fluxo da conversa e iterar. Por exemplo, peça um tom diferente, uma versão mais curta ou uma tradução.

### Tons {#generate-copy-tones}

O tom do texto gerado é orientado pelo seu prompt. Descreva o estilo que você quer — por exemplo, formal, casual, urgente ou chamativo — e o Operator ajusta o resultado para corresponder. Você também pode refinar o tom em prompts de acompanhamento, como pedir uma versão mais descontraída ou mais polida. Quando as [diretrizes da marca](#apply-brand-guidelines) estão configuradas, o Operator as aplica automaticamente para que o texto permaneça consistente com a voz da sua marca.

### Exemplos de prompts {#generate-copy-example-prompts}

{% include copy_block.html content="Write a short, eye-catching push notification announcing our summer sale." %}

{% include copy_block.html content="Rewrite this subject line in a more casual tone." %}

{% include copy_block.html content="Translate this copy into Spanish." %}

## Gerar Liquid {#generate-liquid}

Em qualquer criador de mensagens, abra o Operator para gerar e refinar Liquid para personalização. O Operator entende a [sintaxe Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), seus atributos padrão e [personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), e o [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), e pode explicar o que o código faz.

### Onde você pode gerar Liquid {#generate-liquid-supported-channels}

Assim como na redação de textos, você pode pedir ao Operator para gerar Liquid de qualquer lugar, e ele funciona em todos os canais e criadores de mensagens. Você obtém os melhores resultados de dentro de um criador de mensagens, onde o Operator tem o contexto completo da mensagem que você está criando.

### Funcionalidades de Liquid {#generate-liquid-attributes}

O Operator é altamente capaz com Liquid. Ele pode gerar lógica Liquid complexa baseada nos dados do seu espaço de trabalho — incluindo consultar dados de [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) para encontrar valores de exemplo — e pode revisar e explicar o Liquid existente nas suas Campaigns.

### Práticas recomendadas {#generate-liquid-best-practices}

#### Use linguagem natural {#generate-liquid-use-natural-language}

O Operator é treinado para entender linguagem natural. Converse com ele como faria com um colega de trabalho ao pedir ajuda. Isso ajuda o Operator a compreender suas necessidades e fornecer assistência precisa.

#### Forneça contexto {#generate-liquid-give-context}

Fornecer contexto ajuda o Operator a entender o panorama geral do seu projeto. É útil incluir contexto como:

- O nome e o setor da sua empresa
- Uma Campaign em que você está trabalhando, como Black Friday ou promoções de fim de ano
- Seu objetivo, como aumentar sua taxa de cliques
- Atributos personalizados específicos que você quer incluir na sua mensagem

Incluir contexto no seu prompt ajuda o Operator a adaptar suas respostas para atender melhor às suas necessidades. Você também pode incluir detalhes da sua Campaign, briefing de mensagem ou documento de brainstorming para atualizar o Operator.

#### Seja específico {#generate-liquid-be-specific}

O Operator pode fazer perguntas de acompanhamento, mas fornecer detalhes antecipadamente pode levar a resultados mais precisos mais rapidamente. Considere incluir detalhes como:

- Quaisquer preferências ou requisitos conhecidos para a mensagem
- Instruções sobre como lidar com situações, como falta de respostas do destinatário da mensagem ou opções de mensagem de fallback
- Valores exatos ou semelhantes para os atributos personalizados que você quer usar, que ajudam o Operator a gerar e testar lógica mais precisa
- Ao pedir Liquid que usa Conteúdo conectado, documentação do endpoint da API, uma resposta de API de exemplo, ou ambos

#### Seja criativo {#generate-liquid-get-creative}

Experimente diferentes prompts para ver como o Operator pode aprimorar suas mensagens. Teste diferentes prompts e ideias, pois a criatividade pode levar a resultados mais envolventes.

### Exemplos de prompts {#generate-liquid-example-prompts}

{% tabs local %}
{% tab Sobre Liquid %}

{% include copy_block.html content="What is Liquid, and how can it help me enhance the personalization of my marketing campaigns within Braze?" %}

{% include copy_block.html content="What types of data can I use in Liquid to personalize my marketing messages, such as demographic information or past purchases?" %}

{% include copy_block.html content="Can you give me some examples of how Liquid is used in marketing campaigns to increase engagement and conversion rates?" %}

{% include copy_block.html content="What are some common use cases for Liquid in text messages for summer sales, such as abandoned cart reminders or personalized promotions?" %}

{% endtab %}
{% tab Personalização %}

{% include copy_block.html content="Add a countdown to this message that shows the time until the user's flight." %}

{% include copy_block.html content="Personalize this message with the user's first name, with a fallback if it's missing." %}

{% include copy_block.html content="Improve this Liquid so it's easier to read." %}

{% include copy_block.html content="Create a message that shows different content based on my customer's loyalty status. If we don't know about their loyalty status, send a fallback message." %}

{% include copy_block.html content="Write a dynamic message that includes a user's favorite product and their last purchase date. If there's no last purchase, abort the message." %}

{% include copy_block.html content="Write me Liquid to encourage someone to click my message that includes a countdown with how much time is left. If the offer has expired, abort the message." %}

{% include copy_block.html content="Help me write a message to encourage users to come back and check out if they have items remaining in their cart." %}

{% include copy_block.html content="Write Liquid to personalize a message based on a customer's country. I want to fill in the message with the country's name. If we don't have either of them, suggest they click on a link to update their profile." %}

{% include copy_block.html content="How can I personalize a welcome message with a user's first name and write different copy based on the user's gender?" %}

{% include copy_block.html content="Write Liquid to display different messages based on a custom attribute, \"CUSTOM_ATTRIBUTE_NAME\" and its value. There are six different options I could send. If there's no value for the custom attribute, I want to send a placeholder message." %}

{% endtab %}
{% endtabs %}

## Gerar imagens {#generate-images}

O Operator gera imagens usando o [GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/), um sistema de IA da OpenAI e um provedor terceirizado da Braze. Isso permite que você crie imagens realistas e arte a partir de uma descrição em linguagem natural.

Na [biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library), selecione **Generate with Operator** no painel **Upload Assets**. Descreva a imagem que você quer, e o Operator a gera e salva diretamente na sua biblioteca de mídia.

### Dicas de prompt {#generate-images-prompt-tips}

- Descreva o assunto, estilo, clima e cores de forma específica. Quanto mais detalhes você incluir, melhor o resultado.
- Apenas entrada de texto; o upload de uma imagem de referência não é suportado.
- Quando você aplica [diretrizes da marca](#apply-brand-guidelines) como contexto no seu prompt do Operator, o Operator as aplica diretamente à imagem gerada, para que o resultado reflita o estilo visual da sua marca.
- As gerações de imagens contam para o seu limite diário de uso do Operator. Para saber mais, consulte [Limitações]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting#limitations).

### Exemplos de prompts {#generate-images-example-prompts}

{% include copy_block.html content="Generate a bright, summery banner image of a beach scene for an email header." %}

{% include copy_block.html content="Create a minimalist product background in our brand colors." %}

## Gerar código de transformação de dados {#generate-data-transformation-code}

No editor de [Transformação de dados]({{site.baseurl}}/user_guide/data/unification/data_transformation), selecione **Insert Code** para gerar código de transformação que converte uma carga útil de webhook recebida em solicitações válidas da API da Braze.

Para instruções passo a passo sobre como criar uma transformação, consulte [Criar uma transformação]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation).

### Exemplos de prompts {#generate-data-transformation-example-prompts}

{% include copy_block.html content="Write transformation code that maps this survey webhook to a custom event on the user's profile." %}

{% include copy_block.html content="Update this transformation to identify users by email address instead of external ID." %}

## Revisar a qualidade do conteúdo {#review-content-quality}

Na guia **Test** para SMS, push Android, push iOS e mensagens no app tradicionais, selecione **Review with Operator** para revisar seu conteúdo antes de enviar. Por padrão, o Operator revisa sua Campaign quanto a erros de ortografia e gramática, tom inadequado ou fora da marca, linguagem ofensiva e qualquer código solto, conteúdo de teste ou Liquid não renderizado, e recomenda como corrigir o que encontrar. Você também pode pedir ao Operator para personalizar como ele revisa seu conteúdo diretamente no seu prompt.

### O que você pode pedir ao Operator para verificar {#review-content-quality-supported-features}

Além da revisão padrão, você pode direcionar o Operator para focar em verificações específicas. Considere pedir que ele analise qualquer um dos seguintes itens:

| Verificação | O que pedir |
| --- | --- |
| Ortografia e gramática | Peça ao Operator para revisar erros de ortografia e gramática e sugerir correções que melhorem a precisão do seu conteúdo. |
| Tom | Peça ao Operator para avaliar se o tom corresponde ao seu estilo de comunicação pretendido e sinalizar qualquer coisa que possa ser mal interpretada. |
| Linguagem ofensiva | Peça ao Operator para verificar linguagem potencialmente ofensiva ou inadequada para que você possa revisá-la e manter suas mensagens respeitosas. |
| Conteúdo acidental | Peça ao Operator para detectar código solto, marcação ou mensagens de teste que você adicionou sem querer, incluindo Liquid que não renderizou para um usuário teste. |
| Outros idiomas | Peça ao Operator para revisar conteúdo escrito em outro idioma. O suporte para conteúdo em idiomas diferentes do inglês pode variar, então revise os resultados com atenção. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="O que você pode pedir ao Operator para verificar" }

### Práticas recomendadas {#review-content-quality-best-practices}

Considere o seguinte para aproveitar ao máximo a revisão de conteúdo:

- **Revise sua mensagem:** Embora a revisão de conteúdo possa ajudar a identificar erros, ainda é essencial revisar seu conteúdo manualmente. Use as sugestões geradas por IA como um guia útil, mas confie no seu julgamento para garantir a precisão.
- **Entenda a análise de tom:** Os resultados da análise de tom são subjetivos e baseados na compreensão do modelo de IA. Embora possam fornecer insights úteis, considere o tom pretendido e o contexto da conversa para fazer os ajustes apropriados.
- **Verifique novamente a linguagem ofensiva sinalizada:** A detecção de linguagem ofensiva é projetada para ser robusta, mas pode ocasionalmente sinalizar falsos positivos. Revise as seções sinalizadas com cuidado e faça as alterações apropriadas conforme necessário.

### Exemplos de prompts {#review-content-quality-example-prompts}

{% include copy_block.html content="Review this push notification for spelling, grammar, and tone, and flag any unrendered Liquid or leftover test content before I send it." %}

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Privacidade e segurança de dados {#data-privacy-and-security}

O Operator se integra com a OpenAI para gerar resultados. Para saber mais sobre quais informações a Braze envia para a OpenAI, como esses dados são usados e seus direitos de propriedade intelectual, consulte [Como os dados são usados com a OpenAI]({{site.baseurl}}/user_guide/brazeai/operator#how-data-is-used-with-openai).

## Próximas etapas {#next-steps}

- [Comece a usar o Operator]({{site.baseurl}}/user_guide/brazeai/operator): Acesse e use o Operator
- [Revisar ações]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): Revise e aprove as alterações propostas pelo Operator
- [Solução de problemas]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): Consulte problemas comuns e soluções