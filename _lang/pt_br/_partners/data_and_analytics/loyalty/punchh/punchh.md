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

A integração entre a Braze e a Punchh permite sincronizar dados para fins de presentes e fidelidade entre as duas plataformas. Os dados publicados na Braze estarão disponíveis para segmentação e podem sincronizar dados de usuários de volta para a Punchh por meio de webhooks da Braze.

## Quais são os benefícios? {#what-are-the-benefits}

- Ingira dados de fidelidade da Punchh para a Braze em tempo real.
- Aproveite e combine dados avançados de público da Braze para oferecer experiências dinâmicas e significativas entre canais (app, dispositivo móvel, web, e-mail e SMS)
  - Os clientes abriram os e-mails? Os clientes abriram o app perto de uma loja?
- Padronize a aparência dos e-mails de transação enviados pela Braze.
- Crie jornadas que permitam testes A/B e otimização contínua.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Punchh | Você precisa de uma conta Punchh ativa para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [URL do seu endpoint REST]({{site.baseurl}}/api/basics#endpoints). Seu endpoint depende da URL da Braze para a sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## O que mais preciso saber? {#what-else-should-i-know}

### Antes de integrar {#before-integrating}

- Ao utilizar a integração com a Braze, duas campanhas serão necessárias, uma na Punchh e a segunda na Braze. Por exemplo, se você enviar uma campanha com uma oferta anexada, a campanha de presente será configurada dentro da Punchh, e a notificação pode ser enviada a partir da Braze.
- Os convidados já devem existir na Punchh e na Braze. A Punchh filtrará qualquer cliente que ainda não seja um convidado do programa de fidelidade.

### Pontos importantes a observar {#important-things-to-note}

- A Punchh adicionou a capacidade de desativar o envio de atributos de usuário padrão para a Braze, para que o cliente não incorra em excedentes de pontos de dados. Isso é configurado durante a configuração do adaptador.
- Se estiver usando segmentos personalizados em campanhas recorrentes, o nome da campanha deve ser usado em vez do ID da campanha, pois os IDs mudam cada vez que a campanha é executada.
- Os canais de comunicação disponíveis em cada campanha de presente da Punchh incluem mensagens ricas, notificações por push, SMS e e-mail.
- Depois que os usuários forem enviados para um segmento personalizado da Punchh a partir da Braze, eles não poderão ser removidos. Apenas novos convidados podem ser adicionados a um segmento personalizado existente. Se for necessário remover convidados de um segmento personalizado existente da Punchh, uma nova campanha de webhook precisará ser criada na Braze para enviar usuários a um novo segmento personalizado da Punchh.

## Integração {#integration}

A Punchh oferece vários endpoints disponíveis para clientes da Braze para ajudar a adicionar IDs externos à plataforma Punchh usando os seguintes endpoints de API da Punchh. Depois que os IDs externos forem adicionados, crie um adaptador na Punchh, forneça suas credenciais da Braze e selecione quais eventos você gostaria de sincronizar. Em seguida, você pode pegar o ID do segmento da Punchh e usá-lo para construir um webhook Punchh para disparar a sincronização de clientes em uma jornada Canvas.

Observe que o `user_id` da Punchh e o `external_id` da Braze precisam estar disponíveis em ambas as plataformas para que a integração sincronize corretamente.
- Os eventos enviados da Punchh para a Braze incluirão o `external_id` da Braze como identificador. Se a Punchh estiver configurada para usar o `external_source_id`, esse valor será definido como o `external_id` da Braze. Caso contrário, a integração usará por padrão o `user_id` da Punchh como o `external_id` da Braze.
- Para enviar webhooks da Braze para a Punchh, o `user_id` da Punchh deve estar disponível no perfil de usuário da Braze. Se o `user_id` da Punchh não for usado como o `external_id` da Braze, ele deve ser definido como um atributo personalizado "punchh_user_id".

### Etapa 1: Configurar endpoints de ingestão de ID externo (opcional) {#step-1-set-up-external-id-ingestion-endpoints-optional}

IDs externos da Braze podem ser adicionados usando os seguintes endpoints para usuários novos e existentes da Punchh.

{% alert important %}
Os valores dos campos `external_source` e `external_source_id` devem ser exclusivos na Punchh e não estar associados a perfis existentes.
{% endalert %}

1. Novos usuários Punchh<br>
Crie novos usuários na Punchh com um endpoint de inscrição da Punchh usando os campos `external_source` e `external_source_id`. A Punchh permite que identificadores externos sejam enviados com um perfil de usuário por meio de um dos seguintes endpoints de inscrição:
- [API de inscrição mobile](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [API de inscrição SSO](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. Usuários Punchh existentes <br>
Atualize o `external_source_id` para usuários Punchh existentes. A Punchh permite que identificadores externos sejam adicionados a um perfil por meio de um endpoint de atualização de API de usuário:
- [Atualização de usuário mobile](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [Atualização de usuário SSO](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [Atualização de usuário no dashboard](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
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
Este exemplo permite atualizar identificadores externos com um perfil de usuário. Isso é feito enviando `external_source` como "customer_id" e `external_source_id` como "111111111111111111" como um tipo de dados string.

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
**Configuração da plataforma:** Para ativar identificadores externos na Punchh, no dashboard da Punchh, navegue até **Cockpit** > **Dashboard** > **External User Identifier**.
{% endalert %}

### Etapa 2: Configuração do adaptador Braze na Punchh {#step-2-braze-adapter-setup-in-punchh}

#### Eventos disponíveis para sincronização {#available-events-to-sync}

1. **Guest:** Disparado em qualquer inscrição, atualização do perfil do convidado, desativação ou exclusão
2. **Loyalty Check-in:** Disparado para transações de fidelidade ou pontuação ao escanear código de barras do recibo
3. **Gift Check-in:** Disparado para pontos presenteados por uma campanha
4. **Redemption:** Disparado em caso de qualquer resgate de recompensa, excluindo cupons Punchh, pois esses seriam enviados separadamente como eventos de cupom, incluindo emissão e resgate
5. **Rewards:** Disparado a partir de recompensas presenteadas por campanhas, atividade, conversão de pontos em recompensas ou presenteamento pelo administrador
6. **Transaction Notifications:** Disparado mediante atividade transacional para um usuário dentro do sistema Punchh (por exemplo, expiração de pontos)
7. **Marketing Notifications:** Disparado com base em diferentes configurações de campanha na Punchh para um segmento associado de usuários

{% alert note %}
Consulte a documentação da Punchh para ver exemplos de cargas úteis para esses eventos disponíveis.
{% endalert %}

Trabalhe com seu gerente de implementação da Punchh para configurar esse adaptador.

Para configurar a integração entre Braze e Punchh, faça o seguinte:

1. No dashboard da Punchh, navegue até **Cockpit** > **Dashboard** > **Major Features** > **Enable Webhook Management** e ative **Enable Webhook Management**.<br><br>
2. Em seguida, ative os adaptadores navegando até **Settings** > **Webhooks Manager** > **Configurations** > **Show Adapters Tab** e ative **Show Adapters Tab**.<br><br>
3. Navegue até **Webhooks Manager** na guia **Settings**, selecione a guia **Adapters** e clique em **Create Adapter**. <br><br>![Guia de adaptadores do gerenciador de webhooks da Punchh com a opção Create Adapter selecionada.]({% image_buster /assets/img/punchh/punchh1.png %})<br><br>
4. Preencha o nome do adaptador, a descrição e o e-mail do administrador. Selecione **Braze** como seu adaptador e forneça seu endpoint da REST API da Braze e sua chave de API da Braze.<br><br>
5. Em seguida, selecione os eventos disponíveis que você deseja ativar. Uma lista desses eventos pode ser encontrada em [Eventos disponíveis para sincronização](#available-events-to-sync).<br><br>![Configurações do adaptador Punchh mostrando eventos selecionáveis para sincronização com a Braze.]({% image_buster /assets/img/punchh/punchh3.png %})<br><br>
6. Clique em **Submit** para ativar o webhook.

## Criar webhook Punchh na Braze {#create-punchh-webhook-in-braze}

A Braze pode adicionar usuários a um Segment Punchh por meio de webhooks que utilizam Segments personalizados da Punchh.

1. Crie um Segment personalizado na Punchh e anote o `custom_segment_id` presente na URL do dashboard de Segments da Punchh, conforme mostrado no exemplo a seguir. Tanto o criador de segmentos clássico quanto o beta podem ser usados. No entanto, o beta é recomendado, pois o clássico será descontinuado eventualmente.<br><br>Na plataforma Punchh, acesse **Guest** > **Segment** > **Custom List** > **New Custom List**.<br><br>![Dashboard de Segment personalizado da Punchh mostrando o ID do Segment personalizado na URL.]({% image_buster /assets/img/punchh/update1.png %})<br><br>

2. Crie uma campanha de webhook na Braze usando o endpoint da Punchh para adicionar um usuário a um Segment personalizado como a URL do webhook. Aqui, você pode fornecer o `custom_segment_id` extraído da URL e o `user_id` como pares chave-valor.<br><br>![Criador de webhook da Braze com endpoint da Punchh e campos de carga útil com pares chave-valor.]({% image_buster /assets/img/punchh/punchh4.png %})<br><br>

3. Esse webhook pode ser configurado como uma Campaign singular ou como uma etapa dentro de um Canvas. Alternativamente, se o webhook que adiciona usuários a esse Segment Punchh específico for usado em múltiplas Campaigns ou Canvas, ele pode ser configurado como um [modelo]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates).<br><br>
A chave `user_id` dentro do webhook é mapeada para o ID de usuário da Punchh. Esse identificador precisará ser adicionado a todos os webhooks criados na Braze para adicionar usuários a um Segment personalizado da Punchh. O atributo personalizado `punch_user_id` pode ser preenchido dinamicamente como o valor da chave `user_id` usando [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid#pre-formatted-variables). Você pode inserir a variável do atributo personalizado `punchh_user_id` usando o ícone azul de "mais" na barra de ferramentas do campo de texto com modelo.<br><br>![Campo de carga útil do webhook da Braze com variável Liquid do ID de usuário da Punchh inserida.]({% image_buster /assets/img/punchh/update3.png %}){: style="max-width:65%;"}<br><br>![Seletor de personalização da Braze mostrando o atributo personalizado punchh_user_id.]({% image_buster /assets/img/punchh/update4.png %}){: style="max-width:65%;"}<br><br>

4. Depois que o webhook for salvo, ele poderá ser usado para sincronizar usuários. Por exemplo, 136 convidados seriam adicionados ao Segment personalizado da Punchh quando essa campanha de webhook da Braze for lançada.<br><br>![Exemplo de sincronização de usuários usando o webhook salvo por meio da integração entre Braze e Punchh.]({% image_buster /assets/img/punchh/punchh6.png %})

Para saber mais sobre como webhooks são usados na Braze, confira [Criar um webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook).

## Campanhas de casos de uso {#use-case-campaigns}

### Configuração de Campaign e Canvas {#campaign-and-canvas-configuration}

#### Disparo {#triggering}

Casos de uso para envio de mensagens da Braze disparados por eventos da Punchh enviados à Braze, como eventos de recompensa ou eventos de convidados, podem ser criados como [Campaigns baseadas em ações]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) ou Canvas disparados pelo evento relevante da Punchh.

Adicionar um disparo exibirá a lista de eventos criados na Braze. Escolha o evento que deve disparar sua Campaign ou Canvas para ser enviado ao usuário que registrou o evento.

![Configuração de disparo da Braze mostrando um evento Punchh selecionado para uma Campaign baseada em ação.]({% image_buster /assets/img/punchh/update5.png %})

Filtros de propriedade podem ser adicionados para refinar ainda mais o evento de disparo. Por exemplo, a mensagem só deve ser disparada quando um cliente acionar o evento "checkins_gift" em que a propriedade de evento aprovada é `true`. Este é um recurso opcional que pode não ser aplicável a todos os casos de uso.

#### Segmentação {#segmentation}

Em muitos casos, Campaigns e Canvas da Braze disparados por eventos da Punchh podem ser definidos para um público "Todos os usuários", já que a segmentação dos usuários que disparam esses eventos é determinada dentro da Punchh. No entanto, clientes que desejam refinar ainda mais o público de usuários que receberão as mensagens da Braze disparadas pelo evento podem fazer isso adicionando filtros e Segments adicionais na seção **Públicos-alvo** do criador de Campaign ou no **Público de entrada** do criador de Canvas.

### Casos de uso {#use-cases}

{% tabs local %}
{% tab Inscrição %}
#### Campanha de inscrição {#sign-up-campaign}

Ao utilizar a configuração da Braze para uma campanha de inscrição com uma oferta associada, uma campanha de presente de inscrição precisará ser configurada dentro da Punchh e uma mensagem de boas-vindas na Braze.

A Punchh recomenda que um atraso de execução seja adicionado à campanha de inscrição, para que a Braze possa primeiro disparar a mensagem de boas-vindas com base no evento de convidado. Se você quiser enviar uma mensagem de acompanhamento informando ao usuário que ele recebeu um presente, você pode disparar isso com base no evento de recompensa.

No caso de uma campanha de inscrição, "todos inscritos" pode ser usado para o Segment; portanto, um Segment personalizado da Braze não será necessário.

Configurações Punchh necessárias:
- Campanha: Inscrição
- Segment: Todos inscritos
- Recompensa: Escolha do cliente
Eventos necessários:
- Evento de recompensa
- Evento de convidado
Considerações:
- Atraso de execução, recomenda-se que o convidado adicione um atraso de 5 a 10 minutos

![Um Segment de usuário é configurado na Punchh, e os convidados se inscrevem em um programa de fidelidade. Depois disso, o evento de convidado, se disparado, e a campanha de mensagens da Braze é disparada. Em seguida, a campanha de presente de inscrição da Punchh é disparada após 10 minutos, disparando o evento de recompensa e a mensagem de acompanhamento opcional.]({% image_buster /assets/img/punchh/usecase3.png %})
{% endtab %}

{% tab Boas-vindas da Braze %}
#### Campanha de boas-vindas da Braze {#braze-welcome-campaign}

Quando um novo usuário se inscreve, a Punchh envia à Braze um evento de convidado que cria o usuário e envia um atributo personalizado `signup_channel`, que você pode usar para disparar a campanha de boas-vindas da Braze.

Para configurar a campanha de boas-vindas da Braze, siga estas etapas:

1. Na Braze, crie uma Campaign baseada em ação.
2. Para o disparo, selecione **Alterar valor de atributo personalizado** com o atributo personalizado `signup_channel` definido como **Qualquer novo valor**.
3. Continue criando sua Campaign e depois envie quando estiver pronto!

{% endtab %}
{% tab Oferta em massa %}
#### Campanha de oferta em massa {#mass-offer-campaign}

Ao utilizar uma campanha de oferta em massa para presentes, uma campanha de oferta em massa precisará ser configurada dentro da Punchh e uma campanha de mensagens na Braze.

Se você quiser usar um Segment da Braze para sua campanha ou enviar comunicação da Braze antes de presentear os convidados na plataforma Punchh, então um [Segment personalizado da Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze) será necessário para a campanha de presentes da Punchh.

Criar o Segment de usuários para receber essa oferta na Braze só é recomendado ao utilizar atributos indisponíveis dentro da Punchh. Caso contrário, a segmentação da Punchh pode ser usada, e a campanha de mensagens da Braze será criada como uma Campaign baseada em ação disparada pelos usuários que receberam sua recompensa (o evento de recompensa disparado pela Punchh).

Configurações Punchh necessárias:
- Campanha: Oferta em massa
- Segment: Lista personalizada ou escolha do cliente
- Recompensa: Escolha do cliente

**Usando Punchh para segmentação e presentes, e Braze para envio de mensagens:**<br>
Por exemplo, uma recompensa de $2 de desconto é enviada a um Segment configurável dentro da Punchh com mensagens enviadas pela Braze.<br>
![Um Segment de usuário pode ser configurado na Punchh, e os usuários recebem um presente por meio de uma campanha de oferta em massa da Punchh. Em seguida, um evento de recompensa é disparado, e então a campanha de mensagens da Braze é disparada.]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**Usando segmentação e envio de mensagens da Braze, e Punchh para presentes:**<br>
Por exemplo, uma recompensa de $2 de desconto e mensagens enviadas a um Segment com atributos não disponíveis na Punchh.<br>
![Um Segment de usuário pode ser configurado na Braze, e então uma mensagem pode ser enviada de um Segment Braze para Braze. Em seguida, os usuários são enviados ao Segment personalizado da Punchh por meio de um webhook da Braze com ID de Segment e ID de usuário. Depois disso, o usuário recebe um presente por meio da campanha de oferta em massa da Punchh com Segment personalizado. Após isso, o evento de recompensa é disparado.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**Usando segmentação da Braze e Punchh para presentes ou envio de mensagens, ou ambos:**<br>
Por exemplo, uma recompensa de $2 de desconto é enviada a um Segment com atributos não disponíveis na Punchh, mas nenhum envio de mensagem é necessário, ou o envio de mensagens pode ser feito pela Punchh (observe que todos os convidados devem estar presentes na Punchh).<br>
![Um Segment de usuário pode ser configurado na Braze, e os usuários são enviados ao Segment personalizado da Punchh por meio de um webhook da Braze com ID de Segment e ID de usuário. Depois disso, o usuário recebe um presente por meio da campanha de oferta em massa da Punchh com Segment personalizado. Após isso, o evento de recompensa é disparado.]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab Oferta em massa recorrente %}
#### Campanha de oferta em massa recorrente {#recurring-mass-offer-campaign}

Ao utilizar uma campanha de oferta em massa recorrente para presentes, uma campanha de oferta em massa precisará ser configurada dentro da Punchh e uma campanha de mensagens configurada na Braze. Um Segment personalizado da Punchh será necessário se o cliente quiser usar a segmentação da Braze (recomendado apenas se utilizar atributos indisponíveis dentro da Punchh). Caso contrário, a segmentação da Punchh pode ser usada, e a campanha de mensagens da Braze será disparada com base no evento de recompensa.

Configurações Punchh necessárias:
- Campanha: Oferta em massa recorrente
- Segment: Lista personalizada ou escolha do cliente
- Recompensa: Escolha do cliente
Considerações:
- Os IDs de Campaign e os nomes de Campaign são enviados à Braze como uma propriedade de evento no evento. Se você quiser usar um identificador de campanha Punchh na Braze para filtrar ainda mais o público que recebe a campanha, você deve usar o nome da campanha, pois os IDs de Campaign mudam diariamente.

{% endtab %}
{% tab Oferta pós-check-in com notificação %}
#### Campanha de oferta pós-check-in com notificação {#post-check-in-offer-campaign-with-notification}

Ao utilizar uma campanha de oferta pós-check-in, a Braze enviará a notificação sobre o presente, e quando o convidado fizer um check-in, ele será presenteado pela campanha de pós-check-in da Punchh. Portanto, uma campanha de oferta pós-check-in precisará ser configurada dentro da Punchh e uma campanha de mensagens na Braze (se for notificar os clientes sobre a campanha).

Configurações Punchh necessárias:
- Campanha: Oferta pós-check-in
- Segment: Lista personalizada
- Recompensa: Escolha do cliente

Por exemplo, um e-mail notificando os convidados para visitar neste fim de semana para pontos em dobro a um Segment com atributos não disponíveis na Punchh. A Punchh presenteará esse Segment com pontos após um check-in qualificado e envio de mensagens opcional da Braze.

![Um Segment de usuário é configurado na Braze, e mensagens são enviadas da campanha de pós-check-in da Braze. Em seguida, os usuários qualificados são enviados ao Segment personalizado da Punchh por meio de webhook da Braze com ID de Segment e ID de usuário. Por último, o usuário qualificado no Segment personalizado faz o check-in e recebe o presente e mensagem opcional por meio da campanha de pós-check-in.]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab Oferta pós-check-in sem notificação %}
#### Campanha de oferta pós-check-in sem notificação {#post-check-in-offer-campaign-without-notification}

Ao utilizar uma campanha de oferta pós-check-in que não notifica os clientes previamente, a campanha presenteará (envio de mensagens opcional) e disparará qualquer notificação dentro da Braze. Portanto, uma campanha de oferta pós-check-in deve ser configurada dentro da Punchh; no entanto, uma lista personalizada não é necessária. Em vez disso, você pode escolher o Segment desejado dentro da Punchh.

Configurações Punchh necessárias:
- Campanha: Oferta pós-check-in
- Segment: Escolha do cliente
- Recompensa: Escolha do cliente

Por exemplo, uma Campaign de surpresa e encantamento da Braze é enviada a um Segment disponível na Punchh, agradecendo os convidados pela visita e recompensando-os com $2 de desconto na próxima visita.

![Um Segment de usuário qualificado pode ser configurado dentro da Punchh, e um usuário qualificado faz o check-in e recebe um presente por meio de uma campanha de pós-check-in da Punchh. Após isso, um evento de recompensa é disparado e a mensagem de recuperação é enviada notificando os convidados sobre a recompensa enviada pela Braze.]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab Aniversário %}
#### Campanha de aniversário {#anniversary-campaign}

Ao utilizar uma campanha de aniversário, um usuário será primeiro presenteado pelo seu aniversário pela campanha da Punchh. Esse presente (evento de recompensa) disparará a campanha de mensagens dentro da Braze que notifica o usuário sobre o presente. Portanto, uma lista personalizada não é necessária. Em vez disso, você pode escolher o Segment e a configuração de aniversário dentro da Punchh.

Configurações Punchh necessárias:
- Campanha: Campanha de aniversário
- Segment: Escolha do cliente
- Recompensa: Escolha do cliente
Considerações:
- Mês de inscrição para presente
- Duração do prazo (Por quanto tempo a recompensa de aniversário é válida?)
- Campanhas recorrentes, agendamento necessário

![Um Segment opcional pode ser criado dentro da Punchh, e um usuário qualificado recebe uma recompensa por meio de uma campanha de aniversário da Punchh. Após isso, um evento de recompensa é disparado e a mensagem de recuperação é enviada notificando os convidados sobre a recompensa enviada pela Braze.]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab Recuperação %}
#### Campanha de recuperação {#recall-campaign}

Ao direcionar usuários com base em inatividade, uma campanha de recuperação pode ser usada. O cliente pode criar o Segment e a campanha dentro da Punchh, mas usar a Braze para envio de mensagens.

Se você quiser usar a segmentação criada na Braze, um [Segment personalizado da Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze) baseado em inatividade pode ser associado a uma campanha de oferta em massa recorrente.

Configurações Punchh necessárias:
- Campanha: Campanha de recuperação
- Segment: Escolha do cliente
- Recompensa: Escolha do cliente
Considerações:
- A campanha é executada em um cronograma

![Um Segment opcional pode ser criado dentro da Punchh, e um usuário qualificado recebe uma recompensa por meio de uma campanha de recuperação da Punchh. Após isso, um evento de recompensa é disparado, e a mensagem de recuperação é enviada notificando os convidados sobre a recompensa enviada pela Braze.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}