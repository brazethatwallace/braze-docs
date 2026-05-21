---
nav_title: Amplitude
article_title: Amplitude
page_order: 0
alias: /partners/amplitude_recommend/
description: "Cet article de référence présente le partenariat entre Braze et Amplitude, une plateforme d'analyse des produits et d'aide à la décision."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomamplitude-integration-with-braze-stylefloatrightwidth120pxborder0-classnoimgborderamplitude}

> [Amplitude](https://amplitude.com/) est une plateforme d'analyse de produits et d'aide à la décision.

L'intégration bidirectionnelle entre Braze et Amplitude vous permet d'[importer vos cohortes Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/), traits d'utilisateurs et événements dans Braze, ainsi que de créer des segments pouvant cibler les utilisateurs dans de futures Campaigns ou Canvas. Vous pouvez également tirer parti de Braze Currents pour [exporter vos événements Braze vers Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/#data-export-integration) afin d'analyser plus en profondeur vos données produits et marketing.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Amplitude | Un [compte Amplitude](https://amplitude.com/) est nécessaire pour bénéficier de ce partenariat. |
| Currents | Pour pouvoir exporter des données dans Amplitude, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Choisir une intégration {#choose-an-integration}

Amplitude et Braze proposent deux méthodes d'intégration différentes. Consultez la documentation suivante pour déterminer quelles méthodes répondent à vos besoins :

- Braze Event Streaming : une intégration qui vous permet de transmettre les données brutes des événements d'Amplitude directement à Braze.
- [Importation de cohorte]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/) : une intégration qui vous permet de transmettre les cohortes d'Amplitude à Braze.

## Braze Event Streaming

### Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Clé API REST Braze | Une clé API REST Braze avec toutes les autorisations.<br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Settings** > **API Keys**. |
| Endpoint REST Braze | [L'URL de votre endpoint REST][1]. Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Identifiant de l'application Braze | L'identifiant de l'application qui recevra les événements Amplitude. Vous trouverez cette information dans le **tableau de bord de Braze > Console de développement > Paramètres**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

### Configuration d'Amplitude {#amplitude-setup}

1. Dans Amplitude, accédez à **Data Destinations**, puis recherchez « Braze - Event Stream ».
2. Saisissez un nom de synchronisation, puis cliquez sur **Create Sync**.
3. Cliquez sur **Edit** et indiquez votre endpoint REST API Braze, votre clé REST API et l'identifiant de l'application Braze.
4. Utilisez le filtre d'envoi d'événements pour sélectionner les événements à envoyer. Vous pouvez envoyer tous les événements, mais Amplitude recommande de choisir les plus importants.
5. Lorsque vous avez terminé, activez la destination et enregistrez.

Reportez-vous à la section [Braze Event Streaming](https://www.docs.developers.amplitude.com/data/destinations/braze/) pour plus d'informations sur cette intégration.

## Synchronisation des traits d'utilisateur et des calculs {#sync-user-traits-and-computations}

Utilisez les audiences pour envoyer les propriétés et les calculs des utilisateurs à Braze en tant qu'attributs personnalisés. Vous pourrez synchroniser les propriétés des utilisateurs ou les propriétés calculées pour les utilisateurs qui ont été actifs au cours des 90 derniers jours.

Lorsque la propriété d'un utilisateur ou un calcul est mis à jour, Amplitude met à jour un attribut personnalisé dans Braze portant le même nom que la propriété de l'utilisateur ou le calcul.

Les synchronisations des traits d'utilisateur et des calculs créeront de nouveaux utilisateurs pour les identifiants d'utilisateur qui n'existent pas encore dans Braze. Les calculs et les traits d'utilisateur ne peuvent être synchronisés qu'à l'aide d'identifiants d'utilisateur. Un identifiant d'utilisateur peut être l'un des éléments suivants :
- ID externe
- ID Braze
- Alias d'utilisateur
- Adresse e-mail

Reportez-vous à la documentation d'Amplitude pour en savoir plus sur la [synchronisation des propriétés, des recommandations et des cohortes vers des destinations tierces](https://help.amplitude.com/hc/en-us/articles/360060055531).

#### Comment synchroniser les propriétés et les calculs des utilisateurs {#how-to-sync-user-properties-and-computations}

Dans Amplitude Audiences, sélectionnez **Syncs > Create Sync**.

![]({% image_buster /assets/img/amplitude11.png %})

Ensuite, choisissez de synchroniser une propriété d'utilisateur, un calcul, une cohorte ou une recommandation.

{% tabs %}
{% tab Synchronisation d'une propriété d'utilisateur %}

Sélectionnez **User Property**, puis la propriété d'utilisateur souhaitée à synchroniser.

![]({% image_buster /assets/img/amplitude7.png %})

Ensuite, sélectionnez une destination vers laquelle synchroniser votre propriété d'utilisateur.

![]({% image_buster /assets/img/amplitude8.png %})

Enfin, définissez la fréquence de votre synchronisation.

![Définissez votre cadence comme une synchronisation unique ou une synchronisation planifiée.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% tab Synchronisation d'un calcul %}

Sélectionnez **Computation**, puis le calcul souhaité à synchroniser.

![]({% image_buster /assets/img/amplitude10.png %})

Ensuite, sélectionnez une destination vers laquelle synchroniser votre calcul.

![]({% image_buster /assets/img/amplitude8.png %})

Enfin, définissez la fréquence de votre synchronisation.

![Définissez votre cadence comme une synchronisation unique ou une synchronisation planifiée.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% endtabs %}

## Résolution des problèmes {#troubleshooting}

### « We do not have enough data yet for this filter » lors de la synchronisation d'une cohorte {#we-do-not-have-enough-data-yet-for-this-filter-when-syncing-a-cohort}

Si vous obtenez cette erreur lors de l'[importation d'une cohorte Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/) dans Braze, essayez les étapes suivantes :

1. **Vérifiez l'alignement des ID utilisateur.** L'ID utilisateur dans Amplitude (et non l'ID Amplitude) doit correspondre exactement à l'ID utilisateur externe dans Braze (et non l'ID Braze ou BSON). Par exemple, l'ID utilisateur `12345` dans Amplitude doit correspondre à l'ID utilisateur externe `12345` dans Braze.
2. **Régénérez votre clé API Braze.** Dans le tableau de bord de Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** > **Amplitude** et sélectionnez **Generate New Key**. Réessayez ensuite la synchronisation de la cohorte Amplitude avec la nouvelle clé API.
3. **Confirmez que la cohorte a bien été synchronisée dans Amplitude.** Contactez le [support Amplitude](https://help.amplitude.com/) pour vérifier que la cohorte a été synchronisée avec succès du côté d'Amplitude avant de poursuivre la résolution des problèmes dans Braze.

## Endpoints de l'API du profil utilisateur Amplitude {#amplitude-user-profile-api-endpoints}

Pour découvrir certains des endpoints courants de l'API Amplitude pouvant être utilisés avec le contenu connecté, consultez notre documentation dédiée à l'[API Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_user_profile_api/).