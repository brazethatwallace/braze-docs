---
nav_title: Kognitiv Inspire
article_title: Kognitiv Inspire
description: "Kognitiv Inspire est un système technologique de fidélisation qui vous permet de mettre en œuvre et d'évaluer votre stratégie de fidélisation, en offrant des capacités innovantes et des communications personnalisées avec les membres pour une meilleure efficacité du programme."
alias: /partners/kognitiv/
page_type: partner
search_tag: Partner
---

# Kognitiv Inspire

> [Kognitiv Inspire](http://kognitiv.com) est un système technologique de fidélisation qui permet d'offrir des expériences clients inégalées grâce à des programmes de fidélisation axés sur les résultats qui amplifient l'engagement client, augmentent les dépenses et célèbrent les comportements loyaux.

_Cette intégration est maintenue par Kognitiv Inspire._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Kognitiv vous permet de mettre en œuvre et d'évaluer votre stratégie de fidélisation, en offrant des capacités innovantes et des communications sur mesure avec les membres pour une meilleure efficacité du programme.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Kognitiv | Un compte [Kognitiv](http://kognitiv.com) est nécessaire pour bénéficier de ce partenariat. |
| Clé API Kognitiv | Une clé REST API Kognitiv. Cette clé peut être créée dans la page **API Security Tokens**. |
| Endpoint REST de Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'URL de Braze pour [votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation {#use-cases}

- **Inscription personnalisée au programme de fidélisation** : propulsez vos membres dans leur parcours de fidélité grâce à une inscription fluide au programme et à une notification de bienvenue personnalisée diffusée sur leur canal préféré.
- **Octroi de récompenses et notification d'engagement** : renforcez la fidélité de vos clients en émettant des récompenses et des notifications qui célèbrent chaque jalon des membres.
- **Classification et segmentation stratégiques des membres** : permettez un engagement plus personnalisé en hiérarchisant et en segmentant les membres en fonction des dépenses, de l'engagement et de règles commerciales simples ou complexes adaptées aux besoins spécifiques de votre marque.
- **Notification en temps réel de l'éligibilité à une promotion** : faites en sorte que chaque membre se sente spécial en l'informant instantanément de son éligibilité à des promotions exclusives.

## Intégration {#integration}

Utilisez les webhooks de Kognitiv pour envoyer des requêtes à Braze lorsque des événements de fidélisation se produisent. Les exemples suivants illustrent comment utiliser Kognitiv et Braze pour émettre une récompense, enregistrer un utilisateur Kognitiv dans Braze et lui envoyer un e-mail de bienvenue.

{% raw %}
### Distribution de récompenses Braze {#braze-issue-reward}

L'exemple Kognitiv suivant attribue une récompense à un membre. Kognitiv Inspire communiquera cet événement d'émission de récompense à Braze en tant qu'événement personnalisé via des webhooks. Pour envoyer un e-mail de suivi afin de communiquer la récompense, créez une Campaign ou un Canvas qui se déclenche à partir de cet événement personnalisé.

**URL du webhook** : `<braze-api-rest-endpoint>`
**Corps de la requête** : `Raw Text`

- **Méthode HTTP** : POST
- **En-têtes de la requête** :
  - **Authorization** : Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### Corps de la requête {#request-body}

```json
{
  "events" : [
    {
    "external_id" : "{{memberId}}",
    "app_id" : "93ec5a59-3752-4a45-8559-55b61209ba38",
    "name" : "rewards_issued",
    "time" : "{{issuedDate}}",
    "issued_date" : "{{issuedDate}}",
    "issued_location_name" : "{{issuedLocationName}}",
    "reward_type" : "{{rewardType}}"
    }
  ]
}
```

### Créer un utilisateur et envoyer un e-mail de bienvenue {#create-a-user-and-send-a-welcome-email}

L'exemple Kognitiv suivant crée un nouvel utilisateur dans Braze lorsqu'il s'inscrit à KLS. Pour planifier un e-mail de bienvenue pour cet utilisateur, créez une Campaign ou un Canvas dans Braze qui se déclenche sur la base d'attributs personnalisés spécifiques.

**URL du webhook** : `<braze-api-rest-endpoint>` <br>
**Corps de la requête** : `Raw Text`

- **Méthode HTTP** : POST
- **En-têtes de la requête** :
  - **Authorization** : Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### Corps de la requête

```json
{
  "attributes": [
    {
      "app_id": "93ec5a59-3752-4a45-855b6109ba38",
      "bio": "Software Architect",
      "country": "{{memberAddressCO}}",
      "email": "{{memberEmail}}",
      "email_subscribe": "opted_in",
      "external_id": "{{memberId}}",
      "first_name": "{{memberFirstName}}",
      "home_city": "{{memberAddressCity}}",
      "time_zone": "America/Chicago",
      "total_points_balance": "{{memberPointsAvailable}}",
      "CreatedKLS": "{{issuedTimestamp}}",
      "email_contact_allowed" : "{{memberEmailContactAllowed}}",
      "sms_contact_allowed" : "{{memberSmsContactAllowed}}",
      "date_joined": "{{issuedDate}}"
    }
  ]
}
```
{% endraw %}

## Documentation et fonctionnalités d'intégration de Kognitiv Inspire {#kognitiv-inspire-documentation-and-integration-features}

Une fois Braze intégré à Kognitiv Inspire, Kognitiv vous donne accès à son vaste portefeuille d'API, à ses fonctionnalités webhook de pointe et à ses solides capacités d'importation et d'exportation de données pour un transfert en masse fluide. Pour plus d'informations sur les fonctionnalités et les possibilités d'intégration de Kognitiv Inspire, consultez le [guide des ressources](https://info.kognitivloyalty.com) de Kognitiv ou contactez-les pour une démonstration guidée.

### Endpoints

**Autorisation REST API**
- Région États-Unis : `https://app.kognitivloyalty.com/Auth/connect/token`
- Région CA/EMEA : `https://ca.kognitivloyalty.com/Auth/connect/token`
- Région APAC : `https://aus.kognitivloyalty.com/Auth/connect/token`

**REST API (URL de base)**
- Région États-Unis : `https://app.kognitivloyalty.com/api`
- Région CA/EMEA : `https://ca.kognitivloyalty.com/api`
- Région APAC : `https://aus.kognitivloyalty.com/api`

**Endpoints des services web (URL de base)**
- Région États-Unis : `https://app.kognitivloyalty.com/WS`
- Région CA/EMEA : `https://ca.kognitivloyalty.com/WS`
- Région APAC : `https://aus.kognitivloyalty.com/WS`

Pour plus d'informations sur la configuration des jetons d'accès et des endpoints SFTP, contactez Kognitiv pour une démonstration.