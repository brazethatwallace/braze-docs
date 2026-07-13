---
nav_title: Oracle Crowdtwist
article_title: Crowdtwist
description: "Este artigo descreve a parceria entre a Braze e o Oracle Crowdtwist, por meio de modelos de Transformação de Dados da Braze especialmente criados e dos Data Push Objects do Crowdtwist."
alias: /partners/crowdtwist/
page_type: partner
search_tag: Partner

---

# Oracle Crowdtwist

> O [Oracle Crowdtwist](https://www.oracle.com/uk/cx/marketing/customer-loyalty/) é uma solução líder em fidelidade do cliente nativa da nuvem que capacita as marcas a oferecer experiências personalizadas aos clientes. Sua solução oferece mais de 100 jornadas de engajamento prontas para uso, proporcionando um rápido retorno do investimento para que os profissionais de marketing desenvolvam uma visão mais completa do cliente.

O recurso Data Push do Oracle Crowdtwist permite que os metadados de usuários ou eventos sejam transmitidos sempre que ocorrer uma atualização na plataforma do Crowdtwist.

Este guia descreve como integrar os feeds Live Push de perfil de usuário, atividade de usuário e resgate de usuário do Oracle Crowdtwist ao seu ambiente Braze. Há dois tipos adicionais de Data Push disponíveis que não são explicitamente abordados nesta documentação, mas sua configuração segue os mesmos princípios descritos neste guia.

* [Live Push User Profile](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/PushUserProfile-withTiersv2.html): Inclui a criação de novos perfis e atualizações de perfis existentes.

* [Live Push User Activity](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html): Inclui dados sobre conclusões de atividades de usuários.

* [Live Push User Redemption](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserRedemption.html): Inclui dados sobre resgates de recompensas de usuários.

Ao usar um modelo de Transformação de Dados da Braze, você pode filtrar os elementos do Data Push que não são relevantes para a Braze e atribuir os valores necessários na Braze para que possam ser aproveitados pelos "destinos" disponíveis.

Por exemplo, use um Data Push para passar eventos personalizados e atributos relevantes para a Braze, como quando um usuário muda de nível de fidelidade ou resgata uma recompensa. Também é possível usá-lo para registrar atributos personalizados na Braze assim que esses dados forem atualizados no perfil de usuário de um membro, como o saldo de pontos de um usuário.

## Pré-requisitos {#prerequisites}


| Requisito | Descrição |
| --- | --- |
| Conta Oracle Crowdtwist | É necessário ter uma [conta Oracle Crowdtwist](https://www.oracle.com/uk/cx/marketing/customer-loyalty/) para aproveitar essa parceria. |
| Endpoint de Transformação de Dados da Braze | Essa integração se baseia na [ferramenta de Transformação de Dados]({{site.baseurl}}/user_guide/data/unification/data_transformation) da Braze. Quando você cria uma Transformação de Dados, a Braze gera um endpoint exclusivo que pode ser adicionado como um destino para o Data Push do Crowdtwist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

A Braze e o Oracle Crowdtwist criaram [modelos de Transformação de Dados]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation?redirected=1#step-2-create-a-transformation) para ajudar nossos clientes a desenvolver suas próprias Transformações de Dados que aproveitam os eventos de perfil de usuário, resgate de usuário e atividade de usuário.

## Etapa 1: Criar Transformação de Dados a partir do modelo Oracle Crowdtwist {#step-1-create-data-transformation-from-oracle-crowdtwist-template}

Navegue até **Configurações de dados** > **Transformação de Dados** > **Criar transformações** > **Usar um modelo** e selecione o modelo "BRAZE <> CROWDTWIST" de sua escolha.

Você encontrará quatro modelos — um para transformar eventos de perfil de usuário, atividade de usuário e resgate de usuário, e um modelo mestre que usa lógica condicional para aplicar a vários eventos de Data Push.

Conforme mostrado na [documentação do Data Push do Oracle Crowdtwist](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/DataPush.html), os objetos Data Push contêm metadados diferentes, portanto, cada um requer seu próprio código de transformação para criar objetos Braze apropriados. O modelo mestre ilustra como configurar uma única Transformação de Dados para aceitar cada um dos três tipos de objetos e cria uma saída apropriada com valores de cada objeto.

## Etapa 2: Atualizar e testar o modelo {#step-2-update-and-test-template}

Nesta seção, você verá os modelos anotados. O corpo desses modelos foi projetado para ser aplicado ao destino `/users/track`. As anotações são marcadas pelo início de linha `//` e pelo texto verde, e você pode excluí-las sem afetar a operação do código de transformação.

A transformação usa JavaScript, que cria um objeto chamado "brazecall". Esse objeto é onde você cria o corpo da solicitação que é enviada para um endpoint da REST API da Braze. Para obter orientação sobre as estruturas necessárias das solicitações para esses destinos, consulte os links na seção "destinos".

{% alert note %}
Observe que os "valores" de cada "chave" começam com `payload.`. A carga útil representa o objeto de dados recebido do Oracle Crowdtwist. Use a notação de ponto do JavaScript para escolher qual dado você deseja usar para preencher os elementos do seu objeto Braze. Por exemplo, quando você vê `external_id: payload.thirdPartyId`, isso significa que o ID externo da Braze é definido pelo valor `third_party_id` armazenado no Oracle Crowdtwist. Para saber mais sobre o esquema ou a composição dos objetos provenientes do Oracle Crowdtwist, consulte a [documentação da Oracle](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html).
{% endalert %}

{% alert important %}
 Use os objetos enviados do Oracle Crowdtwist para criar usuários na Braze. Ao incluir a chave `update_existing_only` com o valor `false`, se um objeto de atributo ou evento incluir um identificador que não exista na Braze, a Braze criará um perfil de usuário com os atributos incluídos no objeto de evento ou atributo. Se você preferir que o Oracle Crowdtwist atualize apenas os perfis que já existem na Braze, defina esse atributo como `true` em cada objeto de atributo ou evento.
{% endalert %}

### Modelos de Transformação de Dados {#data-transformation-templates}
{% tabs %}
{% tab User Profile Event Template%}
```javascript
let brazecall = {
 "attributes": [
   {
     //You must include an appropriate identifier for your attribute or event object from data available in Oracle Crowdtwist. This could be an external ID, Braze ID, user alias, phone, or email address for attribute or event objects.
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
   // **Important** To allow Oracle Crowdtwist events to create users in Braze, set the value of "_update_existing_only" to false. Otherwise, set this value to true in your event and attribute objects.
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
 //In this example, the "tierInfo" object from Crowdtwist is transformed into a Braze Nested Custom Attribute. Use the "_merge_objects" value to avoid duplications in a data point efficient manner.
 //The "tierinfo_current_level" attribute is a flat Braze custom attribute, while the following "tierInfo" value is a nested object mirroring the Crowdtwist payload; the difference in capitalization is intentional.
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
//Below we show how to create both custom attributes and events from a single Crowdtwist User Profile object.
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
//Below we can see how to write a timestamp in your object, which is a required value for some objects, like the Event Object.
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
// After the /users/track request is assigned to brazecall, return brazecall to create an output.
return brazecall;

```

{% endtab %}
{% tab User Activity Event Template %}
```javascript
let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
```
{% endtab %}
{% tab Redemption Event Template %}
```javascript
let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   //A user redemption event may not have a third party id, in which case you can instead provide the opportunity to include a user alias.
   "user_alias": { "alias_name" : "crowdtwist_redemption_username", "alias_label" : payload.userName},
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;

```
{%endtab%}
{% tab Master Template %}
```javascript
//The master template uses JavaScript's conditional operators to determine the output of the Data Transformation. This example shows how to apply JavaScript to your transformation to allow for a dynamic range of sources or inputs.

 // We open the transformation with a simple "if" function. We're checking if the value "payload.tierInfo" is present. "tierInfo" is a value that is always populated in the User Profile Live Push object, but is not present in the others.

if (payload.tierInfo) {
let brazecall = {
 "attributes": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
return brazecall;
//Now we use an "else if" operator to change the "brazecall" body if the object is a User Activity event by checking if the unique key "activityId" has been populated.
} else if (payload.activityId) {
 let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
//Finally, this conditional statement triggers if the Data Push object is a User Redemption event, based on whether a value populates in the key "rewardId".
} else if (payload.rewardId) {
 let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;
} else {
 //Include this error message to help with troubleshooting in the log if a call fails. Replace the text in the parentheses with anything that might be clearer to your team based on your Data Transformation.
 throw new Error("No appropriate Identifiers found");
}

```
{% endtab %}
{% endtabs %}

### Destinos {#destinations}

Os modelos deste guia foram criados para serem entregues ao destino "Track Users", mas você pode projetar seu modelo para enviar a qualquer um dos endpoints listados no [guia de Transformação de Dados da Braze]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation#step-2-create-a-transformation), com o suporte da [documentação da REST API]({{site.baseurl}}/api/home) associada.

### Testes {#testing}

Depois de modificar o modelo a seu gosto, você deve validar se ele está funcionando corretamente. No editor de transformação, selecione **Validar** para gerar uma prévia na seção **Saída** e confirmar se a Braze aceitará a solicitação mapeada para o destino escolhido.

Quando estiver satisfeito com o objeto que você vê no campo **Saída**, selecione **Ativar** para que o endpoint da Transformação de Dados esteja pronto para aceitar dados.

Você encontrará a URL do webhook da sua Transformação de Dados no painel de detalhes da transformação. Copie-a e use-a para configuração no Hub de Integração do Oracle Crowdtwist.

{% alert important %}
Os endpoints de Transformação de Dados da Braze têm um limite de frequência de 1.000 solicitações por minuto. Considere a velocidade na qual você deseja que esses dados sejam disponibilizados na Braze e fale com seu gerente de conta da Braze se precisar de um limite de frequência de Transformação de Dados mais alto.
{% endalert %}

As Transformações de Dados são uma ferramenta muito dinâmica, e você pode projetá-las para fins que vão além do que está descrito neste documento com conhecimento de JavaScript e com a orientação da nossa documentação da REST API. Para obter suporte ou solução de problemas em alterações complexas nos seus modelos de Transformação de Dados, fale com seu gerente de sucesso do cliente para saber mais sobre as orientações disponíveis.