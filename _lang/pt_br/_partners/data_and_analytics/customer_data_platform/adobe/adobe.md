---
nav_title: Adobe
article_title: Adobe
description: "Esta página descreve a parceria entre a Braze e a Adobe, uma plataforma de dados do cliente, que permite que as marcas conectem e mapeiem seus dados da Adobe (atributos personalizados e Segments) para a Braze em tempo real. As marcas podem então agir com base nesses dados, oferecendo experiências personalizadas e direcionadas para esses usuários."
page_type: partner
page_order: 1
search_tag: Partner

---

# Adobe

> Criada com base na Adobe Experience Platform, a plataforma de dados do cliente em tempo real da Adobe reúne dados conhecidos e anônimos de várias fontes corporativas para criar perfis de clientes. Esses perfis podem então ser usados para fornecer experiências personalizadas em todos os canais e dispositivos em tempo real.

A integração entre a Braze e o Adobe CDP conecta e mapeia os dados da Adobe da sua marca (atributos personalizados e Segments) para a Braze em tempo real. Em seguida, é possível agir com base nesses dados, oferecendo experiências personalizadas e direcionadas aos seus usuários. Com a Adobe, a integração é intuitiva. Basta pegar qualquer [identidade](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en) da Adobe, mapeá-la para um ID externo da Braze e enviá-la para a plataforma da Braze. Todos os dados enviados estarão acessíveis na Braze por meio de um novo atributo `AdobeExperiencePlatformSegments`.

{% alert important %}
A integração da Adobe Experience Platform atualmente não oferece suporte à associação dinâmica de público. Isso significa que ela só pode adicionar valores aos perfis de usuário, não removê-los.
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Adobe | Uma [conta da Adobe](https://account.adobe.com/) é necessária para aproveitar esta parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Instância da Braze | Sua instância da Braze pode ser obtida com o seu gerente de integração da Braze ou pode ser encontrada na [página de visão geral da API]({{site.baseurl}}/api/basics#endpoints). |
| Endpoint REST da Braze | Sua URL de endpoint REST. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% alert important %}
O envio de atributos personalizados adicionais aumentará o uso de seus pontos de dados. Sugerimos que fale com seu gerente de sucesso do cliente para entender melhor esse possível aumento de pontos de dados.
{% endalert %}

## Integração {#integration}

### Etapa 1: Configurar o destino Braze {#step-1-configure-braze-destination}

Na página de **Settings** da Adobe, selecione **Destinations** em **Collections**. Em seguida, localize o bloco da **Braze** e selecione **Configure**.

![Catálogo de destinos da Adobe com o bloco de destino da Braze e a ação Configure.]({% image_buster /assets/img/adobe/braze-destination-configure.png %})

{% alert note %}
Se já existir uma conexão com a Braze, você verá um botão **Activate** no cartão de destino. Para saber mais sobre a diferença entre ativar e configurar, consulte a seção de catálogo da [documentação](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog) do espaço de trabalho de destinos da Adobe.
{% endalert %}

### Etapa 2: Forneça o token da Braze {#step-2-provide-braze-token}

Na etapa **Account**, forneça sua chave de API da Braze e selecione **Connect to destination**.

![Etapa de conta do destino Adobe Braze com campo de entrada da chave de API e ação de conexão.]({% image_buster /assets/img/adobe/braze-destination-account.png %}){: style="max-width:60%"}

### Etapa 3: Autenticação {#step-3-authentication}

Em seguida, na etapa **Authentication**, insira seus detalhes de conexão da Braze:
- **Name**: Digite o nome pelo qual você gostaria de reconhecer esse destino no futuro.
- **Destination**: Insira uma descrição que o ajude a identificar este destino.
- **Endpoint instance**: Insira sua instância de endpoint da Braze.
- **Marketing use case**: Os casos de uso de marketing indicam a intenção para a qual os dados serão exportados para o destino. Você pode selecionar um dos casos de uso de marketing definidos pela Adobe ou criar seu próprio caso de uso de marketing. Para saber mais sobre os casos de uso de marketing da Adobe, visite [Governança de dados na Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations).

![Etapa de autenticação do destino Adobe com campos de nome, destino e endpoint.]({% image_buster /assets/img/adobe/braze-destination-authentication.png %}){: style="max-width:60%;"}

### Etapa 4: Criar destino {#step-4-create-destination}
Selecione **Create destination**. Seu destino foi criado. Você pode selecionar **Save & Exit** para ativar segmentos mais tarde ou **Next** para continuar o fluxo de trabalho e selecionar segmentos para ativar.

### Etapa 5: Ativar segmentos {#step-5-activate-segments}
Ative os dados que você tem na CDP em tempo real da Adobe mapeando segmentos para o destino da Braze.

A lista a seguir destaca as etapas gerais necessárias para ativar um segmento. Para obter orientações completas sobre os segmentos da Adobe e o fluxo de trabalho de ativação de segmentos, visite [Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites).

