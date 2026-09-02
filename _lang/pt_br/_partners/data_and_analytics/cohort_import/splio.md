---
nav_title: Splio
article_title: Splio
alias: /partners/splio/
description: "Este artigo de referência descreve a parceria entre a Braze e a Splio, que permite enviar campanhas mais direcionadas, encontrar novas oportunidades de produtos e aumentar a receita."
page_type: partner
search_tag: Partner

---

# Splio

> A [Splio](https://splio.com/) é uma ferramenta de criação de público que permite aumentar o número de campanhas e a receita sem prejudicar a experiência do cliente, além de fornecer análise de dados para rastrear o desempenho das campanhas de CRM on-line e off-line.

A integração da Braze com a Splio permite planejar e executar melhores estratégias de CRM, enviar campanhas mais direcionadas, encontrar novas oportunidades de produtos e aumentar a receita.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Splio | Você precisa de uma conta Splio para essa parceria. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração de importação de dados {#data-import-integration}

Para integrar a Braze e a Splio, é necessário configurar a plataforma da Splio, exportar uma campanha existente da Splio e criar um Segment or segmento or segmento de coorte na Braze para direcionar usuários em campanhas futuras.

### Etapa 1: Obter a chave de importação de dados da Braze {#step-1-get-the-braze-data-import-key}

Na Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Splio**.

Encontre seu endpoint REST e gere sua chave de importação de dados da Braze. Depois de gerar a chave, você pode criar uma nova chave ou invalidar uma existente.<br><br>![A página do parceiro de tecnologia Splio com o endpoint REST e a chave de importação de dados.]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"}

Para concluir a integração, forneça a chave de importação de dados e o endpoint REST or transferir estado representacional à sua equipe de operações de dados da Splio. A Splio estabelece a conexão e entra em contato com você após a conclusão da configuração.

### Etapa 2: Exportar uma campanha da plataforma Splio {#step-2-export-a-campaign-from-the-splio-platform}

Toda vez que quiser criar uma coorte de usuários da Splio na Braze, você deve primeiro exportá-la da plataforma da Splio.

Na Splio, selecione as campanhas que deseja exportar e clique em **Export Campaigns**. Após a exportação, o público é automaticamente enviado para sua conta na Braze.

![Exportação de campanhas da plataforma Splio.]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### Etapa 3: Criar um Segment or segmento or segmento a partir do público personalizado da Splio {#step-3-create-a-segment-from-the-splio-custom-audience}

Na Braze, navegue até **Segments**, nomeie seu Segment or segmento or segmento de coorte Splio e selecione **Splio Cohorts** como seu filtro. A partir daí, escolha a coorte da Splio a ser incluída. Depois de criar seu Segment or segmento or segmento de coorte da Splio, você pode selecioná-lo como um filtro de público ao criar uma Campaign ou um Canvas.

![Criação de um segmento de coorte Splio na Braze.]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![No criador de segmentos da Braze, o filtro de atributos do usuário "Splio cohort" está definido como "includes" e "Primary cohort".]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

Está tendo problemas para localizar sua coorte? Consulte a seção de [solução de problemas](#troubleshooting) para obter orientação.

{% alert important %}
Somente os usuários que já existem na Braze são adicionados ou removidos de uma coorte. A importação de coorte não cria novos usuários na Braze.
{% endalert %}

## Usando essa integração {#using-this-integration}

Para usar seu Segment or segmento or segmento Splio, crie uma Campaign ou um Canvas na Braze e selecione o Segment or segmento or segmento como seu público-alvo.

![No criador de campanhas da Braze, na etapa de direcionamento, o filtro "Direcionar usuários por segmento" está definido como "Coorte Splio".]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## Correspondência de usuários {#user-matching}

A Braze faz a correspondência de usuários identificados pelo `external_id` ou `alias`. Usuários anônimos são correspondidos pelo `device_id`. Usuários identificados que foram originalmente criados como anônimos não podem ser correspondidos pelo `device_id` e devem ser correspondidos pelo `external_id` ou `alias`.

## Solução de problemas {#troubleshooting}

Se não conseguir encontrar a coorte correta na lista, visualize os detalhes da sua campanha na Splio e verifique o nome consultando o **Export File Name**.

![A parte inferior da página de detalhes da campanha mostra o nome da sua coorte.]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

Se estiver tendo problemas para recuperar seu público, entre em contato com a [equipe da Splio](mailto:support-team@splio.com) para obter suporte.