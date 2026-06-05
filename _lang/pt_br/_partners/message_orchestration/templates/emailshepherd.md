---
nav_title: EmailShepherd
article_title: EmailShepherd
alias: /partners/emailshepherd/
description: "Este artigo de referência descreve a parceria entre a Braze e o EmailShepherd, uma plataforma de criação de e-mails baseada em agentes, construída sobre o seu Email Design System, que publica e-mails aprovados no seu espaço de trabalho da Braze."
page_type: partner
search_tag: Partner
---

# EmailShepherd

> O [EmailShepherd](https://emailshepherd.com/) é uma plataforma de criação de e-mails baseada em agentes, construída sobre o seu Email Design System, que permite que toda a sua equipe de marketing — e agentes de IA — produza e-mails alinhados à marca e prontos para produção, sem gargalos. A integração com a Braze publica e-mails aprovados diretamente no seu espaço de trabalho da Braze, para que os profissionais de marketing possam escalar a produção de e-mails na Braze sem sacrificar a consistência da marca.

_Essa integração é mantida pelo EmailShepherd._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o EmailShepherd permite que você crie e-mails no seu Email Design System dentro do EmailShepherd e os exporte para a Braze como modelos de e-mail. Sua equipe cria e aprova e-mails no EmailShepherd e, em seguida, publica modelos prontos para produção na Braze sem necessidade de transferência manual de HTML.

## Pré-requisitos {#prerequisites}

Os itens a seguir são necessários para usar esta integração:

| Requisito | Descrição |
| ----------- | ----------- |
| Conta no EmailShepherd | Uma conta no EmailShepherd é necessária para usar esta integração. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões completas de "Templates". <br><br>Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Instância da Braze | A [instância do cluster]({{site.baseurl}}/api/basics/#endpoints) da Braze está alinhada ao seu dashboard e endpoint REST da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

O EmailShepherd foi criado para equipes que desejam escalar a produção de e-mails mantendo cada envio alinhado à marca. É uma ótima opção se você deseja:

- **Garantir consistência de marca em escala:** seu Email Design System define os componentes, cores e layouts aprovados. Todo e-mail publicado na Braze é alinhado à marca por construção.
- **Abrir a produção de e-mails para toda a equipe:** um construtor de arrastar e soltar baseado no seu Email Design System permite que qualquer pessoa crie e-mails prontos para produção.
- **Usar criação de campanhas baseada em agentes:** agentes de IA trabalham dentro das diretrizes do seu Email Design System, então as campanhas que eles produzem são alinhadas à marca e prontas para envio.

## Integração {#integration}

### Etapa 1: Criar seu conector do EmailShepherd {#step-1-create-your-emailshepherd-connector}

{% alert note %}
Esta é uma configuração única. Depois de criar o conector, o EmailShepherd usa essas credenciais para todas as exportações futuras para a Braze.
{% endalert %}

1. No EmailShepherd, acesse **Connectors** > **Add connector**.
2. Selecione **Braze** e insira um nome para o conector.
3. Insira sua chave de API e selecione sua instância da Braze.
4. Selecione **Create Connector** para salvar a conexão.

![Formulário de conector do EmailShepherd com campos de instância da Braze e chave de API]({% image_buster /assets/img_archive/emailshepherd_step1.png %}){: style="max-width:60%;"}

### Etapa 2: Exportar um e-mail do EmailShepherd {#step-2-export-an-email-from-emailshepherd}

No EmailShepherd, localize o e-mail que você deseja exportar para a Braze. Certifique-se de que ele esteja publicado e selecione **Export**.

![Editor de e-mail do EmailShepherd com a ação de exportação]({% image_buster /assets/img_archive/emailshepherd_step2.png %}){: style="max-width:60%;"}

### Etapa 3: Configurar e publicar na Braze {#step-3-configure-and-publish-to-braze}

1. Na página de exportação, selecione seu conector da Braze em **Connectors** (por exemplo, **Braze Prod**).
2. Escolha uma opção de **Image hosting** para as imagens da sua biblioteca de imagens do EmailShepherd. Imagens inseridas por URL não são alteradas durante a exportação.
3. Confirme o **Locale** e insira um **Template name** para o e-mail na Braze.
4. Selecione **Start export**.

![Página de exportação do EmailShepherd com campos de conector da Braze, hospedagem de imagens e nome do modelo]({% image_buster /assets/img_archive/emailshepherd_step3.png %}){: style="max-width:60%;"}

## Usando a integração {#use-the-integration}

Na Braze, encontre seus e-mails exportados em **Conteúdo** > **E-mail**. Você pode usar esses modelos em Campaigns e Canvas da Braze.

## Suporte {#support}

Para saber mais sobre as integrações do EmailShepherd, consulte a [documentação do EmailShepherd](https://emailshepherd.com/docs/).