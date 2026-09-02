---
nav_title: Insights de Segment
article_title: Insights de Segment
page_order: 6
page_type: tutorial
tool:
  - Segments
  - Reports
description: "Este artigo de instruções mostra como usar, interpretar e compartilhar os insights de Segment."
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Insights de segmento {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsegmentation-course-stylefloatrightwidth120pxborder0-classnoimgbordersegment-insights}

> Saiba como usar, interpretar e compartilhar os insights de Segment.

Os insights de Segment mostram o desempenho de um Segment em comparação com outro em um conjunto de KPIs pré-selecionados.

## Visualizando insights de Segment {#viewing-segment-insights}

Acesse a página **Segment Insights** no seu dashboard, em **Analytics**, para visualizar até 10 segmentos diferentes comparados com uma linha de base.

![Dashboard de Segment Insights comparando três segmentos, "UK Users", "FR Users" e "CA Users" com um Segment de linha de base, "All Users".]({% image_buster /assets/img_archive/segment_insights.png %})

{% alert note %}
As estatísticas na página de Segment Insights são estimadas por padrão. Para calcular valores exatos, abra um Segment e selecione **Calculate Exact Statistics**. As estimativas podem ser maiores ou menores do que os valores exatos, especialmente em espaços de trabalho grandes ou para segmentos pequenos.
{% endalert %}

O Segment de linha de base pode ser um Segment específico que você selecionar ou um Segment contendo todos os seus usuários. Você pode comparar as seguintes estatísticas usando Segment Insights:

| Medida | Descrição | Fórmula |
| --------------------- | ------------- | ------------- |
| Sessões por dia | Número médio de sessões por dia dos usuários do Segment | (nº total de sessões) / (nº de dias desde a primeira sessão) |
| Dias desde a primeira sessão | Número médio de dias entre a primeira sessão dos usuários do Segment e agora | hoje – data da primeira sessão |
| Dias desde a última sessão | Número médio de dias entre a última sessão dos usuários do Segment e agora | hoje – data da última sessão |
| Receita vitalícia em dólares | Receita média vitalícia em dólares dos usuários do Segment | gasto vitalício do usuário |
| Dias desde a primeira compra | Número médio de dias entre a primeira sessão e a primeira compra dos usuários do Segment | data da primeira compra – data da primeira sessão |
| Dias desde a última compra | Número médio de dias entre a última compra dos usuários do Segment e agora | hoje – data da última compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Visualizando insights de Segment" }

Você pode compartilhar facilmente comparações específicas com seus colegas usando a URL exclusiva da página, e também pode selecionar o ícone de olho ao lado de cada Segment para revelar mais informações sobre ele. Essas comparações serão redefinidas quando você alternar entre espaços de trabalho.

![Detalhes do Segment "Premium Users (iOS VideoApp)" com um gráfico exibindo o histórico de membros e um quadro que detalha o tamanho estimado para diversos canais de envio de mensagens.]({% image_buster /assets/img_archive/Segment_Insights_Info.png %}){: style="max-width:50%;"}

## Página de detalhes do Segment {#segment-details-page}

Os insights de Segment também foram integrados diretamente à visualização **Detalhes do Segment**. Ao analisar um Segment específico que você configurou anteriormente, é possível encontrar as mesmas seis estatísticas descritas na caixa dinâmica e cinza de Estatísticas do Segment. A partir daqui, você pode iniciar rapidamente a ferramenta de insights de Segment para comparar esse Segment específico com qualquer outro que tenha configurado anteriormente. No entanto, observe que isso substituirá quaisquer Segments que você tenha selecionado anteriormente na ferramenta de insights de Segment.

