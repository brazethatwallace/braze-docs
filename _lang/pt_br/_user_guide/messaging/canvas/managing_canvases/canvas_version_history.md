---
nav_title: Histórico de versões do Canvas
article_title: Histórico de versões do Canvas
alias: "/canvas_version_history/"
page_order: 2
description: "Este artigo de referência aborda como gerenciar o histórico de versões do seu Canvas."
page_type: reference
tool: Canvas
---

# Histórico de versões do Canvas {#canvas-version-history}

> O histórico de versões permite que você visualize e acesse a análise de dados do Canvas e as jornadas de usuários de qualquer versão anterior do seu Canvas.

Consultar o histórico de versões do Canvas pode ser especialmente útil para manter um registro da evolução de um Canvas. Por exemplo, se você fizer uma alteração em grande escala, pode consultar versões anteriores do Canvas para entender melhor como seus fluxos de trabalho progrediram.

{% alert tip %}
Para obter uma lista completa dos Canvas no seu espaço de trabalho (por exemplo, para uma auditoria), use o [endpoint Exportar lista de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) e pagine pelos resultados.
{% endalert %}

## Gerenciando versões {#managing-versions}

![Captura de tela relacionada ao gerenciamento de versões.]({% image_buster /assets/img_archive/canvas_version_history.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Para criar uma nova versão, clique em **Atualizar Canvas**. Isso permite que você faça alterações sem sobrescrever a configuração anterior do Canvas. Quando uma nova versão do Canvas é criada, os usuários que já estão no Canvas avançarão pelo fluxo de trabalho da nova versão. Os usuários que entrarem no Canvas também entrarão na nova versão.

Para acessar o histórico de versões, navegue até os detalhes do Canvas na parte superior do seu Canvas e selecione **# Versions**. Aqui, você tem acesso à barra lateral **Version history**. Selecione qualquer uma das versões do Canvas na barra lateral para visualizar e comparar os detalhes do Canvas. Para alternar entre a análise de dados do Canvas e a configuração do Canvas, clique em **Ver análise de dados** ou **View Canvas** na barra de ferramentas inferior.

{% alert note %}
Os Canvas listados em **Version history** são somente para visualização.
{% endalert %}

Para ver uma lista das alterações feitas em uma versão enquanto ela estava ativa, selecione **View Changes** na barra lateral do histórico de versões. Você também pode ver todas as alterações associadas a uma versão no changelog do Canvas.

Observe que, se você não fez nenhuma edição entre o lançamento de um Canvas e a criação de uma segunda versão, nenhuma alteração aparecerá em **See Changes** para a primeira versão do Canvas.

À medida que o número de versões no histórico aumenta, você também pode renomear cada versão na barra lateral para manter a organização. Por padrão, os nomes das versões são gerados como um número com base em quantas versões foram criadas anteriormente. Se você renomear uma versão que não está mais ativa, isso aparecerá no changelog do Canvas, mas não no changelog da versão dentro da visualização do histórico de versões.

![Exemplo de changelog do Canvas mostrando que duas novas versões do Canvas foram criadas.]({% image_buster /assets/img_archive/canvas_version_history_changelog.png %}){: style="max-width:85%" }

### Descartando versões {#discarding-versions}

Você pode criar até 10 versões por Canvas. Se atingir esse limite, pode descartar uma versão para abrir espaço para uma nova. Observe que as versões são descartadas ao clicar em **Discard**, e não quando você atualiza o Canvas. O descarte de uma versão é refletido no changelog geral do Canvas, e não no changelog de uma versão específica.

Se você descartar uma versão, a configuração do Canvas será perdida imediatamente, mas a análise de dados associada à versão descartada será mantida.

## Visualizando análise de dados {#viewing-analytics}

No histórico de versões, você pode visualizar a análise de dados no nível do Canvas e no nível das etapas. Na visualização de versão do Canvas, os dados serão preenchidos para o intervalo de datas completo, e não apenas para o intervalo de datas daquela versão. No entanto, no nível da etapa, a análise de dados será exibida apenas para as etapas que existiam enquanto aquela versão estava ativa. Essa análise de dados será preenchida usando dias corridos que correspondem ao fuso horário da sua empresa, portanto, os dados não serão específicos para o horário exato do dia em que a versão foi criada.