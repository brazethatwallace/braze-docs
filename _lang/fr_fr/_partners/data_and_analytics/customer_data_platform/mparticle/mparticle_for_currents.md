---
nav_title: mParticle pour Currents
article_title: mParticle pour Currents
alias: /partners/mparticle_for_currents/
description: "Cet article de référence présente le partenariat entre Braze Currents et mParticle, une plateforme de données client qui collecte et achemine les informations entre les sources de votre pile marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle pour Currents {#mparticle-for-currents}

> [mParticle](https://www.mparticle.com) est une plateforme de données client qui collecte et achemine des informations provenant de sources multiples vers divers autres emplacements de votre pile marketing.

L'intégration de Braze et mParticle vous permet de contrôler de façon fluide le flux d'informations entre les deux systèmes. Avec [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), vous pouvez également connecter les données à mParticle pour les rendre exploitables dans l'ensemble des outils de croissance.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Currents | Pour pouvoir exporter des données dans mParticle, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) pour votre compte. |
| Compte mParticle | Un [compte mParticle](https://app.mparticle.com/login) est nécessaire pour profiter de ce partenariat. |
| Clé et secret serveur-à-serveur mParticle | Vous pouvez les obtenir en accédant à votre tableau de bord mParticle et en créant les [flux nécessaires](#step-1-create-feeds) qui permettent à mParticle de recevoir les données d'interaction de Braze pour les plateformes iOS, Android et Web. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## À propos des identifiants mParticle {#about-mparticle-credentials}

mParticle dispose d'identifiants au niveau de l'application et au niveau de l'espace de travail, ce qui a un impact sur la façon dont vos événements sont envoyés.

- **Au niveau de l'application :** mParticle sépare les événements par application individuelle, ce qui signifie que les identifiants au niveau de l'application que vous fournissez pour votre application iOS ne peuvent être utilisés que pour envoyer des événements spécifiques à iOS.
- **Au niveau de l'espace de travail :** mParticle regroupe tous les événements (qui ne sont **pas** spécifiques à une application), ce qui signifie que les identifiants au niveau de l'espace de travail que vous fournissez à votre groupe d'applications seront utilisés pour envoyer tous vos événements non spécifiques à une application.

Vous pouvez considérer cela comme mParticle ingérant un « flux » basé sur chaque application individuelle. Par exemple, si vous avez une application pour iOS, une pour Android et une pour le Web, vos événements seront disjoints. Cela signifie que si vous fournissez les mêmes identifiants pour chaque application, un seul flux mParticle sera utilisé pour recevoir toutes les données de toutes vos applications, sans duplication.

## Intégration {#integration}

### Étape 1 : Créer des flux {#step-1-create-feeds}

Depuis votre compte administrateur mParticle, accédez à **Setup > Inputs**. Localisez **Braze** dans le **Directory** de mParticle et ajoutez l'intégration de flux.

L'intégration de flux Braze prend en charge quatre flux distincts : iOS, Android, Web et Unbound. Le flux Unbound peut être utilisé pour les événements tels que les e-mails qui ne sont pas liés à une plateforme. Vous devrez créer une entrée pour chaque flux de plateforme principal. Vous pouvez créer des entrées supplémentaires depuis **Setup > Inputs**, dans l'onglet **Feed Configurations**.

![Configuration des entrées de flux mParticle affichant les options de flux Braze pour iOS, Android, Web et Unbound.]({% image_buster /assets/img/braze-feed-inputs.png %})

Pour chaque flux, sous **Act as Platform**, sélectionnez la plateforme correspondante dans la liste. Si vous ne voyez pas d'option pour sélectionner un flux **act-as**, les données seront traitées comme non liées, mais pourront tout de même être transmises aux sorties d'entrepôt de données.

![La première boîte de dialogue d'intégration, vous invitant à fournir un nom de configuration, à déterminer un état de flux et à sélectionner une plateforme à simuler.]({% image_buster /assets/img/braze-feed-act1.png %}){: style="max-width:40%;"}  ![La seconde boîte de dialogue d'intégration affichant la clé serveur-à-serveur et le secret serveur-à-serveur.]({% image_buster /assets/img/braze-feed-act2.png %}){: style="max-width:37%;"}

Au fur et à mesure que vous créez chaque entrée, mParticle vous fournira une clé et un secret. Copiez ces identifiants en veillant à noter à quel flux chaque paire d'identifiants correspond.

### Étape 2 : Créer un Current {#step-2-create-current}

Dans Braze, accédez à **Currents > + Create Current > Create mParticle Export**. Fournissez un nom d'intégration, une adresse e-mail de contact ainsi que la clé API mParticle et la clé secrète mParticle pour chaque plateforme. Ensuite, sélectionnez les événements que vous souhaitez suivre ; une liste des événements disponibles est fournie. Enfin, cliquez sur **Launch Current**.

![La page mParticle Currents dans Braze. Vous y trouverez des champs pour le nom d'intégration, l'adresse e-mail de contact, la clé API et la clé secrète.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
Il est important de maintenir votre clé API mParticle et votre clé secrète mParticle à jour ; si les identifiants de votre connecteur expirent, celui-ci cessera d'envoyer des événements. Si cette situation persiste pendant plus de **5 jours**, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

Tous les événements envoyés à mParticle incluront le `external_user_id` de l'utilisateur en tant que `customerid`. À l'heure actuelle, Braze n'envoie pas de données d'événements pour les utilisateurs dont le `external_user_id` n'est pas défini. Si vous souhaitez mapper le `external_user_id` vers un autre identifiant dans mParticle qui n'est pas le `customerid` par défaut, veuillez contacter votre CSM Braze.

## Événements Currents pris en charge {#supported-currents-events}

Braze prend en charge l'exportation des événements suivants vers mParticle :

- [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Pour connaître la structure du payload de chaque événement, sélectionnez l'onglet **mParticle** dans le [glossaire des événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) et le [glossaire des événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

Pour en savoir plus sur l'intégration mParticle, consultez la [documentation mParticle](http://docs.mparticle.com/integrations/braze/feed).