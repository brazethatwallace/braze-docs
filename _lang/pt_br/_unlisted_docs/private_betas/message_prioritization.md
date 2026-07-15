---
article_title: Priorização de mensagens
permalink: /message_prioritization/
toc_headers: h2
description: "Este artigo de referência descreve a priorização de mensagens de nível superior e como configurá-la para o seu espaço de trabalho."
---

# Priorização de mensagens {#message-prioritization}

> Use a priorização de mensagens para garantir que seus usuários recebam as campanhas mais importantes.

{% alert important %}
A priorização de mensagens está atualmente em beta. Entre em contato com o gerente da sua conta Braze se tiver interesse em participar deste beta.<br><br>Este artigo reflete a versão da priorização de mensagens planejada para lançamento em produção no final de julho de 2026. Alguns comportamentos descritos aqui podem ainda não estar disponíveis em todos os espaços de trabalho beta.
{% endalert %}

Apenas administradores podem configurar as definições de priorização de mensagens de nível superior. Usuários com permissões limitadas podem visualizar cada página nesta seção, mas não podem fazer alterações.

Para acessar as configurações de priorização de mensagens de nível superior, acesse **Settings** > **Message Prioritization**.

## Como funciona {#how-it-works}

Use a priorização de mensagens para criar [categorias](#categories) e [regras de priorização](#prioritization-rules) para classificar como suas mensagens são enviadas.

Uma marca de beleza que gerencia promoções por e-mail para parcerias pagas e programas de fidelidade usa a priorização de mensagens para criar duas categorias chamadas "Paid Partnerships" e "Loyalty". A marca classifica essas categorias com base em qual é mais crítica para o negócio. Durante a temporada de festas, a marca classifica "Loyalty" acima de "Paid Partnerships" para priorizar os clientes que fazem parte do programa de membros há mais de um ano.

![Um exemplo de regras de priorização para duas categorias: Paid Partnerships e Loyalty.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

No momento do envio, a Braze compara a mensagem sendo enviada com outras mensagens que o usuário pode receber e que aderiram à priorização, possuem uma categoria de prioridade definida e contam para a mesma regra de limite de frequência dentro da mesma janela de limite de frequência. Se o envio da mensagem atual impedir que uma mensagem de maior prioridade seja enviada posteriormente, a Braze desprioriza a mensagem de menor prioridade. Dependendo do período de nova tentativa configurado, essa mensagem de menor prioridade é tentada novamente mais tarde ou não é enviada.

A priorização de mensagens pode avaliar:

- Campaigns agendadas
- Campaigns baseadas em ação
- Canvas

A Braze usa sua previsão de quando cada mensagem deve ser enviada ao avaliar se o envio de uma mensagem agora poderia impedir que uma mensagem de maior prioridade seja enviada posteriormente. Para saber mais sobre como a Braze prevê o momento de envio futuro para Campaigns e Canvas, consulte [Como a Braze prevê quando uma mensagem futura será enviada?](#how-does-braze-predict-when-a-future-message-sends)

### Tipos de mensagem compatíveis {#supported-message-types}

A priorização de mensagens é compatível com os mesmos canais do limite de frequência:

- Notificações por push
- E-mail
- SMS
- Webhooks
- WhatsApp
- LINE

Para priorização e limite de frequência, push iOS, push Android, web push e outras plataformas de notificação por push são tratadas como um único canal de push compartilhado, e não como canais separados.

## Categorias {#categories}

As regras de priorização são baseadas em uma classificação de categorias, que é um rótulo que você pode atribuir a uma determinada Campaign ou Canvas (semelhante a uma [tag]({{site.baseurl}}/user_guide/administrative/app_settings/tags)). Você pode criar até 20 categorias por vez.

Para adicionar uma nova categoria:

1. Acesse **Settings** > **Message Prioritization** > **Categories**.
2. Selecione **Create new category**.

![O botão "Create new category" na seção de priorização de mensagens.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Dê um nome à categoria e uma descrição opcional.
4. Selecione **Create category**.

![Um exemplo de categoria chamada "P3" com a descrição "This is my third highest priority category."]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

Para editar ou excluir uma categoria, selecione o menu <i class="fas fa-ellipsis-vertical"></i>.

## Regras de priorização {#prioritization-rules}

Depois que suas categorias estiverem configuradas, você pode classificá-las em um conjunto de regras de priorização. As regras são classificadas em ordem decrescente de prioridade. Você pode criar até 10 regras de priorização por vez.

1. Acesse **Settings** > **Message Prioritization** > **Prioritization Rules** para configurar suas regras.

![Seção "Prioritization Rules" sem prioridades definidas ainda.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization4.png %})

{:start="2"}
2. Selecione **Add rule**.
3. Selecione uma categoria no menu suspenso.

![Regra de priorização "Priority 1" com P1 selecionado como categoria.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization5.png %})

{:start="4"}
4. Continue adicionando regras selecionando **+ Add rule** abaixo da sua última regra.

Para reordenar as regras, selecione e arraste o ícone <i class="fa-solid fa-grip-vertical"></i> em uma regra. Para excluir uma regra, selecione o menu <i class="fas fa-ellipsis-vertical"></i> e depois **Delete Rule**.

Não se esqueça de selecionar **Save** para que suas atualizações sejam aplicadas.

## Configurações no nível da Campaign {#campaign-level-settings}

### Adesão {#opt-in}

Para aderir uma Campaign à priorização, marque a caixa de seleção **Opt-in to Message Prioritization** nas configurações de entrega da Campaign.

![A caixa de seleção para "Opt-in to Message Prioritization".]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

Em seguida, atribua a Campaign a uma categoria selecionando uma no menu suspenso **Category**.

![O menu suspenso de categoria da priorização de mensagens nas configurações de entrega de uma Campaign.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

A priorização de mensagens é compatível com Campaigns agendadas e Campaigns baseadas em ação.

### Intelligent Timing

Para Campaigns que usam Intelligent Timing, a priorização de mensagens compara as mensagens usando o horário de envio que a Braze seleciona para cada usuário, em vez de usar apenas o cronograma original da Campaign. Isso permite que a Braze considere a mensagem com maior probabilidade de ser enviada primeiro para aquele usuário.

Para Campaigns recorrentes com Intelligent Timing, a Braze pode usar o horário de envio conhecido selecionado para a recorrência atual ao comparar essa Campaign com outras mensagens priorizadas elegíveis.

### Período de nova tentativa {#retry-window}

Um período de nova tentativa permite que mensagens que aderiram à priorização tentem novamente por até três dias se a primeira tentativa não tiver prioridade alta o suficiente para enviar. Em cada dia subsequente, no mesmo horário em que a mensagem foi originalmente agendada ou disparada, o envio é tentado novamente. Após o último dia do período de nova tentativa, se a mensagem ainda não tiver sido enviada, ela não será mais tentada e será permanentemente despriorizada.

Para Campaigns agendadas recorrentes, o período de nova tentativa deve ser menor que o intervalo mínimo entre envios dessa Campaign. As novas tentativas sempre acontecem um dia por vez a partir do horário de envio original, mesmo que a Campaign normalmente não esteja agendada para enviar naquele dia. Por exemplo, se você tem uma Campaign que envia toda segunda e quarta-feira, a tentativa de nova tentativa ocorre na terça-feira, então o período de nova tentativa deve ser definido como um dia. Se você tem uma Campaign que envia toda segunda, quarta e sexta-feira, e o envio de sexta-feira é tentado novamente com um período de nova tentativa de um dia, a nova tentativa ocorre no sábado, não na segunda-feira.

![A configuração "Retry Window" definida como 1 dia.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

Para Campaigns baseadas em ação, as novas tentativas são baseadas no horário em que a mensagem disparada deveria ter sido enviada originalmente.

Campaigns baseadas em ação que usam eventos de exceção não são compatíveis com períodos de nova tentativa.

Os períodos de nova tentativa para mensagens do Canvas são configurados no nível da etapa. Para etapas de mensagem do Canvas compatíveis, se uma etapa de mensagem do Canvas for despriorizada e tiver um período de nova tentativa configurado, a Braze pode tentar novamente essa etapa mais tarde dentro do período de nova tentativa.

## Configurações no nível do Canvas {#canvas-level-settings}

Para aderir um Canvas à priorização de mensagens, ative a priorização de mensagens nas configurações do Canvas e atribua o Canvas a uma categoria.

Quando um usuário é elegível para múltiplas mensagens priorizadas, a Braze avalia Campaigns que aderiram e etapas de mensagem elegíveis do Canvas juntas nos canais compatíveis.

Para Campaigns, isso inclui envios agendados e baseados em ação elegíveis.

Para Canvas, isso inclui:

- Canvas agendados futuros para os quais o usuário é elegível para entrar
- Canvas nos quais o usuário está atualmente

A priorização do Canvas não é tudo ou nada. Uma Campaign de maior prioridade pode fazer com que uma etapa do Canvas seja despriorizada, enquanto etapas elegíveis posteriores nesse mesmo Canvas ainda podem ser enviadas, dependendo da classificação de categoria, do momento de envio e das regras de limite de frequência.

### Como a Braze avalia mensagens futuras {#how-braze-evaluates-future-messages}

A Braze avalia Campaigns e Canvas de maneiras diferentes com base no tipo de mensagem.

#### Campaigns

A Braze compara cada mensagem elegível de Campaign usando o horário em que essa mensagem deve ser enviada.

#### Canvas {#canvases}

A Braze percorre o Canvas para determinar quais mensagens futuras um usuário pode receber, começando por:

- Entrada no Canvas, para Canvas agendados futuros
- A etapa atual do usuário, se o usuário já estiver no Canvas

A Braze então avalia as etapas do Canvas das seguintes maneiras.

##### Etapas de envio de mensagens {#messaging-steps}

Essas etapas são contabilizadas para a priorização e adicionadas ao conjunto de mensagens elegíveis quando enviam em um canal compatível.

- Etapa de mensagem
- Etapa do Otimizador de Conteúdo

##### Etapas de continuação {#continuation-steps}

Essas etapas são ignoradas para a priorização e não afetam a análise antecipada.

- Etapa de atualização de contexto
- Etapa de atualização de usuário
- Etapa de sincronização de público
- Etapa de Feature Flag
- Etapa de postergação com atraso fixo

##### Etapas de limite {#boundary-steps}

A Braze interrompe a análise antecipada nessas etapas até que o usuário realmente avance por elas no Canvas.

- Etapa de postergação com atraso personalizado
- Etapa de postergação que segue uma etapa de ramificação
- Etapa de jornada de ação
- Etapa de experimento

##### Etapas de ramificação {#branching-steps}

Essas etapas dividem o Canvas em múltiplos caminhos possíveis.

- Etapa de divisão de decisão
- Etapa de jornada do público

Quando um caminho de priorização contém etapas de ramificação, a Braze assume que todos os caminhos são viáveis e considera todas as etapas de mensagem paralelas em canais compatíveis para a priorização. Como as regras de limite de frequência podem ser específicas por canal, as etapas de mensagem paralelas são deduplicadas por canal quando necessário.

Por exemplo, se uma ramificação pode enviar e-mail e outra ramificação também pode enviar e-mail, a Braze trata essas como um único envio de e-mail possível para a priorização antecipada. Se outra ramificação pode enviar push, a Braze também considera esse possível envio de push separadamente.

Para etapas de mensagem do Canvas que usam Intelligent Timing, a Braze prevê o momento do envio com base no melhor esforço até que o usuário realmente alcance essa etapa. Quando o usuário entra na etapa de Intelligent Timing e a Braze calcula o horário de envio por usuário, a priorização de mensagens usa esse horário calculado para a etapa atual. Em caminhos determinísticos, a Braze também reflete esse momento atualizado nas etapas de mensagem seguintes ao determinar seus horários de envio esperados.

As etapas do Otimizador de Conteúdo são tratadas como etapas de envio de mensagens porque sempre enviam em um canal especificado. No entanto, os períodos de nova tentativa não se aplicam às etapas do Otimizador de Conteúdo porque tentar novamente interferiria no experimento. Outras etapas de envio de mensagens do Canvas compatíveis podem usar períodos de nova tentativa. Etapas do Canvas em canais não compatíveis não participam da priorização de mensagens.

## Limites de frequência {#frequency-caps}

A priorização de mensagens funciona dentro das suas regras de limite de frequência existentes. Uma mensagem priorizada só pode ser enviada se:

1. A regra de limite de frequência relevante ainda não tiver sido atingida para aquele usuário, e
2. O envio dessa mensagem não fizer com que o usuário atinja um limite antes que uma mensagem posterior de maior prioridade possa ser enviada.

Mensagens que não estão sujeitas ao limite de frequência não são elegíveis para a priorização de mensagens. Se você deseja que uma mensagem seja sempre enviada, remova-a do limite de frequência. Isso também a remove da priorização de mensagens.

### Para Campaigns e etapas do Canvas compatíveis {#for-supported-campaigns-and-canvas-steps}

Para ser elegível à priorização de mensagens, a Campaign ou etapa do Canvas deve usar um canal compatível e ser avaliada dentro da sua configuração de limite de frequência.

![Um exemplo de regra de limite de frequência.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

### Regras de limite de frequência {#frequency-capping-rules}

A Braze otimiza a prioridade dentro das suas regras de limite de frequência existentes. Mensagens priorizadas são comparadas apenas quando compartilham a mesma regra de limite de frequência aplicável.

Por exemplo, duas Campaigns de e-mail que contam para a mesma regra de limite de frequência de e-mail podem ser priorizadas uma em relação à outra. Uma Campaign de e-mail de menor prioridade não é despriorizada em favor de uma mensagem SMS de maior prioridade, a menos que ambas as mensagens contem para a mesma regra de limite de frequência.

Você pode usar regras de limite de frequência específicas por canal, regras específicas por categoria, filtros de tag ou regras que se aplicam a qualquer canal. A priorização de mensagens funciona com quaisquer regras que se apliquem às suas mensagens que aderiram.

Você pode criar regras de limite de frequência por categoria para gerenciar quantas mensagens um usuário recebe de uma determinada categoria. Isso ajuda a evitar que uma categoria de alta prioridade envie mensagens em excesso. Selecione **Message prioritization category** em **Additional filters** e selecione uma categoria no menu suspenso.

![Um exemplo de regra de limite de frequência com o menu suspenso do campo "Category" para selecionar P2 ou P1.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

Mensagens fora da priorização de mensagens compartilham os limites de frequência com mensagens priorizadas, então mesmo uma mensagem de alta prioridade pode sofrer interrupção devido a uma mensagem fora da priorização de mensagens.

## Exemplos {#examples}

### Campaign de maior prioridade versus Campaign de menor prioridade {#higher-priority-campaign-versus-lower-priority-campaign}

Suponha que um usuário seja elegível para duas Campaigns de e-mail no mesmo dia, e ambas contem para a mesma regra de limite de frequência. Se a Campaign de maior prioridade deve ser enviada mais tarde naquele dia, a Braze pode despriorizar a Campaign de menor prioridade para que a Campaign de maior prioridade possa ser enviada. Se a Campaign de menor prioridade tiver um período de nova tentativa, a Braze pode tentar novamente mais tarde.

### Campaign baseada em ação de maior prioridade versus mensagem de menor prioridade {#higher-priority-action-based-campaign-versus-lower-priority-message}

Suponha que um usuário dispare uma Campaign baseada em ação de maior prioridade que está configurada para enviar duas horas depois. Durante esse atraso, a Braze pode considerar essa Campaign baseada em ação futura ao decidir se outra mensagem priorizada deve ser enviada primeiro. Isso ajuda a evitar que uma mensagem de menor prioridade seja enviada agora se a Campaign baseada em ação de maior prioridade deve ser enviada em breve.

### Canvas de maior prioridade versus Campaign de menor prioridade {#higher-priority-canvas-versus-lower-priority-campaign}

Suponha que um usuário seja elegível para uma Campaign de menor prioridade, mas também deva receber uma mensagem de Canvas de maior prioridade mais tarde naquele dia. Se a Braze já puder avaliar essa mensagem futura do Canvas, ela pode despriorizar a Campaign de menor prioridade para que a mensagem de Canvas de maior prioridade possa ser enviada.

### Canvas de maior prioridade com etapa de limite versus Campaign de menor prioridade {#higher-priority-canvas-with-a-boundary-step-versus-lower-priority-campaign}

Suponha que um Canvas de maior prioridade inclua uma etapa de jornada de ação, um experimento ou uma postergação personalizada antes da próxima etapa de mensagem. Até que o usuário alcance e passe por essa etapa, a Braze não faz a análise antecipada da mensagem de maior prioridade do Canvas a jusante. Nesse caso, uma Campaign de menor prioridade ainda pode ser enviada primeiro.

### Canvas de ramificação de maior prioridade versus mensagem de menor prioridade {#higher-priority-branching-canvas-versus-lower-priority-message}

Suponha que um Canvas de maior prioridade possa enviar mensagens diferentes dependendo de qual ramificação o usuário segue. A Braze avalia esses possíveis caminhos futuros de forma conservadora ao comparar mensagens. Isso ajuda a evitar que uma mensagem de menor prioridade seja enviada agora se uma ramificação de Canvas de maior prioridade puder usar o mesmo limite de frequência posteriormente.

### Etapa de Intelligent Timing do Canvas e etapas a jusante {#canvas-intelligent-timing-step-and-downstream-steps}

Suponha que um usuário entre em uma etapa de mensagem de Canvas de maior prioridade que usa Intelligent Timing. Quando a Braze calcula o horário de envio daquele usuário para a etapa de Intelligent Timing, a priorização de mensagens usa esse horário de envio por usuário para a etapa atual e para etapas de mensagem posteriores no mesmo caminho determinístico. Isso ajuda a Braze a comparar mensagens do Canvas a jusante com outros envios priorizados usando o momento atualizado, em vez de apenas a estimativa anterior do caminho.

## Limitações {#limitations}

A priorização de mensagens tem as seguintes limitações:

- Até 20 categorias por espaço de trabalho
- Até 10 regras de priorização por espaço de trabalho
- Até 25 itens agendados ativos que aderiram à priorização por vez
- Até 25 itens baseados em ação ativos que aderiram à priorização por vez
- Períodos de nova tentativa de até 3 dias

O limite de itens agendados é um total combinado de Campaigns agendadas e Canvas agendados que aderiram. O limite de itens baseados em ação é um total combinado de Campaigns baseadas em ação e Canvas baseados em ação que aderiram.

## Perguntas frequentes {#frequently-asked-questions}

### Como os empates são resolvidos entre mensagens na mesma categoria? {#how-are-ties-broken-between-messages-in-the-same-category}

Ao priorizar duas Campaigns na mesma categoria, a Braze dá maior prioridade à que tem o horário de envio mais cedo. Se um período de nova tentativa estiver configurado, a Braze usa o final desse período de nova tentativa ao comparar Campaigns dentro da mesma regra de prioridade. Para Campaigns recorrentes, o horário de envio é calculado como a próxima ocorrência a partir da meia-noite no horário da empresa. Para Campaigns agendadas no fuso local, a Braze assume um horário de envio no horário da empresa.

Para Canvas na mesma categoria, a Braze usa o momento de entrada no Canvas como critério de desempate, de modo que todas as etapas no mesmo Canvas preservem a mesma prioridade relativa em relação a outras Campaigns e Canvas.

### Como posso garantir que uma mensagem seja sempre enviada? {#how-can-i-make-sure-a-message-is-always-sent}

Pode haver cenários em que você deseja que uma mensagem seja sempre enviada, como no caso de notificações transacionais ou legais. Nesse caso, você deve remover a mensagem do limite de frequência, o que também a torna inelegível para a priorização de mensagens. Isso enviará a mensagem sempre que estiver agendada ou disparada, sem considerar o que mais está sendo enviado.

### Quando as mensagens são realmente priorizadas? Existe um cronograma? {#when-are-messages-actually-prioritized-is-there-a-schedule}

Cada mensagem é priorizada com base em quando deve ser enviada. Não existe um horário universal de avaliação para mensagens priorizadas.

### Como a Braze prevê quando uma mensagem futura será enviada? {#how-does-braze-predict-when-a-future-message-sends}

A Braze prevê o momento de envio futuro de maneiras diferentes para cada tipo de mensagem:

- **Campaigns agendadas:** a Braze usa o horário em que cada Campaign deve ser enviada. Para Campaigns agendadas que usam Intelligent Timing, a Braze usa o horário de envio ideal de cada usuário para aquela ocorrência da Campaign.
- **Campaigns baseadas em ação:** a Braze usa o horário em que cada mensagem disparada deve ser enviada, incluindo qualquer atraso configurado entre o disparo e o envio.
- **Etapas do Canvas:** a Braze usa a entrada do usuário no Canvas ou a posição atual no Canvas, mais o momento das etapas a jusante. Para etapas de mensagem do Canvas que usam Intelligent Timing, quando o usuário entra nessa etapa, a Braze usa o horário de envio por usuário que calcula para aquele usuário. Para etapas de mensagem seguintes no mesmo caminho de priorização determinístico, a Braze usa esse horário de envio do Intelligent Timing ao determinar o momento de envio esperado posterior. Antes de o usuário alcançar a etapa de Intelligent Timing, a previsão permanece com base no melhor esforço.

### Minha mensagem estava agendada para envio, mas ainda não foi enviada por causa de limite de frequência ou outros atrasos. O que isso significa para a priorização de outras campanhas? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

A Braze assume que sua mensagem foi enviada no horário originalmente agendado se ela ainda estiver sendo processada, o que determina se outras mensagens priorizadas futuras devem ser enviadas. Quando essa mensagem for efetivamente enviada, a Braze usa o horário real de envio.

### Minha mensagem foi priorizada, mas sofreu interrupção no último minuto. O que isso significa para a priorização? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

Quando uma mensagem é priorizada, a Braze assume que ela foi enviada no horário originalmente agendado. De modo geral, para a priorização de mensagens, não recomendamos o uso de interrupções via Liquid. Se uma mensagem for interrompida devido à [lógica Liquid `abort_message`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages), a Braze assume que ela foi enviada para aquele usuário e prioriza Campaigns futuras de acordo.

Digamos que você tenha duas mensagens: Mensagem 1 e Mensagem 2. Se a Mensagem 1 for interrompida em favor de uma futura Mensagem 2 de maior prioridade, isso não garante que a Mensagem 2 será realmente enviada. A Mensagem 2 ainda pode ser interrompida por qualquer motivo, incluindo:

- Interrupções via Liquid
- O usuário não estar mais no Segment
- Limites de frequência por causa de uma mensagem fora das regras de priorização.

Se a Mensagem 2 for interrompida, não haverá outra tentativa de enviar a Mensagem 1.

Observe que um usuário pode receber uma mensagem de menor prioridade, mas não uma mensagem de maior prioridade para a mesma regra de limite de frequência, pelos seguintes motivos:

- A mensagem de maior prioridade foi limitada por uma regra diferente.
- A mensagem de maior prioridade conflitou com outra Campaign futura de prioridade ainda maior para uma regra diferente.
- No momento do envio da mensagem de menor prioridade, o usuário não estava no público da mensagem de maior prioridade.
- Ambas as mensagens deveriam ter sido enviadas, mas uma mensagem fora da configuração de priorização foi enviada antes que a mensagem de maior prioridade pudesse ser enviada.

### Como as etapas de limite afetam a priorização do Canvas? {#how-do-boundary-steps-affect-canvas-prioritization}

As etapas de limite interrompem a análise antecipada do Canvas até que o usuário realmente alcance ou conclua aquele ponto no Canvas. Por exemplo, se uma mensagem de maior prioridade está após uma etapa de jornada de ação, uma postergação personalizada ou uma etapa de experimento, a Braze não usa essa mensagem a jusante para bloquear uma Campaign de menor prioridade até que o usuário tenha passado por esse limite.

### Como a ramificação funciona na priorização do Canvas? {#how-does-branching-work-in-canvas-prioritization}

Quando um Canvas contém caminhos de ramificação, a Braze assume que cada caminho é viável e compara o maior volume de envio futuro possível por canal. Isso ajuda a evitar o envio de uma mensagem de menor prioridade agora se um caminho de Canvas de maior prioridade puder consumir o mesmo limite de frequência posteriormente.

### O que acontece se um usuário tem múltiplos caminhos em um Canvas priorizado ao mesmo tempo? {#what-happens-if-a-user-has-multiple-paths-through-a-prioritized-canvas-at-the-same-time}

A Braze trata cada caminho viável como um possível caminho futuro e avalia as etapas de mensagem elegíveis nesses caminhos de forma independente. Quando múltiplos caminhos podem enviar no mesmo canal, a Braze deduplica esses possíveis envios por canal quando necessário.

### Como o Intelligent Timing funciona na priorização do Canvas? {#how-does-intelligent-timing-work-in-canvas-prioritization}

Antes de um usuário alcançar uma etapa de mensagem do Canvas com Intelligent Timing, a Braze prevê o momento dessa etapa com base no melhor esforço. Quando o usuário entra na etapa e a Braze calcula o horário de envio por usuário, a priorização de mensagens usa esse horário calculado para a etapa atual e para etapas de mensagem seguintes no mesmo caminho de priorização determinístico.

### Existe alguma funcionalidade de relatórios ou análise de dados específica para a priorização de mensagens? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

A Braze fornece eventos relacionados à priorização de mensagens no Currents e no compartilhamento de dados para canais compatíveis, incluindo e-mail, LINE, notificações por push, SMS, webhooks e WhatsApp. Esses eventos incluem eventos de despriorização e limite de frequência, registrados na tabela `users.messages.<channel>.abort`, bem como eventos de nova tentativa que mostram quando uma mensagem foi tentada novamente dentro do período de nova tentativa configurado, registrados na tabela `user_messages_<channel>_retry`.

Para Campaigns, você também pode usar o dashboard de diagnóstico de envio de mensagens, as estatísticas diárias existentes de despriorização e nova tentativa, e a [funcionalidade de relatórios existente da Braze]({{site.baseurl}}/user_guide/analytics/reporting) para monitorar a integridade e o desempenho das suas Campaigns e Canvas priorizados.