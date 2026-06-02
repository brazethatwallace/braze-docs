---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "Este artigo de referência descreve a parceria entre a Braze e a Punchh, uma plataforma de fidelidade e engajamento. Com ela, você pode sincronizar dados entre as duas plataformas. Os dados publicados na Braze estarão disponíveis para segmentação e poderão sincronizar os dados de usuários de volta à Punchh por meio de modelos de webhook configurados na Braze."
page_type: partner
search_tag: Partner

---

# Punchh

> A [Punchh](https://punchh.com/) é uma plataforma de fidelidade e engajamento líder do setor que permite às marcas oferecer programas de fidelidade do cliente omnicanal, tanto na loja quanto digitalmente.

_Essa integração é mantida pela Punchh._

## Sobre a integração {#about-the-integration}

A integração da Braze com a Punchh permite que você sincronize dados para fins de presentes e fidelidade nas duas plataformas. Os dados publicados na Braze estarão disponíveis para segmentação e poderão sincronizar os dados de usuários de volta à Punchh por meio de webhooks da Braze.

## Quais são os benefícios? {#what-are-the-benefits}

- Ingerir dados de fidelidade da Punchh para a Braze em tempo real.
- Usar e estratificar os poderosos dados de público da Braze para oferecer experiências significativas e dinâmicas em vários canais (app, celular, web, e-mail e SMS).
  - Os clientes abriram os e-mails? Os clientes abriram o app perto de uma loja?
- Padronizar a aparência dos e-mails de transação enviados pela Braze.
- Criar jornadas que permitam testes A/B e otimização à medida que você avança.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Punchh | Você precisa ter uma conta ativa na Punchh para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/api/basics/#endpoints). Seu endpoint depende da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## O que mais devo saber? {#what-else-should-i-know}

#### Antes de integrar {#before-integrating}

- Ao utilizar a integração da Braze, serão necessárias duas campanhas, uma na Punchh e a segunda na Braze. Por exemplo, se você enviar uma campanha com uma oferta anexada, a campanha de presentes será configurada na Punchh, e a notificação poderá ser enviada pela Braze.
- Os convidados já devem existir na Punchh e na Braze. A Punchh filtrará qualquer cliente que ainda não seja um cliente de fidelidade.

#### Pontos importantes a serem notados {#important-things-to-note}

- A Punchh adicionou a capacidade de desativar o envio de atributos padrão de usuários para a Braze, para que o cliente não incorra em excedentes de pontos de dados. Isso é configurado durante a configuração do adaptador.
- Se estiver usando segmentos personalizados em campanhas recorrentes, o nome da campanha deve ser usado em vez do ID da campanha, pois os IDs mudam a cada vez que a campanha é executada.
- Os canais de comunicação disponíveis em cada campanha de presentes da Punchh incluem mensagens ricas, notificações por push, SMS e e-mail.
- Depois que os usuários forem enviados para um segmento personalizado da Punchh a partir da Braze, eles não poderão ser removidos. Somente novos convidados podem ser adicionados a um segmento personalizado existente. Se os convidados precisarem ser removidos de um segmento personalizado da Punchh existente, será necessário criar uma nova campanha de webhook na Braze para enviar os usuários a um novo segmento personalizado da Punchh.

## Integração {#integration}

A Punchh oferece vários endpoints disponíveis aos clientes da Braze para ajudar a adicionar IDs externos à plataforma Punchh usando os seguintes endpoints da API da Punchh. Depois que os IDs externos forem adicionados, crie um adaptador na Punchh, forneça suas credenciais da Braze e selecione os eventos que deseja sincronizar. Em seguida, você pode pegar o ID do segmento da Punchh e usá-lo para criar um webhook da Punchh para disparar a sincronização do cliente em uma jornada do Canvas.

Observe que o `user_id` da Punchh e o `external_id` da Braze precisam estar disponíveis em qualquer uma das plataformas para que a integração seja sincronizada corretamente.
- Os eventos enviados da Punchh para a Braze incluirão o `external_id` da Braze como identificador. Se a Punchh estiver configurada para usar o `external_source_id`, esse valor será definido como o `external_id` da Braze. Caso contrário, a integração terá como padrão a configuração do `user_id` da Punchh como `external_id` da Braze.
- Para enviar webhooks da Braze para a Punchh, o `user_id` da Punchh deve estar disponível no perfil do usuário da Braze. Se o `user_id` da Punchh não for usado como `external_id` da Braze, ele deverá ser definido como um atributo personalizado "punchh_user_id".

### Etapa 1: Configurar endpoints de ingestão de ID externo (opcional) {#step-1-set-up-external-id-ingestion-endpoints-optional}

Os IDs externos da Braze podem ser adicionados usando os seguintes endpoints para usuários novos e existentes da Punchh.

{% alert important %}
Os valores dos campos `external_source` e `external_source_id` devem ser exclusivos da Punchh e não devem estar associados a perfis existentes.
{% endalert %}

1. Novos usuários da Punchh<br>
Crie novos usuários na Punchh com um endpoint de inscrição da Punchh usando os campos `external_source` e `external_source_id`. A Punchh permite que identificadores externos sejam enviados com um perfil de usuário por meio de um dos seguintes endpoints de inscrição:
- [API de inscrição móvel](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [API de inscrição por SSO](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. Usuários existentes da Punchh <br>
Atualize o `external_source_id` para os usuários existentes da Punchh. A Punchh permite que identificadores externos sejam adicionados a um perfil por meio de um endpoint de atualização da API do usuário:
- [Atualização do usuário móvel](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [Atualização do usuário SSO](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [Atualização do usuário do dashboard](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs local %}
{% tab User sign-up API example %}
Este exemplo permite enviar identificadores externos com um perfil de usuário no momento da inscrição. Isso é feito enviando `external_source` como "customer_id" e `external_source_id` como "111111111111111111" como um tipo de dados string.

```bash
curl --location --request POST 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"CLIENT",
    "user" : {
      "email": "test@example.com",
      "password": "PASSWORD",
      "first_name":"FIRST_NAME",
      "last_name":"LAST_NAME",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"111111111111111111"
      }
}'
```
{% endtab %}
{% tab User update API example %}
Este exemplo permite que você atualize identificadores externos com um perfil de usuário. Isso é feito enviando `external_source` como "customer_id" e `external_source_id` como "111111111111111111" como um tipo de dados string.

```bash
curl --location --request PUT 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Authorization: Bearer ACCESS_TOKEN' \
--data-raw '{
    "client":"CLIENT",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"111111111111111111"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
**Configuração da plataforma:** Para ativar os identificadores externos na Punchh, no dashboard da Punchh, navegue até **Cockpit** > **Dashboard** > **External User Identifier**.
{% endalert %}

### Etapa 2: Configuração do adaptador da Braze na Punchh {#step-2-braze-adapter-setup-in-punchh}

#### Eventos disponíveis para sincronização {#available-events-to-sync}

1. **Convidado:** Disparado em qualquer inscrição, atualização do perfil do convidado, desativação ou exclusão
2. **Check-in de fidelidade:** Disparado para transações de fidelidade ou ganhos por meio da leitura do código de barras do recibo
3. **Check-in de presentes:** Disparado para pontos concedidos em uma campanha
4. **Resgate:** Disparado no caso de qualquer resgate de recompensas, excluindo os cupons da Punchh, pois eles seriam enviados separadamente como eventos de cupom, incluindo a emissão e o resgate
5. **Recompensas:** Disparado a partir de recompensas oferecidas por campanhas, atividades, conversão de pontos em recompensas ou ofertas de administradores
6. **Notificações de transação:** Disparado após a atividade transacional de um usuário no sistema Punchh (por exemplo, expiração de pontos)
7. **Notificações de marketing:** Disparado com base em diferentes configurações de campanha na Punchh para um segmento associado de usuários

{% alert note %}
Consulte a documentação da Punchh para saber como podem ser as cargas úteis de exemplo desses eventos disponíveis.
{% endalert %}

Trabalhe com seu gerente de implementação da Punchh para configurar esse adaptador.

Para configurar a integração da Braze com a Punchh, faça o seguinte:

1. No dashboard da Punchh, navegue até **Cockpit** > **Dashboard** > **Major Features** > **Enable Webhook Management** e ative a opção **Enable Webhook Management**.<br><br>
2. Em seguida, ative os adaptadores navegando até **Settings** > **Webhooks Manager** > **Configurations** > **Show Adapters Tab** e ative **Show Adapters Tab**.<br><br>
3. Navegue até **Webhooks Manager** na guia **Settings**, selecione a guia **Adapters** e clique em **Create Adapter**. <br><br>![]({% image_buster /assets/img/punchh/punchh1.png %})<br><br>
4. Preencha o nome do adaptador, a descrição e o e-mail do administrador. Selecione **Braze** como seu adaptador e forneça seu endpoint da REST API da Braze e a chave de API da Braze.<br><br>
5. Em seguida, selecione os eventos disponíveis que gostaria de ativar. Uma lista desses eventos pode ser encontrada em [Eventos disponíveis para sincronização](#available-events-to-sync).<br><br>![]({% image_buster /assets/img/punchh/punchh3.png %})<br><br>
6. Clique em **Submit** para ativar o webhook.

## Criar webhook da Punchh na Braze {#create-punchh-webhook-in-braze}

A Braze pode adicionar usuários a um segmento da Punchh por meio de webhooks que utilizam os segmentos personalizados da Punchh.

1. Crie um segmento personalizado na Punchh e anote o `custom_segment_id` presente na URL do dashboard do segmento da Punchh, conforme mostrado abaixo. Podem ser usados os criadores de segmentos clássicos ou beta. No entanto, a versão beta é recomendada, pois a versão clássica acabará sendo descontinuada.<br><br>Na plataforma Punchh, navegue até **Guest** > **Segment** > **Custom List** > **New Custom List**.<br><br>![]({% image_buster /assets/img/punchh/update1.png %})<br><br>

2. Crie uma campanha de webhook na Braze usando o endpoint da Punchh para adicionar um usuário a um segmento personalizado como a URL do webhook. Aqui você pode fornecer o `custom_segment_id` extraído da URL e o `user_id` como pares de valores-chave.<br><br>![]({% image_buster /assets/img/punchh/punchh4.png %})<br><br>

3. Esse webhook pode ser configurado como uma campanha singular ou como uma etapa de um Canvas. Como alternativa, se o webhook que adiciona usuários a esse segmento específico da Punchh for usado em várias Campaigns ou Canvas, ele poderá ser configurado como um [modelo]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates/).<br><br>
A chave `user_id` no webhook mapeia o ID de usuário da Punchh. Esse identificador precisará ser adicionado a todos os webhooks criados na Braze para adicionar usuários a um segmento personalizado da Punchh. O atributo personalizado `punchh_user_id` pode ser preenchido dinamicamente como o valor da chave `user_id` usando o [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#pre-formatted-variables). Você pode inserir a variável de atributo personalizado `punchh_user_id` usando o ícone azul de "mais", localizado no canto superior direito de qualquer campo de texto de modelo.<br><br>![]({% image_buster /assets/img/punchh/update3.png %}){: style="max-width:65%;"}<br><br>![]({% image_buster /assets/img/punchh/update4.png %}){: style="max-width:65%;"}<br><br>

4. Depois que o webhook é salvo, ele pode ser usado para sincronizar usuários, conforme mostrado abaixo. Por exemplo, 136 convidados seriam adicionados ao segmento personalizado da Punchh quando essa campanha de webhook da Braze fosse lançada.<br><br>![Um exemplo de sincronização de usuários usando o webhook salvo devido à integração da Braze com a Punchh.]({% image_buster /assets/img/punchh/punchh6.png %})

Para saber mais sobre como os webhooks são usados na Braze, consulte [Criar um webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).

## Campanhas de casos de uso {#use-case-campaigns}

### Configuração de Campaign e Canvas {#campaign-and-canvas-configuration}

#### Disparo {#triggering}

Os casos de uso para envio de mensagens da Braze acionados por eventos da Punchh enviados à Braze, como eventos de recompensas ou eventos de convidados, podem ser criados como [Campaigns baseadas em ações]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#action-based-delivery) ou Canvas disparados pelo evento relevante da Punchh.

A adição de um gatilho abre a lista de eventos criados na Braze. Escolha o evento que deve disparar sua Campaign ou Canvas a ser enviado ao usuário que registrou o evento.

![]({% image_buster /assets/img/punchh/update5.png %})

Filtros de propriedade podem ser adicionados para filtrar ainda mais o evento de disparo. Por exemplo, a mensagem só deve ser disparada quando um cliente acionar o evento "checkins_gift" em que a propriedade do evento aprovado for `true`. Esse é um recurso opcional que pode não ser aplicável a todos os casos de uso.

#### Segmentação {#segmentation}

Em muitos casos, as Campaigns e Canvas da Braze acionados por eventos da Punchh podem ser definidos para um público de "Todos os usuários" porque a segmentação dos usuários que disparam esses eventos é determinada na Punchh. No entanto, os clientes que desejam refinar ainda mais o público de usuários que receberão o envio de mensagens da Braze disparado pelo evento podem fazê-lo adicionando filtros e segmentos adicionais na seção **Target Audiences** do criador da Campaign ou no **Entry Audience** do criador do Canvas.

### Casos de uso {#use-cases}

{% tabs local %}
{% tab Signup %}
#### Campanha de inscrição {#sign-up-campaign}

Ao utilizar a configuração da Braze para uma campanha de inscrição com uma oferta anexada, será necessário configurar uma campanha de presentes de inscrição na Punchh e uma mensagem de boas-vindas na Braze.

A Punchh recomenda que um delay de execução seja adicionado à campanha de inscrição, para que a Braze possa disparar primeiro a mensagem de boas-vindas com base no evento do convidado. Se quiser enviar uma mensagem de acompanhamento informando ao usuário que ele foi presenteado, poderá disparar essa mensagem com base no evento de recompensas.

No caso de uma campanha de inscrição, todas as pessoas que se inscreveram podem ser usadas para o segmento; portanto, não será necessário um segmento personalizado da Braze.

Configurações da Punchh necessárias:
- Campanha: inscrição
- Segmento: Todos inscritos
- Recompensa: Escolha do cliente
Eventos necessários:
- Evento de recompensa
- Evento de convidado
Considerações:
- Delay de execução; recomendamos que o convidado adicione um delay de 5 a 10 minutos

![Um segmento de usuário é configurado na Punchh, e os convidados se inscrevem em um programa de fidelidade. Depois disso, o evento do convidado, se disparado, e a campanha de mensagens da Braze é disparada. Em seguida, a campanha de presentes de inscrição da Punchh é acionada após 10 minutos, disparando o evento de recompensas e a mensagem opcional de acompanhamento.]({% image_buster /assets/img/punchh/usecase3.png %})
{% endtab %}

{% tab Braze welcome %}
#### Campanha de boas-vindas da Braze {#braze-welcome-campaign}

Quando um novo usuário se inscreve, a Punchh envia à Braze um evento Guest que cria o usuário e envia um atributo personalizado `signup_channel`, que pode ser usado para disparar a campanha de boas-vindas da Braze.

Para configurar a campanha de boas-vindas da Braze, siga estas etapas:

1. Na Braze, crie uma Campaign baseada em ações.
2. Para o disparo, selecione **Change Custom Attribute Value** com o atributo personalizado `signup_channel` definido como **Any new value**.
3. Continue criando sua Campaign e envie-a quando estiver pronta!

{% endtab %}
{% tab Mass offer %}
#### Campanha de oferta em massa {#mass-offer-campaign}

Ao utilizar uma campanha de oferta em massa para presentear, uma campanha de oferta em massa precisará ser configurada na Punchh e uma campanha de mensagens na Braze.

Se você quiser utilizar um segmento da Braze para sua campanha ou enviar uma comunicação da Braze antes de presentear os convidados na plataforma Punchh, será necessário um [segmento personalizado da Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) para a campanha de presentes da Punchh.

A criação do segmento de usuários para receber essa oferta na Braze só é recomendada quando se usam atributos indisponíveis na Punchh. Caso contrário, a segmentação da Punchh poderá ser usada, e a campanha de mensagens da Braze será criada como uma Campaign baseada em ação, disparada pelos usuários que receberem suas recompensas (o evento de recompensa disparado pela Punchh).

Configurações da Punchh necessárias:
- Campanha: Oferta em massa
- Segmento: Lista personalizada ou escolha do cliente
- Recompensa: Escolha do cliente

**Usando a Punchh para segmentação e oferta de presentes e a Braze para envio de mensagens:**<br>
Por exemplo, uma recompensa de US$ 2 de desconto é enviada a um segmento configurável na Punchh com envio de mensagens pela Braze.<br>
![Um segmento de usuário pode ser configurado na Punchh, e os usuários recebem um presente por meio de uma campanha de oferta em massa da Punchh. Em seguida, um evento de recompensa é disparado e a campanha de mensagens da Braze é disparada.]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**Usando a segmentação e o envio de mensagens da Braze e a Punchh para presentear:**<br>
Por exemplo, uma recompensa de US$ 2 de desconto e o envio de mensagens para um segmento com atributos não disponíveis na Punchh.<br>
![Um segmento de usuário pode ser configurado na Braze e, em seguida, uma mensagem pode ser enviada de um segmento da Braze para a Braze. Em seguida, os usuários são enviados para o segmento personalizado da Punchh por meio de um webhook da Braze com o segmento e o ID do usuário. Depois disso, o usuário recebe um presente por meio da campanha de oferta em massa da Punchh com um segmento personalizado. Depois disso, o evento de recompensa é disparado.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**Usando a segmentação da Braze e a Punchh para presentes ou envio de mensagens, ou ambos:**<br>
Por exemplo, uma recompensa de US$ 2 de desconto é enviada a um segmento com atributos não disponíveis na Punchh, mas não é necessário o envio de mensagens, ou as mensagens podem ser enviadas por meio da Punchh (note que todos os convidados devem estar presentes na Punchh).<br>
![Um segmento de usuário pode ser configurado na Braze, e os usuários são enviados ao segmento personalizado da Punchh por meio de um webhook da Braze com o segmento e o ID do usuário. Depois disso, o usuário recebe um presente por meio da campanha de oferta em massa da Punchh com um segmento personalizado. Depois disso, o evento de recompensa é disparado.]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab Recurring mass offer %}
#### Campanha de oferta em massa recorrente {#recurring-mass-offer-campaign}

Ao utilizar uma campanha de oferta em massa recorrente para presentear, será necessário configurar uma campanha de oferta em massa na Punchh e uma campanha de mensagens na Braze. Um segmento personalizado da Punchh será necessário se o cliente quiser usar a segmentação da Braze (recomendado somente se estiver utilizando atributos indisponíveis na Punchh). Caso contrário, a segmentação da Punchh pode ser usada, e a campanha de mensagens da Braze será disparada com base no evento de recompensas.

Configurações da Punchh necessárias:
- Campanha: Oferta em massa recorrente
- Segmento: Lista personalizada ou escolha do cliente
- Recompensa: Escolha do cliente
Considerações:
- Os IDs e os nomes das campanhas são enviados à Braze como uma propriedade do evento. Se você quiser usar um identificador de campanha da Punchh na Braze para filtrar ainda mais o público que recebe a campanha, deverá usar o nome da campanha, pois os IDs de campanha mudam diariamente.

{% endtab %}
{% tab Post check-in offer with notification %}
#### Campanha de oferta pós-check-in com notificação {#post-check-in-offer-campaign-with-notification}

Ao utilizar uma campanha de oferta pós-check-in, a Braze enviará a notificação sobre o presente e, quando o convidado fizer um check-in, ele será presenteado pela campanha pós-check-in da Punchh. Portanto, uma campanha de oferta pós-check-in precisará ser configurada na Punchh e uma campanha de mensagens na Braze (para notificar os clientes sobre a campanha).

Configurações da Punchh necessárias:
- Campanha: Oferta pós-check-in
- Segmento: Lista personalizada
- Recompensa: Escolha do cliente

Por exemplo, um e-mail notificando os convidados a visitarem o local neste fim de semana para ganhar pontos em dobro em um segmento com atributos não disponíveis na Punchh. A Punchh presenteará esse segmento com pontos após um check-in qualificado e envio opcional de mensagens da Braze.

![Um segmento de usuário é configurado na Braze, e as mensagens são enviadas da Braze na campanha pós-check-in. Em seguida, os usuários qualificados são enviados para o segmento personalizado da Punchh por meio do webhook da Braze com o segmento e o ID do usuário. Por fim, o usuário qualificado no segmento personalizado faz o check-in e recebe o presente e a mensagem opcional por meio da campanha pós-check-in.]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab Post check-in offer without notification %}
#### Campanha de oferta pós-check-in sem notificação {#post-check-in-offer-campaign-without-notification}

Ao utilizar uma campanha de oferta pós-check-in que não notifique previamente os clientes, a campanha oferecerá (envio de mensagens opcional) e disparará qualquer notificação na Braze. Portanto, uma campanha de oferta pós-check-in deve ser configurada na Punchh; no entanto, não é necessário ter uma lista personalizada. Em vez disso, você pode escolher o segmento que deseja na Punchh.

Configurações da Punchh necessárias:
- Campanha: Oferta pós-check-in
- Segmento: Escolha do cliente
- Recompensa: Escolha do cliente

Por exemplo, uma campanha de surpresa e encantamento da Braze é enviada a um segmento disponível na Punchh, agradecendo aos convidados pela visita e recompensando-os com US$ 2 de desconto em sua próxima visita.

![Um segmento de usuário qualificado pode ser configurado na Punchh, e um usuário qualificado faz o check-in e recebe um presente por meio de uma campanha pós-check-in da Punchh. Depois disso, um evento de recompensa é disparado e a mensagem de recall é enviada notificando os convidados sobre a recompensa enviada pela Braze.]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab Anniversary %}
#### Campanha de aniversário {#anniversary-campaign}

Ao utilizar uma campanha de aniversário, o usuário receberá primeiro o presente de aniversário da campanha da Punchh. Esse presente (evento de recompensa) dispara a campanha de mensagens na Braze que notifica o usuário sobre o presente. Portanto, não é necessária uma lista personalizada. Em vez disso, você pode escolher o segmento e a configuração de aniversário na Punchh.

Configurações da Punchh necessárias:
- Campanha: Campanha de aniversário
- Segmento: Escolha do cliente
- Recompensa: Escolha do cliente
Considerações:
- Presentear no mês de inscrição
- Duração da vida útil (por quanto tempo a recompensa de aniversário é válida?)
- Campanhas recorrentes, programação necessária

![Um segmento opcional pode ser criado na Punchh, e um usuário qualificado recebe recompensas por meio de uma campanha de aniversário da Punchh. Depois disso, um evento de recompensa é disparado e a mensagem de recall é enviada notificando os convidados sobre a recompensa enviada pela Braze.]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab Recall %}
#### Campanha de recall {#recall-campaign}

Ao direcionar os usuários com base na inatividade, uma campanha de recall pode ser usada. O cliente pode criar o segmento e a campanha na Punchh, mas utilizar a Braze para o envio de mensagens.

Se você quiser usar a segmentação criada na Braze, um [segmento personalizado da Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) baseado em inatividade poderá ser anexado a uma campanha de oferta em massa recorrente.

Configurações da Punchh necessárias:
- Campanha: Campanha de recall
- Segmento: Escolha do cliente
- Recompensa: Escolha do cliente
Considerações:
- A campanha é executada em um cronograma

![Um segmento opcional pode ser criado na Punchh, e um usuário qualificado recebe recompensas por meio de uma campanha de recall da Punchh. Depois disso, um evento de recompensa é disparado, e a mensagem de recall é enviada notificando os convidados sobre a recompensa enviada pela Braze.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}