1. Selecione e ative o destino Braze.
2. Selecione os segmentos aplicáveis.
4. Configure o agendamento e os nomes dos arquivos para cada segmento que você exportar.
5. Selecione atributos para enviar para a Braze.
6. Revise e verifique a ativação.

### Etapa 6: Mapeamento de campo {#step-6-field-mapping}

Para enviar corretamente os dados do seu público da Adobe Experience Platform para a Braze, complete a etapa de mapeamento de campo. O mapeamento cria um link entre os campos do modelo de dados da Adobe Experience e os campos correspondentes da plataforma Braze.

1. Na etapa de mapeamento, selecione **Add new mapping**.<br>![Página de mapeamento de campo da Adobe com o botão Add new mapping.]({% image_buster /assets/img/adobe/braze-destination-mapping.png %}){: style="max-width:50%;"}<br><br>
2. Na seção do campo de origem, selecione o botão de seta ao lado do campo vazio para abrir a janela de seleção do campo de origem.<br>![Seletor de campo de origem da Adobe para mapeamento de destino.]({% image_buster /assets/img/adobe/braze-destination-mapping-source.png %})<br><br>
3. Na janela, selecione os atributos da Adobe para mapear para seus atributos da Braze. <br>![Seletor de atributos da Adobe mostrando atributos de origem para mapeamento.]({% image_buster /assets/img/adobe/braze-destination-mapping-attributes.png %}){: style="max-width:70%;"}<br><br>Em seguida, selecione o namespace de identidade. Esta opção é usada para mapear um namespace de identidade da plataforma para um namespace da Braze.<br>![Seletor de namespace de identidade da Adobe usado para mapeamento da Braze.]({% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %}){: style="max-width:80%;"}<br> Escolha seus campos de origem e selecione **Select**.<br><br>
4. Na seção do campo de destino, selecione o ícone de mapeamento ao lado do campo.<br>![Painel de mapeamento de campo de destino da Adobe com o ícone de mapeamento selecionado.]({% image_buster /assets/img/adobe/braze-destination-mapping-target.png %}){: style="max-width:90%;"} <br><br>
5. Na janela de seleção de campo de destino, você pode escolher entre três categorias de campos de destino:<br><br>• **Select identity namespace**: Use esta opção para mapear namespaces de identidade da plataforma para namespaces de identidade da Braze.<br>• **Select custom attributes**: Use esta opção para mapear atributos da Adobe XDM para os atributos personalizados da Braze que você definiu na sua conta da Braze. <br><br>![Seletor de campo de destino da Adobe com opções de namespace de identidade e atributo personalizado.]({% image_buster /assets/img/adobe/braze-destination-mapping-target-fields.png %}){: style="max-width:60%;"}<br><br>**Você também pode usar esta opção para renomear atributos XDM existentes na Braze.** Por exemplo, o mapeamento de um atributo XDM `lastname` para um atributo personalizado `Last_Name` na Braze criará o atributo `Last_Name` na Braze caso ele ainda não exista e mapeará o atributo XDM `lastname` para ele. <br><br> Escolha seus campos de destino e selecione **Select**.<br><br>
6. Seu mapeamento de campo deve aparecer na lista.<br>![Mapeamentos de campo Adobe-para-Braze concluídos listados na etapa de mapeamento de destino.]({% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %})<br><br>
7. Para adicionar mais mapeamentos, repita as etapas de 1 a 6, conforme necessário.

## Caso de uso {#use-case}

Vamos supor que seu esquema de perfil XDM e sua instância da Braze contenham os seguintes atributos e identidades:

|     | Esquema de perfil XDM | Instância da Braze |
| --- | ------------------ | -------------- |
| Atributos | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| Identidades | - `Email`<br>- ID do anúncio do Google (`GAID`)<br>- ID da Apple para anunciantes (`IDFA`) | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Caso de uso" }

O mapeamento correto ficaria assim:

![Mapeamentos de destino: IdentityMap:IDFA mapeado para IdentityMap:external_id, IdentityMap:GAID mapeado para IdentityMap:external_id, IdentityMap:Email mapeado para IdentityMap:external_id, xdm:mobilePhone.number mapeado para CustomAttribute:PhoneNumber, xdm:person.name.lastName mapeado para CustomAttribute:LastName, xdm:person.name.firstName mapeado para CustomAttribute:FirstName]({% image_buster /assets/img/adobe/braze-destination-mapping-example.png %})

## Dados exportados {#exported-data}
Para verificar se os dados foram exportados com sucesso para a Braze, verifique sua conta da Braze. Os segmentos da Adobe Experience Platform são exportados para a Braze sob o atributo `AdobeExperiencePlatformSegments`.

## Uso de dados e governança {#data-usage-and-governance}
Todos os destinos da Adobe Experience Platform estão em conformidade com as políticas de uso de dados ao lidar com seus dados. Consulte [Governança de dados na CDP em tempo real](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en) para obter informações detalhadas sobre como a Adobe Experience Platform aplica a governança de dados.