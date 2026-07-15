---
nav_title: APIs e identificadores
article_title: APIs e identificadores
page_order: 0
page_type: reference
description: "Este artigo aborda a página APIs e identificadores, que exibe as identificações de API do seu espaço de trabalho."

---

# Chaves de API {#api-keys}

> A página **APIs e identificadores** é o hub centralizado para gerenciar todas as suas chaves da REST API em um só lugar. Aqui, você pode acessar o conjunto de chaves de API e identificadores de app de cada espaço de trabalho.

Você pode encontrar a página **APIs e identificadores** em **Configurações**.

## Chaves de API

Esta seção fornece as chaves da REST API do seu espaço de trabalho, os identificadores exclusivos que permitem o acesso aos dados de um espaço de trabalho. Uma chave da REST API é obrigatória em cada solicitação à API da Braze. Para saber mais sobre como criar e usar chaves de API, consulte nossa [visão geral da chave da REST API]({{site.baseurl}}/api/api_key).

### Lista de permissões de IP da API {#api-ip-allowlisting}

Para maior segurança, você pode especificar uma lista de endereços IP e sub-redes com permissão para fazer solicitações à REST API para uma determinada chave da REST API. Isso é chamado de lista de permissões (allowlisting ou whitelisting). Para permitir endereços IP ou sub-redes específicos, adicione-os à seção **Whitelist IPs** ao criar uma nova chave da REST API:

![Seção de lista de permissões de IP da API ao criar uma nova chave de API]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Se você não especificar nenhum, as solicitações poderão ser enviadas de qualquer endereço IP.

{% alert tip %}
Está criando um webhook da Braze para a Braze e usando lista de permissões? Confira nossa lista de [IPs para lista de permissões]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-whitelisting).
{% endalert %}

### Alertas de uso da API {#api-usage-alerts}

Configure alertas de uso da API para monitorar atividades importantes da API e identificar problemas antecipadamente. Esses alertas ajudam a detectar padrões de tráfego inesperados antes que afetem sua experiência.

Você pode rastrear dois tipos de atividade da API:

- **Endpoints da REST API:** ações como enviar mensagens, criar campanhas ou exportar dados.
- **Solicitações da API do SDK:** eventos da sua experiência do cliente, como disparar mensagens no app ou sincronizar perfis de usuário. *Esse recurso está disponível se você adquiriu Monthly Active Users (CY 24–25).*

Depois de escolher o que rastrear, você pode definir as condições do alerta. Por exemplo, ser notificado se as respostas de erro aumentarem 20% em uma hora. Você receberá uma notificação por e-mail, webhook ou ambos, dependendo das suas configurações. Para começar, consulte [Alertas de uso da API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts).

## Identificadores de app {#app-identifiers}

Esta seção inclui uma lista de identificadores usados para referenciar apps específicos em solicitações feitas à API da Braze. Para saber mais sobre identificadores de aplicativo, consulte [Chave de API do identificador de app]({{site.baseurl}}/api/identifier_types).

## Outros identificadores {#other-identifiers}

Para integrar com nossa API, você pode pesquisar os identificadores relacionados a quaisquer Segments, Campaigns, Content Cards e mais que deseja acessar pela API externa da Braze. Todas as mensagens devem seguir a codificação [UTF-8](https://en.wikipedia.org/wiki/UTF-8). Depois de selecionar qualquer um deles, o identificador será exibido abaixo do menu suspenso.

Para saber mais, consulte [Tipos de identificadores de API]({{site.baseurl}}/api/identifier_types).