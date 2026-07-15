---
nav_title: Princípios gerais
article_title: Princípios gerais de dados para o Decisioning Studio
page_order: 1
page_type: reference
description: "Este artigo de referência aborda os princípios gerais de dados que se aplicam a todos os ativos de dados usados pelo BrazeAI Decisioning Studio."
---

# Princípios gerais {#general-principles}

> Dados bem estruturados são a base de um agente eficaz do Decisioning Studio. Antes de mergulhar nos requisitos específicos de cada ativo, é útil entender os quatro princípios fundamentais que se aplicam a todos os dados enviados ao Decisioning Studio. Violações de qualquer um desses princípios estão entre as causas mais comuns de queda no desempenho do modelo.

## Um identificador de cliente consistente em todos os ativos {#one-consistent-customer-identifier-across-all-assets}

Cada ativo de dados (perfis de clientes, ativações, engajamentos, conversões) deve referenciar o mesmo identificador de cliente. Deve existir exatamente um identificador primário que identifique de forma única e consistente cada cliente em todos os ativos.

| Requisito | Implicação se violado |
|-------------|------------------------|
| Um identificador de cliente único deve estar presente em cada ativo | Se ativos diferentes usam sistemas de ID diferentes (por exemplo, um ID de warehouse para features, mas um ID de plataforma para ativações), o mecanismo do Decisioning Studio não consegue uni-los de forma confiável. Isso quebra o ciclo de feedback e prejudica tanto o treinamento do modelo quanto a precisão dos relatórios. Se o mapeamento entre os dois sistemas de ID for muitos-para-muitos em vez de um-para-muitos, as falhas de integridade de dados resultantes podem ser graves. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Um identificador de cliente consistente em todos os ativos" }

Consulte [Usar o ID externo da Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/braze_external_id) para orientações sobre qual identificador usar.

## Dados de eventos devem ser enviados como um fluxo incremental, não como um snapshot {#event-data-must-be-passed-as-an-incremental-stream-not-as-a-snapshot}

Eventos, como conversões, engajamentos e ativações, representam coisas discretas que aconteceram em um momento específico no tempo. Eles devem ser entregues ao Decisioning Studio como um fluxo incremental (somente adição) de registros individuais, não como um snapshot agregado.

| Requisito | Implicação se violado |
|-------------|------------------------|
| Dados de eventos devem ser estruturados como registros individuais com timestamp e entregues de forma incremental | Quando dados de eventos são agregados em um snapshot (por exemplo, armazenando um atributo de "hora do último envio" em vez de registros individuais de envio), você perde a precisão do momento de cada evento. Isso torna impossível atribuir resultados com precisão a decisões específicas, quebrando o ciclo de feedback que o modelo precisa para aprender. Sem timestamps precisos de eventos, não é possível saber exatamente quando uma conversão aconteceu ou qual recomendação a desencadeou. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dados de eventos devem ser enviados como um fluxo incremental, não como um snapshot" }

Consulte [Snapshots versus fluxos de eventos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams) para uma explicação completa da distinção e exemplos de padrões corretos e incorretos.

## Dados de snapshot devem ser atualizados em uma programação regular baseada em tempo {#snapshot-data-must-be-updated-on-a-regular-time-driven-schedule}

Dados de snapshot (como perfis de clientes e features) representam o estado atual de um cliente em um determinado momento. Atualizações de dados de snapshot devem ser orientadas por uma programação regular (por exemplo, diária), não por gatilhos de eventos.

| Requisito | Implicação se violado |
|-------------|------------------------|
| Snapshots devem ser atualizados para todos os clientes em uma programação regular, independentemente de o cliente ter tido um evento naquele dia | Se atualizações de snapshot são disparadas apenas quando um evento ocorre, features que dependem da passagem do tempo (como "dias desde a última compra" ou "dias desde a inscrição") ficarão desatualizadas para clientes que não tiveram um evento recente. O modelo estará treinando com valores de features desatualizados, o que reduz sua capacidade de fazer recomendações precisas e oportunas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dados de snapshot devem ser atualizados em uma programação regular baseada em tempo" }

## Todos os ativos devem atender a requisitos mínimos de qualidade e integridade de dados {#all-assets-must-meet-minimum-data-quality-and-integrity-requirements}

Além da estrutura, os dados em si devem ser internamente consistentes e completos o suficiente para serem úteis.

| Requisito | Implicação se violado |
|-------------|------------------------|
| Cada ativo deve conter os campos necessários para estabelecer uma chave primária e, quando aplicável, chaves de junção com outros ativos. Registros duplicados devem ser removidos ou deduplicados antes da ingestão. | Registros duplicados ou não correspondentes adicionam ruído ao treinamento do modelo e podem causar atribuição incorreta. Chaves ausentes impedem o mecanismo de vincular eventos ao longo da jornada do cliente, desde a recomendação até a conversão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Todos os ativos devem atender a requisitos mínimos de qualidade e integridade de dados" }

Para dados de fluxo de eventos especificamente, cada registro deve incluir no mínimo:

**Campos obrigatórios:**
- Identificador do cliente
- Timestamp de quando o evento ocorreu (não de quando o registro foi criado no seu sistema; são coisas diferentes; consulte [Snapshots versus fluxos de eventos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams) para entender por que isso importa)
- Timestamp de quando o registro foi criado no seu sistema (usado para fatiar exportações incrementais de forma confiável)
- Tipo de evento
- Campos suficientes para filtrar até os eventos específicos que você deseja

**Campos recomendados:**
- Metadados adicionais do evento que permitam correspondência confiável entre tipos de eventos (por exemplo, vincular um evento de conversão à ativação específica que o precedeu)