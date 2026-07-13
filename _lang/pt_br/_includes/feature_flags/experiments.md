# Experimentos com Feature Flag {#feature-flag-experiments}

> Experimentos com Feature Flag permitem que você faça testes A/B de mudanças em suas aplicações para otimizar as taxas de conversão. Os profissionais de marketing podem usar Feature Flags para determinar se um novo recurso impacta positiva ou negativamente as taxas de conversão, ou qual conjunto de propriedades de Feature Flag é o mais otimizado.

## Pré-requisitos {#prerequisites}

Antes que você possa rastrear dados de usuários no experimento, seu app precisa registrar quando um usuário interage com uma Feature Flag. Isso é chamado de impressão de Feature Flag. Certifique-se de registrar uma impressão de Feature Flag sempre que um usuário vir ou puder ter visto o recurso que você está testando, mesmo que ele esteja no grupo de controle.

Para saber mais sobre como registrar impressões de Feature Flag, consulte [Como criar Feature Flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#impressions).

{% tabs %}
{% tab Web %}

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewFeature();
} else {
  return new ExistingFeature();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("my-new-feature")
braze.logFeatureFlagImpression("my-new-feature")
if (featureFlag?.enabled == true) {
  return NewFeature()
} else {
  return ExistingFeature()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Criando um experimento de Feature Flag {#creating-a-feature-flag-experiment}

### Etapa 1: Criar um experimento {#step-1-create-an-experiment}

1. Acesse **Envio de mensagens** > **Campaigns** e selecione **+ Create Campaign**.
2. Selecione **Feature Flag Experiment**.
3. Dê à sua campanha um nome claro e significativo.

### Etapa 2: Adicionar variantes de experimento {#step-2-add-experiment-variants}

Em seguida, crie variações. Para cada variante, escolha a Feature Flag que deseja ativar ou desativar e, em seguida, revise as propriedades atribuídas.

Para testar o impacto do seu recurso, use variantes para dividir o tráfego em dois ou mais grupos. Nomeie um grupo como "Meu grupo de controle" e desative suas Feature Flags.

Experimentos com Feature Flag suportam até nove grupos no total: um grupo de controle mais até oito variantes.

### Etapa 3: Substituir propriedades (opcional) {#step-3-overwrite-properties-optional}

É possível optar por substituir as propriedades padrão configuradas inicialmente para os usuários que recebem uma variante de campanha específica.

Para editar, adicionar ou remover propriedades padrão adicionais, edite a própria Feature Flag em **Envio de mensagens** > **Feature Flags**. Quando uma variante estiver desativada, o SDK retornará um objeto de propriedades vazio para a Feature Flag em questão.

![A seção "Variantes de Experimento" com a chave da variável "link" sobrescrita com "/sales".]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

### Etapa 4: Escolher os usuários a serem direcionados {#step-4-choose-users-to-target}

Use um de seus segmentos ou filtros para escolher seus [usuários-alvo]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users). Por exemplo, é possível usar o filtro **Received Feature Flag Variant** para redirecionar os usuários que já receberam um teste A/B.

![A página "Alvo" em um experimento de Feature Flag com "Received Feature Flag Variant" destacado na barra de pesquisa do grupo de filtros.]({% image_buster /assets/img/feature_flags/variant-filter-dropdown.png %}){: style="max-width:70%"}

{% alert note %}
A associação ao segmento é calculada quando as Feature Flags são atualizadas para um determinado usuário. As alterações são disponibilizadas após o app atualizar as Feature Flags ou quando uma nova sessão é iniciada.
{% endalert %}

### Etapa 5: Distribuir variantes {#step-5-distribute-variants}

Escolha a distribuição percentual para o seu experimento. Como prática recomendada, você não deve alterar a distribuição após o seu experimento ter sido lançado.

### Etapa 6: Atribuir conversões {#step-6-assign-conversions}

A Braze permite que você acompanhe com que frequência os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events), após receberem uma campanha. Especifique uma janela de até 30 dias durante a qual uma conversão será contada se o usuário realizar a ação especificada.

### Etapa 7: Revisar e lançar {#step-7-review-and-launch}

Depois de concluir a construção do seu experimento, revise os detalhes e selecione **Launch Experiment**.

## Revisão dos resultados {#reviewing-the-results}

Após a conclusão do experimento de Feature Flag, é possível revisar os dados de impressão do experimento. Acesse **Envio de mensagens** > **Campaigns** e selecione a campanha com seu experimento de Feature Flag.

### Análise de dados da campanha {#campaign-analytics}

A **Campaign Analytics** oferece uma visão geral de alto nível do desempenho do seu experimento, como:

- O número total de impressões
- O número de impressões únicas
- A taxa de conversão primária
- A receita total gerada pela mensagem
- O público estimado

Você também pode visualizar as configurações do experimento para entrega, público e conversão.

### Desempenho do experimento de Feature Flag {#feature-flag-experiment-performance}

O painel **Feature Flags Experiments Performance** mostra o desempenho da sua mensagem em várias dimensões. As métricas específicas que você vê variam de acordo com o canal de envio de mensagens escolhido e se você está executando um teste multivariante. Para ver os valores de Feature Flag associados a cada variante, selecione **Preview**.