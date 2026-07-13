---
nav_title: Gerenciar segmentos
article_title: Gerenciar segmentos
page_order: 2
page_type: tutorial
tool: Segments
description: "Este artigo aborda as ações que você pode realizar para gerenciar seus segmentos, como filtrar uma lista de segmentos, criar segmentos e editar segmentos."

---

# Gerenciar segmentos {#manage-segments}

> A seção Segments permite visualizar uma lista completa dos seus segmentos existentes, criar novos segmentos e editar segmentos existentes. Você pode refinar a lista de segmentos selecionando diversos filtros e colunas para que apenas as informações mais relevantes para você sejam exibidas.

![A seção Segments exibindo uma lista de segmentos ativos.]({% image_buster /assets/img/segment/segments_page.png %})

## Personalizando sua visualização {#customizing-your-view}

Personalize sua visualização da lista de segmentos usando filtros e alterando as colunas que deseja exibir. Quando você sair da seção **Segments** e retornar, a lista voltará à visualização padrão, removendo todos os filtros que você selecionou anteriormente.

### Filtro de status {#status-filter}

Você pode restringir a lista para exibir apenas segmentos ativos ou arquivados. Qualquer segmento não arquivado é considerado ativo.

### Filtros {#filters}

Ordene os segmentos na lista ajustando os seguintes filtros:
- **Last Edited By:** O usuário que editou os segmentos por último
- **Last Edited:** Intervalo de tempo em que os segmentos foram editados pela última vez
- **Estimated Size:** Faixa aproximada de quantos usuários estão nos segmentos
- **Tags:** Tags associadas aos segmentos
- **Teams:** Equipes associadas aos segmentos
- **Advanced Tracking Segments Only:** Visualize apenas os segmentos que têm o [rastreamento de análise de dados]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) ativado.

### Colunas {#columns}

Estas são as colunas de informações que você pode selecionar para exibir na lista de segmentos:
- **Filters:** Número de filtros no segmento
- **Last edited:** Data em que o segmento foi editado pela última vez
- **Last edited by:** O usuário que editou o segmento por último
- **Tags:** Tags associadas ao segmento
- **Teams:** Equipes associadas ao segmento
- **Estimated size:** Número estimado de usuários no segmento
- **Canvases:** Número de Canvas que usam o segmento
- **Campaigns:** Número de Campaigns que usam o segmento

### Mostrar apenas favoritos {#show-starred-only}

Selecionar **Show Starred Only** restringe sua visualização aos segmentos que foram marcados como favoritos por você.

## Visualizando o uso de um segmento em mensagens {#messaging-use}

Acesse a seção **Messaging Use** de um segmento para ter uma visão geral de onde o segmento está sendo usado, como em outros segmentos, Campaigns e Canvas.

{% alert note %}
Para evitar loops de segmentos referenciando uns aos outros, segmentos que usam o filtro **Segment Membership** não podem ser referenciados por outros segmentos. Para mais detalhes, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).
{% endalert %}

## Gerenciando segmentos específicos {#managing-specific-segments}

![O menu de edição de um segmento mostrando as opções "Edit", "Duplicate", "Archive" e "Add to starred".]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Para gerenciar um segmento específico, passe o cursor sobre ele e selecione o ícone de menu no final da linha para revelar as seguintes opções:
- **Edit:** Edite os filtros do seu segmento.
- **Duplicate:** Faça uma cópia do seu segmento.
- **Archive:** Arquive o segmento. Observe que isso também arquivará quaisquer Campaigns ou Canvas que usem esse segmento.
- **Add to starred:** Marque o segmento como favorito, o que permite acessá-lo rapidamente marcando a caixa Show starred only na seção de segmentos.

Você também pode realizar ações em massa — especificamente, arquivamento em massa e adição de tags em massa — marcando as caixas ao lado de vários nomes de segmentos.

{% alert tip %}
Se você precisar de uma exportação legível por máquina dos segmentos existentes no espaço de trabalho (não apenas da visualização atual da tabela), use o [endpoint Exportar lista de segmentos]({{site.baseurl}}/api/endpoints/export/segments/get_segment) e pagine pelos resultados. Para auditar segmentos arquivados, revise-os separadamente no dashboard **Segments** usando o filtro de status.
{% endalert %}

![Vários segmentos selecionados com "CRM" selecionado no campo dropdown "Tag As".]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### Alterações desde a última visualização {#changes-since-last-viewed}

O número de atualizações nos segmentos feitas por outros membros da sua equipe é rastreado pela métrica *Changes Since Last Viewed* na página de visão geral do segmento. Selecione **Changes Since Last Viewed** para ver um changelog de atualizações no nome, na descrição e no público-alvo do segmento. Para cada atualização, você pode ver quem a realizou e quando. Você pode usar esse changelog para auditar alterações no seu segmento.

## Pesquisando segmentos {#searching-for-segments}

Pesquise nomes de segmentos inserindo termos no campo de pesquisa.

Todos os termos e strings inseridos neste campo serão pesquisados. Por exemplo, pesquisar "test segment 1" retornará segmentos com "test", "segment" ou "1" em qualquer parte do nome. Para pesquisar uma string exata, coloque aspas ao redor do termo de pesquisa. Pesquisar ["test segment 1"] retornará todos os segmentos que contêm a frase exata "test segment 1" no nome.

![Os resultados da pesquisa ao inserir "all users" no campo de pesquisa incluem "All Users (Test)", "All Users", "All Users 15".]({% image_buster /assets/img/segment/segments_search.png %})

### Segmentos em Canvas {#segments-in-canvases}

Para pesquisar todas as referências de segmentos, incluindo aquelas em outros segmentos, Campaigns ou Canvas, acesse a seção [Uso em mensagens](#messaging-use) de um segmento. O filtro **Target segment** na página do **Canvas** pesquisa apenas segmentos de público do Canvas.

![Filtro de Target segment na página do Canvas.]({% image_buster /assets/img/segment/target_segment.png %}){: style="max-width:45%;"}