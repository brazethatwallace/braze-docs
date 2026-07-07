---
nav_title: Relatórios de engajamento
article_title: Relatórios de engajamento
page_order: 5
local_redirect:
  report-glossary: '/docs/user_guide/analytics/metrics_glossary'
page_type: tutorial
description: "Este artigo prático orienta você na criação, personalização e programação de relatórios de engajamento para Campaigns e Canvas."
tool:
  - Campaigns
  - Canvas
  - Reports
---

# Relatórios de engajamento {#engagement-reports}

> Os relatórios de engajamento permitem que você extraia estatísticas de engajamento de mensagens específicas de Campaigns e Canvas para receber por e-mail no horário de sua preferência.

{% alert note %}
Você precisa da permissão "Export User Data" para executar relatórios de engajamento.
{% endalert %}

Com os relatórios de engajamento, você pode selecionar manualmente Campaigns e Canvas para incluir no seu relatório por e-mail ou especificar regras para selecionar automaticamente Campaigns e Canvas relevantes.

Independentemente do número de Campaigns ou Canvas selecionados, até dois arquivos CSV são gerados — um para todos os dados de Campaign e outro para todos os dados de Canvas. Você pode acessar esses arquivos CSV pelo link incorporado no e-mail do relatório. Os relatórios de engajamento não são salvos no dashboard da Braze.

Alguns dados são agregados no nível de Campaign ou Canvas, e não no nível de variante de campanha individual ou etapa do Canvas. Se você [excluir uma etapa do Canvas após o lançamento]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#canvas-details), isso também removerá os dados dos relatórios de engajamento.

{% alert tip %}
Você pode executar o relatório novamente para gerar estatísticas atualizadas.
{% endalert %}

## Criando um novo relatório {#creating-a-new-report}

### Etapa 1: Criar um relatório {#step-1-create-a-report}

Na sua conta do dashboard, acesse **Analytics** > **Engagement Reports**. Selecione **+ Create New Report**.

### Etapa 2: Adicionar mensagens {#step-2-add-messages}

Adicione as Campaigns e mensagens de Canvas que você deseja compilar no seu relatório. Você pode selecionar suas mensagens de duas formas:

- Selecionar manualmente Campaigns e Canvas
- Selecionar automaticamente Campaigns e Canvas com base em regras específicas

![engagement_reports_message_selection]({% image_buster /assets/img_archive/engagement_report_add_messages.png %})

#### Selecionar manualmente Campaigns ou Canvas {#manually-select-campaigns-or-canvases}

Essa opção oferece a liberdade de escolher quais Campaigns ou Canvas você deseja incluir neste relatório.

#### Selecionar automaticamente Campaigns ou Canvas {#automatically-select-campaigns-or-canvases}

Essa opção permite incluir automaticamente todas as mensagens que contêm uma [tag]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) específica. Você pode segmentar mensagens que possuem qualquer uma ou todas as tags listadas. Essa opção é útil se você está configurando relatórios recorrentes e costuma adicionar tags às suas mensagens de engajamento.

{% alert important %}
As tags devem corresponder a pelo menos uma Campaign ou Canvas para que o relatório seja gerado. Se você usar **Automatically select campaigns and Canvases based on specific rules** e encontrar um erro, confirme que pelo menos uma Campaign ou Canvas corresponde às suas tags e outros filtros (por exemplo, quando você exige todas as tags listadas, cada mensagem correspondente deve ter todas as tags).
{% endalert %}

### Etapa 3: Adicionar estatísticas {#add-statistics-to-your-reports}

A etapa **Add Stats** mostra as estatísticas para os tipos de Campaigns ou Canvas que você selecionou. Por exemplo, se você selecionou mensagens de e-mail, poderá visualizar apenas as estatísticas relevantes de e-mail. Se você escolheu uma combinação de e-mail e push, poderá visualizar as estatísticas desses dois canais.

![engagement_report_add_stats]({% image_buster /assets/img_archive/engagement_report_add_stats.png %})

