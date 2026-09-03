---
nav_title: Dados de Segment
article_title: Dados de Segment
page_order: 4
page_type: reference
description: "Esta página explica a seção de Segments do dashboard da Braze e inclui um resumo das estatísticas fornecidas."
alias: /viewing_and_understanding_segment_data/
tool:
  - Segments
  - Reports

---
# Dados de Segment {#segment-data}

> Esta página explica a seção de Segments do dashboard da Braze e inclui um resumo das estatísticas fornecidas.

## Acessando dados sobre seus Segments e associações {#accessing-data-about-your-segments-and-membership}

A página **Segments** do dashboard da Braze contém um resumo de todos os seus Segments e permite que você examine dados detalhados de cada um. Nessa página, pesquise e selecione o nome de um Segment para editar e visualizar seus dados. Para saber como criar um Segment, confira [Criar um Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

![Página de Segments]({% image_buster /assets/img_archive/segments.png %})

Após selecionar o nome de um Segment, você pode visualizar as estatísticas e os filtros do Segment, além de editá-lo adicionando ou removendo filtros. Não se esqueça de salvar as alterações!

Quando você ativa o [rastreamento de análise de dados para um Segment]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking), é possível visualizar sessões, eventos personalizados e receita ao longo do tempo para esse Segment.

![Alternância de rastreamento de análise de dados para um Segment]({% image_buster /assets/img_archive/A_Tracking_2.png %})

### Estatísticas de Segment {#segment-statistics}

Você pode visualizar as seguintes estatísticas de Segment, que são atualizadas em tempo real conforme você adiciona ou remove filtros:

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Estatísticas de Segment">
  <caption>Estatísticas de Segment</caption>
    <thead>
        <tr>
            <th>Estatística</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Total de usuários</td>
            <td class="no-split">Quantos usuários seu app tem no total.</td>
        </tr>
        <tr>
            <td class="no-split">Usuários selecionados</td>
            <td class="no-split">Quantos usuários estão no seu Segment e qual porcentagem da sua base total de usuários eles representam.</td>
        </tr>
        <tr>
            <td class="no-split">LTV (usuários pagantes)</td>
            <td class="no-split">O valor do tempo de vida por usuário (LTV) neste Segment e o valor do tempo de vida por usuário pagante neste Segment. O LTV é calculado dividindo a receita total pelo total de usuários.</td>
        </tr>
        <tr>
            <td class="no-split">Contactável por e-mail (opt-in)</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Emailable' %} Devido às <a href="/docs/help/best_practices/spam_regulations#spam-regulationsspam regulations">regulamentações de SPAM</a>, é uma boa prática pedir que seus usuários façam opt-in explicitamente, implementando uma política de opt-in duplo em que os usuários devem clicar em um link em um e-mail de confirmação inicial. Para incentivar mais usuários a fazer opt-in, você pode direcionar uma mensagem para <a href="/docs/user_guide/channels/email/subscriptions#segmenting-by-user-subscriptions">aqueles que não fizeram opt-in nem opt-out</a>.</td>
        </tr>
        <tr>
            <td class="no-split">Push ativado (opt-in)</td>
            <td class="no-split">Push ativado refere-se ao número de usuários com pelo menos um token por push. Alguns usuários podem ter múltiplos tokens por push (por exemplo, se possuem um iPhone e um iPad), então o número de notificações por push que você envia para este Segment pode ser maior do que o número de usuários com "push ativado". "Opt-in" refere-se ao número de usuários que fizeram opt-in explicitamente para notificações por push. Os usuários devem sempre fazer opt-in explicitamente para que você possa enviar notificações por push a eles.</td>
        </tr>
    </tbody>
</table>

### Insights de Segment {#segment-insights}

Você pode ver como um Segment está se saindo em comparação com outro em um conjunto de KPIs pré-selecionados visitando a página [Insights de Segment]({{site.baseurl}}/user_guide/audience/segments/segment_insights) do seu dashboard.

### Uso em envio de mensagens {#messaging-use}
A seção **Messaging Use** mostra quais Segments, Campaigns ativas e Canvas ativos estão direcionando o seu Segment.

### Histórico de associação {#historical-membership}

A seção **Historical Membership** mostra como o tamanho do seu Segment mudou ao longo do tempo. Use o menu suspenso para filtrar a associação do Segment por intervalo de datas.

Para saber mais sobre como monitorar a associação e o tamanho do seu Segment, consulte [Medindo o tamanho do Segment]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

### Prévia de usuários {#user-preview}

