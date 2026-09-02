---
nav_title: FAQ
article_title: Perguntas frequentes sobre Currents
page_order: 4
page_type: reference
description: "Este artigo aborda algumas das perguntas mais frequentes que surgem ao configurar o Braze Currents."
tool: Currents
---

# Perguntas frequentes {#frequently-asked-questions}

> Esta página fornece respostas a algumas perguntas frequentes sobre o Currents.

## Posso exportar dados de Campaign ou Canvas para uma janela de datas específica? {#can-i-export-campaign-or-canvas-data-for-a-specific-date-window}

Para obter métricas de Campaign ou Canvas para um intervalo de datas definido, use uma das seguintes abordagens:

- {% multi_lang_include product_feedback_cta.md context="gap" feature="date-aligned campaign or Canvas exports for dashboard-style reporting outside standard API or interface de programação do aplicativo (API) windows" %}
- Chame os endpoints de [análise de dados de Campaign]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) ou [análise de dados de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) com os parâmetros `ending_at` e `length` (ou use [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) e [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics)) para dados de séries temporais.
- Transmita eventos para o seu data warehouse com o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) quando precisar de dados contínuos e consultáveis de engajamento com mensagem no Amazon S3, Azure Blob Storage ou outro destino compatível.

## Como edito uma integração ativa do Currents? {#how-do-i-edit-a-live-currents-integration}

Para alterar um conector ativo do Currents, abra a integração e selecione **Editar**. Sem a opção **Editar**, a interface da integração permanece somente leitura, e você não consegue modificar as configurações do conector apenas pelos ícones.

## Como a Braze lida com arquivos Avro do Azure Blob Storage após o upload? {#how-does-braze-handle-azure-blob-storage-avro-files-after-upload}

A Braze não modifica arquivos Avro no [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents) após a conclusão do upload. O Azure pode bloquear a exclusão de um blob enquanto um upload ainda estiver em andamento.

## Como obtenho dados históricos? {#how-do-i-get-historical-data}

Currents é um fluxo de dados em tempo real e ativo, o que significa que os eventos não podem ser reproduzidos. No entanto, você pode armazenar dados do Currents em um data warehouse como o [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) ou o [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents), para que possa agir sobre eventos passados como preferir. Os dados são retidos por 30 dias, mas para dados mais antigos, você pode consultar o [Snowflake]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/s3_to_snowflake).

## Por que o Currents envia dados no formato Avro, e não JSON? {#why-does-currents-output-data-in-the-avro-format-not-json}

Ao contrário do JSON, que não possui esquema nativo, o Avro suporta nativamente a evolução de esquemas. Você também se beneficia da capacidade de enviar arquivos Avro com menos largura de banda e economia de espaço de armazenamento, pois o Avro é altamente compactável.

## Como a Braze lida com a sobrecarga de arquivos? {#how-does-braze-handle-file-overhead}

Nós desenvolvemos um processo de Extração, Transformação e Carregamento (ETL), que permite extrair grandes volumes de dados de um banco de dados para colocá-los e armazená-los em outro.

## Onde devo armazenar esses dados para consulta? {#where-should-i-store-this-data-for-querying}

A Braze tem parcerias com vários data warehouses nos quais você pode armazenar seus dados para consulta. Recomendamos usar:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents).

## Qual é a confiabilidade dos dados do Currents? {#how-reliable-is-currents-data}

O Currents garante a entrega "pelo menos uma vez" (at-least-once), o que significa que eventos duplicados podem ocasionalmente ser gravados no seu bucket de armazenamento. Se o seu caso de uso exigir entrega exatamente uma vez, você pode deduplicar eventos usando o campo de identificador único (`id`) enviado com cada evento. Para saber mais, consulte [Semântica de entrega de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics).

## Com que frequência os dados são sincronizados com o Currents? {#how-often-is-data-synced-to-currents}

Os dados são transmitidos continuamente. A Braze envia um lote de eventos sempre que há um lote completo para enviar, ou a cada 5 minutos, o que ocorrer primeiro. Para conectores de alto volume, os dados chegam quase em tempo real. Para conectores de baixo volume, espere que os dados cheguem dentro de 5 a 30 minutos. Para mais detalhes, consulte [Limite de gravação Avro]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics#avro-write-threshold).

{% alert note %}
Se um dispositivo não estiver conectado à internet, pode haver um atraso na criação do evento. Isso é mais comum para eventos de mensagens no app, já que as mensagens no app podem ser disparadas offline.
{% endalert %}

## Como encontro quais eventos estão disponíveis para o Currents? {#how-do-i-find-which-events-are-available-for-currents}

Para uma lista completa dos eventos que o Currents registra, consulte os glossários de [Eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) e [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events). Você pode filtrar esses glossários por tipo de evento (como envios, entregas ou aberturas).

