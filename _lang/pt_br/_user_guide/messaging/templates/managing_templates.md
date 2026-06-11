---
nav_title: Gerenciar modelos
article_title: Gerenciar modelos
page_order: 1

page_type: reference
description: "Este artigo de referência descreve como duplicar e arquivar modelos na seção Modelos do dashboard da Braze."
tool:
  - Templates
  - Media

---

# Gerenciar modelos {#manage-templates}

> Arquivar ou duplicar modelos pode ajudar a organizá-los e gerenciá-los melhor. Este artigo de referência aborda como arquivar e duplicar modelos na seção **Modelos** do dashboard da Braze.

## Duplicando modelos {#duplicating-templates}

{% tabs %}
{% tab Modelo individual %}

![Menu suspenso com a opção de duplicar.]({% image_buster /assets/img/template_duplicate_cog.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Para duplicar um modelo individual, selecione <i class="fas fa-ellipsis-v"></i> **Mais opções** para o modelo e, em seguida, selecione **Duplicar** no menu suspenso.
<br><br>

{% alert note %}
Para modelos de [bloco de conteúdo]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/), uma cópia de rascunho é criada. Para todos os outros modelos, uma nova cópia duplicada é criada automaticamente.
{% endalert %}

{% endtab %}
{% tab Múltiplos modelos %}

{% raw %}

A duplicação de múltiplos modelos pode ser feita selecionando a caixa de seleção ao lado do nome do modelo. Primeiro, selecione os modelos e depois selecione **Duplicar**.

Os modelos duplicados podem ser encontrados ordenando a coluna **Última edição**. Por padrão, os novos modelos serão nomeados `Copy of ORIGINAL_TEMPLATE_NAME`.

{% endraw %}

![Três modelos ordenados pela última vez que foram editados, com um modelo copiado no topo da lista.]({% image_buster /assets/img/duplicate_multiple_template.gif %})

{% endtab %}
{% endtabs %}

## Arquivando modelos {#archiving-templates}

![Menu suspenso de configurações expandido que mostra três opções: "Arquivar", "Duplicar" e "Copiar para espaço de trabalho", com a opção "Arquivar" destacada.]({% image_buster /assets/img/template_archive_cog.png %}){: style="float:right;max-width:20%;margin-left:15px;"}

Para arquivar um modelo individual, selecione <i class="fas fa-ellipsis-v"></i> **Mais opções** na tela de grade de modelos e selecione **Arquivar**. Quando um modelo é arquivado, observe os seguintes cenários:

- Campaigns ativas continuam usando o modelo arquivado sem nenhuma interrupção.
- Campaigns em rascunho mantêm o conteúdo do modelo arquivado e podem ser editadas e lançadas.
- Para editar um modelo arquivado, você deve primeiro desarquivá-lo. Da mesma forma, para usar um modelo arquivado em uma Campaign, você deve primeiro desarquivar o modelo.

Para arquivar múltiplos modelos, selecione a caixa de seleção ao lado de cada modelo que deseja arquivar. Depois de selecionar múltiplos modelos, selecione **Arquivar**. Você pode encontrar seus modelos arquivados selecionando **Arquivado** em **Mostrar** na grade de modelos.

![Seção de modelos de e-mail de arrastar e soltar salvos que mostra dois modelos selecionados e uma barra de ferramentas com a opção de arquivar.]({% image_buster /assets/img/archive_multiple_template.png %}){: style="max-width:60%;"}

{% alert important %}
O arquivamento não está disponível atualmente para [modelos de link]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing/#link-templates).
{% endalert %}