---
nav_title: Configure seu agente
article_title: Configure seu agente do Decisioning Studio Go
page_order: 0
page_type: reference
description: "Este artigo descreve o fluxo de configuração do Decisioning Studio Go para definir público, cronograma, criativos, restrições e lançar seu agente."
toc_headers: h2
---

# Configure seu agente do Decisioning Studio Go {#set-up-your-decisioning-studio-go-agent}

> Este artigo descreve como configurar um agente do Decisioning Studio Go com o fluxo de configuração self-service no dashboard da Braze.

Para uma visão geral de como o Decisioning Studio Go funciona, consulte [BrazeAI Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go). Para confirmar se seu programa é adequado antes de configurar um agente, consulte [Exemplos para o Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples).

## Pré-requisitos {#prerequisites}

Confirme que você tem o seguinte preparado:

- Um [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) para seu público de entrada que não esteja sendo usado ativamente em outro Canvas ou Campaign
- Pelo menos um modelo de e-mail
- O conteúdo de variantes que você deseja testar, como linhas de assunto alternativas, CTAs e imagens de destaque. Você pode criar variantes durante a configuração, mas tê-las prontas acelera o processo
- Acesso ao espaço de trabalho com permissões para configurar agentes de AI Decisioning

Se seu espaço de trabalho não foi provisionado para o Decisioning Studio Go, você não verá a opção de configuração de agente na guia **AI Decisioning**. Entre em contato com seu gerente de sucesso do cliente para obter acesso.

## Etapa 1: Configure seu agente {#step-1-set-up-your-agent}

1. No dashboard da Braze, acesse a guia **AI Decisioning**.
2. Selecione **Create Agent**.
3. Dê ao seu agente um nome que o diferencie de outros no seu espaço de trabalho. Um exemplo é "Membros Fidelidade — Engajamento Semanal" em vez de "Agente de E-mail".
4. (Opcional) Adicione uma descrição para fornecer contexto que você ou um colega possam precisar depois. Isso pode incluir para que serve o agente, qual Segment ele direciona e como é o sucesso.

O agente otimiza seu criativo de e-mail para maximizar o engajamento genuíno, medido pela atividade de cliques significativos por usuário. Os cliques passam por múltiplos filtros de validação independentes que filtram atividade automatizada e cliques relacionados a opt-out, de modo que o sinal reflete o interesse real do cliente em vez do volume bruto de cliques.

## Etapa 2: Selecione o público-alvo {#step-2-select-the-target-audience}

Selecione o Segment da Braze para o qual seu agente enviará. Os usuários nesse Segment são automaticamente divididos em dois grupos:

- **Grupo do Decisioning Studio:** Recebe conteúdo de e-mail otimizado por IA. O agente escolhe a melhor combinação de variantes para cada usuário.
- **Grupo de controle aleatório:** Mínimo de 5% do Segment. Recebe combinações selecionadas aleatoriamente das mesmas opções em dias selecionados aleatoriamente. Este grupo é obrigatório.

![Um Segment selecionado com 1.100 usuários estimados.]({% image_buster /assets/img/decisioning_studio_go/audience_details.png %})

### Por que um Segment dedicado é importante {#why-a-dedicated-segment-matters}

Se os usuários no Segment selecionado também recebem mensagens de outros Canvas ou Campaigns, o engajamento que o agente observa é afetado por essas outras mensagens. O agente não consegue distinguir se um usuário clicou por causa de suas decisões ou por causa de outra coisa. Um aviso aparece se o Segment selecionado está em uso em outro lugar; prossiga, mas espere resultados mais ruidosos.

### Busca de usuário {#user-lookup}

Use **User Lookup** para verificar se usuários específicos atendem aos critérios do seu Segment. Isso é útil para validar a definição do seu Segment.

### Filtros de público {#audience-filters}

Filtros de público não são suportados nesta versão. Se você precisar de critérios de direcionamento adicionais, [crie um Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) com esses filtros aplicados e selecione esse Segment como seu público de entrada.

### Integração com Canvas existentes {#integrate-with-existing-canvases}

Para usar o Decisioning Studio Go dentro de uma jornada mais ampla:

1. Crie um Segment dedicado para os usuários que devem estar no agente.
2. No seu [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas), use uma etapa de User Update para adicionar o usuário a esse Segment no ponto certo da jornada.
3. Confirme que os usuários saem do Canvas para que o agente (não o Canvas) cuide do envio de e-mail para todos no Segment a partir desse ponto.

## Etapa 3: Configure o cronograma {#step-3-configure-the-schedule}

Determine quando o agente pode enviar.

### Etapa 3.1: Determine a frequência de envio {#step-31-determine-the-send-frequency}

Selecione com que frequência os usuários recebem e-mails deste agente — por exemplo, três vezes por semana. Esta é uma seleção única. O agente não otimiza entre diferentes frequências; ele escolhe dias e horários dentro da frequência que você definiu.