## Por que as contagens de eventos do Currents não correspondem às métricas do meu dashboard ou do relatório de engajamento? {#why-do-my-currents-event-counts-not-match-my-dashboard-or-engagement-report-metrics}

O Currents e o dashboard da Braze calculam determinadas métricas de maneiras diferentes, portanto não é esperado que haja correspondência exata entre os eventos do Currents e as métricas do dashboard.

**Cliques únicos:** Para e-mail, o dashboard rastreia cliques únicos ao longo de um período de sete dias e os mede por `dispatch_id`. O Currents registra cada evento de clique bruto. Para alinhar as contagens de cliques únicos baseadas no Currents com as métricas do dashboard, filtre por eventos em que `is_unique` seja `true`.

**Cancelamentos de inscrição:** A métrica *Unsub* do dashboard reflete cliques no link padrão de cancelamento de inscrição da Braze. Páginas personalizadas de cancelamento de inscrição não incrementam essa métrica, a menos que você atualize o usuário por meio da API or interface de programação do aplicativo (API). O evento `users.messages.email.Unsubscribe` do Currents é um evento de clique especializado que é disparado quando um usuário clica em um link de cancelamento de inscrição no corpo ou rodapé do e-mail, ou pelo cabeçalho list-unsubscribe. Ele não representa todas as mudanças de estado de inscrição de e-mail.

**Timestamps e fusos horários:** Todos os timestamps do Currents estão em UTC. As métricas do dashboard seguem o fuso horário da sua empresa. Agregar dados do Currents por dia do calendário sem converter para o fuso horário da sua empresa pode fazer com que as contagens caiam em intervalos de data diferentes dos que aparecem no dashboard.

**Eventos duplicados:** O Currents oferece entrega com garantia de pelo menos uma vez, o que significa que eventos duplicados podem ocasionalmente ser registrados. Faça a deduplicação pelo campo `id` único de cada evento antes de comparar os totais com as métricas do dashboard.

## Por que o `external_user_id` (esquema da Braze: `external_id`) no meu evento de abertura ou clique de e-mail no Currents difere do perfil de usuário no dashboard da Braze? {#why-does-the-external_user_id-braze-schema-external_id-in-my-currents-email-open-or-click-event-differ-from-the-user-profile-in-the-braze-dashboard}

