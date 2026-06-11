---
nav_title: Relatórios
article_title: Relatórios de Content Cards
page_order: 21
description: "Este artigo de referência fornece uma visão geral das diferentes métricas de relatórios e opções de análise de dados de Content Cards disponíveis no dashboard da Braze."
channel:
  - content cards
tool:
  - Reports

---

# Relatórios de Content Cards {#content-card-reporting}

> Este artigo de referência fornece uma visão geral das diferentes métricas de relatórios e opções de análise de dados de Content Cards disponíveis no dashboard da Braze.

## Quando os envios são registrados {#when-sends-are-logged}

O momento em que um evento _Sent_ é registrado para Content Cards depende do tipo de entrega e da configuração de **Card Creation**.

### Entrega agendada {#scheduled-delivery}

Para Content Cards agendados, o momento do evento _Sent_ depende da configuração de **Card Creation**:

- **At campaign launch:** O envio é registrado no horário de envio agendado, quando o cartão é gravado no feed do usuário. Isso acontece independentemente de o usuário ter aberto o app ou visualizado o cartão.
- **At first impression:** O envio é registrado na primeira vez que o app solicita o cartão após o horário de envio agendado, quando o cartão é criado sob demanda.

Se a sua Campaign estiver configurada para usar **At first impression** (recomendado), a contagem de _Sent_ na análise de dados da Campaign cresce gradualmente à medida que os apps individuais solicitam o cartão. Se o app nunca solicitar um cartão (por exemplo, se o usuário nunca abrir o app) antes de o cartão expirar, nenhum envio será registrado e o cartão nunca será entregue. Se a sua Campaign estiver configurada para usar **At campaign launch**, a contagem de _Sent_ na análise de dados da Campaign aumenta abruptamente no horário agendado.

### Entrega baseada em ação {#action-based-delivery}

Para Content Cards baseados em ação, o envio é registrado logo após o usuário realizar a ação de gatilho, quando o cartão é gravado no feed. Isso acontece independentemente de o usuário ter visualizado o cartão.

### Filtros de Campaigns recebidas e redirecionamento {#campaigns-received-and-retargeting-filters}

Independentemente do tipo de entrega ou da configuração de **Card Creation**, uma Campaign de Content Cards aparece no perfil do usuário em **Campaigns Received** somente após ele ter realmente visualizado o cartão no app. Os filtros de redirecionamento **Last Received Any Message** e **Last Received Campaign** são atualizados no momento da visualização pelo mesmo motivo.

{% multi_lang_include analytics/campaign_analytics.md channel="Content Card" %}