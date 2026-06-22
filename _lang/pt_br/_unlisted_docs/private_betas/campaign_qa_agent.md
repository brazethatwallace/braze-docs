---
nav_title: Agente de QA de Campaign
article_title: Agente de QA de Campaign
permalink: /campaign_qa_agent/
description: "Este artigo de referência aborda os agentes de QA de Campaign, incluindo como esses agentes funcionam e as melhores práticas."
hidden: true
---

# Agente de QA de Campaign {#campaign-qa-agent}

> Os agentes de QA de Campaign são assistentes com tecnologia de IA que executam verificações automatizadas na configuração da sua Campaign. Esses agentes atuam como uma proteção final, validando sua configuração em relação às diretrizes da marca, convenções organizacionais e requisitos técnicos antes do lançamento.

Ao usar os agentes de QA de Campaign, você pode reduzir a supervisão manual e garantir que cada mensagem enviada pela plataforma da Braze seja precisa, esteja em conformidade e pronta para o lançamento.

{% alert important %}
Os agentes de QA de Campaign para o Console do agente estão atualmente em beta. Fale com o gerente da sua conta Braze se tiver interesse em participar deste beta.
{% endalert %}

## Como funciona {#how-it-works}

Ao criar um agente de QA de Campaign, você define regras específicas, agrupadas em "conjuntos de regras", que o agente usa para avaliar uma Campaign. Você pode escolher entre conjuntos de regras pré-criados que cobrem necessidades comuns de marketing ou criar regras personalizadas específicas para sua equipe.

Quando configurado, você pode testar o agente no painel de pré-visualização em qualquer Campaign existente no seu espaço de trabalho. O agente fornece um relatório detalhado, categorizando suas descobertas em Aprovado, Aviso ou Falha.

## Criar um agente de QA de Campaign {#create-a-campaign-qa-agent}

### Etapa 1: Escolher o tipo de agente {#step-1-choose-the-agent-type}

Para criar seu agente, acesse **Console do agente** > **Gerenciamento de agentes**. Selecione **Criar agente** e escolha **Campaign QA** no menu suspenso.

### Etapa 2: Configurar os detalhes {#step-2-set-up-details}

Em seguida, configure os detalhes do seu agente:

1. Insira um nome e uma descrição para ajudar sua equipe a entender a finalidade do agente.
2. (opcional) Adicione tags para filtrar seu agente.
3. Escolha o modelo que seu agente usará. Isso alimenta o raciocínio do agente.

![Um agente de QA de Campaign chamado "Campaign QA for copy" que verificará a qualidade da mensagem da Campaign, usando o modelo Braze Auto.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_details.png %}){: style="max-width:80%;"}

### Etapa 3: Configurar instruções e regras {#step-3-configure-instructions-and-rules}

Na guia **Instruções**, defina as regras que o agente verificará. Você pode adicionar até 10 conjuntos de regras por agente e até 20 regras por conjunto de regras.

1. Selecione **Adicionar conjunto de regras** para ver uma lista das seguintes categorias:

- **Configuração de Campaign:** Valida convenções de nomenclatura, tags e rastreamento de conversão.
Público e direcionamento: Verifica Segments, exclusões e tamanho do público.
- **Conteúdo e texto:** Avalia a qualidade do texto, limites de caracteres e completude da mensagem.
- **Links e rastreamento:** Verifica URLs, CTAs, deep links e parâmetros UTM.
- **Personalização e conteúdo dinâmico:** Verifica a lógica Liquid e valores de fallback.
- **Conformidade e entregabilidade:** Garante que os requisitos legais e as proteções de envio sejam atendidos.
- **Gerar com Operator:** Se você não tem certeza de como formular uma regra, selecione Gerar com Operator para que nosso assistente de IA ajude a elaborar uma lógica específica com base nos seus requisitos.
- **Regras personalizadas:** Selecione Criar conjunto de regras personalizado para definir verificações exclusivas que não se encaixam em nenhuma das categorias pré-configuradas.

![Seis regras configuradas para a categoria Conteúdo e texto.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_instructions.png %}){: style="max-width:80%;"}

### Etapa 4: Testar seu agente {#step-4-test-your-agent}

Antes de implantar seu agente, use o painel de **pré-visualização** para simular uma resposta e confirmar que a lógica está funcionando conforme o esperado.

