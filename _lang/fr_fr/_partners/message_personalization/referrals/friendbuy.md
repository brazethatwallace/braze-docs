---
nav_title: Friendbuy
article_title: Friendbuy
description: "Découvrez comment intégrer Friendbuy à Braze."
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> Utilisez l'intégration entre [Friendbuy](https://www.friendbuy.com/) et Braze pour étendre vos capacités d'e-mail et de SMS tout en automatisant sans effort les communications de votre programme de recommandation et de fidélisation. Braze créera des profils clients pour tous les numéros de téléphone ayant fait l'objet d'un abonnement et collectés par l'intermédiaire de Friendbuy.

_Cette intégration est maintenue par Friendbuy._

## Conditions préalables {#prerequisites}

Avant de commencer, vous aurez besoin des éléments suivants :

| Prérequis          | Description                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Un compte Friendbuy   | Un [compte Friendbuy](https://retailer.friendbuy.io/) est nécessaire pour profiter de ce partenariat.                                                              |
| Une clé REST API de Braze  | Une clé REST API de Braze avec les autorisations `users.track`. Celle-ci peut être créée dans le tableau de bord de Braze depuis **Settings** > **API Keys**.        |
| Un endpoint REST de Braze | L'[URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), qui dépend de l'URL de votre instance Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration de Friendbuy {#integrating-friendbuy}

Dans [Friendbuy](https://retailer.friendbuy.io/), accédez à **Developer Center** > **Integrations**, puis sur la carte d'intégration de Braze, sélectionnez **Add integration**.

![La carte d'intégration de Braze dans Friendbuy.]({% image_buster /assets/img/friendbuy/choosing_braze.png %}){: style="max-width:75%;"}

Dans le formulaire, saisissez votre endpoint REST et votre clé API, puis sélectionnez **Install Integration**.

![Le formulaire d'intégration de Friendbuy.]({% image_buster /assets/img/friendbuy/install_form.png %}){: style="max-width:55%;"}

Retournez à votre [compte Friendbuy](https://retailer.friendbuy.io/) et actualisez la page. Si votre intégration a réussi, vous verrez un message similaire au suivant :

![Intégration installée]({% image_buster /assets/img/friendbuy/install_success.png %}){: style="max-width:55%;"}

### Attributs personnalisés {#custom-attributes}

| Nom de l'attribut personnalisé            | Définition                                                                                                                                         | Type de données |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Friendbuy Referral Status**    | Les référents sont classés dans la catégorie *Advocate* et les personnes recommandées sont classées dans la catégorie *Referred Friend*.                                                          | Chaîne de caractères    |
| **Friendbuy Customer Name**      | Le nom que le client a saisi lorsqu'il a soumis ses informations via un widget de recommandation.                                                                 | Chaîne de caractères    |
| **Friendbuy Referral Link**      | Un lien de recommandation personnel (PURL) généré pour un référent. Par exemple, https://fbuy.io/EzcW                                                       | Chaîne de caractères    |
| **Friendbuy Date of Last Share** | La date et l'heure du dernier partage du référent avec un ami via un canal de partage. Si le référent n'a pas encore partagé, la propriété ne sera pas visible. | Heure      |
| **Friendbuy Campaign ID**        | L'ID de campagne associé au lien de recommandation personnel généré pour un référent.                                                               | Chaîne de caractères    |
| **Friendbuy Campaign Name**      | Le nom de campagne associé au lien de recommandation personnel généré pour un référent.                                                             | Chaîne de caractères    |
| **Friendbuy Coupon Code**        | Le code de réduction de recommandation le plus récent distribué au client. Remarque : un seul code sera affiché.                                            | Chaîne de caractères    |
| **Friendbuy Coupon Value**       | La valeur monétaire du dernier code de réduction distribué au client.                                                                     | Nombre    |
| **Friendbuy Coupon Status**      | L'état du dernier code de réduction distribué au client. Remarque : l'état sera « distributed » ou « redeemed ».                            | Chaîne de caractères    |
| **Friendbuy Coupon Currency**    | Code de devise (USD, CAD, etc.) ou pourcentage (%) associé au code de réduction le plus récent distribué au client.                             | Chaîne de caractères    |
| **Friendbuy Coupon Campaign ID** | L'ID de campagne associé au code de réduction généré pour un client.                                                                          | Chaîne de caractères    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Attributs personnalisés" }

## Comportement par défaut {#default-behavior}

Avant que les données clients puissent être envoyées à Braze, les clients doivent donner leur consentement via le widget de recommandation en cochant une ou plusieurs des cases suivantes :

![Widget de recommandation]({% image_buster /assets/img/friendbuy/referral_widget.png %})

{% alert note %}
Friendbuy utilise la norme internationale (E.164) pour vérifier les numéros de téléphone réels. Les numéros non valides, tels que `555-555-5555`, ne seront pas envoyés à Braze.
{% endalert %}

### Comportement des cases à cocher {#checkbox-behavior}

| Case à cocher sélectionnée | Comportement                                                        |
|-------------------|-----------------------------------------------------------------|
| E-mail uniquement        | Seule l'adresse e-mail du client est envoyée à Braze.             |
| Téléphone uniquement        | Seul le numéro de téléphone du client est envoyé à Braze.              |
| Aucune des deux           | Aucune donnée client n'est envoyée à Braze.                              |
| Les deux              | L'adresse e-mail et le numéro de téléphone du client sont envoyés à Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportement des cases à cocher" }