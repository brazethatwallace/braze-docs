---
nav_title: Insights de segmento
article_title: Insights de segmento
page_order: 6
page_type: tutorial
tool:
  - Segments
  - Reports
description: "Este artigo de instruções mostra como usar, interpretar e compartilhar os Insights de segmento."
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Insights de segmento {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsegmentation-course-stylefloatrightwidth120pxborder0-classnoimgbordersegment-insights}

> Saiba como usar, interpretar e compartilhar os Insights de segmento.

Os Insights de segmento mostram o desempenho de um segmento em comparação com outro em um conjunto de KPIs pré-selecionados.

## Visualizando os Insights de segmento {#viewing-segment-insights}

Acesse a página **Insights de segmento** do seu dashboard, em **Analytics**, para visualizar até 10 segmentos diferentes comparados a uma linha de base.

![Dashboard de Insights de segmento comparando três segmentos, "UK Users", "FR Users" e "CA Users" com um segmento de linha de base, "Todos os usuários".]({% image_buster /assets/img_archive/segment_insights.png %})

O segmento de linha de base pode ser um segmento específico que você selecionar ou um segmento contendo todos os seus usuários. Você pode comparar as seguintes estatísticas usando os Insights de segmento:

| Medida | Descrição | Fórmula |
| --------------------- | ------------- | ------------- |
| Sessões por dia | Número médio de sessões por dia dos usuários do segmento | (total de sessões) / (nº de dias desde a primeira sessão) |
| Dias desde a primeira sessão | Número médio de dias entre a primeira sessão dos usuários do segmento e agora | hoje – data da primeira sessão |
| Dias desde a última sessão | Número médio de dias entre a última sessão dos usuários do segmento e agora | hoje – data da última sessão |
| Lifetime Revenue em dólares | Lifetime Revenue médio em dólares para os usuários do segmento | gasto total do usuário |
| Dias desde a primeira compra | Número médio de dias entre a primeira sessão e a primeira compra dos usuários do segmento | data da primeira compra – data da primeira sessão |
| Dias desde a última compra | Número médio de dias entre a última compra dos usuários do segmento e agora | hoje – data da última compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Viewing Segment Insights" }

Você pode compartilhar facilmente comparações específicas com seus colegas usando a URL exclusiva da página, e também pode selecionar o ícone de olho ao lado de cada segmento para ver mais informações sobre ele. Essas comparações serão redefinidas quando você alternar entre espaços de trabalho.

![Informações do segmento "Premium Users (iOS VideoApp)" com um gráfico exibindo o histórico de membros e um quadro que detalha o tamanho estimado para vários canais de envio de mensagens.]({% image_buster /assets/img_archive/Segment_Insights_Info.png %}){: style="max-width:50%;"}

## Página de informações do segmento {#segment-details-page}

Os Insights de segmento também foram integrados diretamente à visualização **Segment Details**. Ao analisar um segmento específico que você configurou anteriormente, você encontrará as mesmas seis estatísticas descritas na caixa dinâmica e cinza de estatísticas do segmento. A partir daqui, você pode iniciar rapidamente a ferramenta de Insights de segmento para comparar esse segmento específico com qualquer outro que você tenha configurado anteriormente, mas observe que isso substituirá quaisquer segmentos que você tenha selecionado anteriormente na ferramenta de Insights de segmento.

![]({% image_buster /assets/img_archive/Segment_Segment_Insights.png %})

## Casos de uso {#insights-use-cases}

### Comparando padrões demográficos de uso e compra {#comparing-demographic-usage-and-purchasing-patterns}

Um dos melhores usos dos Insights de segmento é responder perguntas sobre o impacto da demografia dos usuários no uso do app e na eficácia das campanhas, como:

- Determinados grupos demográficos de usuários estão tendo um desempenho significativamente melhor ou pior do que a média?
- Devo repensar a localização de uma campanha específica?
- Uma campanha está engajando um determinado grupo demográfico?
- Quais metas devo definir para uma campanha direcionada a um determinado grupo demográfico?

Os Insights de segmento podem ajudar a revelar diferenças entre grupos demográficos de usuários. O exemplo a seguir mostra uma comparação da base de usuários de um app por idioma, ilustrando como falantes de inglês tendem a ter LTV e níveis de atividade mais altos do que falantes de outros idiomas.

![Detalhamento dos Insights de segmento para segmentos de inglês, alemão, francês e espanhol.]({% image_buster /assets/img_archive/Segment_Language_Insights.png %})

Neste exemplo, os falantes de alemão se inscreveram há mais tempo em média, o que pode explicar por que não são mais tão ativos. Isso pode ser devido a vários fatores. Por exemplo, se o app foi lançado primeiro na Europa, mas agora é mais popular nos EUA, onde a maioria das pessoas fala inglês ou espanhol. Para resultados mais robustos, ao analisar KPIs entre grupos demográficos, é sensato testar as descobertas de um estudo geral de demografia (por exemplo, se o idioma impacta o LTV em todos os usuários) analisando uma população menor e mais semelhante para verificar se as descobertas persistem.

Para melhorar as conversões entre falantes de idiomas que não sejam inglês, um bom primeiro passo seria [localizar as campanhas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/) para o idioma do dispositivo do usuário e garantir que o texto dessas mensagens esteja engajando os usuários usando uma [campanha multivariante]({{site.baseurl}}/user_guide/messaging/ab_testing/#creating-tests) para testar diferentes versões do texto em idioma estrangeiro.

### Entendendo indicadores de maior receita {#understanding-indicators-of-higher-revenue}

Converter usuários em compradores pode ser difícil, e tentar empurrar usuários novos, inativos ou desengajados diretamente para a compra pode levar o usuário a desinstalar seu app. Os Insights de segmento podem ajudar a descobrir ações que levam os usuários mais adiante no funil de compra sem exigir que eles comprem imediatamente, como assinar sua newsletter, compartilhar em redes sociais ou inscrever-se para mensagens promocionais. Por exemplo, você pode mapear o impacto nas compras de diferentes comportamentos dentro de um app de eCommerce.

![Detalhamento dos Insights de segmento para usuários que compartilharam em redes sociais, se inscreveram para promoções e se inscreveram para newsletter.]({% image_buster /assets/img_archive/Segment_Insights_Events1.png %})

Neste caso, relativamente poucos usuários estão atualmente inscritos para mensagens promocionais e não são tão ativos, mas esses usuários geram um Lifetime Revenue mais alto. Para aumentar a receita, pode ser uma boa ideia incluir um convite para se inscrever em mensagens promocionais nas campanhas de integração. Para reengajar usuários inativos, um bom plano seria enviar uma [campanha típica para usuários inativos]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/capturing_lapsing_users/#capture-lapsing-users) e direcionar [usuários que converteram]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns/#converted-from-campaign-filter) com uma campanha subsequente para se inscrever em mensagens promocionais.