Para visualizar informações detalhadas e específicas de usuários sobre seus Segments, clique em **User Data** e selecione **User Preview**.

Nessa página, você pode visualizar diversos atributos específicos de usuários, como gênero, idade, número de sessões e se fizeram opt-in para push e e-mail.

Observe que, em casos em que seu Segment é muito pequeno em relação ao tamanho do seu espaço de trabalho, é possível que a prévia de usuários retorne zero usuários. Isso não significa necessariamente que não existem usuários no seu Segment; execute [Calculate Exact Stats]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#statistics-for-segment-size) para determinar o tamanho exato do seu Segment.

![Prévia de usuários]({% image_buster /assets/img_archive/user_preview.png %})

## Visualizando dados de desempenho por Segment {#viewing-performance-data-by-segment}

Use os [modelos de relatório do Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/data_by_segments) para detalhar métricas de desempenho de Campaigns, Canvas, variantes e etapas por Segments.

## Criando um relatório de detalhamento por Segment usando o Criador de consultas {#creating-a-segment-breakdown-report-using-query-builder}

Para criar um relatório a partir de um modelo do [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder), acesse o **Criador de consultas** e faça o seguinte:

1. Selecione **Create SQL Query** > **Query Template**.
2. Filtre os modelos por aqueles que possuem métricas que incluem "segment breakdowns".
3. Selecione o modelo que deseja usar.
4. Preencha as variáveis no seu modelo SQL na guia [Variáveis](#variables).
5. (Opcional) Edite diretamente o SQL no modelo.
6. Selecione **Run Query**. Seus resultados serão exibidos em uma tabela.

## Variáveis {#variables}

Antes de gerar seu relatório, acesse a guia **Variables** para fornecer informações para o modelo do Criador de relatórios, incluindo variáveis obrigatórias que variam de acordo com o relatório.

As variáveis incluem:

- **Campaign ou Canvas:** você pode incluir uma ou várias Campaigns ou Canvas (não há limite máximo para quantas Campaigns ou Canvas você pode especificar). Se você não especificar nenhuma Campaign ou Canvas, o relatório incluirá todas as Campaigns ou Canvas do período escolhido.
- **Variante:** se estiver usando um modelo que oferece detalhamentos por variante, após selecionar uma Campaign ou Canvas, você pode selecionar variantes dentro dessa Campaign ou Canvas. Se você selecionar múltiplas variantes, seus resultados serão agrupados por variante.
- **Etapa:** se você selecionar uma variante de Canvas, poderá selecionar uma etapa do Canvas. Não é possível selecionar uma etapa sem antes selecionar uma variante de Canvas.
- **Período:** identifique o período do qual deseja extrair dados. Se nenhum período for especificado, o padrão será os últimos 30 dias.
- **Nome do produto:** se estiver executando um relatório para dados de compra, você pode identificar um produto específico para extrair dados.
- **Janela de conversão:** sempre obrigatória para relatórios com dados de receita e compra. O número de dias após o recebimento ou clique do e-mail em que a Braze deve atribuir compras ou receita.
- **Segments:** identifique os Segments para detalhar os dados. Se não for especificado, o relatório será executado para todos os Segments que possuem rastreamento de análise de dados ativado.
- **Tags:** especifique tags em **Variables** para executar seu relatório para todas as Campaigns ou Canvas com determinadas tags. Você pode incluir múltiplas tags. Se você adicionar tanto tags quanto Campaigns ou Canvas específicas a um relatório, seu relatório incluirá dados das suas tags e das Campaigns ou Canvas especificadas.

## Disponibilidade de dados {#data-availability}

Os dados estão disponíveis para períodos em que ambas as condições a seguir são atendidas:

1. O [rastreamento de análise de dados de Segment]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) está ativado para os Segments dos quais você deseja ver dados.
2. O recurso de dados de desempenho por Segment está ativado.

Você não pode acessar dados de períodos anteriores à ativação desse recurso para a sua empresa. Por exemplo, se o rastreamento de análise de dados estiver ativado para o Segment A em 1º de outubro e esse recurso for ativado para a sua empresa em 2 de outubro, então você só poderá visualizar dados do Segment A para as Campaigns e Canvas que registraram métricas após 2 de outubro.

Se a sua empresa ativou esse recurso em 2 de outubro e ativou o rastreamento de análise de dados para o Segment B em 3 de outubro, então você só poderá ver dados do Segment B para as Campaigns e Canvas que registraram métricas após 3 de outubro.