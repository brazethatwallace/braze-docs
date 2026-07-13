---
nav_title: Snapshots versus fluxos de eventos
article_title: Snapshots versus fluxos de eventos
page_order: 4
page_type: reference
description: "Este artigo de referência explica a diferença entre dados de snapshot e dados de fluxo de eventos, e como cada um deve ser estruturado e entregue ao BrazeAI Decisioning Studio."
---

# Snapshots versus fluxos de eventos {#snapshots-versus-event-streams}

> Os dados se enquadram em uma de duas categorias fundamentais: snapshots (estado) e fluxos de eventos (o que aconteceu). Entender essa distinção e aplicá-la corretamente é uma das coisas mais importantes que você pode fazer para garantir que seu agente do Decisioning Studio aprenda de forma eficaz.

## Dados de snapshot (estado) {#snapshot-data-state}

Um snapshot representa o estado de um cliente em um ponto específico no tempo. Ele responde à pergunta: "Como esse cliente está agora?"

Um snapshot é estático e agregado. Ele reflete o resultado acumulado de todas as mudanças até aquele momento. Isso é ideal para perfis de clientes, features computadas (por exemplo, "dias desde a última compra", "nível de fidelidade", "pontuação de churn").

### Campos obrigatórios {#required-fields}

| Campo | Finalidade |
|-------|---------|
| Identificador do cliente | Quem este registro descreve |
| Data do snapshot | Quando este snapshot foi capturado |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos obrigatórios" }

### Como os snapshots devem ser atualizados {#how-snapshots-should-be-updated}

- **Gatilho:** Baseado em tempo, não em eventos. Os snapshots devem ser gerados em uma programação fixa (por exemplo, diariamente), independentemente de o cliente ter tido alguma atividade naquele dia.
- **Escopo:** Cada atualização deve incluir todos os clientes relevantes, incluindo aqueles que não tiveram nenhum evento.
- **Método:** Adicione novos registros de snapshot ao dataset em vez de sobrescrever valores anteriores. Isso preserva o estado histórico para o treinamento do modelo.

### Consultar dados de snapshot para entrega diária {#query-snapshot-data-for-daily-delivery}

O Decisioning Studio executa seu pipeline de recomendação uma vez por dia. Ao entregar dados de snapshot, exporte o snapshot do dia anterior em cada execução do pipeline:

```sql
SELECT *
FROM snapshot_data
WHERE snapshot_date = {t-1} -- on pipeline run date t, export the snapshot from t-1
```

## Dados de fluxo de eventos (fluxo) {#event-stream-data-flow}

Um fluxo de eventos registra ações discretas conforme elas acontecem. Ele responde à pergunta: "O que esse cliente fez e quando?" Um fluxo de eventos é ideal para dados brutos, imutáveis, incrementais e cronológicos. Cada registro representa algo que aconteceu em um momento específico. Por exemplo, use esse fluxo de dados para registros de ativação, registros de engajamento (aberturas, cliques), eventos de conversão ou resgates de cupons.

### Campos obrigatórios

| Campo | Finalidade |
|-------|---------|
| Identificador do cliente | Sobre quem é este evento |
| Tipo de evento | O que aconteceu (por exemplo, ativação, conversão, clique) |
| Timestamp do evento | Quando o evento realmente ocorreu |
| Timestamp de criação | Quando este registro foi criado no seu sistema (veja a nota na seção a seguir) |
| Propriedades do evento | Metadados adicionais sobre o evento; quanto mais rico for, melhor o Decisioning Studio poderá vincular eventos ao longo da jornada do cliente |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos obrigatórios" }

{% alert important %}
O timestamp do evento e o timestamp de criação são campos diferentes e ambos são obrigatórios. O timestamp do evento registra quando a ação realmente aconteceu. O timestamp de criação registra quando a entrada de dados foi gravada no seu sistema, o que pode ser posterior devido a atrasos no processamento. Não confunda os dois.
{% endalert %}

### Como os fluxos de eventos devem ser atualizados {#how-event-streams-should-be-updated}

