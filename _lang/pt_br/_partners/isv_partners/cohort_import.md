---
nav_title: Integração de importação de coorte
alias: /cohort_import/
hidden: true
---

# Integração de importação de coorte de parceiros {#partner-cohort-import-integration}

> O recurso de integração de importação de coorte de parceiros permite que nossos parceiros se integrem à Braze para enviar coortes de usuários gerados no aplicativo do parceiro.

## URLs de cluster {#cluster-urls}

A Braze hospeda nosso aplicativo em vários clusters ao redor do mundo. A URL dos endpoints de importação depende do cluster em que a instância da empresa do cliente está hospedada:

| INSTÂNCIA | ENDPOINT REST or transferir estado representacional |
| ----- | ------------------------------- |
| US-01 | `https://rest.iad-01.braze.com` |
| US-02 | `https://rest.iad-02.braze.com` |
| US-03 | `https://rest.iad-03.braze.com` |
| US-04 | `https://rest.iad-04.braze.com` |
| US-05 | `https://rest.iad-05.braze.com` |
| US-06 | `https://rest.iad-06.braze.com` |
| US-07 | `https://rest.iad-07.braze.com` |
| US-08 | `https://rest.iad-08.braze.com` |
| EU-01 | `https://rest.fra-01.braze.eu`  |
| EU-02 | `https://rest.fra-02.braze.eu`  |
| AU-01 | `https://rest.au-01.braze.com`  |
| JP-01 | `https://rest.jp-01.braze.com` |
| ID-01 | `https://rest.id-01.braze.com`  |
| KR-01 | `https://rest.kr-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cluster URLs" }

## URLs dos endpoints {#endpoint-urls}

Além de as URLs de nível superior serem específicas do cluster, cada endpoint também é específico do parceiro. Por exemplo, ao importar para nosso cluster US01, a URL teria o formato `https://rest.iad-01.braze.com/partners/[partner_name]/…`, em que `[partner_name]` é normalmente o nome da empresa do parceiro. As especificações de cada endpoint estão descritas nas seções a seguir.

## Autenticação {#authentication}

Para importar dados de coorte para a Braze, são necessárias duas chaves de autenticação.

### Chave de API or interface de programação do aplicativo (API) do parceiro {#partner-api-key}

A chave de API or interface de programação do aplicativo (API) do parceiro identifica o parceiro de integração e autentica a solicitação como válida para importação. A chave deve ser incluída no corpo da solicitação no campo `partner_api_key`.

Ao configurar a integração no aplicativo do parceiro, o cliente deve ser solicitado a especificar seu cluster Braze para que a integração saiba qual URL de cluster e chave de API or interface de programação do aplicativo (API) do parceiro usar ao importar dados.

A Braze fornecerá a(s) chave(s) de API or interface de programação do aplicativo (API) do parceiro ao parceiro antes de ele iniciar o desenvolvimento da integração. Em geral, forneceremos uma única chave válida para todos os clusters dos EUA e outra chave válida para nosso cluster da UE.

### Chave de importação de dados do cliente {#client-data-import-key}

A chave de importação de dados do cliente identifica o espaço de trabalho do cliente para o qual a coorte deve ser importada. A chave deve ser incluída no corpo da solicitação no campo `client_secret`.

Essa chave é gerada no dashboard do cliente nas configurações de integração com o parceiro. Ao configurar a integração no aplicativo do parceiro, o cliente deve ser solicitado a especificar sua chave de importação de dados para que a integração saiba para qual cliente e espaço de trabalho enviar os dados.

## Especificações dos endpoints da API or interface de programação do aplicativo (API) {#api-endpoint-specifications}

### Endpoint do nome da coorte {#cohort-name-endpoint}

O endpoint do nome da coorte pode ser usado para especificar o nome de uma coorte com base em seu ID. Esse endpoint deve ser chamado sempre que uma coorte for inicialmente exportada para a Braze ou quando o nome de uma coorte já conhecida pela Braze for alterado.

