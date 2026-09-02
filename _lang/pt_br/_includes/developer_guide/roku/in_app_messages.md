{% multi_lang_include developer_guide/prerequisites/roku.md %} Além disso, as mensagens no app só serão enviadas para dispositivos Roku que estejam executando a versão mínima suportada do SDK:

{% sdk_min_versions roku:0.1.2 %}

## Tipos de mensagem {#message-types}

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Ativar mensagens no app {#enabling-in-app-messages}

### Etapa 1: Adicionar um observador {#step-1-add-an-observer}

Para processar mensagens no app, você pode adicionar um observador em `BrazeTask.BrazeInAppMessage`:

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

### Etapa 2: Acessar mensagens disparadas {#step-2-access-triggered-messages}

Dentro do seu manipulador, você tem acesso à mensagem no app de maior prioridade que suas campanhas dispararam:

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## Campos de mensagem {#message-fields}

### Tratamento {#handling}

A seguir estão os campos que você precisará para gerenciar suas mensagens no app:

| Campos | Descrição |
| ------ | ----------- |
| `buttons` | Lista de botões (pode ser uma lista vazia). |
| `click_action` | `"URI"` ou `"NONE"`. Use este campo para indicar se a mensagem no app deve abrir um link URI ou fechar a mensagem quando clicada. Quando não houver botões, isso deve acontecer quando o usuário clicar em "OK" enquanto a mensagem no app estiver sendo exibida. |
| `dismiss_type` | `"AUTO_DISMISS"` ou `"SWIPE"`. Use este campo para indicar se sua mensagem no app será descartada automaticamente ou se exigirá um deslize para ser descartada. |
| `display_delay` | Quanto tempo (em segundos) esperar até exibir a mensagem no app. |
| `duration` | Por quanto tempo (em milissegundos) a mensagem deve ser exibida quando `dismiss_type` está configurado como `"AUTO_DISMISS"`. |
| `extras` | Pares chave-valor. |
| `header` | O texto do cabeçalho. |
| `id` | O ID usado para registrar impressões ou cliques. |
| `image_url` | URL da imagem da mensagem no app. |
| `message` | Texto do corpo da mensagem. |
| `uri` | A URI para a qual os usuários serão direcionados com base no seu `click_action`. Este campo deve ser incluído quando `click_action` é `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Handling" }

{% alert important %}
Para mensagens no app que contêm botões, o `click_action` da mensagem também será incluído na carga útil final se a ação de clique for adicionada antes do texto do botão.
{% endalert %}

### Estilo {#styling}

Existem também vários campos de estilo que você pode usar a partir do dashboard:

| Campos | Descrição |
| ------ | ----------- |
| `bg_color` | Cor de fundo. |
| `close_button_color` | Cor do botão de fechar. |
| `frame_color` | A cor da sobreposição da tela de fundo. |
| `header_text_color` | Cor do texto do cabeçalho. |
| `message_text_color` | Cor do texto da mensagem. |
| `text_align` | "START", "CENTER" ou "END". O alinhamento de texto selecionado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Styling" }

Como alternativa, você pode implementar a mensagem no app e estilizá-la dentro do seu aplicativo Roku usando uma paleta padrão:

### Botões {#buttons}

| Campos | Descrição |
| ------ | ----------- |
| `click_action` | `"URI"` ou `"NONE"`. Use este campo para indicar se a mensagem no app deve abrir um link URI ou fechar a mensagem quando clicada. |
| `id` | O valor de ID do próprio botão. |
| `text` | O texto a ser exibido no botão. |
| `uri` | A URI para a qual os usuários serão direcionados com base no seu `click_action`. Este campo deve ser incluído quando `click_action` é `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Buttons" }