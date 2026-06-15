---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Aprenda a acessar e usar o BrazeAI Operator<sup>TM</sup>, um assistente alimentado por IA integrado ao dashboard da Braze, incluindo suas funcionalidades e melhores práticas."
---

# BrazeAI Operator

> O BrazeAI Operator<sup>TM</sup> é um assistente alimentado por IA integrado ao dashboard. O Operator ajuda a realizar tarefas — respondendo perguntas, orientando na configuração, solucionando problemas e gerando ideias.

## Acesse o Operator {#access-operator}

Abra o Operator de qualquer página no dashboard da Braze.

1. Selecione **BrazeAI Operator<sup>TM</sup>** ao lado do seu perfil de usuário.

![O ícone do BrazeAI Operator ao lado de um perfil de usuário.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2. O painel de chat do Operator se abre no lado direito da tela.

![O painel de chat do Operator.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximize para expandir o painel e facilitar a leitura, ou minimize para manter o Operator disponível enquanto trabalha.
{% endalert %}

Assista a este vídeo para ver um exemplo do que o Operator pode fazer.

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## Use o Operator {#use-operator}

Descreva o que você está tentando realizar usando linguagem natural. As solicitações podem variar de perguntas simples a pedidos complexos:

- **Simples:** Por que meu Liquid não está sendo renderizado?
- **Complexo:** Como posso fazer com que a tag `abort_message` da minha mensagem inclua o atributo do usuário que causou a interrupção?

O Operator pode fornecer instruções passo a passo, links para a documentação da Braze e explicações em linguagem simples. Perguntas claras e específicas levam a respostas mais úteis. O Operator usa o [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2), que oferece raciocínio avançado e é adequado para tarefas complexas e de múltiplas etapas.

## Melhores práticas {#best-practices}

Trate o Operator como uma conversa, não como um mecanismo de busca. Prompts curtos e naturais funcionam melhor.

- **Seja específico:** Em vez de "Me fale sobre o Canvas", tente "Como eu uso jornadas de ação no Canvas?".
- **Faça perguntas de acompanhamento:** Se a primeira resposta não atender à sua necessidade, peça esclarecimentos ou informações adicionais.
- **Use o contexto da página:** O Operator entende sua localização na Braze. Abra o Operator enquanto visualiza a página relevante para obter os resultados mais precisos.

## Personalize sua experiência {#customize-your-experience}

### Aplique diretrizes da marca {#apply-brand-guidelines}

Adicione diretrizes da marca como contexto às consultas do Operator para que as respostas correspondam à voz, ao tom e à personalidade da sua marca. O Operator usa as diretrizes da marca configuradas no seu espaço de trabalho, o que ajuda a garantir uma comunicação consistente quando sugere textos ou explica recursos.

Para configurar diretrizes da marca, acesse **Settings** > **Brand Guidelines**. Para mais informações, veja [Diretrizes da marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/).

![Selecionando diretrizes da marca no painel de chat do Operator.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Aproveite o contexto da página {#leverage-page-aware-context}

O Operator entende automaticamente sua localização na Braze e adapta as respostas com base nesse contexto. Por exemplo, quando você abre o Operator enquanto constrói um Canvas, ele pode sugerir etapas relevantes ou fornecer orientações sobre os recursos do Canvas sem que você precise explicar onde está no seu fluxo de trabalho.

Essa consciência de contexto significa que você pode fazer perguntas mais curtas e naturais, como "Como eu adiciono uma postergação?" em vez de "Como eu adiciono uma etapa de postergação em um fluxo de trabalho no Canvas?"

## Trabalhe com as respostas do Operator {#work-with-operator-responses}

### Comece com prompts sugeridos {#get-started-with-suggested-prompts}

Quando você abre uma conversa com o Operator, prompts sugeridos aparecem com base em tarefas comuns e na sua página atual. Selecione um para começar rapidamente ou digite sua própria pergunta personalizada.

### Entenda como o Operator pensa {#understand-how-operator-thinks}

O Operator mostra seus passos de raciocínio em seções recolhíveis rotuladas **Reasoned**. Selecione o dropdown para expandir essas seções e ver como o Operator chegou a uma resposta. Isso é útil quando você quer entender a lógica por trás de uma sugestão ou verificar a abordagem.

![O dropdown "Reasoned" recolhido em uma resposta do Operator.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Aja com o Operator {#take-action-with-operator}

O Operator pode propor e executar mudanças diretamente no dashboard da Braze, como preencher campos de formulário, atualizar configurações ou gerar conteúdo. Cada mudança proposta é apresentada como um cartão de ação para você revisar e aprovar antes que entre em vigor. Para mais informações sobre como isso funciona, veja [Revisando ações]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/).

### Copie respostas para outras ferramentas {#copy-responses-to-other-tools}

As respostas do Operator são formatadas em Markdown. Quando você receber uma resposta, selecione **Copy** na barra de ferramentas que aparece para copiar a resposta completa para a área de transferência. A maioria das ferramentas renderiza Markdown nativamente ou aceita com pequenos ajustes. Selecione uma guia para o seu destino:

{% tabs %}
{% tab Google Docs %}

Primeiro, acesse **Tools** > **Preferences** e selecione **Automatically detect Markdown**. Depois, para colar Markdown, acesse **Edit** > **Paste from Markdown**. Você também pode clicar com o botão direito e selecionar **Paste from Markdown**.

{% endtab %}
{% tab Microsoft Word e Outlook %}

O Word e o Outlook não renderizam Markdown nativamente. Cole a resposta em um visualizador de Markdown baseado na web, depois copie a saída renderizada e cole no Word ou Outlook com **Keep Source Formatting**. Como alternativa, cole como texto simples e formate manualmente.

{% endtab %}
{% tab Confluence e Notion %}

Cole diretamente. Ambas as plataformas renderizam Markdown automaticamente.

{% endtab %}
{% tab Slack %}

Cole diretamente. O Slack renderiza negrito, código inline, blocos de código, citações em bloco e listas com marcadores, mas não renderiza cabeçalhos Markdown ou sintaxe de links.

{% endtab %}
{% tab Outras ferramentas %}

Se você quiser trabalhar em um arquivo ou usar ferramentas de conversão, também pode:

- Abrir um editor de texto como o [VS Code](https://code.visualstudio.com/) e criar um novo arquivo de texto, depois colar o Markdown e visualizar para revisar a formatação antes de converter ou colar em outro lugar.
- Usar o [Pandoc](https://pandoc.org/) para converter Markdown em um documento Word, HTML ou PDF quando precisar de uma estrutura previsível no Word ou Outlook sem colar de um navegador.

{% endtab %}
{% endtabs %}

## Gerencie sua sessão {#manage-your-session}

### Pare uma resposta {#stop-a-response}

Enquanto o Operator está gerando uma resposta, o botão **Send** se torna um botão **Stop**. Selecione **Stop** para encerrar a resposta antecipadamente se você precisar reformular sua pergunta ou se a resposta estiver indo na direção errada.

### Limpe seu histórico {#clear-your-history}

Para começar do zero ou remover informações sensíveis da conversa, selecione **Clear chat history**. Isso remove todo o conteúdo atual e redefine o contexto da conversa.

### Forneça feedback {#provide-feedback}

Na parte inferior de cada resposta, use os botões de polegar para cima ou para baixo para fornecer feedback rápido. Seu feedback ajuda a melhorar as respostas do Operator ao longo do tempo.

## Privacidade e segurança de dados {#data-privacy-and-security}

### Provedores de modelos como subprocessadores ou provedores terceiros {#model-providers-as-sub-processors-or-third-party-providers}

Quando você usa uma integração com um provedor de LLM fornecida pela Braze por meio dos Serviços Braze ("LLM fornecido pela Braze"), os provedores de tal LLM fornecido pela Braze atuam como subprocessadores da Braze, sujeitos aos termos do Adendo de Processamento de Dados (DPA) entre você e a Braze. O BrazeAI Operator<sup>TM</sup> integra-se com a OpenAI.

### Como os dados são usados com a OpenAI {#how-data-is-used-with-openai}

Para gerar saída de IA por meio dos recursos da BrazeAI que utilizam a OpenAI ("Saída"), a Braze enviará certas informações ("Entrada") para a OpenAI. A Entrada consiste nos seus prompts, no conteúdo exibido no dashboard e nos dados do espaço de trabalho relevantes para suas consultas. De acordo com os [compromissos da plataforma de API da OpenAI](https://openai.com/enterprise-privacy/), os dados enviados para a API da OpenAI via Braze não são usados para treinar ou melhorar os modelos da OpenAI. Entre você e a Braze, a Saída é sua propriedade intelectual. A Braze não reivindicará nenhum direito autoral sobre tal Saída. A Braze não oferece garantia de qualquer tipo em relação a qualquer conteúdo gerado por IA, incluindo a Saída.

## Próximos passos {#next-steps}

- [Revisar ações]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/): Saiba como revisar e aprovar as alterações propostas pelo Operator
- [Abrir tickets de suporte]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets/): Abra tickets de suporte diretamente pelo Operator
- [Solução de problemas]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/): Consulte problemas comuns e soluções