Os relatórios de engajamento agregam dados por Campaign ou Canvas, não no nível do espaço de trabalho. Para monitorar o volume total de envios ou impressões em todas as Campaigns e Canvas ativos, como envios e impressões por canal em todo o espaço de trabalho, use o [Criador de relatórios]({{site.baseurl}}/report_builder).

{% alert note %}
*Envios para operadora* está descontinuado, mas continuará sendo suportado para usuários que já o utilizam.
{% endalert %}

| Canal | Estatísticas disponíveis |
| ------| --------------|
| E-mail | Envios, Aberturas, Aberturas únicas, Cliques, Cliques únicos, Taxa de cliques por abertura, Cancelamentos de inscrição, Bounces, Entregas, Spam reportado |
| Push  | Envios, Aberturas, Aberturas por influência, Bounces, Cliques no corpo |
| Push para a web | Envios, Aberturas, Bounces, Cliques no corpo |
| Mensagem no app | Impressões, Cliques, Cliques no primeiro botão, Cliques no segundo botão |
| Webhook  |  Envios, Erros |
| SMS | Envios, Envios para operadora, Entregas confirmadas, Falhas de entrega, Rejeições |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Adicionar estatísticas" }

### Etapa 4: Concluir a configuração do relatório {#step-4-complete-report-setup}

Dê um nome ao seu relatório, escolha como ele será formatado e selecione os destinatários. Por padrão, os relatórios de engajamento são enviados como um arquivo ZIP com dados delimitados por vírgula (onde cada dado é separado por uma vírgula).

Você pode selecionar entre as seguintes opções de compressão e delimitador:

- **Compressão:** ZIP, Sem compressão ou gzip
- **Delimitador:** Vírgula (`,`), Dois-pontos (`:`), Ponto e vírgula (`;`) ou Pipe (`|`)

{% alert note %}
As estatísticas são coletadas apenas para o intervalo de datas especificado pelo relatório. Para receber estatísticas precisas de taxa de abertura e cliques, selecione um intervalo de datas que inclua quando os eventos de envio foram realizados para suas Campaigns e Canvas.
{% endalert %}

#### Selecionar período {#select-time-frame}

Por padrão, o intervalo de dados exibido é baseado no fuso horário da sua empresa e vai desde a mensagem mais antiga selecionada até a data atual. Você pode personalizar isso selecionando o menu suspenso de datas e usando a seleção de intervalo personalizado OU selecionando o próximo botão de opção e definindo seu intervalo de datas com as opções disponíveis no menu suspenso.

#### Selecionar exibição de dados {#select-data-display}

Por padrão, os dados exibidos nos relatórios de engajamento são diários (um dia). Para visualizar esses dados em intervalos diferentes, escolha um número explícito de dias ou semanas para agregar os dados do relatório. Assim, em vez de ver métricas diárias, você pode visualizar seu engajamento por semana, mês, trimestre ou similar. Caso uma agregação baseada em tempo não seja suficiente, você também pode optar por exportar dados no nível de Campaign ou Canvas.

![engagement_reports_data_coverage]({% image_buster /assets/img_archive/engagement_report_datacoverage.png %})

##### Exibir dados por Campaign ou Canvas completo {#show-data-by-entire-campaign-or-canvas}

Quando você seleciona **Show Data by Entire Campaign or Canvas**, a Braze agrega as métricas em blocos de 1.825 dias (cinco anos) ao longo do intervalo de datas do relatório.

Se o intervalo de datas abranger mais de um bloco, você poderá ver várias linhas para a mesma Campaign ou Canvas com datas diferentes na coluna de data. Algumas linhas podem incluir apenas métricas registradas mais adiante no intervalo (por exemplo, cancelamentos de inscrição). As datas também podem ser anteriores ao início dos seus envios no espaço de trabalho, pois refletem os limites dos blocos na exportação, e não apenas o seu primeiro envio.

