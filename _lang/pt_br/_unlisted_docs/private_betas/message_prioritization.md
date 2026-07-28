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

Os usuários só conseguem receber uma quantidade limitada de mensagens antes que o volume se torne um problema. As mensagens que chegam até eles devem ser as mais importantes para o seu negócio. A Priorização de Mensagens ajuda a garantir que suas mensagens de maior valor ocupem esse espaço limitado, em vez de deixar isso ao acaso.

A maioria das equipes controla o volume de mensagens com limites de frequência. Por si só, os limites de frequência são pouco precisos. Quando um usuário atinge o limite, o momento do envio decide quais mensagens são entregues — e não a importância para o negócio.

Uma promoção de baixo valor que dispara primeiro pode ocupar o espaço que uma recompensa de fidelidade ou uma mensagem urgente usaria mais tarde naquele dia. As equipes costumam contornar isso com regras de limite separadas, agendamento manual e filtros pontuais. Essas abordagens exigem manutenção constante. Elas se tornam mais difíceis de gerenciar à medida que Campaigns e Canvas mudam. E ainda assim não conseguem garantir que a mensagem certa vença.

A Priorização de Mensagens muda a alocação do limite de frequência de **primeiro a chegar, primeiro a ser atendido** para **baseada na prioridade do negócio**: você define o que importa, e a Braze toma as decisões de envio por você.

A Priorização de Mensagens oferece vários benefícios:

- **Defina o que importa uma única vez:** Use categorias e regras classificadas para codificar suas prioridades — por exemplo, "Fidelidade" acima de "Parcerias Pagas". Todo envio com aceitação respeita essas classificações automaticamente.
- **Decisões voltadas para o futuro:** A Braze prevê o que um usuário pode receber depois. Ela pode reter uma mensagem de menor prioridade para preservar espaço no limite para uma de maior prioridade.
- **Funciona em diferentes tipos de mensagens e canais:** Campaigns agendadas, Campaigns baseadas em ação e etapas do Canvas competem em um único pool classificado dentro dos seus limites de frequência compartilhados.
- **Janelas de nova tentativa:** Uma mensagem despriorizada pode tentar novamente se houver capacidade disponível. Isso melhora o mix de mensagens sem descartar completamente os envios de menor prioridade.

O resultado é o mesmo volume de envio limitado, alocado automaticamente para as mensagens que mais importam.

A Priorização de Mensagens é mais valiosa para remetentes de alto volume que atingem os limites de frequência com frequência. Ela funciona melhor quando o valor da mensagem é claramente diferenciado — por exemplo, mensagens de fidelidade ou que geram receita versus promoções rotineiras.

## Como funciona {#how-it-works}