- **Gatilho:** Baseado em eventos. Novos registros são adicionados quando novos eventos ocorrem.
- **Escopo:** Apenas clientes que tiveram um evento recebem novos registros.
- **Método:** Registros existentes são imutáveis. Atualizações são sempre inserções de novos registros.

### Consultar dados de eventos para entrega diária {#query-event-data-for-daily-delivery}

Use `create_timestamp`, não `event_timestamp`, para fatiar as exportações diárias. Eventos às vezes são gravados no seu sistema após terem ocorrido (chegadas tardias). Se você fatiar por `event_timestamp`, esses registros que chegaram com atraso serão permanentemente perdidos.

```sql
-- Correct: use create_timestamp to ensure late-arriving events are captured
SELECT *
FROM events_data
WHERE DATE(create_timestamp) = {t-1} -- on run date t, export all records created yesterday
```

```sql
-- Incorrect: slicing on event_timestamp will permanently lose late-arriving events
SELECT *
FROM events_data
WHERE DATE(event_timestamp) = {t-1}
```

Por exemplo: se um evento ocorreu em 1º de janeiro, mas só foi gravado no seu sistema em 2 de janeiro, fatiar por `event_timestamp` em 2 de janeiro o perderia completamente. Fatiar por `create_timestamp` o captura corretamente.

## Para integrações nativas da Braze {#for-native-braze-integrations}

A Braze fornece dois mecanismos integrados que mapeiam diretamente para esses dois tipos de dados.

### Atributos personalizados: dados de snapshot {#custom-attributes-snapshot-data}

Os atributos personalizados armazenam o estado no nível do usuário em um ponto no tempo. Eles são o veículo correto para perfis de clientes e features computadas (por exemplo, `churn_score`, `total_purchases_last_30d`). Eles **não** são adequados para dados brutos de eventos, porque sobrescrevem em vez de acumular.

### Braze Currents: dados de fluxo de eventos {#braze-currents-event-stream-data}

O Braze Currents fornece dados brutos e imutáveis de fluxo de eventos. A tabela `USER_BEHAVIOR_CUSTOM_EVENTS` captura cada instância de um evento personalizado conforme ele ocorre, tornando-a a fonte correta para eventos de ativação, engajamento e conversão.

{% alert tip %}
Trate os atributos personalizados como a fonte do estado do cliente e o Braze Currents como a fonte dos eventos de comportamento do cliente. Não use atributos personalizados para passar dados brutos de eventos ao Decisioning Studio.
{% endalert %}

## Problemas comuns {#common-issues}

### Passar dados de eventos como snapshot {#pass-event-data-as-a-snapshot}

Agregar dados de eventos em campos de snapshot antes de enviá-los ao Decisioning Studio causa vários problemas:

- **Perda de granularidade:** Uma vez que os dados são agregados em um resumo diário no nível do cliente, os registros individuais de eventos se perdem. O Decisioning Studio não consegue reconstruí-los.
- **Timestamps imprecisos:** Um campo como "last_email_sent" informa a ocorrência mais recente, mas perde o histórico completo de eventos e torna a atribuição precisa impossível.
- **Atualizações fantasma:** Mesmo em dias em que nenhum evento ocorreu, o registro de snapshot é atualizado, criando entradas duplicadas que são difíceis de deduplicar.

Se você está usando a Braze, use exportações do Currents (não atributos personalizados) para entregar dados brutos de eventos ao Decisioning Studio.

### Atualizar dados de snapshot com base em um gatilho de evento {#update-snapshot-data-on-an-event-trigger}

Algumas implementações atualizam dados de snapshot apenas quando um evento ocorre — por exemplo, recalculando uma feature apenas quando um cliente faz uma compra. Isso faz com que features que dependem da passagem do tempo fiquem desatualizadas para clientes que não tiveram um evento recente.

Por exemplo, uma feature como `days_since_last_purchase` tem um valor correto diferente a cada dia. Se ela só é recalculada quando uma compra ocorre, ficará congelada em um valor incorreto para todos os clientes que não compraram recentemente. Sempre atualize dados de snapshot em uma programação baseada em tempo que cubra todos os clientes, todos os dias.