---
nav_title: Funcionalidades
article_title: O que você pode fazer com o Operator
page_order: 1
page_type: reference
toc_headers: h2
description: "Este artigo de referência aborda o que o BrazeAI Operator™ pode fazer no dashboard, incluindo criar Campaigns, Segments e agentes; gerar textos, mensagens, Liquid e imagens; transformar dados; revisar a qualidade do conteúdo; e consultar informações."
---

# O que você pode fazer com o Operator {#operator-capabilities}

> O [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator) é um assistente de IA integrado ao dashboard da Braze. Ele responde perguntas, compõe mensagens e atua nas páginas compatíveis — descreva o que você quer em linguagem natural e o Operator cuida disso no contexto.

Como o Operator entende seu espaço de trabalho — suas diretrizes da marca, atributos personalizados, Connected Content e a página em que você está trabalhando — o resultado é mais contextualizado do que o que assistentes independentes conseguem produzir. Quando o Operator propõe uma alteração em uma Campaign, um Segment ou outro objeto, ele exibe a alteração como um diff visual em um [cartão de ação]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) que você revisa e aprova antes que qualquer coisa seja salva.

Você pode manter o fluxo da conversa com acompanhamentos. O Operator lembra das mensagens anteriores até que você limpe o histórico do chat.

## Pré-requisitos {#prerequisites}

O Operator tem as mesmas permissões que você, então certas ações exigem a permissão relevante para aquela superfície. Por exemplo, gerar uma imagem requer *Editar ativos da biblioteca de mídia*. Se você não encontrar um ponto de entrada, verifique suas permissões com o administrador. Para saber mais, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

## O que o Operator pode criar {#what-operator-can-create}

Além de gerar textos e Liquid, o Operator pode ajudar você a criar vários outros objetos no dashboard, incluindo, entre outros:

