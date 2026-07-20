---
nav_title: Crie seu agente
article_title: Crie seu agente
page_order: 3
description: "Aprenda a projetar um agente Go do BrazeAI Decisioning Studio, incluindo definição de público, dimensões e limitações específicas do Go."
---

# Crie seu agente {#design-your-agent}

> Este artigo aborda como projetar seu agente Decisioning Studio Go, incluindo a definição do seu público, a seleção de dimensões e a compreensão dos recursos e limitações específicos do Go.

Para conceitos básicos sobre agentes de decisão — incluindo métricas de sucesso, dimensões, bancos de ações e restrições — consulte [Projetando agentes de decisão]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/design_agents).

## Recursos Go versus Pro {#go-versus-pro-capabilities}

O Decisioning Studio Go é uma plataforma self-service com recursos simplificados em comparação com o Decisioning Studio Pro. Compreender essas diferenças ajuda você a projetar um agente eficaz dentro do escopo do Go.

| Capacidade | Decisioning Studio Go | Decisioning Studio Pro |
|-----------|----------------------|------------------------|
| **Métrica de sucesso** | Apenas cliques | Qualquer métrica de negócios (receita, conversões ou ARPU) |
| **Dimensões** | Banco de ações limitado | Dimensões ilimitadas |
| **CEPs suportados** | Braze, SFMC | Qualquer CEP (nativo e personalizado) |
| **Dados de cliente** | Apenas engajamento | Todos os dados 1P |
| **Configuração** | Autoatendimento | Suporte dos serviços de tomada de decisões por IA |
| **Grupos experimentais** | Go + Controle aleatório + BAU opcional | Totalmente personalizável |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Recursos Go versus Pro" }

## Projetando seu agente Go {#design-your-go-agent}

Ao projetar um agente do Decisioning Studio Go, você tomará decisões nas seguintes áreas:

### Etapa 1: Defina seu público {#step-1-define-your-audience}

Seu público é o conjunto de clientes com os quais o agente irá interagir. No Go, os públicos são definidos no seu CEP:

{% tabs %}
{% tab Braze %}

**Definindo o público na Braze:**

1. Crie um segmento na Braze que defina os clientes que você deseja que o agente tenha como alvo.
2. Ao configurar seu experimentador no portal Decisioning Studio Go, selecione esse segmento como seu público-alvo.

{% alert tip %}
Considere criar um segmento dedicado para o seu experimentador do Decisioning Studio Go, a fim de manter seus testes isolados e mensuráveis.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

**Definindo o público no SFMC:**

1. Configure uma extensão de dados que contenha seu público-alvo.
2. Atualize essa extensão de dados diariamente com os dados mais recentes de cliente.
3. Faça referência a essa extensão de dados no portal Decisioning Studio Go ao configurar seu experimentador.

{% endtab %}
{% endtabs %}

### Etapa 2: Selecione suas dimensões {#step-2-select-your-dimensions}

As dimensões são as "alavancas" que o agente pode acionar para personalizar a experiência do cliente. Isso inclui dimensões criativas, como linha de assunto e imagem principal, bem como dimensões relacionadas ao tipo de envio, como a frequência dos e-mails ou a hora do dia.

{% alert note %}
As dimensões específicas disponíveis dependem do seu CEP e de como suas campanhas estão configuradas. Use os modelos e o conteúdo já configurados no seu CEP.
{% endalert %}

### Etapa 3: Configure seu banco de ações {#step-3-configure-your-action-bank}

O banco de ações define as opções específicas que o agente pode escolher para cada dimensão. Por exemplo:

- **Modelos de e-mail:** Selecione quais modelos o agente pode usar (eles devem ser configurados primeiro no seu CEP)
- **Linhas de assunto:** Defina as variantes da linha de assunto que o agente pode testar
- **Horários de envio:** Especifique os intervalos de tempo que o agente pode escolher

### Etapa 4: Configure os grupos experimentais {#step-4-set-up-experiment-groups}

O Decisioning Studio Go cria automaticamente grupos de experimentos para medir o desempenho:

| Grupo | Descrição |
|-------|-------------|
| **Decisioning Studio Go** | Clientes que recebem recomendações otimizadas por IA |
| **Controle aleatório** | Clientes que recebem opções selecionadas aleatoriamente (comparação com a linha de base) |
| **Business as Usual (opcional)** | Clientes que recebem sua campanha atual (se comparando com o desempenho atual) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 4: Configure os grupos experimentais" }

{% alert important %}
Para uma comparação precisa, nenhum cliente pode pertencer a mais de um grupo experimental, e os clientes são atribuídos aleatoriamente aos grupos, sem viés.
{% endalert %}

## Limitações a considerar {#limitations-to-consider}

Ao projetar seu agente Go, tenha em mente estas limitações:

- **Apenas cliques:** O Go otimiza as taxas de cliques. Se você precisa otimizar receita, conversões ou outras métricas de negócios, considere o Decisioning Studio Pro.
- **Dimensões limitadas:** O Go suporta um conjunto predefinido de dimensões. Para dimensões personalizadas ou personalizações complexas, considere o Decisioning Studio Pro.
- **Suporte limitado a CEPs:** O Go integra-se apenas com a Braze e o Salesforce Marketing Cloud. Para outras plataformas, considere o Decisioning Studio Pro.

## Melhores práticas {#best-practices}

- **Comece com um escopo reduzido:** Use dois ou três modelos ou variantes de linha de assunto. Isso dá ao agente opções suficientes para aprender, mantendo o experimento gerenciável.
- **Dê tempo ao tempo:** O agente precisa de dados suficientes para aprender. Aguarde pelo menos duas a quatro semanas antes de tirar conclusões sobre o desempenho.
- **Mantenha o conteúdo variado:** Use opções que sejam significativamente diferentes. Testar pequenas variações pode não trazer insights significativos.
- **Monitore regularmente:** Verifique o portal Decisioning Studio Go para monitorar o progresso do experimento e as métricas de engajamento.

## Próximos passos {#next-steps}

Depois de projetar seu agente, configure-o e lance-o no dashboard da Braze:

- [Configure seu agente Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)