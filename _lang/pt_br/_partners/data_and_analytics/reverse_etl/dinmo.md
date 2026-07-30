---
nav_title: DinMo
article_title: DinMo
description: "Este artigo de referência descreve a parceria entre a Braze e a DinMo, uma plataforma de dados do cliente composável que usa ETL reverso para sincronizar dados do data warehouse na Braze."
alias: /partners/dinmo/
page_type: partner
search_tag: Partner

---

# DinMo

> A [DinMo](https://www.dinmo.com/) é uma plataforma de dados do cliente (CDP) composável que conecta seu data warehouse na nuvem à Braze por meio de ETL reverso (Extract, Transform, Load). As equipes de marketing podem criar segmentos de público a partir de dados do data warehouse, sincronizar atributos de usuário e eventos na Braze e manter os status de inscrição atualizados sem uploads de CSV ou suporte de engenharia.

_Essa integração é gerenciada pela DinMo._

A integração entre a Braze e a DinMo envia segmentos e modelos de dados do seu data warehouse para a Braze por meio da REST API da Braze. Quando você conecta um destino Braze na DinMo, as ativações enviam dados dos seus modelos ou segmentos para a Braze.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta DinMo | Uma [conta DinMo](https://www.dinmo.com/) com permissão para criar destinos é necessária para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com as [permissões](#api-key-permissions) necessárias para os serviços de destino que você planeja usar. Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | A URL do seu endpoint REST. Seu endpoint depende da [URL da Braze para sua instância]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). |
| URL do dashboard da Braze | A URL do dashboard da Braze para sua instância (por exemplo, `https://dashboard.iad-01.braze.com`). Para saber mais, consulte [Endpoints de SDK disponíveis]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). |
| Data warehouse e modelo de dados | Antes de iniciar a integração, conecte seu data warehouse na DinMo e defina um modelo ou segmento para os dados que deseja sincronizar com a Braze. Para saber mais, consulte o [guia de integração DinMo Braze](https://docs.dinmo.io/integrations/destination-platforms/braze). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

Com essa integração, você pode:

* Sincronizar atributos de usuário do seu data warehouse na Braze para personalizar Campaigns e Canvas.
* Enviar eventos personalizados e eventos de compra a partir de dados do data warehouse para a Braze para direcionamento comportamental.
* Manter a associação a grupos de inscrições da Braze alinhada com segmentos de público definidos na DinMo.
* Exportar segmentos da DinMo como atributos de usuário da Braze e criar Segments da Braze a partir desses atributos.

## Permissões da chave de API {#api-key-permissions}

Conceda as seguintes permissões na sua chave da API REST da Braze com base nos serviços de destino que você utiliza:

| Permissão | Obrigatória para |
| --- | --- |
| `users.track` | Sincronizar atributos de usuário, enviar eventos de rastreamento e validar a conexão de destino |
| `users.export.ids` | Exportar IDs de usuário para operações em massa |
| `users.alias.update` | Atualizar aliases de usuário |
| `subscription.status.set` | Sincronizar status de inscrição |
| `users.delete` | Somente modo de sincronização espelho (opcional para outros serviços de destino) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permissões da chave de API" }

## Integração {#integration}

### Etapa 1: Configurar o destino Braze na DinMo {#step-1-configure-the-braze-destination-in-dinmo}

1. Na DinMo, acesse **Destinations** na navegação lateral.
2. Selecione **Add a new destination** > **Connect a new platform** > **Braze**.
3. No formulário de conexão, insira os seguintes dados:
   * **Platform Name**: Por exemplo, `Braze – Your Company`
   * **REST API URL**: O endpoint REST da sua instância (por exemplo, `https://rest.eu-01.braze.com`)
   * **Dashboard URL**: A URL do dashboard da sua instância (por exemplo, `https://dashboard.eu-01.braze.com`)
   * **API Key**: A chave que você copiou da Braze
4. Selecione **Connect** para validar suas credenciais.

{% alert note %}
Você deve especificar tanto a URL da REST API quanto a URL do dashboard. Não inclua uma barra final na URL da REST API.
{% endalert %}

### Etapa 2: Verificar a conexão {#step-2-verify-the-connection}

Depois de salvar o destino, a DinMo realiza uma chamada de teste (por exemplo, `users.track`) para confirmar que sua chave de API e endpoint estão funcionando.

Se a validação falhar, confirme o seguinte:

* A URL da REST API está correta e não possui barra final.
* A chave de API é válida e possui as permissões necessárias.
* Se o seu espaço de trabalho da Braze usa uma lista de IPs permitidos, os endereços IP da DinMo estão incluídos.

## Serviços de destino compatíveis {#supported-destination-services}

Cada serviço de destino na DinMo segue o mesmo fluxo geral: criar um destino Braze, construir um modelo ou segmento na DinMo e, em seguida, criar uma ativação para enviar dados para a Braze. Para orientações passo a passo sobre ativação, consulte [Serviços de destino DinMo Braze](https://docs.dinmo.io/integrations/destination-platforms/braze).

Os seguintes serviços de destino estão disponíveis:

| Serviço de destino | Descrição |
| --- | --- |
| [Sincronizar atributos de usuário](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-users-attributes) | Atualizar atributos de perfil de usuário na Braze e, opcionalmente, inserir novos usuários. |
| [Enviar eventos de rastreamento](https://docs.dinmo.io/integrations/destination-platforms/braze/send-track-events) | Enviar eventos personalizados e eventos de compra para a Braze. |
| [Sincronizar status de inscrição](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-subscription-statuses) | Inscrever ou cancelar a inscrição de usuários em um grupo de inscrições da Braze com base na associação ao segmento da DinMo. |
| [Exportar listas de usuários](https://docs.dinmo.io/integrations/destination-platforms/braze/export-user-lists) | Sincronizar a associação a segmentos com um atributo de usuário da Braze para uso na segmentação da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Serviços de destino compatíveis" }

### Sincronizar atributos de usuário {#synchronize-user-attributes}

Use este serviço de destino para atualizar atributos em perfis de usuário existentes na Braze e, opcionalmente, inserir novos usuários.

Quando você executa uma ativação:

* Se você ativar o modo de inserção, novos usuários no modelo são criados na Braze (comportamento UPSERT).
* Os valores de atributos alterados desde a última ativação são atualizados na Braze.

Se você não ativar o modo de inserção, a DinMo atualiza apenas os usuários que já existem na Braze e possuem um ID externo correspondente.

Durante a configuração da ativação, mapeie o campo no seu modelo DinMo que corresponde ao [ID externo]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids) ou ID da Braze do usuário. Mapeie cada campo da DinMo para o nome exato do atributo na Braze. Se um atributo não existir na Braze, a DinMo o cria.

Os seguintes modos de sincronização estão disponíveis para ativações de atributos de usuário:

| Modo de sincronização | Descrição |
| --- | --- |
| UPDATE | Atualiza registros alterados para usuários que já existem na Braze. Não insere nem exclui registros. |
| UPSERT | Insere novos registros e atualiza registros alterados. Não exclui registros. |
| MIRROR | Insere, atualiza e exclui registros na Braze para espelhar a origem. Requer suporte do conector para operações de exclusão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modos de sincronização de atributos de usuário" }

{% alert warning %}
O modo de sincronização espelho exclui permanentemente registros da Braze quando eles não estão mais presentes na origem da DinMo. Use o modo espelho somente quando seu data warehouse for a única fonte de verdade e as exclusões forem intencionais. Valide as regras de exclusão antes de executar sincronizações espelho em produção.
{% endalert %}

### Enviar eventos de rastreamento {#send-track-events}

Use este serviço de destino para enviar eventos personalizados ou eventos de compra de um modelo de eventos ou segmento da DinMo para a Braze. A DinMo trata eventos personalizados e compras como serviços de destino separados porque a Braze usa APIs diferentes para cada tipo.

Cada registro no modelo representa um único tipo de evento (por exemplo, `Purchase`). A DinMo envia apenas novos eventos em cada execução de ativação e não atualiza eventos enviados anteriormente.

Durante a configuração da ativação:

1. Especifique o nome do evento exatamente como ele deve aparecer na Braze. Se o evento não existir, a DinMo o cria.
2. Mapeie os campos obrigatórios:
   * **Event time**: Timestamp de quando o evento ocorreu
   * **External ID**: ID externo do usuário associado ao evento
3. Mapeie propriedades opcionais do evento para nomes de atributos da Braze.
4. Defina o cronograma de frequência com que novos eventos são enviados para a Braze.

### Sincronizar status de inscrição {#synchronize-subscription-statuses}

Use este serviço de destino para manter um grupo de inscrições da Braze alinhado com um segmento ou modelo da DinMo.

Antes de ativar este serviço:

1. Crie o grupo de inscrições de destino (SMS ou e-mail) na Braze.
2. Construa um modelo ou segmento na DinMo contendo os usuários que devem pertencer a esse grupo de inscrições.

Durante a configuração da ativação, insira o ID exato do grupo de inscrições da Braze. Para sincronizar múltiplos grupos de inscrições, crie uma ativação por grupo.

Quando a ativação é executada:

* Se os usuários já existirem na Braze, os usuários que entrarem no segmento da DinMo são marcados como inscritos no grupo de inscrições de destino.
* Os usuários que saírem do segmento da DinMo são marcados como não inscritos no grupo de inscrições.

A DinMo não modifica usuários que nunca fizeram parte do segmento e não cria novos usuários da Braze neste serviço de destino.

### Exportar listas de usuários {#export-user-lists}

Use este serviço de destino para representar um segmento da DinMo como um atributo de usuário da Braze. Devido a uma limitação da Braze, a DinMo não cria uma lista da Braze diretamente. Em vez disso, ela define um atributo de usuário como `true` para os usuários no segmento e `false` para os usuários que saem do segmento.

Durante a configuração da ativação, especifique o nome do público. A DinMo usa esse nome como o atributo da Braze (espaços são substituídos por underscores). Confirme que um atributo com o mesmo nome ainda não existe na Braze. Mapeie o campo da DinMo que corresponde ao ID externo do usuário.

Após a execução da ativação, crie um Segment da Braze que filtre os usuários cujo atributo sincronizado seja igual a `true`.

Somente usuários com um ID externo que corresponda a um usuário existente da Braze são atualizados. Este serviço de destino não cria novos usuários.