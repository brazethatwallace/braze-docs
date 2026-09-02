---
nav_title: Optimizely
article_title: Optimizely
page_order: 2
description: "Cet article de référence présente le partenariat entre Braze et Optimizely qui vous permet de synchroniser vos Segments, événements et événements Currents de Braze vers Optimizely Data Platform."
alias: /partners/optimizely/
page_type: partner
search_tag: Partner
---

# Optimizely

> [Optimizely](https://www.optimizely.com/) est une plateforme d'expérience numérique de premier plan qui propose des outils d'expérimentation et de gestion de contenu pour les produits numériques et les campagnes marketing.

L'intégration entre Braze et Optimizely est une intégration bidirectionnelle qui vous permet de :

{% multi_lang_include partners/ab_testing/optimizely_integration_bullets.md %}

## Prérequis {#prerequisites}

| Condition                        | Description |
|----------------------------------|-------------|
| Compte Optimizely Data Platform  | Un compte Optimizely Data Platform (ODP) est requis pour tirer parti de ce partenariat. |
| Clé API REST Braze               | Une clé API REST Braze avec les permissions suivantes : `users.track`, `users.export.segments`, `segments.list`, `campaigns.trigger.send` et `canvas.trigger.send`. |
| Currents                         | Pour exporter des données vers Optimizely, vous devez avoir configuré Braze Currents pour votre compte. |
| URL et jeton Optimizely          | Vous pouvez les obtenir en accédant à votre tableau de bord Optimizely et en copiant l'URL d'ingestion et le jeton. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Configurer l'intégration {#step-1-configure-the-integration}

1. Dans le **App Directory** d'Optimizely Data Platform (ODP), sélectionnez l'application **Braze**, puis sélectionnez **Install App**.
2. Accédez à l'onglet **Settings**. Dans la section **Authorization**, procédez comme suit :
    1. Saisissez la **clé API REST** de Braze.
    2. Sélectionnez votre **URL d'instance** Braze.
    2. Sélectionnez **Verify API Key**.
3. Dans Braze, accédez à **[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents)**.
4. Sélectionnez **Create New Current** > **Custom Currents Export**.
5. Configurez le Current à l'aide de l'endpoint et du jeton fournis dans ODP. Cette étape est nécessaire pour synchroniser les événements Braze vers ODP.

![Autorisation Optimizely.]({% image_buster /assets/img/optimizely/image1_authorization.png %})

{:start="6"}
6. Dans ODP, développez la section **Segments** et sélectionnez des segments spécifiques dans la liste **Segments to Sync**, ou sélectionnez **Import All Customers** pour synchroniser tous les segments.
7. Ajoutez les [mappages de champs supplémentaires](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/29918568615949-Integrate-Braze%23h_01J6Z1P53JVDBFZ758Q78CK1QB&sa=D&source=editors&ust=1733948158380300&usg=AOvVaw3WSAND5ie3LCVuSxUlLanR) souhaités entre Braze et ODP.
8. Sélectionnez **Save**.

![Synchronisation de segments Braze dans Optimizely.]({% image_buster /assets/img/optimizely/image2_syncsegment.png %})

{% alert tip %}
Vous devez sélectionner des segments pour importer les profils clients Braze. Si vous ne sélectionnez aucun segment, l'intégration n'importera aucun profil client.
{% endalert %}

### Étape 2 : Mapper les champs de données {#step-2-map-data-fields}

L'intégration dispose de mappages de champs de données par défaut entre Braze et ODP. Par exemple, le champ **Email** dans Braze est mappé au champ **Last Seen Email** dans ODP.

![Mappage des champs de segments entre Optimizely et Braze.]({% image_buster /assets/img/optimizely/image3_emailmapfield.png %})

#### Mapper des champs supplémentaires (facultatif) {#map-additional-fields-optional}

Si vous souhaitez mapper des champs de données supplémentaires de Braze vers ODP, procédez comme suit dans ODP :

1. Dans la section **Segments** de l'application, sélectionnez le champ Braze dans la liste déroulante **Braze User Data Fields**.
2. Sélectionnez le champ ODP dans la liste déroulante **ODP Customer Fields**.
3. Sélectionnez **Save Field Map**.

![Enregistrement du mappage des champs de segments Braze dans Optimizely.]({% image_buster /assets/img/optimizely/image4_mapfields.png %})

#### Supprimer les mappages de champs non requis (facultatif) {#delete-non-required-field-mappings-optional}

Vous pouvez également supprimer les mappages de champs de données qui ne sont pas nécessaires. Procédez comme suit dans ODP :

1. Dans la section **Segments** de l'application, sélectionnez le mappage de champ que vous souhaitez supprimer dans la liste déroulante **Field Map**.
2. Sélectionnez **Delete Field Map**.

![Suppression du mappage des champs de segments Braze dans Optimizely.]({% image_buster /assets/img/optimizely/image5_deletephonefield.png %})

### Étape 3 : Synchroniser les données d'Optimizely Data Platform (ODP) vers Braze {#step-3-sync-data-from-optimizely-data-platform-odp-to-braze}

Après avoir configuré l'intégration, vous pouvez mettre en place une activation dans ODP pour synchroniser vos données clients ODP vers Braze.

1. Accédez à **Activation** > **Engage** et sélectionnez **Create New Campaign**.
2. Sélectionnez **Behavioral** pour configurer une synchronisation automatisée et récurrente.
3. Sélectionnez **Create From Scratch**, puis saisissez un nom pour votre activation qui représente les données que vous synchronisez vers Braze (par exemple **Braze Data Sync**).
4. Dans la section **Enrollment**, vous pouvez synchroniser les données des clients correspondant à un segment ou synchroniser les données des clients qui déclenchent un événement (par exemple lorsqu'ODP enregistre qu'un client ouvre un e-mail) :
   - **Clients correspondant à un segment :** Sélectionnez le segment souhaité, puis sélectionnez **Next**.<br><br>![Sélection de segment dans Optimizely.]({% image_buster /assets/img/optimizely/image6_segment.png %})
   - **Clients qui déclenchent un événement :** Développez la liste déroulante **Filter** et sélectionnez l'événement ODP à utiliser comme déclencheur pour cette synchronisation de données vers Braze. Ensuite, développez **Automation Rules** et ajustez selon vos besoins. <br><br>![Événement déclencheur dans Optimizely.]({% image_buster /assets/img/optimizely/image7_trigger.png %})
5. Développez **Touchpoints**, sélectionnez pour modifier **Touchpoint 1**, puis sélectionnez **Braze**.
6. Développez la section **Targeting**, puis sélectionnez le **Target Identifier**.
7. Sélectionnez l'une des options suivantes pour **Add Users To** dans la section **Configure** :
    - **Campaign :** Ajoutez des clients à une Campaign spécifique dans Braze. Après avoir choisi cette option, vous devez sélectionner la Campaign Braze.
    - **Canvas :** Ajoutez des clients à un Canvas spécifique dans Braze. Après avoir choisi cette option, vous devez sélectionner le Canvas Braze.
    - **Profile Update Only :** Mettez à jour uniquement le profil client Braze.
8. (Facultatif) Sélectionnez le **Number of Additional Fields** que vous souhaitez synchroniser vers Braze (jusqu'à 20).
    Ensuite, sélectionnez les éléments suivants pour chaque liste déroulante et champ de saisie de champ supplémentaire :
    - Dans chaque liste déroulante **Field #**, sélectionnez le champ Braze que vous souhaitez renseigner.
    - Dans chaque champ **Field # Value** correspondant, saisissez le champ ODP que vous souhaitez envoyer au champ Braze sélectionné. Par exemple, si vous avez sélectionné **Company Name** dans la liste déroulante **Field #**, saisissez `{{customer.company_name}}` pour le **Field # Value** correspondant.
9. Sélectionnez **Save**, puis sélectionnez le nom de votre activation dans le fil d'Ariane.
10. Sélectionnez **Select start time and schedule** dans la section **Touchpoints** si vous avez sélectionné **Customers that match a segment** pour l'inscription.
11. Complétez les paramètres suivants :
    - **Recurring or Continuous :** Sélectionnez **Recurring**.
    - **Start Date :** Saisissez la date à laquelle vous souhaitez envoyer les données à Braze.
    - **End :** La valeur par défaut est **Never**. Si vous souhaitez mettre fin à la synchronisation des données Braze à une date spécifique, définissez-la ici.
    - **Repeats :** Définissez sur **Daily**.
    - **Repeat Every :** Définissez sur **1 day**.
    - **Timing :** Saisissez l'heure à laquelle vous souhaitez envoyer les données à Braze.
    - **Time Zone :** Sélectionnez le fuseau horaire dans lequel vous souhaitez envoyer ces données.
12. Sélectionnez **Apply**, **Save**, puis **Go en direct or en ligne/en production/instantané**. Votre synchronisation démarre à la date et à l'heure de début désignées (ou lorsque l'événement déclencheur se produit).

## Résolution des problèmes {#troubleshooting}

### Inspecter les événements {#inspect-events}

Pour vérifier que les données se synchronisent correctement d'ODP vers Braze, vous pouvez inspecter les événements dans ODP.

1. Dans ODP, accédez à **Account Settings** > **Event Inspector**.
2. Sélectionnez **Start Inspector**.
3. Lorsque des données sont disponibles dans l'inspecteur, un nombre s'affiche à côté de **Refresh**. Sélectionnez-le pour afficher les données.
4. Les données brutes qu'ODP et Braze s'échangent s'affichent. Sélectionnez **View Details** pour voir la version formatée de ces données brutes.
5. Les champs de données envoyés de Braze vers ODP commencent par `_braze`.

### Vérifier les journaux d'activité {#check-activity-logs}

Chaque synchronisation de données est également enregistrée dans le [journal d'activité ODP](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/4407268804365-Use-the-Activity-Log&sa=D&source=editors&ust=1733948158385124&usg=AOvVaw2tMOxzcTKfL0-oYLT4IMpP) :

1. Accédez à **Account Settings** > **Activity Log**.
2. Filtrez les catégories par **braze**.
3. Sélectionnez **View Details** pour une vue formatée des détails du journal, y compris le nombre de correspondances.