# Caso de uso: Sistema de e-mail de lembrete de reserva {#use-case-booking-reminder-email-system}

> A Braze é uma plataforma abrangente de engajamento com clientes projetada para ser altamente controlável de forma programática. Neste caso de uso, vamos demonstrar algumas maneiras pelas quais a Braze oferece funcionalidades que você pode integrar em casos de uso na interseção de produto e marketing, como sistemas de reserva.

Este caso de uso mostra como você pode usar os recursos da Braze para construir um serviço de envio de mensagens de e-mail de lembrete de reserva. O serviço permitirá que os usuários agendem compromissos e enviará lembretes sobre seus compromissos futuros. Embora este caso de uso utilize mensagens por e-mail, você pode enviar mensagens em qualquer canal, ou em múltiplos canais, com base em uma única atualização no perfil de usuário.

Outros benefícios de criar este serviço incluem:
- As mensagens enviadas terão rastreamento e relatórios completos.
- Usuários da empresa não técnicos podem atualizar o conteúdo das mensagens.
- As mensagens obedecem aos status de opt-in e descadastramento nos perfis dos usuários conforme a configuração da Campaign.
- Você pode usar tanto os dados de reserva quanto os dados de interação com mensagens para segmentar e redirecionar usuários para envio de mensagens adicionais. Por exemplo, você pode redirecionar aqueles que não abrem a mensagem de lembrete inicial com um lembrete adicional antes do compromisso.

Siga estas etapas para alcançar este caso de uso:
1. [Grave os dados de reserva futuros em um perfil de usuário da Braze](#step-1)
2. [Configure e lance uma mensagem de lembrete de reserva](#step-2)
3. [Gerencie reservas atualizadas e cancelamentos](#step-3)

## Etapa 1: Grave os dados de reserva futuros em um perfil de usuário da Braze {#step-1}

Use o endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) da Braze para gravar um [atributo personalizado aninhado]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support) em um perfil de usuário cada vez que uma reserva for realizada. Certifique-se de que o atributo personalizado aninhado contenha todas as informações necessárias para enviar e personalizar a mensagem de lembrete. Neste caso de uso, nomearemos o atributo personalizado aninhado como "trips".

### Adicionar reserva {#add-booking}

Quando um usuário cria uma reserva, use a seguinte estrutura para o array de objetos para enviar os dados à Braze através do endpoint `/users/track`.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": [
               {"trip_id":"1","name":"London Trip","start_date"{$time:"2025-11-11"}},
               {"trip_id":"2","name":"Sydney Trip","start_date"{$time:"2025-11-11"}}
           ]
       }
   ]
}
```
{% endraw %}

O atributo personalizado aninhado "trips" será exibido no perfil de usuário assim.

![Dois atributos personalizados aninhados para uma viagem a Londres e uma viagem a Sydney.]({% image_buster /assets/img/use_cases/2_nested_attributes.png %}){: style="max-width:70%;"}

### Atualizar reserva {#update-booking}

Quando um usuário atualiza uma reserva, use a seguinte estrutura para o array de objetos para enviar os dados à Braze através do endpoint `/users/track`.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$update:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value":"1",
                       "$new_object":{"trip_id":"1","name":"London Trip","start_date":{"$time":"2025-11-11"}}
                   }
               ]
           }
       }
 ]
}
```
{% endraw %}

### Remover reserva {#remove-booking}

{% tabs %}
{% tab /users/track endpoint %}
#### Enviar dados através do endpoint `/users/track` {#send-data-through-the-userstrack-endpoint}

Quando um usuário exclui uma reserva, use a seguinte estrutura para o array de objetos para enviar os dados à Braze através do endpoint `/users/track`.

