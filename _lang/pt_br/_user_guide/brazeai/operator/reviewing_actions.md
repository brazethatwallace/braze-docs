---
nav_title: Revisar ações
article_title: Revisando ações do BrazeAI Operator<sup>TM</sup>
page_order: 2
description: "Aprenda como revisar e aprovar ações quando o BrazeAI Operator propõe mudanças no dashboard."
---

# Revisando ações do BrazeAI Operator {#reviewing-brazeai-operator-actions}

> Aprenda como revisar e aprovar ações quando o BrazeAI Operator<sup>TM</sup> propõe mudanças no dashboard.

![Operator apresentando cartões de ação sugeridos para revisão.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## Como os cartões de ação funcionam {#how-action-cards-work}

Quando o Operator propõe alterações no dashboard (como preencher campos de formulário, atualizar configurações ou gerar imagens), ele apresenta cada alteração como um cartão de ação para revisão.

1. **O Operator resume o plano:** O Operator explica o que planeja fazer antes de mostrar os cartões de ação.
2. **Cartões de ação individuais aparecem:** Cada alteração proposta é apresentada como um cartão separado que mostra o que o Operator deseja alterar ou fazer no dashboard. Para alterações em valores existentes, o valor anterior e o valor proposto são exibidos lado a lado para comparação.
3. **Revise e aprove:** Revise cada cartão e aprove ou recuse.
4. **A ação é executada:** As ações aprovadas são executadas na Braze. As ações recusadas não são aplicadas.

Se uma ação falhar após a aprovação, o Operator notifica você com detalhes sobre a falha.

### Disponibilidade {#availability}

O Operator pode propor cartões de ação em páginas compatíveis do dashboard, incluindo criadores de mensagens, páginas de lista e visão geral, configurações e outras superfícies onde ele pode atuar. Para uma cobertura representativa, consulte [O que você pode fazer com o Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities). Para canais de mensagens e editores compatíveis, consulte [Gerar mensagens]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages).

A cobertura é expandida regularmente. Se o Operator não puder atuar na página em que você está, ele fornece uma lista de etapas a seguir na interface.

## Modificar um plano {#modify-a-plan}

Para modificar o plano do Operator, primeiro aprove ou rejeite as ações pendentes. Em seguida, descreva a alteração desejada em uma nova mensagem no chat.

Ações aprovadas não podem ser desfeitas pelo Operator. Descreva a nova alteração para o Operator ou faça as mudanças manualmente no dashboard.

## Ações de aprovação automática {#auto-approve-actions}

O botão **Ações de aprovação automática** está localizado no painel de chat do Operator.

- **Ativado:** As ações sugeridas pelo Operator são executadas imediatamente, sem necessidade de aprovação manual, incluindo [navegar para uma página diferente]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard) para concluir sua solicitação. Algumas ações ainda exigem aprovação explícita por segurança, como gerar imagens ou fazer modificações em configurações no nível do espaço de trabalho.
- **Desativado (padrão):** Todas as ações propostas seguem o processo de revisão manual descrito, incluindo a navegação entre páginas — o Operator propõe a mudança e aguarda sua aprovação antes de levá-lo até lá.

![O botão de aprovação automática e o modal de confirmação no painel de chat do Operator.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

A aprovação automática é redefinida quando você atualiza a página, abre uma nova guia ou faz logout e login novamente. Navegar entre páginas no dashboard não a redefine. A aprovação automática pode ser desativada a qualquer momento.

Para informações sobre como restringir o acesso do Operator e auditar o uso pela equipe, consulte [Privacidade de dados e segurança]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security).