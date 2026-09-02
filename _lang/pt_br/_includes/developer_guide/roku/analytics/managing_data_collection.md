{% multi_lang_include developer_guide/prerequisites/roku.md %}

## Limpando dados armazenados anteriormente {#wiping-previously-stored-data}

O Roku SDK or kit de desenvolvimento de software não inclui um método `wipeData`. Para produzir um estado limpo funcionalmente equivalente ao `wipeData()` em outros SDKs da Braze, limpe as quatro seções de registro da Braze e, em seguida, reinicialize o SDK or kit de desenvolvimento de software.

O Roku SDK or kit de desenvolvimento de software da Braze persiste dados nas seguintes seções de registro:

| Seção | Conteúdo |
|---------|----------|
| `braze.section.device_id` | O UUID do dispositivo usado para identificar este dispositivo na Braze. |
| `braze.section.user_id` | O ID de usuário externo, se um tiver sido definido. |
| `braze.section.session` | O UUID da sessão ativa, horário de início e horário de término. |
| `braze.section.config` | Configuração do SDK or kit de desenvolvimento de software em cache e dados de Feature Flag. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limpando dados armazenados anteriormente" }

### Etapa 1: Limpar as seções de registro {#step-1-clear-the-registry-sections}

Use [`roRegistry.Delete()`](https://developer.roku.com/docs/references/brightscript/components/roregistry.md) para excluir cada seção da Braze e, em seguida, chame `Flush()` para persistir as alterações:

```brightscript
sub WipeBrazeData()
    registry = CreateObject("roRegistry")
    registry.Delete("braze.section.device_id")
    registry.Delete("braze.section.user_id")
    registry.Delete("braze.section.session")
    registry.Delete("braze.section.config")
    registry.Flush()
end sub
```

### Etapa 2: Reinicializar o SDK or kit de desenvolvimento de software da Braze {#step-2-re-initialize-the-braze-sdk}

Quando você [inicializar o SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku) novamente, o SDK or kit de desenvolvimento de software lida com os dados de registro ausentes de forma adequada:

- A seção de ID do dispositivo está vazia, então o SDK or kit de desenvolvimento de software gera um novo UUID e trata o dispositivo como anônimo.
- A seção de ID do usuário está vazia, então o SDK or kit de desenvolvimento de software assume o padrão de um usuário anônimo (uma string vazia `""`).
- A seção de sessão está vazia, então o SDK or kit de desenvolvimento de software inicia uma nova sessão.
- A seção de configuração está vazia, então o SDK or kit de desenvolvimento de software busca novamente a configuração no servidor.

{% alert note %}
O Roku SDK or kit de desenvolvimento de software não gera nenhuma solicitação de exclusão no lado do servidor quando você limpa o registro. Se você também precisar remover o usuário da Braze, envie uma solicitação para [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) usando o `external_id` ou `braze_id` do usuário.
{% endalert %}

## Logout e cancelamento de registro de push {#logout-and-unregister-push}

Este recurso ainda não é compatível com o Roku SDK or kit de desenvolvimento de software.