Use a Priorização de Mensagens para criar [categorias](#categories) e [regras de priorização](#prioritization-rules) para classificar como suas mensagens são enviadas.

Para gerenciar essas configurações, acesse **Configurações** > **Priorização de Mensagens**. Somente administradores podem definir as configurações de nível superior da Priorização de Mensagens. Os usuários precisam da permissão "View Message Prioritization" para visualizar as configurações nesta seção e da permissão "Edit Message Prioritization" para editá-las.

Por exemplo, uma marca de beleza que gerencia promoções por e-mail para parcerias pagas e programas de fidelidade usa a Priorização de Mensagens para criar duas categorias: "Parcerias Pagas" e "Fidelidade". A marca classifica essas categorias por importância para o negócio. Durante a temporada de festas, ela classifica "Fidelidade" em primeiro lugar e "Parcerias Pagas" em segundo para priorizar membros de longo prazo.

![Um exemplo de regras de priorização para duas categorias: Parcerias Pagas e Fidelidade.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

No momento do envio, a Braze compara a mensagem sendo enviada com outras mensagens que o usuário pode receber e que estão habilitadas para priorização, possuem uma categoria de prioridade definida e contam para a mesma regra de limite de frequência dentro da mesma janela de limite de frequência. Se o envio da mensagem atual impedir que uma mensagem de maior prioridade seja enviada posteriormente, a Braze reduz a prioridade da mensagem de menor prioridade. Dependendo da janela de nova tentativa configurada, essa mensagem de menor prioridade é reenviada posteriormente ou não é enviada.

A Priorização de Mensagens pode avaliar:

- Campaigns agendadas
- Campaigns baseadas em ação
- Canvas

Atualmente, Campaigns ou Canvas disparados por API não são compatíveis com a Priorização de Mensagens e não participam da priorização.

A Braze usa sua previsão de quando cada mensagem deve ser enviada ao avaliar se o envio de uma mensagem agora poderia impedir que uma mensagem de maior prioridade seja enviada posteriormente. Para saber mais sobre como a Braze prevê o momento de envio futuro para Campaigns e Canvas, consulte [Como a Braze prevê quando uma mensagem futura será enviada?](#how-does-braze-predict-when-a-future-message-sends)

### Canais de mensagem compatíveis {#supported-message-channels}

A Priorização de Mensagens é compatível com os mesmos canais do limite de frequência:

- Notificações por push
- E-mail
- SMS
- Webhooks
- WhatsApp
- LINE

Para priorização e limite de frequência, push para iOS, push para Android, web push e outras plataformas de notificação por push são tratados como um único canal de push compartilhado, e não como canais separados.

Estes canais não são elegíveis para a Priorização de Mensagens porque não estão sujeitos ao limite de frequência:

- Content Cards
- Mensagens no app
- Banners

Mensagens no app e Banners usam suas próprias configurações de prioridade para decidir qual mensagem é exibida quando várias mensagens competem pelo mesmo disparo ou posicionamento. Para mensagens no app, consulte [Escolher uma prioridade]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority). Para Banners, consulte [Prioridade de Banners]({{site.baseurl}}/user_guide/channels/banners#priority).

Se uma Campaign ou etapa do Canvas usa apenas canais não elegíveis, ela não participará da priorização.

## Categorias {#categories}

As regras de priorização são baseadas em uma classificação de categorias, que são rótulos que você pode atribuir a uma determinada Campaign ou Canvas (semelhante a uma [tag]({{site.baseurl}}/user_guide/administrative/app_settings/tags)). Existe um limite para o número de categorias que você pode criar em um determinado momento; fale com seu gerente de conta se quiser um limite maior.

Para adicionar uma nova categoria:

1. Acesse **Configurações** > **Priorização de mensagens** > **Categorias**.
2. Selecione **Criar nova categoria**.

![O botão "Criar nova categoria" na seção Priorização de mensagens.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Dê um nome à categoria e uma descrição opcional.
4. Selecione **Criar categoria**.

![Um exemplo de categoria chamada "P3" com a descrição "Esta é minha terceira categoria de maior prioridade."]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

Para editar ou excluir uma categoria, selecione o menu <i class="fas fa-ellipsis-vertical" aria-label="Mais opções"></i>.

## Regras de priorização {#prioritization-rules}

Depois que suas categorias estiverem configuradas, você pode classificá-las em um conjunto de regras de priorização. As regras são classificadas em ordem decrescente de prioridade. Há um limite para o número de regras de priorização que você pode criar em um determinado momento; fale com seu gerente de conta se quiser um limite maior.

1. Acesse **Configurações** > **Priorização de mensagens** > **Regras de priorização** para configurar suas regras.

![Seção "Regras de priorização" sem prioridades definidas ainda.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization4.png %})

{:start="2"}
2. Selecione **Adicionar regra**.
3. Selecione uma categoria no menu suspenso.

![Regra de priorização "Prioridade 1" com P1 selecionada como categoria.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization5.png %})

{:start="4"}
4. Continue adicionando regras selecionando **+ Adicionar regra** abaixo da sua última regra.

Para reordenar as regras, selecione e arraste o ícone <i class="fa-solid fa-grip-vertical" aria-label="Arrastar para reordenar"></i> em uma regra. Para excluir uma regra, selecione o menu <i class="fas fa-ellipsis-vertical" aria-label="Mais opções"></i> e depois **Excluir regra**.

Não se esqueça de selecionar **Salvar** para que suas atualizações sejam aplicadas.

## Limites de frequência {#frequency-caps}

A Priorização de Mensagens funciona dentro das suas regras de limite de frequência existentes. Para ser elegível para priorização, uma Campaign ou etapa do Canvas deve usar um canal compatível e estar sujeita à sua configuração de limite de frequência. Mensagens que não estão sujeitas ao limite de frequência não são elegíveis para a Priorização de Mensagens. Se você quiser que uma mensagem seja sempre enviada, desative o limite de frequência para ela. Isso também a remove da Priorização de Mensagens.

Uma mensagem priorizada só pode ser enviada se:

1. A regra de limite de frequência relevante ainda não tiver sido atingida para aquele usuário, e
2. O envio dessa mensagem não fizer com que o usuário atinja um limite antes que uma mensagem posterior de maior prioridade possa ser enviada.

![Um exemplo de uma regra de limite de frequência.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

Você pode usar regras de limite de frequência específicas por canal, regras específicas por categoria, filtros de tag ou regras que se aplicam a qualquer canal. A Priorização de Mensagens funciona com quaisquer regras que se apliquem às suas mensagens com aceitação ativa.

Você também pode criar regras de limite de frequência por categoria para gerenciar quantas mensagens um usuário recebe de uma determinada categoria. Isso ajuda a evitar que uma categoria de alta prioridade envie mensagens em excesso. Selecione **Message prioritization category** em **Additional filters** e selecione uma categoria no menu suspenso.

![Um exemplo da regra de limite de frequência com o menu suspenso do campo "Category" para selecionar P2 ou P1.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

## Aceitação {#opting-in}

### Aceitação de Campaign {#campaign-opt-in}

Para aceitar a priorização de uma Campaign, marque a caixa de seleção **Opt-in to Message Prioritization** nas configurações de entrega da Campaign.

![A caixa de seleção "Opt-in to Message Prioritization".]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

Em seguida, atribua a Campaign a uma categoria selecionando uma opção no menu suspenso **Category**.

![O menu suspenso de categoria de priorização de mensagens nas configurações de entrega de uma Campaign.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

A priorização de mensagens é compatível com Campaigns agendadas e Campaigns baseadas em ação. Campaigns disparadas por API não são compatíveis.

### Aceitação de Canvas {#canvas-opt-in}

A aceitação de Canvas funciona de forma semelhante às Campaigns. Para aceitar a priorização de mensagens em um Canvas, ative a priorização de mensagens nas configurações do Canvas e atribua o Canvas a uma categoria. Todas as etapas do Canvas compartilham essa categoria e o mesmo nível de prioridade, o que significa que não é possível definir a prioridade individualmente por etapa.

A priorização de mensagens é compatível com Canvas agendados e Canvas baseados em ação. Canvas disparados por API não são compatíveis.

## Intelligent Timing {#intelligent-timing}

Com o Intelligent Timing, a Braze envia uma mensagem no horário ideal de envio de cada usuário, de modo que a mesma Campaign ou etapa de mensagem do Canvas pode alcançar diferentes usuários em horários diferentes. A Priorização de Mensagens leva isso em conta: em vez de presumir que a mensagem é enviada a todos no horário agendado, ela classifica as mensagens concorrentes de um usuário usando o horário ideal de envio desse usuário.

Para Campaigns e etapas de mensagem do Canvas que usam Intelligent Timing, a Braze prevê o horário de envio com base no melhor esforço até calcular o horário de envio por usuário de cada um. Para Campaigns, a Priorização de Mensagens usa o horário ideal de envio desse usuário para a ocorrência atual ao comparar a Campaign com as outras mensagens priorizadas elegíveis do usuário. Para Campaigns recorrentes com Intelligent Timing, a Braze usa o horário ideal de envio escolhido para aquela ocorrência.

Para etapas de mensagem do Canvas, a Braze atualiza essa previsão assim que o usuário entra na etapa e a Braze calcula o horário ideal de envio desse usuário para a etapa. A Priorização de Mensagens usa esse horário de envio calculado para a etapa atual. Em jornadas determinísticas (jornadas sem ramificação, onde a sequência de etapas é fixa), a Braze também reflete esse horário atualizado nas etapas de mensagem seguintes ao determinar seus horários de envio esperados.

## Janelas de nova tentativa {#retry-windows}

Uma janela de nova tentativa permite que mensagens com aceitação façam novas tentativas por um número limitado de dias, caso a primeira tentativa não tenha prioridade alta o suficiente para ser enviada. O comprimento máximo da janela de nova tentativa depende da edição da sua plataforma Braze. Em cada dia subsequente, no mesmo horário em que a mensagem foi originalmente agendada ou disparada para envio, a mensagem é tentada novamente. Após o último dia na janela de nova tentativa, se a mensagem ainda não tiver sido enviada, ela não será tentada novamente e será permanentemente despriorizada.

Para Campaigns agendadas recorrentes, a janela de nova tentativa deve ser menor do que o tempo mínimo entre envios dessa Campaign. As novas tentativas sempre acontecem um dia por vez a partir do horário de envio original, mesmo que a Campaign não esteja normalmente agendada para enviar naquele dia. Por exemplo, se você tem uma Campaign que envia toda segunda e quarta-feira, a nova tentativa ocorre na terça-feira, então a janela de nova tentativa deve ser definida como um dia. Se você tem uma Campaign que envia toda segunda, quarta e sexta-feira, e o envio de sexta-feira é tentado novamente com uma janela de nova tentativa de um dia, a nova tentativa ocorre no sábado, não na segunda-feira.

![A configuração "Janela de nova tentativa" definida como 1 dia.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

Para Campaigns baseadas em ação, as novas tentativas são baseadas no horário em que a mensagem disparada era originalmente esperada para envio.

Campaigns baseadas em ação que usam eventos de exceção não oferecem suporte a janelas de nova tentativa.

As janelas de nova tentativa para mensagens do Canvas são configuradas no nível da etapa. Para etapas de mensagens do Canvas compatíveis, se uma etapa de mensagem do Canvas for despriorizada e tiver uma janela de nova tentativa configurada, a Braze pode tentar novamente essa etapa posteriormente dentro da janela de nova tentativa.

## Como a Braze avalia mensagens {#how-braze-evaluates-messages}

{% alert tip %}
Você não precisa entender tudo nesta seção para usar a Priorização de Mensagens. Depois de definir suas categorias e regras e ativar suas mensagens, a Braze avalia e prioriza as mensagens automaticamente, fazendo o possível para enviar as que mais importam. Os detalhes aqui são para quando você quiser entender como essas decisões são tomadas.
{% endalert %}

Quando um usuário é elegível para várias mensagens priorizadas, a Braze avalia Campaigns com aceitação e etapas de mensagem elegíveis do Canvas juntas nos canais compatíveis.

Para Campaigns, isso inclui envios agendados e baseados em ação elegíveis.

Para Canvas, isso inclui:

- Canvas agendados futuros para os quais o usuário é elegível para entrar
- Canvas nos quais o usuário está atualmente

A priorização do Canvas não é tudo ou nada. Uma Campaign de prioridade mais alta pode fazer com que uma etapa do Canvas seja despriorizada, enquanto etapas elegíveis posteriores nesse mesmo Canvas ainda podem ser enviadas, dependendo da classificação da categoria, do momento do envio e das regras de limite de frequência.

A Braze compara mensagens priorizadas somente quando elas compartilham a mesma regra de limite de frequência aplicável. Por exemplo, duas Campaigns de e-mail que contam para a mesma regra de limite de frequência de e-mail podem ser priorizadas uma em relação à outra, mas uma Campaign de e-mail de prioridade mais baixa não é despriorizada em favor de uma mensagem SMS de prioridade mais alta, a menos que ambas contem para a mesma regra. Mensagens fora da Priorização de Mensagens também compartilham esses limites de frequência, então até mesmo uma mensagem de alta prioridade pode sofrer interrupção por causa de uma mensagem fora da Priorização de Mensagens.

A Braze avalia Campaigns e Canvas de maneira diferente, porque um Canvas pode se ramificar e se desdobrar ao longo do tempo.

### Avaliar Campaigns {#evaluating-campaigns}

A Braze compara cada mensagem de Campaign elegível usando o horário em que se espera que a mensagem seja enviada.

### Avaliar Canvas {#evaluating-canvases}

Para avaliar um Canvas, a Braze realiza uma **análise antecipada**: ela percorre o Canvas a partir de um ponto inicial para prever quais mensagens futuras um usuário pode receber e quando. A análise antecipada começa a partir de:

- Entrada no Canvas, para Canvas agendados futuros
- A etapa atual do usuário, se o usuário já estiver no Canvas

Ao fazer a análise antecipada, a Braze trata cada tipo de etapa do Canvas de maneira diferente. O tipo de etapa determina se a análise antecipada a conta, a ignora, para nela ou se divide em vários caminhos:

| Categoria da etapa | Efeito na análise antecipada |
|---|---|
| Etapas de mensagem | Contadas como mensagens elegíveis para priorização |
| Etapas de continuação | Ignoradas; a análise antecipada passa por elas |
| Etapas de limite | A análise antecipada para até o usuário passar pela etapa |
| Etapas de ramificação | A análise antecipada segue todos os caminhos possíveis |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Avaliando Canvas" }

#### Etapas de mensagem {#messaging-steps}

Essas etapas são contadas para a priorização e adicionadas ao conjunto de mensagens elegíveis quando enviam em um canal compatível.

- Etapa de mensagem
- Etapa do Otimizador de Conteúdo

#### Etapas de continuação {#continuation-steps}

Essas etapas são ignoradas para a priorização e não afetam a análise antecipada.

- Etapa de atualização de contexto
- Etapa de atualização de usuário
- Etapa de sincronização de público
- Etapa de Feature Flag
- Etapa de postergação com atraso fixo

#### Etapas de limite {#boundary-steps}

A Braze interrompe a análise antecipada nessas etapas até que o usuário realmente avance por elas no Canvas.

- Etapa de postergação com atraso personalizado
- Etapa de postergação que segue uma etapa de ramificação
- Etapa de jornada de ação
- Etapa de experimento

#### Etapas de ramificação {#branching-steps}

Essas etapas dividem o Canvas em vários caminhos possíveis.

- Etapa de divisão de decisão
- Etapa de jornada do público

Quando um caminho de priorização contém etapas de ramificação, a Braze assume que todos os caminhos são viáveis e considera todas as etapas de mensagem paralelas em canais compatíveis para priorização. Como as regras de limite de frequência podem ser específicas por canal, as etapas de mensagem paralelas são deduplicadas por canal quando necessário.

Por exemplo, se uma ramificação pode enviar e-mail e outra ramificação também pode enviar e-mail, a Braze trata essas como um único envio de e-mail possível durante a análise antecipada. Se outra ramificação pode enviar push, a Braze também considera esse possível envio de push separadamente.

Para etapas de mensagem do Canvas que usam Intelligent Timing, a Braze usa o horário de envio calculado de cada usuário assim que o usuário chega à etapa. Para saber mais, consulte [Intelligent Timing](#intelligent-timing).

As etapas do Otimizador de Conteúdo são tratadas como etapas de mensagem porque sempre enviam em um canal especificado. No entanto, janelas de nova tentativa não se aplicam às etapas do Otimizador de Conteúdo porque uma nova tentativa interferiria no experimento. Outras etapas de mensagem compatíveis do Canvas podem usar janelas de nova tentativa. Etapas do Canvas em canais não compatíveis não participam da Priorização de Mensagens.

## Exemplos {#examples}

### Campaign de maior prioridade versus Campaign de menor prioridade {#higher-priority-campaign-versus-lower-priority-campaign}

Suponha que um usuário seja elegível para duas Campaigns de e-mail no mesmo dia, e ambas contam para a mesma regra de limite de frequência. Se a Campaign de maior prioridade estiver programada para enviar mais tarde naquele dia, a Braze pode reduzir a prioridade da Campaign de menor prioridade para que a de maior prioridade possa ser enviada. Se a Campaign de menor prioridade tiver uma janela de nova tentativa, a Braze pode tentar enviá-la novamente depois.

### Campaign baseada em ação de maior prioridade versus mensagem de menor prioridade {#higher-priority-action-based-campaign-versus-lower-priority-message}

Suponha que um usuário dispare uma Campaign baseada em ação de maior prioridade configurada para enviar duas horas depois. Durante essa postergação, a Braze pode considerar essa Campaign baseada em ação futura ao decidir se outra mensagem priorizada deve ser enviada primeiro. Isso ajuda a evitar que uma mensagem de menor prioridade seja enviada agora se a Campaign baseada em ação de maior prioridade estiver prevista para enviar em breve.

### Canvas de maior prioridade versus Campaign de menor prioridade {#higher-priority-canvas-versus-lower-priority-campaign}

Suponha que um usuário seja elegível para uma Campaign de menor prioridade, mas também esteja previsto para receber uma mensagem de Canvas de maior prioridade mais tarde naquele dia. Se a Braze já puder avaliar essa mensagem futura do Canvas, ela pode reduzir a prioridade da Campaign de menor prioridade para que a mensagem de Canvas de maior prioridade possa ser enviada.

### Canvas de maior prioridade com uma etapa de limite versus Campaign de menor prioridade {#higher-priority-canvas-with-a-boundary-step-versus-lower-priority-campaign}

Suponha que um Canvas de maior prioridade inclua uma etapa de Jornada de Ação, um experimento ou uma postergação personalizada antes da próxima etapa de Mensagem. Até que o usuário alcance e passe por essa etapa, a Braze não antecipa a mensagem de Canvas de maior prioridade que está adiante. Nesse caso, uma Campaign de menor prioridade ainda pode ser enviada primeiro.

### Canvas com ramificações de maior prioridade versus mensagem de menor prioridade {#higher-priority-branching-canvas-versus-lower-priority-message}

Suponha que um Canvas de maior prioridade possa enviar mensagens diferentes dependendo de qual ramificação o usuário seguir. A Braze avalia esses possíveis caminhos futuros de forma conservadora ao comparar mensagens. Isso ajuda a evitar que uma mensagem de menor prioridade seja enviada agora se uma ramificação de Canvas de maior prioridade puder usar o mesmo limite de frequência depois.

### Etapa do Canvas com Intelligent Timing e etapas subsequentes {#canvas-step-with-intelligent-timing-and-downstream-steps}

Suponha que um usuário entre em uma etapa de Mensagem de Canvas de maior prioridade que usa Intelligent Timing. Depois que a Braze calcula o horário de envio daquele usuário para a etapa com Intelligent Timing, a Priorização de Mensagens usa esse horário de envio por usuário para a etapa atual e para etapas de Mensagem posteriores no mesmo caminho determinístico. Isso ajuda a Braze a comparar mensagens de Canvas subsequentes com outros envios priorizados usando o horário atualizado, em vez de apenas a estimativa anterior do caminho.

## Limitações {#limitations}

A Priorização de Mensagens possui os seguintes limites de recurso. Os limites específicos dependem da edição da sua plataforma Braze; entre em contato com o gerente da sua conta Braze para mais detalhes.

- Um limite no número de Campaigns e Canvas agendados ativos com aceitação (combinados)
- Um limite no número de Campaigns e Canvas baseados em ação ativos com aceitação (combinados)
- Um limite no número de decisões de priorização por mês
- Um limite no número de categorias por espaço de trabalho
- Um limite no número de regras de priorização por espaço de trabalho
- Uma duração máxima da janela de nova tentativa

## Perguntas frequentes {#frequently-asked-questions}

### Como os empates de prioridade são resolvidos entre mensagens na mesma categoria? {#how-are-ties-in-priority-broken-between-messages-in-the-same-category}

Ao priorizar duas campanhas na mesma categoria, a Braze dá prioridade mais alta àquela com o horário de envio mais cedo. Se uma janela de nova tentativa estiver configurada, a Braze usa o final dessa janela ao comparar campanhas dentro da mesma regra de prioridade. Para campanhas recorrentes, o horário de envio é calculado como a próxima ocorrência a partir da meia-noite no fuso horário da empresa. Para campanhas agendadas no fuso local, a Braze assume um horário de envio no fuso horário da empresa.

Para Canvas na mesma categoria, a Braze usa o momento de entrada no Canvas como critério de desempate, de modo que todas as etapas no mesmo Canvas preservem a mesma prioridade relativa em relação a outras campanhas e Canvas.

### Como posso garantir que uma mensagem seja sempre enviada? {#how-can-i-make-sure-a-message-is-always-sent}

Pode haver cenários em que você deseja que uma mensagem seja sempre enviada, como no caso de notificações transacionais ou legais. Nesse caso, você deve excluir a mensagem do limite de frequência, o que também a torna inelegível para a Priorização de Mensagens. Isso envia a mensagem sempre que ela for agendada ou disparada, sem considerar o que mais está sendo enviado.

### Quando as mensagens são realmente priorizadas? Existe um cronograma? {#when-are-messages-actually-prioritized-is-there-a-schedule}

Cada mensagem é priorizada com base no momento em que se espera que seja enviada. Não existe um horário universal de avaliação para mensagens priorizadas.

### Como a Braze prevê quando uma mensagem futura será enviada? {#how-does-braze-predict-when-a-future-message-sends}

A Braze prevê o momento de envio futuro de forma diferente para cada tipo de mensagem:

- **Campaigns agendadas:** a Braze usa o horário em que se espera que cada campanha seja enviada. Para campanhas agendadas que usam Intelligent Timing, a Braze usa o horário de envio ideal de cada usuário para aquela ocorrência da campanha.
- **Campaigns baseadas em ação:** a Braze usa o horário em que se espera que cada mensagem disparada seja enviada, incluindo qualquer postergação configurada entre o disparo e o envio.
- **Etapas do Canvas:** a Braze usa a entrada do usuário no Canvas ou a posição atual no Canvas, mais o momento das etapas subsequentes. Para etapas de mensagem do Canvas que usam Intelligent Timing, quando um usuário entra nessa etapa, a Braze usa o horário de envio por usuário que calcula para ele. Para etapas de mensagem seguintes no mesmo caminho determinístico, a Braze usa esse horário de envio do Intelligent Timing ao determinar o momento de envio esperado posterior. Antes de um usuário alcançar a etapa com Intelligent Timing, a previsão permanece como melhor estimativa.

### Minha mensagem já estava agendada para envio, mas ainda não foi enviada por causa de limite de frequência ou outros atrasos. O que isso significa para a priorização de outras campanhas? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

A Braze assume que sua mensagem foi enviada no horário originalmente agendado se ela ainda estiver sendo processada, o que determina se outras mensagens priorizadas futuras devem ser enviadas. Quando essa mensagem é finalmente enviada, a Braze usa o horário de envio real.

### Minha mensagem foi priorizada, mas sofreu interrupção de última hora. O que isso significa para a priorização? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

Quando uma mensagem é priorizada, a Braze assume que ela foi enviada no horário originalmente agendado. De modo geral, para a Priorização de Mensagens, não recomendamos o uso de interrupções via Liquid. Se uma mensagem for interrompida devido à [lógica Liquid `abort_message`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages), assumimos que ela foi enviada para aquele usuário e priorizamos campanhas futuras de acordo.

Digamos que você tenha duas mensagens: Mensagem 1 e Mensagem 2. Se a Mensagem 1 for interrompida em favor de uma Mensagem 2 de prioridade mais alta no futuro, isso não garante que a Mensagem 2 será realmente enviada. A Mensagem 2 ainda pode ser interrompida por qualquer motivo, incluindo:

- Interrupções via Liquid
- O usuário não estar mais no Segment
- Limites de frequência por causa de uma mensagem fora das regras de priorização.

Se a Mensagem 2 for interrompida, não haverá outra tentativa de enviar a Mensagem 1.

Observe que um usuário pode receber uma mensagem de prioridade mais baixa, mas não uma mensagem de prioridade mais alta para a mesma regra de limite de frequência pelos seguintes motivos:

- A mensagem de prioridade mais alta teve o limite de frequência aplicado por uma regra diferente.
- A mensagem de prioridade mais alta entrou em conflito com outra campanha futura de prioridade ainda mais alta para uma regra diferente.
- No momento do envio da mensagem de prioridade mais baixa, o usuário não estava no público da mensagem de prioridade mais alta.
- Ambas as mensagens deveriam ter sido enviadas, mas uma mensagem fora da configuração de priorização foi enviada antes que a mensagem de prioridade mais alta pudesse ser enviada.

### Como o Intelligent Timing funciona com a Priorização de Mensagens? {#how-does-intelligent-timing-work-with-message-prioritization}

Para campanhas, a Priorização de Mensagens usa o horário de envio ideal de cada usuário para a ocorrência atual. Para etapas de mensagem do Canvas, a Braze usa o horário de envio calculado de cada usuário quando ele alcança a etapa, e reflete esse momento nas etapas de mensagem seguintes no mesmo caminho determinístico. Para saber mais, consulte [Intelligent Timing](#intelligent-timing).

### Existe alguma funcionalidade de relatório ou análise de dados específica para a Priorização de Mensagens? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

A Braze fornece eventos relacionados à Priorização de Mensagens no Currents e no compartilhamento de dados para canais compatíveis, incluindo e-mail, LINE, notificações por push, SMS, webhooks e WhatsApp. Isso inclui eventos de despriorização e de limite de frequência, registrados como o evento `users.messages.<channel>.Abort`, bem como eventos de nova tentativa que mostram quando uma mensagem foi posteriormente reenviada dentro da janela de nova tentativa configurada, registrados como o evento `users.messages.<channel>.Retry`.

Você também pode usar o dashboard de Diagnóstico de Mensagens, as estatísticas diárias existentes de despriorização e nova tentativa, e a [funcionalidade de relatórios da Braze]({{site.baseurl}}/user_guide/analytics/reporting) existente para monitorar a integridade e o desempenho das suas campanhas e Canvas priorizados.