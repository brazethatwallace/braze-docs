---
nav_title: Eventos personalizados
article_title: Eventos personalizados
page_order: 1
page_type: reference
description: "Este artigo descreve eventos e propriedades personalizados, segmentação, uso, propriedades de entrada do Canvas, onde visualizar análises de dados relevantes e muito mais."
search_rank: 2
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Eventos personalizados {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> Este artigo descreve eventos e propriedades personalizados, histórico de eventos do perfil de usuário, filtros de segmentação relacionados, propriedades de entrada do Canvas, análises de dados relevantes e muito mais. Para saber mais sobre os eventos da Braze em geral, consulte [Eventos]({{site.baseurl}}/user_guide/data/activation/events).

Os eventos personalizados são ações realizadas por seus usuários ou atualizações sobre eles. Quando os eventos personalizados são registrados, eles podem disparar qualquer número e tipo de campanhas de acompanhamento. Em seguida, é possível usar os [filtros de segmentação](#segmentation-filters) para segmentar os usuários com base na frequência e em quão recentemente esses eventos personalizados ocorreram. Isso faz com que os eventos personalizados sejam mais adequados para o rastreamento de interações de alto valor com o usuário dentro do seu app.

## Casos de uso

Alguns casos de uso comuns de eventos personalizados incluem:

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## Gerenciando eventos personalizados

Você pode gerenciar, criar ou bloquear eventos personalizados no dashboard acessando **Data Settings** > **Custom Events**.

### Solução de problemas para atributos ou eventos personalizados duplicados

{% multi_lang_include data_activation/troubleshooting_duplicate_custom_data_entries.md %}

Selecione o menu ao lado de um evento personalizado para as seguintes ações:

### Bloqueio

Você pode bloquear eventos personalizados individuais pelo menu de ações ou selecionar e bloquear até 100 eventos em massa.

Quando você bloqueia um evento personalizado:

{% multi_lang_include data_activation/custom_event_block_effects.md %}

Além disso, se um evento personalizado bloqueado estiver sendo referenciado por filtros ou gatilhos em outras áreas da Braze, um modal de aviso aparecerá explicando que todas as instâncias dos filtros ou gatilhos que o referenciam serão removidas e arquivadas.

Para saber mais sobre bloqueio e exclusão de dados personalizados, consulte [Bloquear dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data).

### Adicionando descrições

Você pode adicionar uma descrição a um evento personalizado após sua criação se tiver a [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) `Manage Events, Attributes, Purchases`. Selecione **Edit description** para o evento personalizado e insira o que desejar, como uma nota para sua equipe.

### Adicionando tags

Você pode adicionar tags a um evento personalizado após sua criação se tiver a [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) "Manage Events, Attributes, Purchases". As tags podem então ser usadas para filtrar a lista de eventos.

### Exportando dados

Para exportar a lista de eventos personalizados como um arquivo CSV, selecione **Export all** no topo da página. O arquivo CSV é gerado e um link para download é enviado para o seu e-mail.

{% alert note %}
Não há um limite fixo no dashboard para a quantidade de **eventos personalizados** ou **atributos personalizados** que você pode definir ou armazenar em um perfil. Os limites práticos dependem do formato dos dados, do volume de ingestão e do desempenho do espaço de trabalho. Se você planeja rastrear um catálogo muito grande de eventos ou atributos, trabalhe com a equipe de conta da Braze para modelagem e higienização dos dados (por exemplo, [bloqueio]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data) de dados não utilizados).
{% endalert %}

## Visualizando relatórios de uso

O relatório de uso lista todos os Canvas, Campaigns e Segments que utilizam um evento personalizado específico. Essa lista não inclui usos de Liquid.

Você pode visualizar até 100 relatórios de uso por vez selecionando as caixas de seleção ao lado dos respectivos eventos personalizados e, em seguida, selecionando **Visualizar relatório de uso**.

## Registrando eventos personalizados

Eventos personalizados exigem configuração adicional. Consulte a documentação da plataforma a seguir para conhecer os métodos usados para registrar eventos personalizados e como adicionar propriedades e quantidades aos seus eventos personalizados.

{% details Expandir para documentação por plataforma %}

- [Android e FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=unity)
- [.NET MAUI (anteriormente Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=roku)

{% enddetails %}

Todos os dados armazenados no **Perfil de Usuário**, incluindo metadados de eventos personalizados (primeira ou última ocorrência, contagem total e X em Y ao longo de 30 dias), são retidos indefinidamente enquanto cada perfil estiver <a href="/docs/user_archival#active-users">ativo</a>.

## Visualizar o histórico de eventos de um usuário

{% alert important %}
O Histórico de Eventos está atualmente em acesso antecipado. Entre em contato com o gerente da sua conta Braze se tiver interesse em participar.
{% endalert %}

Use a guia **Histórico de Eventos** no perfil de um usuário para visualizar os eventos personalizados e compras recentes desse usuário. Isso ajuda a confirmar se a sua integração está registrando eventos corretamente e a solucionar problemas no nível do usuário diretamente no dashboard.

Para visualizar o histórico de eventos de um usuário:

1. Acesse **Público** > **Pesquisar Usuários** e selecione um usuário para abrir o perfil.
2. Selecione a guia **Histórico de Eventos**.

A guia lista os eventos personalizados e compras do usuário dos últimos 30 dias, até os 100 eventos mais recentes, ordenados do mais novo para o mais antigo.

Cada evento inclui:

- **Tipo de evento:** Se o evento é um evento personalizado ou uma compra.
- **Nome do evento:** O nome do evento conforme foi registrado.
- **Hora:** Quando o evento ocorreu.
- **Propriedades:** As propriedades completas do evento para aquela ocorrência, exibidas como JSON.

Casos de uso comuns incluem:

- Verificar se a integração do SDK ou da API está enviando eventos conforme esperado durante o desenvolvimento ou após um lançamento.
- Solucionar por que um usuário entrou ou não entrou em uma Campaign ou Canvas disparada por evento.
- Investigar um problema de suporte para um usuário específico sem precisar configurar uma exportação de dados.

{% alert note %}
Visualizar a guia **Histórico de Eventos** requer as permissões de usuário **Pesquisar Usuários**, **Visualizar IPI** e **Visualizar Propriedades de Eventos do Usuário**, pois as propriedades de eventos podem conter dados pessoais. Para saber mais, consulte [Permissões de usuário da empresa]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).
{% endalert %}

## Filtros de segmentação

A tabela a seguir mostra os filtros disponíveis para segmentar usuários por eventos personalizados.

| Opções de segmentação | Filtro suspenso | Opções de entrada |
| ---------------------| --------------- | ------------- |
| Verificar se o evento personalizado ocorreu **mais de X vezes** | **MORE THAN** | **NUMBER** |
| Verificar se o evento personalizado ocorreu **menos de X vezes** | **LESS THAN** | **NUMBER** |
| Verificar se o evento personalizado ocorreu **exatamente X vezes** | **EXACTLY** | **NUMBER** |
| Verificar se o evento personalizado ocorreu pela última vez **após a data X** | **AFTER** | **TIME** |
| Verificar se o evento personalizado ocorreu pela última vez **antes da data X** | **BEFORE** | **TIME** |
| Verificar se o evento personalizado ocorreu pela última vez **há mais de X dias** | **MORE THAN** | **NUMBER OF DAYS AGO** (número positivo) |
| Verificar se o evento personalizado ocorreu pela última vez **há menos de X dias** | **LESS THAN** | **NUMBER OF DAYS AGO** (número positivo) |
| Verificar se o evento personalizado ocorreu **mais de X (máx. = 50) vezes** | **MORE THAN** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
| Verificar se o evento personalizado ocorreu **menos de X (máx. = 50) vezes** | **LESS THAN** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
| Verificar se o evento personalizado ocorreu **exatamente X (máx. = 50) vezes** | **EXACTLY** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtros de segmentação" }

## Análise de dados

A Braze registra o número de vezes que eventos personalizados ocorreram e a última vez que foram realizados por cada usuário para segmentação. Para configuração de relatórios, filtros e opções de exportação, consulte [Relatório de eventos personalizados]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report).

