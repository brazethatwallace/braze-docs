---
nav_title: Relatórios
article_title: Relatórios de e-mail
page_order: 21
description: "Este artigo de referência aborda os diferentes componentes dos relatórios de e-mail e onde encontrá-los no dashboard."
tool:
  - Reports
channel:
  - email

---

# Relatórios de e-mail {#email-reporting}

> Este artigo aborda os diferentes componentes dos seus relatórios de e-mail e onde encontrá-los no dashboard.

{% multi_lang_include analytics/campaign_analytics.md channel="email" %}

## Solução de problemas {#troubleshooting}

### E-mails com bounce {#bounced-emails}

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy:** Tente outro endereço, reengaje por outro canal ou remova o endereço da lista de supressão apenas para seus próprios endereços de teste. Evite remover supressões de usuários reais, pois isso pode prejudicar a reputação.
- **Mailbox full / invalid account:** Geralmente é um sinal de qualidade da lista. Priorize usuários que abriram ou clicaram recentemente (por exemplo, nos últimos 30 a 60 dias) enquanto você limpa endereços inativos ou inválidos.

### Domínios inválidos {#invalid-domains}

Erros como `unable to get mx info` geralmente significam que muitos destinatários usam domínios incorretos (por exemplo, erros de digitação). Segmente, exporte, corrija e reimporte esses perfis.

### IPs com throttling {#throttled-ips}

Você pode ver a mensagem `Email was deferred due to the following reason(s): [IPs were throttled by recipient server]` no [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) quando um provedor de caixa de e-mail reduz ou bloqueia temporariamente a entrega do seu IP por causa de volume, reputação ou ambos. A Braze tenta reenviar mensagens adiadas; se os adiamentos se concentrarem por esse motivo, é comum ver soft bounces elevados junto com eles.

Esse padrão geralmente significa que você está enviando mais rápido do que o provedor de caixa de e-mail aceita para a sua reputação atual. Além de melhorar o engajamento e a qualidade da lista, use o [limite de taxa de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) para limitar a velocidade com que as mensagens saem da Braze para uma Campaign ou Canvas. Isso ajuda a reduzir o throttling enquanto você trabalha com sua equipe de entregabilidade em correções de longo prazo.

Se o throttling persistir para domínios específicos, reduza o volume para esses domínios e entre em contato com o suporte de entregabilidade da Braze para orientação.