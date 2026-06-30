---
article_title: Priorização de mensagens
permalink: /message_prioritization/
toc_headers: h2
description: "Este artigo de referência descreve a Priorização de Mensagens de nível superior e como configurá-la para o seu espaço de trabalho."
---

# Priorização de mensagens {#message-prioritization}

> Use a Priorização de Mensagens para garantir que seus usuários recebam as Campaigns mais importantes.

{% alert important %}
A Priorização de Mensagens está atualmente em beta. Entre em contato com o gerente da sua conta Braze se tiver interesse em participar deste beta.
{% endalert %}

Apenas administradores podem configurar as definições de Priorização de Mensagens de nível superior. Usuários com permissões limitadas podem visualizar cada página nesta seção, mas não podem fazer alterações.

Para acessar as configurações de Priorização de Mensagens de nível superior, acesse **Configurações** > **Priorização de Mensagens**.

## Como funciona {#how-it-works}

A Priorização de Mensagens permite que você crie [categorias](#categories) e [regras de priorização](#prioritization-rules) para classificar como suas mensagens são enviadas.

Digamos que você esteja gerenciando promoções por e-mail para parcerias pagas e programas de fidelidade de uma marca de beleza. Com a Priorização de Mensagens, você poderia criar duas categorias chamadas "Parcerias Pagas" e "Fidelidade". Em seguida, poderia classificar essas categorias com base em qual é mais crítica para o seu negócio. Por exemplo, durante a temporada de festas, você poderia classificar "Fidelidade" acima de "Parcerias Pagas" para priorizar os clientes da sua marca que fazem parte do seu programa de membros há mais de um ano.

![Um exemplo de regras de priorização para duas categorias: Parcerias Pagas e Fidelidade.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

## Categorias {#categories}

As regras de priorização são baseadas em uma classificação de categorias, que é um rótulo que você pode atribuir a uma determinada Campaign (semelhante a uma [tag]({{site.baseurl}}/user_guide/administrative/app_settings/tags/)). Você pode criar até 20 categorias por vez.

Para adicionar uma nova categoria:

1. Acesse **Configurações** > **Priorização de Mensagens** > **Categorias**.
2. Selecione **Criar nova categoria**.

![O botão "Criar nova categoria" na seção de Priorização de Mensagens.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Dê um nome à categoria e uma descrição opcional.
4. Selecione **Criar categoria**.

![Um exemplo de categoria chamada "P3" com a descrição "Esta se tornará minha terceira categoria de maior prioridade."]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

Para editar ou excluir uma categoria, selecione o menu <i class="fas fa-ellipsis-vertical"></i>.

## Regras de priorização {#prioritization-rules}

Depois que suas categorias estiverem configuradas, você pode classificá-las em um conjunto de regras de priorização. As regras são classificadas em ordem decrescente de prioridade. Você pode criar até 10 regras de priorização por vez.

1. Acesse **Configurações** > **Priorização de Mensagens** > **Regras de Priorização** para configurar suas regras.

![Seção "Regras de Priorização" sem prioridades definidas ainda.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization4.png %})

{:start="2"}
2. Selecione **Adicionar regra**.
3. Selecione uma categoria no menu suspenso.

![Regra de priorização "Prioridade 1" com P1 selecionado como categoria.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization5.png %})

{:start="4"}
4. Continue adicionando regras selecionando **+ Adicionar regra** abaixo da sua última regra.

Para reordenar as regras, selecione e arraste o ícone <i class="fa-solid fa-grip-vertical"></i> no canto superior esquerdo de uma regra. Para excluir uma regra, selecione o menu <i class="fas fa-ellipsis-vertical"></i> e depois **Excluir Regra**.

Não se esqueça de selecionar **Salvar** para que suas atualizações sejam aplicadas.

## Configurações no nível da Campaign {#campaign-level-settings}

### Opt-in

{% alert important %}
Apenas Campaigns agendadas e de canal único podem aderir à priorização neste momento. Campaigns baseadas em ação, disparadas por API e Canvas não são compatíveis.
{% endalert %}

Para aderir uma Campaign à priorização, marque a caixa de seleção **Aderir à Priorização de Mensagens** na página **Programar Entrega** da Campaign.

![A caixa de seleção para "Aderir à Priorização de Mensagens".]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

Em seguida, atribua a Campaign a uma categoria selecionando uma no menu suspenso **Categoria**.

![A caixa de seleção para "Aderir à Priorização de Mensagens".]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

Você pode aderir até 25 Campaigns ativas por vez. Campaigns em rascunho, paradas ou arquivadas não contam para esse limite.

### Período de nova tentativa {#retry-window}

Um período de nova tentativa permite que Campaigns que aderiram à priorização tentem novamente por até três dias se a primeira tentativa não tiver prioridade alta o suficiente para enviar. Em cada dia subsequente, no mesmo horário em que a mensagem foi originalmente agendada, o envio é tentado novamente. Após o último dia do período de nova tentativa, se a mensagem ainda não tiver sido enviada, ela não será mais tentada e será permanentemente despriorizada.

O período de nova tentativa deve ser menor que o intervalo entre envios dessa Campaign. Se você tem uma Campaign que envia toda segunda e quarta-feira, a tentativa de nova tentativa ocorre na terça-feira. Isso significa que o período de nova tentativa deve ser definido como um dia.

![A configuração "Período de Nova Tentativa" definida como 1 dia.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

## Limites de frequência {#frequency-caps}

### Para Campaigns {#for-campaigns}

Para ser elegível à Priorização de Mensagens, uma Campaign deve ter aderido ao limite de frequência. Você pode confirmar que a Campaign aderiu na seção **Controles de Entrega** da página **Programar Entrega**.

![Um exemplo da regra de limite de frequência para qualquer canal aplicável e sem filtros adicionais.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

### Regras do limite de frequência {#frequency-capping-rules}

Otimizaremos a prioridade dentro das suas regras de limite de frequência existentes. Embora não seja obrigatório, recomendamos fortemente que você defina pelo menos uma regra de limite de frequência que capture todas as mensagens, independentemente de canal, tag ou categoria. Essa regra de limite de frequência capturará todas as mensagens que aderiram à Priorização de Mensagens, de modo que as mensagens priorizadas sejam comparadas entre si — e não apenas com outras mensagens que compartilham as mesmas características.

Para configurar isso, acesse **Configurações** > **Regras do Limite de Frequência**. Crie uma regra em que o canal seja **Qualquer canal aplicável** e os filtros adicionais sejam **Nenhum**.

![Um exemplo da regra de limite de frequência para qualquer canal aplicável e sem filtros adicionais.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization11.png %})

Você também pode criar regras de limite de frequência por categoria. Isso permite gerenciar suas mensagens de marketing para evitar o envio de muitas mensagens de uma determinada categoria apenas porque ela está marcada como alta prioridade. Selecione **Categoria de priorização de mensagens** em **Filtros adicionais** e selecione uma categoria no menu suspenso.

![Um exemplo da regra de limite de frequência com o menu suspenso do campo "Categoria" para selecionar P2 ou P1.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

Mensagens fora da Priorização de Mensagens compartilharão os limites de frequência com mensagens priorizadas, então mesmo uma mensagem de alta prioridade pode ser abortada devido a uma mensagem fora da Priorização de Mensagens.

## Perguntas frequentes {#frequently-asked-questions}

### Como os empates são resolvidos entre mensagens na mesma categoria? {#how-are-ties-broken-between-messages-in-the-same-category}

Ao priorizar duas mensagens na mesma categoria, daremos maior prioridade à mensagem com o horário de envio mais cedo. Para Campaigns recorrentes, o horário de envio é calculado como a próxima ocorrência a partir da meia-noite de hoje no horário da empresa. Para Campaigns agendadas no horário local, assumiremos um horário de envio no horário da empresa.

### Qual é a relação entre a Priorização de Mensagens e o limite de frequência? {#what-is-the-relationship-between-message-prioritization-and-frequency-capping}

No momento do envio, compararemos a mensagem sendo enviada com outras mensagens que o usuário é elegível para receber, que seguem a mesma regra de limite de frequência e que aderiram à priorização de mensagens. A mensagem será enviada se:

1. A regra de limite de frequência relevante ainda não tiver sido atingida para aquele usuário, e
2. O envio dessa mensagem para esse usuário não fizer com que um limite seja atingido antes que uma mensagem subsequente de maior prioridade seja enviada.

### Como posso garantir que uma mensagem seja sempre enviada? {#how-can-i-make-sure-a-message-is-always-sent}

Pode haver cenários em que você deseja que uma mensagem seja sempre enviada, como no caso de notificações transacionais ou legais. Nesse caso, você deve remover a mensagem do limite de frequência (o que também a torna inelegível para a Priorização de Mensagens). Isso enviará a mensagem sempre que estiver agendada ou disparada, sem considerar o que mais está sendo enviado.

### Quando as mensagens são realmente priorizadas? Existe um cronograma? {#when-are-messages-actually-prioritized-is-there-a-schedule}

Cada mensagem é priorizada no seu próprio horário de envio agendado. Não existe um horário universal de avaliação para mensagens priorizadas.

### Minha mensagem estava agendada para envio, mas ainda não foi enviada por causa de limite de taxa ou outros atrasos. O que isso significa para a priorização de outras Campaigns? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

Assumiremos que sua mensagem foi enviada no horário originalmente agendado se ela ainda estiver sendo processada. Usaremos essa suposição para determinar se devemos enviar outras mensagens priorizadas futuras. Quando essa mensagem for efetivamente enviada, usaremos o horário real de envio.

### Minha mensagem foi priorizada, mas abortada no último minuto. O que isso significa para a priorização? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

Quando uma mensagem é priorizada, a Braze assumirá que ela foi enviada no horário originalmente agendado. De modo geral, para a Priorização de Mensagens, não recomendamos o uso de aborts via Liquid. Se uma mensagem for abortada devido à [lógica Liquid `abort_message`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/), assumiremos que ela foi enviada para aquele usuário e priorizaremos Campaigns futuras de acordo.

Digamos que você tenha duas mensagens: Mensagem 1 e Mensagem 2. Se a Mensagem 1 for abortada em favor de uma futura Mensagem 2 de maior prioridade, isso não garante que a Mensagem 2 será realmente enviada. A Mensagem 2 ainda pode ser abortada por qualquer motivo, incluindo:

- Aborts via Liquid
- O usuário não estar mais no Segment
- Limites de frequência por causa de uma mensagem fora das regras de priorização.

Se a Mensagem 2 for abortada, não haverá outra tentativa de enviar a Mensagem 1.

Observe que um usuário pode receber uma mensagem de menor prioridade, mas não uma mensagem de maior prioridade para a mesma regra de limite de frequência, pelos seguintes motivos:

- A mensagem de maior prioridade foi limitada por uma regra diferente.
- A mensagem de maior prioridade conflitou com outra Campaign futura de prioridade ainda maior para uma regra diferente.
- No momento do envio da mensagem de menor prioridade, o usuário não estava no público da mensagem de maior prioridade.
- Ambas as mensagens deveriam ter sido enviadas, mas uma mensagem fora da configuração de priorização foi enviada antes que a mensagem de maior prioridade pudesse ser enviada.

### Posso aderir Canvas à Priorização de Mensagens? {#can-i-opt-canvases-into-message-prioritization}

Não. Neste momento, você não pode aderir Canvas à Priorização de Mensagens.

### E quanto a Campaigns baseadas em ação ou disparadas por API? {#what-about-action-based-or-api-triggered-campaigns}

Neste momento, a Priorização de Mensagens não é compatível com Campaigns baseadas em ação ou disparadas por API.

### Existe alguma funcionalidade de relatórios ou análise de dados específica para a Priorização de Mensagens? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

Neste momento, não há funcionalidade de relatórios ou análise de dados específica para esse recurso. Recomendamos que você use a [funcionalidade de relatórios existente da Braze]({{site.baseurl}}/user_guide/analytics/reporting/) para monitorar a integridade e o desempenho das suas Campaigns priorizadas.