- **No dashboard da Braze:** Quando um usuário associado a um endereço de e-mail abre ou clica em um e-mail, todos os perfis de usuário que compartilham esse endereço de e-mail são marcados como tendo aberto ou clicado naquele e-mail. Para saber mais, consulte [O que acontece quando um e-mail é enviado e vários perfis têm o mesmo endereço de e-mail?]({{site.baseurl}}/user_guide/channels/email/faq#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address).
- **No Currents:** Essa mesma abertura ou clique é armazenada em um único perfil. A Braze atribui ao perfil que foi originalmente direcionado para o envio, caso esse perfil ainda compartilhe o endereço de e-mail. Caso contrário, a Braze atribui a um perfil selecionado aleatoriamente entre aqueles que compartilham o endereço de e-mail.

Por conta disso, o valor de `external_user_id` (chamado `external_id` na tabela de mapeamento do esquema da Braze) em um evento de abertura ou clique de e-mail no Currents pode não corresponder ao perfil de usuário esperado quando você compara o Currents com o dashboard da Braze.

## Todos os eventos de envio são registrados no Currents? {#are-all-send-events-logged-to-currents}

Todos os eventos são registrados no Currents. Não há cenários em que um evento seria intencionalmente suprimido do fluxo do Currents.

## Os dados podem ser corrompidos no Currents? {#can-data-be-corrupted-in-currents}

Em circunstâncias normais, os dados do Currents não são corrompidos. Embora sempre exista a possibilidade de um problema raro, não há condições conhecidas em que os dados seriam sistematicamente corrompidos.

## Por que vejo dados de eventos personalizados com datas anteriores à configuração da minha integração com o Currents? {#why-do-i-see-custom-event-data-dated-before-my-currents-integration-was-set-up}

A Braze não preenche retroativamente eventos no Currents. No entanto, eventos personalizados podem ser registrados com um registro de data e hora no passado (por exemplo, se um dispositivo estava offline quando o evento ocorreu e sincronizou depois). Nesses casos, o registro de data e hora do evento reflete quando o evento ocorreu originalmente, o que pode ser antes da configuração da integração com o Currents.

## Quais identificadores de usuário são incluídos nos eventos do Currents? {#what-user-identifiers-are-included-in-currents-events}

Eventos de engajamento com mensagem (envios, aberturas, cliques e assim por diante) incluem o ID de usuário da Braze (`user_id`) e, quando presente no perfil, o identificador externo (`external_user_id` nas cargas úteis de eventos, chamado de `external_id` na tabela de mapeamento de esquema da Braze). Alguns eventos de engajamento com mensagens de e-mail também incluem `email_address`. Atributos personalizados não são incluídos.

Se você está direcionando dados do Currents para um data warehouse ou CRM e precisa fazer a junção com dados de perfil, realize essa junção no seu sistema downstream usando `user_id` ou `external_user_id`.

## Posso incluir atributos personalizados nos eventos de envio do Currents? {#can-i-include-custom-attributes-in-currents-send-events}

Não. O Currents não inclui atributos personalizados nos eventos de envio. O Currents registra eventos personalizados e eventos de engajamento com mensagem. Para uma lista completa dos campos disponíveis, consulte os [glossários de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary).

## O Currents inclui tags de Campaign ou Canvas, ou pares de chave-valor? {#does-currents-include-campaign-or-canvas-tags-or-key-value-pairs}

Não. O Currents não inclui tags de Campaign ou Canvas nem pares de chave-valor no nível da mensagem. Para recuperar dados de tags, use a [REST or transferir estado representacional API or interface de programação do aplicativo (API) de exportação]({{site.baseurl}}/api/endpoints/export). Como alternativa, você pode usar um canal de webhook em uma Campaign para enviar dados de tags ou pares de chave-valor para o seu próprio endpoint, usando [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) para modelar os valores.

## Como a Braze notifica os clientes sobre mudanças no Currents? {#how-does-braze-notify-customers-of-changes-to-currents}

Na rara circunstância em que ocorrem alterações incompatíveis, a Braze envia um e-mail antecipado para o contato em qualquer integração ativa e para todos os administradores com integrações ativas do Currents que usaram o dashboard nos últimos 30 dias. Para alterações não incompatíveis, como novos eventos ou novos campos em um evento existente, a Braze não envia uma notificação. Você pode consultar o [changelog do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) para ver as alterações mais recentes.

## Qual capacidade de armazenamento eu preciso para os dados do Currents? {#how-much-storage-do-i-need-for-currents-data}

Os requisitos de armazenamento dependem do volume de eventos e dos tipos de eventos que você está exportando. A Braze fornece [exemplos de eventos no formato Avro](https://github.com/appboy/currents-examples/tree/master/sample-data) que você pode usar para estimar os tamanhos de arquivo para o seu caso de uso.

## Por que o nome da campanha ou da etapa do Canvas aparece como `NULL` nos meus dados do Currents? {#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data}

Quando você cria uma nova Campaign ou Canvas, o nome pode levar algum tempo para se propagar por todos os sistemas da Braze. Eventos enviados pelo Currents durante esse intervalo podem ter `NULL` nos campos de nome (como `campaign_name` ou `canvas_step_name`). Isso também é esperado se o nome foi modificado pouco antes de os eventos serem registrados. Para evitar isso, aguarde algum tempo após criar ou renomear uma Campaign ou etapa do Canvas antes de realizar o envio.

## Por que os eventos de término de sessão estão atrasados ou ausentes no Currents? {#why-are-session-end-events-delayed-or-missing-in-currents}

Os eventos de término de sessão seguem o cronograma normal de upload do SDK or kit de desenvolvimento de software. O SDK or kit de desenvolvimento de software da Braze armazena os dados de sessão localmente e os envia periodicamente com base na qualidade da rede — por exemplo, aproximadamente a cada 10 segundos em uma conexão forte. Até que o SDK or kit de desenvolvimento de software faça o upload do evento, ele não aparece no Currents.

Se um usuário forçar o encerramento do app ou ficar offline antes do próximo envio, o evento de término de sessão pode chegar com atraso ou simplesmente não chegar. No iOS, os eventos de término de sessão geralmente não são enviados até que o app seja reaberto, porque o SDK or kit de desenvolvimento de software não consegue enviar dados enquanto o app está em segundo plano.

Quando você precisar de limites de sessão mais oportunos no Currents, chame `requestImmediateDataFlush()` em pontos do ciclo de vida, como quando o app vai para segundo plano ou retorna ao primeiro plano. Para saber mais, consulte [Upload e download de dados]({{site.baseurl}}/developer_guide/getting_started/sdk_overview#data-upload-and-download) e [Término de sessão e início de sessão com timestamps semelhantes (iOS)]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log#session-end-and-session-start-have-similar-timestamps-ios).

## O que acontece se meu bucket de armazenamento estiver indisponível quando o Currents tentar gravar dados? {#what-happens-if-my-storage-bucket-is-unavailable-when-currents-tries-to-write-data}

Se o seu bucket de armazenamento estiver indisponível no momento da transferência de dados, esses dados serão perdidos. A Braze não consegue preencher retroativamente eventos que não foram entregues com sucesso. Para evitar perda de dados, garanta que seu bucket de armazenamento esteja disponível e configurado corretamente o tempo todo.

## Por que vejo mensagens de limite de direitos ao criar ou editar uma integração do Currents? {#why-do-i-see-entitlement-limit-messages-when-creating-or-editing-a-currents-integration}

O Currents usa pools de direitos separados para diferentes capacidades de conectores:

- **Engagement Events**: necessário para criar ou fazer upgrade de um conector padrão do Currents.
- **Customer Behavior Events**: necessário para ativar **Track Customer Behavior and User Events**.
- **User Profiles and Attributes**: necessário para ativar **Track user profiles and attributes**.

Se algum pool estiver esgotado, a Braze exibe um aviso de direitos e bloqueia essa ação. Entre em contato com o gerente da sua conta Braze para solicitar direitos adicionais ou ajuda para ajustar sua configuração.

## Com que frequência a versão do Currents no caminho de armazenamento muda? {#how-often-does-the-currents-version-in-the-storage-path-change}

O Segment or segmento or segmento `version=<currents_version>` no caminho de armazenamento avança a cada lançamento do Currents em uma cadência mensal (por exemplo, de `version=6` para `version=7`). Recomendamos a leitura de arquivos de forma recursiva a partir do caminho raiz, em vez de codificar um Segment or segmento or segmento de versão específico, para que seu pipeline capture automaticamente os dados após uma mudança de versão. Para mais detalhes sobre o formato do caminho, consulte [Semântica de entrega de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics). Para um histórico de alterações por versão, consulte o [changelog do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs).

## Por que `campaign_id` ou `canvas_id` estão ausentes em um evento de engajamento com mensagem? {#why-are-campaign_id-or-canvas_id-missing-from-a-message-engagement-event}

Dependendo do tipo e do contexto do evento, um evento de engajamento com mensagem pode não estar vinculado a uma Campaign ou etapa do Canvas específica. Nesses casos, `campaign_id`, `canvas_id` e os campos de nome relacionados podem ser omitidos da carga útil do evento. Se você não encontrar esses campos em um determinado evento, verifique se o tipo e o contexto desse evento normalmente incluem identificadores de Campaign ou Canvas.

## Por que os timestamps do Currents são limitados à precisão de segundos? {#why-are-currents-timestamps-limited-to-second-precision}

O campo `time` nos eventos do Currents é armazenado como um inteiro de 32 bits e, portanto, é limitado à precisão de segundos. Alguns eventos também incluem um campo de timestamp separado com precisão de milissegundos em 64 bits. Consulte o [glossário de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary) para ver os campos disponíveis em cada tipo de evento.

## Por que o evento `users.canvas.Conversion` do Currents tem um horário diferente do Canvas? {#why-does-the-userscanvasconversion-event-from-currents-have-a-different-time-than-the-canvas}

O horário do evento `users.canvas.Conversion` no Currents reflete a janela de conversão total — a duração do Canvas mais o prazo de conversão — medida a partir da entrada no Canvas.

## O que acontece quando relatórios de engajamento são enviados para o S3? {#what-happens-when-engagement-reports-are-sent-to-s3}

Se as credenciais do S3 estiverem configuradas para exportação de dados, mas não para o Currents, a Braze faz o upload dos relatórios de engajamento para o bucket S3 especificado. O usuário listado no campo **Send Report To** recebe um e-mail com um link para o relatório no S3.

## Dados de usuários anônimos podem ser enviados para a Amplitude por meio do Braze Currents? {#can-anonymous-user-data-be-sent-to-amplitude-through-braze-currents}

Dados de usuários anônimos, identificados por `device_id`, podem ser enviados para a Amplitude por meio do Currents. Isso requer a ativação do recurso pela equipe de conta da Braze.

## Como as impressões do grupo de controle para Content Cards e mensagens no app são registradas no Currents? {#how-are-control-group-impressions-for-content-cards-and-in-app-messages-logged-in-currents}

Quando um usuário é atribuído a um grupo de controle para uma Campaign de Content Cards ou mensagem no app, o Currents emite um evento `users.campaigns.EnrollInControl` em vez de um evento de impressão.

## O que acontece quando você direciona um usuário inexistente pela API or interface de programação do aplicativo (API)? {#what-happens-when-you-target-a-non-existent-user-through-the-api}

Quando você direciona um usuário que não existe, a API or interface de programação do aplicativo (API) retorna uma resposta `200`, mas o envio é cancelado com o resultado "Unknown external ID". Nenhum evento do Currents é gerado para esse envio. Observe que o parâmetro `send_to_existing_only` tem o valor padrão `true`, então envios para usuários desconhecidos são silenciosamente ignorados, a menos que você defina explicitamente como `false`.