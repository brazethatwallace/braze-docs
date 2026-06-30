---
nav_title: "PUT: Substituir um ativo na biblioteca de mídia"
article_title: "PUT: Substituir um ativo na biblioteca de mídia"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint `PUT /media_library/replace_file`."
---

{% api %}
# Substituir um ativo na biblioteca de mídia {#replace-an-asset-in-the-media-library}
{% apimethod put %}
/media_library/replace_file
{% endapimethod %}

> Use este endpoint para substituir o arquivo de um ativo existente na [Biblioteca de mídia da Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library), preservando o ID e a URL do ativo. Você pode fornecer o arquivo de substituição usando uma URL hospedada externamente (`asset_url`) ou dados binários de arquivo enviados no corpo da solicitação (`asset_file`).

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key) com a permissão `media_library.replace`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='media_library' %}

## Corpo da solicitação {#request-body}

Quando você inclui `asset_url`, o endpoint baixa o arquivo a partir da URL. Quando você inclui `asset_file`, o endpoint usa os dados binários no corpo da solicitação.

Exemplo de corpo da solicitação para `asset_url`:

```json
{
  "asset_id": "your-asset-id",
  "asset_url": "https://cdn.example.com/assets/cat.jpg"
}
```

Exemplo de corpo da solicitação para `asset_file`:

```json
{
  "asset_id": "your-asset-id",
  "asset_file": <BINARY FILE DATA>
}
```

O corpo da solicitação inclui os seguintes parâmetros:

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `asset_id` | Obrigatória | String | O ID do ativo a ser substituído. |
| `asset_url` | Opcional | String | Uma URL publicamente acessível para o arquivo de substituição. |
| `asset_file` | Opcional | Binário | Dados binários do arquivo de substituição. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Corpo da solicitação" }

{% alert important %}
`asset_url` e `asset_file` são mutuamente exclusivos. Você deve incluir apenas um deles na sua solicitação de API.
{% endalert %}

### Requisitos do arquivo de substituição {#replacement-file-requirements}

- A extensão do arquivo de substituição deve corresponder exatamente à extensão do ativo existente. Por exemplo, você não pode substituir um ativo `.png` por um arquivo `.jpg`.
- A substituição de arquivo é compatível com imagens, SVGs, documentos, fontes, cartões de contato e arquivos de código. Ativos de vídeo não podem ser substituídos.

## Exemplo de solicitação {#example-request}

Esta seção inclui dois exemplos de solicitações `curl`, um para substituir um ativo usando uma URL e outro usando dados binários de arquivo.

Esta solicitação mostra um exemplo de substituição de um ativo na Biblioteca de mídia usando um `asset_url`.

```
curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_url": "https://cdn.example.com/assets/cat.jpg"}'
```

Esta solicitação mostra um exemplo de substituição de um ativo na Biblioteca de mídia usando um `asset_file`.

```
curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_file":<BINARY FILE DATA>}'
```

### Respostas de erro {#error-responses}

Esta seção lista possíveis erros e suas mensagens e descrições correspondentes.

#### Erros de validação {#validation-errors}

Erros de validação retornam uma estrutura como esta:

```json
{
  "message": (String) Human-readable error description
}
```

Esta tabela lista os possíveis erros de validação.

| Status HTTP | Mensagem | Descrição |
| --- | --- | --- |
| 400 | "asset_id is required." | Nenhum ID de ativo foi fornecido na solicitação. |
| 400 | "Either file or asset_url is required." | Nem `asset_file` nem `asset_url` foram fornecidos; um deles é obrigatório. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros de validação" }

#### Erros de processamento {#processing-errors}

Erros de processamento retornam uma resposta diferente com códigos de erro:

```json
{
  "message": (String) Human-readable error description,
  "error_code": (String) error code,
  "meta": { }
}
```

Esta tabela lista os possíveis erros de processamento.

| Código de erro | Status HTTP | Descrição |
| --- | --- | --- |
| `ASSET_NOT_FOUND` | 404 | Nenhum ativo com o `asset_id` fornecido existe neste espaço de trabalho. O objeto `meta` inclui `asset_id`. |
| `INVALID_ASSET_URL` | 400 | O valor de `asset_url` não é uma URI válida. O objeto `meta` inclui `asset_url`. |
| `EXTENSION_MISMATCH` | 400 | A extensão do arquivo de substituição não corresponde à extensão do ativo existente. O objeto `meta` inclui `expected_extension` e `received_extension`. |
| `UNSUPPORTED_ASSET_TYPE_FOR_REPLACE` | 400 | A substituição de arquivo não é compatível com este tipo de ativo (por exemplo, vídeo). O objeto `meta` inclui `asset_type`. |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | O arquivo excede o tamanho máximo permitido. O objeto `meta` inclui `size_limit_bytes` e `file_size_bytes`. |
| `CORRUPT_FILE` | 400 | O arquivo de imagem está corrompido ou ilegível. O objeto `meta` inclui `file_name`. |
| `GENERIC_ERROR` | 500 | Ocorreu um erro inesperado durante a substituição do arquivo. O objeto `meta` inclui `original_error` para depuração. Tente novamente ou entre em contato com o [Suporte]({{site.baseurl}}/support_contact). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros de processamento" }

## Resposta {#response}

Existem cinco respostas de código de status para este endpoint: `200`, `400`, `404`, `429` e `500`.

O JSON a seguir mostra o formato esperado da resposta.

```json
{
  "info": "Asset file updated successfully.",
  "new_image_asset": {
    "name": (String) the name of the asset,
    "size": (Integer) the byte size of the asset,
    "url": (String) the URL to access the asset,
    "ext": (String) the file extension (e.g., "png", "jpg", "gif")
  }
}
```

{% endapi %}