---
nav_title: Dados personalizados
article_title: Dados personalizados
page_order: 0
page_type: landing
description: "Os dados personalizados são a base da sua estratégia de engajamento na Braze. Saiba mais sobre atributos personalizados, eventos, catálogos, tipos de dados e como manter a integridade dos seus dados."
---

# Dados personalizados {#custom-data}

> Os dados personalizados são o combustível da sua estratégia de engajamento. Embora atributos padrão como nome e país já venham integrados, os dados personalizados permitem capturar detalhes únicos que definem o seu relacionamento com os clientes — desde o gênero de filme favorito até o momento exato em que concluíram uma compra.

Ao trazer essas informações para a Braze, você pode ir além de mensagens genéricas e criar experiências que pareçam pessoais, oportunas e relevantes. Você pode usar esses dados para criar segmentos precisos, personalizar o conteúdo das mensagens com Liquid e disparar jornadas automatizadas com base no comportamento em tempo real.

## Atributos e eventos {#attributes-and-events}

A decisão mais importante ao configurar seus dados é escolher entre um atributo e um evento.

### Atributos personalizados: quem são seus usuários {#custom-attributes-who-your-users-are}

Pense nos atributos personalizados como características ou propriedades persistentes dos seus usuários. Eles são ideais para armazenar informações que representam um estado atual ou que mudam com pouca frequência.

- **Caso de uso:** Você pode usar um atributo `loyalty_tier` para distinguir entre membros "Silver" e "Gold".
- **Personalização:** Atributos são perfeitos para personalização. Você pode inserir a `favorite_category` de um usuário na linha de assunto de um e-mail para chamar a atenção.
- **Armazenamento:** Esses dados permanecem no perfil do usuário indefinidamente, desde que o perfil continue ativo.

Para saber mais, consulte [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).

### Eventos personalizados: o que seus usuários fazem {#custom-events-what-your-users-do}

Eventos personalizados rastreiam ações específicas que seus usuários realizam em um determinado momento. São interações de alto valor que ajudam você a entender o "quando" e o "com que frequência" do comportamento dos usuários.

- **Caso de uso:** Quando um usuário conclui um cadastro, você pode registrar um evento `completed_registration`.
- **Gatilho:** Eventos são a principal forma de disparar a entrega baseada em ação. Você pode enviar uma notificação por push de "Boas-vindas" no momento em que o evento `completed_registration` é registrado.
- **Metadados:** Você pode adicionar detalhes extras a um evento usando propriedades de evento, como o nome do item adicionado ao carrinho.
- **Análise de dados:** Eventos alimentam a segmentação, relatórios e análise de dados para que você possa medir o engajamento e otimizar o envio de mensagens.

Para saber mais, consulte [Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events).

## Catálogos {#catalogs}

Enquanto atributos e eventos focam nos seus usuários, os catálogos permitem trazer dados que não são de usuários, como inventários de produtos, detalhes de cursos ou listagens de eventos.

Ao importar esses metadados via CSV ou API, você pode enriquecer suas mensagens com informações que não estão armazenadas no perfil do usuário. Por exemplo, você pode usar um catálogo para notificar automaticamente os clientes quando um item que eles visualizaram anteriormente voltou ao estoque ou teve uma queda de preço.

Para saber mais, consulte [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs).

## Tipos de dados {#data-types}

A Braze oferece suporte a vários tipos de dados para seus dados personalizados — incluindo booleano, número, string, array, data/hora e objeto — cada um com comportamentos e opções de segmentação específicos. O tipo de dado que você escolher afeta como você pode filtrar e personalizar em Campaigns e Segments.

Para uma referência completa dos tipos de dados compatíveis com atributos personalizados, propriedades de eventos e catálogos, consulte [Tipos de dados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types).

## Gerenciando a integridade dos seus dados {#managing-your-data-integrity}

A Braze oferece diversas ferramentas para ajudar você a gerenciar seus dados personalizados à medida que sua estratégia evolui.

### Detecção e alteração de tipos de dados {#data-type-detection-and-changes}

A Braze reconhece automaticamente o tipo de dado (como número ou string) do primeiro valor recebido para um atributo. Para manter a precisão, garanta que sua equipe envie tipos de dados consistentes em todos os seus ambientes. Se for necessário alterar um tipo de dado, tenha em mente que os dados existentes nos perfis de usuários não serão atualizados retroativamente, o que pode afetar seus segmentos.

### Lista de bloqueio e exclusão {#blocklist-and-delete}

Se você perceber que determinados atributos ou eventos não são mais úteis ou foram adicionados por engano, é possível removê-los do seu espaço de trabalho.

- **Lista de bloqueio:** Impede que a Braze colete novos dados para aquele objeto. Os dados deixam de aparecer em filtros ou gráficos, mas os dados existentes nos perfis são mantidos.
- **Excluir:** Remove permanentemente os dados de todos os perfis de usuários. É necessário manter o objeto na lista de bloqueio por 7 dias antes que ele se torne elegível para exclusão.

Para saber mais, consulte [Gerenciar dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data) e [Bloquear dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data).