Para alinhar a coluna de data com o momento em que suas Campaigns e Canvas selecionados realmente enviaram, defina a [data de início do relatório em **Selecionar período**](#select-time-frame) para a data mais antiga que você deseja no arquivo — normalmente quando essas mensagens começaram a ser enviadas — em vez de manter o intervalo padrão que retrocede até a mensagem selecionada mais antiga.

#### Programar seu relatório {#schedule-your-report}

Existem duas opções ao programar seu relatório:

- **Send immediately:** Após o lançamento do relatório, a Braze enviará este relatório imediatamente.
- **Send at a designated time:** Essa opção oferece flexibilidade para escolher com que frequência você recebe este relatório. Você pode optar por enviar este relatório a cada número definido de dias, semanas ou meses. Também é possível definir quando parar de enviar o relatório.

![engagement_reports_schedule_report]({% image_buster /assets/img_archive/engagement_report_reportschedule.png %}){: style="max-width:65%;" }

### Etapa 5: Revisar e lançar {#step-5-review-and-launch}

A etapa final da configuração do seu relatório mostra uma visão geral somente leitura das opções configuradas. Revise seu relatório e, quando estiver satisfeito, selecione **Launch Report**.

### Etapa 6: Verificar seu e-mail {#step-6-check-your-email}

Você receberá um e-mail com links para seus relatórios no horário ou programação escolhidos. **Esses links expiram 1 hora após o envio do relatório.** Ao selecionar os links fornecidos, você fará o download automático de um arquivo ZIP contendo seus arquivos CSV — um para todas as Campaigns.

O relatório contém todas as estatísticas selecionadas na seção [Adicionar estatísticas](#add-statistics-to-your-reports) do processo de configuração.

## Solução de problemas {#troubleshooting}

### O relatório de engajamento não corresponde às métricas do Canvas ou da Campaign {#engagement-report-doesnt-match-metrics-from-the-canvas-or-campaign}

#### Intervalo de datas incompatível {#mismatched-time-range}

Certifique-se de que as datas no relatório de engajamento correspondam às datas na análise de dados do Canvas ou da Campaign (por exemplo, ambos cobrem de 1 a 15 de dezembro), mesmo que o Canvas tenha enviado apenas uma vez. Nas configurações do relatório de engajamento, verifique **Data Display** para confirmar que você está visualizando o Canvas ou a Campaign corretos. Se **Data Display** estiver configurado para mostrar dados a cada *X* dias, você obterá uma linha por data em que as métricas foram registradas para cada etapa.

Se os totais parecerem incorretos em uma planilha, limpe os filtros extras na exportação. Você pode somar as linhas diárias para reconciliá-las com os totais do Canvas ou da Campaign para o mesmo intervalo de datas.

{% alert note %}
Se você deseja linhas agregadas por Campaign ou Canvas completo em vez de buckets diários, semanais ou outros recorrentes, defina **Data Display** como **Show Data by Entire Campaign or Canvas**. Se a contagem de linhas ou as datas parecerem incorretas no CSV, consulte [Exibir dados por Campaign ou Canvas completo](#show-data-by-entire-campaign-or-canvas).
{% endalert %}

#### Cliques duplicados em botões em mensagens no app HTML {#duplicate-button-clicks-in-html-in-app-messages}

Se você usa mensagens no app HTML e os **Cliques no corpo** parecem altos no relatório de engajamento, pode ser que o registro de cliques esteja sendo disparado duas vezes — por exemplo, chamando `brazeBridge.logClick()` para um clique genérico no corpo e também `brazeBridge.logClick('body click')` (ou outro ID) na mesma interação. Pesquise no seu markup por `brazeBridge.logClick(` e alinhe com um padrão por controle. Para o uso recomendado, consulte [Rastreamento de botões]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#button-tracking-improvements).

#### Links quebrados em e-mails de relatórios de engajamento {#broken-links-in-emailed-engagement-reports}

Se os links em um e-mail de relatório de engajamento programado não abrirem corretamente no seu cliente de e-mail, tente os seguintes passos:

1. Encaminhe o relatório para uma caixa de entrada do Gmail e abra os links no Google Chrome.
2. Nas configurações do relatório de engajamento, confirme que **Report Schedule** está configurado para enviar quando você espera (por exemplo, imediatamente após a geração do relatório, em vez de em uma programação atrasada).