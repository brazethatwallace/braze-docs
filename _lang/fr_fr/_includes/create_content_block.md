{% if include.location == "dnd" %}

1. Accédez à **Contenu** > **Content Block**. Sélectionnez <i class="fas fa-plus"></i> **Create Content Block**, puis sélectionnez **Drag-and-drop Content Block**.
2. Glissez-déposez les [blocs éditeur]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) pour créer un Content Block par glisser-déposer.
3. Glissez-déposez un bloc de format depuis l'onglet **Rows** dans l'éditeur pour définir la disposition de votre Content Block. <br><br> ![Compositeur de Content Block par glisser-déposer.]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. Ajoutez des Content Blocks par glisser-déposer selon vos besoins pour construire vos campagnes e-mail.
5. Une fois votre Content Block créé, sélectionnez **Done**.
6. Donnez un nom à votre Content Block. Ce nom sera automatiquement intégré à l'**étiquette Liquid du Content Block**.
7. (Facultatif) Ajoutez une description.
8. Sélectionnez l'onglet **Preview** pour voir à quoi ressemblera votre Content Block. Vous pouvez également sélectionner **Copy preview link** pour générer et copier un lien de prévisualisation partageable montrant l'apparence de l'e-mail pour un utilisateur aléatoire. Ce lien reste valide pendant sept jours avant de devoir être régénéré.<br><br> ![Onglet Preview du compositeur de Content Block par glisser-déposer.]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. Sélectionnez **Launch Content Block**.

{% elsif include.location == "html" %}

1. Accédez à **Contenu** > **Content Block**. Sélectionnez <i class="fas fa-plus"></i> **Create Content Block**, puis sélectionnez **HTML code editor**.
2. Saisissez votre HTML dans l'onglet **HTML**, ou créez votre Content Block dans l'onglet **Classic**. <br><br> ![Compositeur de l'éditeur de code HTML.]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
3. Une fois votre Content Block créé, sélectionnez **Done**.
4. Saisissez un nom pour votre Content Block. Ce nom sera automatiquement intégré à l'**étiquette Liquid du Content Block**.
5. (Facultatif) Ajoutez une description.
6. Sélectionnez l'onglet **Preview** pour voir à quoi ressemblera votre Content Block. Vous pouvez également sélectionner **Copy preview link** pour générer et copier un lien de prévisualisation partageable montrant l'apparence de l'e-mail pour un utilisateur aléatoire. Ce lien reste valide pendant sept jours avant de devoir être régénéré.<br><br> ![Onglet Preview du compositeur de l'éditeur de code HTML.]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
7. Sélectionnez **Launch Content Block**.

{% endif %}