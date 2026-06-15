{% if include.location == "dnd" %}

1. Acesse **Conteúdo** > **Content Block**. Selecione <i class="fas fa-plus"></i> **Create Content Block** e selecione **Drag-and-drop Content Block**.
2. Arraste e solte os [blocos do editor]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) para construir um bloco de conteúdo de arrastar e soltar.
3. Arraste e solte um bloco de formato da guia **Rows** no editor para criar a disposição do seu bloco de conteúdo. <br><br> ![Criador de blocos de conteúdo de arrastar e soltar.]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. Adicione blocos de conteúdo de arrastar e soltar conforme necessário para criar suas campanhas de e-mail.
5. Depois de criar seu bloco de conteúdo, selecione **Done**.
6. Dê um nome ao seu bloco de conteúdo. Esse nome será preenchido automaticamente como parte da **Content Block Liquid Tag**.
7. (Opcional) Adicione uma descrição.
8. Selecione a guia **Preview** para ver como seu bloco de conteúdo aparecerá. Opcionalmente, selecione **Copy preview link** para gerar e copiar um link de pré-visualização compartilhável que mostra como o e-mail ficará para um usuário aleatório. O link terá validade de sete dias antes de precisar ser gerado novamente.<br><br> ![Guia de pré-visualização do criador de blocos de conteúdo de arrastar e soltar.]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. Selecione **Launch Content Block**.

{% elsif include.location == "html" %}

1. Acesse **Conteúdo** > **Content Block**. Selecione <i class="fas fa-plus"></i> **Create Content Block** e selecione **HTML code editor**.
2. Insira seu HTML na guia **HTML** ou construa seu bloco de conteúdo na guia **Classic**. <br><br> ![Criador do editor de código HTML.]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
3. Depois de criar seu bloco de conteúdo, selecione **Done**.
4. Digite um nome para o seu bloco de conteúdo. Esse nome será preenchido automaticamente como parte da **Content Block Liquid Tag**.
5. (Opcional) Adicione uma descrição.
6. Selecione a guia **Preview** para ver como seu bloco de conteúdo aparecerá. Opcionalmente, selecione **Copy preview link** para gerar e copiar um link de pré-visualização compartilhável que mostra como o e-mail ficará para um usuário aleatório. O link terá validade de sete dias antes de precisar ser gerado novamente.<br><br> ![Guia de pré-visualização do criador do editor de código HTML.]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
7. Selecione **Launch Content Block**.

{% endif %}