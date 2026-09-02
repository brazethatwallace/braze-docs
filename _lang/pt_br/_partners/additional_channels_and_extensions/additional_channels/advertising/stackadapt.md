---
nav_title: StackAdapt
article_title: StackAdapt
description: "Este artigo de referência descreve a parceria entre a Braze e a StackAdapt."
alias: /partners/stackadapt/
page_type: partner
search_tag: Partner
---

# StackAdapt

> [StackAdapt](https://www.stackadapt.com/) é a principal plataforma de marketing impulsionada por IA usada por profissionais de marketing digital para entregar publicidade direcionada e orientada por desempenho.

_Esta integração é mantida pela StackAdapt._

A integração entre a Braze e a StackAdapt permite que você sincronize dados de perfil de usuário da Braze no StackAdapt Data Hub. Ao conectar as duas plataformas, você pode criar uma visão unificada de seus clientes e ativar dados primários para melhorar o desempenho dos anúncios.

## Casos de uso {#use-cases}

- **Reengajar usuários inativos:** Identifique usuários que cancelaram a inscrição das listas de marketing por e-mail na Braze e direcione-os com anúncios programáticos na StackAdapt para reengajá-los por meio de um canal diferente.
- **Criar experiências multicanal:** Estenda a jornada de um usuário além do e-mail. Por exemplo, se um usuário clicar em uma Campaign de e-mail na Braze, você pode usar a StackAdapt para mostrar a ele um anúncio programático complementar, reforçando a mensagem e impulsionando uma ação adicional.
- **Personalizar em escala:** Aproveite pontos de dados granulares da Braze, como "Cidade Natal" ou "Idioma", para veicular anúncios e e-mails altamente relevantes, localizados e específicos para o idioma.
- **Aprofundar a compreensão do seu público:** Ao sincronizar atributos de perfil, você pode criar segmentos de público mais ricos na StackAdapt, permitindo um direcionamento mais preciso e experiências de anúncios personalizadas.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ------------------- |
| **Conta StackAdapt** | Você precisa de uma conta StackAdapt ativa com permissões para gerenciar integrações do Data Hub. |
| **Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze** | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com as seguintes permissões: <br>- users.export.ids<br>- users.export.Segment or segmento<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get<br><br>Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| **Endpoint REST or transferir estado representacional da Braze** | [Sua URL de endpoint REST or transferir estado representacional]({{site.baseurl}}/api/basics/#endpoints). Seu endpoint depende da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Como funciona {#how-it-works}

O StackAdapt Data Hub se conecta diretamente à sua conta da Braze para extrair atributos de perfil de usuário. Isso permite que você aproveite os dados de cliente da Braze diretamente na StackAdapt para segmentação e ativação avançadas do público.

### Fluxo de dados {#data-flow}

1. A StackAdapt inicia uma conexão segura com sua instância da Braze usando as credenciais de API or interface de programação do aplicativo (API) fornecidas.
2. A StackAdapt recupera dados de perfil de usuário e especificamente as propriedades que você selecionou e mapeou.
3. Os dados são normalizados e ingeridos no seu StackAdapt Data Hub, tornando-se disponíveis para segmentação e uso em suas campanhas.
4. A integração permite sincronizações de dados programadas (por exemplo, diárias) para manter seus públicos da StackAdapt atualizados com os dados de perfil mais recentes da Braze.

## Campos sincronizados {#fields-synced}

A StackAdapt pode sincronizar uma variedade de campos de perfil da Braze, incluindo, mas não se limitando a:

{% tabs local %}
{% tab Standard attributes %}
- E-mail
- Data de nascimento
- Nome
- Sobrenome
- Telefone
- Cidade
- País
- Gênero
- Fuso horário
- Data de criação
- ID externo
- Idioma

{% endtab %}
{% tab Custom attributes %}
Atributos que são específicos para seu app ou negócio, definidos com base nas necessidades específicas do seu negócio.

{% endtab %}
{% tab Attribution data %}
- Anúncio atribuído
- Grupo de anúncios atribuído
- Campaign atribuída
- Origem atribuída

{% endtab %}
{% tab Subscription status %}
- Status de inscrição de e-mail
- Status de inscrição de push

É crucial mapear com precisão os campos na Braze que refletem o consentimento do usuário para comunicações de marketing (por exemplo, status de inscrição de e-mail) para que seus esforços publicitários permaneçam em conformidade com as preferências do usuário e as regulamentações de privacidade.

{% endtab %}
{% endtabs %}

## Configuração da integração {#setting-up-the-integration}

Siga estas etapas para importar seus perfis de usuário da Braze:

1. Faça login na sua conta da StackAdapt.
2. No menu de navegação, selecione **Data Hub**.
3. Selecione **Import Profiles** e, em seguida, selecione **Braze** na lista de integrações disponíveis.
4. Insira suas credenciais de API or interface de programação do aplicativo (API) da Braze quando solicitado.
- **Braze REST or transferir estado representacional API or interface de programação do aplicativo (API) Key:** Localizada na Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. Como melhor prática de segurança, recomendamos criar uma chave de API or interface de programação do aplicativo (API) dedicada para sua integração com a StackAdapt.
- **Braze App Key:** Localizada na Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)** ou **Manage Apps**.
- **Braze REST or transferir estado representacional Endpoint URL:** A URL base para sua instância da Braze (por exemplo, `https://rest.iad-01.braze.com`).
5. Selecione **Connect** para verificar as credenciais.

![Conexão da Braze na StackAdapt.]({% image_buster /assets/img/stackadapt/stackadapt_braze_connection_settings.png %})

{: start="6"}
6. Escolha sua conexão e selecione seu anunciante da StackAdapt.
7. Configure seus **Property Mappings**. Revise e confirme os mapeamentos padrão e as propriedades pré-selecionadas que a StackAdapt sugere.
8. (Opcional) Se você quiser importar propriedades adicionais, selecione-as marcando as respectivas caixas de seleção e especifique se contêm IPI e seu tipo de dado.

![Mapeamentos de propriedades na conexão da Braze com a StackAdapt.]({% image_buster /assets/img/stackadapt/stackadapt_mappings.png %})

{: start="9"}
9. Adicione seus perfis a uma **List** ou crie uma nova para que você possa agrupar e segmentar seus perfis.
10. Selecione **Activate Integration** para iniciar a sincronização inicial de dados.

## Considerações {#considerations}

- **Importação de eventos e propriedades personalizados:** Este recurso ainda não é suportado.
- **Latência de dados:** Pode levar até 24 horas para importar todos os dados de perfil de usuário.
- **Gerenciamento de consentimento:** Confirme que suas práticas de coleta de dados na Braze estão alinhadas com as regulamentações de privacidade e que você possui o consentimento necessário para usar dados de clientes para fins publicitários. A StackAdapt depende do status de consentimento passado pelos seus sistemas de origem.
- **Consistência de atributos:** Para maximizar a eficácia dos seus dados, mantenha a consistência na forma como os atributos são nomeados e preenchidos na Braze antes de sincronizá-los com a StackAdapt.