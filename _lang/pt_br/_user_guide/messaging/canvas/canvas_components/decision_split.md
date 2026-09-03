---
nav_title: Divisão de decisão
article_title: Divisão de decisão
alias: /decision_split/
page_order: 7
page_type: reference
description: "Este artigo de referência aborda como criar e usar divisões de decisão no seu Canvas."
tool: Canvas

---

# Divisão de decisão {#decision-split}

> O componente de divisão de decisão no Canvas permite entregar experiências personalizadas e em tempo real para seus usuários.

![Uma etapa de Divisão de decisão chamada "Push ativado?" para usuários que não têm push ativado e usuários que têm push ativado.]({% image_buster /assets/img/decision-split-1.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

Esse componente pode ser usado para criar ramificações no Canvas com base em se um usuário corresponde a uma consulta.

## Crie uma divisão de decisão {#create-a-decision-split}

Para criar uma divisão de decisão no seu fluxo de trabalho, adicione uma etapa ao seu Canvas. Em seguida, arraste e solte o componente da barra lateral, ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Decision Split**.

### Defina sua divisão {#define-your-split}

Como você deseja dividir seus usuários? Você pode usar [Segments]({{site.baseurl}}/user_guide/audience/segments) e filtros para traçar a linha. Essencialmente, você está criando uma consulta `true` ou `false` que avaliará seus usuários e os direcionará para uma etapa ou outra. Você deve usar pelo menos um Segment ou um filtro. Não é necessário usar ambos.

![Uma etapa de divisão de decisão com o filtro "Foreground Push Enabled is true" selecionado.]({% image_buster /assets/img/define-split-2.png %})

{% alert note %}
Por padrão, os Segments e filtros de uma etapa de divisão de decisão são verificados logo após o recebimento de uma etapa anterior, a menos que você adicione uma postergação.
{% endalert %}

#### Filtros de redirecionamento em Canvas com reentrada {#retargeting-filters-in-canvases-with-re-entry}

Os filtros de redirecionamento em uma etapa de divisão de decisão, como `Clicked/Opened Step In This Canvas`, avaliam o engajamento em todas as entradas do Canvas para um usuário, incluindo entradas anteriores. Por exemplo, se um usuário interagiu com uma etapa durante uma entrada anterior, a divisão de decisão reconhece essa interação quando ele reentra no Canvas.

Para Canvas com reentrada ativada, use uma etapa de [jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) com o disparador **Interact with Step** quando precisar avaliar o engajamento apenas durante a entrada atual do Canvas dentro de uma janela de tempo. As jornadas de ação contam apenas as interações que ocorrem durante a janela de avaliação da etapa.

## Use sua divisão de decisão {#use-your-split}

Usar uma divisão de decisão pode ajudar você a distinguir jornadas para seus usuários com base no Segment ou nos atributos deles, e até mesmo se eles usam determinados canais de envio de mensagens para receber suas mensagens!

Digamos que você esteja criando um fluxo de integração. Você pode começar com um e-mail de boas-vindas no momento do cadastro. Depois, dois dias mais tarde, você quer enviar uma mensagem push, mas apenas para usuários que têm push ativado. Após isso, todos os usuários recebem outro e-mail três dias depois do cadastro. Você também pode usar sua divisão de decisão para enviar uma mensagem no app aos usuários que não têm push ativado, incentivando-os a ativar o push.

Se não houver nenhuma etapa após uma das jornadas, os usuários que seguirem por essa jornada sairão do Canvas.

![Uma etapa de divisão de decisão chamada "Push ativado?" para usuários que não têm push ativado e para aqueles que têm. Para usuários que não têm push ativado, eles passam por uma postergação de 3 dias e depois recebem uma mensagem de e-mail. Para usuários que têm push ativado, eles passam por uma postergação de 1 dia, recebem uma notificação por push seguida de uma postergação de 2 dias, e depois recebem a mesma mensagem de e-mail que os usuários que não têm push ativado.]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## Análise de dados {#analytics}

Consulte a tabela a seguir para descrições da análise de dados desta etapa:

| Métrica | Descrição |
|---|---|
| _Entraram_ | O número total de vezes que a etapa foi acessada. Se o seu Canvas tiver reelegibilidade e um usuário entrar em uma etapa de divisão de decisão duas vezes, duas entradas serão registradas. |
| _Sim_ | O número de entradas que atenderam aos critérios especificados e seguiram pela jornada "sim". |
| _Não_ | O número de entradas que não atenderam aos critérios especificados e seguiram pela jornada "não". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Análise de dados" }