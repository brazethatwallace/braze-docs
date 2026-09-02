---
nav_title: APIs de exportação
article_title: APIs de exportação
page_order: 5
page_type: reference
description: "Este artigo de referência ajuda você a decidir quando usar APIs de exportação em vez de downloads de CSV do dashboard."
platform: API

---

# APIs de exportação {#export-apis}

> Esta página ajuda você a decidir quando usar APIs de exportação em vez de downloads de CSV do dashboard.

As APIs de exportação da Braze permitem exportar dados da Braze programaticamente como JSON. Para saber mais sobre o que você pode exportar, pré-requisitos e como a entrega funciona, consulte [Endpoints de exportação]({{site.baseurl}}/api/endpoints/export).

## Quando usar APIs de exportação em vez de downloads de CSV {#when-to-use-export-apis-instead-of-csv-downloads}

A tabela a seguir descreve cenários comuns em que usar a API or interface de programação do aplicativo (API) de exportação é uma escolha melhor do que um download de CSV pelo dashboard.

| Cenário | Informações |
| --- | --- |
| Sua exportação é grande demais para o dashboard | As exportações de CSV do dashboard são limitadas a 500.000 linhas. Se você está exportando dados de um Segment or segmento or segmento com mais de 500.000 usuários, use a API or interface de programação do aplicativo (API) de exportação, que não tem limite de quantidade para exportação. |
| Você quer automatizar relatórios recorrentes | Programe exportações via API or interface de programação do aplicativo (API) por meio de uma integração para obter dados em uma cadência regular, sem interação manual com o dashboard. |
| Você precisa alimentar dados em ferramentas externas | Envie dados de exportação diretamente para ferramentas de BI, data warehouses ou outras plataformas de análise de dados. |
| Você precisa de dados que não estão disponíveis como exportação de CSV no dashboard | Algumas categorias de dados, incluindo KPIs, séries de receita, análise de dados de eventos personalizados e dados de sessão, estão disponíveis apenas pela API or interface de programação do aplicativo (API). |
| Você quer interagir com os dados de forma programática | Use a saída JSON para processamento personalizado, transformações ou integrações. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Quando usar APIs de exportação em vez de downloads de CSV" }

{% alert tip %}
Para obter ajuda com exportações de CSV e API or interface de programação do aplicativo (API), consulte [Solução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}