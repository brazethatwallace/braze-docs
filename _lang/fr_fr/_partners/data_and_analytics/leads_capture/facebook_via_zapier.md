---
nav_title: Facebook Lead Ads via Zapier
article_title: Facebook Lead Ads via Zapier
description: "Cet article de référence présente l'intégration entre Braze et Facebook Lead Ads via Zapier pour automatiser le transfert des données de prospects de Facebook vers Braze, permettant ainsi un engagement en temps réel et des actions de suivi personnalisées."
alias: /partners/facebook_via_zapier/
page_type: partner
search_tag: Partner
---

# Intégration Facebook Lead Ads via Zapier {#facebook-lead-ads-via-zapier-integration}

> Grâce à l'intégration Facebook Lead Ads via <a href="https://zapier.com/" target="_blank">Zapier</a>, vous pouvez importer vos prospects depuis Facebook dans Braze et suivre un événement personnalisé lorsque des prospects sont capturés.

Facebook Lead Ads est un format publicitaire qui permet aux entreprises de collecter des informations sur les prospects directement dans Facebook. Ces publicités sont conçues pour rendre le processus de génération de prospects simple et fluide. En tirant parti d'une intégration Zapier et de Braze, vous pouvez automatiser le transfert des données de prospects de Facebook vers Braze, ce qui permet un engagement en temps réel et des actions de suivi personnalisées.

## Prérequis {#prerequisites}

| Conditions requises | Description |
|---|---|
| Compte Zapier | Un compte Zapier est requis pour bénéficier de ce partenariat. Cette intégration nécessite l'utilisation d'<a href="https://zapier.com/app/pricing/" target="_blank">applications Zapier premium</a>, vérifiez donc que votre forfait Zapier donne accès aux applications premium. |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">Accès Facebook Leads</a> | L'accès Facebook Leads est requis pour chaque compte publicitaire que vous prévoyez d'utiliser avec Braze. |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">Facebook Business gestionnaire</a> | Vous utiliserez Facebook Business gestionnaire, un outil centralisé pour gérer les ressources Facebook de votre marque (par exemple, les comptes publicitaires, les pages et les applications), dans le cadre de cette intégration. |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">Compte publicitaire Facebook</a> | Vous aurez besoin d'un compte publicitaire Facebook actif lié au gestionnaire d'entreprise de votre marque. <br><br>Assurez-vous que vous disposez de la permission « Manage ad accounts » pour chaque compte publicitaire que vous prévoyez d'utiliser avec Braze, et que vous avez accepté les conditions générales de votre compte publicitaire. |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">Page Facebook</a> | Vous aurez besoin d'une page Facebook active liée au gestionnaire d'entreprise de votre marque. <br><br>Assurez-vous que vous disposez des permissions « Manage Pages » pour chaque page Facebook que vous prévoyez d'utiliser avec Braze. |
| Endpoint REST Braze | Assurez-vous de connaître l'[URL de votre endpoint REST]({{site.baseurl}}/api/basics#api-definitions). Votre endpoint d'API correspond à l'URL du tableau de bord de votre instance Braze. <br><br> Par exemple, si l'URL de votre tableau de bord est `https://dashboard-03.braze.com`, votre endpoint sera `dashboard-03`. |
| Clé API REST Braze | Assurez-vous de disposer d'une clé API REST Braze avec les permissions `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Créer une campagne Lead Ads avec un formulaire instantané {#step-1-create-a-lead-ads-campaign-with-an-instant-form}

Depuis le gestionnaire de publicités Facebook, créez une <a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">campagne Facebook Leads et un formulaire Facebook Lead Ads</a>.

Vous pouvez utiliser une adresse e-mail ou un numéro de téléphone lorsque vous effectuez une requête vers l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) pour mettre à jour ou créer le profil utilisateur. Pour cette raison, incluez un **champ de contact** pour l'**e-mail** ou le **téléphone** dans votre formulaire de publicité de prospect. Si vous collectez les prénoms ou les noms de famille, collectez-les séparément dans votre formulaire au lieu d'utiliser les noms complets.

### Étape 2 : Connecter votre compte Facebook à Zapier {#step-2-connect-your-facebook-account-to-zapier}

#### Étape 2a : Sélectionner votre méthode de connexion dans Zapier {#step-2a-select-your-connection-method-in-zapier}

