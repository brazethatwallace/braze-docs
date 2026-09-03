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
| Endpoint REST da Braze | Sua URL do endpoint REST. Seu endpoint depende dos [endpoints de API]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints) da sua instância da Braze. |
| URL do dashboard da Braze | A URL do dashboard da Braze para sua instância (por exemplo, `https://dashboard.iad-01.braze.com`). Para saber mais, consulte [Endpoints de SDK disponíveis]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). |
| Data warehouse e modelo de dados | Antes de iniciar a integração, conecte seu data warehouse no DinMo e defina um modelo ou Segment para os dados que você deseja sincronizar com a Braze. Para saber mais, consulte o [Guia de integração DinMo com a Braze](https://docs.dinmo.io/integrations/destination-platforms/braze). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

Com essa integração, você pode:

* Sincronizar atributos de usuário do seu data warehouse na Braze para personalizar Campaigns e Canvas.
* Enviar eventos personalizados e eventos de compra a partir dos dados do data warehouse para a Braze para direcionamento comportamental.
* Manter a associação ao grupo de inscrições da Braze alinhada com os Segments de público definidos no DinMo.
* Exportar Segments do DinMo como atributos de usuário da Braze e criar Segments da Braze a partir desses atributos.

## Permissões da chave de API {#api-key-permissions}

Conceda as seguintes permissões na sua chave da API REST da Braze com base nos serviços de destino que você utiliza:

| Permissão | Necessária para |
| --- | --- |
| `users.track` | Sincronizar atributos de usuário, enviar eventos de rastreamento e validar a conexão de destino |
| `users.export.ids` | Exportar IDs de usuário para operações em massa |
| `users.alias.update` | Atualizar aliases de usuário |
| `subscription.status.set` | Sincronizar status de inscrição |
| `users.delete` | Apenas modo de sincronização espelho (opcional para outros serviços de destino) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permissões da chave de API" }

## Integração {#integration}

### Etapa 1: Configurar o destino da Braze no DinMo {#step-1-configure-the-braze-destination-in-dinmo}

1. No DinMo, acesse **Destinations** na navegação lateral.
2. Selecione **Add a new destination** > **Connect a new platform** > **Braze**.
3. No formulário de conexão, insira os seguintes dados:
   * **Platform Name**: Por exemplo, `Braze – Your Company`
   * **REST API URL**: O endpoint REST da sua instância (por exemplo, `https://rest.eu-01.braze.com`)
   * **Dashboard URL**: A URL do dashboard da sua instância (por exemplo, `https://dashboard.eu-01.braze.com`)
   * **API Key**: A chave que você copiou da Braze
4. Selecione **Connect** para validar suas credenciais.

{% alert note %}
Você precisa especificar tanto a URL da REST API quanto a URL do dashboard. Não inclua uma barra final na URL da REST API.
{% endalert %}

### Etapa 2: Verificar a conexão {#step-2-verify-the-connection}

Depois de salvar o destino, o DinMo realiza uma chamada de teste (por exemplo, `users.track`) para confirmar que sua chave de API e o endpoint estão funcionando.

Se a validação falhar, confirme o seguinte:

* A URL da REST API está correta e não tem barra final.
* A chave de API é válida e possui as permissões necessárias.
* Se o seu espaço de trabalho da Braze usa uma lista de IPs permitidos, os endereços IP do DinMo estão incluídos.

## Serviços de destino compatíveis {#supported-destination-services}

Cada serviço de destino no DinMo segue o mesmo fluxo de trabalho geral: criar um destino Braze, construir um modelo ou Segment do DinMo e, em seguida, criar uma ativação para enviar dados à Braze. Para orientações passo a passo sobre ativação, consulte [Serviços de destino Braze do DinMo](https://docs.dinmo.io/integrations/destination-platforms/braze).

Os seguintes serviços de destino estão disponíveis:

| Serviço de destino | Descrição |
| --- | --- |
| [Sincronizar atributos de usuário](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-users-attributes) | Atualiza atributos de perfil de usuário na Braze e, opcionalmente, insere novos usuários. |
| [Enviar eventos de rastreamento](https://docs.dinmo.io/integrations/destination-platforms/braze/send-track-events) | Envia eventos personalizados e eventos de compra à Braze. |
| [Sincronizar status de inscrição](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-subscription-statuses) | Inscreve ou cancela a inscrição de usuários em um grupo de inscrições da Braze com base na participação no Segment do DinMo. |
| [Exportar listas de usuários](https://docs.dinmo.io/integrations/destination-platforms/braze/export-user-lists) | Sincroniza a participação em Segments com um atributo de usuário da Braze para uso na segmentação da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Serviços de destino compatíveis" }

### Sincronizar atributos de usuário {#synchronize-user-attributes}

Use este serviço de destino para atualizar atributos em perfis de usuário existentes na Braze e, opcionalmente, inserir novos usuários.

Quando você executa uma ativação:

* Se você ativar o modo de inserção, novos usuários no modelo são criados na Braze (comportamento UPSERT).
* Valores de atributos alterados desde a última ativação são atualizados na Braze.

Se você não ativar o modo de inserção, o DinMo atualiza apenas os usuários que já existem na Braze e possuem um ID externo correspondente.

Durante a configuração da ativação, mapeie o campo no seu modelo do DinMo que corresponde ao [ID externo]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web) ou ID da Braze do usuário. Mapeie cada campo do DinMo para o nome exato do atributo na Braze. Se um atributo não existir na Braze, o DinMo o cria.

Os seguintes modos de sincronização estão disponíveis para ativações de atributos de usuário:

| Modo de sincronização | Descrição |
| --- | --- |
| UPDATE | Atualiza registros alterados para usuários que já existem na Braze. Não insere nem exclui registros. |
| UPSERT | Insere novos registros e atualiza registros alterados. Não exclui registros. |
| MIRROR | Insere, atualiza e exclui registros na Braze para espelhar a fonte. Requer suporte do conector para operações de exclusão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modos de sincronização de atributos de usuário" }

{% alert warning %}
O modo de sincronização MIRROR exclui permanentemente registros da Braze quando eles não estão mais presentes na fonte do DinMo. Use o modo MIRROR somente quando seu data warehouse for a única fonte de verdade e as exclusões forem intencionais. Valide as regras de exclusão antes de executar sincronizações MIRROR em produção.
{% endalert %}

### Enviar eventos de rastreamento {#send-track-events}

Use este serviço de destino para enviar eventos personalizados ou eventos de compra de um modelo de eventos ou Segment do DinMo à Braze. O DinMo trata eventos personalizados e compras como serviços de destino separados porque a Braze usa APIs diferentes para cada tipo.

Cada registro no modelo representa um único tipo de evento (por exemplo, `Purchase`). O DinMo envia apenas novos eventos em cada execução de ativação e não atualiza eventos enviados anteriormente.

Durante a configuração da ativação:

1. Especifique o nome do evento exatamente como ele deve aparecer na Braze. Se o evento não existir, o DinMo o cria.
2. Mapeie os campos obrigatórios:
   * **Horário do evento**: Timestamp de quando o evento ocorreu
   * **ID externo**: ID externo do usuário associado ao evento
3. Mapeie propriedades opcionais do evento para nomes de atributos da Braze.
4. Defina o cronograma de frequência de envio de novos eventos à Braze.

### Sincronizar status de inscrição {#synchronize-subscription-statuses}

Use este serviço de destino para manter um grupo de inscrições da Braze alinhado com um Segment ou modelo do DinMo.

Antes de ativar este serviço:

1. Crie o grupo de inscrições de destino (SMS ou e-mail) na Braze.
2. Construa um modelo ou Segment do DinMo contendo os usuários que devem pertencer a esse grupo de inscrições.

Durante a configuração da ativação, insira o ID exato do grupo de inscrições da Braze. Para sincronizar múltiplos grupos de inscrições, crie uma ativação por grupo.

Quando a ativação é executada:

* Se os usuários já existirem na Braze, os usuários que entram no Segment do DinMo são marcados como inscritos no grupo de inscrições de destino.
* Os usuários que saem do Segment do DinMo são marcados como não inscritos no grupo de inscrições.

O DinMo não modifica usuários que nunca fizeram parte do Segment e não cria novos usuários na Braze neste serviço de destino.

### Exportar listas de usuários {#export-user-lists}

Use este serviço de destino para representar um Segment do DinMo como um atributo de usuário da Braze. Devido a uma limitação da Braze, o DinMo não cria uma lista da Braze diretamente. Em vez disso, ele define um atributo de usuário como `true` para usuários no Segment e `false` para usuários que saem do Segment.

Durante a configuração da ativação, especifique o nome do público. O DinMo usa esse nome como o atributo da Braze (espaços são substituídos por underscores). Confirme que um atributo com o mesmo nome ainda não existe na Braze. Mapeie o campo do DinMo que corresponde ao ID externo do usuário.

Após a execução da ativação, crie um Segment da Braze que filtre os usuários cujo atributo sincronizado seja igual a `true`.

Somente usuários com um ID externo que corresponda a um usuário existente na Braze são atualizados. Este serviço de destino não cria novos usuários.