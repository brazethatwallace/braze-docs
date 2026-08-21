---
nav_title: Formulaires multi-étapes
article_title: Formulaires multi-étapes pour pages de destination
page_order: 2
page_type: reference
description: "Découvrez comment créer un formulaire multi-étapes sur une page de destination Braze, gérer les étapes dans l'éditeur par glisser-déposer et personnaliser l'étape de confirmation intégrée."
---

# Formulaires multi-étapes pour pages de destination {#multi-step-landing-page-forms}

> Divisez un long formulaire de page de destination en plusieurs étapes, chacune avec ses propres champs, afin que les utilisateurs progressent dans votre formulaire une étape à la fois. Chaque formulaire multi-étapes inclut une étape de confirmation verrouillée, de sorte que les utilisateurs voient toujours une confirmation après avoir soumis le formulaire.

## Prérequis {#prerequisites}

Pour accéder au générateur de pages de destination, vous avez besoin de [certaines autorisations]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites). Si vous n'avez pas accès, demandez de l'aide à votre administrateur Braze.

Vous devez également être familiarisé avec les [blocs de formulaire des pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-3-customize-the-page).

## Fonctionnement des formulaires multi-étapes {#how-multi-step-forms-work}

Pour créer un formulaire multi-étapes, ajoutez une ligne **Form** depuis la section **Layout** du panneau **Build**. La ligne **Form** inclut des boutons d'action intégrés et la prise en charge multi-étapes, vous n'avez donc pas besoin d'assembler la structure de la ligne vous-même.

Vous ne pouvez ajouter qu'une seule ligne **Form** par page de destination. Lorsque vous la faites glisser sur votre page, elle commence avec une seule étape et une étape de confirmation verrouillée qui s'exécute après la soumission.

{% alert note %}
Étant donné que la ligne **Form** gère sa propre navigation multi-étapes, toutes vos étapes se trouvent dans cette unique ligne sur une seule page. Cela diffère de l'approche standard qui consiste à créer un formulaire à une seule étape et à lier son bouton **Submit** à une page de destination de confirmation séparée. Pour plus d'informations, consultez [Étape 4 : Créer une page de confirmation]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional).
{% endalert %}

![Un formulaire multi-étapes de page de destination dans le compositeur de pages de destination.]({% image_buster /assets/img/landing_pages/multi_step_form.png %})

## Ajouter un formulaire multi-étapes {#add-a-multi-step-form}

1. Dans l'éditeur de pages de destination, accédez au panneau **Build** et sélectionnez **Layout**.
2. Faites glisser la ligne **Form** dans votre page.
3. Avec la ligne **Form** sélectionnée, utilisez la section **Steps** dans le panneau de propriétés à droite pour construire votre formulaire :
   - Ajoutez des [blocs de formulaire]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-3-customize-the-page) (tels que **Email Capture**, **Phone Capture**, **Input Field**, **Dropdown**, **Checkbox** ou **Checkbox Group**) à **Step 1**.
   - Sélectionnez **Add step** pour créer des étapes supplémentaires, et ajoutez des blocs de formulaire à chacune d'entre elles.

Par exemple, un formulaire en trois étapes pourrait demander un nom à **Step 1**, un numéro de téléphone à **Step 2**, puis arriver à l'étape **Confirmation** pour remercier l'utilisateur d'avoir soumis le formulaire.

## Naviguer entre les étapes pendant l'édition {#navigate-between-steps-while-editing}

Déplacez-vous entre les étapes dans l'éditeur de deux manières :

| Méthode | Comment faire |
|---------|---------------|
| Navigateur d'étapes | Dans le canevas, utilisez le contrôle **Step X of Y** pour passer à l'étape précédente ou suivante. |
| Panneau des étapes | Sélectionnez la ligne **Form**, puis utilisez la section **Steps** dans le panneau de propriétés à droite pour accéder directement à une étape, y compris l'étape **Confirmation**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Naviguer entre les étapes pendant l'édition" }

## Gérer les étapes {#manage-steps}

Utilisez la section **Steps** dans le panneau de propriétés de la ligne **Form** pour ajouter, supprimer et réorganiser les étapes :

| Action | Comment faire |
|--------|---------------|
| Ajouter une étape | Sélectionnez **Add step**. Les nouvelles étapes sont ajoutées après vos étapes existantes et avant l'étape **Confirmation**. |
| Supprimer une étape | Sélectionnez l'icône de corbeille à côté de l'étape que vous souhaitez supprimer.<br><br>Notez que l'étape **Confirmation** n'a pas d'icône de corbeille et ne peut être ni supprimée ni réorganisée. Elle s'exécute toujours en dernier, après qu'un utilisateur a complété les étapes précédentes. |
| Réorganiser les étapes | Utilisez la poignée de glissement à côté d'une étape pour modifier son ordre. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gérer les étapes" }

## Personnaliser l'étape de confirmation {#customize-the-confirmation-step}

Chaque formulaire multi-étapes inclut une étape **Confirmation** répertoriée sous **After submission** dans la section **Steps**. Cette étape est verrouillée afin qu'elle ne puisse pas être supprimée, ce qui signifie que les utilisateurs voient toujours une expérience de confirmation après avoir soumis votre formulaire.

Bien que l'étape **Confirmation** ne puisse pas être supprimée, vous pouvez la personnaliser comme n'importe quelle autre étape : sélectionnez-la dans la section **Steps**, puis ajoutez et stylisez des blocs pour construire votre message de confirmation.

## Suivre les données des formulaires partiellement complétés {#track-data-from-partially-completed-forms}

Si un utilisateur quitte votre formulaire avant d'atteindre l'étape **Confirmation**, Braze enregistre tout de même les données des étapes qu'il a complétées dans son profil utilisateur. L'événement **Submitted a Landing Page form** n'est pas enregistré tant que l'utilisateur n'a pas complété toutes les étapes et atteint l'étape **Confirmation**.

{% alert note %}
Le [reciblage et la distribution déclenchée]({{site.baseurl}}/user_guide/messaging/landing_pages/retargeting_users) reposent sur l'événement **Submitted a Landing Page form**. Un utilisateur qui soumet certaines étapes mais pas toutes est enregistré dans son profil, mais n'est pas inclus dans cet événement, même si ses données partielles ont été capturées.
{% endalert %}

Cela diffère des [sondages de pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys), où un utilisateur qui n'atteint pas la dernière étape est suivi comme une soumission partielle.

## Limitations et considérations {#limitations-and-considerations}

- Une page de destination prend en charge une seule ligne **Form**, de sorte que toutes vos étapes et votre étape de confirmation se trouvent dans cette unique ligne.
- Vous pouvez ajouter jusqu'à 10 étapes de collecte de données. L'étape **Confirmation** n'est pas comptabilisée dans cette limite.
- Chaque étape inclut un bouton par défaut dont le clic est configuré pour passer à l'étape suivante. Cette action valide et enregistre les saisies de l'étape en cours ; à la dernière étape de collecte de données, elle enregistre également l'événement **Submitted a Landing Page form** et passe à l'étape **Confirmation**. Si une étape n'est pas connectée, ajoutez un comportement au clic pour que le bouton passe à l'étape suivante. Pour plus d'informations, consultez [Button]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=landing%20pages) dans les blocs éditeur.
- Vous n'avez pas besoin de créer ou de lier une deuxième page de destination pour servir d'expérience de confirmation, car l'étape **Confirmation** est intégrée dans la ligne **Form**.
- Si vous ne voyez pas la ligne **Form** sous **Layout**, contactez votre gestionnaire de compte Braze.