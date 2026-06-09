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

### Posso exportar dados de Campaign ou Canvas para um período específico? {#can-i-export-campaign-or-canvas-data-for-a-specific-date-window}

Para obter métricas de Campaign ou Canvas em um intervalo de datas definido, use uma das seguintes abordagens:

- Envie uma [solicitação de produto](https://portal.braze.com/) para exportações alinhadas por data quando precisar de relatórios no estilo do dashboard fora das janelas padrão da API.
- Chame os endpoints de [análise de dados de Campaign]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) ou [análise de dados de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) com os parâmetros `ending_at` e `length` (ou use [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) e [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/)) para dados de séries temporais.
- Transmita eventos para o seu data warehouse com o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) quando precisar de dados contínuos e consultáveis de engajamento com mensagem no Amazon S3, Azure Blob Storage ou outro destino compatível.

### Como edito uma integração ativa do Currents? {#how-do-i-edit-a-live-currents-integration}

Para alterar um conector ativo do Currents, abra a integração e clique em **Editar** no canto inferior esquerdo da página. Sem o botão **Editar**, a interface da integração permanece somente leitura e você não consegue modificar as configurações do conector apenas pelos ícones.

### Como a Braze lida com arquivos Avro do Azure Blob Storage após o upload? {#how-does-braze-handle-azure-blob-storage-avro-files-after-upload}

A Braze não modifica arquivos Avro no [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) após a conclusão do upload. O Azure pode bloquear a exclusão de um blob enquanto um upload ainda estiver em andamento.

### Como faço para obter dados históricos? {#how-do-i-get-historical-data}

O Currents é um fluxo de dados ao vivo e em tempo real, o que significa que os eventos não podem ser reproduzidos. No entanto, é possível armazenar os dados do Currents em um data warehouse, como o [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) ou o [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/), para que você possa agir com base em eventos passados conforme achar necessário. Os dados são retidos por 30 dias, mas para obter mais dados históricos, você pode consultar o [Snowflake]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/s3_to_snowflake/).

### Por que o Currents gera dados no formato Avro, e não em JSON? {#why-does-currents-output-data-in-the-avro-format-not-json}

O Avro, ao contrário do JSON sem esquema, suporta nativamente a evolução do esquema. Você também se beneficiará da capacidade de enviar arquivos Avro com menos largura de banda e economizar espaço de armazenamento, pois o Avro é altamente compactável.

### Como a Braze lida com a sobrecarga de arquivos? {#how-does-braze-handle-file-overhead}

Criamos um processo de extração, transformação e carga (ETL), que permite extrair grandes quantidades de dados de um banco de dados para colocá-los e armazená-los em outro.

### Onde devo armazenar esses dados para consulta? {#where-should-i-store-this-data-for-querying}

A Braze tem parceria com vários data warehouses nos quais você pode armazenar seus dados para consulta. Recomendamos o uso de:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).

### Qual é a confiabilidade dos dados do Currents? {#how-reliable-is-currents-data}

O Currents garante a entrega "pelo menos uma vez" (at-least-once), o que significa que eventos duplicados podem ser gravados ocasionalmente no seu bucket de armazenamento. Se o seu caso de uso exigir entrega exatamente uma vez, você pode deduplicar eventos usando o campo de identificador único (`id`) enviado com cada evento. Para mais informações, consulte [Semântica de entrega de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/).

### Com que frequência os dados são sincronizados com o Currents? {#how-often-is-data-synced-to-currents}

Os dados são transmitidos continuamente. A Braze envia um lote de eventos sempre que há um lote completo para enviar, ou a cada 5 minutos, o que ocorrer primeiro. Para conectores de alto volume, os dados chegam quase em tempo real. Para conectores de baixo volume, espere que os dados cheguem entre 5 e 30 minutos. Para mais informações, consulte [Limite de gravação Avro]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/#avro-write-threshold).

{% alert note %}
Se um dispositivo não estiver conectado à internet, pode haver um atraso na criação do evento. Isso é mais comum para eventos de mensagens no app, já que mensagens no app podem ser disparadas offline.
{% endalert %}

