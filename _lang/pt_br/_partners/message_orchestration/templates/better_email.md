---
nav_title: Better Email
article_title: Better Email
alias: /partners/better_email/
description: "Este artigo de referência descreve a parceria entre a Braze e a Better Email, uma plataforma colaborativa de criação de e-mails construída em torno de um Email Design System que permite exportar modelos prontos para produção para a Braze."
page_type: partner
search_tag: Partner
---

# Better Email

> A [Better Email](https://better.email) é uma plataforma colaborativa de criação de e-mails construída em torno de um Email Design System. As equipes podem projetar, gerenciar e exportar e-mails prontos para produção a partir de um sistema compartilhado de blocos e estilos, garantindo consistência de marca em escala sem depender de desenvolvedores ou agências.

_Essa integração é mantida pela Better Email._

## Sobre a integração {#about-the-integration}

Com a integração entre a Braze e a Better Email, você cria e gerencia modelos de e-mail no editor colaborativo da Better Email e os exporta diretamente para a Braze como modelos de e-mail prontos para uso.

Ao reexportar um e-mail, a Better Email atualiza o modelo existente na Braze em vez de criar uma duplicata, mantendo sua biblioteca de modelos organizada.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Better Email | Uma conta Better Email com acesso de administrador para criar integrações |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões completas de **Modelos**.<br><br>Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [URL do seu endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Use o host REST, não a URL do dashboard — por exemplo, `rest.fra-01.braze.eu`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

A Better Email foi criada para equipes de marketing que desejam gerenciar e-mails por meio de um design system e exportá-los para a Braze sem trabalho manual com HTML. Considere a Better Email se você:

- Mantém uma grande biblioteca de modelos de e-mail e precisa de consistência em todos eles
- Deseja aplicar diretrizes da marca por meio de um Email Design System compartilhado
- Colabora entre equipes — designers, profissionais de marketing e desenvolvedores — na produção de e-mails
- Usa a Braze para execução de campanhas e quer eliminar o gargalo entre design e implantação

## Integrar a Better Email com a Braze {#integrate-better-email-with-braze}

### Etapa 1: Encontre seus valores da Braze {#step-1-find-your-braze-values}

No dashboard da Braze, colete as seguintes informações:

- **Instance URL** — Use o host REST, não a URL do dashboard (por exemplo, `rest.fra-01.braze.eu`).
- **API key** — Uma chave da API REST com permissões completas de **Modelos**, criada em **Configurações** > **Chaves de API**.

### Etapa 2: Configure a integração na Better Email {#step-2-set-up-the-integration-in-better-email}

1. Acesse **Integrations**.
2. Crie uma nova integração.
3. Insira um nome para a integração (por exemplo, `Braze`).
4. Selecione **Braze** como o tipo.
5. Opcionalmente, restrinja a integração a usuários ou grupos específicos em **Access**.
6. Selecione **Save**.
7. Insira a **Instance URL** e a **API Key**.
8. Ative a integração.
9. Selecione **Save** novamente.

### Etapa 3: Exporte para a Braze {#step-3-export-to-braze}

Quando a integração estiver ativa, abra qualquer e-mail na Better Email. Em seguida, selecione **Export** > **Braze**.

A Better Email cria ou atualiza o modelo de e-mail correspondente na Braze. Após a primeira exportação, a Better Email armazena o ID do modelo da Braze — reexportar o mesmo e-mail atualiza esse modelo em vez de criar uma duplicata.

### Sincronizar campos de destinatários da Braze (opcional) {#sync-recipient-fields-from-braze-optional}

A Better Email pode sincronizar atributos personalizados da Braze para uso como merge tags e campos de segmentação.

1. Abra a integração da Braze na Better Email.
2. Ative **Sync recipient fields**.
3. Selecione **Save**.
4. Acesse **Recipient Fields**.
5. Selecione **Sync from** ao lado da sua integração.

A Better Email lê os atributos personalizados disponíveis na Braze e os mapeia em campos de destinatários.

## Solução de problemas {#troubleshooting}

Se uma exportação ou sincronização falhar, verifique o seguinte:

- A **Instance URL** é a URL REST, não a URL do dashboard.
- A chave de API ainda está ativa e possui as permissões necessárias de **Modelos**.
- A integração está ativada na Better Email.
- Os usuários ou grupos que precisam da integração têm acesso em **Access**.

Para mais ajuda, [entre em contato com o suporte da Better Email](mailto:support@better.email).

## Use a integração {#use-the-integration}

Encontre seus modelos exportados da Better Email na Braze em **Modelos e mídia** > **Modelos de e-mail**. Use-os em qualquer Campaign ou Canvas da Braze.