---
nav_title: Eventos personalizados
article_title: Eventos personalizados
page_order: 1
page_type: reference
description: "Este artigo descreve eventos e propriedades personalizados, segmentação, uso, propriedades de entrada do Canvas, onde visualizar análises de dados relevantes e muito mais."
search_rank: 2
---

# [![curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Eventos personalizados {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> Este artigo descreve eventos e propriedades personalizados, histórico de eventos do perfil de usuário, filtros de segmentação relacionados, propriedades de entrada do Canvas, análises de dados relevantes e muito mais. Para saber mais sobre os eventos da Braze em geral, consulte [Eventos]({{site.baseurl}}/user_guide/data/activation/events/).

Os eventos personalizados são ações realizadas por seus usuários ou atualizações sobre eles. Quando os eventos personalizados são registrados, eles podem disparar qualquer número e tipo de campanhas de acompanhamento. Em seguida, é possível usar os [filtros de segmentação](#segmentation-filters) para segmentar os usuários com base na frequência e em quão recentemente esses eventos personalizados ocorreram. Isso faz com que os eventos personalizados sejam mais adequados para o rastreamento de interações de alto valor com o usuário dentro do seu app.

## Casos de uso {#use-cases}

Alguns casos de uso comuns de eventos personalizados incluem:

- Disparar uma Campaign ou Canvas com base em um evento personalizado usando a [entrega baseada em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/)
- Segmentar usuários pela quantidade de vezes que realizaram um evento personalizado, quando foi a última vez que o evento ocorreu, e similares
- Usar a [análise de dados de eventos personalizados](#analytics) do dashboard para visualizar um agregado de quantas vezes cada evento ocorreu
- Encontrar análises de dados adicionais usando relatórios de [funil]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/#step-2-select-events-for-funnel-steps) e [retenção]({{site.baseurl}}/user_guide/analytics/reports/retention_reports/)
- Aproveitar [propriedades de entrada persistentes]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/) para usar metadados do seu evento personalizado para personalização nas etapas do Canvas
- Gerar análises de dados mais sofisticadas com o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)
- Configurar [critérios de saída]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria/) para definir quando os usuários devem sair do seu Canvas

## Gerenciando eventos personalizados {#managing-custom-events}

Você pode gerenciar, criar ou bloquear eventos personalizados no dashboard acessando **Configurações de dados** > **Eventos personalizados**.

Selecione o menu ao lado de um evento personalizado para as seguintes ações:

### Bloqueio {#blocklisting}

Você pode bloquear eventos personalizados individuais pelo menu de ações, ou selecionar e bloquear até 100 eventos em massa.

Quando você bloqueia um evento personalizado:

- Dados futuros não serão coletados para esse evento.
- Dados existentes não estarão disponíveis a menos que o evento seja desbloqueado.
- Esse evento não aparecerá em filtros ou gráficos.

Além disso, se um evento personalizado bloqueado estiver sendo referenciado por filtros ou gatilhos em outras áreas da Braze, um modal de aviso aparecerá explicando que todas as instâncias dos filtros ou gatilhos que o referenciam serão removidas e arquivadas.

Para mais detalhes sobre bloqueio e exclusão de dados personalizados, consulte [Bloquear dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).

### Adicionando descrições {#adding-descriptions}

Você pode adicionar uma descrição a um evento personalizado após sua criação se tiver a [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) `Manage Events, Attributes, Purchases`. Selecione **Editar descrição** para o evento personalizado e insira o que desejar, como uma nota para sua equipe.

### Adicionando tags {#adding-tags}

Você pode adicionar tags a um evento personalizado após sua criação se tiver a [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) "Manage Events, Attributes, Purchases". As tags podem então ser usadas para filtrar a lista de eventos.

### Exportando dados {#exporting-data}

Para exportar a lista de eventos personalizados como um arquivo CSV, selecione **Exportar tudo** no topo da página. O arquivo CSV será gerado e um link para baixar será enviado por e-mail para você.

{% alert note %}
Não há um limite fixo no dashboard para a quantidade de **eventos personalizados** ou **atributos personalizados** distintos que você pode definir ou armazenar em um perfil; os limites práticos dependem do formato dos dados, do volume de ingestão e do desempenho do espaço de trabalho. Se você planeja rastrear um catálogo muito grande de eventos ou atributos, trabalhe com a equipe de conta da Braze para modelagem e higienização (por exemplo, [bloqueio]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/) de dados não utilizados).
{% endalert %}

## Visualizando relatórios de uso {#viewing-usage-reports}

O relatório de uso lista todos os Canvas, Campaigns e Segments que utilizam um evento personalizado específico. Esta lista não inclui usos de Liquid.

Você pode visualizar até 100 relatórios de uso por vez selecionando as caixas de seleção ao lado dos respectivos eventos personalizados e então selecionando **Visualizar relatório de uso**.

## Registrando eventos personalizados {#logging-custom-events}

Eventos personalizados requerem configuração adicional. Consulte a lista abaixo para a documentação de cada plataforma, onde você encontrará informações sobre os métodos usados para registrar eventos personalizados e como adicionar propriedades e quantidades aos seus eventos personalizados.

{% details Expandir para documentação por plataforma %}

