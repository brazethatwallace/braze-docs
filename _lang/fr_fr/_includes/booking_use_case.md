# Cas d'utilisation : Système d'e-mail de rappel de réservation

> Braze est une plateforme complète d'engagement client conçue pour être hautement programmable. Dans ce cas d'utilisation, nous vous montrons quelques-unes des façons dont Braze met à votre disposition des fonctionnalités que vous pouvez intégrer à des cas d'utilisation situés à l'intersection du produit et du marketing, comme les systèmes de réservation.

Ce cas d'utilisation montre comment utiliser les fonctionnalités de Braze pour créer un service d'envoi d'e-mails de rappel de réservation. Ce service permettra aux utilisateurs de prendre des rendez-vous et leur enverra des rappels concernant leurs rendez-vous à venir. Bien que ce cas d'utilisation repose sur des e-mails, vous pouvez envoyer des messages sur n'importe quel canal, ou sur plusieurs à la fois, à partir d'une seule mise à jour du profil utilisateur.

Autres avantages de la création de ce service :
- Les messages envoyés bénéficient d'un suivi et d'un rapport complets.
- Les utilisateurs non techniques de l'entreprise peuvent mettre à jour le contenu des messages.
- Les messages respectent les statuts d'abonnement et de désabonnement définis sur les profils utilisateurs selon la configuration de la campagne.
- Vous pouvez exploiter à la fois les données de réservation et les données d'interaction avec les messages pour segmenter et cibler les utilisateurs en vue de messages supplémentaires. Par exemple, vous pouvez recibler les personnes qui n'ouvrent pas le rappel initial en leur envoyant un rappel supplémentaire avant leur rendez-vous.

