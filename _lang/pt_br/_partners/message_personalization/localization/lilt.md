---
nav_title: LILT
article_title: LILT
description: "Este artigo de referência descreve a parceria entre a Braze e a LILT."
alias: /partners/lilt/
page_type: partner
search_tag: Partner
---

# LILT

> [A LILT](https://lilt.com/) é a solução completa de IA para tradução empresarial e criação de conteúdo. A LILT permite que organizações globais dimensionem e otimizem suas operações de conteúdo, produtos, comunicações e suporte, com agentes de IA e fluxos de trabalho totalmente automatizados.

_Essa integração é mantida pela LILT._

## Sobre essa integração {#about-this-integration}

O LILT Braze Connector permite a tradução de modelos de e-mail em HTML com velocidade de IA e qualidade de nível empresarial. Solicite a Tradução Instantânea alinhada à marca ou a Tradução Verificada com garantia de qualidade e receba conteúdo de e-mail multilíngue da LILT diretamente na Braze.

## Casos de uso {#use-cases}

A integração LILT Braze automatiza e acelera o processo de tradução, permitindo que equipes de marketing global lancem suas campanhas multilíngues rapidamente e com consistência de marca.

### Lançamento simplificado de campanha global {#streamlined-global-campaign-launch}

Lance campanhas de marketing em várias regiões simultaneamente, sem atrasos decorrentes de transferências manuais de tradução.

- **Cenário:** Sua empresa está lançando um novo produto em 10 países.
- **Solução:** Sua equipe de marketing finaliza o modelo de e-mail em inglês na Braze, adiciona a tag `LILT: Ready`, e o LILT Connector extrai automaticamente o conteúdo. Linguistas especializados no domínio revisam os prompts de tradução de IA na plataforma LILT para garantia de qualidade, e o conector envia as versões traduzidas de volta para a Braze.
- **Benefício:** Reduz o tempo de lançamento de suas campanhas globais de dias para horas, para que todos os clientes possam receber o anúncio do novo produto no momento ideal.

### Localização instantânea alinhada à marca {#instant-brand-aligned-localization}

Use a IA da LILT para obter traduções imediatas e alinhadas à marca para comunicações urgentes.

- **Cenário:** Você precisa enviar e-mails imediatamente para uma promoção relâmpago, uma oferta por tempo limitado ou uma interrupção urgente de serviço em cinco mercados geográficos.
- **Solução:** Você marca o modelo de e-mail com `LILT: Instant`. A LILT usa sua IA e ativos linguísticos específicos da sua empresa (como terminologia e guias de estilo) para gerar uma tradução de alta qualidade e consistente com a marca em questão de minutos.
- **Benefício:** Permite comunicações hiper-responsivas e em tempo real sem sacrificar a voz ou a qualidade da marca, o que é fundamental para marketing sensível ao tempo.

## Pré-requisitos {#prerequisites}

| Requisito       | Descrição |
|-----------------------|-----------------|
| Uma conta LILT   | É necessário ter uma conta LILT para aproveitar essa parceria.  |
| Uma chave da API REST da Braze  | Uma chave da API REST da Braze com as seguintes permissões:<br>- `templates.email.create`<br>- `templates.email.update`<br>- `templates.email.info`<br>- `templates.email.list`<br>- `templates.translations.source.get`<br>- `templates.translations.update`<br>- `templates.translations.get`<br>- `templates.translations.all.get`. <br><br> Crie essa chave no dashboard da Braze em **Settings** > **API Keys**. |
| Um endpoint REST da Braze | [A URL do seu endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint depende da URL da Braze para sua instância.  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }


## Integração {#integration}

### Etapa 1: Configurar o LILT Braze Connector {#step-1-configure-the-lilt-braze-connector}

1. Faça login na LILT e acesse **Connect** > **New Connector** > **Braze**.

![Conector Braze na LILT.]({% image_buster /assets/img/lilt/image_1_select_connector.png %})

{: start="2"}
2. Selecione o fluxo de trabalho de localização desejado para seu conteúdo Braze.

![Fluxo de trabalho Braze na LILT.]({% image_buster /assets/img/lilt/image_2_select_workflow.png %})

{: start="3"}
3. Insira e verifique os detalhes de configuração necessários:
- Sua chave de API da Braze
- Endpoint REST da Braze

![Credenciais de API completas.]({% image_buster /assets/img/lilt/image_3_api_creds.png %})

{: start="4"}
4. Selecione **Verify** para testar a configuração. Depois que a conexão for confirmada, salve a configuração.

### Etapa 2: Preparar seu espaço de trabalho na Braze {#step-2-prepare-your-braze-workspace}

1. Ative os recursos multilíngues nas configurações do seu espaço de trabalho da Braze.

![Configurar locais na Braze.]({% image_buster /assets/img/lilt/image_4_lilt_locales.png %})

{: start="2"}
2. Crie as seguintes tags na Braze para seu fluxo de trabalho LILT:
- `LILT: Ready`
- `LILT: In progress`
- `LILT: Sent to LILT`
- `LILT: Delivered`
- `LILT: Needs Attention`
- `LILT: Instant`

![Configurar tags LILT na Braze.]({% image_buster /assets/img/lilt/image_5_lilt_tags.png %})

{: start="3"}
### Etapa 3: Enviar conteúdo para a LILT para tradução {#step-3-send-content-to-lilt-for-translation}

1. Depois de configurar o LILT Braze Connector, use as tags de tradução Liquid nos seus modelos de e-mail da Braze para identificar o conteúdo a ser traduzido.
- Exemplo:  {% raw %}`{% translation id_0 %}`Hello, `{{first_name}}!{% endtranslation %}`{% endraw %}
2. Inicie a tradução atualizando a tag do modelo para indicar o fluxo de trabalho desejado:
- Escolha `LILT: Ready` para Tradução Verificada
- Escolha `LILT: Instant` para Tradução Instantânea alinhada à marca
3. O LILT Braze Connector é executado no horário predefinido para extrair o conteúdo marcado para a LILT. Acompanhe o progresso da tradução, pois as tags de conteúdo são atualizadas automaticamente na Braze para refletir o estágio do seu projeto.

![Modelo de e-mail da Braze com tags de tradução.]({% image_buster /assets/img/lilt/image_6_braze_template.png %})