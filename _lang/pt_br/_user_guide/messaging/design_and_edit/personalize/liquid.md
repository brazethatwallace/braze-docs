---
nav_title: Referência de Liquid
article_title: Referência de Liquid
page_order: 3
layout: dev_guide
alias: /liquid/
search_rank: 3
guide_top_header: "Referência de Liquid"
guide_top_text: "Liquid é uma linguagem de modelo de código aberto criada pela Shopify e usada pela Braze para possibilitar a personalização dinâmica. Em vez de enviar uma mensagem estática para todos, o Liquid permite criar modelos que alteram seu conteúdo com base nos dados de perfil, comportamento ou idioma de cada destinatário."
description: "Esta landing page abrange tudo sobre Liquid, como tags de personalização compatíveis, filtros, definição de valores padrão e muito mais."

guide_featured_title: "Artigos da seção"
guide_featured_list:
- name: Usar Liquid
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid
  image: /assets/img/braze_icons/beaker-02.svg
- name: Tags de personalização compatíveis
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags
  image: /assets/img/braze_icons/tag-01.svg
- name: Operadores
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/operators
  image: /assets/img/braze_icons/code-02.svg
- name: Filtros
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/filters
  image: /assets/img/braze_icons/flag-02.svg
- name: Filtros avançados
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters
  image: /assets/img/braze_icons/settings-01.svg
- name: Definir valores padrão
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values
  image: /assets/img/braze_icons/table.svg
- name: Lógica condicional de mensagens
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic
  image: /assets/img/braze_icons/columns-01.svg
- name: Cancelar mensagens
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Casos de uso de Liquid
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases
  image: /assets/img/braze_icons/list.svg
- name: Tutoriais
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/tutorials
  image: /assets/img/braze_icons/book-open-01.svg
- name: Perguntas frequentes
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/faq
  image: /assets/img/braze_icons/annotation-question.svg

---

## Sobre o Liquid {#about-liquid}

O Liquid funciona como uma ponte entre sua mensagem e os dados dos seus usuários. Quando você envia uma mensagem, a Braze analisa o texto em busca de sintaxe Liquid. Ao encontrá-la, ela busca os dados relevantes daquele usuário específico e substitui o código pelo valor real antes de a mensagem ser enviada.

Por exemplo, você pode recuperar um atributo personalizado de um perfil de usuário que seja do tipo inteiro e arredondar esse valor para o número inteiro mais próximo. Para saber mais sobre a sintaxe e o uso do Liquid, consulte [**Tags de personalização compatíveis**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

A linguagem de modelo Liquid suporta o uso de objetos, tags e filtros.

- [**Objetos**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) permitem inserir atributos personalizados nas suas mensagens.
- [**Tags**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/) permitem inserir dados nas mensagens e usar lógica condicional para enviar mensagens quando determinadas condições são atendidas. Por exemplo, você pode usar tags para incluir lógica inteligente, como instruções "if", nas suas campanhas.
- [**Filtros**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters/) permitem reformatar atributos personalizados e conteúdo dinâmico. Por exemplo, você pode usar o [filtro `date`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters/#date-filter) para converter um timestamp, como *2016-09-07 08:43:50 UTC*, em uma data, como *7 de setembro de 2016*.

{% alert warning %}
Atualmente, a Braze não oferece suporte a 100% do Liquid da Shopify, apenas a determinadas partes que tentamos descrever em nossa documentação. Recomendamos fortemente testar todas as mensagens que usam Liquid antes de enviá-las, para reduzir o risco de erros ou de uso de Liquid não compatível.
{% endalert %}

### Suporte ao Liquid 5 {#liquid-5-support}

A Braze oferece suporte ao Liquid até e incluindo o **Liquid 5 da Shopify**. A implementação do Liquid suporta tipos de tags de personalização de sintaxe e controle de espaços em branco. Para saber mais sobre tags específicas, consulte [tags de sintaxe]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/#syntax-tags).

Os seguintes filtros novos de array e matemáticos estão disponíveis para uso no seu Liquid ao criar suas mensagens.
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

Consulte [Filtros]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters/) para ver as definições.

## Termos importantes {#terms-to-know}

Estes termos são reinterpretados a partir da [**documentação da Shopify**](https://shopify.github.io/liquid/basics/introduction/) com base no nosso nível de suporte.

{% raw %}

| Termo | Definição | Exemplo |
|---|---|---|
| Liquid | Uma linguagem de modelo voltada ao cliente, amplamente utilizada, criada pela Shopify e escrita em Ruby, usada para carregar e exibir conteúdo dinâmico. | `{{${first_name}}}` insere o nome do usuário em uma mensagem. |
| Objeto | Uma indicação de variável e localização do nome da variável pretendida que diz ao Liquid onde exibir o conteúdo na mensagem. | `{{${city}}}` insere a cidade do usuário em uma mensagem. |
| Tag de lógica condicional | Usada para criar lógica e controlar o fluxo do conteúdo da mensagem. Na Braze, as tags de lógica condicional são usadas para criar exceções e variações nas mensagens com base em determinados critérios predefinidos. | ```{% if ${language} == 'en' %}``` acionará sua mensagem de uma forma específica caso o usuário tenha definido "Inglês" como idioma. |
| Filtros | Usados para alterar, restringir ou reformatar a saída do objeto Liquid. Frequentemente utilizados para criar operações matemáticas. | ```{{"Big Sale" | upcase}}``` fará com que as palavras "Big Sale" apareçam como "BIG SALE" na mensagem. |
| Operadores | Usados nas mensagens para criar dependências ou critérios que podem afetar qual mensagem o usuário recebe. | Se um usuário atender aos critérios definidos em uma mensagem marcada com `{% custom_attribute.${Total_Revenue} > 0%}`, ele receberá a mensagem. Caso contrário, receberá outra mensagem designada (ou não), dependendo do que você configurou. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Termos importantes" }

{% endraw %}

<br>