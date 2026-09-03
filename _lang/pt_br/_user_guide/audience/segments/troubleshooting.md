---
nav_title: Solução de problemas
article_title: Solução de problemas de Segments
page_order: 9
page_type: reference
tool:
  - Segments
description: "Este artigo de referência aborda a solução de problemas para erros de Segments, elegibilidade de usuários, problemas com filtros e divergências na análise de dados. Para definições de filtros, consulte Filtros de segmentação. Para estimativas de tamanho de Segments e contagens exatas, consulte Medir o tamanho do Segment."
---

# Solução de problemas de Segments {#troubleshoot-segments}

> Encontre seu sintoma na lista abaixo para ir à seção correta. Esta página aborda erros de lançamento, elegibilidade de usuários, problemas com filtros e divergências na análise de dados. Para definições de filtros, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters). Para estimativas de tamanho de Segments, contagens exatas e gráficos de histórico de membros, consulte [Medir o tamanho do Segment]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

## Comece aqui: identifique seu sintoma {#start-here-match-your-symptom}

| Sintoma | Acesse |
|---------|-------|
| O público é muito complexo | [O público-alvo é muito complexo para lançar](#target-audience-is-too-complex-to-launch) |
| O filtro não salva | [O filtro excede 10.000 bytes](#filter-exceeds-10000-bytes-or-is-too-long-to-save) |
| O Segment não tem usuários | [O Segment mostra zero usuários](#segment-shows-zero-users) |
| O usuário não está no Segment | [Caminho de investigação padrão](#standard-investigation-path) |
| O Segment é maior do que o esperado | [O Segment é muito maior do que o esperado](#segment-is-much-larger-than-expected) |
| A contagem do Segment não corresponde à análise de dados da Campaign | [Divergência em *Mensagens enviadas* ou *Destinatários únicos*](#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count) |
| As opções de filtro mudaram | [As opções de filtro mudaram](#filter-options-changed) |
| Atributo personalizado aninhado não disponível como filtro | [Atributo personalizado aninhado não disponível como opção de filtro](#nested-custom-attribute-not-available-as-a-filter-option) |
| O usuário está no app errado | [Informações exibidas para usuários de outros apps](#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app) |
| Um usuário estava neste Segment em um momento passado? | [Associação retroativa ao Segment](#retroactive-segment-membership) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comece aqui: identifique seu sintoma" }

## Caminho de investigação padrão {#standard-investigation-path}

Use este fluxo de trabalho quando um usuário deveria estar em um Segment mas não está, ou quando a contagem de um Segment parece incorreta.

1. **Lançamento bloqueado:** Se você vir um erro de complexidade de público ou de filtro de 10.000 bytes em uma Campaign ou Canvas, comece por [Erros](#errors) (solução alternativa com CSV, simplificação de filtros).
2. **Prévia do usuário ou busca de usuário:** Teste um usuário específico em relação aos filtros do seu Segment. Quando um usuário não corresponde a parte ou a todos os critérios, os critérios ausentes são listados para solução de problemas. Para ver as etapas, consulte [Testando Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments) em Criar um Segment.
3. **Calcular estatísticas exatas:** Se a estimativa do Segment mostrar 0 usuários ou parecer incorreta, selecione **Calcular estatísticas exatas** no painel **Usuários contatáveis**. Salve seu Segment antes de calcular. Se um cálculo já estiver em andamento, aguarde a conclusão; números desatualizados podem ser exibidos até que o novo cálculo seja concluído. Para saber mais, consulte [Calculando estatísticas exatas]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#calculating-exact-statistics).
4. **Verificar valores dos filtros:** Procure erros de digitação, incompatibilidades de tipo de dados, referências desatualizadas de etapas do Canvas e [lógica de filtro negativo + OR](#segment-is-much-larger-than-expected).
5. **Verificar complexidade:** Se o lançamento estiver bloqueado, consulte [O público-alvo é complexo demais para lançamento](#target-audience-is-too-complex-to-launch).
6. **Entrar em contato com o suporte:** Se você ainda estiver bloqueado, entre em contato com o [suporte da Braze]({{site.baseurl}}/braze_support).

## Segment mostra zero usuários {#segment-shows-zero-users}

O tamanho do Segment no dashboard geralmente é uma estimativa baseada em uma amostra de usuários. Segments muito pequenos podem exibir um intervalo estimado que inclui 0, mesmo quando há usuários que correspondem aos seus filtros.

- Selecione **Calculate exact stats** no painel **Usuários contatáveis** para obter uma contagem precisa. Salve o Segment primeiro. Para saber mais, consulte [Considerações sobre contagens estimadas]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#considerations-for-estimate-counts).
- Se a **Prévia de usuário** retornar zero usuários para um Segment pequeno, isso não significa necessariamente que o Segment está vazio. Execute **Calculate exact stats** para confirmar. Para saber mais, consulte [Prévia de usuário]({{site.baseurl}}/user_guide/audience/segments/segment_data#user-preview).

## Associação retroativa a Segments {#retroactive-segment-membership}

A Braze não armazena o histórico de associação a Segments por usuário. Não é possível verificar se um usuário específico estava em um Segment em um momento passado de envio.

Para capturar a associação em um determinado momento, exporte os usuários do Segment no dashboard ou chame o endpoint [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) antes de enviar uma Campaign ou Canvas. Para saber mais, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) (filtro de associação a Segment) e [Exportar dados de Segment para CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv).

## Erros {#errors}

### O público-alvo é complexo demais para ser lançado {#target-audience-is-too-complex-to-launch}

Esse erro raro ocorre quando o público-alvo contém muitos valores de regex, valores de regex excessivamente longos, filtros excessivamente detalhados (como "é qualquer um de 30.000 CEPs") ou filtros demais. Isso inclui todos os filtros no público de uma Campaign ou Canvas, independentemente de os filtros estarem dentro dos Segments referenciados ou adicionados como filtros na etapa **Target Audience**.

![Erro para um público-alvo que atinge o limite de complexidade.]({% image_buster /assets/img/segment/target_audience_too_complex_error.png %})

Quando você adiciona filtros de Segment a uma Campaign ou Canvas, esses filtros são traduzidos em consultas na Braze (a contagem de caracteres dessas consultas não é 1:1 em relação ao número de caracteres que o usuário do dashboard vê). Quando a Braze envia uma Campaign ou Canvas, executamos uma consulta que combina todos os filtros do público-alvo. Aplicamos um limite ao número de caracteres na consulta resultante para um público-alvo. Para uma determinada Campaign ou Canvas, somamos a contagem de caracteres de todos os Segments referenciados, incluindo todos os filtros adicionais. Para um determinado Segment, somamos a contagem de caracteres de todos os filtros e valores de filtro.

O dashboard exibirá um erro quando uma Campaign, Canvas ou Segment exceder o limite e não puder ser lançado. Se você receber esse erro, simplifique o público-alvo antes de lançar novamente, incluindo:

- Se o público referencia múltiplos Segments, verifique se os Segments não possuem redundâncias, como os mesmos filtros aparecendo em múltiplos Segments.
- Verifique se você não está referenciando dados desatualizados nos filtros de Segment. Por exemplo, um filtro desatualizado pode procurar usuários que não receberam uma determinada etapa do Canvas na última semana, mesmo que o Canvas tenha sido interrompido há meses.
- Segments que são apenas listas de IDs de usuários ou e-mails (que frequentemente usam um filtro de regex) podem ser convertidos em uma [importação de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) e simplificados em um único filtro baseado em CSV.
- Se você usa CDI, pode ser possível criar um Segment CDI que extrai o grupo diretamente do seu data warehouse.

Você também pode [entrar em contato com o suporte]({{site.baseurl}}/braze_support) para obter assistência adicional com a otimização de filtros.

{% alert note %}
Começamos a limitar a contagem de caracteres em abril de 2025. Campaigns e Canvas lançados antes de abril de 2025 foram isentos, o que significa que podem continuar excedendo o limite, enquanto Campaigns e Canvas recém-criados não podem exceder o limite. Se você editar ou clonar uma Campaign ou Canvas isento, não será possível lançá-lo até que o público seja atualizado para ficar abaixo do limite.
{% endalert %}

### X Campaigns ou Canvas ativos ou parados excedem o limite de complexidade do público {#x-active-or-stopped-campaigns-or-canvases-exceed-the-audience-complexity-threshold}

Esse banner é exibido no topo de uma lista de Campaigns ou Canvas sempre que Campaigns ou Canvas ativos ou parados possuem públicos que excedem o limite de complexidade do público. Selecione o banner para filtrar a lista apenas para as Campaigns ou Canvas que excedem o limite e, em seguida, siga as etapas de solução de problemas em [O público-alvo é complexo demais para ser lançado](#target-audience-is-too-complex-to-launch).

![Banner de erro informando que 4 Canvas ativos ou parados excedem o limite de complexidade do público.]({% image_buster /assets/img/segment/audience_complexity_threshold_banner.png %})

### O filtro excede 10.000 bytes ou é longo demais para salvar {#filter-exceeds-10000-bytes-or-is-too-long-to-save}

A Braze limita filtros individuais de Segment a um máximo de 10.000 bytes, o que equivale a 10.000 caracteres em inglês ou 3.333 caracteres em japonês. Um aviso aparece sempre que um filtro individual excede 10.000 bytes, seja o filtro dentro de um Segment ou adicionado diretamente a uma Campaign ou Canvas.

![Banner de erro para um filtro que possui um valor que excede 10.000 caracteres.]({% image_buster /assets/img/segment/filter_error.png %})

![Erro para um filtro de atributo personalizado, `menu_item`, que possui um valor de atributo que excede 10.000 caracteres.]({% image_buster /assets/img/segment/segment_filter_error.png %})

Esse erro ocorre muito raramente, mas quando ocorre, geralmente é com filtros de regex que visam uma lista de IDs de usuários ou endereços de e-mail. Nesse caso, você pode seguir estas etapas para converter os filtros em um CSV:

1. Exporte os usuários do Segment afetado ou do filtro de regex específico.
2. Limpe o CSV conforme necessário. Você precisa do Braze ID ou Appboy ID, mas pode remover todas as outras colunas se não forem necessárias. Também recomendamos revisar seus dados para confirmar que estão atualizados (por exemplo, remova usuários que você não está mais tentando alcançar).
3. [Importe]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) o arquivo CSV novamente, o que agrupa automaticamente os usuários em um único filtro baseado em CSV altamente eficiente.

## Comportamento do usuário {#user-behavior}

### O usuário não está mais em um Segment {#user-is-no-longer-in-a-segment}

Se um usuário não estiver disponível ao criar um Segment, os dados do usuário que determinam sua elegibilidade para o Segment podem ter mudado como resultado de sua própria atividade ou de outras Campaigns e Canvas com os quais ele interagiu anteriormente. Se a reelegibilidade estiver ativada, o perfil de usuário mostra os dados mais recentes da Campaign recebida.

Para testar se um usuário específico corresponde ao seu Segment hoje, use a [prévia de usuário ou busca de usuário]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).

### Informações de usuários de outros apps aparecem quando filtro por um app específico {#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app}

Os usuários podem ter vários apps, então selecionar um app específico na seção **Apps usados** da página de segmentação retornará resultados para usuários que possuem pelo menos aquele app. O filtro não retorna resultados apenas para os usuários que possuem exclusivamente aquele app.

## Filtragem {#filtering}

### As opções de filtro mudaram {#filter-options-changed}

Suas opções de filtro estão relacionadas ao formato (tipo de dados) que você está enviando para a Braze para seu atributo personalizado. Para revisar o tipo de dados que a Braze está reconhecendo para seus atributos personalizados, acesse **Data Settings** > **Custom Attributes**.

Se suas opções de filtro mudaram, isso indica que seus dados estão sendo enviados para a Braze em um formato (tipo de dados) diferente do anterior. Para descrições detalhadas dos diferentes tipos de dados e suas opções de filtragem, consulte [tipos de dados de atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types).

Lembre-se de que alterar o tipo de dados de um atributo personalizado no dashboard rejeita dados enviados para a Braze em um formato diferente. Não é possível alterar o tipo de dados de um atributo personalizado enquanto esse atributo estiver referenciado em Campaigns, Canvas ou Segments ativos; o dashboard exibe um erro e bloqueia a alteração.

A guia **Values** em um atributo personalizado mostra resultados de uma amostra de aproximadamente 250.000 usuários. Não use a guia **Values** para confirmar se um valor de atributo específico existe para fins de solução de problemas. Para saber mais, consulte [Guia Values]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#values-tab).

### Atributo personalizado aninhado não disponível como opção de filtro {#nested-custom-attribute-not-available-as-a-filter-option}

Se seu atributo personalizado aninhado não está aparecendo como opção de filtro ao criar um Segment, gere o esquema primeiro. Acesse **Data Settings** > **Custom Attributes**, encontre o atributo e selecione **Generate Schema**. Depois de gerado, o atributo fica disponível no menu suspenso de filtros do Segment. Para saber mais, consulte [Gerar um esquema usando o explorador de objetos aninhados]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes#generate-schema).

### O Segment é muito maior do que o esperado {#segment-is-much-larger-than-expected}

Se seu Segment parece muito maior do que você espera, apesar de filtros aparentemente restritivos, verifique se você está usando filtros negativos (`is not`, `does not equal`, `does not match regex` ou `not included`) com o operador **OR** no mesmo atributo mais de uma vez. Essa combinação pode segmentar usuários com todos os valores para o atributo.

Para orientações sobre quando usar **AND** em vez de **OR**, consulte [Quando evitar o operador OR]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#segmentation-logic-using-and-and-or) em Criar um Segment.

## Análise de dados e relatórios {#analytics-and-reporting}

### *Mensagens Enviadas* ou *Destinatários Únicos* na análise de dados de Campaign não corresponde à contagem do Segment {#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count}

Se a contagem de *Mensagens Enviadas* ou *Destinatários Únicos* na análise de dados da sua Campaign não corresponde ao número de usuários no filtro de Segment `Has received message from campaign X`, pode haver três possíveis razões.

1. **Usuários podem ter sido arquivados, ficado órfãos ou sido excluídos desde o lançamento da Campaign**<br><br>Por exemplo, digamos que 1.000 usuários recebam uma Campaign e você faça uma exportação CSV no mesmo dia. Você verá 1.000 usuários reportados. Ao longo do mês seguinte, 50 desses 1.000 usuários são excluídos (por exemplo, pelo endpoint `users/delete`). Quando você fizer outra exportação CSV, verá 950 usuários reportados, enquanto a contagem de *Destinatários Únicos* em **Campaign Analytics** ainda será 1.000.<br><br>Em outras palavras, a métrica de *Destinatários Únicos* é uma contagem incremental, enquanto o segmentador e a exportação CSV fornecem uma contagem de usuários existentes no momento.<br><br>

2. **A Campaign tem reelegibilidade configurada, permitindo que os usuários reentrem na Campaign várias vezes**<br><br>Por exemplo, digamos que uma Campaign de e-mail tenha a reelegibilidade configurada para zero minutos (os usuários podem reentrar na Campaign desde que atendam aos requisitos do Segment de público), e a Campaign esteja em execução há mais de um mês. O número de *Mensagens Enviadas* em **Campaign Analytics** não corresponderia ao número no Segment porque esse campo incluiria mensagens enviadas a usuários duplicados.<br><br>Isso acontece porque a Braze conta usuários únicos como *Destinatários Únicos Diários*, ou o número de usuários que receberam uma mensagem específica em um dia. Isso significa que usuários reelegíveis são contados mais de uma vez como destinatário único, pois a janela de "unicidade" dura apenas um dia. Isso pode resultar em um número de *Destinatários Únicos Diários* maior do que o número de perfis de usuário na exportação CSV. Os perfis de usuário no arquivo CSV são verdadeiramente únicos.<br><br>

3. **Usuários que compartilham um identificador de canal corresponderam ao filtro**<br><br> O filtro `Has received message from campaign X` (e outros filtros de "recebimento") pode corresponder a usuários que compartilham um identificador de canal, como o mesmo token por push ou endereço de e-mail, com outro perfil de usuário que recebeu, abriu ou clicou na mensagem.

### Usuário é atribuído a dois apps apesar de ter registrado uma sessão em apenas um app {#user-is-assigned-to-two-apps-despite-logging-a-session-in-only-one-app}

Ao criar um Segment, você pode segmentar usuários que [usaram apps específicos]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#step-3-choose-your-app-or-platform). Um usuário precisa ter tido uma sessão em um app específico para ser atribuído a esse app; no entanto, existem dois cenários em que um usuário ainda pode ser atribuído a um app específico sem ter registrado sessões nele.

O primeiro cenário é quando o campo `app_id` é preenchido ao usar o endpoint `/users/track` — especificamente ao usar um [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object) ou [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object), como neste exemplo:

```json
{
    "events": [
    {
      "external_id": "john_doe123",
      "app_id": "my_web_app_id",
      "name": "Custom Event",
      "time": "2025-08-17T19:20:30+1:00"
    }
  ]
}
```

O segundo cenário é quando o campo `app_id` é preenchido ao usar o endpoint `/users/track` para migrar tokens por push, como neste exemplo:

```json
{
"app_group_id": "{YOUR_APP_GROUP_ID}",
"attributes": [
{
      "push_token_import": false,
      "external_id": "external_id1",
      "country": "US",
      "language": "en",
      "{YOUR_CUSTOM_ATTRIBUTE}": "{YOUR_VALUE}",
      "push_tokens": [
        {"app_id": "{APP_ID_OF_OS}", "token": "{PUSH_TOKEN_STRING}"}
      ]
  }
]
}
```
