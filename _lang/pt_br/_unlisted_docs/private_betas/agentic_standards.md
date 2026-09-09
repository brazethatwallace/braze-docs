---
nav_title: Padrões Agênticos
article_title: Padrões Agênticos
permalink: /agentic_standards/
description: "Este artigo de referência aborda os Padrões Agênticos, incluindo como os Padrões de Campaign funcionam e as práticas recomendadas."
hidden: true
---

# Padrões Agênticos {#agentic-standards}

> Os Padrões Agênticos são regras e conjuntos de regras para aplicar políticas corporativas e proteções em Campaigns na Braze. Eles são seguidos pelo Operator durante o processo de criação e edição. Esses padrões podem ser avaliados agenticamente antes do lançamento de uma Campaign, atuando como uma proteção final para validar diretrizes da marca, convenções organizacionais e requisitos técnicos antes do lançamento.

Os Padrões Agênticos reduzem a supervisão manual para que cada mensagem enviada pela Braze seja precisa, conforme e pronta para o lançamento.

{% alert important %}
Os Padrões Agênticos para o Agent Console estão atualmente em beta. Entre em contato com o gerente da sua conta Braze se tiver interesse em participar deste beta.
{% endalert %}

## Como funciona {#how-it-works}

Ao criar um Padrão de Campaign, você define regras específicas, agrupadas em "conjuntos de regras", que o Operator segue e avalia antes do lançamento de uma Campaign. Você pode escolher entre conjuntos de regras pré-configurados que cobrem necessidades comuns de marketing ou criar regras personalizadas específicas para sua equipe.

Após a configuração, você pode testar o Padrão de Campaign no painel **Prévia da avaliação** contra qualquer Campaign existente no seu espaço de trabalho. A avaliação agêntica fornece um relatório detalhado com categorias das suas descobertas.

## Criar um Padrão de Campaign {#create-a-campaign-standard}

### Etapa 1: Escolha o tipo de padrão {#step-1-choose-the-standard-type}

Para criar seu padrão, acesse **Agent Console** > **Agentic Standards**. Selecione **Create Agentic Standard** e escolha **Campaign Standards** no menu suspenso.

### Etapa 2: Configure os detalhes {#step-2-set-up-details}

Em seguida, configure os detalhes do seu padrão:

1. Insira um nome e uma descrição para ajudar sua equipe a entender seu propósito.
2. (Opcional) Adicione tags para filtrar seu padrão.
3. Escolha o modelo de avaliação que seu padrão utilizará. Ele potencializa a avaliação agêntica do padrão.

![Um Padrão de Campaign "Abandoned Cart Campaign Standards" que define as regras e conjuntos de regras para Campaigns de carrinho abandonado na Braze.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_details.png %}){: style="max-width:80%;"}

### Etapa 3: Configure as regras de Campaign {#step-3-configure-campaign-rules}

Na etapa **Campaign Rules**, defina as regras que devem ser aplicadas como parte deste padrão. Você pode adicionar até 10 conjuntos de regras por padrão e até 20 regras por conjunto de regras.

Selecione **Add ruleset** para ver uma lista das seguintes categorias:

- **Configuração de Campaign:** Valida convenções de nomenclatura, tags e rastreamento de conversão.
- **Público e direcionamento:** Verifica Segments, exclusões e tamanho do público.
- **Conteúdo e texto:** Define requisitos para qualidade do texto, limites de caracteres e completude da mensagem.
- **Links e rastreamento:** Verifica URLs, CTAs, deep links e parâmetros UTM.
- **Personalização e conteúdo dinâmico:** Define verificações para lógica Liquid e valores de fallback.
- **Conformidade e entregabilidade:** Define requisitos para obrigações legais e proteções de envio.
- **Regras personalizadas:** Selecione **Create custom ruleset** para definir requisitos específicos que não se encaixam em nenhuma das categorias pré-configuradas.

Se não tiver certeza de como formular uma regra, selecione **Generate with Operator** para que o Operator ajude você a elaborar uma lógica específica com base nos seus requisitos.

![Quatro regras configuradas para a categoria de público e direcionamento.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_instructions.png %}){: style="max-width:80%;"}

### Etapa 4: Teste seu padrão {#step-4-test-your-standard}

