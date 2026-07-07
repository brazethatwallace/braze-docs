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
**Os nomes são correspondências exatas.** As chaves de atributos personalizados são **sensíveis a maiúsculas e minúsculas** — por exemplo, `Home_City` e `home_city` são dois atributos diferentes. Quando você envia dados pela [REST API]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ou por um SDK, a Braze **remove espaços iniciais e finais** dos nomes de atributos, então `greeting` e ` greeting ` são resolvidos para a mesma chave. Use a mesma ortografia e capitalização em todos os lugares onde você referencia um atributo — em **Configurações de dados** > **Atributos personalizados**, cargas úteis de API e SDK e importações de CSV. Para saber como a Braze converte valores recebidos quando você [força um tipo de dados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data#data-type-coercion), consulte [Gerenciando dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data).
{% endalert %}

## Casos de uso {#use-cases}

Alguns casos de uso comuns de atributos personalizados incluem:

- Direcionamento e supressão de públicos por meio da segmentação de usuários com base em características como nível de fidelidade, status de inscrição, idioma preferido ou tipo de plano
- Personalização de mensagens com [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) referenciando atributos como o nome do usuário, pontos de recompensas ou categoria favorita
- Rastreamento de estágios do ciclo de vida e estados do usuário, como estágio de integração, status da conta ou data de término do período de teste
- Contagem de ações de baixo valor com [atributos numéricos]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#numbers), como incrementar um atributo `feature_views_count` cada vez que um usuário visualiza um recurso
- Registro de quando ações de baixo valor ocorreram pela última vez usando [atributos de tempo]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#time), como `last_support_ticket_at` ou `last_password_reset_at`
- Armazenamento de interesses e histórico do usuário como [arrays]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#arrays), como gêneros favoritos ou conteúdo visualizado recentemente, para direcionamento baseado em interesses
- Armazenamento de dados de perfil mais ricos como [objetos]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support) ou [vetores de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects), como preferências estruturadas ou múltiplos endereços salvos
- Disparo de mensagens baseadas em ação quando o valor de um atributo muda usando [gatilhos de atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers), como enviar uma notificação de upgrade de nível quando o `rewards_tier` de um usuário muda

## Gerenciar atributos personalizados {#managing-custom-attributes}

Para criar e gerenciar atributos personalizados no dashboard, acesse **Configurações de dados** > **Atributos personalizados**.

![Quatro atributos personalizados que são booleanos.]({% image_buster /assets/img/export_custom_attributes.png %})

A coluna **Última atualização** lista a última vez que o atributo personalizado foi editado, por exemplo, quando foi definido pela última vez como lista de bloqueio ou ativo.

{% alert important %}
Para o direcionamento adequado de mensagens, certifique-se de que o tipo de dados do seu atributo personalizado corresponda ao atributo personalizado real. <br><br>Por exemplo, se `newsletter_subscribed` for definido como uma string, sua sintaxe Liquid deve ser {% raw %}`{% if {{custom_attribute.${newsletter_subscribed}}} == 'true' %}`{% endraw %}. Se `newsletter_subscribed` for definido como booleano, a sintaxe Liquid não deve ter aspas simples: {% raw %}`{% if {{custom_attribute.${newsletter_subscribed}}} == true %}`{% endraw %}.
{% endalert %}

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

Você pode adicionar uma descrição a um atributo personalizado após sua criação, se tiver a [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) `Manage Events, Attributes, Purchases`. Selecione **Editar descrição** para o atributo personalizado e insira o que desejar, como uma nota para sua equipe.

### Adicionar tags {#add-tags}

Você pode adicionar tags a um atributo personalizado após sua criação, se tiver a [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) "Manage Events, Attributes, Purchases". As tags podem então ser usadas para filtrar a lista de atributos.

### Remover atributos personalizados {#remove-custom-attributes}

Existem duas maneiras de remover atributos personalizados dos perfis de usuário:

* Selecione o nome do atributo personalizado a ser removido em uma [etapa de Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#removing-custom-attributes).
* Defina o valor `null` na sua solicitação de API para o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track).

### Exportar dados {#export-data}

Para exportar a lista de atributos personalizados como um arquivo CSV, selecione **Exportar tudo** no topo da página. O arquivo CSV será gerado e um link para download será enviado por e-mail.

## Alterar o tipo de atributo personalizado {#change-custom-attribute-type}

### Pré-requisitos {#prerequisites}

O atributo personalizado não pode estar em uso em nenhuma campanha, Canvas ou segmento ativo. Se você tentar alterar o tipo de dados enquanto o atributo ainda estiver sendo referenciado, o dashboard exibirá um erro e bloqueará a alteração.

