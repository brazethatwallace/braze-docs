---
nav_title: Criar um segmento
article_title: Criar um segmento
page_order: 1
page_type: tutorial
description: "Este artigo prático orienta você sobre como configurar e criar um segmento usando a Braze."
tool: Segments
search_rank: 3
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Criar um segmento {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsegmentation-course-stylefloatrightwidth120pxborder0-classnoimgbordercreate-a-segment}

> A segmentação permite direcionar usuários com base em suas características e ações demográficas, comportamentais ou técnicas. O uso criativo e inteligente da segmentação e da automação de envio de mensagens permite mover seus usuários de forma fluida, do primeiro contato até se tornarem clientes de longo prazo. Os segmentos são atualizados em tempo real conforme os dados mudam, e você pode criar quantos segmentos precisar para fins de direcionamento e envio de mensagens.

## Etapa 1: Navegue até a seção de Segments {#step-1-navigate-to-the-segments-section}

Acesse **Público** > **Segments**.

## Etapa 2: Nomeie seu Segment {#step-2-name-your-segment}

Selecione **Create Segment** para começar a criar seu Segment. Nomeie seu Segment descrevendo o tipo de usuário que você pretende filtrar. Isso ajuda a identificar o Segment quando você quiser direcioná-lo para suas Campaigns ou Canvas. Títulos vagos de Segment podem ser confusos.

