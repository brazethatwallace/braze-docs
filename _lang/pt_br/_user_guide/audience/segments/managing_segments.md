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

Adapte sua visualização da lista de Segments usando filtros e alterando as colunas que deseja exibir. Quando você sair da seção **Segments** e retornar, a lista voltará à visualização padrão, removendo quaisquer filtros que você tenha selecionado anteriormente.

### Filtro de status {#status-filter}

Você pode restringir a lista para exibir apenas Segments ativos ou arquivados. Qualquer Segment não arquivado é considerado ativo.

### Filtros {#filters}

Filtre os Segments na lista ajustando os seguintes filtros:
- **Last Edited By:** O usuário que editou os Segments por último
- **Last Edited:** Intervalo de tempo em que os Segments foram editados pela última vez
- **Estimated Size:** Intervalo aproximado de quantos usuários estão nos Segments
- **Tags:** Tags associadas aos Segments
- **Teams:** Equipes associadas aos Segments
- **Advanced Tracking Segments Only:** Visualize apenas os Segments que têm o [rastreamento de análise de dados]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) ativado.

### Colunas {#columns}

Estas são as colunas de informação que você pode selecionar para exibir na lista de Segments:
- **Filters:** Número de filtros no Segment
- **Last edited:** Data em que o Segment foi editado pela última vez
- **Last edited by:** O usuário que editou o Segment por último
- **Tags:** Tags associadas ao Segment
- **Teams:** Equipes associadas ao Segment
- **Estimated size:** Número estimado de usuários no Segment
- **Canvases:** Número de Canvas que usam o Segment
- **Campaigns:** Número de Campaigns que usam o Segment

### Exibir apenas favoritos {#show-starred-only}

Selecionar **Show Starred Only** restringe sua visualização aos Segments que foram marcados como favoritos por você.

## Visualizando o uso de um segmento em mensagens {#messaging-use}

Acesse a seção **Messaging Use** de um segmento para ter uma visão geral de onde o segmento está sendo usado, como em outros segmentos, Campaigns e Canvas.

{% alert note %}
Para evitar loops de segmentos referenciando uns aos outros, segmentos que usam o filtro **Segment Membership** não podem ser referenciados por outros segmentos. Para mais detalhes, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).
{% endalert %}

## Gerenciando segments específicos {#managing-specific-segments}

![O menu de edição de um segment mostrando as opções "Edit", "Duplicate", "Archive" e "Add to starred".]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Para gerenciar um segment específico, passe o cursor sobre ele e selecione o ícone de menu no final da linha para revelar as seguintes opções:
- **Edit:** Edite os filtros do seu segment.
- **Duplicate:** Crie uma cópia do seu segment.
- **Archive:** Arquive o segment. Isso também arquivará quaisquer Campaigns ou Canvas que usem esse segment.
- **Add to starred:** Marque o segment com estrela, o que permite acessá-lo rapidamente marcando a caixa "Show starred only" na seção de segments.

Você também pode realizar ações em massa — especificamente, arquivamento em massa e adição de tags em massa — marcando as caixas de seleção ao lado de vários nomes de segments.

{% alert tip %}
Se você precisar de uma exportação legível por máquina dos segments existentes no espaço de trabalho (não apenas a visualização atual da tabela), use o [endpoint Exportar lista de segments]({{site.baseurl}}/api/endpoints/export/segments/get_segment) e pagine pelos resultados. Para auditar segments arquivados, revise-os separadamente no dashboard de **Segments** usando o filtro de status.
{% endalert %}

![Vários segments selecionados com "CRM" selecionado no campo dropdown "Tag As".]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### Alterações desde a última visualização {#changes-since-last-viewed}

O número de atualizações nos segments feitas por outros membros da sua equipe é rastreado pela métrica *Alterações desde a última visualização* na página de visão geral do segment. Selecione **Changes Since Last Viewed** para visualizar um changelog de atualizações no nome, descrição e público-alvo do segment. Para cada atualização, você pode ver quem realizou a alteração e quando. Você pode usar esse changelog para auditar alterações no seu segment.

## Pesquisando Segments {#searching-for-segments}

Pesquise nomes de Segments inserindo termos no campo de pesquisa.

Todos os termos e strings inseridos nesse campo serão pesquisados. Por exemplo, ao pesquisar "test segment 1", serão retornados Segments que contenham "test", "segment" ou "1" em qualquer parte do nome. Para pesquisar uma string exata, coloque aspas ao redor do termo de pesquisa. Pesquisar ["test segment 1"] retornará todos os Segments que contenham a frase exata "test segment 1" no nome.

![Os resultados da pesquisa ao inserir "all users" no campo de pesquisa incluem "All Users (Test)", "All Users" e "All Users 15".]({% image_buster /assets/img/segment/segments_search.png %})

### Segments em Canvas {#segments-in-canvases}

Para pesquisar todas as referências de Segments, incluindo aquelas em outros Segments, Campaigns ou Canvas, acesse a seção [Uso em mensagens](#messaging-use) de um Segment. O filtro **Target segment** na página **Canvas** pesquisa apenas Segments de público do Canvas.

![Filtro Target segment na página Canvas.]({% image_buster /assets/img/segment/target_segment.png %}){: style="max-width:45%;"}

## Solução de problemas {#troubleshooting}

{% multi_lang_include audience/segments.md section='Canvas variant archived segment' %}