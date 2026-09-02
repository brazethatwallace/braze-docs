---
nav_title: Adikteev
article_title: Previsão de churn do Adikteev
description: "Este artigo de referência descreve a parceria entre a Braze e a Adikteev, um mecanismo de retenção de usuários que combina a previsão de churn com o redirecionamento de aplicativos full-service."
alias: /partners/adikteev/
page_type: partner
search_tag: Partner

---

# Previsão de churn do Adikteev {#adikteev-churn-prediction}

> A [Adikteev](https://www.adikteev.com/churn-prediction) é um mecanismo de retenção de usuários que combina a previsão de churn com o redirecionamento de aplicativos full-service.

_Essa integração é mantida pela Adikteev._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Adikteev permite aumentar a retenção de usuários, aproveitando a tecnologia de previsão de churn da Adikteev nas Campaigns do Braze CRM para direcionar prioritariamente os segmentos de usuários de alto risco.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta da Adikteev | É necessário ter uma conta Adikteev para aproveitar essa parceria. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com a permissão `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **APIs e identificadores**. |
| Endpoint REST or transferir estado representacional da Braze | [Sua URL de endpoint REST or transferir estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso {#use-cases}

{% tabs %}
{% tab Filtragem de público %}
Refinamento de seus segmentos de público com base no risco de churn.<br> Os nomes e valores dos atributos personalizados enviados pela Adikteev são configuráveis.

![Uma captura de tela mostrando um exemplo de como usar um atributo personalizado enviado pela Adikteev como um filtro de segmento de público.]({% image_buster /assets/img/adikteev/audience.png %})
{% endtab %}
{% tab Direcionamento de mensagens %}
Personalização de suas campanhas de envio de mensagens da Braze com base no risco de churn dos destinatários.

![Uma captura de tela mostrando um exemplo de como usar um atributo personalizado enviado pela Adikteev como um filtro de direcionamento de campanha.]({% image_buster /assets/img/adikteev/campaign.png %})
{% endtab %}
{% endtabs %}

## Integração {#integration}

### Etapa 1: Compartilhe o fluxo de eventos do seu app {#step-1-share-the-event-stream-of-your-app}

Para começar a executar a previsão de churn no público do seu app, a Adikteev precisará que você ative os postbacks de eventos da sua plataforma de medição móvel. Siga as diretrizes no [site de suporte da Adikteev](https://help.adikteev.com/hc/en-us/sections/8185123408914-Data-stream-activation) para configurar isso.

### Etapa 2: Crie sua chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze {#step-2-create-your-braze-rest-api-key}

Na Braze, navegue até **Configurações** > **APIs e identificadores**. Selecione **Criar nova chave de API or interface de programação do aplicativo (API)**, digite o nome da chave de API or interface de programação do aplicativo (API) de sua escolha e verifique se a permissão a seguir foi adicionada:

- `users.track`

### Etapa 3: Forneça informações à equipe da Adikteev {#step-3-provide-information-to-the-adikteev-team}

Para concluir a integração, você deve fornecer sua chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional e a URL do endpoint REST or transferir estado representacional ao gerente da sua conta na Adikteev. A Adikteev estabelecerá a conexão e entrará em contato com você após a conclusão da configuração para validar a integração.

## Loteamento e limites de taxa {#batching-and-rate-limits}

O endpoint `user.track` é usado para atualizar detalhes sobre seus usuários. Consulte a [documentação da API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para obter detalhes completos sobre os limites de taxa do endpoint, solicitações em lote e detalhes da solicitação.

{% alert tip %}
Lembre-se de que as chamadas de API or interface de programação do aplicativo (API) devem ser feitas apenas para atualizar dados que foram alterados, a fim de reduzir o número total de chamadas. Em outras palavras, atualize apenas os usuários cujo Segment or segmento or segmento de churn foi alterado.
{% endalert %}

## Identificadores de usuários e dispositivos {#user-and-device-identifiers}

Os perfis de usuário na Braze podem ser associados a qualquer tipo de identificador de usuário ou dispositivo; a lista de opções disponíveis depende de como você integrou a coleta de dados com a Braze. Para a Adikteev, será necessário encontrar um identificador comum entre o seu MMP e os perfis de usuário na Braze para enviar as informações do Segment or segmento or segmento de churn corretamente.

## Retenção e exclusão de dados {#data-retention-and-deletion}

Se nenhuma atualização for feita, o atributo e seu valor serão mantidos indefinidamente nos perfis de usuário da Braze.

Para remover um atributo de perfil, defina-o como `null`.

## Cargas úteis de solicitação {#request-payloads}

A carga útil enviada da Adikteev para a Braze é personalizável e pode ser configurada para atender às necessidades do cliente. Isso inclui a configuração dos identificadores usados, o nome do atributo personalizado e se a Adikteev pode criar novos usuários na Braze ou apenas atualizar os usuários existentes.


## Suporte e solução de problemas {#support-and-troubleshooting}

Entre em contato com o gerente de contas da Adikteev para tirar dúvidas relacionadas à integração ou para obter suporte para seus casos de uso.