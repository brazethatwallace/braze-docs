---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Aprenda a acessar e usar o BrazeAI Operator<sup>TM</sup>, um assistente alimentado por IA integrado ao dashboard da Braze, incluindo seus recursos e melhores práticas."
---

# BrazeAI Operator

> O BrazeAI Operator<sup>TM</sup> é um assistente alimentado por IA integrado ao dashboard. O Operator ajuda você a criar — rascunhando Campaigns, Segments e conteúdo — e ajuda a se desbloquear, desde responder perguntas e solucionar problemas até gerar ideias.

## Acessar o Operator {#access-operator}

Abra o Operator em qualquer página do dashboard da Braze.

1. Selecione **BrazeAI Operator<sup>TM</sup>** ao lado do seu perfil de usuário.
2. O painel de conversa do Operator será aberto em um painel lateral.

![O painel de conversa do Operator.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximize para expandir o painel e facilitar a leitura, ou minimize para manter o Operator disponível enquanto você trabalha.
{% endalert %}

## Usar o Operator {#use-operator}

Descreva o que você está tentando realizar usando linguagem natural. Prompts claros e específicos levam a respostas mais úteis. Os prompts podem variar de uma única pergunta a uma solicitação completa de criação:

- **Fazer uma pergunta:** Por que meu Liquid não está renderizando?
- **Criar algo:** Crie um Segment de usuários que abandonaram o carrinho nos últimos 7 dias.

O Operator pode fornecer instruções passo a passo, links para a documentação da Braze, explicações em linguagem simples e rascunhos de Campaigns, Segments e conteúdo que você pode revisar e inserir diretamente no seu trabalho. Para saber como o Operator propõe e aplica mudanças, consulte [Agir com o Operator](#take-action-with-operator).

O Operator usa o [GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra), que é adequado para tarefas complexas e com várias etapas. Para conhecer toda a gama do que o Operator pode ajudar você a criar, consulte [O que você pode fazer com o Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities). Para exemplos prontos para uso, consulte a [biblioteca de prompts]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library).

Assista a este vídeo para ver um exemplo do que o Operator pode fazer.

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## Boas práticas {#best-practices}

Trate o Operator como uma conversa, não como um mecanismo de busca. Prompts curtos e naturais funcionam melhor.

- **Seja específico:** Em vez de "Me fale sobre o Canvas", tente "Como uso jornadas de ação no Canvas?".
- **Faça perguntas de acompanhamento:** Se a primeira resposta não atender à sua necessidade, peça esclarecimentos ou detalhes adicionais. O Operator lembra das mensagens anteriores na conversa até que você limpe o histórico do chat.
- **Aproveite o contexto da página:** O Operator entende sua localização na Braze. Abra o Operator enquanto visualiza a página relevante para obter os resultados mais precisos.

## Personalize sua experiência {#customize-your-experience}

### Aplicar diretrizes da marca {#apply-brand-guidelines}

Adicione diretrizes da marca como contexto às consultas do Operator para que as respostas correspondam à voz, ao tom e à personalidade da sua marca. O Operator usa as diretrizes da marca configuradas no seu espaço de trabalho, o que ajuda a garantir mensagens consistentes quando ele sugere textos ou explica recursos.

Para configurar diretrizes da marca, acesse **Conteúdo** > **Diretrizes da marca**. Para saber mais, consulte [Diretrizes da marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines).

![Selecionando diretrizes da marca no painel de conversa do Operator.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Aproveitar o contexto da página {#leverage-page-aware-context}

O Operator entende automaticamente onde você está na Braze e adapta as respostas com base nesse contexto. Por exemplo, quando você abre o Operator enquanto cria um Canvas, ele pode sugerir etapas relevantes ou fornecer orientações sobre recursos do Canvas sem que você precise explicar em que ponto do fluxo de trabalho está.

Essa consciência de contexto significa que você pode usar prompts curtos e naturais para interagir com o Operator, como "Atualize as configurações do meu editor para corresponder às minhas diretrizes da marca." Quando sua solicitação exige uma parte diferente do dashboard, o Operator pode [navegar até lá]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard) diretamente.

Para ideias de prompts prontos para uso, consulte a [biblioteca de prompts]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library).

## Trabalhar com respostas do Operator {#work-with-operator-responses}

### Comece com prompts sugeridos {#get-started-with-suggested-prompts}

Quando você abre uma conversa com o Operator, prompts sugeridos aparecem com base em tarefas comuns e na sua página atual. Selecione um para começar rapidamente ou digite sua própria pergunta personalizada.

### Entenda como o Operator pensa {#understand-how-operator-thinks}

O Operator mostra suas etapas de raciocínio em seções recolhíveis rotuladas como **Reasoned**. Selecione o dropdown para expandir essas seções e ver como o Operator chegou a uma resposta. Isso é útil quando você quer entender a lógica por trás de uma sugestão ou verificar a abordagem.

![O dropdown "Reasoned" recolhido em uma resposta do Operator.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Tome ações com o Operator {#take-action-with-operator}

O Operator pode propor e executar mudanças diretamente no dashboard da Braze, como preencher campos de formulário, atualizar configurações, gerar conteúdo ou navegar você até uma página diferente para concluir sua solicitação. Cada mudança proposta é apresentada como um cartão de ação para você revisar e aprovar antes que ela entre em vigor. Para saber mais sobre como isso funciona, consulte [Revisar ações]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions).

### Copiar respostas para outras ferramentas {#copy-responses-to-other-tools}

As respostas do Operator são formatadas em Markdown. Quando você receber uma resposta, selecione **Copy** na barra de ferramentas que aparece para copiar a resposta completa para a área de transferência. A maioria das ferramentas renderiza Markdown nativamente ou aceita com pequenos ajustes. Selecione uma guia para o seu destino:

{% tabs %}
{% tab Google Docs %}

Primeiro, acesse **Tools** > **Preferences** e selecione **Automatically detect Markdown**. Em seguida, para colar Markdown, acesse **Edit** > **Paste from Markdown**. Você também pode clicar com o botão direito e selecionar **Paste from Markdown**.

{% endtab %}
{% tab Microsoft Word e Outlook %}

O Word e o Outlook não renderizam Markdown nativamente. Cole a resposta em um visualizador de Markdown baseado na web, depois copie a saída renderizada e cole no Word ou Outlook com **Keep Source Formatting**. Como alternativa, cole como texto simples e formate manualmente.

{% endtab %}
{% tab Confluence e Notion %}

Cole diretamente. Ambas as plataformas renderizam Markdown automaticamente.

{% endtab %}
{% tab Slack %}

Cole diretamente. O Slack renderiza negrito, código inline, blocos de código, citações em bloco e listas com marcadores, mas não renderiza títulos Markdown nem sintaxe de links.

{% endtab %}
{% tab Outras ferramentas %}

Se você quiser trabalhar em um arquivo ou usar ferramentas de conversão, também pode:

- Abrir um editor de texto como o [VS Code](https://code.visualstudio.com/) e criar um novo arquivo de texto, depois colar o Markdown e visualizar para revisar a formatação antes de converter ou colar em outro lugar.
- Usar o [Pandoc](https://pandoc.org/) para converter Markdown em um documento Word, HTML ou PDF quando você precisar de uma estrutura previsível no Word ou Outlook sem colar a partir de um navegador.

{% endtab %}
{% endtabs %}

## Gerenciar sua sessão {#manage-your-session}

### Interromper uma resposta {#stop-a-response}

Enquanto o Operator está gerando uma resposta, o botão **Send** se transforma em um botão **Stop**. Selecione **Stop** para encerrar a resposta antecipadamente se você precisar reformular sua pergunta ou se a resposta estiver indo na direção errada.

### Limpar seu histórico {#clear-your-history}

Para recomeçar do zero ou remover informações sensíveis da conversa, selecione **Clear chat history**. Isso remove todo o conteúdo atual e redefine o contexto da conversa.

### Enviar feedback {#provide-feedback}

Na parte inferior de cada resposta, use os botões de polegar para cima ou polegar para baixo para enviar um feedback rápido. Seu feedback ajuda a melhorar as respostas do Operator ao longo do tempo.

## Privacidade e segurança de dados {#data-privacy-and-security}

O BrazeAI Operator<sup>TM</sup> se integra com a OpenAI, que atua como subprocessadora da Braze, sujeita ao Adendo de Processamento de Dados (DPA) entre você e a Braze. Os dados enviados à OpenAI por meio da Braze não são usados para treinar ou melhorar os modelos da OpenAI. Para mais detalhes sobre conformidade com HIPAA, retenção de dados, tratamento de IPI e governança, consulte [Privacidade e segurança de dados]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security).

## Próximos passos {#next-steps}

- [O que você pode fazer com o Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities): Navegue pelas funcionalidades do Operator no dashboard
- [Biblioteca de prompts]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library): Navegue por exemplos de prompts organizados por página do dashboard
- [Revisar ações]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): Aprenda como revisar e aprovar as mudanças propostas pelo Operator
- [Abrir tickets de suporte]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets): Abra tickets de suporte diretamente pelo Operator
- [Solução de problemas]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): Consulte problemas comuns e soluções
- [Privacidade e segurança de dados]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security): Revise orientações sobre conformidade com HIPAA, retenção de dados e minimização de IPI