Antes de usar seu padrão para Campaigns na Braze, use o painel **Prévia da avaliação** para simular uma avaliação agêntica.

1. Escolha uma Campaign existente no menu suspenso para usar como caso de teste.
2. Escolha testar todos os conjuntos de regras ou um específico.
3. Selecione o botão **Simulate response**.

Em seguida, revise os resultados. A avaliação é executada contra a Campaign e exibe os resultados nas seguintes categorias:

- **Pass:** Essas regras foram atendidas com sucesso. Por exemplo, a avaliação pode confirmar que suas convenções de nomenclatura correspondem aos padrões esperados.
- **Warning:** São problemas não críticos que podem exigir atenção. Por exemplo, se você estiver testando um conjunto de regras de e-mail contra uma Campaign de webhook, a avaliação agêntica pode emitir um alerta de que nomes de remetente não se aplicam.
- **Fail:** São problemas críticos que devem ser corrigidos antes do lançamento. Exemplos incluem datas agendadas que estão no passado ou tags organizacionais obrigatórias ausentes.

## Usar Padrões Agênticos {#use-agentic-standards}

Depois de configurar um Padrão de Campaign, você pode usá-lo para avaliar qualquer Campaign durante o processo de revisão final. Isso confirma que sua Campaign atende a todos os requisitos antes de ser enviada aos seus usuários.

### Executar uma avaliação {#run-an-evaluation}

Para executar uma avaliação automatizada, acesse a etapa **Review Summary** do fluxo de criação da sua Campaign.

1. Acesse a seção **Agentic Standards** e selecione o padrão desejado no menu suspenso.
2. Selecione **Run evaluation**.

Se você fizer alterações na sua Campaign após executar uma avaliação inicial, selecione **Re-run evaluation** para atualizar os resultados.

### Revisar os resultados da avaliação {#review-evaluation-results}

Após a conclusão da avaliação, um resumo exibe as descobertas nestas categorias: **Pass**, **Fail** e **Warning**.

A guia **Fail** lista as regras que não foram atendidas. Para cada falha, o padrão fornece:

- **Rule:** O critério específico sendo verificado, como "Spelling & Grammar Check".
- **Reason:** Uma explicação de por que a verificação falhou. Por exemplo, a avaliação pode identificar que "personalized" foi usado em vez da grafia do inglês australiano "personalised".

A guia **Pass** lista todas as regras que sua Campaign seguiu com sucesso. Isso confirma que verificações como **Offensive Language Detection** ou **Naming Convention Validation** foram aprovadas.

A guia **Warning** lista problemas não críticos que podem exigir atenção. Por exemplo, se você estiver testando um conjunto de regras de e-mail contra uma Campaign de webhook, a avaliação do padrão pode gerar um alerta de que nomes de remetente não se aplicam.

### Resolver ou ignorar problemas {#resolve-or-ignore-issues}

Para cada falha ou alerta identificado, você pode decidir como proceder antes do lançamento. Selecione **Resolve** ao lado de um problema e escolha entre as seguintes opções:

- **Mark as fixed:** Selecione esta opção após atualizar a configuração ou o texto da sua Campaign com base na sugestão da avaliação.
- **Ignore this issue:** Selecione esta opção para pular o problema apenas nesta execução. Isso é útil para desvios intencionais ou casos específicos em que a sugestão da avaliação pode não se aplicar.
- **Ask BrazeAI Operator:** Selecione esta opção para corrigir o problema usando o Operator.

Após todos os problemas críticos serem resolvidos ou ignorados, você pode prosseguir para lançar sua Campaign.

## Práticas recomendadas {#best-practices}

- **Comece com modelos:** Use os conjuntos de regras pré-configurados para configuração de Campaign e links e rastreamento primeiro, pois eles cobrem os erros manuais mais comuns e fornecem o contexto adequado para a avaliação agêntica.
- **Seja específico:** Ao escrever regras personalizadas, forneça exemplos claros de como o "correto" deve ser. Por exemplo, em vez de escrever "Verifique a convenção de nomenclatura", tente "O nome da Campaign começa com o ano atual (por exemplo, 2026_)."
- **Itere com frequência:** Conforme suas diretrizes da marca ou processos internos mudam, atualize os conjuntos de regras do seu Padrão de Campaign para manter suas verificações automatizadas relevantes.