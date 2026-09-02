---
page_order: 6
nav_title: Prompts de soft push
article_title: Prompts de soft push para web
description: "Saiba como configurar prompts de soft push para o SDK or kit de desenvolvimento de software web da Braze antes do prompt nativo de permissão de notificação do navegador."
channel:
  - push notifications
---

# Prompts de soft push para web {#soft-push-prompts-for-web}

> Prompts de soft push são mensagens personalizadas exibidas antes do prompt nativo de permissão de notificação do navegador. Eles explicam por que os usuários devem ativar as notificações por push e podem melhorar as taxas de aceitação em comparação com a exibição do prompt do sistema na primeira visita. Este guia aborda como implementar prompts de soft push com o SDK or kit de desenvolvimento de software web da Braze, incluindo quando disparar o prompt, como personalizar o conteúdo da mensagem e práticas recomendadas para cronometrar a solicitação após os usuários entenderem o valor do push.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications/soft_push_prompts.md %}
{% endsdktab %}
{% endsdktabs %}

## Perguntas frequentes {#frequently-asked-questions}

### O que é um prompt de soft push? {#what-is-a-soft-push-prompt}

Um prompt de soft push é uma mensagem personalizada no app ou no site exibida antes da caixa de diálogo nativa de permissão de notificação do navegador. Ele explica o valor do push para que os usuários tenham mais probabilidade de aceitar quando o prompt do sistema aparecer.

### Quando devo exibir um prompt de soft push? {#when-should-i-show-a-soft-push-prompt}

Exiba um prompt de soft push depois que os usuários entenderem o valor do seu produto — por exemplo, após a integração ou uma ação significativa no app — e não no primeiro carregamento da página. Consulte as etapas do SDK or kit de desenvolvimento de software web neste guia para detalhes de implementação.