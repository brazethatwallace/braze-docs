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

Pour accéder au générateur de pages de destination, vous devez disposer de [certaines autorisations]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites). Si vous n'avez pas accès, demandez de l'aide à votre administrateur Braze.

Vous devriez également vous familiariser avec les [blocs de formulaire de page de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-3-customize-the-page).

## Fonctionnement des formulaires multi-étapes {#how-multi-step-forms-work}

Pour créer un formulaire multi-étapes, ajoutez une ligne **Formulaire** depuis la section **Disposition** du panneau **Créer**. La ligne **Formulaire** inclut des boutons d'action intégrés et la prise en charge du multi-étapes, vous n'avez donc pas besoin d'assembler la structure de la ligne vous-même.

Vous ne pouvez ajouter qu'une seule ligne **Formulaire** par page de destination. Lorsque vous la glissez sur votre page, elle commence avec une seule étape et une étape de confirmation verrouillée qui s'exécute après la soumission.

{% alert note %}
Étant donné que la ligne **Formulaire** gère sa propre navigation multi-étapes, toutes vos étapes se trouvent dans cette seule ligne sur une même page. Cela diffère de l'approche standard consistant à créer un formulaire à étape unique et à lier son bouton **Soumettre** à une page de destination de confirmation distincte. Pour en savoir plus, consultez [Étape 4 : Créer une page de confirmation]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional).
{% endalert %}

![Un formulaire multi-étapes de page de destination dans le compositeur de pages de destination.]({% image_buster /assets/img/landing_pages/multi_step_form.png %})

## Ajouter un formulaire à plusieurs étapes {#add-a-multi-step-form}

1. Dans l'éditeur de page de destination, accédez au panneau **Build** et sélectionnez **Layout**.
2. Faites glisser la ligne **Form** dans votre page.
3. Avec la ligne **Form** sélectionnée, utilisez la section **Steps** dans le panneau de propriétés sur le côté droit pour construire votre formulaire :
   - Ajoutez des [blocs de formulaire]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-3-customize-the-page) (tels que **Email Capture**, **Phone Capture**, **Input Field**, **Dropdown**, **Checkbox** ou **Checkbox Group**) à **Step 1**.
   - Sélectionnez **Add step** pour créer des étapes supplémentaires, et ajoutez des blocs de formulaire à chacune d'entre elles.

Par exemple, un formulaire en trois étapes pourrait demander un nom à **Step 1**, un numéro de téléphone à **Step 2**, puis aboutir à l'étape **Confirmation** pour remercier l'utilisateur d'avoir soumis le formulaire.

## Naviguer entre les étapes pendant la modification {#navigate-between-steps-while-editing}

Passez d'une étape à l'autre dans l'éditeur de deux façons :

| Méthode | Comment faire |
|---------|---------------|
| Navigateur d'étapes | Dans le canvas, utilisez le contrôle **Étape X sur Y** pour passer à l'étape précédente ou suivante. |
| Panneau des étapes | Sélectionnez la ligne **Form**, puis utilisez la section **Steps** dans le panneau de propriétés sur le côté droit pour accéder directement à une étape, y compris l'étape **Confirmation**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Naviguer entre les étapes pendant la modification" }

## Gérer les étapes {#manage-steps}

Utilisez la section **Steps** dans le panneau de propriétés de la ligne **Form** pour ajouter, supprimer et réorganiser les étapes :

| Action | Comment faire |
|--------|--------|
| Ajouter une étape | Sélectionnez **Add step**. Les nouvelles étapes sont ajoutées après vos étapes existantes et avant l'étape **Confirmation**. |
| Supprimer une étape | Sélectionnez l'icône de corbeille à côté de l'étape que vous souhaitez supprimer.<br><br>Notez que l'étape **Confirmation** ne dispose pas d'icône de corbeille et ne peut être ni supprimée ni réorganisée. Elle s'exécute toujours en dernier, après qu'un utilisateur a complété les étapes précédentes. |
| Réorganiser les étapes | Utilisez la poignée de glissement à côté d'une étape pour modifier son ordre. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gérer les étapes" }

