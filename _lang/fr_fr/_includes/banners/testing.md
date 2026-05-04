{% if include.page == "testing" %}Lors de la [rédaction de votre message bannière]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#compose-a-banner), sélectionnez{% elsif include.page == "campaigns" %}Sélectionnez{% endif %} **Prévisualisation** pour prévisualiser votre bannière ou envoyer un message test.

![Onglet Prévisualisation du composeur de bannière.]({% image_buster /assets/img/banners/select_preview.png %}){: style="max-width:50%;"}

Gardez à l'esprit que la prévisualisation peut différer du rendu final sur l'appareil d'un utilisateur en raison des différences matérielles.

Pour envoyer un message test, ajoutez un groupe de test de contenu ou un ou plusieurs utilisateurs individuels en tant que **destinataires du test**, puis sélectionnez **Envoyer le test**. Vous pourrez consulter votre message test sur l'appareil pendant 5 minutes maximum. Vous pouvez ensuite sélectionner **Copier le lien de prévisualisation** pour générer et copier un lien de prévisualisation partageable qui montre à quoi ressemblera la bannière pour un utilisateur aléatoire. Ce lien restera valide pendant sept jours avant de devoir être régénéré.

![Onglet Prévisualisation du composeur de bannière.]({% image_buster /assets/img/banners/preview_banner.png %})

Lors de la vérification de votre bannière test, assurez-vous des points suivants :

- Votre Campaign de bannière est-elle affectée à un emplacement ?
- Les images et les médias s'affichent-ils et fonctionnent-ils comme prévu sur les types d'appareils et les tailles d'écran ciblés ?
- Vos liens et boutons dirigent-ils l'utilisateur vers la bonne destination ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous prévu une valeur d'attribut par défaut dans le cas où le Liquid ne renvoie aucune information ?
- Votre texte est-il clair, concis et correct ?

Pour en savoir plus, consultez [Envoyer des messages test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/).