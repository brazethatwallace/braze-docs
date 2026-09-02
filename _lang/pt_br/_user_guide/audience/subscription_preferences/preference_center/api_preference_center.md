---
nav_title: Central de Preferências de e-mail via API
article_title: Central de Preferências de e-mail via API
page_order: 1
description: "Este artigo descreve a Central de Preferências de e-mail via API e como personalizá-la."
channel:
  - email
---

# Central de Preferências de e-mail via API {#api-email-preference-center}

> Configurar uma Central de Preferências oferece um local centralizado para que seus usuários editem e gerenciem suas preferências de notificação para o [envio de mensagens por e-mail]({{site.baseurl}}/user_guide/channels/email). Este artigo inclui etapas para criar uma Central de Preferências gerada por API, mas você também pode criar uma Central de Preferências usando o [editor de arrastar e soltar]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center).

{% multi_lang_include alerts/tip_alerts.md alert="Landing pages manage subscriptions" %}

No dashboard da Braze, acesse **Audience** > **Email Preference Centers**.

Aqui é onde você pode gerenciar e visualizar cada grupo de inscrições. Cada grupo de inscrições que você criar será adicionado a esta lista da Central de Preferências. Você pode criar múltiplas centrais de preferências.

{% alert important %}
A Central de Preferências foi projetada para ser usada dentro do canal de e-mail da Braze. Os links da Central de Preferências são dinâmicos com base em cada usuário e não podem ser hospedados externamente.
{% endalert %}

## Criar uma Central de Preferências com API {#create-a-preference-center-with-api}

Ao usar os [endpoints da Central de Preferências da Braze]({{site.baseurl}}/api/endpoints/preference_center), você pode criar uma Central de Preferências, um site hospedado pela Braze, que pode exibir o estado de inscrição e os status dos grupos de inscrições dos seus usuários. Usando HTML e CSS, sua equipe de desenvolvedores pode construir a Central de Preferências para que o estilo da página esteja alinhado com as diretrizes da sua marca.

O uso de Liquid permite recuperar os nomes dos seus grupos de inscrições e o status de cada usuário. Dessa forma, a Braze armazena e recupera esses dados quando a página é carregada.

### Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Central de Preferências ativada | Seu dashboard da Braze tem permissões para usar o recurso de Central de Preferências. |
| Espaço de trabalho válido com um grupo de inscrições para e-mail, SMS ou WhatsApp | Um espaço de trabalho funcional com usuários válidos e um grupo de inscrições para e-mail, SMS ou WhatsApp. |
| Usuário válido | Um usuário com um endereço de e-mail e um ID externo. |
| Chave de API gerada com permissões da Central de Preferências | No dashboard da Braze, acesse **Configurações** > **Chaves de API** para confirmar que você tem acesso a uma chave de API com permissões da Central de Preferências. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

### Etapa 1: Usar o endpoint Criar Central de Preferências {#step-1-use-the-create-preference-center-endpoint}

Vamos começar a construir uma Central de Preferências usando o [endpoint Criar Central de Preferências]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center). Para personalizar sua Central de Preferências, você pode incluir HTML alinhado com a identidade da sua marca nos campos `preference_center_page_html` e `confirmation_page_html`.

O [endpoint Gerar URL da Central de Preferências]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) permite obter a URL da Central de Preferências para um usuário específico fora de um e-mail enviado pela Braze.

{% alert note %}
A Braze renderiza `confirmation_page_html` em um iframe que usa uma URL `data:`. Os navegadores tratam URLs `data:` como origens opacas. Como resultado, scripts nesse iframe não conseguem carregar recursos externos adicionais, e a navegação na janela pai ou a comunicação entre frames a partir dessa página falha.<br><br>Em vez disso, você pode criar um link para conteúdo externo, como uma URL de pesquisa hospedada, em vez de incorporar scripts. Se você precisar incorporar uma ferramenta de terceiros e o fornecedor permitir, use um `<iframe title="Descrição do conteúdo incorporado" src="https://example.com/...">` apontando para a URL HTTPS hospedada da ferramenta.
{% endalert %}