## Personnaliser l'étape de confirmation {#customize-the-confirmation-step}

Chaque formulaire à plusieurs étapes comprend une étape **Confirmation** répertoriée sous **After submission** dans la section **Steps**. Cette étape est verrouillée et ne peut pas être supprimée, ce qui signifie que les utilisateurs voient toujours une expérience de confirmation après avoir soumis votre formulaire.

Bien que l'étape **Confirmation** ne puisse pas être supprimée, vous pouvez la personnaliser comme n'importe quelle autre étape : sélectionnez-la dans la section **Steps**, puis ajoutez et stylisez des blocs pour créer votre message de confirmation.

## Personnaliser le style du bloc de formulaire {#style-the-form-block}

Avec la ligne **Form** sélectionnée, utilisez la section **Styles** dans le panneau **Multi-step form** pour personnaliser le conteneur du formulaire :

| Contrôle | Description |
|---|---|
| Image d'arrière-plan | Ajoutez une image derrière le formulaire. Vous pouvez également ajuster la taille, la position et les paramètres de répétition de l'image. |
| Couleur d'arrière-plan | Définissez la couleur d'arrière-plan du conteneur du formulaire. |
| Style de bordure | Choisissez une bordure pleine, en tirets ou en pointillés pour le conteneur du formulaire. |
| Couleur de bordure | Définissez la couleur de bordure du conteneur du formulaire. |
| Rayon de bordure | Arrondissez les coins du conteneur du formulaire. |
| Marge intérieure | Ajustez l'espace entre le bord du conteneur du formulaire et son contenu. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Contrôles de style du formulaire multi-étapes" }

Ces styles s'appliquent au conteneur du formulaire pour toutes les étapes, y compris l'étape **Confirmation**.

## Suivre les données des formulaires partiellement remplis {#track-data-from-partially-completed-forms}

Si un utilisateur quitte votre formulaire avant d'atteindre l'étape **Confirmation**, Braze enregistre tout de même les données des étapes qu'il a complétées dans son profil utilisateur. L'événement **Submitted a Landing Page form** n'est pas journalisé tant que l'utilisateur n'a pas terminé toutes les étapes et atteint l'étape **Confirmation**.

{% alert note %}
Le [reciblage et la distribution déclenchée]({{site.baseurl}}/user_guide/messaging/landing_pages/retargeting_users) reposent sur l'événement **Submitted a Landing Page form**. Un utilisateur qui soumet certaines étapes, mais pas toutes, voit ses données enregistrées dans son profil, mais n'est pas inclus dans cet événement, même si ses données partielles ont été capturées.
{% endalert %}

Ce fonctionnement diffère des [sondages sur les pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys), où un utilisateur qui n'atteint pas la dernière étape est suivi en tant que soumission partielle.

## Limitations et considérations {#limitations-and-considerations}

- Une page de destination prend en charge une seule ligne **Formulaire**, de sorte que toutes vos étapes et votre étape de confirmation se trouvent dans cette unique ligne.
- Vous pouvez ajouter jusqu'à 10 étapes de collecte de données. L'étape **Confirmation** n'est pas comptabilisée dans cette limite.
- Chaque étape inclut un bouton par défaut dont le clic est configuré pour passer à l'étape suivante. Cette action valide et enregistre les entrées de l'étape en cours ; lors de la dernière étape de collecte de données, elle enregistre également l'événement **Submitted a Landing Page form** et passe à l'étape **Confirmation**. Si une étape n'est pas connectée, ajoutez un comportement au clic pour que le bouton passe à l'étape suivante. Pour plus d'informations, consultez [Bouton]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=landing%20pages) dans Blocs éditeur.
- Vous n'avez pas besoin de créer ou de lier une seconde page de destination pour servir d'expérience de confirmation, car l'étape **Confirmation** est intégrée à la ligne **Formulaire**.
- Si vous ne voyez pas la ligne **Formulaire** sous **Disposition**, contactez votre gestionnaire de compte Braze.