Você também pode pedir ao Operator para ajudar a criar a lógica de filtro do seu Segment a partir de uma descrição do seu público-alvo. Para mais detalhes, consulte [O que você pode fazer com o Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#campaigns-and-audiences).

Opcionalmente, você pode fazer o seguinte:
- Adicionar uma descrição ao Segment para fornecer mais detalhes sobre a intenção desse público e deixar anotações para outros membros da equipe consultarem.
- Adicionar uma [equipe]({{site.baseurl}}/user_guide/administer/global/user_management/teams) ao seu Segment.
- Adicionar [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) ao seu Segment para uma organização mais detalhada.

Os Segments são salvos assim que você seleciona **Create Segment**. Não é necessário selecionar **Save** no editor de Segment primeiro.

{% alert note %}
Se você tiver a permissão "Edit Segments" apenas no nível da equipe (não no nível do espaço de trabalho), a Braze atribui uma equipe quando o Segment é criado:
<br><br>
- **Uma equipe elegível:** Essa equipe é atribuída automaticamente.
- **Múltiplas equipes elegíveis:** A Braze atribui a primeira equipe da sua lista de equipes elegíveis. Você pode alterar a equipe no editor de Segment antes de compartilhar ou usar o Segment.
{% endalert %}

## Etapa 3: Escolha seu app ou plataforma {#step-3-choose-your-app-or-platform}

Escolha quais apps ou plataformas você deseja direcionar selecionando **Users from all apps** (padrão) ou **Users from specific apps**. **Users from specific apps** direciona usuários com pelo menos uma sessão nos apps especificados.

Por exemplo, se você deseja enviar uma mensagem no app apenas para dispositivos iOS, selecione seu app iOS. Isso garante que os usuários que usam tanto um dispositivo iOS quanto um Android recebam a mensagem apenas no dispositivo iOS. Na lista de apps específicos, a opção **Users from no apps** permite incluir usuários sem sessões e sem dados de app (normalmente criados por meio de importação de usuário ou REST API).

![Painel de detalhes do Segment com a opção "Users from all apps" selecionada na seção Apps Used.]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:80%;"}

## Etapa 4: Adicionar filtros ao seu Segment {#step-4-add-filters-to-your-segment}

Adicione pelo menos um filtro ao seu Segment. Você pode combinar quantos filtros quiser para tornar sua segmentação mais específica.

{% multi_lang_include alerts/note_alerts.md alert='Segment profiles first app use' %}

### Grupos de filtros {#filter-groups}

Os filtros são organizados em grupos de filtros. Cada filtro deve fazer parte de um grupo de filtros que tenha no mínimo um filtro. Um Segment pode ter vários grupos de filtros. Para adicionar um, selecione **Adicionar grupo de filtros**. Edite o nome do grupo de filtros selecionando o ícone que aparece quando você passa o cursor ao lado dele.

![Grupo de filtros com um ícone de edição ao lado do nome.]({% image_buster /assets/img_archive/edit_filter_group_name.png %})

Selecione os ícones ao lado de cada filtro para recolher o editor de filtros ou duplicar filtros individuais. Após duplicar um filtro, você pode ajustar seus valores em cada menu suspenso.

### Lógica de segmentação usando AND e OR {#segmentation-logic-using-and-and-or}

Dentro de um grupo de filtros, os filtros podem ser unidos por "AND" ou "OR". Entre grupos de filtros, os grupos podem ser unidos por "AND" ou "OR". Ao usar grupos de filtros, você pode criar lógicas de segmentação como:
- (A AND B AND C) OR (C AND E AND F)
- (A OR B OR C) AND (C OR D OR F)

Selecionar "OR" para seus filtros significa que seu Segment conterá usuários que satisfaçam qualquer combinação de um, alguns ou todos esses filtros. Selecionar "AND" significa que os usuários que não passarem por esse filtro não serão incluídos no seu Segment.

{% alert tip %}
Ao selecionar "OR" para filtros que incluem um filtro negativo (como "não é" em um grupo de inscrições), lembre-se de que os usuários só precisam atender a um dos filtros "OR" para serem incluídos no Segment. Para aplicar o filtro negativo independentemente dos outros filtros, use um [grupo de exclusão](#exclusion).
{% endalert %}

{% details Quando evitar o operador OR %}

Pode haver situações de direcionamento de usuários em que o uso do operador `OR` deve ser evitado. O operador `OR` cria uma declaração que é avaliada como verdadeira se um usuário atender aos critérios de um ou mais filtros em uma declaração. Por exemplo, se você quiser criar um Segment de usuários que pertencem a "Foodies" mas não pertencem a "Non-foodies" ou "Candy-lovers", então usar o operador `OR` funcionaria aqui.

![Grupo de filtros para usuários no Segment "foodies" e que não estão nos Segments "non-foodies" ou "candy-lovers".]({% image_buster /assets/img_archive/or_operator_segment.png %})

No entanto, se seu objetivo é segmentar usuários que pertencem ao Segment "Foodies" e não estão em nenhum dos Segments "Non-foodies" e "Candy-lovers", então use o operador `AND`. Dessa forma, os usuários que receberem a Campaign ou o Canvas estarão no Segment pretendido ("foodies") e não estarão nos outros Segments ("Non-foodies" e "Candy-lovers") ao mesmo tempo.

Os seguintes critérios de direcionamento negativo não devem ser usados com o operador `OR` quando dois ou mais filtros fazem referência ao mesmo atributo:

- `not included`
- `is not`
- `does not equal`
- `does not match regex`

Se `not included`, `is not`, `does not equal` ou `does not match regex` forem usados com o operador `OR` duas ou mais vezes em uma declaração, os usuários com todos os valores para o atributo relevante serão direcionados.

{% enddetails %}

### Operadores de filtro {#filter-operators}

Dependendo do filtro específico que você selecionar, haverá diferentes operadores para identificar valores de filtro. Para se aprofundar nos operadores disponíveis para diferentes tipos de atributos personalizados, consulte [Armazenamento de atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#set-custom-attributes). Observe que, ao usar o operador "is any of", o número máximo de itens que você pode incluir nesse campo é 256.

{% alert note %}
A Braze não gera perfis para usuários até que eles tenham usado o app pela primeira vez, então você não pode direcionar usuários que ainda não abriram seu app.
{% endalert %}

![Grupos de filtros do segmentador com o operador AND.]({% image_buster /assets/img_archive/segmenter_filter_groups.png %})

{% alert important %}
Segments que já usam o filtro **Segment Membership** não podem ser incluídos ou aninhados em outros Segments. Isso evita um ciclo em que o Segment A inclui o Segment B, que então tenta incluir o Segment A novamente. Se isso acontecesse, o Segment ficaria referenciando a si mesmo continuamente, tornando impossível calcular quem realmente pertence a ele.

Além disso, aninhar Segments dessa forma adiciona complexidade e pode tornar as coisas mais lentas. Em vez disso, recrie o Segment que você está tentando incluir usando os mesmos filtros.
{% endalert %}

### Grupos de exclusão (opcional) {#exclusion}

Ao criar um Segment, você pode aplicar um ou vários grupos de exclusão. Os grupos de exclusão contêm critérios que identificam usuários a serem excluídos do seu Segment e sempre serão conectados aos seus grupos de filtros com um operador "AND NOT".

Os grupos de exclusão substituem os critérios do Segment. Se um usuário se enquadrar nos critérios do seu grupo de exclusão, ele não fará parte do seu Segment, mesmo que atenda aos critérios dentro dos seus grupos de filtros.

Crie um grupo de exclusão adicionando filtros da mesma forma que faria para grupos de filtros. A estatística _Usuários contatáveis estimados_ em um grupo de exclusão mostra o número estimado de usuários restantes no seu Segment após a aplicação dos critérios de exclusão.

Os usuários excluídos não serão contados como parte da estatística _Total de usuários contatáveis_ do seu Segment.

![Um grupo de exclusão com dois filtros.]({% image_buster /assets/img_archive/segmenter_exclusion_groups.png %})

### Ver estatísticas de funil {#viewing-funnel-statistics}

Selecione **Ver estatísticas de funil** para exibir as estatísticas desse grupo de filtros e ver como cada filtro adicionado impacta as estatísticas do seu Segment. Você verá uma contagem estimada e a porcentagem de usuários que são direcionados por todos os filtros até aquele ponto. Depois que as estatísticas forem exibidas para um grupo de filtros, elas serão atualizadas automaticamente sempre que você alterar os filtros. Essas estatísticas são estimadas e podem levar um momento para serem geradas.

Tenha em mente que, se você usar AND entre seus filtros, as estatísticas de funil diminuirão; se usar OR entre seus filtros, as estatísticas de funil aumentarão.

![Dois filtros com estatísticas de funil do Segment.]({% image_buster /assets/img_archive/segment_funnel_statistics.png %})

Ao adicionar filtros que documentam o fluxo do seu usuário, você pode ver os pontos em que os usuários desistem. Por exemplo, se você tem um app de rede social e quer ver onde pode estar perdendo usuários durante o processo de integração, pode adicionar filtros de dados personalizados para cadastro, adição de amigos e envio da primeira mensagem. Se você descobrir que 85% dos usuários estão se cadastrando e adicionando amigos, mas apenas 45% enviaram a primeira mensagem, então saberá que deve focar em incentivar mais envios de mensagens durante suas Campaigns de integração e marketing.

### Testar Segments {#testing-segments}

Após adicionar apps e filtros ao seu Segment, você pode testar se o Segment está configurado conforme esperado buscando um usuário para confirmar se ele corresponde aos critérios do Segment. Para isso, pesquise o `external_id` ou `braze_id` de um usuário na seção **Busca de usuário**.

{% alert note %}
A **Busca de usuário** aceita apenas `external_id` e `braze_id`. Ela não aceita endereços de e-mail, números de telefone ou outros identificadores. Para encontrar um perfil por e-mail, telefone ou outros campos, use [**Pesquisar usuários**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles).
{% endalert %}

![Seção de busca de usuário com um campo de pesquisa.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%;"}

A busca de usuário está disponível ao:
- Criar um Segment
- Configurar o público de uma Campaign ou Canvas
- Configurar uma etapa de jornada do público

Quando um usuário corresponde aos critérios do Segment, filtro e app, um alerta indicará isso.

![Uma busca de usuário de "testuser" dispara um alerta informando: "testuser corresponde a todos os Segments, filtros e apps."]({% image_buster /assets/img_archive/user_lookup_match.png %})

Quando um usuário não corresponde a parte ou a todos os critérios do Segment, filtro ou app, os critérios ausentes são listados para fins de solução de problemas.

![Uma busca de usuário com um alerta informando: "test1 não corresponde aos seguintes critérios de direcionamento:" e exibe os critérios ausentes.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %})

### Segments de usuário único {#single-user-segments}

Você pode criar Segments de usuário único (ou Segments com um punhado de usuários) usando atributos exclusivos que identificam usuários, como um nome de usuário ou um ID de usuário.

No entanto, as estatísticas de segmentação ou a prévia podem não mostrar esse usuário individual porque as estatísticas do Segment são calculadas com base em uma amostra aleatória com um intervalo de confiança de 95% de que o resultado está dentro de +/- 1%. Quanto maior for sua base de usuários, mais provável é que o tamanho do seu Segment seja uma estimativa aproximada. Para garantir que seu Segment contenha o único usuário que você está direcionando, selecione **Calcular estatísticas exatas**. Isso calculará o número exato de usuários no seu Segment com precisão superior a 99,999%.

A Braze possui filtros de teste para direcionar usuários específicos por ID de usuário ou endereço de e-mail.

## Etapa 5: Salvar seu Segment {#step-5-save-your-segment}

Selecione **Salvar**. Agora você está pronto para começar a enviar mensagens para seus usuários!

## Medindo o tamanho do Segment {#measuring-segment-size}

Para saber mais sobre como monitorar a associação e o tamanho do seu Segment, consulte [Medindo o tamanho do Segment]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

## Arquivando Segments {#archiving-segments}

Se você não precisa mais ou deseja desativar um Segment específico, pode arquivá-lo acessando a página **Segments** e selecionando **Archive** no menu na linha desse Segment.

{% alert warning %}
Quando você arquiva um Segment, quaisquer Campaigns ou Canvas que o utilizem (mesmo que o Segment seja usado apenas em um único componente do Canvas) também serão arquivados. Isso também inclui Segments aninhados, onde ambos os Segments e quaisquer Campaigns ou Canvas que os utilizem também serão arquivados.
<br><br>
Você receberá um alerta listando quais Campaigns e Canvas estão prestes a ser arquivados ao arquivar o Segment associado.
{% endalert %}

Você pode desarquivar o Segment navegando até ele na página **Segments** e selecionando **Unarchive**.

## Comportamento de direcionamento quando os usuários têm vários dispositivos {#targeting-behavior-when-users-have-multiple-devices}

Os usuários têm mais de um dispositivo quando fazem login na mesma conta em vários dispositivos. Você pode verificar a existência de vários dispositivos na seção **Dispositivos recentes** de um [perfil de usuário]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles).

Ao segmentar com filtros dependentes de dispositivo (modelo do dispositivo, sistema operacional do dispositivo e versão do app), seu Segment conterá todos os usuários que correspondem aos critérios do filtro. Esses usuários receberão uma mensagem em todos os seus dispositivos, incluindo aqueles que podem não atender aos critérios do filtro. Por exemplo, digamos que o Usuário A tenha dois dispositivos: o Dispositivo 1 tem o SO 13.0 e o Dispositivo 2 tem o SO 10.0. Se um Segment direcionar usuários com SO 10.0, esse usuário fará parte desse Segment e receberá mensagens em ambos os dispositivos.

### Notificações por push {#push-notifications}

Você pode especificar que apenas uma notificação por push seja enviada a cada usuário. Ao [compor sua mensagem]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#step-4-compose-your-push-message), selecione **Only send to the user's last used device** em **Additional Settings**.

!["Configurações adicionais" com uma caixa de seleção para enviar apenas para o último dispositivo usado pelo usuário.]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### Considerações {#considerations}

- **As mensagens enviadas podem exceder o tamanho do público.** Quando alguns usuários têm mais de um dispositivo, cada dispositivo pode receber uma mensagem. Isso resulta em um número de envios de mensagens maior do que o de usuários no seu Segment.
- **A participação de um usuário no Segment pode não parecer como você esperaria.**
    - Um usuário pode ser direcionado no dispositivo atual com base em atributos associados a um dispositivo diferente. Se você não esperava que um usuário recebesse uma mensagem, verifique o perfil de usuário dele para identificar vários dispositivos.
    - Um usuário pode ter estado no seu Segment de destino no momento do envio, mas, devido a comportamentos associados a qualquer um de seus dispositivos, pode não fazer mais parte desse Segment depois. Isso pode resultar em um usuário recebendo uma Campaign ou Canvas mesmo que ele atualmente não corresponda aos critérios do filtro. <br><br>Por exemplo, um usuário pode receber uma mensagem direcionada a usuários com a versão mais recente do app com SO 10.0, mesmo que atualmente ele tenha o SO 13.0. Nesse caso, o usuário tinha o SO 10.0 quando a mensagem foi enviada e depois fez upgrade para o SO 13.0.<br><br> Da mesma forma, se um usuário usar posteriormente um dispositivo com uma versão diferente do app, o perfil de usuário dele será atualizado com a nova versão mais recente do app. Isso pode fazer parecer que o usuário não deveria ter se qualificado para a mensagem, mesmo que ele tenha se qualificado no momento do envio.