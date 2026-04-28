---
nav_title: Gerenciar segments
article_title: Gerenciar segments
page_order: 2
page_type: tutorial
tool: Segments
description: "Este artigo aborda as ações que você pode realizar para gerenciar seus segments, como filtrar uma lista de segments, criar segments e editar segments."

---

# Gerenciar segments {#manage-segments}

> A seção Segments permite visualizar uma lista completa dos seus segments existentes, criar novos segments e editar segments existentes. Você pode refinar a lista de segments selecionando diversos filtros e colunas para que apenas as informações mais relevantes para você sejam exibidas.

![A seção Segments exibindo uma lista de segments ativos.]({% image_buster /assets/img/segment/segments_page.png %})

## Personalizando sua visualização {#customizing-your-view}

Personalize sua visualização da lista de segments usando filtros e alterando as colunas que deseja exibir. Quando você sair da seção **Segments** e retornar, a lista voltará à visualização padrão, removendo todos os filtros que você selecionou anteriormente.

### Filtro de status {#status-filter}

Você pode restringir a lista para exibir apenas segments ativos ou arquivados. Qualquer segment não arquivado é considerado ativo.

### Filtros {#filters}

Ordene os segments na lista ajustando os seguintes filtros:
- **Last Edited By:** O usuário que editou os segments por último
- **Last Edited:** Intervalo de tempo em que os segments foram editados pela última vez
- **Estimated Size:** Faixa aproximada de quantos usuários estão nos segments
- **Tags:** Tags associadas aos segments
- **Teams:** Equipes associadas aos segments
- **Advanced Tracking Segments Only:** Visualize apenas os segments que têm o [rastreamento de análise de dados]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/#segment-analytics-tracking) ativado.

### Colunas {#columns}

Estas são as colunas de informações que você pode selecionar para exibir na lista de segments:
- **Filters:** Número de filtros no segment
- **Last edited:** Data em que o segment foi editado pela última vez
- **Last edited by:** O usuário que editou o segment por último
- **Tags:** Tags associadas ao segment
- **Teams:** Equipes associadas ao segment
- **Estimated size:** Número estimado de usuários no segment
- **Canvases:** Número de Canvas que usam o segment
- **Campaigns:** Número de Campaigns que usam o segment

### Mostrar apenas favoritos {#show-starred-only}

Selecionar **Show Starred Only** restringe sua visualização aos segments que foram marcados como favoritos por você.

## Visualizando o uso de um segment em mensagens {#messaging-use}

Acesse a seção **Messaging Use** de um segment para ter uma visão geral de onde o segment está sendo usado, como em outros segments, Campaigns e Canvas.

{% alert note %}
Para evitar loops de segments referenciando uns aos outros, segments que usam o filtro **Segment Membership** não podem ser referenciados por outros segments. Para mais detalhes, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).
{% endalert %}

## Gerenciando segments específicos {#managing-specific-segments}

![O menu de edição de um segment mostrando as opções "Edit", "Duplicate", "Archive" e "Add to starred".]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Para gerenciar um segment específico, passe o cursor sobre ele e selecione o ícone de menu no final da linha para revelar as seguintes opções:
- **Edit:** Edite os filtros do seu segment.
- **Duplicate:** Faça uma cópia do seu segment.
- **Archive:** Arquive o segment. Observe que isso também arquivará quaisquer Campaigns ou Canvas que usem esse segment.
- **Add to starred:** Marque o segment como favorito, o que permite acessá-lo rapidamente marcando a caixa Show starred only na seção de segments.

Você também pode realizar ações em massa — especificamente, arquivamento em massa e adição de tags em massa — marcando as caixas ao lado de vários nomes de segments.

![Vários segments selecionados com "CRM" selecionado no campo dropdown "Tag As".]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### Alterações desde a última visualização {#changes-since-last-viewed}

O número de atualizações nos segments feitas por outros membros da sua equipe é rastreado pela métrica *Changes Since Last Viewed* na página de visão geral do segment. Selecione **Changes Since Last Viewed** para ver um changelog de atualizações no nome, descrição e público-alvo do segment. Para cada atualização, você pode ver quem realizou a atualização e quando. Você pode usar esse changelog para auditar alterações no seu segment.

## Pesquisando segments {#searching-for-segments}

Pesquise nomes de segments inserindo termos no campo de pesquisa.

Todos os termos e strings inseridos neste campo serão pesquisados. Por exemplo, pesquisar "test segment 1" retornará segments com "test", "segment" ou "1" em qualquer parte do nome. Para pesquisar uma string exata, coloque aspas ao redor do termo de pesquisa. Pesquisar ["test segment 1"] retornará todos os segments que contêm a frase exata "test segment 1" no nome.

![Os resultados da pesquisa ao inserir "all users" no campo de pesquisa incluem "All Users (Test)", "All Users", "All Users 15".]({% image_buster /assets/img/segment/segments_search.png %})

### Segments em Canvas {#segments-in-canvases}

Para pesquisar todas as referências de segments, incluindo aquelas em outros segments, Campaigns ou Canvas, acesse a seção [Uso em mensagens](#messaging-use) de um segment. O filtro **Target segment** na página do **Canvas** pesquisa apenas segments de público do Canvas.

![Filtro de Target segment na página do Canvas.]({% image_buster /assets/img/segment/target_segment.png %}){: style="max-width:45%;"}