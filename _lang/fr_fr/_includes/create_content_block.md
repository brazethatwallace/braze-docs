{% if include.location == "dnd" %}

1. Accédez à **Modèles** > **Blocs de contenu**. Sélectionnez <i class="fas fa-plus"></i> **Créer un bloc de contenu**, puis sélectionnez **Bloc de contenu par glisser-déposer**.
2. Glissez-déposez les [blocs éditeur]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) pour créer un bloc de contenu par glisser-déposer. 
3. Glissez-déposez un bloc de format depuis l'onglet **Lignes** dans l'éditeur pour définir la disposition de votre bloc de contenu. <br><br> ![Compositeur de blocs de contenu par glisser-déposer.]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. Ajoutez des blocs de contenu par glisser-déposer selon vos besoins pour créer vos campagnes e-mail.
5. Une fois votre bloc de contenu créé, sélectionnez **Terminé**.
6. Donnez un nom à votre bloc de contenu. Ce nom sera automatiquement intégré à l'**étiquette Liquid du bloc de contenu**.
7. (Facultatif) Ajoutez une description.
8. Sélectionnez l'onglet **Prévisualisation** pour voir à quoi ressemblera votre bloc de contenu. Vous pouvez également sélectionner **Copier le lien de prévisualisation** pour générer et copier un lien de prévisualisation partageable montrant l'apparence de l'e-mail pour un utilisateur aléatoire. Ce lien reste valide pendant sept jours avant de devoir être régénéré.<br><br> ![Onglet Prévisualisation du compositeur de blocs de contenu par glisser-déposer.]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. Sélectionnez **Lancer le bloc de contenu**.

{% elsif include.location == "html" %}

1. Accédez à **Modèles** > **Blocs de contenu**. Sélectionnez <i class="fas fa-plus"></i> **Créer un bloc de contenu**, puis sélectionnez **Éditeur de code HTML**.
2. Saisissez votre HTML dans l'onglet **HTML**, ou créez votre bloc de contenu dans l'onglet **Classique**. <br><br> ![Compositeur de l'éditeur de code HTML.]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
3. Une fois votre bloc de contenu créé, sélectionnez **Terminé**.
4. Saisissez un nom pour votre bloc de contenu. Ce nom sera automatiquement intégré à l'**étiquette Liquid du bloc de contenu**.
5. (Facultatif) Ajoutez une description.
6. Sélectionnez l'onglet **Prévisualisation** pour voir à quoi ressemblera votre bloc de contenu. Vous pouvez également sélectionner **Copier le lien de prévisualisation** pour générer et copier un lien de prévisualisation partageable montrant l'apparence de l'e-mail pour un utilisateur aléatoire. Ce lien reste valide pendant sept jours avant de devoir être régénéré.<br><br> ![Onglet Prévisualisation du compositeur de l'éditeur de code HTML.]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
7. Sélectionnez **Lancer le bloc de contenu**.

{% endif %}