- Campaigns
- Content Blocks
- Agentes personalizados
- Imagens
- Mensagens e modelos de mensagem (consulte [Gerar mensagens](#generate-messages) e [Criar modelos de mensagem](#create-message-templates))
- Segments
- Extensões de segmento

{% alert note %}
As funcionalidades do Operator no dashboard são expandidas regularmente. **Pergunte diretamente ao Operator** para obter a resposta mais atualizada sobre o que ele pode fazer.
{% endalert %}

## Campaigns e públicos {#campaigns-and-audiences}

O Operator pode ajudar você a ir de uma ideia a uma Campaign ou público rascunhado, e refinar qualquer um deles depois de criado. Quaisquer alterações que o Operator propõe a uma Campaign ou Segment aparecem como um cartão de ação que você revisa antes de serem salvas.

Para começar, procure a opção **Create with Operator** ao criar uma Campaign ou Segment.

![Os menus Criar Campaign e Criar Segment, cada um mostrando a opção Create with Operator.]({% image_buster /assets/img/operator/operator_create_with_operator.png %}){:style="max-width:90%"}

- **Criar e editar Campaigns:** ao iniciar uma Campaign, o Operator pode ajudar você a rascunhá-la de ponta a ponta a partir de um único briefing em linguagem natural. Isso inclui público, conteúdo e configurações de entrega. Você também pode pedir ao Operator para ajudar a editar uma Campaign existente, como ajustar o direcionamento ou atualizar o conteúdo da mensagem.
- **Do briefing à Campaign:** descreva um briefing completo de Campaign, e o Operator ajuda você a criar um rascunho que inclui texto, imagens, personalização, direcionamento e recomendações de horário de envio. Revise o rascunho no criador de Campaign e refine com prompts de acompanhamento antes de lançar.
- **Criar e editar Segments:** ao iniciar um Segment, descreva o público que você quer e o Operator ajuda a construir a lógica de filtros, incluindo condições de atributos, histórico de eventos e consultas de catálogo. O Operator também pode ajudar a editar os filtros de um Segment existente quando sua estratégia de direcionamento precisa de alterações.
- **Criar extensões de segmento:** o Operator pode ajudar você a criar uma [extensão de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) definida por SQL, escrevendo a consulta que a define. Descreva a lógica de público que você quer, e o Operator rascunha a consulta para você revisar antes de salvar. Para saber mais sobre o Operator e SQL, consulte [Escrever consultas de SQL](#write-sql-queries).

## Agentes {#agents}

![O menu Criar agente, mostrando a opção Agente personalizado e modelos de agente criados pelo Operator.]({% image_buster /assets/img/operator/operator_create_agent.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

O Operator pode ajudar você a criar e refinar agentes no [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents). Quaisquer alterações que o Operator propõe a um agente aparecem como um cartão de ação que você revisa antes de serem salvas.

- **Criar um agente do zero:** o Operator tem acesso a todos os campos do Agent Console, então você pode descrever o agente que quer e o Operator ajuda a configurá-lo. Isso inclui instruções, configurações de saída e outros campos do agente.
- **Começar a partir de um modelo:** o Agent Console oferece uma opção **Create agent with Operator** que carrega um prompt pré-escrito para um caso de uso comum, como redação de textos, análise de sentimento, roteamento de jornada ou enriquecimento de catálogo. Selecione uma categoria, e o Operator ajuda a rascunhar um agente que você pode refinar. Para a lista completa de modelos, consulte [Modelos de agente criados com o Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).
- **Refinar um agente existente:** ao editar um agente, selecione **Generate with Operator** ou **Refine with Operator** próximo ao campo de instruções do agente para obter a ajuda do Operator na escrita ou revisão do prompt e das configurações de saída do agente.

## Conteúdo e criação {#content-and-creative}

O Operator pode gerar e revisar o conteúdo das suas mensagens, incluindo texto, HTML de mensagem, Liquid e imagens, e aplica suas diretrizes da marca automaticamente onde quer que estejam configuradas.

### Aplicar diretrizes da marca {#apply-brand-guidelines}

O Operator usa as diretrizes da marca configuradas no seu espaço de trabalho para que textos, modelos e imagens gerados correspondam à voz, ao tom e ao estilo da sua marca. Para configurar as diretrizes da marca, acesse **Content** > **Brand Guidelines**. Para saber mais, consulte [Diretrizes da marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) e [Aplicar diretrizes da marca]({{site.baseurl}}/user_guide/brazeai/operator#apply-brand-guidelines) no guia de uso do Operator.

### Gerar texto {#generate-copy}

Você pode usar o Operator para fazer brainstorming ou gerar textos de qualquer lugar, mas a melhor experiência é usá-lo diretamente no criador de mensagens, onde ele pode trabalhar junto com você na mensagem que está sendo criada. Descreva seu produto ou Campaign, e o Operator retorna um texto que você pode revisar e inserir.

O Operator melhora o copywriter independente de algumas formas:

- Ele aplica suas [diretrizes da marca](#apply-brand-guidelines) automaticamente quando estão configuradas.
- Ele usa [contexto da página]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context), então você não precisa descrever novamente o canal ou a mensagem em que está trabalhando. Como ele reconhece a página, você também pode usá-lo para editar ou refinar uma mensagem existente em vez de gerar uma do zero.
- Ele pode consultar seus [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) e eventos, então você pode pedir que ele personalize recomendações de texto com Liquid real.
- Você pode manter o fluxo da conversa e iterar. Por exemplo, peça um tom diferente, uma versão mais curta ou uma tradução.

#### Tons {#generate-copy-tones}

O tom do texto gerado é orientado pelo seu prompt. Descreva o estilo que você quer e o Operator ajusta o resultado para corresponder. Por exemplo, peça um tom formal, casual, urgente ou chamativo. Você também pode refinar o tom em prompts de acompanhamento, como pedir uma versão mais descontraída ou mais polida. Quando as diretrizes da marca estão configuradas, o Operator as aplica automaticamente para que o texto permaneça consistente com a voz da sua marca.

### Gerar mensagens {#generate-messages}

O Operator pode gerar um design completo de mensagem para qualquer canal ou editor com modo HTML, incluindo, entre outros:

- E-mail
- SMS/MMS/RCS
- Mensagem no app
- Cartão de conteúdo
- Banner
- Push
- Webhook

Editores de arrastar e soltar não suportam geração direta de design, embora o Operator ainda possa ajudar com texto ou outro conteúdo que você adiciona manualmente. Descreva a mensagem que você quer em linguagem natural, revise o resultado e insira no seu criador. Mantenha o fluxo da conversa para refinar o resultado. Por exemplo, você pode pedir um layout diferente, um texto mais curto ou um estilo de botão atualizado antes de inserir o HTML no editor.

Você obtém os melhores resultados quando usa o Operator no criador em que está trabalhando, onde ele tem [contexto da página]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context) para o canal e o tipo de mensagem. Quando as diretrizes da marca estão configuradas, o Operator as aplica automaticamente.

### Criar Content Blocks {#create-content-blocks}

O Operator pode ajudar você a criar [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks), as peças reutilizáveis de conteúdo que você insere em diferentes mensagens. Descreva o bloco que você quer, e o Operator rascunha o conteúdo para você revisar antes de salvar. Como os Content Blocks são compartilhados, atualizar um atualiza todas as mensagens que o referenciam.

O Operator cria Content Blocks um de cada vez no dashboard. Para criar Content Blocks em massa, use o endpoint [Create Content Block]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) com uma chave de API que tenha a permissão `content_blocks.create`.

### Criar modelos de mensagem {#create-message-templates}

O Operator pode ajudar você a criar [modelos de mensagem]({{site.baseurl}}/user_guide/messaging/templates) reutilizáveis que você pode aplicar em diferentes Campaigns. Descreva o modelo que você quer, e o Operator o rascunha para você revisar antes de salvar. Gerar um modelo funciona de forma semelhante a gerar uma mensagem, então consulte [Gerar mensagens](#generate-messages) para os canais e editores compatíveis.

### Gerar Liquid {#generate-liquid}

O Operator é altamente capaz com a [sintaxe Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid). Ele pode gerar lógica Liquid complexa baseada nos dados do seu espaço de trabalho, incluindo consultar dados de atributos, eventos e [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) para encontrar valores de exemplo. Ele também pode revisar e explicar o Liquid existente nas suas Campaigns.

Assim como na redação de textos, você pode pedir ao Operator para gerar Liquid de qualquer lugar, e ele funciona em todos os canais e criadores de mensagens. Você obtém os melhores resultados de dentro de um criador de mensagens, onde o Operator tem o contexto completo da mensagem que você está criando.

{% details Práticas recomendadas para prompts de Liquid %}

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
- Ao pedir Liquid que usa Connected Content, documentação do endpoint da API, uma resposta de API de exemplo, ou ambos

#### Seja criativo {#generate-liquid-get-creative}

Experimente diferentes prompts para ver como o Operator pode aprimorar suas mensagens. Teste diferentes prompts e ideias, pois a criatividade pode levar a resultados mais envolventes.

{% enddetails %}

### Gerar imagens {#generate-images}

O Operator gera imagens usando o [GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/), um sistema de IA da OpenAI e um provedor terceirizado da Braze. Isso permite que você crie imagens realistas e arte a partir de uma descrição em linguagem natural.

Na [biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library), selecione **Generate with Operator** no painel **Upload Assets**. Descreva a imagem que você quer, e o Operator a gera e salva diretamente na sua biblioteca de mídia.

#### Dicas de prompt {#generate-images-prompt-tips}

- Descreva o assunto, estilo, clima e cores de forma específica. Quanto mais detalhes você incluir, melhor o resultado. O upload de uma imagem de referência não é compatível.
- Quando você aplica [diretrizes da marca](#apply-brand-guidelines) como contexto no seu prompt do Operator, o Operator as aplica diretamente à imagem gerada, para que o resultado reflita o estilo visual da sua marca.
- As gerações de imagens contam para o seu limite diário de uso do Operator. Para saber mais, consulte [Limitações](#limitations).

### Revisar a qualidade do conteúdo {#review-content-quality}

Na guia **Test** para SMS, push Android, push iOS e mensagens no app tradicionais, selecione **Review with Operator** para revisar seu conteúdo antes de enviar. Por padrão, o Operator revisa sua Campaign quanto a erros de ortografia e gramática, tom inadequado ou fora da marca, linguagem ofensiva e qualquer código solto, conteúdo de teste ou Liquid não renderizado, e recomenda como corrigir o que encontrar. Você também pode pedir ao Operator para personalizar como ele revisa seu conteúdo diretamente no seu prompt.

Além da revisão padrão, você pode direcionar o Operator para focar em verificações específicas. Considere pedir que ele analise qualquer um dos seguintes itens:

- **Ortografia e gramática:** revise erros de ortografia e gramática e sugira correções que melhorem a precisão do seu conteúdo.
- **Tom:** avalie se o tom corresponde ao seu estilo de comunicação pretendido e sinalize qualquer coisa que possa ser mal interpretada.
- **Linguagem ofensiva:** verifique linguagem potencialmente ofensiva ou inadequada para que você possa revisá-la e manter suas mensagens respeitosas.
- **Conteúdo acidental:** detecte código solto, marcação ou mensagens de teste que foram adicionados sem querer, incluindo Liquid que não renderizou para um usuário teste.
- **Outros idiomas:** revise conteúdo escrito em outro idioma. O suporte para conteúdo em idiomas diferentes do inglês pode variar, então revise os resultados com atenção.

#### Práticas recomendadas {#review-content-quality-best-practices}

Considere o seguinte para aproveitar ao máximo a revisão de conteúdo:

- **Revise sua mensagem:** embora a revisão de conteúdo possa ajudar a identificar erros, ainda é essencial revisar seu conteúdo manualmente. Use as sugestões geradas por IA como um guia útil, mas confie no seu julgamento para garantir a precisão.
- **Entenda a análise de tom:** os resultados da análise de tom são subjetivos e baseados na compreensão do modelo de IA. Embora possam fornecer insights úteis, considere o tom pretendido e o contexto da conversa para fazer os ajustes apropriados.
- **Verifique novamente a linguagem ofensiva sinalizada:** a detecção de linguagem ofensiva é projetada para ser robusta, mas pode ocasionalmente sinalizar falsos positivos. Revise as seções sinalizadas com cuidado e faça as alterações apropriadas conforme necessário.

## Automação de dados e consulta {#data-automation-and-lookup}

O Operator pode atuar como referência para os dados do seu espaço de trabalho e a documentação da Braze, escrever SQL quando você precisa consultar esses dados diretamente e gerar o código que transforma dados recebidos, como uma carga útil de webhook, em um formato que a Braze pode usar.

### O que o Operator pode consultar {#what-operator-can-look-up}

O Operator pode referenciar os itens a seguir para responder perguntas ou fundamentar o conteúdo que gera, incluindo, entre outros:

- Documentação da Braze
- [Segments]({{site.baseurl}}/user_guide/audience/segments)
- [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) e [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events)
- Dados de [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs)
- Configuração de [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns) e [Canvas]({{site.baseurl}}/user_guide/messaging/canvas) existentes, como direcionamento e configurações de entrega
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
- [Códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes)
- Respostas de [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Agentes]({{site.baseurl}}/user_guide/brazeai/agents)

Pergunte diretamente ao Operator se você não tem certeza se ele pode consultar uma informação específica.

### Analisar dados de desempenho {#analyze-performance-data}

Faça perguntas em linguagem natural ao Operator sobre o desempenho das suas Campaigns e Canvas, e ele retorna gráficos, comparações e insights resumidos extraídos dos dados do seu espaço de trabalho. Diferentemente dos recursos do Operator que dependem do contexto da página em que você está, o Analyze responde de qualquer lugar no dashboard. Para saber mais, consulte [Operator Analyze]({{site.baseurl}}/user_guide/brazeai/operator/analyze).

### Escrever consultas de SQL {#write-sql-queries}

O Operator pode ajudar você a escrever SQL para [extensões de segmento](#campaigns-and-audiences) e para [modelos de consulta]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) do Query Builder. Descreva a consulta que você quer em linguagem natural, e o Operator gera o SQL para você revisar antes de executar.

### Gerar código de transformação de dados {#generate-data-transformation-code}

No editor de [Transformação de dados]({{site.baseurl}}/user_guide/data/unification/data_transformation), selecione **Insert Code** para gerar código de transformação que converte uma carga útil de webhook recebida em solicitações válidas da API da Braze. Para instruções passo a passo sobre como criar uma transformação, consulte [Criar uma transformação]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation).

## Configurações do espaço de trabalho {#workspace-settings}

O Operator pode revisar e atualizar configurações em várias páginas de configuração do espaço de trabalho. Descreva a alteração desejada, e o Operator a propõe como um cartão de ação para você revisar antes de salvar. As páginas de configurações compatíveis incluem, entre outras:

- [Horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)
- [Configurações de push]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings)
- [Limites de frequência de envio de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits)
- [Fluxos de aprovação]({{site.baseurl}}/user_guide/messaging/governance/approvals), incluindo [regras de envio de mensagens]({{site.baseurl}}/user_guide/messaging/governance/approvals/messaging_rules) e aprovação sempre ativa
- [APIs e identificadores]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers), incluindo [outros identificadores]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers#other-identifiers) e limites de API
- [Informações de contato das configurações de administrador]({{site.baseurl}}/user_guide/administer/global/admin_settings/contact_information)

{% alert note %}
A cobertura de páginas de configurações do Operator é expandida regularmente. **Pergunte diretamente ao Operator** para obter a resposta mais atualizada sobre o que ele pode configurar.
{% endalert %}

## Limitações {#limitations}

{% alert note %}
A cobertura do Operator muda com frequência. Se você não tem certeza se uma tela ou fluxo de trabalho específico é compatível, pergunte diretamente ao Operator.
{% endalert %}

O suporte do Operator no dashboard é amplo, mas tem limites.

- **Canvas:** o Operator não pode criar ou editar [Canvas]({{site.baseurl}}/user_guide/messaging/canvas), mas pode referenciar a configuração de um Canvas existente, como direcionamento e configurações de entrega, para responder perguntas e fundamentar seu resultado.
- **Duplicação de Campaign:** o Operator não pode duplicar uma Campaign existente a partir da visualização de lista de Campaigns. Para criar uma Campaign semelhante, peça ao Operator para criar uma nova do zero, ou duplique a Campaign manualmente pelo menu **More Actions** da visualização de lista.
- **Editores de arrastar e soltar:** o Operator não pode gerar ou inserir um design de mensagem diretamente em um editor de arrastar e soltar, como os de [e-mail]({{site.baseurl}}/user_guide/channels/email/drag_and_drop), [Banners]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner) e [mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop). Mude para o editor de HTML correspondente para usar o Operator, ou peça ao Operator para gerar conteúdo, como texto, que você pode colar manualmente. Consulte [Gerar mensagens](#generate-messages) para os canais e editores compatíveis.
- **Visibilidade da tela:** o Operator usa contexto da página para entender o que você está vendo, incluindo conteúdo dentro de prévias e editores compatíveis. Quando parte de uma página está fora do que o Operator pode ler, ele avisa em vez de adivinhar, para que você saiba descrever esse conteúdo por conta própria.
- **Limites de uso:** o Operator tem um limite diário de uso para toda a empresa que é redefinido a cada 24 horas. As gerações de imagens contam para esse limite. Se o limite for atingido, uma mensagem "Daily usage limit exceeded" aparece e nenhuma solicitação adicional pode ser feita até que ele seja redefinido. Para etapas de solução de problemas, consulte [Solução de problemas]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting).

## Assistentes legados {#legacy-assistants}

Antes do Operator, vários recursos de IA funcionavam como assistentes independentes separados: o AI Copywriter, o AI Liquid Assistant, o AI Image Generator, o AI SQL Generator, o Data Transformations AI Copilot e a revisão de conteúdo. Todos os seus pontos de entrada permanecem no lugar e direcionam para o Operator, então seus fluxos de trabalho existentes não são afetados. Para saber o que eles fazem hoje, consulte [Conteúdo e criação](#content-and-creative) e [Automação de dados e consulta](#data-automation-and-lookup).

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Privacidade e segurança de dados {#data-privacy-and-security}

O Operator se integra com a OpenAI para gerar resultados. Para saber mais sobre quais informações a Braze envia para a OpenAI, como esses dados são usados e seus direitos de propriedade intelectual, consulte [Como os dados são usados com a OpenAI]({{site.baseurl}}/user_guide/brazeai/operator#data-privacy-and-security).

## Próximas etapas {#next-steps}

- [Comece a usar o Operator]({{site.baseurl}}/user_guide/brazeai/operator): acesse e use o Operator
- [Biblioteca de prompts]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library): explore exemplos de prompts prontos para uso
- [Revisar ações]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): revise e aprove as alterações propostas pelo Operator
- [Solução de problemas]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): consulte problemas comuns e soluções