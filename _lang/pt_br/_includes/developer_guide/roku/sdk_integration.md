## Integrando o Roku SDK or kit de desenvolvimento de software {#integrating-the-roku-sdk}

### Etapa 1: Adicionar arquivos {#step-1-add-files}

Os arquivos do SDK or kit de desenvolvimento de software da Braze podem ser encontrados no diretório `sdk_files` no [repositório do Braze Roku SDK or kit de desenvolvimento de software](https://github.com/braze-inc/braze-roku-sdk).

1. Adicione `BrazeSDK.brs` ao seu app no diretório `source`.
2. Adicione `BrazeTask.brs` e `BrazeTask.xml` ao seu app no diretório `components`.

### Etapa 2: Adicionar referências {#step-2-add-references}

Adicione uma referência a `BrazeSDK.brs` na sua cena principal usando o seguinte elemento `script`:

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### Etapa 3: Configurar {#step-3-configure}

Dentro de `main.brs`, defina a configuração da Braze no nó global:

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

Você pode encontrar seu [endpoint de SDK or kit de desenvolvimento de software or endpoint do SDK or kit de desenvolvimento de software]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) e chave de API or interface de programação do aplicativo (API) no dashboard da Braze.

### Etapa 4: Inicializar a Braze {#step-4-initialize-braze}

Inicialize a instância da Braze:

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Configurações opcionais {#optional-configurations}

### Registro de logs {#logging}

Para depurar sua integração com a Braze, você pode visualizar o console de depuração do Roku para verificar os logs da Braze. Consulte [Depuração de código](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) da Roku Developers para saber mais.