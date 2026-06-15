---
nav_title: OneTrust
article_title: OneTrust
description: "Cet article de référence présente le partenariat entre Braze et OneTrust, un fournisseur de logiciels de confidentialité et de sécurité des données, vous permettant d'utiliser le générateur de flux de travail OneTrust pour créer des flux de travail de sécurité pour votre produit."
alias: /partners/onetrust/
page_type: partner
search_tag: Partner

---

# OneTrust

> [OneTrust](https://www.onetrust.com/) est un fournisseur de logiciels de confidentialité et de sécurité offrant la visibilité dont vous avez besoin pour mieux comprendre votre paysage de confiance, les actions à entreprendre pour exploiter des informations pertinentes et l'automatisation pour vous permettre de garder une longueur d'avance sur la concurrence.

_Cette intégration est maintenue par OneTrust._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et OneTrust vous permet d'utiliser le générateur de flux de travail OneTrust pour créer des flux de travail de sécurité pour votre produit.
## Conditions préalables {#prerequisites}

| Exigences | Description |
|---|---|
| Compte OneTrust | Un compte [OneTrust](https://www.onetrust.com/) est nécessaire pour profiter de ce partenariat. |
| Clé API Braze | Une clé REST API de Braze avec les autorisations requises pour l'endpoint que votre action OneTrust utilisera.<br><br>Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Instance Braze | Votre instance Braze peut être obtenue auprès de votre gestionnaire d'onboarding Braze ou sur la [page d'aperçu des API]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

L'intégration suivante fournit des indications sur la création d'un flux de travail de mise à jour du consentement utilisateur et d'un flux de travail de suppression utilisateur. Pour plus de détails sur les autres endpoints Braze pris en charge, reportez-vous à [Autres actions prises en charge](#Other-supported-actions).

### Ajouter les identifiants Braze dans OneTrust {#add-braze-credentials-to-onetrust}

Dans le menu OneTrust **Integrations**, naviguez vers **Credentials** > bouton **Add New** pour faire apparaître l'écran **Select System**. Recherchez **Braze**, puis cliquez sur le bouton **Next**.

Suivez les invites de l'écran **Enter Credential Details** et fournissez les informations suivantes. Enregistrez vos identifiants lorsque vous avez terminé.
  - Nom de l'identifiant
  - Définissez le type de connecteur sur **Web App**
  - Nom d'hôte : `<your-braze-instance-url>`
  - **En-tête de la requête** :
    - **Authorization** : Bearer
    - **Content-Type** : application/json
  - Jeton : `<your-braze-api-key>`

### Ajouter Braze en tant que système {#add-braze-as-a-system}

#### Étape 1 : Créer un flux de travail {#step-1-create-a-workflow}

{% tabs %}
{% tab User Consent Update %}
1. Dans le menu des intégrations OneTrust, naviguez vers **Gallery** > **Braze** > **Add** pour créer un nouveau flux de travail.![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Indiquez un nom et un e-mail de notification dans la fenêtre modale du flux de travail. Cliquez sur le bouton **Create**. Lors de la création, vous accéderez au générateur de flux de travail. Votre flux de travail Braze sera initialisé avec des appels d'API et des actions pouvant être utilisés pour traiter les requêtes de suppression. <br><br>
3. Dans le générateur de flux de travail, choisissez l'action que vous souhaitez déclencher dans le flux de travail.<br>![]({% image_buster /assets/img/onetrust/onetrust2.png %})

{% endtab %}
{% tab User Deletion %}

1. Dans le menu des intégrations OneTrust, naviguez vers **Gallery** > **Braze** > **Add** pour créer un nouveau flux de travail.![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Indiquez un nom et un e-mail de notification dans la fenêtre modale du flux de travail. Cliquez sur le bouton **Create**. Lors de la création, vous accéderez au générateur de flux de travail. Votre flux de travail Braze sera initialisé avec des appels d'API et des actions pouvant être utilisés pour traiter les requêtes de suppression. <br><br>
3. Dans le générateur de flux de travail, choisissez l'action que vous souhaitez déclencher dans le flux de travail.<br>![]({% image_buster /assets/img/onetrust/onetrust8.png %})
{% endtab %}
{% endtabs %}

#### Étape 2 : Sélectionner une action {#step-2-select-action}
{% tabs %}
{% tab User Consent Update %}

1. Lorsque vous avez terminé, cliquez sur **Done** et choisissez **Add Action**. Notez que l'action que vous choisissez dépend du type de préférence mis à jour et de votre endpoint préféré.
- Pour mettre à jour les préférences d'abonnement globales d'un utilisateur, sélectionnez l'action **POST User track - Attributes**.
- Pour mettre à jour les préférences d'un utilisateur en matière de groupe d'abonnement, choisissez l'action **POST User Track - Attributes** ou l'action **POST Set Users Subscription Group Status**.<br>![]({% image_buster /assets/img/onetrust/onetrust4.png %})<br><br>
2. Choisissez l'action souhaitée, sélectionnez vos identifiants Braze créés précédemment et cliquez sur **Next**.<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% tab User Deletion %}

1. Lorsque vous avez terminé, cliquez sur **Done** et choisissez **Add Action**.
- Pour supprimer un utilisateur de Braze, sélectionnez l'action **POST User Delete Action**.
<br>![]({% image_buster /assets/img/onetrust/onetrust9.png %})<br><br>
2. Choisissez l'action souhaitée, sélectionnez vos identifiants Braze créés précédemment et cliquez sur **Next**.<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% endtabs %}
#### Étape 3 : Mettre à jour le corps de la requête {#step-3-update-request-body}
{% tabs %}
{% tab User Consent Update %}

1. Mettez à jour le corps de la requête pour y inclure toutes les valeurs dynamiques nécessaires. Assurez-vous que le corps de l'action correspond à l'[endpoint `/users/track`](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) et à l'[endpoint `/subscription/status/set`](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).
2. Personnalisez le flux de travail avec des paramètres supplémentaires ou une logique conditionnelle pour répondre aux besoins de votre organisation.
3. Une fois la modification terminée, cliquez sur **Finish**, puis sur **Activate** pour activer le flux de travail.

{% alert note %}
Lorsque vous utilisez les flux de travail OneTrust pour mettre à jour les préférences des groupes d'abonnement dans Braze, le paramètre `subscription_group_id` doit correspondre à l'ID défini par Braze lors de la création du groupe d'abonnement. Vous pouvez accéder au `subscription_group_id` d'un groupe d'abonnement en naviguant vers la page **Subscription Group** dans le tableau de bord de Braze.
{% endalert %}

![]({% image_buster /assets/img/onetrust/onetrust6.png %})

{% endtab %}
{% tab User Deletion %}

1. Mettez à jour le corps de la requête pour y inclure toutes les valeurs dynamiques nécessaires. Assurez-vous que le corps de l'action correspond à l'[endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).
2. Une fois la modification terminée, sélectionnez **Finish** puis **Activate** pour activer le flux de travail.

![]({% image_buster /assets/img/onetrust/onetrust10.png %})

#### Mettre à jour le flux de travail pour les requêtes des personnes concernées {#update-the-data-subject-request-workflow}
1. Dans le menu **Privacy Rights Automation**, sélectionnez **Workflows**.
2. Sélectionnez le flux de travail que vous souhaitez mettre à jour avec l'intégration Braze.
3. Sélectionnez le bouton **Edit** pour activer la modification.
4. Ensuite, sélectionnez l'étape du flux de travail à laquelle ajouter l'intégration Braze et cliquez sur **Add Connection**.
5. Ajoutez le flux de travail Braze créé précédemment en tant que sous-tâche système.

{% endtab %}
{% endtabs %}

## Autres actions prises en charge {#other-supported-actions}

Outre les actions **POST User track - Attributes**, **POST Set Users Subscription Group Status** et **POST User Delete**, Braze prend en charge d'autres endpoints qui peuvent être utilisés pour créer des flux de travail personnalisés et servir de sous-tâches dans des flux de travail existants.

Pour consulter la liste complète des actions prises en charge :
1. Dans OneTrust, cliquez sur **Systems** dans votre menu **Integrations**.
2. Choisissez le système **Braze**.
3. Accédez à l'onglet **Actions**.

![]({% image_buster /assets/img/onetrust/onetrust7.png %})