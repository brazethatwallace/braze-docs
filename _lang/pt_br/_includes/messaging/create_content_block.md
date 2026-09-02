{% if include.location == "dnd" %}

1. Acesse **Content** > **Content Block**. Selecione <i class="fas fa-plus"></i> **Create Content Block** e selecione **Drag-and-drop Content Block**.
2. Arraste e solte os [blocos do editor]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/dnd_editor_blocks) para construir um Content Block de arrastar e soltar.
3. Arraste e solte um bloco de formato da guia **Rows** no editor para criar o layout do seu Content Block. <br><br> ![Criador de Content Blocks de arrastar e soltar.]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. Adicione Content Blocks de arrastar e soltar conforme necessário para construir suas campanhas de e-mail.
5. Depois de criar seu Content Block, selecione **Done**.
6. Dê um nome ao seu Content Block. Esse nome será preenchido automaticamente como parte da **Content Block Liquid Tag**.
7. (Opcional) Adicione uma descrição.
8. Selecione a guia **prévia** para ver como seu Content Block aparecerá. Opcionalmente, selecione **Copy prévia link** para gerar e copiar um link de prévia compartilhável que mostra como o e-mail ficará para um usuário aleatório. O link terá validade de sete dias antes de precisar ser gerado novamente.<br><br> ![Guia de prévia do criador de Content Blocks de arrastar e soltar.]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. Selecione **Launch Content Block**.

{% elsif include.location == "html" %}

1. Acesse **Content** > **Content Block**. Selecione <i class="fas fa-plus"></i> **Create Content Block** e selecione **HTML code editor**.
2. Insira seu HTML na guia **HTML** ou construa seu Content Block na guia **Classic**. <br><br> ![Criador do editor de código HTML.]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
3. Depois de criar seu Content Block, selecione **Done**.
4. Digite um nome para o seu Content Block. Esse nome será preenchido automaticamente como parte da **Content Block Liquid Tag**.
5. (Opcional) Adicione uma descrição.
6. Selecione a guia **prévia** para ver como seu Content Block aparecerá. Opcionalmente, selecione **Copy prévia link** para gerar e copiar um link de prévia compartilhável que mostra como o e-mail ficará para um usuário aleatório. O link terá validade de sete dias antes de precisar ser gerado novamente.<br><br> ![Guia de prévia do criador do editor de código HTML.]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
7. Selecione **Launch Content Block**.

{% endif %}