### Etapa 2: Incluir na sua campanha de e-mail {#step-2-include-in-your-email-campaign}

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Para inserir um link para a Central de Preferências nos seus e-mails, use a seguinte Liquid tag no local desejado do seu e-mail, de forma semelhante a como você inseriria URLs de cancelamento de inscrição.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Você também pode usar uma combinação de HTML que inclua Liquid. Por exemplo, você pode colar o seguinte como URL no editor de HTML ou no editor de arrastar e soltar. Isso exibe o layout básico da Central de Preferências que lista todos os grupos de inscrições para e-mail automaticamente. Se você usar [alias de link]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing), adicione um ponto de interrogação (`?`) após a Liquid tag para que a Braze possa anexar parâmetros de rastreamento.

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}?">Edit your preferences</a>
```
{%endraw%}

A Central de Preferências tem uma caixa de seleção que permite que seus usuários cancelem a inscrição de todos os e-mails.

{% multi_lang_include preference_center/testing.md section="api" %}

#### Editar uma Central de Preferências {#edit-a-preference-center}

Você pode editar e atualizar sua Central de Preferências usando o [endpoint Atualizar Central de Preferências]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center).

#### Identificar Centrais de Preferências e detalhes {#identify-preference-centers-and-details}

Para identificar suas Centrais de Preferências, use o [endpoint Visualizar detalhes da Central de Preferências]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) para retornar informações relacionadas, como o timestamp da última atualização, o ID da Central de Preferências e mais.

## Personalizar uma Central de Preferências {#customize-a-preference-center}

A Braze gerencia as atualizações de estado de inscrição da Central de Preferências, o que mantém a Central de Preferências sincronizada. No entanto, você também pode criar e hospedar sua própria Central de Preferências usando as [APIs de grupos de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups) com as seguintes opções.

### Opção 1: Link com parâmetros de string de consulta {#option-1-link-with-string-query-parameters}

Use pares de campo-valor de string de consulta no corpo da URL para passar o ID do usuário e a categoria de e-mail para a página, de modo que os usuários só precisem confirmar sua escolha para cancelar a inscrição. Essa opção é ideal para quem armazena um identificador de usuário em formato hash e ainda não possui uma central de inscrições.

Para essa opção, cada categoria de e-mail requer seu próprio link de cancelamento de inscrição específico:<br>
`http://mycompany.com/query-string-form-fill?field_id=Alex&field_category=offers`

{% alert tip %}
Também é possível aplicar hash ao ID externo do usuário no momento do envio usando um filtro Liquid. Isso converterá o `user_id` em um valor de hash MD5, por exemplo:
{% raw %}
```liquid
{% assign my_string = ${user_id} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### Opção 2: Autenticar com JSON web token {#option-2-authenticate-with-json-web-token}

Use um [JSON web token](https://auth0.com/learn/json-web-tokens/) para autenticar usuários em uma parte do seu servidor web (por exemplo, preferências da conta) que normalmente está protegida por uma camada de autenticação, como login com nome de usuário e senha.

Essa abordagem não requer pares de campo-valor de string de consulta incorporados na URL, pois eles podem ser passados na carga útil do JSON web token, por exemplo:

```json
{
    "user_id": "1234567890",
    "name": "Alex Smith",
    "category": "offers"
}
```

## Perguntas frequentes {#frequently-asked-questions}

### Por que minha Central de Preferências não funciona em um envio de teste? {#why-doesnt-my-preference-center-work-in-a-test-send}

Os links da Central de Preferências exigem um contexto de envio real. Envios de teste não geram URLs válidas da Central de Preferências, e o botão **Salvar Preferências** fica desativado se a página for carregada. Esse é o comportamento esperado. Para testar de ponta a ponta, lance uma Campaign ou etapa do Canvas para um usuário teste ou um Segment interno pequeno, ou use o [endpoint Gerar URL da Central de Preferências]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center). Para mais detalhes, consulte [Testando Centrais de Preferências](#testing-preference-centers).

### Eu não criei uma Central de Preferências. Por que estou vendo "PreferenceCenterBrazeDefault" no meu dashboard? {#i-havent-created-a-preference-center-why-am-i-seeing-preferencecenterbrazedefault-on-my-dashboard}

Isso é usado para renderizar a Central de Preferências quando o Liquid legado {%raw%}`${preference_center_url}`{%endraw%} é utilizado, o que significa que etapas do Canvas ou modelos que referenciam {%raw%}`${preference_center_url}` ou `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} não funcionarão. Isso também se aplica a mensagens enviadas anteriormente que incluíam o Liquid legado ou "PreferenceCenterBrazeDefault" como parte da mensagem.

