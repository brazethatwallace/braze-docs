---
nav_title: Atributos personalizados
article_title: Atributos personalizados
page_order: 1
page_type: reference
description: "Esta página descreve os atributos personalizados e explica os vários tipos de dados de atributos personalizados."
search_rank: 1
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Atributos personalizados {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-attributes}

> Esta página aborda os atributos personalizados, que são uma coleção de características exclusivas dos seus usuários. Atributos personalizados são ideais para armazenar informações sobre seus usuários ou sobre ações de baixo valor dentro do seu app.

Quando armazenados na Braze, os atributos personalizados podem ser usados para criar segmentos de público e personalizar o envio de mensagens usando Liquid. Lembre-se de que a Braze não armazena informações de séries temporais para atributos personalizados, portanto, você não poderá gerar gráficos com base neles, como é possível para eventos personalizados.

{% alert important %}
**Os nomes são correspondências exatas.** As chaves de atributos personalizados são **sensíveis a maiúsculas e minúsculas** — por exemplo, `Home_City` e `home_city` são dois atributos diferentes. Quando você envia dados pela [REST API]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ou por um SDK, a Braze **remove espaços iniciais e finais** dos nomes de atributos, então `greeting` e ` greeting ` são resolvidos para a mesma chave. Use a mesma ortografia e capitalização em todos os lugares onde você referencia um atributo — em **Data Settings** > **Custom Attributes**, cargas úteis de API e SDK e importações de CSV. Para saber como a Braze converte valores recebidos quando você [força um tipo de dados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data#data-type-coercion), consulte [Gerenciando dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data).
{% endalert %}

## Casos de uso {#use-cases}

Alguns casos de uso comuns de atributos personalizados incluem:

- Direcionar e suprimir públicos segmentando usuários com base em características como nível de fidelidade, status de inscrição, idioma preferido ou tipo de plano
- Personalizar mensagens com [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) referenciando atributos como o nome do usuário, pontos de recompensas ou categoria favorita
- Rastrear estágios do ciclo de vida e estados do usuário, como estágio de integração, status da conta ou data de término do período de teste
- Contar ações de baixo valor com [atributos numéricos]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types), como incrementar um atributo `feature_views_count` cada vez que um usuário visualiza um recurso
- Registrar quando ações de baixo valor ocorreram pela última vez usando [atributos de tempo]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types), como `last_support_ticket_at` ou `last_password_reset_at`
- Armazenar interesses e histórico do usuário como [arrays]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types), como gêneros favoritos ou conteúdo visualizado recentemente, para direcionamento baseado em interesses
- Armazenar dados de perfil mais detalhados como [objetos]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support) ou [arrays de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects), como preferências estruturadas ou múltiplos endereços salvos
- Disparar mensagens baseadas em ação quando o valor de um atributo muda usando [gatilhos de atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers), como enviar uma notificação de upgrade de nível quando o `rewards_tier` de um usuário muda

## Gerenciar atributos personalizados {#managing-custom-attributes}

Para criar e gerenciar atributos personalizados no dashboard, acesse **Data Settings** > **Custom Attributes**.

![Quatro atributos personalizados que são booleanos.]({% image_buster /assets/img/export_custom_attributes.png %})

A coluna **Last updated** lista a última vez que o atributo personalizado foi editado, por exemplo, quando foi definido pela última vez como lista de bloqueio ou ativo.