### Como descubro quais eventos estão disponíveis para o Currents? {#how-do-i-find-which-events-are-available-for-currents}

Para uma lista completa dos eventos que o Currents registra, consulte os glossários de [Eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) e [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/). Você pode filtrar esses glossários por tipo de evento (como envios, entregas ou aberturas).

### Por que o `external_id` no meu evento de abertura ou clique de e-mail do Currents é diferente do perfil de usuário no dashboard da Braze? {#why-does-the-external_id-in-my-currents-email-open-or-click-event-differ-from-the-user-profile-in-the-braze-dashboard}

- **No dashboard da Braze:** Quando um usuário associado a um endereço de e-mail abre ou clica em um e-mail, todos os perfis de usuário que compartilham esse endereço de e-mail são marcados como tendo aberto ou clicado nesse e-mail. Para mais informações, consulte [O que acontece quando um e-mail é enviado e vários perfis têm o mesmo endereço de e-mail?]({{site.baseurl}}/user_guide/channels/email/faq/#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address).
- **No Currents:** Essa mesma abertura ou clique é armazenado em um único perfil. A Braze atribui o evento ao perfil que foi originalmente direcionado para o envio, caso esse perfil ainda compartilhe o endereço de e-mail. Caso contrário, a Braze atribui o evento a um perfil selecionado aleatoriamente entre aqueles que compartilham o endereço de e-mail.

Por isso, o `external_id` em um evento de abertura ou clique de e-mail do Currents pode não corresponder ao perfil de usuário que você espera ao comparar o Currents com o dashboard da Braze.

### Todos os eventos de envio são registrados no Currents? {#are-all-send-events-logged-to-currents}

Todos os eventos são registrados no Currents. Não há cenários em que um evento seria intencionalmente suprimido do fluxo do Currents.

### Os dados podem ser corrompidos no Currents? {#can-data-be-corrupted-in-currents}

Em circunstâncias normais, os dados do Currents não são corrompidos. Embora sempre exista a possibilidade de um problema raro, não há condições conhecidas em que os dados seriam sistematicamente corrompidos.

### Por que vejo dados de eventos personalizados com datas anteriores à configuração da minha integração com o Currents? {#why-do-i-see-custom-event-data-dated-before-my-currents-integration-was-set-up}

A Braze não preenche retroativamente eventos no Currents. No entanto, eventos personalizados podem ser registrados com um timestamp passado (por exemplo, se um dispositivo estava offline quando o evento ocorreu e sincronizou depois). Nesses casos, o timestamp do evento reflete quando o evento ocorreu originalmente, o que pode ser antes da configuração da integração com o Currents.

### Posso incluir atributos personalizados nos eventos de envio do Currents? {#can-i-include-custom-attributes-in-currents-send-events}

Não. O Currents não inclui atributos personalizados nos eventos de envio. O Currents registra eventos personalizados e eventos de engajamento com mensagem. Para uma lista completa dos campos disponíveis, consulte os [glossários de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/).

### O Currents inclui tags de Campaign ou pares chave-valor? {#does-currents-include-campaign-tags-or-key-value-pairs}

Não. O Currents não inclui tags de Campaign ou pares chave-valor no nível da mensagem. Como alternativa, você pode usar um canal de webhook na Campaign para enviar essas informações ao seu próprio endpoint, usando [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) para modelar os dados de tags e pares chave-valor.

### Como a Braze notifica os clientes sobre mudanças no Currents? {#how-does-braze-notify-customers-of-changes-to-currents}

Quando ocorrem mudanças no Currents (como novos campos de evento ou tipos de evento), a Braze envia um e-mail para todos os clientes com integrações ativas do Currents que usaram o dashboard nos últimos 30 dias. Você também pode consultar o [changelog do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/) para ver as últimas alterações.

### Quanto armazenamento eu preciso para os dados do Currents? {#how-much-storage-do-i-need-for-currents-data}

Os requisitos de armazenamento dependem do volume de eventos e dos tipos de eventos que você está exportando. A Braze fornece [exemplos de eventos no formato Avro](https://github.com/appboy/currents-examples/tree/master/sample-data) que você pode usar para estimar o tamanho dos arquivos para o seu caso de uso.

### Por que o nome da Campaign ou o nome da etapa do Canvas está `NULL` nos meus dados do Currents? {#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data}

Quando você cria uma nova Campaign ou Canvas, o nome pode levar algum tempo para se propagar por todos os sistemas da Braze. Eventos enviados pelo Currents durante esse intervalo podem ter `NULL` nos campos de nome (como `campaign_name` ou `canvas_step_name`). Isso também é esperado se o nome foi modificado pouco antes dos eventos serem registrados. Para evitar isso, aguarde algum tempo após criar ou renomear uma Campaign ou etapa do Canvas antes de enviar.

### Por que os eventos de fim de sessão estão atrasados ou ausentes no Currents? {#why-are-session-end-events-delayed-or-missing-in-currents}

Os eventos de fim de sessão seguem o cronograma normal de upload do SDK. O SDK da Braze armazena os dados de sessão localmente em cache e os envia periodicamente com base na qualidade da rede — por exemplo, a cada 10 segundos em uma conexão estável. Até que o SDK faça o upload do evento, ele não aparece no Currents.

Se um usuário forçar o encerramento do app ou ficar offline antes do próximo envio, o evento de fim de sessão pode chegar com atraso ou não chegar. No iOS, os eventos de fim de sessão geralmente não são enviados até que o app seja reaberto, pois o SDK não consegue enviar dados enquanto o app está em segundo plano.

Quando você precisar de limites de sessão mais precisos no Currents, chame `requestImmediateDataFlush()` em pontos do ciclo de vida, como quando o app vai para segundo plano ou retorna ao primeiro plano. Para mais informações, consulte [Upload e download de dados]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/#data-upload-and-download) e [Fim de sessão e início de sessão com timestamps semelhantes (iOS)]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log/#session-end-and-session-start-have-similar-timestamps-ios).

### O que acontece se meu bucket de armazenamento estiver indisponível quando o Currents tentar gravar dados? {#what-happens-if-my-storage-bucket-is-unavailable-when-currents-tries-to-write-data}

Se o seu bucket de armazenamento estiver indisponível no momento da transferência de dados, esses dados serão perdidos. A Braze não consegue preencher retroativamente eventos que não foram entregues com sucesso. Para evitar perda de dados, certifique-se de que seu bucket de armazenamento esteja disponível e configurado corretamente o tempo todo.

### Por que vejo "You do not have any remaining Customer Behavior Events entitlements" ao editar minha integração com o Currents? {#why-do-i-see-you-do-not-have-any-remaining-customer-behavior-events-entitlements-when-editing-my-currents-integration}

Essa mensagem pode aparecer quando você atualiza uma integração existente do Currents e seu espaço de trabalho atingiu o limite de direitos para eventos de comportamento do cliente. Entre em contato com o gerente de conta da Braze para solicitar um aumento de direitos ou ajustar sua configuração.

### Com que frequência a versão do Currents no caminho de armazenamento muda? {#how-often-does-the-currents-version-in-the-storage-path-change}

O segmento `version=<currents_version>` no caminho de armazenamento avança a cada lançamento do Currents em uma cadência mensal (por exemplo, de `version=6` para `version=7`). Recomendamos ler os arquivos recursivamente a partir do caminho raiz em vez de codificar um segmento de versão específico, para que seu pipeline capture automaticamente os dados após uma mudança de versão. Para mais informações sobre o formato do caminho, consulte [Semântica de entrega de eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/). Para um histórico de alterações por versão, consulte o [changelog do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/).

### Por que `campaign_id` ou `canvas_id` estão ausentes em um evento de engajamento com mensagem? {#why-are-campaign_id-or-canvas_id-missing-from-a-message-engagement-event}

Dependendo do tipo de evento e do contexto, um evento de engajamento com mensagem pode não estar vinculado a uma Campaign ou etapa do Canvas específica. Nesses casos, `campaign_id`, `canvas_id` e campos de nome relacionados podem ser omitidos da carga útil do evento. Se você não encontrar esses campos em um determinado evento, verifique se aquele tipo de evento e contexto normalmente incluem identificadores de Campaign ou Canvas.