Dans Zapier, accédez à **Apps** pour rechercher les applications Facebook disponibles. Sélectionnez **Facebook Lead Ads** ou **Facebook Lead Ads (for Business admins)**.

Pour plus d'informations sur ces deux méthodes de connexion de votre compte Facebook à Zapier, consultez :

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Facebook Lead Ads (for Business Admins)</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">Facebook Lead Ads</a>

![Recherche d'applications Zapier affichant les options de connexion Facebook Lead Ads.]({% image_buster /assets/img/fb_lead_ads_zapier/integration1.png %}){: style="max-width:80%;"}

#### Étape 2b : Ajouter Zapier à l'accès aux prospects dans Facebook Business gestionnaire {#step-2b-add-zapier-to-leads-access-in-facebook-business-manager}

Dans votre Facebook Business gestionnaire, accédez à **Integrations** > **Leads Access** dans le menu de navigation. Sélectionnez votre page Facebook, puis cliquez sur **CRMs**. Dans l'onglet CRM, sélectionnez **Assign CRMs** et ajoutez **Zapier**.

![Page d'accès aux prospects de Facebook Business Manager avec Zapier assigné comme intégration CRM.]({% image_buster /assets/img/fb_lead_ads_zapier/integration2.png %}){: style="max-width:80%;"}

Pour les étapes d'attribution de Zapier en tant qu'intégration CRM, consultez la <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862" target="_blank">documentation</a> de Facebook.

### Étape 3 : Créer votre Zap {#step-3-create-your-zap}

#### Étape 3a : Créer le déclencheur {#step-3a-create-the-trigger}

Une fois votre compte Facebook connecté, vous pouvez procéder à la création d'un Zap. Pour le **déclencheur**, sélectionnez **Facebook Lead Ads** ou **Facebook Lead Ads (for Business Admins)** en fonction de votre choix à l'étape 2.

![Étape de déclencheur Zapier avec Facebook Lead Ads sélectionné.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap1.png %}){: style="max-width:80%;"}

Pour l'**événement**, sélectionnez **New Leads** > **Continue**.

![Sélection de l'événement déclencheur Zapier affichant New Leads.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap2.png %}){: style="max-width:80%;"}

Sélectionnez votre compte Facebook, puis **Continue**.

![Étape de connexion du compte Facebook Zapier pour le déclencheur.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap3.png %}){: style="max-width:80%;"}

Sélectionnez votre page Facebook et le formulaire instantané que vous avez créé précédemment, puis **Continue**.

![Configuration du déclencheur Zapier sélectionnant une page Facebook et un formulaire instantané.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap4.png %}){: style="max-width:80%;"}

Testez ensuite ce déclencheur. Après avoir validé la sortie de votre formulaire, sélectionnez **Continue with selected record**.

#### Étape 3b : Créer une action {#step-3b-create-an-action}

Ajoutez une nouvelle étape, puis sélectionnez **Webhooks by Zapier**. Ensuite, sélectionnez **Custom Request** pour le champ **Event**, puis cliquez sur **Continue**.

![Étape d'action Zapier configurée avec Webhooks by Zapier et Custom Request.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap5.png %}){: style="max-width:80%;"}

Enfin, configurez votre requête personnalisée en insérant les champs dans votre payload. L'extrait de code suivant montre un exemple de payload.

```
{
    "attributes": [
        {
            "email": "<insert_email_field>",
            "first_name": "<insert_first_name_field>",
            "last_name": "<insert_last_name_field>",
            "lead_form": "<insert_form_name_field>",
            "fb_campaign": "<insert_campaign_id_field>",
            "fb_ad_set": "<insert_campaign_id_field>",
            "fb_ad": "<insert_campaign_id_field>",
            "email_subscribe": "subscribed",
            "subscription_groups" : [{
                "subscription_group_id": "<subscription_group_id>",
                "subscription_state": "subscribed"
                }
            ]
        }
    ],
    "events": [
        {
            "email": "<insert_email_field>",
            "name": "<insert_custom_event_name>",
            "time": "<insert_timestamp_field>",
            "_update_existing_only": false
        }
    ]
}`
```

Voici un exemple de ce à quoi cela ressemble dans Zapier :

![Exemple de mappage du payload webhook dans Zapier pour envoyer les champs de prospects Facebook vers Braze.]({% image_buster /assets/img/fb_lead_ads_zapier/configuration_example.png %}){: style="max-width:80%;"}

Après avoir configuré votre webhook, sélectionnez **Continue and test**. Si le test est réussi, vous pouvez publier votre Zap.

### Étape 4 : Tester votre Zap Facebook Lead Ads {#step-4-test-your-facebook-lead-ads-zap}

Pour tester ce flux de bout en bout, utilisez l'outil de test Lead Ads de Facebook dans votre console de développement Facebook. Pour plus d'informations, consultez <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">Testing and Troubleshooting</a>.

## Gestion de l'identité utilisateur {#user-identity-management}

Cette intégration vous permet d'attribuer vos prospects Facebook par e-mail via l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#update-a-user-profile-by-phone-number).

* Si l'e-mail correspond à un profil utilisateur existant, Braze mettra à jour le profil avec les données de prospects Facebook.
* S'il existe plusieurs profils utilisateur avec le même e-mail, Braze donnera la priorité au profil mis à jour le plus récemment disposant d'un ID externe.
* Si l'ID externe n'existe pas, Braze donnera la priorité au profil mis à jour le plus récemment correspondant à l'e-mail.
* Si aucun profil n'existe avec l'e-mail fourni, Braze créera un nouveau profil et un nouveau profil utilisateur alias sera créé. Pour identifier les profils utilisateur alias nouvellement créés, utilisez l'[endpoint `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).

