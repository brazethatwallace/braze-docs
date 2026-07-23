---
nav_title: Gestion de la collecte de données
article_title: Gérer la collecte de données pour le SDK Braze
page_order: 8
description: "Découvrez comment gérer la collecte des données pour le SDK Braze."

---

# Gestion de la collecte de données {#manage-data-collection}

> Découvrez comment gérer la collecte des données pour le SDK Braze, afin de vous conformer à toute réglementation en matière de confidentialité des données, le cas échéant.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/analytics/managing_data_collection.md %}
{% endsdktab %}

{% sdktab android %}
## Questionnaire sur la protection de la vie privée dans Google Play {#privacy-questionnaire}

À partir d'avril 2022, les développeurs Android devront remplir le [formulaire de sécurité des données](https://support.google.com/googleplay/android-developer/answer/10787469) de Google Play pour divulguer leurs pratiques en matière de confidentialité et de sécurité. Ce guide fournit des instructions sur la façon de remplir ce nouveau formulaire avec des informations sur la manière dont Braze gère les données de votre application.

En tant que développeur d'applications, vous contrôlez les données que vous envoyez à Braze. Les données reçues par Braze sont traitées conformément à vos instructions. Google classifie ceci en tant que [fournisseur de services](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform).

{% alert important %}
Cet article fournit des informations relatives aux données traitées par le SDK Braze en lien avec la rubrique de sécurité du questionnaire Google. Cet article ne constitue pas un avis juridique ; nous vous recommandons donc de consulter votre équipe juridique avant de soumettre toute information à Google.
{% endalert %}

### Questions

| Questions | Réponses concernant le SDK Braze |
|---|---|
| Votre application collecte-t-elle ou partage-t-elle un des types de données utilisateur requis ? | Oui, le SDK Android de Braze collecte des données telles que configurées par le développeur de l'application. |
| Toutes les données utilisateur collectées par votre application sont-elles chiffrées en transit ? | Oui. |
| Offrez-vous aux utilisateurs un moyen de demander la suppression de leurs données ? | Oui. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Questions" }

Pour plus d'informations sur le traitement des demandes des utilisateurs concernant leurs données et leur suppression, consultez [Informations sur la conservation des données Braze]({{site.baseurl}}/api/data_retention).

### Collecte de données {#data-collection}

