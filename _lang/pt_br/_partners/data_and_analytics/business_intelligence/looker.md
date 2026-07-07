---
nav_title: Looker
article_title: Looker
alias: /partners/looker/
description: "Este artigo de referência descreve a parceria entre a Braze e o Looker, uma plataforma de business intelligence e análise de big data."
page_type: partner
search_tag: Partner

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/looker-integration-with-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Looker {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomlooker-integration-with-braze-stylefloatrightwidth120pxborder0-classnoimgborderlooker}

> O [Looker](https://looker.com/), uma plataforma de business intelligence e análise de big data, permite que você explore, analise e compartilhe análises de negócios em tempo real de forma integrada.

A integração entre a Braze e o Looker permite que os usuários da empresa aproveitem a sinalização de usuários dos [blocos do Looker](#looker-blocks) e do [Looker Actions](#looker-actions) por meio da REST API. Esses usuários sinalizados podem ser adicionados a segmentos para [direcionar](#segment-users) futuras Campaigns ou Canvas da Braze. Para usar o Looker com a Braze, recomendamos enviar seus dados da Braze para um [data warehouse usando o Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) e, em seguida, usar os blocos do Looker da Braze para modelar e visualizar rapidamente seus dados da Braze no Looker.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Looker | É necessário ter uma [conta Looker](https://looker.com/) para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Ela pode ser criada no dashboard da Braze em **Settings** > **API Keys**. |
| Endpoint REST da Braze | A URL do seu endpoint REST. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

#### Considerações {#considerations}

- Esse processo só funciona com dados que não tenham sido pivotados.
- A API processa um máximo de 100.000 linhas por vez.
- A contagem final da sinalização de um usuário pode ser menor devido a duplicatas ou não usuários.

## Integração {#integration}

### Blocos do Looker {#looker-blocks}

Nossos blocos do Looker ajudam os clientes da Braze a acessar rapidamente uma visão dos dados granulares que oferecemos via [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/). Nossos blocos fornecem visualizações e modelagens pré-fabricadas para os dados do Currents, de modo que os clientes da Braze possam implementar facilmente padrões analíticos, como retenção, avaliar a entregabilidade das mensagens, analisar mais detalhadamente o comportamento dos usuários e muito mais.

Para implementar os blocos do Looker, siga as instruções nos arquivos README do código do GitHub.
- [README do bloco de análise de engajamento com mensagem](https://github.com/llooker/braze_message_engagement_block/blob/master/README.md)
- [README do bloco de análise de comportamento do usuário](https://github.com/llooker/braze_retention_block/blob/master/README.md)

Ambas as integrações pressupõem que sua [integração inicial da Braze]({{site.baseurl}}/user_guide/get_started/sdk_overview/), bem como sua integração da Braze com um [data warehouse](https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) compatível com o Looker, estejam configuradas adequadamente para capturar e enviar os dados necessários.


{% alert important %}
A Braze criou nossos blocos do Looker usando o [Snowflake](https://www.snowflake.com/) como data warehouse. Embora nosso objetivo seja que nossos blocos funcionem com o maior número possível de data warehouses, algumas funções SQL podem diferir em disponibilidade, sintaxe ou comportamento entre dialetos.
{% endalert %}

{% alert warning %}
Esteja ciente das diferentes convenções de nomenclatura! Nomes personalizados podem causar incongruências nos dados, a menos que você altere todos os nomes correspondentes. Se você personalizou algum nome de visualização/tabela ou modelo, renomeie cada um deles no LookML com o nome que você selecionou.
{% endalert %}

#### Blocos disponíveis {#available-blocks}

| Bloco | Descrição |
|---|---|
| Bloco de análise de engajamento com mensagem | Esse bloco inclui dados sobre push, e-mail, mensagens no app, webhook, conversão, entrada no Canvas e eventos de inscrição no grupo de controle de Campaign. <br><br>Saiba mais sobre este [bloco do Looker](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) ou confira o [código do GitHub](https://github.com/llooker/braze_message_engagement_block). |
| Bloco de análise de comportamento do usuário | Este bloco inclui dados sobre eventos personalizados, compras, sessões, eventos de localização e desinstalações.<br><br>Saiba mais sobre este [bloco do Looker](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) ou confira o [código do GitHub](https://github.com/llooker/braze_retention_block). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Blocos disponíveis" }

### Looker Actions {#looker-actions}

As Looker Actions permitem que você sinalize usuários na Braze por meio do endpoint da REST API a partir de um Looker Look. As ações exigem que uma dimensão seja marcada com `braze_id`. A ação anexará o valor sinalizado ao atributo personalizado `looker_export` do usuário.

{% alert important %}
Somente os usuários existentes serão sinalizados. Não é possível usar Looks pivotados ao sinalizar dados na Braze.
{% endalert %}

#### Etapa 1: Configurar uma ação do Looker da Braze {#step-1-set-up-a-braze-looker-action}

Configure uma ação do Looker da Braze com sua chave da API REST e o endpoint REST da Braze.

![A página de configuração do Looker Braze. Aqui você pode encontrar campos para a chave de API e o endpoint da API REST da Braze.]({% image_buster /assets/img/braze-looker-action.png %})

#### Etapa 2: Configurar o Looker Develop {#step-2-set-up-looker-develop}

No Looker Develop, selecione as visualizações apropriadas. Adicione `braze_id` à tag de dimensões e confirme as alterações.
A tag `braze_id` é usada para determinar qual campo é a chave exclusiva.

```lookml
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

**Certifique-se de confirmar as alterações. O Looker Actions só funciona em configurações de produção.**

#### Etapa 3: Definir atributos do usuário nas tags {#step-3-set-user-attributes-in-tags}

Opcionalmente, qualquer atributo pode ser definido usando uma tag `braze[]` com o nome do atributo entre colchetes. Por exemplo, se você quisesse que um atributo personalizado `user_segment` fosse enviado, a tag seria `braze[user_segment]`.

Observe as seguintes limitações:
- Os atributos só serão enviados se forem **incluídos como campo no look**.
- Os tipos suportados são `Strings`, `Boolean`, `Numbers` e `Dates`.
- Os nomes de atributos diferenciam maiúsculas de minúsculas.
- Os atributos padrão também podem ser definidos, desde que correspondam exatamente aos nomes do [perfil de usuário padrão]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields).
- A tag completa deve ser formatada entre aspas. Por exemplo, `tags: ["braze[first_name]"]`. Outras tags também podem ser atribuídas, mas serão ignoradas.
- Informações adicionais podem ser encontradas no [GitHub](https://github.com/looker/actions/tree/master/src/actions/braze).

#### Etapa 4: Enviar a ação do Looker {#step-4-send-the-looker-action}

1. Em um Look com uma dimensão `braze_id` selecionada, clique na engrenagem de configurações (<i class="fas fa-cog"></i>) no canto superior direito e selecione **Send...**.
2. Selecione a ação personalizada da Braze.
3. Em **Unique Key**, forneça a chave de mapeamento do usuário primário para a conta Braze (`external_id` ou `braze_id`).
4. Dê um nome à exportação. Se nenhum for fornecido, `LOOKER_EXPORT` será usado.
5. Em **Advanced Options**, selecione **Results in Table** ou **All Results** e, em seguida, **Send**.<br><br>![]({% image_buster /assets/img/send-looker-action.png %})<br><br>Se a exportação tiver sido enviada corretamente, `LOOKER_EXPORT` deverá aparecer no perfil do usuário como um atributo personalizado com o valor inserido na ação.<br><br>![]({% image_buster /assets/img/custom-attributes-looker.png %})

##### Exemplo de API de saída {#example-outgoing-api}

A seguir, um exemplo de uma chamada de API de saída, que será enviada para o [endpoint `/users/track/`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

###### Cabeçalho {#header}
```
Authorization: Bearer [API_KEY]
```

###### Corpo {#body}
```json
{
   "attributes" : [
      {
        "external_id" : "user_01",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_02",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_03",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      .....
   ]
}
```

### Segmentar usuários na Braze {#segment-users}

Na Braze, para criar um segmento desses usuários sinalizados, navegue até **Segments** em **Engagement**, nomeie seu segmento e selecione **Looker_Export** como o filtro. Em seguida, use a opção "includes value" e forneça o sinalizador de atributo personalizado que você atribuiu no Looker.

![No criador de segmentos da Braze, o filtro "looker_export" está definido como "includes_value" e "Looker".]({% image_buster /assets/img/braze_segments.png %})

Depois de salvo, você pode fazer referência a esse segmento durante a criação de Canvas ou Campaign na etapa de direcionamento de usuários.

## Solução de problemas {#troubleshooting}
Se estiver tendo problemas com o Looker Actions, adicione um usuário teste aos [grupos internos]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/) e verifique o seguinte:

* A chave de API tem as permissões `users.track`.
* O endpoint REST correto foi inserido, como `https://rest.iad-01.braze.com`.
* Uma tag `braze_id` está definida na visualização da dimensão.
* Sua consulta inclui a dimensão ou atributo Id como uma coluna.
* Os resultados do Looker não são pivotados.
* A chave exclusiva foi selecionada corretamente. Normalmente, o `external_id`.
* O `braze_id` na dimensão é diferente do `braze_id` na API. O `braze_id` na dimensão é usado para indicar que é o campo `id` para a API da Braze. Para a maioria das finalidades, o `external_id` é a chave primária no ato do envio.
* O usuário `external_id` existe na plataforma Braze.
* O campo `looker_export` está definido como `Automatically Detect` em `Braze Platform > Settings > Manage Settings > Custom Attributes`.
* As alterações são confirmadas para a produção. O Looker Actions funciona em configurações de produção.