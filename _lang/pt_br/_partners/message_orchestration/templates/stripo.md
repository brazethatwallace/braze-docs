---
nav_title: Stripo
article_title: Stripo
alias: /partners/stripo
description: "Este artigo de referência descreve a parceria entre a Braze e o Stripo, um construtor de modelos de e-mail do tipo arrastar e soltar para criar e-mails sofisticados com elementos interativos."
page_type: partner
search_tag: Partner

---

# Stripo

> [O Stripo](https://stripo.email/) é um construtor de modelos de e-mail do tipo arrastar e soltar para criar e-mails responsivos com elementos interativos. Os usuários do Stripo também podem editar em HTML e decidir quais elementos exibir ou ocultar em vários dispositivos por meio do editor Stripo.

_Essa integração é mantida pelo Stripo._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o Stripo permite que você exporte seus e-mails personalizados do Stripo e faça upload deles como modelos na Braze.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ------------| ----------- |
| Conta Stripo | É necessário ter uma conta Stripo para aproveitar esta parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões completas de **Templates**. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Instância do cluster | Sua [instância de cluster]({{site.baseurl}}/api/basics/#endpoints) da Braze se alinha com o dashboard e o endpoint REST da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Criar e-mail no Stripo {#step-1-create-stripo-email}

Crie um e-mail no Stripo na plataforma Stripo e clique em **Export**.

![Exportação do Stripo]({% image_buster /assets/img_archive/stripo_export.png %})

### Etapa 2: Exportar modelo para a Braze {#step-2-export-template-to-braze}

Na caixa de diálogo que aparece, selecione **Braze** como seu método de exportação.

Em seguida, insira seu **nome da conta** (como o nome do espaço de trabalho), **chave de API** e sua **instância do cluster**.

![Formulário do Stripo]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
Esta é uma configuração única, e qualquer exportação futura utilizará automaticamente essa chave de API.
{% endalert %}

## Uso {#usage}

Encontre o modelo do Stripo que você fez upload na seção **Modelos e mídia > Modelos de e-mail** da sua conta na Braze. Agora você pode usar esse modelo de e-mail para começar a enviar mensagens de e-mail envolventes para seus clientes!