### Alterando o tipo de dados {#changing-the-data-type}

1. Interrompa quaisquer campanhas ou Canvas ativos que usem o atributo em segmentos ou filtros.
2. Remova o atributo de todos os filtros de segmento, campanha e Canvas.
3. Acesse **Configurações de dados** > **Atributos personalizados** (ou **Eventos personalizados**), encontre o atributo e atualize-o para o tipo de dados desejado.
4. Atualize os valores do atributo nos perfis de usuário existentes para corresponder ao novo tipo de dados (por exemplo, usando o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)).
5. Reaplique o atributo aos segmentos, campanhas e Canvas relevantes e reative quaisquer campanhas ou Canvas interrompidos.

### Informações importantes {#things-to-know}

- **Os dados de usuários não são atualizados retroativamente.** Se um perfil de usuário tinha o atributo com o tipo de dados antigo, esse valor permanece inalterado. O filtro de segmentação procura o novo tipo de dados, então usuários com o valor antigo são excluídos dos segmentos correspondentes até que seu perfil seja atualizado.
- **Novos dados devem corresponder ao novo tipo de dados.** Após a alteração, chamadas de API ou eventos do SDK que enviem o tipo de dados anterior para esse atributo não serão aceitos. Apenas valores que correspondam ao novo tipo de dados serão processados.
- **Os filtros não são atualizados automaticamente.** Segmentos e filtros de campanha que referenciam o atributo alterado não são atualizados retroativamente. Você deve removê-los e adicioná-los novamente após a alteração.

## Visualizar relatórios de uso {#view-usage-reports}

O relatório de uso lista todos os Canvas, campanhas e segmentos que usam um atributo personalizado específico. Esta lista não inclui usos de Liquid.

Você pode visualizar até 100 relatórios de uso por vez selecionando as caixas de seleção ao lado dos respectivos atributos personalizados e depois selecionando **Visualizar relatório de uso**.

### Guia Valores {#values-tab}

Ao visualizar um relatório de uso, selecione a guia **Valores** para ver os principais valores dos atributos personalizados selecionados com base em uma amostra de aproximadamente 250.000 usuários. Como os resultados são amostrados de um subconjunto de usuários, a amostra não incluirá todos os valores existentes. Isso significa que a guia **Valores** não deve ser usada para solução de problemas ou para casos de uso que exijam a incorporação de dados de todos os usuários.

![Relatório de uso para atributos personalizados selecionados com a guia "Valores" aberta mostrando um gráfico de pizza dos valores do atributo de país, como "US" e "PR".]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## Definir atributos personalizados {#set-custom-attributes}

A seguir estão listados os métodos em várias plataformas usados para definir atributos personalizados.

{% details Expandir para documentação por plataforma %}

- [Android e FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=unity)
- [.NET MAUI (anteriormente Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)

{% enddetails %}

## Armazenamento de atributos personalizados {#custom-attribute-storage}

Todos os dados armazenados no **Perfil de usuário**, incluindo dados de atributos personalizados, são retidos indefinidamente enquanto cada perfil estiver [ativo]({{site.baseurl}}/user_archival#active-users).

Para uma referência completa de todos os tipos de dados que podem ser armazenados como atributos personalizados — incluindo booleanos, números, strings, arrays, tempo, objetos e vetores de objetos — consulte [Tipos de dados de atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types).

### Strings vazias versus valores nulos {#blank-strings-versus-null-values}

Ao limpar ou remover um atributo personalizado, o comportamento difere dependendo de você passar uma string vazia (`""`) ou `null`:

| Valor | Comportamento |
| --- | --- |
| `""` (string vazia) | O atributo é definido como um valor vazio e permanece visível no perfil de usuário. |
| `null` | O atributo é removido completamente do perfil de usuário. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings vazias versus valores nulos" }
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings vazias versus valores nulos" }
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings vazias versus valores nulos" }

{% alert important %}
Para tipos de dados que não são string, em que o tipo de dados é definido manualmente no dashboard da Braze (não detectado automaticamente), você deve usar `null` para remover o valor. Passar `""` é válido apenas para atributos do tipo string — por exemplo, definir um atributo booleano como `""` é tratado como uma string vazia, que é um valor inválido para esse tipo. Para remover um booleano, passe `null`.

Observe que a importação de CSV não suporta `null` — valores booleanos em importações de CSV devem ser `TRUE` ou `FALSE`.
{% endalert %}