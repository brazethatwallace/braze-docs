---
nav_title: Tags
article_title: Tags
page_order: 6
page_type: reference
description: "Este artigo de referência aborda tags para campanhas, Canvas, segmentos e dados personalizados no dashboard da Braze."
tool:
  - Campaigns
  - Canvas
---

# Tags {#tags}

> A Braze rastreia informações de autor, editor, data e status sobre segmentos, campanhas e Canvas, e oferece a capacidade de criar tags para organizar e classificar ainda mais seus engajamentos.

## Tags de Campaign, Canvas e segmento {#campaign-canvas-and-segment-tags}

Você pode adicionar tags ao criar ou editar uma campanha, um Canvas ou um segmento. Clique em <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tags** abaixo do nome do engajamento e selecione uma tag existente ou comece a digitar para adicionar uma nova tag.

![Adicionando tags durante a criação de uma campanha.]({% image_buster /assets/img_archive/tags_add_tag.png %}){: style="max-width:60%;" }

{% alert important %}
Você pode adicionar até 175 tags a uma campanha, um Canvas ou um segmento.
{% endalert %}

### Aplicação de tags em massa {#bulk-tagging}

Você também pode adicionar tags a várias campanhas, Canvas ou segmentos selecionando múltiplos engajamentos e clicando em <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tag As**.

![Adicionando tags a várias campanhas ao mesmo tempo.]({% image_buster /assets/img_archive/tags_apply_multiple.gif %})

{% alert important %}
Quando você usa a aplicação de tags em massa para adicionar uma nova tag a várias campanhas que já possuem tags diferentes, cada campanha selecionada recebe a nova tag, e todas as tags presentes em uma campanha são aplicadas a todas as outras campanhas selecionadas, mesmo que essas tags não estivessem originalmente associadas a elas.
{% endalert %}

### Visualizando tags {#viewing-tags}

As tags definidas em uma campanha, um Canvas ou um segmento ficam visíveis na página de detalhes, próximo ao nome do engajamento. Elas também aparecem na análise de dados da campanha.

![Tags exibidas na página de análise de dados da campanha.]({% image_buster /assets/img_archive/tag_details_page.png %}){: style="max-width:60%;" }

### Filtrando por tag {#filtering-by-tag}

As tags ficam visíveis na lista de campanhas, Canvas ou segmentos, junto com tags adicionais para rótulos de status como **Archived** e **Draft**. Para filtrar por uma tag, selecione o nome da tag na lista de tags.

![Tags na lista de campanhas.]({% image_buster /assets/img_archive/tags_grid.png %})

## Tags de dados personalizados {#custom-data-tags}

Tags também podem ser adicionadas a dados personalizados ao gerenciar [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#managing-custom-attributes) e [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events#adding-tags).

{% alert important %}
Esse recurso está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar desse acesso antecipado.
{% endalert %}

Para informações sobre como renomear, remover ou aninhar tags no seu dashboard, consulte [Gerenciamento de tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags).