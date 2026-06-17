---
nav_title: Blocos de conteúdo
article_title: Blocos de conteúdo
alias: "/dnd/content_blocks/"
page_order: 4
description: "Saiba como criar, usar e gerenciar blocos de conteúdo reutilizáveis em suas campanhas e Canvas na Braze."
page_type: reference
tool:
  - Templates
  - Media

---

# Blocos de conteúdo {#content-blocks}

> Os blocos de conteúdo permitem que você gerencie conteúdo reutilizável e multicanal em um único local centralizado. Use-os para criar uma aparência consistente em suas campanhas, distribuir os mesmos códigos de oferta por diferentes canais ou criar ativos predefinidos para envio de mensagens consistente em escala. Você também pode criar e gerenciar seus blocos de conteúdo [usando a API]({{site.baseurl}}/api/endpoints/templates/).

## Criar um bloco de conteúdo {#create-a-content-block}

Existem dois tipos de blocos de conteúdo: arrastar e soltar e HTML. Cada tipo corresponde ao seu editor.

{% tabs %}
{% tab Arrastar e soltar %}

{% multi_lang_include create_content_block.md location="dnd" %}

{% alert important %}
Cada bloco de conteúdo de arrastar e soltar é limitado a uma linha. No entanto, você pode usar blocos do editor de arrastar e soltar para criar e personalizar o bloco de conteúdo de acordo com o seu envio de mensagens por e-mail.
{% endalert %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### Especificações dos blocos de conteúdo {#content-block-specifications}

| Atributo do bloco de conteúdo | Especificações |
|---|---|
| Nome | Campo obrigatório com no máximo 100 caracteres. Não pode ser renomeado após o bloco de conteúdo ter sido salvo. Além disso, você não pode dar a um novo bloco de conteúdo o mesmo nome de um bloco anterior, mesmo que o anterior tenha sido arquivado. |
| Descrição | (opcional) No máximo 250 caracteres. Descreva o bloco de conteúdo para que outros usuários da Braze saibam para que serve e onde é usado. |
| Tamanho do conteúdo | No máximo 50 KB. |
| Posicionamento | Os blocos de conteúdo não podem ser usados em um rodapé de e-mail, mas você pode [criar um bloco de conteúdo que inclua um rodapé](#email-footers) para uso em seus e-mails. |
| Criação | Editor de HTML ou editor de arrastar e soltar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Especificações dos blocos de conteúdo" }

{% alert tip %}
Ao criar blocos de conteúdo, pode ser útil visualizar HTML e Liquid adicionando quebras de linha. Se essas quebras de linha forem mantidas durante o envio, você corre o risco de ter espaços extras que podem afetar a renderização do bloco. Para evitar isso, use a tag **Capture** no seu bloco junto com o filtro **&#124; strip**.
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Usar blocos de conteúdo {#use-content-blocks}

Após criar seu bloco de conteúdo, você pode inseri-lo em suas mensagens usando o editor ou Liquid.

### Usando o editor de arrastar e soltar {#using-the-editor}

Para adicionar um bloco de conteúdo no editor de arrastar e soltar:

1. Acesse a guia **Rows** no editor e selecione **Content Blocks**.
2. Arraste e solte seu bloco de conteúdo no editor de e-mail.
3. (Opcional) Ajuste a largura do seu bloco de conteúdo selecionando o botão no menu de navegação. A largura padrão é 100% quando não especificada nas configurações globais de estilo do e-mail; caso contrário, as configurações globais serão respeitadas. <br><br>![Uma seta de dois lados com a opção de editar a largura.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }<br><br>

{% alert note %}
Os blocos de conteúdo adicionados por arrastar e soltar **não estão vinculados** ao bloco de conteúdo original. Para visualizar as alterações feitas no original, arraste-o novamente para o editor de e-mail.
{% endalert %}

Desalinhamentos no editor de arrastar e soltar podem ocorrer quando vários blocos de conteúdo são adicionados a um único bloco de linha. Tente usar blocos de linha separados para manter o alinhamento do conteúdo no nível da linha.

### Usando Liquid {#using-liquid}

Para inserir um bloco de conteúdo usando Liquid:

1. Copie a **Content Block Liquid Tag** na seção **Content Block Details**.
2. Insira a Liquid tag do bloco de conteúdo na mensagem. Você também pode começar a digitar o Liquid e a tag será preenchida automaticamente.

No editor de arrastar e soltar, você também pode adicionar um bloco de conteúdo pelo painel de **Personalization**:

1. Acesse sua campanha de e-mail e selecione **Edit Email Body**.
2. Clique em <i class="fas fa-plus"></i> **Personalization**.
3. Selecione **Content Blocks** no menu suspenso **Personalization Type**.
4. Selecione o nome do seu bloco de conteúdo no campo **Attribute**.
5. Copie e cole o trecho Liquid em um bloco de texto do editor. <br>![A guia Adicionar personalização com opções.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

{% alert important %}
Os blocos de conteúdo inseridos via Liquid **estão vinculados** ao bloco de conteúdo original e refletirão quaisquer alterações no modelo.
{% endalert %}

### Informações importantes {#things-to-know}

- Usar blocos de conteúdo HTML em e-mails de arrastar e soltar **ou** blocos de conteúdo de arrastar e soltar em e-mails HTML pode resultar em problemas inesperados de renderização. Isso ocorre porque o editor de arrastar e soltar gera HTML e CSS que renderizam o conteúdo dinamicamente, enquanto o editor de HTML é mais estático.
- Se você inserir um bloco de conteúdo de arrastar e soltar usando Liquid, a Braze não inclui os estilos do `<head>` do HTML do bloco. Estilos responsivos, como CSS específico para dispositivos móveis, podem não ser renderizados como esperado. Se o bloco depende de CSS responsivo, adicione esse CSS à mensagem ou ao modelo que inclui o bloco de conteúdo.
- As propriedades de eventos do Canvas são suportadas apenas em um Canvas. Se você referenciar um bloco de conteúdo com propriedades de entrada do Canvas em uma Campaign, ele não será preenchido.

## Pré-visualizar blocos de conteúdo {#preview-content-blocks}

Após adicionar um bloco de conteúdo em uma Campaign ou Canvas ativo, você pode pré-visualizá-lo na Biblioteca de blocos de conteúdo passando o cursor sobre o bloco de conteúdo e selecionando o ícone <i class="fa fa-eye preview-icon"></i> **Pré-visualização**.

Essa pré-visualização inclui informações sobre o bloco de conteúdo, como quem o criou, tags, data de criação, data da última edição, descrição, tipo de editor, contagem de inclusões com detalhes (uma lista clicável de mensagens ou blocos de conteúdo que usam o bloco de conteúdo) e uma pré-visualização real do bloco de conteúdo.


## Aninhar blocos de conteúdo {#nest-content-blocks}

Os blocos de conteúdo podem ser aninhados, mas apenas uma vez. Você pode aninhar o bloco de conteúdo A no bloco de conteúdo B, mas não poderá aninhar o bloco de conteúdo B no bloco de conteúdo C.

{% alert warning %}
Nada impedirá que você aninhe um terceiro nível de bloco de conteúdo, mas o conteúdo não será expandido em aninhamentos além do segundo nível. O conteúdo e o trecho Liquid serão removidos da mensagem.
{% endalert %}

## Atualizar e copiar blocos de conteúdo {#update-and-copy-content-blocks}

Se você optar por atualizar um bloco de conteúdo, ele será atualizado em todas as mensagens onde foi inserido via Liquid. Se o bloco de conteúdo foi importado usando o menu suspenso **Content Blocks** em **Rows** no editor de arrastar e soltar, ele não será atualizado em todas as mensagens.

Se você quiser atualizar um bloco de conteúdo para uma única mensagem ou fazer uma cópia para usar em outras mensagens, pode copiar o HTML da mensagem original para a nova ou editar o bloco de conteúdo original (ele já deve ter sido usado em uma mensagem) e salvá-lo. Você receberá uma solicitação que permite salvá-lo como um novo bloco de conteúdo.

Após fazer edições em um bloco de conteúdo, você pode salvar e lançar o bloco de conteúdo atualizado selecionando **Launch Content Block**. Ou você pode selecionar **More** > **Duplicate** para criar uma cópia do seu bloco de conteúdo.

![Um bloco de conteúdo que diz "Welcome to our newsletter".]({% image_buster /assets/img/copy-content-block.png %})

## Usar rodapés de e-mail em blocos de conteúdo {#email-footers}

Os blocos de conteúdo não podem ser usados em um rodapé de e-mail, mas você pode criar um bloco de conteúdo que inclua conteúdo de rodapé para uso em seus e-mails. Para fazer isso:

1. Acesse **Settings** > **Email Preferences** > **Custom Footer** e crie o rodapé.
2. Adicione o rodapé a um bloco de conteúdo na **Biblioteca de blocos de conteúdo**.
3. Adicione esse bloco de conteúdo aos seus modelos de e-mail ou mensagens.

## Arquivar blocos de conteúdo {#archive-content-blocks}

![Menu suspenso de configurações expandido mostrando três opções: Arquivar, Duplicar e Copiar para espaço de trabalho.]({% image_buster /assets/img/template_archive_cog.png %}){: style="max-width:20%;float:right;margin-left:15px;" }

Quando terminar de usar um bloco de conteúdo, você pode arquivá-lo na página **Modelos**. Blocos de conteúdo arquivados são somente leitura, então desarquive o bloco de conteúdo antes de editá-lo. Blocos de conteúdo não podem ser arquivados se estiverem sendo usados em alguma mensagem.

### Práticas recomendadas {#best-practices}

- Quando seu bloco é usado em poucos e-mails, recomendamos arquivar o bloco desatualizado e atualizar suas mensagens ativas com um bloco mais recente que não tenha sido arquivado.
- Quando seu bloco tem apenas um erro de digitação ou precisa de uma pequena alteração, não recomendamos arquivar o bloco. Em vez disso, atualize o bloco e continue enviando!
- Quando seu bloco é usado em mais mensagens do que você pode gerenciar razoavelmente com a primeira sugestão desta lista, recomendamos remover todo o conteúdo do bloco. Isso evita a inclusão de informações desatualizadas em qualquer mensagem.
- Se você arquivar acidentalmente um bloco de conteúdo, pode desarquivá-lo.

![Painel de blocos de conteúdo salvos onde o menu suspenso de configurações de "Test_32" está expandido mostrando três opções: Desarquivar, Duplicar e Copiar para espaço de trabalho]({% image_buster /assets/img/unarchive-content-block.png %})