{% alert note %}
Vous pouvez également utiliser un numéro de téléphone ou un ID externe dans la requête envoyée à Braze si ces champs sont disponibles et constituent l'identifiant principal que vous souhaitez utiliser pour l'intégration. Pour ce faire, modifiez le payload de votre requête comme indiqué dans l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).
{% endalert %}

## Résolution des problèmes {#troubleshooting}

{% details J'ai testé le déclencheur et l'action avec succès, alors pourquoi ne puis-je pas publier mon Zap Zapier ? %}
Pour utiliser cette intégration, vous devez disposer d'un <a href="https://zapier.com/app/pricing/" target="_blank">forfait Zapier</a> qui prend en charge les applications premium.
{% enddetails %}

{% details Pourquoi les prospects Facebook ne se synchronisent-ils pas avec Braze ? %}
1. Vérifiez que vous disposez d'un accès administrateur à votre page Facebook, votre compte publicitaire et l'accès aux prospects. Ensuite, reconnectez votre compte dans Zapier.
2. Vérifiez que le formulaire instantané que vous avez créé dans Facebook correspond au formulaire sélectionné dans votre étape de déclencheur.
3. Vérifiez que vous avez attribué l'accès aux prospects à Zapier en accédant à **Facebook Business gestionnaire** > **Integrations** > **Lead Access**.
{% enddetails %}

{% details Pourquoi est-ce que je vois des profils utilisateur en double avec le même e-mail ? %}
Il existe différentes façons de créer et de gérer des profils utilisateur dans Braze en fonction de leur [cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle).

En fonction de vos processus internes et du moment où vous déclenchez la création de clients dans Braze, vous pouvez rencontrer des profils utilisateur en double en raison d'une condition de concurrence entre la création du profil utilisateur par l'intégration et la création de l'utilisateur depuis votre système. Vous pouvez [fusionner les profils utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) dans Braze.
{% enddetails %}

{% details Je n'ai pas de compte Zapier. Comment puis-je déclencher des webhooks Facebook Lead Ads dans Braze ? %}
Si vous n'utilisez pas Zapier et ne prévoyez pas de l'utiliser, vous pouvez créer l'intégration directement depuis Facebook vers Braze. Consultez la <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">documentation Lead Ads</a> pour plus d'informations.

Pour récupérer les prospects depuis Facebook, utilisez les <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">webhooks</a>. Consultez la <a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">documentation Webhooks</a> pour commencer à utiliser les webhooks dans Facebook.

Après avoir établi l'URL des webhooks dans Facebook, travaillez avec votre équipe pour déterminer le meilleur moyen de transmettre les données à l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Comme pour l'approche Zapier, nous recommandons d'effectuer une [requête par e-mail]({{site.baseurl}}/api/endpoints/user_data/post_user_track#update-a-user-profile-by-phone-number) via l'endpoint `users/track`.
{% enddetails %}

{% alert tip %}
Pour plus de conseils de résolution des problèmes, consultez le <a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">guide de résolution des problèmes Facebook Leads</a> de Zapier.
{% endalert %}