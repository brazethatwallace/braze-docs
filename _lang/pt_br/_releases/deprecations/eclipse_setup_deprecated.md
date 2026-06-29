---
nav_title: Configuração inicial do SDK com o Eclipse
page_order: 1
page_type: update
noindex: true
description: "Este artigo arquivado descreve como realizar uma configuração inicial do SDK com o Eclipse. A Braze descontinuou o suporte ao Eclipse IDE."
---

# Configuração inicial do SDK com o Eclipse {#initial-sdk-setup-with-eclipse}

{% alert update %}
A Braze removeu o suporte ao Eclipse IDE devido ao [encerramento do suporte do Google ao plug-in Eclipse Android Developer Tools](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html). Se precisar de ajuda com a integração com o Eclipse antes da migração, [envie um e-mail para o Suporte]({{site.baseurl}}/support_contact/) para obter assistência.
{% endalert %}

## Etapa 1 {#step-1}
Na sua linha de comando, clone o [repositório GitHub da Braze para Android](https://github.com/braze-inc/braze-android-sdk).

```bash
$ git clone git@github.com:braze-inc/braze-android-sdk.git
```

## Etapa 2 {#step-2}
Importe o projeto Braze no seu espaço de trabalho local

No Eclipse:

  - Acesse File > Import.

    ![Importação de arquivo]({{site.baseurl}}/assets/img_archive/file_import.png)
  - Selecione Android > Existing Android Code into Workspace.

    ![Importação para Android]({{site.baseurl}}/assets/img_archive/android_import.png)
  - Clique em "Browse".

    ![Navegar]({{site.baseurl}}/assets/img_archive/click_browse.png)
  - Marque a pasta do projeto Braze UI e a opção "copy project into workspace" e clique em "Finish".

    ![Selecione o projeto Android UI]({{site.baseurl}}/assets/img_archive/select_project_android.png)

## Etapa 3 {#step-3}
Faça referência à Braze no seu próprio projeto.
No Eclipse:

  - Clique com o botão direito do mouse no seu projeto e selecione "Properties".

    ![Clique em Properties]({{site.baseurl}}/assets/img_archive/click_properties.png)
  - Em "Android", clique em "Add..." na seção Library e adicione android-sdk-ui como uma biblioteca ao seu app.

    ![Adicionar Braze]({{site.baseurl}}/assets/img_archive/add_appboy_ui.png)

## Etapa 4 {#step-4}
Resolva erros de dependência e corrija o alvo de compilação.

Nesse momento, você poderá ver erros no código da Braze, porque suas dependências não estão preenchidas e o alvo de compilação está possivelmente incorreto:

   - Clique com o botão direito do mouse no projeto Braze UI e selecione Properties->Android para garantir que o alvo de compilação esteja definido para a versão atual das ferramentas de compilação da Braze.

      ![Alvo de compilação]({{site.baseurl}}/assets/img_archive/build_target.png)
   - Clique com o botão direito do mouse no projeto Braze UI e selecione Properties->Java Build Path->Add JARs… e adicione 'android-support-v4.jar' do aplicativo principal como uma biblioteca.

      ![Suporte]({{site.baseurl}}/assets/img_archive/android_support_v4.png)

## Etapa 5 {#step-5}

Adicione os itens finais.

  - Para a versão 1.10.0 ou superior do SDK, você precisará adicionar
  `<service android:name="com.appboy.services.AppboyDataSyncService" />`
  ao seu AndroidManifest.xml, pois o Eclipse não oferece suporte à mesclagem de manifestos.

  - Para a versão 1.7.0 ou superior do SDK, você precisará copiar "assets/fontawesome-webfont.ttf" do nosso projeto de biblioteca para o seu aplicativo. O Eclipse não inclui automaticamente a pasta de ativos das bibliotecas.