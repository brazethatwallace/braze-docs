## Questionário de privacidade do Google Play {#privacy-questionnaire}

A partir de abril de 2022, os desenvolvedores de Android deverão preencher o [formulário de segurança de dados](https://support.google.com/googleplay/android-developer/answer/10787469) do Google Play para divulgar práticas de privacidade e segurança. Este guia fornece instruções sobre como preencher esse novo formulário com informações sobre como a Braze lida com os dados do seu app.

Como desenvolvedor do app, você tem o controle dos dados que envia à Braze. Os dados recebidos pela Braze são processados de acordo com suas instruções. Isso é o que o Google classifica como um [prestador de serviço](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform).

{% alert important %}
Este artigo traz informações relacionadas aos dados que o SDK da Braze processa em relação ao questionário da seção de segurança do Google. Este artigo não fornece orientação jurídica, portanto, recomendamos consultar sua equipe jurídica antes de enviar qualquer informação ao Google.
{% endalert %}

### Perguntas {#questions}

| Perguntas | Respostas para o Braze SDK |
|---|---|
| O seu app coleta ou compartilha algum dos tipos de dados de usuários necessários? | Sim, o SDK da Braze para Android coleta dados conforme configurado pelo desenvolvedor do app. |
| Todos os dados de usuários coletados pelo seu app são criptografados em trânsito? | Sim. |
| Vocês oferecem uma maneira de os usuários solicitarem a exclusão de seus dados? | Sim. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Perguntas" }

Para saber mais sobre como lidar com solicitações de dados de usuários e exclusão, consulte [Informações de retenção de dados da Braze]({{site.baseurl}}/api/data_retention).

### Coleta de dados {#data-collection}

Os dados coletados pela Braze são determinados pela sua integração específica e pelos dados de usuários que você escolher coletar. Para saber mais sobre quais dados a Braze coleta por padrão e como desativar determinados atributos, consulte nossas [opções de coleta de dados do SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection#minimum-integration).

<table aria-label="Coleta de dados" id="datatypes">
    <thead>
        <tr>
            <th width="25%">Categoria</th>
            <th width="25%">Tipo de dados</th>
            <th width="50%">Uso da Braze</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">Local</td>
            <td>Local aproximado</td>
            <td rowspan="15">Não coletado por padrão.</td>
        </tr>
        <tr>
            <td>Localização precisa</td>
        </tr>
        <tr>
            <td rowspan="9">Informações pessoais</td>
            <td>Nome</td>
        </tr>
        <tr>
            <td>Endereço de e-mail</td>
        </tr>
        <tr>
            <td>IDs de usuário</td>
        </tr>
        <tr>
            <td>Endereço</td>
        </tr>
        <tr>
            <td>Número de telefone</td>
        </tr>
        <tr>
            <td>Raça e etnia</td>
        </tr>
        <tr>
            <td>Crenças políticas ou religiosas</td>
        </tr>
        <tr>
            <td>Orientação sexual</td>
        </tr>
        <tr>
            <td>Outras informações</td>
        </tr>
        <tr>
            <td rowspan="4">Informações financeiras</td>
            <td>Informações de pagamento do usuário</td>
        </tr>
        <tr>
            <td>Histórico de compras</td>
        </tr>
        <tr>
            <td>Pontuação de crédito</td>
        </tr>
        <tr>
            <td>Outras informações financeiras</td>
        </tr>
        <tr>
            <td rowspan="2">Saúde e condicionamento físico</td>
            <td>Informações sobre saúde</td>
            <td rowspan="2">Não coletado por padrão.</td>
        </tr>
        <tr>
            <td>Informações sobre condicionamento físico</td>
        </tr>
        <tr>
            <td rowspan="3">Mensagens</td>
            <td>E-mails</td>
            <td rowspan="2">Não coletado por padrão.</td>
        </tr>
        <tr>
            <td>SMS ou MMS</td>
        </tr>
        <tr>
            <td>Outras mensagens no app</td>
            <td>Se você enviar mensagens no app ou notificações por push por meio da Braze, coletaremos informações sobre quando os usuários abriram ou leram essas mensagens.</td>
        </tr>
        <tr>
            <td rowspan="2">Fotos e vídeos</td>
            <td>Fotos</td>
            <td rowspan="8">Não coletado.</td>
        </tr>
        <tr>
            <td>Vídeos</td>
        </tr>
        <tr>
            <td rowspan="3">Arquivos de áudio</td>
            <td>Gravações de voz ou som</td>
        </tr>
        <tr>
            <td>Arquivos de música</td>
        </tr>
        <tr>
            <td>Outros arquivos de áudio</td>
        </tr>
        <tr>
            <td>Arquivos e documentos</td>
            <td>Arquivos e documentos</td>
        </tr>
        <tr>
            <td>Calendário</td>
            <td>Eventos do calendário</td>
        </tr>
        <tr>
            <td>Contatos</td>
            <td>Contatos</td>
        </tr>
        <tr>
            <td rowspan="5">Atividade do app</td>
            <td>Interações do app</td>
            <td>A Braze coleta dados de atividade da sessão por padrão. Todas as outras interações e atividades são determinadas pela integração personalizada do seu app.</td>
        </tr>
        <tr>
            <td>Histórico de pesquisa no app</td>
            <td>Não coletado.</td>
        </tr>
        <tr>
            <td>Aplicativos instalados</td>
            <td>Não coletado.</td>
        </tr>
        <tr>
            <td>Outros conteúdos gerados por usuários</td>
            <td rowspan="2">Não coletado por padrão.</td>
        </tr>
        <tr>
            <td>Outras ações</td>
        </tr>
        <tr>
            <td>Navegação na web</td>
            <td>Histórico de navegação na web</td>
            <td>Não coletado.</td>
        </tr>
        <tr>
            <td rowspan="3">Informações e desempenho do app</td>
            <td>Registros de falhas</td>
            <td>A Braze coleta registros de falhas para erros que ocorrem no SDK. Eles contêm o modelo do telefone do usuário e o nível do sistema operacional, juntamente com um ID de usuário específico da Braze.</td>
        </tr>
        <tr>
            <td>Diagnóstico</td>
            <td>Não coletado.</td>
        </tr>
        <tr>
            <td>Outros dados de desempenho do app</td>
            <td>Não coletado.</td>
        </tr>
        <tr>
            <td>IDs de dispositivos ou outros</td>
            <td>IDs de dispositivos ou outros</td>
            <td>A Braze gera um ID de dispositivo para diferenciar os dispositivos dos usuários e verifica se as mensagens são enviadas para o dispositivo correto.</td>
        </tr>
    </tbody>
</table>

Para saber mais sobre outros dados de dispositivos que a Braze coleta e que podem estar fora do escopo das diretrizes de segurança de dados do Google Play, consulte nossa [visão geral do armazenamento Android]({{site.baseurl}}/developer_guide/storage/?tab=android) e nossas [opções de coleta de dados do SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection#minimum-integration).

## Desabilitando o rastreamento de dados {#disabling-data-tracking}

Para desabilitar a atividade de rastreamento de dados no SDK para Android, use o método [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html). Isso fará com que todas as conexões de rede sejam canceladas, o que significa que o SDK da Braze não enviará mais nenhum dado para os servidores da Braze.

## Limpando dados armazenados anteriormente {#wiping-previously-stored-data}

Você pode usar o método [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) para limpar completamente todos os dados do lado do cliente armazenados no dispositivo.

## Retomando o rastreamento de dados {#resuming-data-tracking}

Para retomar a coleta de dados, você pode usar o método [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html). Lembre-se de que isso não recuperará nenhum dado previamente apagado.

## Logout e cancelamento de registro de push {#logout-and-unregister-push}

O SDK da Braze fornece métodos para parar de direcionar um dispositivo quando um usuário cancela o registro de notificações por push ou faz logout. Esses métodos removem os dados de registro de push do usuário atual no servidor da Braze e no SDK, de modo que a Braze não envia mais Campaigns de notificação por push futuras para esse usuário.

### Logout {#logout}

Quando um usuário faz logout de um aplicativo, chame o método `logout` do SDK para remover o registro de push do dispositivo do usuário atual e executar automaticamente ações de limpeza no SDK. O método `logout` executa o seguinte:

- Cancela o registro do token de push do dispositivo do usuário atual no servidor da Braze.
- Se a chamada de cancelamento de registro for bem-sucedida, o SDK limpa os dados do SDK armazenados localmente e desabilita o SDK.
- Em caso de falha, gera um erro e um sinalizador `isRetriable` para permitir que o integrador tome uma ação.

O exemplo de retorno de chamada a seguir mostra o tratamento de sucesso e erro do `logout`. Use-o para fluxos de logout baseados em retorno de chamada e substitua o registro de log pela sua lógica de nova tentativa ou reautenticação.

```kotlin
// Completion callback
Braze.getInstance(context).logout { result ->
  result
    .onSuccess {
      Log.d(TAG, "Logout successful")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(TAG, "Logout failed: ${error.message}, isRetriable: ${pushError?.isRetriable}")
    }
}
```

O exemplo de coroutine a seguir mostra a API suspensa `logout`. Use-o em fluxos baseados em coroutine e personalize as ramificações de sucesso e falha para o seu app.

```kotlin
lifecycleScope.launch {
  runCatching { Braze.getInstance(context).logout() }
    .onSuccess {
      Log.d(TAG, "Logout successful")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(TAG, "Logout failed: ${error.message}, isRetriable: ${pushError?.isRetriable}")
    }
}
```

#### Reativar o rastreamento e push após `logout` {#re-enable-tracking-and-push-after-logout}

Após um `logout` bem-sucedido, reative o SDK com [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html) e, em seguida, registre-se novamente para notificações com o seu sistema operacional (SO) ou provedor de push seguindo a [configuração de push para Android]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

#### Evite chamadas imediatas de cancelamento de registro {#avoid-immediate-unregister-calls}

Evite chamar `logout` ou `unregisterPush` diretamente após registrar-se para notificações por push com o SO ou provedor de push. Devido ao processamento assíncrono do servidor, isso pode, raramente, readicionar o token de push ao usuário da Braze.

### Cancelar registro de push {#unregister-push}

Para parar de enviar push para um dispositivo sem limpeza automatizada adicional, use o método `unregisterPush`. Isso remove o token de push do dispositivo do usuário atual no servidor da Braze e limpa o token armazenado localmente.

O exemplo de retorno de chamada a seguir mostra como lidar com os resultados de `unregisterPush`. Use-o quando o seu fluxo for baseado em retorno de chamada e substitua o registro de log pelo seu próprio tratamento de nova tentativa.

```kotlin
// Completion callback
Braze.getInstance(context).unregisterPush { result ->
  result
    .onSuccess {
      Log.d(TAG, "Push unregistered successfully")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(
        TAG,
        "Push unregistration failed: ${error.message}, isRetriable: ${pushError?.isRetriable}"
      )
    }
}
```

O exemplo de coroutine a seguir mostra a API suspensa `unregisterPush`. Use-o em fluxos baseados em coroutine e personalize as ramificações de sucesso e falha para o seu app.

```kotlin
lifecycleScope.launch {
  runCatching { Braze.getInstance(context).unregisterPush() }
    .onSuccess {
      Log.d(TAG, "Push unregistered successfully")
    }
    .onFailure { error ->
      val pushError = error as? BrazePushUnregistrationException
      Log.e(
        TAG,
        "Push unregistration failed: ${error.message}, isRetriable: ${pushError?.isRetriable}"
      )
    }
}
```

#### Registrar-se novamente para push após `unregisterPush` {#re-register-push-after-unregisterpush}

Após chamar `unregisterPush`, registre-se novamente para notificações com o seu SO ou provedor de push seguindo a [configuração de push para Android]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) antes de enviar notificações por push da Braze novamente.

#### Evite chamadas imediatas de cancelamento de registro

Evite chamar `logout` ou `unregisterPush` diretamente após registrar-se para notificações por push com o SO ou provedor de push. Devido ao processamento assíncrono do servidor, isso pode, raramente, readicionar o token de push ao usuário da Braze.