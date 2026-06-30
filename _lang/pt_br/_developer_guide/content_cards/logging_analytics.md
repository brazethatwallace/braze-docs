---
nav_title: Registro de análise de dados
article_title: Registro de análise de dados
page_order: 1
description: "Este artigo aborda como registrar manualmente impressões, cliques, dispensas e lidar com o comportamento ao clicar para seus Content Cards personalizados."
toc_headers: "h2"

---

# Registro de análise de dados {#log-analytics}

{% multi_lang_include developer_guide/_shared/logging_analytics/content_cards.md %}

## Dispensas únicas maiores que impressões únicas {#unique-dismissals-higher-than-unique-impressions}

Se *Dispensas únicas* excede *Impressões únicas*, sua integração personalizada de Content Cards registrou dispensas sem registrar impressões para esses mesmos cartões. A interface padrão de Content Cards da Braze registra ambos automaticamente, então essa discrepância aparece apenas quando você usa uma interface personalizada.

Registre uma impressão cada vez que exibir um cartão e registre uma dispensa quando o usuário dispensá-lo. Para nomes de métodos e exemplos, consulte as seções de plataforma abaixo.

## Análise de dados ausente nos Content Cards {#missing-content-cards-analytics}

Se os Content Cards aparecem corretamente no seu app, mas você não recebe nenhuma análise de dados de forma consistente (impressões, cliques etc.), provavelmente trata-se de um problema de integração de SDK.

- **Visualizações personalizadas de Content Cards (Android, iOS, Web):** A interface padrão da Braze registra impressões e cliques automaticamente em todas as plataformas. Se você está usando uma visualização ou implementação personalizada de Content Cards, é necessário chamar os métodos de registro apropriados explicitamente dentro do seu aplicativo. Consulte [Registro de análise de dados]({{site.baseurl}}/developer_guide/content_cards/logging_analytics) para a sua plataforma. Para implementações Web personalizadas especificamente, verifique se o SDK Web da Braze está carregado, confira o console do navegador em busca de erros e confirme que os dados dos cartões estão sendo recebidos.
- **Inicialização do SDK e identificação do usuário:** Certifique-se de que o SDK esteja totalmente inicializado antes de exibir os cartões. Os eventos são descartados silenciosamente (não enfileirados) se o SDK não estiver inicializado, estiver em modo de inicialização com postergação ou desabilitado por GDPR. O SDK registra análise de dados para usuários anônimos, mas métricas do dashboard como "impressões diárias únicas" exigem uma identidade de usuário resolvida, então chame `changeUser` antes de exibir os cartões sempre que possível.

## ID do Content Card {#content-card-id}

Cada envio de Campaign para um destinatário gera um novo ID de Content Card. Se o mesmo usuário receber a Campaign novamente em um envio posterior, a Braze atribui um novo ID. Faça referência ao `id` do cartão ao registrar impressões, cliques e dispensas em implementações personalizadas.