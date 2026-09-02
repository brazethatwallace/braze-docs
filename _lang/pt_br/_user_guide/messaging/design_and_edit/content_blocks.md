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

> Os blocos de conteúdo permitem que você gerencie conteúdo reutilizável e multicanal em um único local centralizado. Use-os para criar uma aparência consistente em suas campanhas, distribuir os mesmos códigos de oferta por diferentes canais ou criar ativos predefinidos para envio de mensagens consistente em escala. Você também pode criar e gerenciar seus blocos de conteúdo [usando a API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/templates).

## Criar um bloco de conteúdo {#create-a-content-block}

Existem dois tipos de Content Blocks: arrastar e soltar e HTML. Cada tipo corresponde ao seu editor.

{% tabs %}
{% tab Arrastar e soltar %}

{% multi_lang_include messaging/create_content_block.md location="dnd" %}

{% alert important %}
Cada Content Block de arrastar e soltar é limitado a uma linha. No entanto, você pode usar blocos do editor de arrastar e soltar para criar e personalizar o Content Block de acordo com suas necessidades de envio de mensagens por e-mail.
{% endalert %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include messaging/create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### Especificações de Content Blocks {#content-block-specifications}

| Atributo do Content Block | Especificações |
|---|---|
| Nome | Campo obrigatório com no máximo 100 caracteres. Os nomes de Content Blocks podem conter apenas letras (A-Z), números (0-9), hifens (`-`) e underscores (`_`). Espaços e outros caracteres especiais não são permitidos e são convertidos automaticamente (por exemplo, espaços são substituídos por underscores). Os nomes não podem ser alterados após o Content Block ser salvo, e você não pode reutilizar o nome de um Content Block anterior, mesmo que arquivado. |
| Descrição | (opcional) No máximo 250 caracteres. Descreva o Content Block para que outros usuários da Braze saibam para que serve e onde é usado. |
| Tamanho do conteúdo | No máximo 50 KB. |
| Posicionamento | Content Blocks não podem ser usados em um rodapé de e-mail, mas você pode [criar um Content Block que inclua um rodapé](#email-footers) para uso nos seus e-mails. |
| Criação | Editor de HTML ou editor de arrastar e soltar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Especificações de Content Blocks" }

{% alert tip %}
Ao criar Content Blocks, pode ser útil visualizar HTML e Liquid adicionando quebras de linha. Se essas quebras de linha forem mantidas durante o envio, você corre o risco de ter espaços extras que podem afetar a renderização do bloco. Para evitar isso, use a tag **Capture** no seu bloco junto com o filtro **&#124; strip**.
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Usar Content Blocks {#use-content-blocks}

Depois de criar seu bloco de conteúdo, você pode inseri-lo nas suas mensagens usando o editor ou Liquid.

### Usando o editor de arrastar e soltar {#using-the-editor}

Para adicionar um bloco de conteúdo no editor de arrastar e soltar:

1. Acesse a guia **Rows** no editor e selecione **Content Blocks**.
2. Arraste e solte seu bloco de conteúdo no editor de e-mail.
3. (Opcional) Ajuste a largura do seu bloco de conteúdo selecionando o botão no menu de navegação. A largura padrão é 100% quando não especificada nas configurações globais de estilo do e-mail; caso contrário, as configurações globais serão respeitadas. <br><br>![Uma seta de duas pontas com a opção de editar a largura.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }<br><br>

{% alert note %}
Content Blocks adicionados por arrastar e soltar **não estão vinculados** ao bloco de conteúdo original. Para visualizar as alterações feitas no original, arraste-o novamente para o editor de e-mail.
{% endalert %}

Desalinhamentos no editor de arrastar e soltar podem ocorrer quando vários Content Blocks são adicionados a um único bloco de linha. Tente usar blocos de linha separados para manter o alinhamento do conteúdo no nível da linha.

### Usando Liquid {#using-liquid}

Para inserir um bloco de conteúdo usando Liquid:

1. Copie a **Content Block Liquid Tag** na seção **Content Block Details**.
2. Insira a Liquid tag do bloco de conteúdo na mensagem. Você também pode começar a digitar o Liquid e deixar a tag ser preenchida automaticamente.

No editor de arrastar e soltar, você também pode adicionar um bloco de conteúdo pelo painel de **Personalização**:

1. Acesse sua campanha de e-mail e selecione **Edit Email Body**.
2. Clique em <i class="fas fa-plus" aria-label="Adicionar personalização"></i> **Personalization**.
3. Selecione **Content Blocks** no menu suspenso **Personalization Type**.
4. Selecione o nome do seu bloco de conteúdo no campo **Attribute**.
5. Copie e cole o snippet Liquid em um bloco de editor de texto. <br>![A guia Adicionar Personalização com opções.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

{% alert important %}
Content Blocks inseridos via Liquid **estão vinculados** ao bloco de conteúdo original e refletirão quaisquer alterações feitas no modelo.
{% endalert %}

## Prévia de Content Blocks {#preview-content-blocks}

Depois de adicionar um Content Block em uma Campaign ou Canvas ativo, você pode visualizar a prévia a partir da biblioteca de Content Blocks passando o cursor sobre o Content Block e selecionando o ícone <i class="fa fa-eye prévia-icon"></i> **Prévia**.

Essa prévia inclui informações sobre o Content Block, como quem o criou, tags, data de criação, data da última edição, descrição, tipo de editor, contagem de inclusões com detalhes (uma lista clicável de mensagens ou Content Blocks que usam o Content Block) e uma prévia real do Content Block.

{% alert note %}
Ao auditar onde um Content Block está sendo usado, revise cada mensagem ou etapa vinculada individualmente para confirmar seu status.
{% endalert %}

## Aninhar Content Blocks {#nest-content-blocks}

Content Blocks podem ser aninhados, mas apenas uma vez. Você pode aninhar o Content Block A dentro do Content Block B, mas não pode aninhar o Content Block B dentro do Content Block C.

{% alert warning %}
Nada impede que você aninhe um terceiro nível de Content Block, mas o conteúdo não será expandido em aninhamentos além do segundo. O conteúdo e o snippet Liquid são removidos da mensagem.
{% endalert %}

Os links dentro de um Content Block aninhado contam para o total de links da mensagem principal. Se você usar um único Content Block com muitos links condicionais, como URLs específicas por país para localização, a mensagem principal pode acumular um grande número de links, o que pode tornar lento ou impedir o salvamento de um Canvas. Para localização em grande escala, [mensagens multilíngues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) são mais adequadas do que links condicionais em um único Content Block.

## Atualizar e copiar Content Blocks {#update-and-copy-content-blocks}

Se você optar por atualizar um Content Block, ele será atualizado em todas as mensagens onde foi inserido via Liquid. Se o Content Block for importado usando o menu suspenso **Content Blocks** em **Rows** no editor de arrastar e soltar, ele não será atualizado em todas as mensagens.

Se você quiser atualizar um Content Block para uma única mensagem ou fazer uma cópia para usar em outras mensagens, pode copiar o HTML da mensagem original para a nova ou editar o Content Block original (ele já deve ter sido usado em uma mensagem) e salvá-lo. Você receberá uma solicitação que permite salvá-lo como um novo Content Block.

Após fazer edições em um Content Block, você pode salvar e lançar o Content Block atualizado selecionando **Lançar Content Block**. Ou pode selecionar **Mais** > **Duplicar** para criar uma cópia do seu Content Block.

![Um Content Block que diz "Welcome to our newsletter".]({% image_buster /assets/img/copy-content-block.png %})

## Usar rodapés de e-mail em blocos de conteúdo {#email-footers}

Os blocos de conteúdo não podem ser usados em um rodapé de e-mail, mas você pode criar um bloco de conteúdo que inclua conteúdo de rodapé para uso em seus e-mails. Para fazer isso:

1. Acesse **Configurações** > **Preferências de e-mail** > **Rodapé personalizado** e crie o rodapé.
2. Adicione o rodapé a um bloco de conteúdo na **Biblioteca de blocos de conteúdo**.
3. Adicione esse bloco de conteúdo aos seus modelos de e-mail ou mensagens.

## Informações importantes {#things-to-know}

- Usar Content Blocks em HTML em e-mails de arrastar e soltar ou Content Blocks de arrastar e soltar em e-mails HTML pode resultar em problemas inesperados de renderização. Isso ocorre porque o editor de arrastar e soltar gera HTML e CSS que renderizam o conteúdo dinamicamente, enquanto o editor de HTML é mais estático.
- Se você inserir um Content Block de arrastar e soltar usando Liquid, a Braze não inclui os estilos do `<head>` HTML do bloco. Estilos responsivos, como CSS específico para dispositivos móveis, podem não ser renderizados conforme esperado. Se o bloco depende de CSS responsivo, adicione esse CSS à mensagem ou ao modelo que inclui o Content Block.
- As propriedades de entrada do Canvas são compatíveis apenas com Canvas. Se você fizer referência a um Content Block com propriedades de entrada do Canvas em uma Campaign, ele não será preenchido.
- Se uma mensagem com vários Content Blocks não estiver sendo renderizada conforme esperado, como quando tags Liquid ou HTML aparecem como texto visível em vez de serem processadas, uma tag não fechada ou outro erro em um dos Content Blocks geralmente é a causa. Para identificar a origem:
    1. Remova os Content Blocks da mensagem afetada um de cada vez.
    2. Verifique se a mensagem é renderizada corretamente após cada remoção.
    3. O último Content Block que você remover antes de o problema desaparecer é o que está causando o problema.
- As tags HTML `<code>` são renderizadas em fonte monoespaçada na maioria dos clientes de e-mail por padrão, independentemente de qualquer estilo de fonte definido no Content Block. Evite envolver texto em tags `<code>`, a menos que você queira essa aparência monoespaçada.
- Quando você insere um Content Block com Liquid em um modelo de e-mail HTML personalizado, as regras CSS no modelo pai podem substituir os estilos definidos dentro do Content Block. Para saber mais, consulte [Content Blocks em modelos HTML personalizados]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline#content-blocks-in-custom-html-templates).

## Arquivar Content Blocks {#archive-content-blocks}

![Menu suspenso de configurações expandido mostrando três opções: Arquivar, Duplicar e Copiar para o espaço de trabalho.]({% image_buster /assets/img/template_archive_cog.png %}){: style="max-width:20%;float:right;margin-left:15px;" }

Quando terminar de usar um Content Block, você pode arquivá-lo na página **Modelos**. Content Blocks arquivados são somente leitura, então desarquive o Content Block antes de editá-lo. Content Blocks não podem ser arquivados se estiverem sendo usados em alguma mensagem.

### Práticas recomendadas {#best-practices}

- Quando seu bloco é usado em poucos e-mails, recomendamos arquivar o bloco desatualizado e atualizar suas mensagens ativas com um bloco mais recente que não tenha sido arquivado.
- Quando seu bloco tem apenas um erro de digitação ou precisa de uma pequena alteração, não recomendamos arquivar o bloco. Em vez disso, atualize o bloco e continue enviando!
- Quando seu bloco é usado em mais mensagens do que você consegue gerenciar razoavelmente com a primeira sugestão desta lista, recomendamos remover todo o conteúdo do bloco. Isso evita a inclusão de informações desatualizadas em qualquer mensagem.
- Se você arquivar um Content Block acidentalmente, pode desarquivá-lo.

![Painel de Content Blocks salvos onde o menu suspenso de configurações de "Test_32" está expandido mostrando três opções: Desarquivar, Duplicar e Copiar para o espaço de trabalho]({% image_buster /assets/img/unarchive-content-block.png %})