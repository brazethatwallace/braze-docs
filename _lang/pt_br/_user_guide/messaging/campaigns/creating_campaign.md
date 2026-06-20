---
nav_title: Criar uma campanha
article_title: Criar uma campanha
page_order: 1
page_type: tutorial
description: "Saiba como criar uma campanha de mensagens na Braze, desde a composição até o lançamento — incluindo envios multicanal — e como programar a entrega, direcionar públicos, atribuir eventos de conversão, enviar testes e lançar."
tool: Campaigns
---

# Criar uma campanha {#create-a-campaign}

> Use campanhas quando quiser alcançar consumidores com uma única etapa de envio de mensagens em um ou mais canais compatíveis. Para jornadas com várias etapas, use o [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/).

## Pré-requisitos {#prerequisites}

Para criar e lançar uma campanha, você precisa das permissões "Edit Campaigns" e "Launch Campaigns". Para ver a lista completa de permissões do espaço de trabalho e como elas aparecem no dashboard, consulte [Permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/).

### Antes de começar {#before-you-begin}

- Crie ou escolha os [segmentos]({{site.baseurl}}/user_guide/audience/segments/) que definem quem deve receber suas mensagens.
- Revise os [Conceitos básicos de campanhas]({{site.baseurl}}/user_guide/messaging/campaigns/campaign_basics/) para que os canais de envio de mensagens, tipos de entrega e metas de conversão estejam alinhados ao seu caso de uso.
- Para um passo a passo guiado sobre entrega, direcionamento e conversões, faça o curso do Braze Learning [Campaign Setup](https://learning.braze.com/campaign-setup-delivery-targeting-conversions).

## Criador de campanhas {#campaign-composer}

O criador de campanhas é onde você define as configurações de entrega, públicos, conversões e lançamento. Decida se você está criando uma campanha de canal único ou multicanal antes de continuar.

{% tabs %}
{% tab Canal único %}

Uma campanha de canal único alcança os usuários por meio de um canal de envio de mensagens por lançamento.

### O que é diferente {#whats-different}

#### Conversões e relatórios {#single-channel-conversions}

Para campanhas de canal único, a Braze rastreia os [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) que você atribui à campanha em relação aos envios daquele canal. Para janelas de atribuição e regras de contagem, consulte [Regras de rastreamento de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/#conversion-tracking-rules).

O [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/) e os limites de envio do espaço de trabalho ainda se aplicam.

### Criar uma campanha de canal único {#create-a-single-channel-campaign}

Para criar uma campanha:

1. Acesse **Messaging** > **Campaigns**.
2. Selecione **Create Campaign**.
3. Selecione o [canal]({{site.baseurl}}/user_guide/channels/) adequado ao seu caso de uso.
4. Na [etapa Redigir](#step-1-compose-messages), escreva e pré-visualize o conteúdo para esse canal.

Cada campanha usa um tipo de canal por vez. Adicione variantes quando quiser comparar divisões criativas ou executar [testes A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% endtab %}
{% tab Multicanal %}

Uma campanha multicanal alcança os usuários por meio de mais de um canal de envio de mensagens em um único lançamento. Por exemplo, enviar um e-mail e uma notificação por push juntos.

{% alert note %}
[In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages/) não estão disponíveis em campanhas multicanal. Crie uma campanha de canal único ou um Canvas.
{% endalert %}

### O que é diferente

#### Grupos de controle {#multichannel-control-groups}

Os grupos de controle de campanhas comparam variantes dentro de um canal (por exemplo, E-mail A versus E-mail B). Eles não são usados para comparar canais inteiros dentro de uma campanha multicanal. Para testar canais, criativos ou timing juntos ao longo de uma jornada, use o [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/).

#### Conversões e relatórios {#multichannel-conversions}

Para campanhas multicanal, a Braze rastreia os [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) por canal. Quando um usuário converte após receber mensagens em mais de um canal, a Braze pode atribuir essa conversão a esses canais. As contagens de conversão podem exceder *Usuários únicos*, e as taxas podem ultrapassar 100%. Para ver as regras completas, consulte [Regras de rastreamento de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/#conversion-tracking-rules).

Os limites de taxa para envios que abrangem canais estão descritos em [Campanhas multicanal e Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#multichannel-campaigns-and-canvases). Para regras em nível de espaço de trabalho (incluindo como envios multicanal contam para os limites), consulte [Limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/).

### Criar uma campanha multicanal {#create-a-multichannel-campaign}

1. Acesse **Messaging** > **Campaigns**.
2. Selecione **Create Campaign**.
3. Selecione **Multichannel**.
4. Na [etapa Redigir](#step-1-compose-messages), selecione **Add Channel** e escolha cada canal necessário. Selecione os ícones de canal para alternar entre os criadores enquanto escreve o conteúdo de cada canal.

{% endtab %}
{% endtabs %}

## Etapa 1: Redigir mensagens {#step-1-compose-messages}

### Detalhes da campanha {#campaign-details}

Use os campos a seguir para registrar metadados que ajudam sua equipe a encontrar e gerenciar a campanha.

| Campo | Finalidade |
| --- | --- |
| Nome | Use um nome claro que reflita o objetivo da campanha. |
| Descrição | Opcional. Explique a intenção ou inclua links para briefings para colaboradores. |
| Equipe | Opcional. Atribua [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) para que os grupos certos possam editar ou gerar relatórios sobre esse envio. |
| Tags | Opcional. Adicione [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) para filtrar em listas e ferramentas como o [Criador de relatórios]({{site.baseurl}}/user_guide/analytics/reports/report_builder/). |
| ID da campanha | Quando exibido no criador ou no resumo, copie esse identificador para chamadas de API, relatórios e integrações que referenciam uma campanha específica. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalhes da campanha" }

### Canais e editores {#channels-and-editors}

Componha o conteúdo específico do canal nesta etapa. Para orientações detalhadas, consulte [Canais]({{site.baseurl}}/user_guide/channels/) e abra o artigo do canal que você selecionou.

### Variantes {#variants}

Adicione variantes quando quiser comparar divisões criativas ou de entrega. Para informações sobre experimentos e controles, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% alert tip %}
Quando cada variante usa conteúdo semelhante, componha a mensagem **antes** de adicionar variantes extras. Em seguida, use **Copy from Variant** no menu **Add Variant** para reutilizar o trabalho entre variantes ou canais.
{% endalert %}

## Etapa 2: Programar entrega {#step-2-schedule-delivery}

Escolha quando os usuários se tornam elegíveis para receber a campanha:

| Tipo de entrega | Resumo |
| --- | --- |
| [Entrega agendada]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery/) | Envie em um horário ou cadência especificados. |
| [Entrega baseada em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/) | Envie quando os usuários realizarem comportamentos ou atenderem a condições que você definir. |
| [Entrega disparada por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/) | Envie quando seus sistemas chamarem a Braze para disparar a campanha para usuários elegíveis. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Programar entrega" }

Para conceitos de agendamento na Braze, consulte [Programar sua campanha]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

### Controles de entrega {#delivery-controls}

Dependendo do tipo de entrega, você pode ajustar a [reelegibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/) (se os usuários podem entrar na campanha novamente) e respeitar as regras de [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/) do espaço de trabalho. Você também pode configurar o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/) para que as mensagens não sejam enviadas durante janelas restritas.

## Etapa 3: Direcionar públicos {#step-3-target-audiences}

Em **Target Audiences**, defina quem é elegível para receber a campanha. Para ver todas as opções de direcionamento, passo a passo da interface e capturas de tela, consulte [Direcionar usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/).

### Opções de direcionamento {#targeting-options}

Nesta seção, você pode direcionar usuários escolhendo segmentos ou filtros para refinar seu público. Os usuários elegíveis ainda precisam atender ao gatilho ou critério que você definiu na etapa **Schedule Delivery**. O público-alvo funciona como uma sala de espera — apenas as pessoas que já estão dentro podem avançar quando a próxima ação acontecer.

As [listas de supressão]({{site.baseurl}}/user_guide/audience/suppression_lists/) do espaço de trabalho excluem automaticamente os usuários listados, a menos que você permita uma exceção para esta campanha.

### Resumo do público {#audience-summary}

Após adicionar segmentos ou filtros, o **Resumo do público** oferece uma pré-visualização de como é a população desse segmento, incluindo quantos usuários dentro dele são alcançáveis pelos canais selecionados. As contagens de alcance refletem os dados do seu espaço de trabalho, a configuração do canal e os filtros. Lembre-se de que a composição exata do segmento é sempre calculada antes do envio da mensagem. Para públicos muito grandes, a Braze pode exibir estimativas até que você calcule as estatísticas exatas.

### Busca de usuário {#user-lookup}

Após adicionar segmentos ou filtros, você pode testar se seu público está configurado conforme esperado buscando um usuário para confirmar se ele corresponde aos critérios do segmento. Para isso, pesquise o `external_id` ou `braze_id` de um usuário na seção **User Lookup**. Não é possível pesquisar por endereço de e-mail aqui. Consulte [Testando segmentos]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#testing-segments) para saber mais.

Quando um usuário corresponde aos critérios de segmento, filtro e app, um alerta informa isso. Quando um usuário não corresponde a parte ou a todos os critérios de segmento, filtro ou app, os critérios ausentes são listados para fins de solução de problemas.

### Enviar para estes usuários {#send-to-these-users}

Para canais baseados em inscrição (e-mail, SMS e similares), use **Send to these users** para enviar sua campanha apenas para usuários que tenham um status de inscrição específico, como aqueles que estão inscritos e optaram por receber e-mail.

### Limitar volume de envio {#limit-send-volume}

Você pode limitar o número total de usuários que recebem sua mensagem. Isso funciona como uma verificação independente dos filtros da sua campanha. Para mais informações, consulte [Definir um limite máximo de usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#setting-a-maximum-user-cap).

### Limitar a taxa de envio desta campanha {#limit-the-rate-at-which-this-campaign-sends}

Se você prevê que campanhas grandes causarão um pico na atividade dos usuários e sobrecarregarão seus servidores, pode especificar um limite de taxa por minuto para o envio de mensagens. Isso significa que a Braze não envia mais do que o limite configurado dentro de um minuto. Para mais informações, consulte [Limitação de taxa de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-speed-rate-limiting).

### Testes A/B {#ab-testing}

Você pode criar um [teste multivariante ou A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/) para qualquer campanha que direcione um único canal, mesmo que esse canal inclua vários dispositivos. Por exemplo, se quiser usar testes multivariantes ou A/B para uma campanha de push, você pode direcionar apenas dispositivos iOS ou apenas dispositivos Android — não ambos os tipos de dispositivo na mesma campanha.

Para campanhas de push, e-mail e webhook agendadas para envio único, você também pode usar uma [otimização]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations/). Uma otimização reserva uma parte do seu público-alvo do teste A/B e a mantém para um segundo envio otimizado com base nos resultados do primeiro teste.

## Etapa 4: Atribuir eventos de conversão {#step-4-assign-conversion-events}

Os [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) medem os resultados após um usuário receber sua campanha (ou entrar no grupo de controle). A Braze define como padrão **Starts Session** dentro de uma janela curta (três dias). Você pode definir eventos de conversão que correspondam aos seus KPIs, com até quatro eventos por campanha.

Após o lançamento, use o [dashboard de conversões]({{site.baseurl}}/user_guide/analytics/dashboards/conversions/) para analisar tendências de conversão em várias campanhas ou Canvas, comparar canais e ajustar intervalos de datas, métodos de atribuição e detalhamentos em um só lugar.

{% alert important %}
Não é possível adicionar ou remover eventos de conversão após o lançamento da campanha. Confirme os eventos antes de lançar.
{% endalert %}

## Etapa 5: Revisar resumo e lançar {#step-5-review-summary-and-launch}

A etapa **Review Summary** mostra as escolhas de agendamento, público, variantes e envio de mensagens. Antes de lançar sua campanha:

1. Confirme se os segmentos, variantes e configurações de entrega correspondem à sua intenção.
2. [Envie mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/) para validar a renderização e o comportamento nos seus dispositivos de teste ou destinatários internos.

Quando estiver pronto, selecione **Launch Campaign**.

### Aprovações {#approvals}

Se o seu espaço de trabalho usa aprovações, um colega com permissão para aprovar campanhas deve aprovar antes do lançamento. Para saber mais, consulte [Aprovações para campanhas e Canvas]({{site.baseurl}}/user_guide/messaging/governance/approvals/).

## Artigos relacionados {#related-articles}

- [Design e edição]({{site.baseurl}}/user_guide/messaging/design_and_edit/)
- [Testes A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/)
- [Saiba antes de enviar]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send/)
- [Análise de dados de campanhas]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics/)