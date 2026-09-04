---
article_title: Priorização de mensagens
permalink: /message_prioritization/
toc_headers: h2
description: "Este artigo de referência descreve a priorização de mensagens de nível superior e como configurá-la para o seu espaço de trabalho."
---

# Priorização de mensagens {#message-prioritization}

> Use a priorização de mensagens para garantir que os usuários recebam as mensagens mais importantes para o seu negócio, e não apenas aquelas que são enviadas primeiro.

{% alert important %}
A priorização de mensagens está atualmente em beta. Entre em contato com o gerente da sua conta Braze se tiver interesse em participar deste beta.<br><br>Este artigo reflete a versão da priorização de mensagens planejada para lançamento em produção no final de julho de 2026. Alguns comportamentos descritos aqui podem ainda não estar disponíveis em todos os espaços de trabalho beta.
{% endalert %}

## Por que usar a Priorização de Mensagens? {#why-use-message-prioritization}

Os usuários só conseguem receber uma certa quantidade de mensagens antes que o volume se torne um problema. As mensagens que chegam até eles devem ser aquelas que mais importam para o seu negócio. A Priorização de Mensagens ajuda a garantir que suas mensagens de maior valor ocupem esse espaço limitado, em vez de deixar isso ao acaso.

A maioria das equipes controla o volume de mensagens com limites de frequência. Por si só, os limites de frequência são uma ferramenta imprecisa. Quando um usuário atinge o limite, o horário de envio decide quais mensagens são entregues, e não a importância para o negócio.

Uma promoção de baixo valor disparada primeiro pode ocupar um espaço que uma recompensa de fidelidade ou uma mensagem urgente teria usado mais tarde naquele dia. As equipes frequentemente contornam isso com regras de limite separadas, agendamento manual e filtros ad-hoc. Essas abordagens exigem manutenção constante. Elas ficam mais difíceis de gerenciar à medida que Campaigns e Canvas mudam. E ainda assim não conseguem garantir que a mensagem certa seja a vencedora.

A Priorização de Mensagens muda a alocação de limites de frequência de **primeiro a chegar, primeiro a ser servido** para **consciente da prioridade de negócio**: você classifica o que importa, e a Braze toma as decisões de envio por você.

A Priorização de Mensagens oferece diversos benefícios:

- **Defina o que importa uma única vez:** Use categorias e regras classificadas para codificar suas prioridades — por exemplo, "Fidelidade" acima de "Parcerias Pagas". Todo envio com aceitação respeita essas classificações automaticamente.
- **Decisões voltadas para o futuro:** A Braze prevê o que um usuário pode receber depois. Ela pode reter uma mensagem de menor prioridade para preservar espaço no limite para uma de maior prioridade.
- **Funciona em diferentes tipos de mensagens e canais:** Campaigns agendadas, Campaigns baseadas em ação e etapas do Canvas competem em um único pool classificado dentro dos seus limites de frequência compartilhados.
- **Janelas de nova tentativa:** Uma mensagem despriorizada pode tentar novamente se houver capacidade disponível. Isso melhora o mix de mensagens sem descartar completamente os envios de menor prioridade.

O resultado é o mesmo volume de envio com limite, alocado automaticamente para as mensagens que mais importam.

A Priorização de Mensagens é mais valiosa para remetentes de alto volume que atingem limites de frequência regularmente. Ela funciona melhor quando o valor da mensagem é claramente diferenciado — por exemplo, mensagens de fidelidade ou que geram receita versus promoções rotineiras.

## Como funciona {#how-it-works}