### Etapa 3.2: Selecione os dias da semana {#step-32-select-the-days-of-the-week}

Escolha em quais dias o agente pode enviar. Você deve selecionar pelo menos tantos dias quanto sua frequência exige (se o agente envia três vezes por semana, selecione pelo menos três dias; selecionar mais dias dá ao agente mais flexibilidade). O agente otimiza dentro desse conjunto, escolhendo os melhores dias para cada usuário. Para máxima flexibilidade, selecione todos os sete dias.

### Etapa 3.3: Defina o horário de silêncio {#step-33-set-quiet-hours}

Especifique horários em que o agente não deve enviar. O horário de silêncio usa o fuso local do usuário. O uso mais comum é bloquear envios tarde da noite e muito cedo pela manhã. Fora do horário de silêncio, o agente agenda envios nos horários com maior probabilidade de gerar cliques para cada usuário.

### Etapa 3.4: Defina regras de limite de frequência {#step-34-set-frequency-capping-rules}

Suas regras de limite de frequência podem ser aplicadas no nível do agente:

- **Aplicar limite de frequência:** Impede que o agente envie para um usuário quando o limite de frequência dele for atingido. Dependendo de como suas regras estão configuradas, esse limite pode se aplicar no nível do usuário individual ou no nível geral da conta. Em ambos os casos, as mensagens não são enviadas para esse usuário enquanto o limite estiver atingido.
- **Contar para o limite:** Escolha se os envios deste agente contam para o limite geral do usuário.

{% alert tip %}
Se seu limite de frequência protege a experiência do usuário, os envios do agente já são direcionados e talvez você não precise contá-los para o limite. Se seu limite controla o volume geral de envios ou gastos, provavelmente você vai querer que sejam contados. Seu gerente de sucesso do cliente ou consultor de soluções pode ajudar a confirmar a abordagem certa para seu espaço de trabalho.
{% endalert %}

## Etapa 4: Adicione conteúdo e modelos {#step-4-add-content-and-templates}

Defina com o que o agente tem para trabalhar:

- **Criativos base:** Os modelos de e-mail completos. O agente primeiro escolhe qual criativo base enviar para um determinado usuário.
- **Componentes criativos:** Os elementos específicos dentro de um criativo base — linha de assunto, CTA e imagem de destaque — que o agente personaliza por usuário.

Você pode criar criativos base:

- Usando o criador de e-mail padrão da Braze.
- Importando um e-mail de um Canvas ou Campaign existente.

Use um único criativo base ou vários. Com um criativo base, o agente personaliza apenas os componentes dentro dele. Com múltiplos criativos base — por exemplo, um casual, um formal e um promocional — o agente também escolhe qual criativo base é o certo para cada usuário. O agente também pode escolher entre vários criativos base sem componentes criativos adicionais.

### Etapa 4.1: Marque pontos de personalização com tags Liquid {#step-41-mark-personalization-points-with-liquid-tags}

Para cada componente que você deseja que o agente personalize, substitua o conteúdo estático no seu criativo base por uma tag Liquid do menu de personalização. Em seguida, forneça as opções de variantes na seção **Creative Components**.

Os componentes suportados nesta versão são:

- **Linha de assunto:** Substitua a linha de assunto em **Sending Settings** pela tag Liquid para linha de assunto.
- **CTA:** Substitua o texto do botão no corpo do e-mail pela tag Liquid para CTA.
- **Imagem:** Substitua a URL da imagem de destaque pela tag Liquid para imagem.

{% alert note %}
[Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) não são suportados como pontos de substituição para componentes personalizados. Coloque sua linha de assunto, CTA e imagem personalizados diretamente no corpo do e-mail em vez de dentro de um bloco de conteúdo.
{% endalert %}

### Etapa 4.2: Adicione variantes {#step-42-add-variants}

Na seção **Creative Components**, adicione as opções de variantes para cada ponto de personalização:

- Múltiplas opções de linha de assunto
- Múltiplas opções de texto de CTA
- Múltiplas URLs de imagem

Cada variante pode ser associada a criativos base específicos ou disponibilizada para todos os criativos base. Por exemplo, se você tem um criativo base promovendo uma liquidação e outro promovendo novidades, você pode restringir sua linha de assunto `Don't miss our biggest savings of the year` apenas ao criativo de liquidação, enquanto mantém seu CTA `Just dropped` disponível em ambos.

As imagens devem ser selecionadas da biblioteca de mídia da Braze. Se houver uma imagem que você deseja usar, faça o upload para a biblioteca de mídia primeiro.

### Etapa 4.3: Prévia e teste {#step-43-preview-and-test}

Conforme você adiciona mais conteúdo, visualize e teste sua mensagem usando a prévia dinâmica que mostra como diferentes combinações de variantes são renderizadas. Isso é útil para identificar e resolver problemas de renderização antes do lançamento. Depois que seus criativos base e variantes estiverem configurados, você pode ver uma lista completa de todas as combinações que o agente pode enviar.

