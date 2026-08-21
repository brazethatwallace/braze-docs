---
nav_title: Copiar entre espaços de trabalho
article_title: Copiar entre espaços de trabalho
page_order: 3
alias: "/copying_to_workspaces/"
page_type: reference
description: "Este artigo de referência fornece uma visão geral de como copiar Campaigns, Canvas e landing pages para diferentes espaços de trabalho."
tool:
    - Campaigns
    - Canvas
---

# Copiar Campaigns, Canvas e landing pages entre espaços de trabalho {#copy-campaigns-canvases-and-landing-pages-across-workspaces}

> Copiar Campaigns, Canvas e landing pages entre espaços de trabalho permite que você agilize a criação de conteúdo usando conteúdo existente de um espaço de trabalho diferente como ponto de partida. Esta página explica como copiar Campaigns, Canvas e landing pages para diferentes espaços de trabalho e lista o que é e o que não é copiado.

Quando você copia uma Campaign, um Canvas ou uma landing page para um espaço de trabalho diferente, a cópia permanece como rascunho até que você edite e lance a Campaign ou o Canvas, ou publique a landing page. Isso ajuda você a manter e desenvolver suas estratégias de envio de mensagens bem-sucedidas.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
A cópia de Campaigns entre espaços de trabalho está disponível de forma geral. O suporte de canal para Content Cards não está disponível no momento.
{% endalert %}

Você pode copiar Campaigns entre espaços de trabalho para os seguintes canais compatíveis: SMS, mensagens no app, notificações por push, e-mail e webhooks. Você também pode copiar modelos de e-mail, Feature Flags e Content Blocks. Observe que campanhas multicanais com canais não compatíveis não podem ser copiadas para um espaço de trabalho diferente.

Para copiar uma Campaign para um espaço de trabalho diferente:

1. Selecione o ícone de engrenagem <i class="fas fa-cog"></i> ao lado da Campaign selecionada.
2. Selecione **Copiar para espaço de trabalho**.
3. Após a cópia, revise e teste sua Campaign para confirmar que todos os campos funcionam corretamente.

{% endtab %}
{% tab canvas %}

{% alert important %}
A cópia de Canvas entre espaços de trabalho está disponível de forma geral. Os seguintes canais não são compatíveis no momento: LINE, Content Cards e WhatsApp.
{% endalert %}

Você pode copiar Canvas entre espaços de trabalho para os seguintes canais compatíveis: e-mail, mensagens no app, push, webhooks e SMS.

Para copiar um Canvas para um espaço de trabalho diferente:

1. Selecione o menu <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;ao lado do Canvas selecionado.
2. Selecione **Copiar para espaço de trabalho**.
3. Após a cópia, revise e teste seu Canvas para confirmar que todos os campos funcionam corretamente.

Ao copiar um Canvas com etapas de Audience Sync, as configurações não são copiadas para o espaço de trabalho de destino, mas as etapas da jornada são.

{% endtab %}
{% tab landing pages %}

Você pode copiar landing pages entre espaços de trabalho.

Para copiar uma landing page para um espaço de trabalho diferente:

1. Acesse **Mensagens** > **Landing Pages**.
2. Selecione o menu <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;ao lado da landing page selecionada.
3. Selecione **Copiar para espaço de trabalho**.
4. Revise e teste sua landing page para confirmar que todos os campos funcionam corretamente.

{% endtab %}
{% endtabs %}

{% alert note %}
Você pode copiar uma Campaign ou um Canvas para outro espaço de trabalho em qualquer momento do seu ciclo de vida, inclusive após o lançamento. A Braze copia a versão ativa.<br><br>Se você tiver [alterações de rascunho salvas]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/change_your_campaign_after_launch#campaign-drafts) para uma Campaign ou [salvo um rascunho de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_drafts) que ainda não foi lançado, a Braze não inclui essas edições pendentes. Lance o rascunho no espaço de trabalho original primeiro e depois faça a cópia.
{% endalert %}