| Campo | Tipo | Obrigatória | Notas |
| ----- | ---- | -------- | ----- |
| `partner_api_key` | String | Sim | Chave de API or interface de programação do aplicativo (API) específica do parceiro, usada em todas as solicitações do parceiro para a Braze. Essa chave será específica do cluster (consulte [Chave de API or interface de programação do aplicativo (API) do parceiro](#partner-api-key)), portanto, o parceiro precisará conhecer o cluster no qual as coortes serão gravadas. |
| `client_secret` | String | Sim | Chave de importação de dados para o cliente ao qual a coorte pertence. |
| `cohort_id` | String | Sim | Identificador da coorte. Esse identificador deve ser exclusivo para o cliente especificado. |
| `name` | String | Sim | Nome especificado pelo cliente para a coorte |
| `created_at` | String | Sim | Carimbo de data/hora no formato ISO-8601 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Cohort name endpoint" }

#### Exemplo de solicitação: {#example-request}

`POST: https://rest.iad-01.braze.com/partners/[partner_name]/cohorts`
```
{
	"partner_api_key" : "123456-1234-1234-12345678",
	"client_secret" : "234567-2345-2345-23456789",
	"cohort_id" : "[some unique identifier generated by the partner]",
	"name" : "Name of the cohort that will appear in the Braze dashboard",
	"created_at" : "2021-01-21T19:20:30+05:00"
}
```

### Endpoint de coorte de usuários {#user-cohort-endpoint}

O endpoint de coorte de usuários permite especificar quais usuários foram adicionados ou removidos de uma determinada coorte. Esse endpoint deve ser chamado quando uma coorte é atualizada. Somente os usuários que entraram recentemente na coorte ou que saíram da coorte desde a última atualização devem ser enviados à Braze.

| Campo | Tipo | Obrigatória | Notas |
| ----- | ---- | -------- | ----- |
| `partner_api_key` | String | Sim | Chave de API or interface de programação do aplicativo (API) específica do parceiro, usada em todas as solicitações do parceiro para a Braze. Essa chave será específica do cluster (consulte [Chave de API or interface de programação do aplicativo (API) do parceiro](#partner-api-key)), portanto, a integração precisará conhecer o cluster no qual as coortes serão gravadas. |
| `client_secret` | String | Sim | Chave de importação de dados para o cliente ao qual a coorte pertence. |
| `cohort_id` | String | Sim | Identificador da coorte. O identificador deve ser exclusivo para o cliente especificado. |
| `cohort_changes` | Vetor de objetos | Sim | Os objetos podem ter dois campos. Um deles, `user_ids`, é obrigatório e pode ser um vetor de `external_ids`, `device_ids` e `aliases`. Cada elemento é um ID de um usuário cujo status na coorte foi alterado. O segundo campo, `should_remove`, é um booleano opcional que indica se os usuários desse objeto devem ser removidos da coorte em vez de adicionados. O padrão é false. O comprimento máximo combinado dos IDs de usuário em uma única solicitação é de 1.000.<br/><br/>Os usuários identificados podem ser correspondidos pelo `external_id` ou `alias`. Os usuários anônimos podem ser correspondidos pelo `device_id`. Se você passar um ID de dispositivo para um usuário identificado, a Braze não adicionará nem removerá esse usuário. Você deve usar IDs externos ou aliases para usuários identificados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="User cohort endpoint" }

#### Exemplo de solicitação:

`POST: https://rest.iad-01.braze.com/partners/[partner_name]/cohorts/users`
```
{
	"partner_api_key" : "123456-1234-1234-12345678",
	"client_secret" : "234567-2345-2345-23456789",
	"cohort_id" : "[some unique identifier generated by the partner]",
	"cohort_changes" : [
	   {"user_ids": ["test_user_1", "test_user_2"]}
	]
}
```

## Limite de taxa {#rate-limiting}

Além do máximo de 1.000 IDs de usuário por solicitação no endpoint de coorte de usuários, essas solicitações de endpoint têm um limite de taxa de 250.000 solicitações por hora.

## Filtro de coorte {#cohort-filter}

A Braze adicionará um filtro que permite que um usuário do dashboard inclua ou exclua usuários de um público-alvo se eles estiverem em uma coorte de parceiros. O filtro fornecerá uma lista suspensa com os nomes de todas as coortes conhecidas pela Braze para esse cliente. Esse filtro só será visível para os clientes com os quais o parceiro e a Braze concordaram em fazer parceria nessa integração.

## Solução de problemas {#troubleshooting}

Consulte a tabela a seguir para ver os códigos de erro específicos dos endpoints de importação de coorte e como solucioná-los.

| Código de erro | Descrição |
| ----- | ---- |
| `400` | `cohort_id` deve ser uma string válida |
|  | `cohort_changes` deve ser um vetor de objetos, cada um com a chave `user_ids` e/ou `device_ids` mapeando para um vetor de strings, ou um objeto `aliases` |
|  | Somente 1.000 `user_ids`, `device_ids` e `aliases` são permitidos por solicitação |
|  | `name` deve ser uma string não vazia |
|  | `created_at` deve ser uma hora válida como uma string [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) |
| `401` | Chave de API or interface de programação do aplicativo (API) de parceiro inválida |
|  | Segredo de cliente inválido |
|  | Parceiro não ativado para cliente com segredo de cliente: **&#60;client secret&#62;** |
|  | Acesso não autorizado |
| `423` | Recurso bloqueado |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

Para obter mais informações sobre solução de problemas, consulte [Erros e respostas]({{site.baseurl}}/api/errors/), que aborda os vários erros e respostas do servidor que podem surgir ao usar a API or interface de programação do aplicativo (API) da Braze.