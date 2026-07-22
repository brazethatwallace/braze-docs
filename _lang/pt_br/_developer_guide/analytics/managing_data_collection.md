---
nav_title: Gerenciar a coleta de dados
article_title: Gerenciar a coleta de dados para o SDK da Braze
page_order: 8
description: "Aprenda a gerenciar a coleta de dados para o SDK da Braze."

---

# Gerenciar a coleta de dados {#manage-data-collection}

> Aprenda a gerenciar a coleta de dados para o SDK da Braze, para que você possa cumprir todas as regulamentações de privacidade de dados, conforme necessário.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/analytics/managing_data_collection.md %}
{% endsdktab %}

{% sdktab android %}
## Questionário de privacidade do Google Play {#privacy-questionnaire}

A partir de abril de 2022, os desenvolvedores de Android deverão preencher o [formulário de segurança de dados](https://support.google.com/googleplay/android-developer/answer/10787469) do Google Play para divulgar práticas de privacidade e segurança. Este guia fornece instruções sobre como preencher esse novo formulário com informações sobre como a Braze lida com os dados do seu app.

Como desenvolvedor do app, você tem o controle dos dados que envia à Braze. Os dados recebidos pela Braze são processados de acordo com suas instruções. Isso é o que o Google classifica como um [prestador de serviço](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform).

{% alert important %}
Este artigo traz informações relacionadas aos dados que o SDK da Braze processa em relação ao questionário da seção de segurança do Google. Este artigo não fornece orientação jurídica, portanto, recomendamos consultar sua equipe jurídica antes de enviar qualquer informação ao Google.
{% endalert %}

### Perguntas {#questions}

| Perguntas | Respostas para o SDK da Braze |
|---|---|
| O seu app coleta ou compartilha algum dos tipos de dados de usuários necessários? | Sim, o SDK da Braze para Android coleta dados conforme configurado pelo desenvolvedor do app. |
| Todos os dados de usuários coletados pelo seu app são criptografados em trânsito? | Sim. |
| Você oferece uma forma para os usuários solicitarem a exclusão dos seus dados? | Sim. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Perguntas" }

Para saber mais sobre como lidar com solicitações de dados e exclusão de usuários, consulte [Informações de retenção de dados da Braze]({{site.baseurl}}/api/data_retention).

### Coleta de dados {#data-collection}

Os dados coletados pela Braze são determinados pela sua integração específica e pelos dados de usuários que você escolhe coletar. Para saber mais sobre quais dados a Braze coleta por padrão e como desativar determinados atributos, consulte nossas [opções de coleta de dados do SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection#minimum-integration).

<table aria-label="Coleta de dados" id="datatypes">
    <thead>
        <tr>
            <th width="25%">Categoria</th>
            <th width="25%">Tipo de dado</th>
            <th width="50%">Uso pela Braze</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">Localização</td>
            <td>Localização aproximada</td>
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
            <td rowspan="2">Saúde e fitness</td>
            <td>Informações de saúde</td>
            <td rowspan="2">Não coletado por padrão.</td>
        </tr>
        <tr>
            <td>Informações de fitness</td>
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
            <td>Se você envia mensagens no app ou notificações por push pela Braze, coletamos informações sobre quando os usuários abriram ou leram essas mensagens.</td>
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
            <td>Interações com o app</td>
            <td>A Braze coleta dados de atividade de sessão por padrão. Todas as outras interações e atividades são determinadas pela integração personalizada do seu app.</td>
        </tr>
        <tr>
            <td>Histórico de pesquisa no app</td>
            <td>Não coletado.</td>
        </tr>
        <tr>
            <td>Apps instalados</td>
            <td>Não coletado.</td>
        </tr>
        <tr>
            <td>Outro conteúdo gerado pelo usuário</td>
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
            <td>Logs de falhas</td>
            <td>A Braze coleta logs de falhas para erros que ocorrem no SDK. Esses logs contêm o modelo do telefone e o nível do sistema operacional do usuário, além de um ID de usuário específico da Braze.</td>
        </tr>
        <tr>
            <td>Diagnósticos</td>
            <td>Não coletado.</td>
        </tr>
        <tr>
            <td>Outros dados de desempenho do app</td>
            <td>Não coletado.</td>
        </tr>
        <tr>
            <td>Dispositivo ou outros IDs</td>
            <td>Dispositivo ou outros IDs</td>
            <td>A Braze gera um ID de dispositivo para diferenciar os dispositivos dos usuários e verifica se as mensagens são enviadas ao dispositivo correto.</td>
        </tr>
    </tbody>
</table>

Para saber mais sobre outros dados de dispositivo que a Braze coleta e que podem estar fora do escopo das diretrizes de segurança de dados do Google Play, consulte nossa [visão geral de armazenamento do Android]({{site.baseurl}}/developer_guide/storage/?tab=android) e nossas [opções de coleta de dados do SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection#minimum-integration).

## Desabilitando o rastreamento de dados {#disabling-data-tracking}

Para desabilitar a atividade de rastreamento de dados no SDK para Android, use o método [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html). Isso fará com que todas as conexões de rede sejam canceladas, o que significa que o SDK da Braze não enviará mais nenhum dado para os servidores da Braze.

## Limpando dados armazenados anteriormente {#wiping-previously-stored-data}

Você pode usar o método [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) para limpar completamente todos os dados do lado do cliente armazenados no dispositivo.

## Retomando o rastreamento de dados {#resuming-data-tracking}

Para retomar a coleta de dados, você pode usar o método [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html). Lembre-se de que isso não restaura nenhum dado previamente apagado.

{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/analytics/managing_data_collection.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/analytics/managing_data_collection.md %}
{% endsdktab %}

{% sdktab roku %}
{% multi_lang_include developer_guide/roku/analytics/managing_data_collection.md %}
{% endsdktab %}

{% endsdktabs %}