Suivez ces étapes pour mettre en œuvre ce cas d'utilisation :
1. [Écrire les données de réservation à venir dans un profil utilisateur Braze](#step-1)
2. [Configurer et lancer un message de rappel de réservation](#step-2)
3. [Gérer les mises à jour de réservation et les annulations](#step-3)

## Étape 1 : Écrire les données de réservation à venir dans un profil utilisateur Braze {#step-1}

Utilisez l'endpoint Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour écrire un [attribut personnalisé imbriqué]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/) dans le profil d'un utilisateur à chaque réservation. Assurez-vous que l'attribut personnalisé imbriqué contient toutes les informations nécessaires pour envoyer et personnaliser le message de rappel. Dans ce cas d'utilisation, nous nommerons l'attribut personnalisé imbriqué « trips ».

### Ajouter une réservation

Lorsqu'un utilisateur crée une réservation, utilisez la structure suivante pour le tableau d'objets afin d'envoyer les données à Braze via l'endpoint `/users/track`.

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

L'attribut personnalisé imbriqué « trips » s'affichera dans le profil utilisateur de la manière suivante.

![Deux attributs personnalisés imbriqués pour un voyage à Londres et un voyage à Sydney.]({% image_buster /assets/img/use_cases/2_nested_attributes.png %}){: style="max-width:70%;"}

### Mettre à jour une réservation
Lorsqu'un utilisateur met à jour une réservation, utilisez la structure suivante pour le tableau d'objets afin d'envoyer les données à Braze via l'endpoint `/users/track`.

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

### Supprimer une réservation

{% tabs %}
{% tab /users/track endpoint %}
#### Envoyer des données via l'endpoint `/users/track`
Lorsqu'un utilisateur supprime une réservation, utilisez la structure suivante pour le tableau d'objets afin d'envoyer les données à Braze via l'endpoint `/users/track`.

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
{% tab SDK %}
#### Écrire des attributs imbriqués dans les profils utilisateurs via le SDK

Si vous collectez des réservations de rendez-vous avec votre application, votre site web ou les deux, et que vous souhaitez écrire ces données directement dans un profil utilisateur, vous pouvez utiliser le SDK Braze pour transmettre ces informations. Voici un exemple avec le SDK Web :

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

Braze supprime la réservation spécifiée de l'attribut personnalisé imbriqué dans le profil utilisateur et affiche les réservations restantes.

![Un attribut personnalisé imbriqué pour un voyage à Londres.]({% image_buster /assets/img/use_cases/1_nested_attribute.png %}){: style="max-width:70%;"}

## Étape 2 : Configurer et lancer un message de rappel de réservation {#step-2}

### Étape 2a : Créer une audience cible
Créez une audience cible pour recevoir les rappels à l'aide d'une segmentation multicritères. Par exemple, si vous souhaitez envoyer un rappel deux jours avant la date de réservation, sélectionnez les critères suivants :

- Une date de début **dans plus d'un jour** et
- Une date de début **dans moins de 2 jours**

![Un attribut personnalisé imbriqué « trips » avec des critères pour une date de début comprise entre un jour et deux jours.]({% image_buster /assets/img/use_cases/custom_nested_attribute.png %})

### Étape 2b : Créer votre message

Créez le message de rappel par e-mail en suivant les étapes décrites dans [Création d'un e-mail avec HTML personnalisé]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/). Utilisez Liquid pour personnaliser le message avec les données de l'attribut personnalisé que vous avez créé (« trips »), comme dans cet exemple.

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

### Étape 2c : Lancer votre campagne

Lancez la campagne pour le message de rappel par e-mail. Désormais, chaque fois que Braze reçoit l'attribut personnalisé « trips », Braze planifie un message en fonction des données incluses dans l'objet de la réservation correspondante.

## Étape 3 : Gérer les mises à jour de réservation et les annulations {#step-3}

Maintenant que vous envoyez des messages de rappel, vous pouvez configurer des messages de confirmation à envoyer lorsque des réservations sont mises à jour ou annulées.

### Étape 3a : Envoyer les données mises à jour

{% tabs %}
{% tab /users/track %}

#### Envoyer des données via l'endpoint `/users/track`
Utilisez l'endpoint Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour envoyer un événement personnalisé lorsqu'un utilisateur met à jour ou annule une réservation. Intégrez les données nécessaires dans les propriétés d'événement pour confirmer la modification.

Supposons que dans ce cas d'utilisation, un utilisateur ait mis à jour la date de son voyage à Sydney. L'événement se présenterait ainsi :

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
{% tab SDK %}

#### Écrire des attributs imbriqués dans les profils utilisateurs via le SDK

Envoyez des événements personnalisés au profil utilisateur via le SDK. Par exemple, si vous utilisez le SDK Web, vous pouvez envoyer :

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

### Étape 3b : Créer un message pour confirmer la mise à jour

Créez une [campagne basée sur des actions]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) pour envoyer à l'utilisateur une confirmation de sa réservation mise à jour. Vous pouvez [utiliser Liquid pour intégrer les propriétés d'événement]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) qui reflètent le nom, l'ancienne date et la nouvelle date de la réservation (ou uniquement le nom en cas d'annulation) directement dans le message.

Par exemple, vous pouvez rédiger le message suivant :

{% raw %}
```liquid
Hi {{${first_name}}}, you have successfully updated the date of your trip, {{event_properties.${name}}}, from {{event_properties.${old_time}}} to {{event_properties.${new_time}}}
```
{% endraw %}

### Étape 3c : Modifier le profil utilisateur pour refléter la mise à jour

Enfin, pour que les rappels de réservation des étapes 1 et 2 s'appuient sur les données les plus récentes, mettez à jour les attributs personnalisés imbriqués afin de refléter la modification ou l'annulation de la réservation.

#### Réservation mise à jour

Si l'utilisateur de ce cas d'utilisation a mis à jour son voyage à Sydney, vous utiliseriez l'endpoint `/users/track` pour modifier la date avec un appel comme celui-ci :

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

#### Réservation annulée

Si l'utilisateur de ce cas d'utilisation a annulé son voyage à Sydney, vous enverriez l'appel suivant à l'endpoint `/users/track` :

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

Une fois ces appels envoyés et le profil utilisateur mis à jour, les messages de rappel de réservation refléteront les données les plus récentes concernant les dates de réservation de l'utilisateur.