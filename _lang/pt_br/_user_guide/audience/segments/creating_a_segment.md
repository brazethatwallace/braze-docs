---
nav_title: Criar um segmento
article_title: Criar um segmento
page_order: 1
page_type: tutorial
description: "Este artigo prático vai orientar você sobre como configurar e criar um segmento usando a Braze."
tool: Segments
search_rank: 3
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Criar um segmento {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsegmentation-course-stylefloatrightwidth120pxborder0-classnoimgbordercreate-a-segment}

> A segmentação permite direcionar usuários com base em suas características e ações demográficas, comportamentais ou técnicas. O uso criativo e inteligente da segmentação e da automação de envio de mensagens permite mover seus usuários de forma fluida, do primeiro contato até se tornarem clientes de longo prazo. Os segmentos são atualizados em tempo real conforme os dados mudam, e você pode criar quantos segmentos precisar para fins de direcionamento e envio de mensagens.

## Etapa 1: Navegue até a seção de segmentos {#step-1-navigate-to-the-segments-section}

Acesse **Público** > **Segments**.

## Etapa 2: Nomeie seu segmento {#step-2-name-your-segment}

Selecione **Criar segmento** para começar a construir seu segmento. Nomeie seu segmento descrevendo o tipo de usuário que você pretende filtrar. Isso ajudará a identificar o segmento quando você quiser direcioná-lo para suas Campaigns ou Canvas. Títulos vagos de segmentos podem causar confusão.

Opcionalmente, você pode fazer o seguinte:
- Adicionar uma descrição ao segmento para fornecer mais detalhes sobre a intenção desse público e deixar anotações para outros membros da equipe consultarem.
- Adicionar uma [equipe]({{site.baseurl}}/user_guide/administer/global/user_management/teams) ao seu segmento.
- Adicionar [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) ao seu segmento para melhor organização.

![Modal de criação de segmento onde o segmento é nomeado "Lapsed Users" com a descrição "This is our main Lapsed User segment to target non-actives within the past fourteen days." com dois botões: Cancelar e Criar segmento.]({% image_buster /assets/img_archive/segment_app_selection.png %}){: style="max-width:80%;"}

## Etapa 3: Escolha seu app ou plataforma {#step-3-choose-your-app-or-platform}

Escolha quais apps ou plataformas você deseja direcionar selecionando **Usuários de todos os apps** (padrão) ou **Usuários de apps específicos**. **Usuários de apps específicos** direciona usuários com pelo menos uma sessão nos apps especificados.

Por exemplo, se você deseja enviar uma mensagem no app apenas para dispositivos iOS, selecione seu app iOS. Isso garantirá que usuários que possam usar tanto um dispositivo iOS quanto Android receberão a mensagem apenas no dispositivo iOS. Na lista de apps específicos, a opção **Usuários sem apps** permite incluir usuários sem sessões e sem dados de app (normalmente criados por importação de usuários ou REST API).

![Painel de detalhes do segmento com a opção "Usuários de todos os apps" selecionada na seção Apps utilizados.]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:80%;"}

## Etapa 4: Adicione filtros ao seu segmento {#step-4-add-filters-to-your-segment}

Adicione pelo menos um filtro ao seu segmento. Você pode combinar quantos filtros quiser para tornar sua segmentação mais específica.

{% multi_lang_include alerts/note_alerts.md alert='Segment profiles first app use' %}

### Grupos de filtros {#filter-groups}

Os filtros são organizados em grupos de filtros. Cada filtro deve fazer parte de um grupo de filtros que tenha no mínimo um filtro. Um segmento pode ter vários grupos de filtros. Para adicionar um, selecione **Adicionar grupo de filtros**. Edite o nome do grupo de filtros selecionando o ícone que aparece ao passar o cursor ao lado dele.

![Grupo de filtros com um ícone de edição ao lado do nome.]({% image_buster /assets/img_archive/edit_filter_group_name.png %})

Selecione os ícones ao lado de cada filtro para recolher o editor de filtros ou duplicar filtros individuais. Após duplicar um filtro, você pode ajustar seus valores em cada menu suspenso.

### Lógica de segmentação usando AND e OR {#segmentation-logic-using-and-and-or}