## O que é copiado entre espaços de trabalho {#whats-copied-across-workspaces}

Observe que as tabelas a seguir cobrem campos de Campaigns e Canvas, e não são uma lista abrangente do que é copiado entre espaços de trabalho e do que é omitido. Como prática recomendada, verifique os detalhes da Campaign, do Canvas e da landing page e teste para confirmar que sua mensagem funciona conforme o esperado.

As landing pages são copiadas como rascunhos. Antes de publicar uma landing page copiada, revise a URL da página, as configurações de domínio personalizado, o tratamento de envio de formulários e quaisquer referências de Liquid ou específicas do espaço de trabalho.

{% alert note %}
As traduções não são copiadas ao copiar Campaigns de e-mail, Canvas ou modelos entre espaços de trabalho. Após a cópia, insira novamente ou faça o upload das traduções no espaço de trabalho de destino.
{% endalert %}

### Detalhes {#details}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Descrição | Territórios |
| Tipo | Tags |
| Ações (aninhadas) | Segments e filtros |
| Comportamentos de conversão (aninhados) | [Aprovações]({{site.baseurl}}/user_guide/messaging/governance/approvals) |
| Configurações de horário de silêncio | Cronograma de disparo |
| Configurações de limite de frequência | Resumos da Campaign |
| Estado de inscrição do destinatário |  |
| Cronograma recorrente |  |
| É Transacional |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalhes" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Descrição | Territórios |
| Tipo | Tags |
| Ações (aninhadas) | Segments e filtros |
| Comportamentos de conversão (aninhados) | [Aprovações]({{site.baseurl}}/user_guide/messaging/governance/approvals) |
| Configurações de horário de silêncio | Cronograma de disparo |
| Configurações de limite de frequência | Resumos do Canvas |
| Estado de inscrição do destinatário |  |
| Cronograma recorrente | Critérios de saída |
| É Transacional |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalhes" }

Os critérios de filtro das etapas do Canvas (por exemplo, etapas de [divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)) não são copiados para o espaço de trabalho de destino. Reconfigure esses filtros após a cópia.

{% endtab %}
{% endtabs %}

### Comportamentos de conversão {#conversion-behaviors}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs do espaço de trabalho |
| Interação com a Campaign | ID da Campaign |
| Nome do evento personalizado |  |
| Nome do produto |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportamentos de conversão" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs do espaço de trabalho |
| Interação com o Canvas | ID do Canvas |
| Nome do evento personalizado |  |
| Nome do produto |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportamentos de conversão" }

{% endtab %}
{% endtabs %}

### Ações {#actions}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs do espaço de trabalho |
| Interação com a Campaign | ID da Campaign |
| Nome do evento personalizado |  |
| Nome do produto |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ações" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamento | IDs do espaço de trabalho |
| Interação com o Canvas | ID do Canvas |
| Nome do evento personalizado |  |
| Nome do produto |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ações" }

{% endtab %}
{% endtabs %}

### Variações de mensagem {#message-variations}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Percentual de envio | ID da API |
| Tipo | IDs do grupo de teste |
|  | IDs do modelo de link |
|  | IDs do grupo de usuários internos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variações de mensagem" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Percentual de envio | ID da API |
| Tipo | IDs do grupo de teste |
|  | IDs do modelo de link |
|  | IDs do grupo de usuários internos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variações de mensagem" }

{% endtab %}
{% endtabs %}


### Variação de mensagem de e-mail {#email-message-variation}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Corpo do e-mail | Endereço de remetente |
| Extras da mensagem | Responder para |
| Título | BCC |
| Assunto | Modelo de link |
|  | Alias de link |
|  | Traduções |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variação de mensagem de e-mail" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Corpo do e-mail | Endereço de remetente |
| Extras da mensagem | Responder para |
| Título | BCC |
| Assunto | Modelo de link |
|  | Alias de link |
|  | Traduções |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variação de mensagem de e-mail" }

{% endtab %}
{% endtabs %}