- [Android e FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=unity)
- [.NET MAUI (anteriormente Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## Armazenamento de eventos personalizados {#custom-event-storage}

Todos os dados armazenados no **Perfil de usuário**, incluindo metadados de eventos personalizados (primeira ou última ocorrência, contagem total e X em Y ao longo de 30 dias), são retidos indefinidamente enquanto cada perfil estiver [ativo]({{site.baseurl}}/user_archival/#active-users).

## Visualizar o histórico de eventos de um usuário {#view-a-users-event-history}

{% alert important %}
O Histórico de eventos está atualmente em acesso antecipado. Entre em contato com o gerente de conta da Braze se tiver interesse em participar.
{% endalert %}

Use a guia **Histórico de eventos** no perfil de um usuário para visualizar os eventos personalizados e compras recentes desse usuário. Isso ajuda a confirmar se a integração está registrando eventos corretamente e a solucionar problemas no nível do usuário diretamente no dashboard.

Para visualizar o histórico de eventos de um usuário:

1. Acesse **Público** > **Pesquisar usuários** e selecione um usuário para abrir o perfil.
2. Selecione a guia **Histórico de eventos**.

A guia lista os eventos personalizados e compras do usuário nos últimos 30 dias, até os 100 eventos mais recentes, ordenados do mais novo para o mais antigo.

Cada evento inclui:

- **Tipo de evento:** Se o evento é um evento personalizado ou uma compra.
- **Nome do evento:** O nome do evento conforme foi registrado.
- **Horário:** Quando o evento ocorreu.
- **Propriedades:** As propriedades completas do evento para aquela ocorrência, exibidas como JSON.

Casos de uso comuns incluem:

- Verificar se a integração do SDK ou da API está enviando eventos conforme esperado durante o desenvolvimento ou após um lançamento.
- Solucionar problemas sobre por que um usuário entrou ou não em uma Campaign ou Canvas disparados por evento.
- Investigar um problema de suporte para um usuário específico sem precisar configurar uma exportação de dados.

{% alert note %}
Visualizar a guia **Histórico de eventos** requer as permissões de usuário **Pesquisar usuários** e **Visualizar IPI**, pois as propriedades de eventos podem conter dados pessoais. Para saber mais, consulte [Permissões de usuário da empresa]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/).
{% endalert %}

## Filtros de segmentação {#segmentation-filters}

A tabela a seguir mostra os filtros disponíveis para segmentar usuários por eventos personalizados.

| Opções de segmentação | Filtro do dropdown | Opções de entrada |
| ---------------------| --------------- | ------------- |
| Verificar se o evento personalizado ocorreu **mais de X vezes** | **MAIS QUE** | **NÚMERO** |
| Verificar se o evento personalizado ocorreu **menos de X vezes** | **MENOS QUE** | **NÚMERO** |
| Verificar se o evento personalizado ocorreu **exatamente X vezes** | **EXATAMENTE** | **NÚMERO** |
| Verificar se o evento personalizado ocorreu pela última vez **após a data X** | **APÓS** | **DATA** |
| Verificar se o evento personalizado ocorreu pela última vez **antes da data X** | **ANTES** | **DATA** |
| Verificar se o evento personalizado ocorreu pela última vez **há mais de X dias** | **MAIS QUE** | **NÚMERO DE DIAS ATRÁS** (Número positivo) |
| Verificar se o evento personalizado ocorreu pela última vez **há menos de X dias** | **MENOS QUE** | **NÚMERO DE DIAS ATRÁS** (Número positivo) |
| Verificar se o evento personalizado ocorreu **mais de X (Máx = 50) vezes** | **MAIS QUE** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
| Verificar se o evento personalizado ocorreu **menos de X (Máx = 50) vezes** | **MENOS QUE** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
| Verificar se o evento personalizado ocorreu **exatamente X (Máx = 50) vezes** | **EXATAMENTE** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtros de segmentação" }

## Análise de dados {#analytics}

A Braze registra o número de vezes que eventos personalizados ocorreram e a última vez que foram realizados por cada usuário para segmentação. Visualize essas análises de dados acessando **Analytics** > **Relatório de eventos personalizados**.

Na página **Relatório de eventos personalizados** no dashboard, você pode visualizar de forma agregada a frequência com que cada evento personalizado ocorre. As linhas cinzas sobrepostas na série temporal indicam a última vez que uma Campaign foi enviada, o que é útil para ver como suas Campaigns afetaram a atividade de eventos personalizados.

![Gráfico de contagem de eventos personalizados na página de Eventos personalizados no dashboard mostrando tendências para um evento personalizado]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

Você também pode usar **Filtros** para detalhar seus eventos personalizados por hora, média mensal de usuários ativos (MAU), segmentos ou fórmulas de KPI.

![Filtros do gráfico de eventos personalizados]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[Incremente atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#integers) para manter um contador de ações do usuário semelhante a um evento personalizado. No entanto, você não pode visualizar dados de atributos personalizados em uma série temporal. Ações do usuário que não precisam ser analisadas em uma série temporal devem ser registradas usando este método.
{% endalert %}

### Por que a análise de dados de eventos personalizados não está aparecendo {#why-custom-events-analytics-arent-showing}

Segmentos criados com dados de eventos personalizados não podem exibir dados históricos anteriores à sua criação.

## Propriedades de eventos personalizados {#custom-event-properties}

Propriedades de eventos personalizados são metadados ou atributos de eventos personalizados que descrevem uma ocorrência específica de um evento. Essas propriedades podem ser usadas para qualificar ainda mais condições de disparo, aumentar a personalização no envio de mensagens, rastrear conversões e gerar análises de dados mais sofisticadas por meio da exportação de dados brutos.

Para saber mais, consulte [Propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/).