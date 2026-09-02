---
nav_title: Digioh
article_title: Digioh
description: "Este artigo de referência descreve a parceria entre a Braze e a Digioh, uma plataforma de pesquisa para a criação de pop-ups, formulários, pesquisas e centrais de preferências de comunicação que impulsionam o engajamento por meio das suas Campaigns na Braze."
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# Digioh

> A [Digioh](https://www.digioh.com/) oferece suporte ao crescimento da lista, à captura de dados primários e ao uso desses dados nas Campaigns da Braze.

_Essa integração é mantida pela Digioh._

## Sobre a integração {#about-the-integration}

A integração da Braze com a Digioh permite que você use um construtor do tipo arrastar e soltar para criar formulários, pop-ups, centrais de preferências, landing pages e pesquisas que conectem você aos seus clientes. A Digioh auxilia na configuração da integração e pode criar, projetar e lançar sua primeira campanha.

!["Crie centrais de preferências de e-mail e comunicações flexíveis com a Digioh"]({% image_buster /assets/img/digioh/pref_pop_examples.png %}){: style="border:0"}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Digioh | É necessário ter uma [conta da Digioh](https://www.digioh.com/) para usar essa parceria. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Endpoint da API or interface de programação do aplicativo (API) da Braze `/users/track/` | A URL do seu endpoint REST or transferir estado representacional com os detalhes de `/users/track/` anexados a ela. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/api/basics/#endpoints).<br><br>Por exemplo, se seu endpoint da API or interface de programação do aplicativo (API) REST or transferir estado representacional for `https://rest.iad-01.braze.com`, seu endpoint `/users/track/` será `https://rest.iad-01.braze.com/users/track/`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

Para integrar a Digioh, configure primeiro o conector da Braze. Quando terminar, você precisará aplicar a integração a uma lightbox (widget). Visite a [Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/) para saber mais sobre os conceitos básicos de integração.

### Etapa 1: Criar integração com a Digioh {#step-1-create-digioh-integration}

Na Digioh, clique na guia **Integrations** e, em seguida, no botão **New Integration**. Selecione **Braze** no menu suspenso **Integration** e nomeie a integração.

!["Selecione a integração correta no menu suspenso"]({% image_buster /assets/img/digioh/2.png %}){: style="max-width:50%;"}

Em seguida, insira a chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze e seu endpoint da API or interface de programação do aplicativo (API) da Braze `/users/track/`.

Por fim, use a seção de mapeamento de campos para mapear campos personalizados adicionais além do e-mail e do nome. O trecho de código a seguir mostra um exemplo de carga útil. Quando concluído, selecione **Create Integration**.

```json
{
    "attributes" : [
         {
           "external_id": "[EMAIL_MD5]",
           "email" : "[EMAIL]"
         }
     ]
}
```

### Etapa 2: Criar uma lightbox da Digioh {#step-2-create-a-digioh-lightbox}

Use o [editor de design](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) da Digioh para criar uma lightbox (widget). <br>
Quer ver uma galeria de maneiras de aproveitar o editor de design? Visite a [galeria de temas](https://www.digioh.com/theme-gallery) da Digioh.

### Etapa 3: Aplicar integração {#step-3-apply-integration}

Para aplicar essa integração a uma [lightbox](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) da Digioh, navegue até a página **Boxes** e selecione o link **Add** ou **Edit** na coluna **Integrations**. Isso também pode ser adicionado na seção **Integration** do editor.

!["Adicione a integração a uma lightbox"]({% image_buster /assets/img/digioh/3.png %}){: style="max-width:90%"}

Aqui, selecione **Add Integration**, escolha a integração desejada e clique em **Save**. A Digioh passará seus leads capturados para a Braze em tempo real.