Na página **Custom Events Report**, você pode visualizar de forma agregada a frequência com que cada evento personalizado ocorre. As linhas cinzas sobrepostas na série temporal indicam a última vez que uma Campaign foi enviada, o que é útil para visualizar como suas Campaigns afetaram a atividade de eventos personalizados.

![Gráfico de contagem de eventos personalizados na página Custom Events no dashboard mostrando tendências para um evento personalizado]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

Você também pode usar **Filters** para detalhar seus eventos personalizados por hora, média mensal de usuários ativos (MAU), Segments ou fórmulas de KPI.

![Filtros do gráfico de eventos personalizados]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[Incremente atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) para manter um contador de uma ação do usuário semelhante a um evento personalizado. No entanto, não é possível visualizar dados de atributos personalizados em uma série temporal. Ações do usuário que não precisam ser analisadas em uma série temporal devem ser registradas usando esse método.
{% endalert %}

### Por que a análise de dados de eventos personalizados não está aparecendo

Segments criados com dados de eventos personalizados não podem exibir dados históricos anteriores à data de criação.

## Propriedades de eventos personalizados

As propriedades de eventos personalizados são metadados ou atributos de eventos personalizados que descrevem uma ocorrência específica de um evento. Essas propriedades podem ser usadas para qualificar ainda mais as condições de gatilho, aumentar a personalização no envio de mensagens, rastrear conversões e gerar análises de dados mais sofisticadas por meio da exportação de dados brutos.

Para saber mais, consulte [Propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).