### Corpo do e-mail {#email-body}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Texto simples | Alias de link |
| Conteúdo HTML e arrastar e soltar | Traduções |
| Pré-cabeçalho |  |
| CSS inline |  |
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Corpo do e-mail" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Texto simples | Alias de link |
| Conteúdo HTML e arrastar e soltar | Traduções |
| Pré-cabeçalho |  |
| CSS inline |  |
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Corpo do e-mail" }

{% endtab %}
{% endtabs %}

### Modelos de e-mail {#email-templates}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Corpo do e-mail | IDs da API |
| Descrição | IDs de imagem |
| Assunto | Territórios |
| Cabeçalhos | Tags |
| | Traduções |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modelos de e-mail" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Corpo do e-mail | IDs da API |
| Descrição | IDs de imagem |
| Assunto | Territórios |
| Cabeçalhos | Tags |
| | Traduções |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modelos de e-mail" }

{% endtab %}
{% endtabs %}

### Content Blocks

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Nome | Alias de link |
| Descrição | Chaves de API |
| Conteúdo | Territórios |
| Conteúdo HTML e arrastar e soltar | Tags |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Nome | Alias de link |
| Descrição | Chaves de API |
| Conteúdo | Territórios |
| Conteúdo HTML e arrastar e soltar | Tags |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% endtabs %}

### Variação de mensagem SMS {#sms-message-variation}

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Corpo | Serviço de envio de mensagens |
| Encurtamento de link | Itens de mídia VCF |
| Rastreamento de cliques |  |
| Itens de mídia |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variação de mensagem SMS" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Corpo | Serviço de envio de mensagens |
| Encurtamento de link | Itens de mídia VCF |
| Rastreamento de cliques |  |
| Itens de mídia |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variação de mensagem SMS" }

{% endtab %}
{% endtabs %}

## Copiando mensagens que contêm Liquid {#copying-messages-that-contain-liquid}

As referências de Liquid dentro do corpo das mensagens são copiadas para o espaço de trabalho de destino, mas podem não funcionar como esperado. Isso significa que, se um Canvas do Espaço de trabalho A for copiado para o Espaço de trabalho B, o Espaço de trabalho B não poderá referenciar os detalhes do Espaço de trabalho A, incluindo referências de Liquid. Por exemplo, campos como ações-gatilho, filtros de público e critérios de filtro da [divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) não são copiados.

Acompanhe as seguintes referências de Liquid com dependências ao copiar Campaigns, Canvas e landing pages entre espaços de trabalho:

- Tags de itens de catálogo
- Tags de Connected Content
- Content Blocks
- Atributos personalizados
- Centrais de Preferências
- Recomendações de produtos
- Tags de estado de inscrição
- Tags de vouchers e promoções

## Copiando mensagens com feature flags {#copying-messages-with-feature-flags}

Para copiar uma campanha de feature flag e um Canvas com uma etapa de Feature Flag entre espaços de trabalho, certifique-se de que o espaço de trabalho de destino tenha um [experimento de feature flag]({{site.baseurl}}/developer_guide/feature_flags/experiments) configurado com um ID que corresponda à feature flag referenciada na campanha original ou à etapa de Feature Flag referenciada no Canvas original.

Se você copiar uma campanha ou um Canvas que tenha uma etapa de Feature Flag com um ID de feature flag que não existe no espaço de trabalho de destino, a etapa de Feature Flag será copiada, mas seu conteúdo não será.

## Copiando mensagens com Content Blocks {#copying-messages-with-content-blocks}

Quando você copia uma campanha entre espaços de trabalho, os Content Blocks não são copiados. No entanto, um Content Block pode ser referenciado no espaço de trabalho de destino se existir um bloco com o mesmo nome. Como alternativa, você pode criar o Content Block (ou essas referências Liquid) no espaço de trabalho de destino para evitar erros ao lançar uma campanha.

Para Canvas que fazem referência a um Content Block, o Content Block deve primeiro ser copiado para o espaço de trabalho de destino.