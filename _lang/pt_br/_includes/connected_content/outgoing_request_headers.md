A Braze adiciona os seguintes cabeçalhos às solicitações de Connected Content de saída. A maioria é definida apenas quando você ainda não os forneceu na tag. Os cabeçalhos que você fornece com `:headers`, credenciais ou opções da tag são enviados conforme fornecidos.

| Cabeçalho | Quando a Braze o define |
| --- | --- |
| `User-Agent` | Se você ainda não o definiu, a Braze envia `Braze Sender <version>`. A string de versão pode mudar. Se você filtra tráfego por `User-Agent`, permita todos os valores que começam com `Braze Sender`. Para enviar um valor consistente, defina `User-Agent` em `:headers`. |
| `X-Braze-Sender-Version` | Sempre definido como a versão do remetente de Connected Content. |
| `Accept-Encoding` | Se você ainda não o definiu, a Braze envia `gzip`. |
| `Authorization` | Se a URL incluir um nome de usuário e uma senha (`user:pass@host`), a Braze adiciona um cabeçalho Basic `Authorization` derivado dessas credenciais. Um cabeçalho `Authorization` explícito o substitui. Prefira [`:basic_auth`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#using-basic-authentication) ou `:headers` em vez de colocar credenciais na URL. |
| `Host` | Nome do host da URL da solicitação (por exemplo, `www.example.com` para `https://www.example.com/abc/123`), a menos que você defina um cabeçalho `Host`. |
| `Content-Length` | Tamanho do corpo da solicitação em bytes quando um corpo está presente. |
| `BrazeToBraze` | Definido como `true` apenas para solicitações a endpoints REST da Braze. Omitido para outros destinos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cabeçalhos de solicitação de saída que a Braze adiciona ao Connected Content" }