{% alert note %}
Os [insights de Segment](#viewing-segment-insights) e a página **Detalhes do Segment** calculam estimativas de tamanho separadamente, usando amostras de usuários e tamanhos de amostra diferentes. Portanto, é esperado que os números possam não coincidir.
{% endalert %}

![Os insights de Segment também foram integrados diretamente à visualização de detalhes do Segment. Ao analisar um Segment específico que você configurou anteriormente, é possível encontrar as mesmas seis estatísticas descritas na caixa dinâmica e cinza de Estatísticas do Segment. A partir daqui, você pode iniciar rapidamente a ferramenta de insights de Segment para comparar esse Segment específico com qualquer outro que tenha configurado anteriormente. No entanto, observe que isso substituirá quaisquer Segments que você tenha selecionado anteriormente na ferramenta de insights de Segment.]({% image_buster /assets/img_archive/Segment_Segment_Insights.png %})

## Casos de uso {#insights-use-cases}

### Comparando padrões demográficos de uso e compra {#comparing-demographic-usage-and-purchasing-patterns}

Um dos melhores usos dos insights de Segment é responder perguntas sobre o impacto da demografia dos usuários no uso do app e na eficácia das campanhas, como:

- Determinados grupos demográficos de usuários estão tendo um desempenho significativamente melhor ou pior do que a média?
- Devo repensar a localização de uma campanha específica?
- Uma campanha está engajando um determinado grupo demográfico?
- Quais metas devo definir para uma campanha direcionada a um determinado grupo demográfico?

Os insights de Segment podem ajudar a revelar diferenças entre grupos demográficos de usuários. O exemplo a seguir mostra uma comparação da base de usuários de um app por idioma, ilustrando como falantes de inglês tendem a ter LTV e níveis de atividade mais altos do que falantes de outros idiomas.

![Detalhamento dos insights de Segment para segmentos de inglês, alemão, francês e espanhol.]({% image_buster /assets/img_archive/Segment_Language_Insights.png %})

Neste exemplo, os falantes de alemão se inscreveram há mais tempo em média, o que pode explicar por que não são mais tão ativos. Isso pode ser devido a vários fatores. Por exemplo, se o app foi lançado primeiro na Europa, mas agora é mais popular nos EUA, onde a maioria das pessoas fala inglês ou espanhol. Para resultados mais robustos, ao analisar KPIs entre grupos demográficos, é sensato testar as descobertas de um estudo geral de demografia (por exemplo, se o idioma impacta o LTV em todos os usuários) analisando uma população menor e mais semelhante para verificar se as descobertas persistem.

Para melhorar as conversões entre falantes de idiomas que não sejam inglês, um bom primeiro passo seria [localizar as campanhas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) para o idioma do dispositivo do usuário e garantir que o texto dessas mensagens esteja engajando os usuários usando uma [campanha multivariante]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) para testar diferentes versões do texto em idioma estrangeiro.

### Entendendo indicadores de maior receita {#understanding-indicators-of-higher-revenue}

Converter usuários em compradores pode ser difícil, e tentar empurrar usuários novos, inativos ou desengajados diretamente para a compra pode levar o usuário a desinstalar seu app. Os insights de Segment podem ajudar a descobrir ações que levam os usuários mais adiante no funil de compra sem exigir que eles comprem imediatamente, como assinar sua newsletter, compartilhar em redes sociais ou inscrever-se para mensagens promocionais. Por exemplo, você pode mapear o impacto nas compras de diferentes comportamentos dentro de um app de eCommerce.

![Detalhamento dos insights de Segment para usuários que compartilharam em redes sociais, se inscreveram para promoções e se inscreveram para newsletter.]({% image_buster /assets/img_archive/Segment_Insights_Events1.png %})

Neste caso, relativamente poucos usuários estão atualmente inscritos para mensagens promocionais e não são tão ativos, mas esses usuários geram uma receita vitalícia mais alta. Para aumentar a receita, pode ser uma boa ideia incluir um convite para se inscrever em mensagens promocionais nas campanhas de integração. Para reengajar usuários inativos, um bom plano seria enviar uma [campanha típica para usuários inativos]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/capturing_lapsing_users) e redirecionar [usuários que converteram]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#converted-from-campaign) com uma campanha subsequente para se inscrever em mensagens promocionais.