{% raw %}
```json

{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$remove:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value": "1"
                   }
               ]
           }
       }
   ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK or kit de desenvolvimento de software %}
#### Gravar atributos aninhados nos perfis de usuário através do SDK or kit de desenvolvimento de software {#write-nested-attributes-to-user-profiles-through-the-sdk}

Se você está coletando reservas de compromissos com seu app, website ou ambos e deseja gravar esses dados diretamente em um perfil de usuário, pode usar o SDK or kit de desenvolvimento de software da Braze para transmitir esses dados. Aqui está um exemplo utilizando o Web SDK or kit de desenvolvimento de software:

{% raw %}
```json
const json = [{
  "id": 1,
  "name": "London Trip",
  "start_date": {"$time”: “2025-05-08”}
}, {
  "id": 1,
  "name": "Sydney Trip",
  "start_date": {"$time”: “2025-11-11”}
}];
braze.getUser().setCustomUserAttribute("trips", json);
```
{% endraw %}
{% endtab %}
{% endtabs %}

A Braze remove a reserva especificada do atributo personalizado aninhado no perfil de usuário e exibe quaisquer reservas restantes.

![Um atributo personalizado aninhado para uma viagem a Londres.]({% image_buster /assets/img/use_cases/1_nested_attribute.png %}){: style="max-width:70%;"}

## Etapa 2: Configure e lance uma mensagem de lembrete de reserva {#step-2}

### Etapa 2a: Crie um público-alvo {#step-2a-create-a-target-audience}
Crie um público-alvo para receber lembretes usando segmentação multicritério. Por exemplo, se você quiser enviar um lembrete dois dias antes da data da reserva, selecione o seguinte:

- Uma data de início **em mais de 1 dia** e
- Uma data de início **em menos de 2 dias**

![Um atributo personalizado aninhado "trips" com critérios para uma data de início que seja mais de um dia e menos de dois dias.]({% image_buster /assets/img/use_cases/custom_nested_attribute.png %})

### Etapa 2b: Crie sua mensagem {#step-2b-create-your-message}

Crie a mensagem de e-mail de lembrete seguindo as etapas em [Criando um e-mail com HTML personalizado]({{site.baseurl}}/user_guide/channels/email/html_editor). Use Liquid para personalizar a mensagem com dados do atributo personalizado do cliente que você criou ("trips"), como neste exemplo.

{% raw %}
```liquid
{% assign dates = {{custom_attribute.${trips}}} %}
{% assign today = "now" | date: "%s" %}
{% assign two_days = today | plus: 172800 | date: "%F" %}
You have the following booked in 2 days! Check the information below:
{% for date in dates %}
{% if date.start_date == two_days %}
{{date.trip_id}}
{{date.name}}
{% endif %}
{% endfor %}
```
{% endraw %}

### Etapa 2c: Lance sua Campaign {#step-2c-launch-your-campaign}

Lance a Campaign para a mensagem de e-mail de lembrete. Agora, cada vez que a Braze recebe o atributo personalizado "trips", ela agenda uma mensagem de acordo com os dados incluídos no objeto da respectiva reserva.

## Etapa 3: Gerencie atualizações de reservas e cancelamentos {#step-3}

Agora que você está enviando mensagens de lembrete, pode configurar mensagens de confirmação para enviar quando as reservas forem atualizadas ou canceladas.

### Etapa 3a: Envie dados atualizados {#step-3a-send-updated-data}

{% tabs %}
{% tab /users/track %}

#### Enviar dados através do endpoint `/users/track`
Use o endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) da Braze para enviar um evento personalizado quando um usuário atualiza ou cancela uma reserva. Nesse evento, coloque os dados necessários nas propriedades do evento que confirmarão a mudança.

Vamos supor que, neste caso de uso, um usuário atualizou a data de sua viagem para Sydney. O evento seria assim:

{% raw %}
```json
{
  "events": [
    {
      "external_id": "user_id",
      "name": "trip_updated",
      "time": "2025-03-07T08:19:23+01:00",
      "properties": {
        "id": 2,
        "name": "Sydney Trip",
        "old_time": "2025-11-12"
        "new_time": "2026-01-21"
      }
    }
  ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK or kit de desenvolvimento de software %}

#### Gravar atributos aninhados nos perfis de usuário através do SDK or kit de desenvolvimento de software

Envie eventos personalizados para o perfil de usuário através do SDK or kit de desenvolvimento de software. Por exemplo, se você estiver usando o web SDK or kit de desenvolvimento de software, poderá enviar:

{% raw %}
```json
braze.logCustomEvent("trip_updated", {
  id: 2,
  name: "Sydney Trip",
  old_time: "2025-11-12",
  new_time: "2026-01-21"
});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Etapa 3b: Crie uma mensagem para confirmar a atualização {#step-3b-create-a-message-to-confirm-the-update}

Crie uma [Campaign baseada em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) para enviar ao usuário uma confirmação da reserva atualizada. Você pode [usar Liquid para inserir propriedades do evento]({{site.baseurl}}/user_guide/data/activation/events/custom_events) que refletem o nome, o horário antigo e o novo horário da reserva (ou apenas o nome, se for um cancelamento) na própria mensagem.

Por exemplo, você poderia redigir a seguinte mensagem:

{% raw %}
```liquid
Hi {{${first_name}}}, you have successfully updated the date of your trip, {{event_properties.${name}}}, from {{event_properties.${old_time}}} to {{event_properties.${new_time}}}
```
{% endraw %}

### Etapa 3c: Modifique o perfil de usuário para refletir a atualização {#step-3c-modify-the-user-profile-to-reflect-the-update}

Por fim, para enviar os lembretes de reserva das etapas 1 e 2 com base nos dados mais recentes, atualize os atributos personalizados aninhados para refletir a alteração ou o cancelamento na reserva.

#### Reserva atualizada {#updated-booking}

Se o usuário neste caso de uso atualizou sua viagem para Sydney, você usaria o endpoint `/users/track` para alterar a data com uma chamada como esta:

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "trips": {
	  "$update": [
	    {
            "$identifier_key": "id",
            "$identifier_value": 2,
            "$new_object": {
              "start_date": "2026-01-21"
            }
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

#### Reserva cancelada {#cancelled-booking}

Se o usuário neste caso de uso cancelou sua viagem para Sydney, você enviaria a seguinte chamada para o endpoint `/users/track`:

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "trips": {
	  "$remove": [
	   {
            "$identifier_key": "id",
            "$identifier_value": 2
          }
         ]
      }
    }
  ]
}
```
{% endraw %}

Depois que essas chamadas forem enviadas e o perfil de usuário for atualizado, as mensagens de lembrete de reserva refletirão os dados mais recentes sobre as datas de reserva do usuário.