Se você referenciar {%raw%}`${preference_center_url}`{%endraw%} em uma nova mensagem novamente, uma Central de Preferências chamada "PreferenceCenterBrazeDefault" será criada novamente.

### As Centrais de Preferências suportam múltiplos idiomas? {#do-preference-centers-support-multiple-languages}

Não. No entanto, você pode alavancar o Liquid ao escrever o HTML para páginas personalizadas de aceitação e cancelamento de inscrição. Se você estiver usando links dinâmicos para gerenciar cancelamentos de inscrição, trata-se de um único link.

Por exemplo, se você estiver rastreando a taxa de cancelamento de inscrição para usuários que falam espanhol, seria necessário usar Campaigns separadas ou alavancar análise de dados com o Currents (como verificar quando um usuário cancela a inscrição e checar o idioma preferido desse usuário).

Como outro exemplo, para rastrear taxas de cancelamento de inscrição para usuários que falam espanhol, você poderia adicionar uma string de parâmetro de consulta como `?Spanish=true` à URL de cancelamento de inscrição se o idioma do usuário for espanhol e usar um link de cancelamento de inscrição regular caso contrário:

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

Então, por meio do Currents, você poderia identificar quais usuários falam espanhol e quantos eventos de clique houve para esse link de cancelamento de inscrição.

### Tanto os links de cancelamento de inscrição quanto as Centrais de Preferências de e-mail são obrigatórios para envio? {#are-both-unsubscribe-links-and-email-preference-centers-required-for-sending}

Não. Se você vir a mensagem "Your Email Body does not include an unsubscribe link" ao compor uma Campaign de e-mail, esse alerta é esperado se o seu link de cancelamento de inscrição estiver em um bloco de conteúdo.

### Como atualizo o ícone padrão do navegador? {#how-do-i-update-the-default-browser-icon}

Por padrão, o ícone ao lado do nome da guia do navegador (favicon) usa o logotipo da Braze. Para adicionar um favicon personalizado, defina-o por meio do atributo `links-tags` na sua chamada de API para Criar ou Atualizar a [Central de Preferências]({{site.baseurl}}/api/endpoints/preference_center). A Braze então injeta a tag {% raw %}`<link rel="icon" ...>`{% endraw %} na página hospedada para você.

{% raw %}
```
{
  "name": "MyPreferenceCenter",
  "preference_center_title": "Email Preferences",
  "preference_center_page_html": "<!doctype html> ...",
  "confirmation_page_html": "<!doctype html> ...",
  "state": "active",
  "options": {
    "links-tags": [
      {
        "rel": "icon",
        "type": "image/png",
        "sizes": "32x32",
        "href": "https://yourcdn.com/path/to/favicon-32x32.png"
      },
      {
        "rel": "shortcut icon",
        "type": "image/x-icon",
        "href": "https://yourcdn.com/path/to/favicon.ico"
      },
      {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://yourcdn.com/path/to/apple-touch-icon.png"
      }
    ]
  }
}
```
{% endraw %}