Dentro de um grupo de filtros, os filtros podem ser unidos por "AND" ou "OR". Entre grupos de filtros, os grupos podem ser unidos por "AND" ou "OR". Ao usar grupos de filtros, você pode criar lógicas de segmentação como:
- (A AND B AND C) OR (C AND E AND F)
- (A OR B OR C) AND (C OR D OR F)

Selecionar "OR" para seus filtros significa que seu segmento conterá usuários que satisfaçam qualquer combinação de um, alguns ou todos esses filtros. Selecionar "AND" significa que usuários que não passarem nesse filtro não serão incluídos no seu segmento.

{% alert tip %}
Ao selecionar "OR" para filtros que incluem um filtro negativo (como "não é" em um grupo de inscrições), lembre-se de que os usuários só precisam atender a um dos filtros "OR" para serem incluídos no segmento. Para aplicar o filtro negativo independentemente dos outros filtros, use um [grupo de exclusão](#exclusion).
{% endalert %}

{% details Quando evitar o operador OR %}

Pode haver situações de direcionamento de usuários em que o uso do operador `OR` deve ser evitado. O operador `OR` cria uma declaração que é avaliada como verdadeira se um usuário atender aos critérios de um ou mais filtros em uma declaração. Por exemplo, se você quiser criar um segmento de usuários que pertencem a "Foodies" mas não pertencem a "Non-foodies" ou "Candy-lovers", usar o operador `OR` funcionaria aqui.

![Grupo de filtros para usuários no segmento "foodies" e que não estão nos segmentos "non-foodies" ou "candy-lovers".]({% image_buster /assets/img_archive/or_operator_segment.png %})

No entanto, se seu objetivo é segmentar usuários que pertencem ao segmento "Foodies" e não estão em nenhum dos segmentos "Non-foodies" e "Candy-lovers", use o operador `AND`. Dessa forma, os usuários que receberem a Campaign ou Canvas estarão no segmento pretendido ("foodies") e não estarão nos outros segmentos ("Non-foodies" e "Candy-lovers") ao mesmo tempo.

Os seguintes critérios de direcionamento negativo não devem ser usados com o operador `OR` quando dois ou mais filtros fazem referência ao mesmo atributo:

- `not included`
- `is not`
- `does not equal`
- `does not match regex`

Se `not included`, `is not`, `does not equal` ou `does not match regex` forem usados com o operador `OR` duas ou mais vezes em uma declaração, usuários com todos os valores para o atributo relevante serão direcionados.

{% enddetails %}

### Operadores de filtro {#filter-operators}

Dependendo do filtro específico que você selecionar, haverá diferentes operadores para identificar valores de filtro. Para se aprofundar nos operadores disponíveis para diferentes tipos de atributos personalizados, consulte [Armazenamento de atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#setting-custom-attributes). Observe que, ao usar o operador "is any of", o número máximo de itens que você pode incluir nesse campo é 256.

{% alert note %}
A Braze não gera perfis para usuários até que eles usem o app pela primeira vez, então você não pode direcionar usuários que ainda não abriram seu app.
{% endalert %}

![Grupos de filtros do segmentador com o operador AND.]({% image_buster /assets/img_archive/segmenter_filter_groups.png %})

{% alert important %}
Segments que já usam o filtro **Segment Membership** não podem ser incluídos ou aninhados em outros segmentos. Isso evita um ciclo em que o Segment A inclui o Segment B, que então tenta incluir o Segment A novamente. Se isso acontecesse, o segmento ficaria referenciando a si mesmo, tornando impossível calcular quem realmente pertence a ele.

Além disso, aninhar segmentos dessa forma adiciona complexidade e pode tornar as coisas mais lentas. Em vez disso, recrie o segmento que você está tentando incluir usando os mesmos filtros.
{% endalert %}

### Grupos de exclusão (opcional) {#exclusion}

Ao construir um segmento, você pode aplicar um ou vários grupos de exclusão. Grupos de exclusão contêm critérios que identificam usuários a serem excluídos do seu segmento e sempre serão conectados aos seus grupos de filtros com um operador "AND NOT".

Grupos de exclusão substituem os critérios do segmento. Se um usuário se enquadrar nos critérios do seu grupo de exclusão, ele não fará parte do seu segmento, mesmo que atenda aos critérios dos seus grupos de filtros.

Crie um grupo de exclusão adicionando filtros da mesma forma que faria para grupos de filtros. A estatística *Usuários contatáveis estimados* em um grupo de exclusão mostra o número estimado de usuários restantes no seu segmento após a aplicação dos critérios de exclusão.

Usuários excluídos não serão contados como parte da estatística *Total de usuários contatáveis* do seu segmento.

![Um grupo de exclusão com dois filtros.]({% image_buster /assets/img_archive/segmenter_exclusion_groups.png %})

### Visualizar estatísticas de funil {#viewing-funnel-statistics}

Selecione **Visualizar estatísticas de funil** para exibir as estatísticas desse grupo de filtros e ver como cada filtro adicionado impacta as estatísticas do seu segmento. Você verá uma contagem estimada e a porcentagem de usuários que são direcionados por todos os filtros até aquele ponto. Depois que as estatísticas forem exibidas para um grupo de filtros, elas serão atualizadas automaticamente sempre que você alterar os filtros. Essas estatísticas são estimadas e podem levar um momento para serem geradas.

Tenha em mente que, se você usar AND entre seus filtros, as estatísticas de funil diminuirão; se usar OR entre seus filtros, as estatísticas de funil aumentarão.

![Dois filtros com estatísticas de funil do segmento.]({% image_buster /assets/img_archive/segment_funnel_statistics.png %})

Ao adicionar filtros que documentam o fluxo dos seus usuários, você pode ver os pontos onde os usuários desistem. Por exemplo, se você tem um app de rede social e quer ver onde pode estar perdendo usuários durante o processo de integração, pode adicionar filtros de dados personalizados para cadastro, adição de amigos e envio da primeira mensagem. Se você descobrir que 85% dos usuários estão se cadastrando e adicionando amigos, mas apenas 45% enviaram a primeira mensagem, então saberá que deve focar em incentivar mais envios de mensagens durante suas campanhas de integração e marketing.

### Testando segmentos {#testing-segments}

Após adicionar apps e filtros ao seu segmento, você pode testar se o segmento está configurado conforme esperado procurando um usuário para confirmar se ele corresponde aos critérios do segmento. Para isso, pesquise o `external_id` ou `braze_id` de um usuário na seção **Busca de usuário**.

{% alert note %}
A **Busca de usuário** aceita apenas `external_id` e `braze_id`. Não aceita endereços de e-mail, números de telefone ou outros identificadores. Para encontrar um perfil por e-mail, telefone ou outros campos, use [**Pesquisar usuários**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles).
{% endalert %}

![Seção de busca de usuário com um campo de pesquisa.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%;"}

A busca de usuário está disponível quando:
- Você está criando um segmento
- Você está configurando o público de uma Campaign ou Canvas
- Você está configurando uma etapa de Jornadas do público

Quando um usuário corresponde aos critérios do segmento, filtro e app, um alerta indicará isso.

![Uma busca de usuário de "testuser" aciona um alerta informando: "testuser corresponde a todos os segmentos, filtros e apps."]({% image_buster /assets/img_archive/user_lookup_match.png %})

Quando um usuário não corresponde a parte ou a todos os critérios do segmento, filtro ou app, os critérios ausentes são listados para fins de solução de problemas.

![Uma busca de usuário com um alerta informando: "test1 não corresponde aos seguintes critérios de direcionamento:" e exibe os critérios ausentes.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %})

### Segmentos de usuário único {#single-user-segments}

Você pode criar segmentos de usuário único (ou segmentos com poucos usuários) usando atributos únicos que identificam usuários, como um nome de usuário ou um ID de usuário.

No entanto, as estatísticas de segmentação ou a pré-visualização podem não mostrar esse usuário individual porque as estatísticas de segmento são calculadas com base em uma amostra aleatória com um intervalo de confiança de 95% de que o resultado está dentro de +/- 1%. Quanto maior for sua base de usuários, mais provável é que o tamanho do seu segmento seja uma estimativa aproximada. Para garantir que seu segmento contenha o único usuário que você está direcionando, selecione **Calcular estatísticas exatas**. Isso calculará o número exato de usuários no seu segmento com precisão superior a 99,999%.

A Braze possui filtros de teste para direcionar usuários específicos por ID de usuário ou endereço de e-mail.

## Etapa 5: Salve seu segmento {#step-5-save-your-segment}

Selecione **Salvar**. Agora você está pronto para começar a enviar mensagens aos seus usuários!

## Medindo o tamanho do segmento {#measuring-segment-size}

Para saber mais sobre como monitorar a associação e o tamanho do seu segmento, consulte [Medindo o tamanho do segmento]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

## Arquivando segmentos {#archiving-segments}

Se você não precisa mais ou deseja desativar um segmento específico, pode arquivá-lo acessando a página **Segments** e selecionando **Arquivar** no menu na linha desse segmento.

{% alert warning %}
Ao arquivar um segmento, quaisquer Campaigns ou Canvas que o utilizem (mesmo que o segmento seja usado apenas em um único componente do Canvas) também serão arquivados. Isso também inclui segmentos aninhados, onde ambos os segmentos e quaisquer Campaigns ou Canvas que os utilizem também serão arquivados.
<br><br>
Você receberá um aviso listando quais Campaigns e Canvas estão prestes a ser arquivados ao arquivar o segmento associado.
{% endalert %}

Você pode desarquivar o segmento navegando até ele na página **Segments** e selecionando **Desarquivar**.

## Comportamento de direcionamento quando os usuários têm vários dispositivos {#targeting-behavior-when-users-have-multiple-devices}

Os usuários têm mais de um dispositivo se fizerem login na mesma conta em vários dispositivos. Você pode verificar múltiplos dispositivos na seção **Dispositivos recentes** de um [perfil de usuário]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles).

Ao segmentar com filtros dependentes de dispositivo (modelo do dispositivo, sistema operacional do dispositivo e versão do app), seu segmento conterá todos os usuários que correspondem aos critérios do filtro. Esses usuários receberão uma mensagem em todos os seus dispositivos, incluindo aqueles que podem não atender aos critérios do filtro. Por exemplo, digamos que o Usuário A tem dois dispositivos: o Dispositivo 1 tem o SO 13.0 e o Dispositivo 2 tem o SO 10.0. Se um segmento direcionar usuários com SO 10.0, esse usuário fará parte desse segmento e receberá mensagens em ambos os dispositivos.

### Notificações por push {#push-notifications}

Você pode especificar que apenas uma notificação por push seja enviada para cada usuário. Ao [redigir sua mensagem]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#step-4-compose-your-push-message), selecione **Enviar apenas para o último dispositivo usado pelo usuário** em **Configurações adicionais**.

!["Configurações adicionais" com uma caixa de seleção para enviar apenas para o último dispositivo usado pelo usuário.]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### Considerações {#considerations}

- **As mensagens enviadas podem exceder o tamanho do público.** Quando alguns usuários têm mais de um dispositivo, cada dispositivo pode receber uma mensagem. Isso causa um número maior de envios de mensagens do que de usuários no seu segmento.
- **A associação de um usuário ao segmento pode não parecer como você esperaria.**
    - Um usuário pode ser direcionado no dispositivo atual com base em atributos associados a um dispositivo diferente. Se você não esperava que um usuário recebesse uma mensagem, verifique o perfil de usuário dele para múltiplos dispositivos.
    - Um usuário pode ter estado no seu segmento-alvo no momento do envio, mas devido a comportamentos associados a qualquer um de seus dispositivos, pode não fazer mais parte desse segmento depois. Isso pode resultar em um usuário recebendo uma Campaign ou Canvas mesmo que atualmente não corresponda aos critérios do filtro. <br><br>Por exemplo, um usuário poderia receber uma mensagem direcionada a usuários com a versão mais recente do app com SO 10.0, mesmo que atualmente tenha o SO 13.0. Nesse caso, o usuário tinha o SO 10.0 quando a mensagem foi enviada e depois atualizou para o SO 13.0.<br><br> Da mesma forma, se um usuário usar posteriormente um dispositivo com uma versão diferente do app, seu perfil de usuário será atualizado com uma nova versão mais recente do app. Isso pode fazer parecer que o usuário não deveria ter se qualificado para a mensagem, mesmo que tenha se qualificado quando ela foi enviada.