Use a Priorização de Mensagens para criar [categorias](#categories) e [regras de priorização](#prioritization-rules) para classificar como suas mensagens são enviadas.

Para gerenciar essas configurações, acesse **Configurações** > **Priorização de Mensagens**. Somente administradores podem configurar as definições de nível superior da Priorização de Mensagens. Os usuários precisam da permissão `View Message Prioritization` para visualizar as configurações nesta seção e da permissão `Edit Message Prioritization` para editá-las.

Por exemplo, uma marca de beleza que gerencia promoções de e-mail para parcerias pagas e programas de fidelidade usa a Priorização de Mensagens para criar duas categorias: "Parcerias Pagas" e "Fidelidade". A marca classifica essas categorias por importância para o negócio. Durante a temporada de festas, ela classifica "Fidelidade" em primeiro e "Parcerias Pagas" em segundo para priorizar membros de longo prazo.

![Exemplo de regras de priorização para duas categorias: Parcerias Pagas e Fidelidade.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

No momento do envio, a Braze compara a mensagem sendo enviada com outras mensagens que o usuário pode receber e que estão incluídas na priorização, têm uma categoria de prioridade definida e contam para a mesma regra de limite de frequência dentro da mesma janela de limite de frequência. Se o envio da mensagem atual impedir que uma mensagem de maior prioridade seja enviada posteriormente, a Braze reduz a prioridade da mensagem de menor prioridade. Dependendo da janela de reenvio configurada, essa mensagem de menor prioridade é reenviada posteriormente ou não é enviada.

A Priorização de Mensagens pode avaliar:

- Campaigns agendadas
- Campaigns baseadas em ação
- Canvas

Atualmente, Campaigns ou Canvas disparados por API não são compatíveis com a Priorização de Mensagens e não participam da priorização.

A Braze usa sua previsão de quando cada mensagem deve ser enviada ao avaliar se o envio de uma mensagem agora poderia impedir que uma mensagem de maior prioridade seja enviada depois. Para saber mais sobre como a Braze prevê o momento de envio futuro para Campaigns e Canvas, consulte [Como a Braze prevê quando uma mensagem futura será enviada?](#how-does-braze-predict-when-a-future-message-sends)

### Canais de mensagem compatíveis {#supported-message-channels}

A Priorização de Mensagens é compatível com os mesmos canais do limite de frequência:

- Notificações por push
- E-mail
- SMS
- Webhooks
- WhatsApp
- LINE

Para priorização e limite de frequência, push iOS, push Android, web push e outras plataformas de notificação por push são tratados como um único canal de push compartilhado, e não como canais separados.

Estes canais não são elegíveis para a Priorização de Mensagens porque não estão sujeitos ao limite de frequência:

- Content Cards
- In-App Messages
- Banners

In-App Messages e Banners usam suas próprias configurações de prioridade para decidir qual mensagem é exibida quando várias mensagens competem pelo mesmo disparador ou posicionamento. Para In-App Messages, consulte [Escolher uma prioridade]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority). Para Banners, consulte [Prioridade de Banners]({{site.baseurl}}/user_guide/channels/banners#priority).

Se uma Campaign ou etapa do Canvas usa apenas canais não elegíveis, ela não participará da priorização.

## Categorias {#categories}

As regras de priorização são baseadas em um ranqueamento de categorias, que são rótulos que você pode atribuir a uma determinada Campaign ou Canvas (semelhante a uma [tag]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)). Existe um limite para o número de categorias que você pode criar em um determinado momento; fale com seu gerente de conta se precisar de um limite maior.

Para adicionar uma nova categoria:

1. Acesse **Configurações** > **Priorização de mensagens** > **Categorias**.
2. Selecione **Criar nova categoria**.

![O botão "Criar nova categoria" na seção Priorização de mensagens.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Dê um nome à categoria e uma descrição opcional.
4. Selecione **Criar categoria**.

![Um exemplo de categoria chamada "P3" com a descrição "Esta é minha terceira categoria de maior prioridade."]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

Para editar ou excluir uma categoria, selecione o menu <i class="fas fa-ellipsis-vertical" aria-label="Abrir menu de opções"></i>.

## Regras de priorização {#prioritization-rules}

Depois que suas categorias estiverem configuradas, você pode classificá-las em um conjunto de regras de priorização. As regras são classificadas em ordem decrescente de prioridade. Há um limite para o número de regras de priorização que você pode criar em um determinado momento; fale com seu gerente de conta se quiser um limite maior.

1. Acesse **Configurações** > **Priorização de mensagens** > **Regras de priorização** para configurar suas regras.

![Seção "Regras de priorização" sem nenhuma prioridade definida ainda.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization4.png %})

{:start="2"}
2. Selecione **Adicionar regra**.
3. Selecione uma categoria no menu suspenso.

![Regra de priorização "Prioridade 1" com P1 selecionada como categoria.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization5.png %})

{:start="4"}
4. Continue adicionando regras selecionando **+ Adicionar regra** abaixo da sua última regra.

Para reordenar as regras, selecione e arraste o ícone <i class="fa-solid fa-grip-vertical" aria-label="Arrastar para reordenar"></i> em uma regra. Para excluir uma regra, selecione o menu <i class="fas fa-ellipsis-vertical" aria-label="Mais opções"></i> e depois **Excluir regra**.

Não se esqueça de selecionar **Salvar** para que suas atualizações sejam aplicadas.

## Limites de frequência {#frequency-caps}

A Priorização de Mensagens funciona dentro das suas regras de limite de frequência existentes. Para ser elegível para priorização, uma Campaign ou etapa do Canvas deve usar um canal compatível e estar sujeita à sua configuração de limite de frequência. Mensagens que não estão sujeitas ao limite de frequência não são elegíveis para a Priorização de Mensagens. Se você deseja que uma mensagem seja sempre enviada, desative o limite de frequência para ela. Isso também a remove da Priorização de Mensagens.

Uma mensagem priorizada só pode ser enviada se:

1. A regra de limite de frequência relevante ainda não tiver sido atingida para esse usuário, e
2. O envio dessa mensagem não fizer com que o usuário atinja um limite antes que uma mensagem posterior de maior prioridade possa ser enviada.

![Um exemplo de regra de limite de frequência.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

Você pode usar regras de limite de frequência específicas por canal, regras específicas por categoria, filtros de tag ou regras que se aplicam a qualquer canal. A Priorização de Mensagens funciona com quaisquer regras que se apliquem às suas mensagens com aceitação ativada.

Você também pode criar regras de limite de frequência por categoria para gerenciar quantas mensagens um usuário recebe de uma determinada categoria. Isso ajuda a evitar que uma categoria de alta prioridade envie mensagens em excesso. Selecione **Message prioritization category** em **Additional filters** e selecione uma categoria no menu suspenso.

![Um exemplo da regra de limite de frequência com o menu suspenso do campo "Category" para selecionar P2 ou P1.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

## Aceitação {#opting-in}

### Aceitação de Campaign {#campaign-opt-in}

Para incluir uma Campaign na priorização, marque a caixa de seleção **Opt-in to Message Prioritization** nas configurações de entrega da Campaign.

![A caixa de seleção para "Opt-in to Message Prioritization".]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

Em seguida, atribua a Campaign a uma categoria selecionando uma no menu suspenso **Category**.

![O menu suspenso de categoria de priorização de mensagens nas configurações de entrega de uma Campaign.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

A priorização de mensagens é compatível com Campaigns agendadas e Campaigns baseadas em ação. Campaigns disparadas por API não são compatíveis.

### Aceitação de Canvas {#canvas-opt-in}

A aceitação de Canvas funciona de forma semelhante às Campaigns. Para incluir um Canvas na priorização de mensagens, ative a priorização de mensagens nas configurações do Canvas e atribua o Canvas a uma categoria. Todas as etapas do Canvas compartilham essa categoria e o mesmo nível de prioridade, o que significa que não é possível definir a prioridade individualmente por etapa.

A priorização de mensagens é compatível com Canvas agendados e Canvas baseados em ação. Canvas disparados por API não são compatíveis.

## Intelligent Timing {#intelligent-timing}

Com o Intelligent Timing, a Braze envia uma mensagem no horário ideal de envio de cada usuário, então a mesma Campaign ou etapa de mensagem do Canvas pode alcançar diferentes usuários em horários diferentes. A Priorização de Mensagens leva isso em conta: em vez de assumir que a mensagem é enviada para todos no horário agendado, ela classifica as mensagens concorrentes de um usuário usando o horário ideal de envio desse usuário.

Para Campaigns e etapas de mensagem do Canvas que usam Intelligent Timing, a Braze prevê o horário de envio com base no melhor esforço até calcular o horário de envio por usuário para cada um. Para Campaigns, a Priorização de Mensagens usa o horário ideal de envio desse usuário para a ocorrência atual ao comparar a Campaign com as outras mensagens priorizadas elegíveis do usuário. Para Campaigns recorrentes com Intelligent Timing, a Braze usa o horário ideal de envio escolhido para aquela ocorrência.

Para etapas de mensagem do Canvas, a Braze atualiza essa previsão assim que o usuário entra na etapa e a Braze calcula o horário ideal de envio desse usuário para a etapa. A Priorização de Mensagens usa esse horário de envio calculado para a etapa atual. Em jornadas determinísticas (jornadas sem Branch, onde a sequência de etapas é fixa), a Braze também reflete esse horário atualizado nas etapas de mensagem seguintes ao determinar os horários de envio esperados.

## Janelas de nova tentativa {#retry-windows}

Uma janela de nova tentativa permite que mensagens com aceitação façam novas tentativas por um número limitado de dias se a primeira tentativa não tiver prioridade alta o suficiente para ser enviada. O comprimento máximo da janela de nova tentativa depende da sua edição da plataforma Braze. Em cada dia subsequente, no mesmo horário em que a mensagem foi originalmente agendada ou disparada para envio, a mensagem é tentada novamente. Após o último dia na janela de nova tentativa, se a mensagem ainda não tiver sido enviada, nenhuma nova tentativa será feita e a mensagem será permanentemente despriorizada.

Para Campaigns recorrentes agendadas, a janela de nova tentativa deve ser mais curta do que o tempo mínimo entre envios dessa Campaign. As novas tentativas sempre acontecem um dia por vez a partir do horário de envio original, mesmo que a Campaign não esteja normalmente agendada para envio naquele dia. Por exemplo, se você tem uma Campaign que envia toda segunda e quarta-feira, a nova tentativa ocorre na terça-feira, então a janela de nova tentativa deve ser configurada para um dia. Se você tem uma Campaign que envia toda segunda, quarta e sexta-feira, e o envio de sexta é retentado com uma janela de nova tentativa de um dia, a nova tentativa ocorre no sábado, não na segunda-feira.

![Configuração "Janela de nova tentativa" definida como 1 dia.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

Para Campaigns baseadas em ação, as novas tentativas são baseadas no horário em que a mensagem disparada deveria ser enviada originalmente.

Campaigns baseadas em ação que utilizam eventos de exceção não suportam janelas de nova tentativa.

As janelas de nova tentativa para mensagens do Canvas são configuradas no nível da etapa. Para etapas de mensagem do Canvas compatíveis, se uma etapa de mensagem do Canvas for despriorizada e tiver uma janela de nova tentativa configurada, a Braze pode fazer uma nova tentativa dessa etapa posteriormente dentro da janela de nova tentativa.

## Como a Braze avalia mensagens {#how-braze-evaluates-messages}

{% alert tip %}
Você não precisa entender tudo nesta seção para usar a Priorização de Mensagens. Depois de configurar suas categorias, regras e aceitar suas mensagens, a Braze avalia e prioriza as mensagens automaticamente e faz o possível para enviar as que mais importam. Os detalhes aqui são para quando você quiser entender como essas decisões são tomadas.
{% endalert %}

Quando um usuário é elegível para várias mensagens priorizadas, a Braze avalia Campaigns aceitas e etapas de mensagem elegíveis do Canvas juntas nos canais compatíveis.

Para Campaigns, isso inclui envios agendados e baseados em ação elegíveis.

Para Canvas, isso inclui:

- Canvas agendados futuros para os quais o usuário é elegível para entrar
- Canvas nos quais o usuário está atualmente

A priorização do Canvas não é tudo ou nada. Uma Campaign de prioridade mais alta pode fazer com que uma etapa do Canvas seja desprioritizada, enquanto etapas elegíveis posteriores nesse mesmo Canvas ainda podem ser enviadas, dependendo da classificação da categoria, do momento do envio e das regras de limite de frequência.

A Braze compara mensagens priorizadas apenas quando elas compartilham a mesma regra de limite de frequência aplicável. Por exemplo, duas Campaigns de e-mail que contam para a mesma regra de limite de frequência de e-mail podem ser priorizadas uma em relação à outra, mas uma Campaign de e-mail de menor prioridade não é desprioritizada em favor de uma mensagem SMS de maior prioridade, a menos que ambas contem para a mesma regra. Mensagens fora da Priorização de Mensagens também compartilham esses limites de frequência, então até uma mensagem de alta prioridade pode sofrer interrupção por causa de uma mensagem fora da Priorização de Mensagens.

A Braze avalia Campaigns e Canvas de forma diferente, porque um Canvas pode se ramificar e se desdobrar ao longo do tempo.

### Avaliar Campaigns {#evaluating-campaigns}

A Braze compara cada mensagem elegível de Campaign usando o horário em que se espera que essa mensagem seja enviada.

### Avaliar Canvas {#evaluating-canvases}

Para avaliar um Canvas, a Braze realiza uma **antecipação**: ela percorre o Canvas a partir de um ponto inicial para prever quais mensagens futuras um usuário pode receber e quando. A antecipação começa a partir de:

- Entrada no Canvas, para Canvas agendados futuros
- A etapa atual do usuário, se o usuário já estiver no Canvas

Conforme a antecipação avança, a Braze trata cada tipo de etapa do Canvas de forma diferente. O tipo da etapa determina se a antecipação a conta, a pula, para nela ou se divide em múltiplas jornadas:

| Categoria da etapa | Efeito na antecipação |
|---|---|
| Etapas de mensagem | Contadas como mensagens elegíveis para priorização |
| Etapas de continuação | Puladas; a antecipação passa por elas |
| Etapas de limite | A antecipação para até que o usuário passe pela etapa |
| Etapas de Branch | A antecipação segue todas as jornadas possíveis |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Avaliando Canvas" }

#### Etapas de mensagem {#messaging-steps}

Essas etapas são contadas para a priorização e adicionadas ao conjunto de mensagens elegíveis quando enviam em um canal compatível.

- Etapa de mensagem
- Etapa do Otimizador de Conteúdo

#### Etapas de continuação {#continuation-steps}

Essas etapas são ignoradas para priorização e não afetam a antecipação.

- Etapa de atualização de contexto
- Etapa de atualização de usuário
- Etapa de sincronização de público
- Etapa de Feature Flag
- Etapa de postergação com atraso fixo

#### Etapas de limite {#boundary-steps}

A Braze interrompe a antecipação nessas etapas até que o usuário realmente avance por elas no Canvas.

- Etapa de postergação com atraso personalizado
- Etapa de postergação que segue uma etapa de Branch
- Etapa de jornada de ação
- Etapa de experimento

#### Etapas de Branch {#branching-steps}

Essas etapas dividem o Canvas em múltiplas jornadas possíveis.

- Etapa de divisão de decisão
- Etapa de jornada do público

Quando uma jornada de priorização contém etapas de Branch, a Braze assume que todas as jornadas são viáveis e considera todas as etapas de mensagem paralelas em canais compatíveis para priorização. Como as regras de limite de frequência podem ser específicas por canal, as etapas de mensagem paralelas são deduplicadas por canal quando necessário.

Por exemplo, se uma Branch pode enviar e-mail e outra Branch também pode enviar e-mail, a Braze as trata como um único envio de e-mail possível durante a antecipação. Se outra Branch pode enviar push, a Braze também considera esse possível envio de push separadamente.

Para etapas de mensagem do Canvas que usam Intelligent Timing, a Braze usa o horário de envio calculado de cada usuário assim que o usuário chega à etapa. Para mais detalhes, consulte [Intelligent Timing](#intelligent-timing).

As etapas do Otimizador de Conteúdo são tratadas como etapas de mensagem porque sempre enviam em um canal especificado. No entanto, janelas de nova tentativa não se aplicam às etapas do Otimizador de Conteúdo porque uma nova tentativa interferiria no experimento. Outras etapas de mensagem compatíveis do Canvas podem usar janelas de nova tentativa. Etapas do Canvas em canais não compatíveis não participam da Priorização de Mensagens.

## Exemplos {#examples}

### Campaign de prioridade mais alta versus Campaign de prioridade mais baixa {#higher-priority-campaign-versus-lower-priority-campaign}

Suponha que um usuário seja elegível para duas Campaigns de e-mail no mesmo dia, e ambas contam para a mesma regra de limite de frequência. Se a Campaign de prioridade mais alta deve ser enviada mais tarde naquele dia, a Braze pode reduzir a prioridade da Campaign de prioridade mais baixa para que a de prioridade mais alta possa ser enviada. Se a Campaign de prioridade mais baixa tiver uma janela de nova tentativa, a Braze pode tentar enviá-la novamente mais tarde.

### Campaign baseada em ação de prioridade mais alta versus mensagem de prioridade mais baixa {#higher-priority-action-based-campaign-versus-lower-priority-message}

Suponha que um usuário dispare uma Campaign baseada em ação de prioridade mais alta configurada para ser enviada duas horas depois. Durante esse intervalo, a Braze pode considerar essa Campaign baseada em ação futura ao decidir se outra mensagem priorizada deve ser enviada primeiro. Isso ajuda a evitar que uma mensagem de prioridade mais baixa seja enviada agora, caso a Campaign baseada em ação de prioridade mais alta esteja prevista para ser enviada em breve.

### Canvas de prioridade mais alta versus Campaign de prioridade mais baixa {#higher-priority-canvas-versus-lower-priority-campaign}

Suponha que um usuário seja elegível para uma Campaign de prioridade mais baixa, mas também esteja previsto para receber uma mensagem de Canvas de prioridade mais alta mais tarde naquele dia. Se a Braze já puder avaliar essa mensagem futura do Canvas, ela pode reduzir a prioridade da Campaign de prioridade mais baixa para que a mensagem do Canvas de prioridade mais alta possa ser enviada.

### Canvas de prioridade mais alta com uma etapa de limite versus Campaign de prioridade mais baixa {#higher-priority-canvas-with-a-boundary-step-versus-lower-priority-campaign}

Suponha que um Canvas de prioridade mais alta inclua uma etapa de Jornada de Ação, um experimento ou uma postergação personalizada antes da próxima etapa de Mensagem. Até que o usuário alcance e passe por essa etapa, a Braze não antecipa a mensagem do Canvas de prioridade mais alta que está adiante. Nesse caso, uma Campaign de prioridade mais baixa ainda pode ser enviada primeiro.

### Canvas com Branch de prioridade mais alta versus mensagem de prioridade mais baixa {#higher-priority-branching-canvas-versus-lower-priority-message}

Suponha que um Canvas de prioridade mais alta possa enviar mensagens diferentes dependendo de qual Branch o usuário seguir. A Braze avalia esses possíveis caminhos futuros de forma conservadora ao comparar mensagens. Isso ajuda a evitar que uma mensagem de prioridade mais baixa seja enviada agora, caso uma Branch do Canvas de prioridade mais alta possa usar o mesmo limite de frequência mais tarde.

### Etapa do Canvas com Intelligent Timing e etapas subsequentes {#canvas-step-with-intelligent-timing-and-downstream-steps}

Suponha que um usuário entre em uma etapa de Mensagem de Canvas de prioridade mais alta que usa Intelligent Timing. Depois que a Braze calcula o horário de envio daquele usuário para a etapa com Intelligent Timing, a Priorização de Mensagens usa esse horário de envio por usuário para a etapa atual e para etapas de Mensagem posteriores no mesmo caminho determinístico. Isso ajuda a Braze a comparar mensagens do Canvas subsequentes com outros envios priorizados usando o horário atualizado, em vez de apenas a estimativa anterior do caminho.

## Limitações {#limitations}

A Priorização de Mensagens tem os seguintes limites de recurso. Os limites específicos dependem da sua edição da plataforma Braze; entre em contato com o gerente da sua conta Braze para obter detalhes.

- Um limite no número de Campaigns e Canvas agendados ativos com aceitação (combinados)
- Um limite no número de Campaigns e Canvas baseados em ação ativos com aceitação (combinados)
- Um limite no número de decisões de priorização por mês
- Um limite no número de categorias por espaço de trabalho
- Um limite no número de regras de priorização por espaço de trabalho
- Um comprimento máximo da janela de nova tentativa

## Perguntas frequentes {#frequently-asked-questions}

### Como os empates de prioridade são resolvidos entre mensagens na mesma categoria? {#how-are-ties-in-priority-broken-between-messages-in-the-same-category}

Ao priorizar duas campanhas na mesma categoria, a Braze dá maior prioridade àquela com o horário de envio mais cedo. Se uma janela de nova tentativa estiver configurada, a Braze usa o final dessa janela ao comparar campanhas dentro da mesma regra de prioridade. Para campanhas recorrentes, o horário de envio é calculado como a próxima ocorrência a partir da meia-noite no fuso da empresa. Para campanhas agendadas no fuso local, a Braze assume um horário de envio no fuso da empresa.

Para Canvas na mesma categoria, a Braze usa o momento de entrada no Canvas como critério de desempate, de modo que todas as etapas no mesmo Canvas preservem a mesma prioridade relativa em relação a outras campanhas e Canvas.

### Como posso garantir que uma mensagem seja sempre enviada? {#how-can-i-make-sure-a-message-is-always-sent}

Pode haver cenários em que você deseja que uma mensagem seja sempre enviada, como no caso de notificações transacionais ou legais. Nesse caso, você deve excluir a mensagem do limite de frequência, o que também a torna inelegível para a Priorização de Mensagens. Isso envia a mensagem sempre que ela estiver agendada ou for disparada, sem considerar o que mais está sendo enviado.

### Quando as mensagens são realmente priorizadas? Existe um cronograma? {#when-are-messages-actually-prioritized-is-there-a-schedule}

Cada mensagem é priorizada com base no momento em que se espera que ela seja enviada. Não há um horário universal de avaliação para mensagens priorizadas.

### Como a Braze prevê quando uma mensagem futura será enviada? {#how-does-braze-predict-when-a-future-message-sends}

A Braze prevê o momento de envio futuro de forma diferente para cada tipo de mensagem:

- **Campaigns agendadas:** a Braze usa o horário em que cada campanha deve ser enviada. Para campanhas agendadas que usam Intelligent Timing, a Braze usa o horário ideal de envio de cada usuário para aquela ocorrência da campanha.
- **Campaigns baseadas em ação:** a Braze usa o horário em que cada mensagem disparada deve ser enviada, incluindo qualquer postergação configurada entre o disparo e o envio.
- **Etapas do Canvas:** a Braze usa a entrada do usuário no Canvas ou sua posição atual no Canvas, mais o momento das etapas subsequentes. Para etapas de mensagem do Canvas que usam Intelligent Timing, quando um usuário entra nessa etapa, a Braze usa o horário de envio por usuário calculado para ele. Para etapas de mensagem seguintes no mesmo caminho determinístico, a Braze usa esse horário de envio do Intelligent Timing ao determinar o momento de envio esperado posteriormente. Antes de um usuário alcançar a etapa com Intelligent Timing, a previsão permanece com base no melhor esforço.

### Minha mensagem estava agendada para envio, mas ainda não foi enviada por causa de limite de frequência ou outros atrasos. O que isso significa para a priorização de outras campanhas? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

A Braze assume que sua mensagem foi enviada no horário originalmente agendado, caso ela ainda esteja sendo processada, o que determina se outras mensagens priorizadas futuras devem ser enviadas. Quando essa mensagem é de fato enviada, a Braze usa o horário real de envio.

### Minha mensagem foi priorizada, mas abortada no último momento. O que isso significa para a priorização? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

Quando uma mensagem é priorizada, a Braze assume que ela foi enviada no horário originalmente agendado. De modo geral, para a Priorização de Mensagens, não recomendamos o uso de interrupções via Liquid. Se uma mensagem for abortada devido à [lógica Liquid de `abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages), assumimos que ela foi enviada para aquele usuário e priorizamos as campanhas futuras de acordo.

Digamos que você tenha duas mensagens: Mensagem 1 e Mensagem 2. Se a Mensagem 1 for abortada em favor de uma futura Mensagem 2 de maior prioridade, isso não garante que a Mensagem 2 será de fato enviada. A Mensagem 2 ainda pode ser abortada por qualquer motivo, incluindo:

- Interrupções via Liquid
- O usuário não fazer mais parte do Segment
- Limites de frequência devido a uma mensagem fora das regras de priorização.

Se a Mensagem 2 for abortada, não haverá outra tentativa de enviar a Mensagem 1.

Note que um usuário pode receber uma mensagem de menor prioridade, mas não uma mensagem de maior prioridade para a mesma regra de limite de frequência, pelos seguintes motivos:

- A mensagem de maior prioridade teve o limite de frequência aplicado por uma regra diferente.
- A mensagem de maior prioridade conflitou com outra campanha futura de prioridade ainda mais alta para uma regra diferente.
- No momento do envio da mensagem de menor prioridade, o usuário não estava no público da mensagem de maior prioridade.
- Ambas as mensagens deveriam ter sido enviadas, mas uma mensagem fora da configuração de priorização foi enviada antes que a mensagem de maior prioridade pudesse ser enviada.

### Como o Intelligent Timing funciona com a Priorização de Mensagens? {#how-does-intelligent-timing-work-with-message-prioritization}

Para campanhas, a Priorização de Mensagens usa o horário ideal de envio de cada usuário para a ocorrência atual. Para etapas de mensagem do Canvas, a Braze usa o horário de envio calculado de cada usuário quando ele alcança a etapa e reflete esse momento nas etapas de mensagem seguintes no mesmo caminho determinístico. Para saber mais, consulte [Intelligent Timing](#intelligent-timing).

### Existe alguma funcionalidade de relatório ou análise de dados específica para a Priorização de Mensagens? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

A Braze fornece eventos relacionados à Priorização de Mensagens no Currents e no compartilhamento de dados para canais compatíveis, incluindo e-mail, LINE, notificações por push, SMS, webhooks e WhatsApp. Esses eventos incluem eventos de despriorização e de limite de frequência, registrados como o evento `users.messages.<channel>.Abort`, bem como eventos de nova tentativa que mostram quando uma mensagem foi retentada posteriormente dentro da janela de nova tentativa configurada, registrados como o evento `users.messages.<channel>.Retry`.

Você também pode usar o dashboard de Diagnóstico de Mensagens, as estatísticas diárias existentes de despriorização e nova tentativa, e a [funcionalidade de relatórios da Braze]({{site.baseurl}}/user_guide/analytics/reports) existente para monitorar a integridade e o desempenho de suas campanhas e Canvas priorizados.