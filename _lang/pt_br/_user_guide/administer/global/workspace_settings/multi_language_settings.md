---
nav_title: Configurações de localização
article_title: Configurações de localização
alias: "/multi_language_support/"
page_order: 4
description: "Este artigo fornece uma visão geral das configurações multilíngues no dashboard da Braze e como usar localidades no seu envio de mensagens."
---

# Configurações de localização {#localization-settings}

> O recurso multilíngue permite que você use [tags de tradução]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) para direcionar usuários em diferentes idiomas e locais, tudo dentro de uma única mensagem.

## Pré-requisitos {#prerequisites}

{% multi_lang_include locales.md section='multi-language prerequisites' %}

## Adicionar uma localidade {#add-a-locale}

1. Acesse **Configurações** > **Configurações de localização**.
2. Selecione **Add locale** e, em seguida, selecione **Default locale** ou **Custom Attributes**.

![O menu suspenso "Add locale" com opções para selecionar a localidade padrão ou atributos personalizados.]({% image_buster /assets/img/multi-language_support/add_locale_options.png %}){: style="max-width:40%;"}

{: start="3"}
3. Digite um nome para a localidade.
4. [Selecione um idioma para acessibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/#language-settings-and-accessibility). Essa configuração permite que tecnologias assistivas, como leitores de tela, pronunciem o texto corretamente.
5. Selecione os respectivos atributos do usuário para a opção de localidade escolhida. Ao configurar uma localidade, você pode selecionar idiomas nos atributos padrão do usuário ou nos atributos personalizados. Não é possível selecionar de ambos.

{% tabs %}
{% tab Default locale %}

Para **Default locale**, use os menus suspensos para selecionar o idioma a ser adicionado e, opcionalmente, o país a ser associado ao idioma.

![Uma janela chamada "Add locale - Default Language and Country" para especificar o idioma e o país.]({% image_buster /assets/img/multi-language_support/default_option.png %})

{% endtab %}
{% tab Custom attributes %}

Para **Custom Attributes**, use o menu suspenso para selecionar o atributo personalizado associado e, no campo de texto, insira o valor.

![Uma janela chamada "Add locale - Custom Attributes" para especificar o atributo personalizado e o valor.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %})

{% endtab %}
{% endtabs %}

{: start="6"}
6. Selecione **Add locale**.

Para saber como usar essas localidades nas suas mensagens, consulte [Usando localidades]({{site.baseurl}}/locales_in_messages/).

## Considerações {#considerations}

- Você pode selecionar até dois atributos personalizados em uma única localidade, ou até dois idiomas de atributos padrão do usuário. Em ambos os casos, o segundo atributo é opcional.
- Ao editar os valores traduzidos no arquivo CSV, evite modificar quaisquer valores padrão no arquivo.
- A chave da localidade no arquivo enviado deve corresponder à chave nas suas configurações multilíngues.

### Suporte e priorização {#support-and-prioritization}

- Se um usuário corresponder tanto a uma localidade definida por atributos personalizados quanto a uma definida por atributos padrão do usuário, a localidade de atributo personalizado terá prioridade.
- Atributos personalizados suportam valores de texto (string) com correspondência exata.
- Se um atributo personalizado for excluído ou seu tipo for alterado, o usuário não poderá mais se enquadrar nessa localidade e seguirá pela lista de prioridade de localidades em que se encaixa ou receberá as traduções de marketing padrão.
- Se uma localidade for inválida (o atributo personalizado foi alterado ou excluído), o erro aparecerá na página **Multi-Language Support**.

## Perguntas frequentes {#frequently-asked-questions}

#### Quantas localidades posso adicionar? {#how-many-locales-can-i-add}

Você pode adicionar até 200 localidades.

#### Onde os arquivos de tradução são armazenados na Braze? {#where-are-the-translation-files-stored-in-braze}

Os arquivos de tradução são armazenados no nível da Campaign, o que significa que cada variante de mensagem deve ter traduções enviadas. As traduções também podem ser armazenadas em Content Blocks. Quando o bloco é adicionado a uma mensagem, suas traduções são incluídas automaticamente.

#### O nome da localidade precisa seguir um padrão ou formato específico? {#does-the-locale-name-have-to-follow-a-specific-pattern-or-format}

Não. Você pode usar a convenção de nomenclatura que preferir. O nome da localidade é usado ao selecionar a localidade no editor e aparecerá nos cabeçalhos do arquivo que você baixar com os IDs de tradução.