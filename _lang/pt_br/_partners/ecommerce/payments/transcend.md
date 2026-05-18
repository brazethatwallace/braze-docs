---
nav_title: Transcend
article_title: Transcend
description: "Este artigo de referência descreve a parceria entre a Braze e a Transcend, uma plataforma de infraestrutura de privacidade de dados, que ajuda os usuários da Braze a automatizar o atendimento de solicitações de titulares de dados."
alias: /partners/transcend/
page_type: partner
search_tag: Partner

---

# Transcend

> A Transcend é uma empresa de infraestrutura de privacidade de dados que simplifica o processo para que as empresas forneçam aos usuários o controle sobre seus dados, atendendo automaticamente às solicitações dos titulares dos dados dentro das empresas em todos os seus sistemas de dados e fornecedores.

_Essa integração é mantida pela Transcend._

## Sobre a integração {#about-the-integration}

A parceria entre Braze e Transcend ajuda os usuários a automatizar solicitações de privacidade orquestrando dados em dezenas de sistemas de dados, ajudando as equipes a cumprir regulamentos como GDPR e CCPA. A Transcend fornece aos usuários finais um painel de controle, ou centro de privacidade, hospedado em `privacy.\<company\>.com`, onde é possível gerenciar preferências de privacidade, exportar dados ou excluí-los.

## Pré-requisitos {#prerequisites}

| Requisitos | Descrição |
|---|---|
| Conta Transcend | É necessário ter uma conta [Transcend](https://app.transcend.io/) com privilégios de administrador para aproveitar essa parceria. |
| Chave de API da Braze | Uma chave da API REST da Braze com as permissões `users.delete, users.alias.new, users.export.ids, email.unsubscribe,` e `email.blacklist`.<br><br>Isso pode ser criado no dashboard da Braze em **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

A Transcend permite acessar, excluir e recusar de forma programática a comunicação dos usuários na plataforma da Braze, de acordo com os regulamentos de privacidade de dados.

### Etapa 1: Configurar a integração da Braze {#step-1-set-up-the-braze-integration}
Para começar, faça login na [Transcend](https://app.transcend.io/login).
1. Navegue até **Data Map > Add Data Silo > Braze** e selecione o botão **Connect**.<br><br>
2. Quando sua conta for provisionada, você fará login em um dos URLs correspondentes: `https://dashboard-01.braze.com`, `https://dashboard-02.braze.com, ..., https://dashboard-01.braze.eu`.<br> Use a [tabela]({{site.baseurl}}/api/basics/#endpoints) a seguir para descobrir qual subdomínio você deve incluir com base no URL do seu dashboard.<br><br>
3. Após a conexão, navegue até a guia **Privacy Center** da Transcend. Aqui você precisará mapear os dados na Braze conforme suas práticas de dados. Para fazer isso, crie uma nova categoria e uma nova coleta de dados com a convenção de nomenclatura apropriada (por exemplo, "Listas de e-mail ou perfil de usuário"). Quando concluído, selecione **Publish**.<br><br>
4. Navegue de volta ao Data Map e selecione o silo de dados da Braze. Expanda **Manage Datapoints** e selecione o rótulo (categoria) da coleção que você criou na etapa anterior no menu suspenso. Você também pode escolher quais ações de dados (por exemplo, acesso ou exclusão) estão ativadas para quais pontos de dados. <br><br>
5. Em seguida, enquanto ainda estiver no silo de dados da Braze, expanda **Manage Identifiers**. Marque as respectivas caixas para os identificadores que você gostaria de ativar. Por exemplo, se quiser que a Transcend pesquise usuários por endereço de e-mail, marque a caixa para ativar o identificador de endereço de e-mail.

{% alert note %}
Se os identificadores não forem ativados corretamente, a Transcend poderá não processar solicitações de determinados usuários.
{% endalert %}

### Etapa 2: Testar solicitações {#step-2-test-requests}
A Transcend recomenda testar as solicitações no Data Map antes de começar a processar as solicitações dos usuários finais.
1. Acesse **Privacy Center** na Transcend e selecione **View your Privacy Center**.<br><br>
2. No **Privacy Center**, selecione **Take Control** e, em seguida, **Download my data**. Digite seu e-mail ou faça login para se autenticar antes de enviar a solicitação.<br><br>
3. Verifique se há uma mensagem da Transcend em seu e-mail. Você será solicitado a clicar em um link de verificação para confirmar a solicitação.<br><br>
4. Em seguida, de volta ao dashboard **Admin**, navegue até a guia **Incoming Requests** e selecione sua solicitação. Entre em contato com a Transcend pelo e-mail [support@transcend.io](mailto:support@transcend.io) se não encontrar a solicitação aqui.<br><br>
5. Depois de clicar na sua solicitação, navegue até a guia **Data Silos** e selecione **Braze**. Inspecione e confirme os dados retornados.<br><br>
6. Por fim, navegue até a guia **Report** e clique em **Approve and Send**. Você deverá receber o relatório no endereço de e-mail que enviou com a solicitação.

## Remover a integração da Braze {#remove-the-braze-integration}
Para remover o silo de dados da Braze do seu Data Map da Transcend:
1. Navegue até seu **Data Map** e clique em **Braze**. <br><br>
2. Na parte inferior da tela, expanda **Remove Braze** e clique em **Remove Silo**. Você será solicitado a confirmar que deseja remover o silo. Clique em **Ok**. <br><br>
3. Para confirmar se o silo foi removido, volte ao Data Map.