{% alert note %}
Se um atributo personalizado de array aparecer em um perfil de usuário sem valores, verifique se o **Max Length** do atributo é maior que `0`. Para solução de problemas passo a passo, consulte [Tipos de dados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#arrays).
{% endalert %}

{% alert important %}
Para o direcionamento adequado de mensagens, certifique-se de que o tipo de dados do seu atributo personalizado corresponda ao atributo personalizado real. <br><br>Por exemplo, se `newsletter_subscribed` for definido como uma string, sua sintaxe Liquid deve ser {% raw %}`{% if {{custom_attribute.${newsletter_subscribed}}} == 'true' %}`{% endraw %}. Se `newsletter_subscribed` for definido como booleano, a sintaxe Liquid não deve ter aspas simples: {% raw %}`{% if {{custom_attribute.${newsletter_subscribed}}} == true %}`{% endraw %}.
{% endalert %}

### Solução de problemas com atributos personalizados ou eventos duplicados {#troubleshooting-duplicate-custom-attributes-or-events}

{% multi_lang_include data_activation/troubleshooting_duplicate_custom_data_entries.md %}

Nesta página, você pode visualizar, gerenciar, criar ou bloquear atributos personalizados existentes. Selecione o menu ao lado de um atributo personalizado para as seguintes ações:

### Lista de bloqueio {#blocklisting}

Você pode bloquear atributos personalizados individuais pelo menu de ações, ou selecionar e bloquear até 100 atributos em massa.

Quando você bloqueia um atributo personalizado:

- Dados futuros não serão coletados para esse atributo.
- Os dados existentes não estarão disponíveis, a menos que o atributo seja desbloqueado.
- Esse atributo não aparecerá em filtros ou gráficos.

Além disso, se um atributo personalizado bloqueado estiver sendo referenciado por filtros ou gatilhos em outras áreas da Braze, um modal de aviso aparecerá explicando que todas as instâncias dos filtros ou gatilhos que o referenciam serão removidas e arquivadas.

Para mais detalhes sobre bloqueio e exclusão de dados personalizados, consulte [Bloquear dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data).

### Marcar como informação de identificação pessoal (IPI) {#mark-as-personally-identifiable-information-pii}

Administradores também podem criar atributos personalizados e marcá-los como IPI nesta página. Esses atributos são visíveis apenas para administradores e usuários do dashboard com a permissão "View Custom Attributes Marked as PII".

### Adicionar descrições {#add-descriptions}

Você pode adicionar uma descrição a um atributo personalizado após sua criação, se tiver a [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) `Manage Events, Attributes, Purchases`. Selecione **Edit description** para o atributo personalizado e insira o que desejar, como uma nota para sua equipe.

### Adicionar tags {#add-tags}

Você pode adicionar tags a um atributo personalizado após sua criação, se tiver a [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) "Manage Events, Attributes, Purchases". As tags podem então ser usadas para filtrar a lista de atributos.

### Remover atributos personalizados {#remove-custom-attributes}

Existem duas maneiras de remover atributos personalizados dos perfis de usuário:

* Selecione o nome do atributo personalizado a ser removido em uma [etapa de Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#removing-custom-attributes).
* Defina o valor `null` na sua solicitação de API para o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

### Exportar dados {#export-data}

Para exportar a lista de atributos personalizados como um arquivo CSV, selecione **Export all** no topo da página. O arquivo CSV será gerado e um link para download será enviado por e-mail.

## Alterar o tipo de atributo personalizado {#change-custom-attribute-type}

### Pré-requisitos {#prerequisites}

O atributo personalizado não pode estar em uso em nenhuma Campaign, Canvas ou Segment ativo. Se você tentar alterar o tipo de dados enquanto o atributo ainda estiver referenciado, o dashboard exibirá um erro e bloqueará a alteração.

### Alterando o tipo de dados {#changing-the-data-type}

1. Interrompa quaisquer Campaigns ou Canvas ativos que usem o atributo em Segments ou filtros.
2. Remova o atributo de todos os filtros de Segment, Campaign e Canvas.
3. Acesse **Configurações de dados** > **Atributos personalizados** (ou **Eventos personalizados**), encontre o atributo e atualize-o para o tipo de dados desejado.
4. Atualize os valores do atributo nos perfis de usuário existentes para corresponder ao novo tipo de dados (por exemplo, usando o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)).
5. Reaplique o atributo aos Segments, Campaigns e Canvas relevantes e, em seguida, reative quaisquer Campaigns ou Canvas interrompidos.

### O que você precisa saber {#things-to-know}

- **Os dados de usuários não são atualizados retroativamente.** Se um perfil de usuário tinha o atributo com o tipo de dados antigo, esse valor permanece inalterado. O filtro de segmentação procura o novo tipo de dados, então os usuários com o valor antigo são excluídos dos Segments correspondentes até que o perfil seja atualizado.
- **Os novos dados devem corresponder ao novo tipo de dados.** Após a alteração, chamadas de API ou eventos do SDK que enviem o tipo de dados anterior para esse atributo não serão aceitos. Somente valores que correspondam ao novo tipo de dados serão ingeridos.
- **Os filtros não são atualizados automaticamente.** Segments e filtros de Campaign que fazem referência ao atributo alterado não são atualizados retroativamente. Você deve removê-los e adicioná-los novamente após a alteração.

## Visualizar relatórios de uso {#view-usage-reports}

O relatório de uso lista todos os Canvas, Campaigns e Segments que utilizam um atributo personalizado específico. Essa lista não inclui usos de Liquid.

Você pode visualizar até 100 relatórios de uso por vez, selecionando as caixas de seleção ao lado dos respectivos atributos personalizados e, em seguida, selecionando **Visualizar relatório de uso**.

### Guia Valores {#values-tab}

Ao visualizar um relatório de uso, selecione a guia **Valores** para ver os principais valores dos atributos personalizados selecionados com base em uma amostra de aproximadamente 250.000 usuários. Como os resultados são amostrados a partir de um subconjunto de usuários, a amostra não incluirá todos os valores existentes. Isso significa que a guia **Valores** não deve ser usada para solução de problemas ou para casos de uso que exigem a incorporação de dados de todos os usuários.

![Relatório de uso para atributos personalizados selecionados com a guia "Valores" aberta, mostrando um gráfico de pizza com valores do atributo de país, como "US" e "PR".]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## Definir atributos personalizados {#set-custom-attributes}

A seguir estão os métodos em várias plataformas usados para definir atributos personalizados.

{% details Expandir para ver a documentação por plataforma %}

- [Android e FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=unity)
- [.NET MAUI (anteriormente Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)

{% enddetails %}

## Armazenamento de atributos personalizados {#custom-attribute-storage}

Todos os dados armazenados no **Perfil de Usuário**, incluindo dados de atributos personalizados, são retidos indefinidamente enquanto cada perfil estiver <a href="/docs/user_archival#active-users">ativo</a>.

Para uma referência completa de todos os tipos de dados que você pode armazenar como atributos personalizados — incluindo booleanos, números, strings, arrays, tempo, objetos e arrays de objetos — consulte [Tipos de dados de atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types).

### Strings em branco versus valores nulos {#blank-strings-versus-null-values}

Ao limpar ou remover um atributo personalizado, o comportamento difere dependendo de você passar uma string em branco (`""`) ou `null`:

| Valor | Comportamento |
| --- | --- |
| `""` (string em branco) | O atributo é definido como um valor vazio e permanece visível no perfil de usuário. |
| `null` | O atributo é removido completamente do perfil de usuário. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings em branco versus valores nulos" }
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings em branco versus valores nulos" }
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings em branco versus valores nulos" }

Esse comportamento também afeta a segmentação. Para atributos personalizados, o filtro **IS NOT BLANK** verifica se há um valor não vazio. Isso significa que uma string em branco (`""`) não corresponde, mesmo que o atributo permaneça visível no perfil. Um valor `null` também não corresponde, porque o atributo é removido do perfil.

{% alert important %}
Para tipos de dados que não são string, em que o tipo de dados é definido manualmente no dashboard da Braze (não detectado automaticamente), você deve usar `null` para remover o valor. Passar `""` é válido apenas para atributos do tipo string — por exemplo, definir um atributo booleano como `""` é tratado como uma string vazia, que é um valor inválido para esse tipo. Para remover um booleano, passe `null`.

Note que a importação de CSV não oferece suporte a `null` — valores booleanos em importações de CSV devem ser `TRUE` ou `FALSE`.
{% endalert %}