1. Escolha uma Campaign existente no menu suspenso para usar como caso de teste.
2. Escolha testar todos os conjuntos de regras ou um específico.
3. Selecione o botão **Simular resposta**.

Em seguida, revise os resultados. O agente avalia a Campaign e exibe os resultados nas seguintes categorias:

- **Aprovado:** Essas regras foram atendidas com sucesso. Por exemplo, o agente pode confirmar que suas convenções de nomenclatura correspondem aos padrões esperados.
- **Aviso:** São problemas não críticos que podem exigir atenção. Por exemplo, se você estiver testando um conjunto de regras de e-mail em uma Campaign de webhook, o agente pode emitir um aviso de que nomes de remetente não se aplicam.
- **Falha:** São problemas críticos que devem ser corrigidos antes do lançamento. Exemplos incluem datas agendadas que estão no passado ou tags organizacionais obrigatórias ausentes.

## Usar agentes de QA de Campaign {#use-campaign-qa-agents}

Depois de configurar um agente de QA de Campaign, você pode usá-lo para auditar qualquer Campaign durante o processo de revisão final. Isso garante que sua Campaign atenda a todos os requisitos antes de ser enviada aos seus usuários.

### Executar uma auditoria {#run-an-audit}

Para executar uma verificação automatizada, acesse a etapa **Resumo da revisão** do fluxo de criação da sua Campaign.

1. Acesse a seção **Agente de QA** e selecione o agente desejado no menu suspenso.
3. Selecione **Executar agente de QA**.

Se você fizer alterações na sua Campaign após executar uma verificação inicial, selecione **Reexecutar agente de QA** para atualizar os resultados.

### Revisar os resultados da auditoria {#review-audit-results}

Após a conclusão da avaliação, o agente fornece um resumo das suas descobertas, categorizadas nestas guias: **Aprovado**, **Falha** e **Aviso**.

A guia **Falha** lista as regras que não foram atendidas. Para cada falha, o agente fornece:

- **Regra:** O critério específico sendo verificado, como "Verificação de ortografia e gramática".
- **Raciocínio:** Uma explicação detalhada do motivo pelo qual a verificação falhou. Por exemplo, o agente pode identificar que "personalized" foi usado em vez da grafia do inglês australiano "personalised".
- **Correções diretas:** Alterações específicas de texto ou configuração sugeridas pelo agente para corrigir o problema.

A guia **Aprovado** lista todas as regras que sua Campaign seguiu com sucesso. Isso confirma que verificações como **Detecção de linguagem ofensiva** ou **Validação de convenção de nomenclatura** foram aprovadas.

A guia **Aviso** lista problemas não críticos que podem exigir atenção. Por exemplo, se você estiver testando um conjunto de regras de e-mail em uma Campaign de webhook, o agente pode emitir um aviso de que nomes de remetente não se aplicam.

### Resolver ou ignorar problemas {#resolve-or-ignore-issues}

Para cada falha ou aviso identificado, você pode decidir como proceder antes do lançamento. Selecione **Resolver** ao lado de um problema e escolha entre as seguintes opções:

- **Corrigi o problema:** Selecione esta opção depois de atualizar a configuração ou o texto da sua Campaign com base no feedback do agente.
- **Ignorar este problema:** Selecione esta opção para abrir uma exceção à regra. Isso é útil para desvios intencionais ou casos extremos em que a sugestão do agente pode não se aplicar.

Depois que todos os problemas críticos forem resolvidos ou ignorados, você pode prosseguir com o lançamento da sua Campaign.

## Melhores práticas {#best-practices}

- **Comece com modelos:** Use os conjuntos de regras pré-criados para configuração de Campaign e links e rastreamento primeiro, pois eles cobrem os erros manuais mais comuns e garantem que o agente tenha o contexto certo para verificar.
- **Seja específico:** Ao escrever regras personalizadas, forneça exemplos claros de como o "correto" deve ser. Por exemplo, em vez de escrever "Verificar a convenção de nomenclatura", tente "Garantir que o nome da Campaign comece com o ano atual (por exemplo, 2026_)."
- **Iterate com frequência:** À medida que suas diretrizes da marca ou processos internos mudam, atualize os conjuntos de regras do seu agente de QA de Campaign para manter suas verificações automatizadas relevantes.