Les données collectées par Braze sont déterminées par votre intégration spécifique et les données utilisateur que vous choisissez de collecter. Pour en savoir plus sur les données collectées par défaut par Braze et sur la façon de désactiver certains attributs, consultez nos [options de collecte de données du SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection#minimum-integration).

<table aria-label="Collecte de données" id="datatypes">
    <thead>
        <tr>
            <th width="25%">Catégorie</th>
            <th width="25%">Type de données</th>
            <th width="50%">Utilisation par Braze</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">Localisation</td>
            <td>Localisation approximative</td>
            <td rowspan="15">Non collecté par défaut.</td>
        </tr>
        <tr>
            <td>Localisation précise</td>
        </tr>
        <tr>
            <td rowspan="9">Informations personnelles</td>
            <td>Nom</td>
        </tr>
        <tr>
            <td>Adresse e-mail</td>
        </tr>
        <tr>
            <td>ID utilisateur</td>
        </tr>
        <tr>
            <td>Adresse</td>
        </tr>
        <tr>
            <td>Numéro de téléphone</td>
        </tr>
        <tr>
            <td>Race et origine ethnique</td>
        </tr>
        <tr>
            <td>Convictions politiques ou religieuses</td>
        </tr>
        <tr>
            <td>Orientation sexuelle</td>
        </tr>
        <tr>
            <td>Autres informations</td>
        </tr>
        <tr>
            <td rowspan="4">Informations financières</td>
            <td>Informations de paiement de l'utilisateur</td>
        </tr>
        <tr>
            <td>Historique des achats</td>
        </tr>
        <tr>
            <td>Score de crédit</td>
        </tr>
        <tr>
            <td>Autres informations financières</td>
        </tr>
        <tr>
            <td rowspan="2">Santé et forme physique</td>
            <td>Informations de santé</td>
            <td rowspan="2">Non collecté par défaut.</td>
        </tr>
        <tr>
            <td>Informations de forme physique</td>
        </tr>
        <tr>
            <td rowspan="3">Messages</td>
            <td>E-mails</td>
            <td rowspan="2">Non collecté par défaut.</td>
        </tr>
        <tr>
            <td>SMS ou MMS</td>
        </tr>
        <tr>
            <td>Autres messages in-app</td>
            <td>Si vous envoyez des messages in-app ou des notifications push via Braze, nous collectons des informations sur le moment où les utilisateurs ont ouvert ou lu ces messages.</td>
        </tr>
        <tr>
            <td rowspan="2">Photos et vidéos</td>
            <td>Photos</td>
            <td rowspan="8">Non collecté.</td>
        </tr>
        <tr>
            <td>Vidéos</td>
        </tr>
        <tr>
            <td rowspan="3">Fichiers audio</td>
            <td>Enregistrements vocaux ou sonores</td>
        </tr>
        <tr>
            <td>Fichiers musicaux</td>
        </tr>
        <tr>
            <td>Autres fichiers audio</td>
        </tr>
        <tr>
            <td>Fichiers et documents</td>
            <td>Fichiers et documents</td>
        </tr>
        <tr>
            <td>Calendrier</td>
            <td>Événements du calendrier</td>
        </tr>
        <tr>
            <td>Contacts</td>
            <td>Contacts</td>
        </tr>
        <tr>
            <td rowspan="5">Activité de l'application</td>
            <td>Interactions avec l'application</td>
            <td>Braze collecte les données d'activité de session par défaut. Toutes les autres interactions et activités sont déterminées par l'intégration personnalisée de votre application.</td>
        </tr>
        <tr>
            <td>Historique de recherche dans l'application</td>
            <td>Non collecté.</td>
        </tr>
        <tr>
            <td>Applications installées</td>
            <td>Non collecté.</td>
        </tr>
        <tr>
            <td>Autre contenu généré par l'utilisateur</td>
            <td rowspan="2">Non collecté par défaut.</td>
        </tr>
        <tr>
            <td>Autres actions</td>
        </tr>
        <tr>
            <td>Navigation web</td>
            <td>Historique de navigation web</td>
            <td>Non collecté.</td>
        </tr>
        <tr>
            <td rowspan="3">Informations et performances de l'application</td>
            <td>Journaux de plantage</td>
            <td>Braze collecte les journaux de plantage pour les erreurs qui surviennent au sein du SDK. Ceux-ci contiennent le modèle de téléphone et le niveau d'OS de l'utilisateur, ainsi qu'un ID utilisateur spécifique à Braze.</td>
        </tr>
        <tr>
            <td>Diagnostics</td>
            <td>Non collecté.</td>
        </tr>
        <tr>
            <td>Autres données de performance de l'application</td>
            <td>Non collecté.</td>
        </tr>
        <tr>
            <td>Appareil ou autres identifiants</td>
            <td>Appareil ou autres identifiants</td>
            <td>Braze génère un ID d'appareil pour différencier les appareils des utilisateurs et vérifier que les messages sont envoyés à l'appareil prévu.</td>
        </tr>
    </tbody>
</table>

Pour en savoir plus sur les autres données d'appareil collectées par Braze qui peuvent ne pas relever du champ d'application des directives de sécurité des données de Google Play, consultez notre [aperçu du stockage Android]({{site.baseurl}}/developer_guide/storage/?tab=android) et nos [options de collecte de données du SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection#minimum-integration).

## Désactivation du suivi des données {#disabling-data-tracking}

Pour désactiver l'activité de suivi des données sur le SDK Android, utilisez la méthode [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html). Cela entraînera l'annulation de toutes les connexions réseau, ce qui signifie que le SDK Braze ne transmettra plus aucune donnée aux serveurs Braze.

## Effacer les données précédemment stockées {#wiping-previously-stored-data}

Vous pouvez utiliser la méthode [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) pour effacer complètement toutes les données côté client stockées sur l'appareil.

## Reprise du suivi des données {#resuming-data-tracking}

Pour reprendre la collecte de données, vous pouvez utiliser la méthode [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html). Gardez à l'esprit que cela ne restaure pas les données précédemment effacées.

{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/analytics/managing_data_collection.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/analytics/managing_data_collection.md %}
{% endsdktab %}

{% sdktab roku %}
{% multi_lang_include developer_guide/roku/analytics/managing_data_collection.md %}
{% endsdktab %}

{% endsdktabs %}