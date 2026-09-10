---
nav_title: Criador de relatórios
article_title: Criador de relatórios
alias: /report_builder/
page_type: reference
description: "Este artigo de referência descreve o recurso Criador de relatórios."
tool:
    - Reports
page_order: 3
---

# Criador de relatórios {#report-builder}

> Esta página explica como usar o Criador de relatórios para criar e visualizar relatórios detalhados com dados da Braze, e como adicionar relatórios a dashboards.

O vídeo a seguir apresenta uma visão geral de como criar e personalizar relatórios no Criador de relatórios.

{% multi_lang_include video.html id="oi66kwwldv" source="wistia" %}

## Usando um modelo de relatório {#using-a-report-template}

1. Acesse **Analytics** > **Report Builder (New)**.
2. Selecione a seta **Mais opções** ao lado do botão **Create New Report** e, em seguida, selecione **Use a report template**.<br><br>![Menu suspenso do botão "Create New Report" com opções para criar um relatório personalizado ou usar um modelo.]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Selecione um dos modelos de relatório da biblioteca de modelos da Braze.
    - Use os menus suspensos **Row items** e **Tags** para encontrar relatórios relevantes para seus casos de uso.<br><br>![Janela "Braze report templates" com uma lista de modelos da Braze para selecionar.]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. Siga a etapa 3 em diante em [Criando um relatório](#creating-a-report) para personalizar ainda mais o relatório de acordo com seu caso de uso.

## Criando um relatório {#creating-a-report}

1. Acesse **Analytics** > **Report Builder (New)**.
2. Selecione **Create New Report**.
3. No menu suspenso **Rows**, selecione sobre o que você deseja gerar o relatório:
    - Campaigns
    - Canvas
    - Campaigns e Canvas
    - Canais
    - Tags

    Sua seleção em **Rows** impacta [as métricas que você pode visualizar](#metrics-availability). Por exemplo, você pode visualizar métricas multivariantes apenas se gerar o relatório sobre **Canvas** ou **Campaigns** com um detalhamento por **Variant**. Não é possível visualizar essas métricas ao gerar relatórios sobre **Campaigns and Canvases**, mesmo que essas Campaigns e Canvas tenham testes multivariantes.

![A seção "Rows and columns" com campos para selecionar as linhas e agrupamentos do seu relatório.]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

{: start="4"}
4. (Opcional) Selecione **Add drilldown** para detalhar seus dados em visualizações mais granulares:
    - Canais
    - Data
        - Use isso para dividir seus dados em intervalos de tempo menores. Por exemplo, se você quer saber como suas Campaigns se saíram por dia, selecione a seguinte configuração:
            - **Rows**: Campaigns
            - **Grouping:** Data
            - **Interval:** Dias
    - Variantes
    - Campaigns e Canvas

{% alert tip %}
Experimente diferentes configurações de opções de detalhamento para explorar as [diversas maneiras de detalhar seus dados](#metrics-availability).
{% endalert %}

{: start="5"}
5. Na seção **Columns**, selecione **Customize Metrics**.

![A seção "Customize Metrics" com opções para selecionar múltiplas métricas.]({% image_buster /assets/img/report_builder_2/customize_metrics.png %}){: style="width:90%;"}

{: start="6"}
6. Navegue pelas métricas por categoria e marque a caixa de seleção correspondente para adicionar uma métrica ao seu relatório.
    - Em **General**, selecione **Tags** para incluir as tags aplicadas a cada Campaign ou Canvas nas linhas do seu relatório.
    - Reordene as métricas e colunas arrastando o ícone pontilhado para cima ou para baixo.
7. Em **Report content**, configure o intervalo de datas para o qual você deseja incluir dados no seu relatório.
8. Em seguida, dependendo das suas seleções na etapa 3, escolha adicionar manualmente ou automaticamente Campaigns, Canvas ou ambos ao seu relatório.
    - **Adicionar manualmente:** Escolha cada Campaign ou Canvas a ser incluída no relatório usando os filtros de datas de **Last Sent** e tags ou canais, ou pesquisando pelo nome da Campaign ou Canvas.<br><br>![A seção "Manually add campaigns and canvases" com uma lista de Campaigns para selecionar.]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **Adicionar automaticamente:** Defina regras para quais Campaigns ou Canvas devem ser incluídas no relatório. Você só precisa selecionar um campo nesta página.
        - À medida que Campaigns ou Canvas adicionais atendam às condições definidas nesta tela, elas serão automaticamente adicionadas às futuras execuções do seu relatório.
        - Banner não é uma opção no menu suspenso **Channel**, então você não pode usar regras de canal para adicionar automaticamente Campaigns ou Canvas de Banner. Ainda assim, você pode incluir KPIs de Banner nas métricas do seu relatório.<br><br>![A seção "Automatically add campaigns and canvases" com campos para definir regras de quais Campaigns e Canvas devem ser adicionadas ao relatório.]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9. Execute o relatório selecionando **Save & Run**.

{% alert note %}
O relatório pode levar alguns minutos para ser executado, dependendo do intervalo de datas e do número de Campaigns ou Canvas selecionados na etapa de configuração.
{% endalert %}

## Disponibilidade de métricas {#metrics-availability}

Sua seleção para **Linhas** afeta as métricas que você pode selecionar.

{% alert tip %}
Se você deseja gerar relatórios sobre variantes ou etapas de Canvas, selecione **Canvas** para linhas e deixe o campo vazio ou selecione **Data** como detalhamento. Após executar o relatório, um menu suspenso **Visualização de Canvas** aparece na página de resultados para visualizar métricas apenas do Canvas, ou agrupar métricas por variante, etapa ou mensagem.<br><br> Ao editar seu relatório, a tabela de prévia exibe no máximo 50 linhas. Execute o relatório para visualizar todas as linhas na página de resultados com paginação (100 linhas por página) ou exporte o conjunto de dados completo como CSV.

![O menu suspenso "Visualização de Canvas" aberto.]({% image_buster /assets/img/report_builder_2/canvas_view_dropdown.png %}){: style="width:40%;"}
{% endalert %}

| Métrica | Descrição |
| --- | --- |
| Métricas de conversão | Disponível para Campaigns, Canvas, Campaigns e Canvas. |
| Entradas | Disponível para Campaigns, Canvas, Campaigns e Canvas, Tags. |
| Data do último envio | Disponível para Campaigns, Canvas, Campaigns e Canvas. Exibido apenas para campanhas agendadas — não é preenchido para campanhas baseadas em ação ou disparadas por API. |
| Tags | Disponível para Campaigns, Canvas, Campaigns e Canvas. Lista as tags aplicadas a cada Campaign ou Canvas. Quando uma mensagem possui várias tags, elas aparecem como uma lista separada por ponto e vírgula. |
| Envios | Disponível para cada canal relevante. |
| Mensagens enviadas | Disponível para Campaigns, Canvas, Campaigns e Canvas, Tags. |
| Linha de assunto | Disponível para Campaigns de e-mail com detalhamento por **Variante**, Canvas e Canvas com detalhamento por **Variante**. |
| Receita total | Disponível para Campaigns, Canvas, Campaigns e Canvas, Tags. Indisponível com detalhamento por **Canais**. |
| Impressões únicas | Disponível para Campaigns, Canvas, Campaigns e Canvas, Tags. |
| Destinatários únicos | Disponível para Campaigns, Canvas, Campaigns e Canvas, Tags. Indisponível com detalhamento por **Canais**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Disponibilidade de métricas" }

### Variantes de mensagem excluídas {#deleted-message-variants}

As estatísticas de variantes de mensagem excluídas não são exibidas quando você detalha seu relatório por Campaigns ou Canvas. No entanto, os totais no nível do canal incluem todas as estatísticas, independentemente de a variante ter sido excluída. Por exemplo, _Envios_ para e-mail incluem todos os envios de e-mail, mas se você detalhar essas estatísticas por Campaign, os números podem ser menores porque os envios de variantes de mensagem excluídas são filtrados.

No mesmo relatório, _Destinatários únicos_ pode ser maior do que _Impressões únicas_ quando uma variante de mensagem foi excluída após o envio. _Destinatários únicos_ no nível da Campaign ainda podem incluir usuários que receberam a variante excluída, enquanto _Impressões únicas_ omitem as estatísticas de variantes excluídas nas agregações no nível da mensagem.

## Visualizando um relatório {#viewing-a-report}

Após executar seu relatório, você pode visualizar os resultados em formato de tabela na página de resultados do relatório.

![Uma tabela com os dados do relatório para as métricas de cada Campaign.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### Criando um gráfico de relatório {#creating-a-report-chart}

Na parte inferior da página, você pode criar um gráfico dos seus dados selecionando um **Tipo de gráfico** e configurando as métricas do gráfico. Por padrão, a primeira métrica será exibida.

![Um gráfico dos dados do relatório com opções para configurar o eixo x, o eixo y, o tipo de gráfico e mais.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
Para criar um gráfico de linhas, selecione **Data** como opção de detalhamento ao configurar o relatório. Isso exibe tendências ao longo do tempo.
{% endalert %}

#### Baixando um gráfico de relatório {#downloading-a-report-chart}

Para baixar uma imagem do gráfico de relatório, selecione o ícone de pontos e escolha uma opção de download.

![Um menu com opções de download para diferentes formatos de arquivo.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:70%;"}

## Compartilhando um relatório {#sharing-a-report}

Você pode compartilhar um link do dashboard para o relatório selecionando **Share** e uma destas opções:
- **Share a link:** Copie e compartilhe o link.
- **Send or schedule an email:** Envie um e-mail imediatamente ou em um horário designado contendo um link para download que expira após uma hora. Você pode selecionar destinatários a partir dos usuários da empresa listados no menu suspenso **Email Recipients** ou inserir qualquer outro endereço de e-mail.

{% alert note %}
O menu suspenso **Email Recipients** lista apenas usuários da empresa na Braze e salva os endereços de e-mail deles entre os agendamentos de relatórios. Endereços de e-mail externos devem ser inseridos manualmente cada vez que você criar um novo agendamento de relatório. Se você envia relatórios com frequência para destinatários externos, como um contato de parceiro, considere adicioná-los como usuário da empresa com as permissões apropriadas para que o endereço apareça no menu suspenso.
{% endalert %}

![Janela "Schedule an email" com campos para escolher como o relatório é formatado, quem deve recebê-lo e quando ele deve ser enviado.]({% image_buster /assets/img/report_builder_2/schedule_an_email.png %}){: style="max-width:70%;"}

- **Download CSV:** Faça o download de um CSV do relatório.

## Adicionando um relatório a um dashboard {#adding-a-report-to-a-dashboard}

1. Selecione o ícone de três pontos no topo da tabela do relatório.
2. Selecione **Adicionar ao dashboard**.
3. Selecione se deseja criar um novo dashboard ou adicionar a um dashboard existente.<br><br>![Janela com opções para selecionar se você deseja adicionar o relatório a um dashboard novo ou existente.]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. Siga as etapas no [Criador de dashboards]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder) para saber mais sobre como criar um dashboard.

## Permissões de equipe {#team-permissions}

Os relatórios do Criador de relatórios não suportam [atribuição de equipe]({{site.baseurl}}/user_guide/administer/global/user_management/teams) como Campaigns ou Canvas. Não é possível limitar um relatório salvo a uma equipe específica ao criá-lo.

Usuários com permissão ["View Dashboard Reports"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) no nível de equipe (em vez de no nível do espaço de trabalho) ainda podem usar o Criador de relatórios, mas a visibilidade dos relatórios é limitada:

- Esses usuários só veem relatórios em que todas as Campaigns e Canvas selecionados estão atribuídos às suas equipes.
- Relatórios com **Canais** como linhas ficam ocultos.
- Relatórios que usam seleção automática para adicionar Campaigns ou Canvas ficam ocultos, porque a Braze não consegue verificar o acesso da equipe para mensagens que podem ser adicionadas quando o relatório é executado.

O [Criador de relatórios (legado)]({{site.baseurl}}/report_builder_legacy) define por equipe quais Campaigns e Canvas você pode adicionar a um relatório, mas os relatórios salvos não são filtrados da lista da mesma forma que no Criador de relatórios (novo). Para configuração de permissões, consulte [Configuração de permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) e [Equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams).

## Solução de problemas {#troubleshooting}

### O relatório não mostra envios para uma Campaign ou Canvas {#report-shows-no-sends-for-a-campaign-or-canvas}

Uma Campaign ou Canvas aparece no relatório quando a data do **Último envio** está dentro da janela de **Último envio** que você configurou. **Envios** e outras métricas só são preenchidos para atividades dentro do intervalo de datas de **Exibir dados para**. Se a mensagem não foi enviada durante o período de **Exibir dados para**, a linha ainda pode listar a Campaign ou Canvas com zero envios.

Por exemplo, suponha que **Último envio** seja de 1º de janeiro de 2025 a 14 de abril de 2025, então uma Campaign é incluída, mas **Exibir dados para** está definido como 1º de dezembro de 2024 a 14 de janeiro de 2025. Se essa Campaign não teve envios em dezembro ou janeiro, ela ainda aparece na tabela sem métricas de envio.

### O link de download expirou {#download-link-has-expired}

Os links de download de relatórios expiram após uma hora. Se o seu link expirou, gere um novo relatório e faça o download dentro de uma hora. Não há como estender o tempo de vencimento.

Se você tiver um [bucket Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) conectado em **Integrações com parceiros**, é possível recuperar dados de relatórios anteriores navegando diretamente no seu bucket S3.