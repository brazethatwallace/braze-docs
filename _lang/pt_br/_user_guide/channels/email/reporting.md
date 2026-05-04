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

# Relatórios de e-mail

> Este artigo aborda os diferentes componentes dos seus relatórios de e-mail e onde encontrá-los no dashboard.

{% multi_lang_include analytics/campaign_analytics.md channel="email" %}

## Solução de problemas

### E-mails com bounce

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy:** Tente outro endereço, reengaje por outro canal ou remova o endereço da lista de supressão apenas para seus próprios endereços de teste. Evite remover supressões de usuários reais, pois isso pode prejudicar a reputação.
- **Mailbox full / invalid account:** Geralmente é um sinal de qualidade da lista. Priorize usuários que abriram ou clicaram recentemente (por exemplo, nos últimos 30 a 60 dias) enquanto você limpa endereços inativos ou inválidos.

### Domínios inválidos

Erros como `unable to get mx info` geralmente significam que muitos destinatários usam domínios incorretos (por exemplo, erros de digitação). Segmente, exporte, corrija e reimporte esses perfis.

### IPs com throttling

Se um servidor de destinatário aplicar throttling ao seu IP, reduza o volume para esse domínio, melhore o engajamento e entre em contato com o suporte de entregabilidade caso o throttling persista.