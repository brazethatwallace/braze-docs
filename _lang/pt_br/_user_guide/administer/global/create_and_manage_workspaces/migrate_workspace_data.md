---
nav_title: Migrar dados entre espaços de trabalho
article_title: Migrar dados entre espaços de trabalho e instâncias
page_order: 1
page_type: reference
description: "Saiba como os dados do espaço de trabalho são isolados, o que a Braze pode copiar ou importar entre espaços de trabalho e como planejar migrações entre ambientes de staging, produção ou dashboards separados."
---

# Migrar dados entre espaços de trabalho e instâncias {#migrate-data-between-workspaces-and-instances}

> Os espaços de trabalho mantêm seus dados da Braze separados. Esta página explica como esse isolamento afeta a migração, o que você pode mover com recursos do produto e APIs, e o que precisa ser recriado ou tratado fora da Braze. A migração geralmente é um esforço multifuncional — não apenas uma tarefa de administrador da empresa. Os administradores costumam ser responsáveis pela configuração do espaço de trabalho e dos canais; os desenvolvedores cuidam das alterações no SDK e na API; os profissionais de marketing recriam segmentos e copiam o conteúdo das mensagens. Cada etapa exige as [permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) relevantes nos espaços de trabalho de origem e destino.

Tudo o que você armazena na Braze — perfis de usuários, segmentos, conteúdo de mensagens e histórico de engajamento — fica dentro de um espaço de trabalho. Um segmento, uma Campaign ou um Canvas não consegue ler ou direcionar dados de outro espaço de trabalho. Os usuários do dashboard frequentemente usam vários espaços de trabalho no mesmo dashboard da empresa para staging e produção, para marcas diferentes ou para divisões regionais. Essa configuração oferece isolamento, mas também significa que não existe uma ação única no dashboard que mova todos os dados de um espaço de trabalho para outro espaço de trabalho ou outra instância da Braze.

Para contexto de planejamento, consulte [Primeiros passos: Espaços de trabalho]({{site.baseurl}}/user_guide/get_started/workspaces) e [Criar e gerenciar espaços de trabalho]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces).

## O que a Braze não migra automaticamente entre espaços de trabalho {#what-braze-does-not-automatically-migrate-between-workspaces}

Os itens a seguir não são migrados em massa quando você aponta SDKs ou APIs para um novo espaço de trabalho (ou um novo ambiente de dashboard da Braze com seus próprios espaços de trabalho):