Você também pode enviar uma mensagem de teste para si mesmo ou para um colega. Os envios de teste exibem a combinação de variantes específica que você selecionar, não o que o agente escolheria para qualquer usuário em particular.

## Etapa 5: Defina restrições {#step-5-define-constraints}

As restrições impedem que o agente envie conteúdo repetitivo para o mesmo usuário. Os seguintes níveis estão disponíveis:

- **Nível de criativo base:** Impede que o mesmo criativo base seja enviado para um usuário mais de uma vez dentro de uma janela que você define. Útil quando cada criativo base é distinto o suficiente para que repeti-lo dentro de, por exemplo, uma semana pareça ultrapassado.
- **Nível de linha de assunto:** Impede que a mesma linha de assunto seja enviada para um usuário mais de uma vez dentro de uma janela que você define. Útil quando as linhas de assunto são o sinal de repetição mais visível.

Restrições no nível de variante para imagens ou CTAs específicos não são suportadas nesta versão.

## Etapa 6: Revise e lance {#step-6-review-and-launch}

A tela **Review** exibe sua configuração completa: público e divisão de controle aleatório, cronograma, criativos base, contagens de variantes e restrições ativas. Revise e resolva quaisquer avisos de validação (por exemplo, sobreposição de Segment com outra Campaign) que apareçam nesta seção.

Selecione **Launch** para ativar o agente. Ele transiciona de **Draft** para **Live** e começa a enviar no próximo dia elegível.

## Após o lançamento {#after-launch}

### Período de treinamento {#training-period}

Quando seu agente é lançado, ele entra em um período de treinamento. Um indicador de treinamento é exibido na interface de relatórios. O desempenho pode flutuar nos primeiros dias enquanto o agente explora combinações. Os e-mails continuam sendo enviados enquanto ele aprende. Não há período de espera.

Mudanças significativas no desempenho aparecem depois que o agente sai do treinamento e entra na personalização ativa. Os relatórios indicam quando essa transição acontece, para que você sempre saiba em qual estágio seu agente está.

### Visualizações de relatórios {#reporting-views}

A interface de relatórios oferece três visualizações principais:

| Visualização | Descrição |
|---|---|
| **Performance** | Taxas de cliques, métricas de engajamento e o aumento do grupo do Decisioning Studio em relação ao controle aleatório. |
| **Configuration** | As configurações atuais do agente — útil para confirmar o que está em execução. |
| **Agent preferences** | Contagens de quantas vezes cada variante foi escolhida pelo agente, mostrando para o que o agente está gravitando para seu público. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Visualizações de relatórios" }

Detalhamentos no nível de elemento mostram como linhas de assunto, CTAs e imagens individuais se comportam em todas as combinações.

### Editar um agente ativo {#edit-a-live-agent}

Acesse a visualização **Configuration** para modificar público, cronograma, criativos ou restrições após o lançamento. A visualização Configuration mostra um resumo das alterações. Promova as alterações antes que entrem em vigor. Adicionar novas variantes não redefine o treinamento do agente nas variantes existentes; apenas adiciona novas opções ao menu do agente.

### Pausar ou parar {#pause-or-stop}

O ciclo de vida de um agente é **Draft** > **Live** > **Stopped**. Selecione **Stop** a qualquer momento para interromper um agente; ele para de enviar e retoma quando você o reativar.

## Referência {#reference}

A tabela a seguir resume as áreas do Decisioning Studio Go e detalhes relacionados.

| Área | Detalhes |
|---|---|
| **Canal** | Somente e-mail |
| **Métrica de conversão** | Somente cliques (cliques únicos diários por usuário) |
| **Pontos de personalização** | Linha de assunto, CTA, imagem de destaque (por criativo base) |
| **Público** | Um Segment da Braze, com controle aleatório obrigatório (mínimo 5%) |
| **Frequência** | Seleção única (sem decisão de frequência) |
| **Envios de teste** | Pelo criador de e-mail da Braze |
| **Relatórios** | Visualizações de Performance, Configuration e Agent preferences, além de detalhamentos no nível de elemento |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Escopo do Decisioning Studio Go" }

### Considerações {#considerations}

- Content Blocks não são suportados como pontos de substituição de personalização.
- URLs de imagem devem ser adicionadas manualmente. Atualmente, a integração com a biblioteca de mídia não é suportada.
- Filtros de público não são suportados além da seleção de Segment.
- Personalização de corpo do texto, pré-cabeçalho e cabeçalho ainda não estão disponíveis.

## Solução de problemas {#troubleshooting}

Entre em contato com seu gerente de sucesso do cliente ou consultor de soluções para obter ajuda com configuração de agente, análise de desempenho ou design de programa.

Para perguntas comuns, consulte o [FAQ do Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq).