---
nav_title: Feature Flag
article_title: Feature Flag
page_order: 8
page_type: reference
description: "Este artigo de referência aborda como as Feature Flags podem ser usadas no Canvas."
tool: Canvas
local_redirect:
  create-a-feature-flag: '/docs/user_guide/messaging/feature_flags/create_feature_flags'
---

# Feature Flag

> As Feature Flags permitem que você experimente e confirme suas hipóteses sobre novos recursos. Profissionais de marketing podem usar Feature Flags para segmentar seu público no [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) e acompanhar o impacto do lançamento de recursos nas conversões. Além disso, as [Jornadas do experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#experiment-paths) permitem otimizar essas conversões testando diferentes mensagens ou jornadas entre si e determinando qual é a mais eficaz. Use a Jornada Vencedora à medida que você lança progressivamente seu recurso para um público mais amplo.

Quer saber mais sobre Feature Flags e como elas podem ser usadas na Braze? Confira nossos artigos dedicados sobre [Feature Flags]({{site.baseurl}}/developer_guide/feature_flags/).

## Criando uma Feature Flag

![Um exemplo de etapa Feature Flag para o recurso Botão de Chat ao Vivo.]({% image_buster /assets/img/feature_flags/feature_flag_canvas_step.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Para criar um componente Feature Flag, primeiro adicione uma etapa ao seu Canvas. Arraste e solte o componente da barra lateral, ou clique no botão de mais <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Feature Flag**. Em seguida, selecione a Feature Flag no menu suspenso, que contém todas as Feature Flags que não estão arquivadas.

## Como essa etapa funciona

Quando um Canvas é interrompido, arquivado ou uma etapa Feature Flag é removida, os usuários que passaram por essa etapa deixam de receber a Feature Flag e suas propriedades.

Para uma Feature Flag que não tem rollout nem experimento de Feature Flag, após interromper um Canvas que contém uma etapa Feature Flag referenciando essa flag:

- Nenhum usuário terá essa Feature Flag na guia **Feature Flags Eligibility**.
- Nenhum usuário corresponderá ao filtro de segmentação `Feature Flags` para essa Feature Flag.

Se a Feature Flag tiver um rollout, um experimento de Feature Flag ou outro Canvas ativo que a referencie, os usuários ainda poderão ser elegíveis por meio desses canais.

As propriedades em uma etapa do Canvas podem ser alteradas após o lançamento, e mesmo depois que um usuário passa pela etapa. Os usuários sempre recebem uma versão dinâmica e em tempo real da Feature Flag, em vez da versão anterior salva.

- **Dois Canvas referenciam a mesma Feature Flag e um usuário entra em ambos:** O usuário recebe o valor definido no Canvas em que entrou mais recentemente, não no anterior. Esse valor aparece na guia **Feature Flags Eligibility**.
- **Um Canvas tem duas etapas Feature Flag que referenciam a mesma Feature Flag:** O usuário recebe o valor definido na segunda etapa enquanto está nessa jornada, e esse valor aparece na guia **Feature Flags Eligibility**.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## Sobrescrever propriedades {#overwriting-properties}

Ao criar uma Feature Flag, você especifica propriedades padrão. Ao configurar uma etapa Feature Flag no Canvas, você pode manter os valores padrão ou sobrescrever os valores para os usuários que entrarem nessa etapa.

![Uma Feature Flag "Central de Preferências" com "String" como propriedade, "url" como chave da propriedade e um valor.]({% image_buster /assets/img/feature_flags/feature_flags_canvas_details.png %}){: style="max-width:90%"}

Acesse **Envio de mensagens** > **Feature Flags** para editar, adicionar ou remover propriedades adicionais.

## Diferenças entre Canvas e rollout

O Canvas e o rollout de uma Feature Flag (arrastar o controle deslizante) podem funcionar de forma independente. Uma ressalva importante é que a entrada em uma etapa do Canvas sobrescreve qualquer configuração padrão de rollout. Isso significa que, se um usuário não se qualificar para uma Feature Flag, uma etapa do Canvas pode ativar o recurso para esse usuário.

Da mesma forma, se um usuário se qualificar para o rollout de uma Feature Flag com determinadas propriedades e também entrar na etapa do Canvas, ele receberá os valores sobrescritos dessa etapa do Canvas.