| Área | Comportamento |
| --- | --- |
| **Perfis de usuários** | Os perfis não são transferidos como um pacote. Recrie ou importe os usuários no espaço de trabalho de destino (consulte [Dados do perfil de usuário](#user-profile-data)). |
| **Segmentos e filtros** | As definições de segmentos permanecem no espaço de trabalho de origem. Recrie os segmentos no espaço de trabalho de destino usando a mesma lógica sempre que possível. |
| **Histórico de mensagens** | O histórico de recebimento de Campaigns e Canvas em um perfil está vinculado ao espaço de trabalho de origem. Ele não aparece em um novo perfil em outro espaço de trabalho, a menos que você modele isso por conta própria (por exemplo, via atributos personalizados), conforme observado nas [Perguntas frequentes sobre integração da Braze]({{site.baseurl}}/user_guide/onboarding_faq). |
| **Configuração específica do canal** | Domínios de envio, inscrições de SMS, números de WhatsApp e configurações semelhantes são limitados ao espaço de trabalho. Reconfigure-os no espaço de trabalho de destino quando aplicável. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="O que a Braze não migra automaticamente entre espaços de trabalho" }

{% alert important %}
Se você usa espaços de trabalho separados para staging e produção, lembre-se de que os conectores do [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) não são compartilhados entre espaços de trabalho. Planeje qual espaço de trabalho será responsável pelas exportações de produção. Para mais detalhes, consulte [Primeiros passos: Espaços de trabalho]({{site.baseurl}}/user_guide/get_started/workspaces#currents-connectors).
{% endalert %}

## O que você pode mover ou recriar {#what-you-can-move-or-recreate}

### Conteúdo de Campaigns, Canvas e landing pages {#campaign-canvas-and-landing-page-content}

Você pode copiar muitas definições de Campaigns, Canvas e landing pages para outro espaço de trabalho como rascunhos. Os canais compatíveis, campos omitidos e ressalvas sobre Liquid estão documentados em [Copiar Campaigns, Canvas e landing pages entre espaços de trabalho]({{site.baseurl}}/user_guide/messaging/governance/copy_across_workspaces). Após a cópia, atualize os segmentos, gatilhos e quaisquer referências específicas do espaço de trabalho antes de lançar ou publicar.

### Dados do perfil de usuário {#user-profile-data}

Abordagens comuns:

- **REST API:** Use [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para criar ou atualizar usuários no espaço de trabalho de destino com os identificadores e atributos necessários. Esse é o mesmo padrão descrito para [migrar dados legados de usuários]({{site.baseurl}}/developer_guide/getting_started/integration_overview#migrating-legacy-user-data) ao trazer dados históricos para a Braze.
- **Importação por CSV:** Para importações feitas por profissionais de marketing, consulte [Importar usuários]({{site.baseurl}}/user_guide/audience/manage_audience/import_users) e [Importação por CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).
- **Ingestão de dados na nuvem:** Para sincronizar atributos de um data warehouse com o espaço de trabalho de destino, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).
- **Exportações do espaço de trabalho de origem:** Use [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) ou [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) para extrair os dados que você tem permissão para mover e, em seguida, mapeie-os para `users/track` ou CSV no destino. Respeite suas obrigações de retenção de dados, privacidade e contratuais ao exportar e recarregar dados.

{% alert note %}
A mesclagem de perfis duplicados com o endpoint [Mesclar usuários]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) ou [usuários duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users) no dashboard se aplica dentro de um único espaço de trabalho, não entre dois espaços de trabalho.
{% endalert %}

### Campos de exportação de usuários que não mapeiam para APIs padrão de perfil {#user-export-fields-that-dont-map-to-standard-profile-apis}

Ao recriar usuários em um espaço de trabalho de destino a partir de uma [exportação de usuários]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier), alguns campos da exportação não podem ser gravados de volta nos campos padrão de perfil da Braze por meio da REST API ou CSV (da forma como o SDK e o servidor os preenchem). Muitas vezes, você pode manter esses valores como atributos personalizados. Esteja ciente das seguintes limitações.

#### Informações do dispositivo (`devices`) {#device-information-devices}

Os registros de dispositivos na exportação são preenchidos pelo SDK. Não é possível migrar esses dados para os campos padrão de dispositivo da Braze por meio da REST API.

Se você precisar dessas informações antes que o usuário inicie uma sessão em um app que aponta para o espaço de trabalho de destino, envie-as como atributos personalizados ao importar o usuário. Os filtros de segmentação padrão e as referências Liquid que dependem de dados nativos de dispositivo não utilizam a carga útil de dispositivo exportada até que o usuário abra uma sessão em uma instância do app conectada ao novo espaço de trabalho (quando o SDK atualiza os campos padrão de dispositivo).

{% alert note %}
Isso é diferente da [migração de tokens por push](#push-tokens), que usa o campo `push_tokens` no [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).
{% endalert %}

#### Total de sessões e dados de sessão por app (`apps` e `sessions` aninhados) {#total-sessions-and-per-app-session-data-apps-and-nested-sessions}

Os totais de sessões e os dados de sessão aninhados do objeto `apps` em uma exportação não podem ser reimportados para os mesmos campos nativos. Para preservar contagens legadas (por exemplo, total de sessões do espaço de trabalho de origem), armazene-as em atributos personalizados e segmente com base nesses campos no espaço de trabalho de destino.

Você pode definir `date_of_first_session` e `date_of_last_session` por meio do [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ou importação por CSV. Para os formatos aceitos, consulte o [Objeto de atributos de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) e [Importação por CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).

#### Bucket aleatório (`random_bucket`) {#random-bucket-random_bucket}

Cada usuário recebe um [número de bucket aleatório]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-update-events) em seu espaço de trabalho. Esse valor não pode ser reimportado; o usuário recebe um novo bucket aleatório no espaço de trabalho de destino.

Se você depende do número antigo para holdouts ou amostragem (por exemplo, excluir usuários cujo `random_bucket` está abaixo de um limite), salve o valor exportado como um atributo personalizado e crie segmentos ou filtros com base nesse atributo em vez do campo nativo de bucket aleatório.

#### Campos de atribuição de parceiros (`attributed_*`) {#partner-attribution-fields-attributed_}

Os campos de atribuição de integrações com parceiros (os campos `attributed_*` em uma exportação) não podem ser definidos nos campos padrão de atribuição da Braze por meio da REST API. Mapeie-os para atributos personalizados no espaço de trabalho de destino se precisar mantê-los para segmentação ou envio de mensagens.

### Tokens por push {#push-tokens}

Quando os usuários já possuem tokens por push de um provedor anterior ou versão do app, você pode importar tokens para apps móveis por meio da API ou contar com o SDK após a integração. Tokens por push para web têm limitações na API. Para detalhes completos e exemplos, consulte [Migrar tokens por push]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens).

### WhatsApp

Números de telefone e grupos de inscrições podem ser movidos entre espaços de trabalho com um fluxo de transferência específico. Consulte [Transferir números de telefone e grupos de inscrições do WhatsApp entre espaços de trabalho]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/transfer_between_workspaces).

### Dados de engajamento e análise de dados fora da Braze {#engagement-and-analytics-data-outside-braze}

Se você precisa de um registro histórico de envios, aberturas ou cliques ao consolidar ambientes, o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) e outras exportações são a forma suportada de enviar esses dados para seu data warehouse ou ferramentas. Esses dados não são reingeridos na Braze como histórico nativo de mensagens por usuário em outro espaço de trabalho.

## Antes de alterar as chaves do SDK ou da API {#before-you-change-sdk-or-api-keys}

Quando você aponta seu app ou site para um novo espaço de trabalho:

- Os usuários que abrirem o app ou site podem criar novos perfis no novo espaço de trabalho. Eles não carregam automaticamente o histórico específico do espaço de trabalho anterior.
- Se a mesma pessoa puder existir em ambos os espaços de trabalho, você pode encontrar [cenários semelhantes a duplicatas]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces#should-i-create-a-new-workspace-when-im-releasing-an-updated-app) (por exemplo, sobreposição de alcance de push). Prefira um plano deliberado de dados e direcionamento em vez de compartilhar chaves de produção e staging de forma não intencional.

{% alert tip %}
Para limites de exclusão de espaços de trabalho ou instâncias de app, movimentações especiais de conta ou planejamento de migração em larga escala, [fale com o suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) com os links do seu dashboard e um resumo dos espaços de trabalho de origem e destino.
{% endalert %}