---
nav_title: "Email Love"
article_title: "Email Love"
description: "Aprenda a integrar a Braze com o Email Love, um plugin do Figma que permite projetar e exportar e-mails HTML responsivos e acessíveis diretamente do Figma."
alias: /partners/email_love/
page_type: partner
search_tag: Partner

---

# Email Love

> [Email Love](https://emaillove.com/) é um plugin do Figma que permite projetar e exportar e-mails HTML responsivos e acessíveis diretamente do Figma. O recurso Exportar para a Braze do Email Love utiliza a API da Braze para fazer upload dos seus modelos de e-mail para a Braze de forma integrada.

## Pré-requisitos {#prerequisites}

| Requisito            | Descrição                                                      |
|------------------------|------------------------------------------------------------------|
| **Conta do Email Love** | Uma conta do Email Love é necessária para aproveitar esta parceria. |
| **Chave da API REST da Braze** | Uma chave da API REST da Braze com permissão total de `Templates` ativada. Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Usando o Email Love com a Braze {#using-email-love-with-braze}

### Etapa 1: Execute o plugin {#step-1-run-the-plugin}

Para projetar seu modelo de e-mail, você precisará primeiro carregar o plugin. Para instruções mais detalhadas, consulte a documentação do Email Love para [fazer upload do seu e-mail para a Braze](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm).

### Etapa 2: Crie seu primeiro quadro {#step-2-create-your-first-frame}

No plugin, selecione o botão **[+ No Template Selected]** para criar um novo quadro para o design do seu e-mail.

### Etapa 3: Projete o modelo com os componentes pré-construídos do Email Love {#step-3-design-the-template-with-email-loves-pre-built-components}

Selecione o quadro que você criou e comece a adicionar componentes (cabeçalhos, blocos de conteúdo, CTAs e rodapés) da biblioteca de **Assets** do plugin para estruturar seu e-mail.

![Componentes pré-construídos do Email Love.]({% image_buster /assets/img/email_love/emaillove1_content.png %})

### Etapa 4: Personalize os componentes {#step-4-customize-the-components}

Modifique os componentes usando as ferramentas do Figma para ajustar texto, imagens, cores e elementos de layout, alinhando o design do modelo com a sua marca. Se você adicionar um componente de rodapé, um link de cancelamento de inscrição da Braze será incluído automaticamente na exportação.

![Personalize componentes no Figma.]({% image_buster /assets/img/email_love/emaillove2_components.png %})

### Etapa 5: Exporte seu modelo de e-mail para a Braze {#step-5-export-your-email-template-to-braze}

1. Quando terminar, selecione o quadro que deseja exportar. Observe que você precisará usar um rodapé do Email Love que contenha um link de cancelamento de inscrição para que a exportação funcione.
2. Selecione o botão **Export** no plugin e selecione **Braze** no menu suspenso.
3. Copie e cole sua chave de API na caixa **Braze API Key** dentro do plugin Email Love para Figma.
4. Selecione o botão **Set API Key**.
5. Selecione **Change Instance ID** e, em seguida, selecione o ID da sua instância da Braze.

![Exportando um modelo para a Braze a partir do plugin Email Love.]({% image_buster /assets/img/email_love/emaillove3_exportbraze.png %}){: style="max-width:50%;"}

### Etapa 6: Edite seu e-mail na Braze {#step-6-edit-your-email-in-braze}

Na Braze, acesse **Modelos** > **Editar Modelos** > **Editar Mensagem**. Dentro do editor de modelos, você pode editar o HTML do seu e-mail ou usar o **editor de rich text** na guia **Classic**.

## Suporte e solução de problemas {#support-and-troubleshooting}

Para instruções mais detalhadas, consulte a documentação do Email Love sobre [exportar um design de e-mail](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm). Para suporte adicional, entre em contato com a equipe de suporte do Email Love.