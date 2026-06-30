---
nav_title: "Segments de catálogo"
article_title: "Segments de catálogo"
page_order: 0
page_type: reference
alias: "/catalog_segments/"
description: "Este artigo descreve como criar segments de catálogo, que usam dados de catálogo em extensões de segmento SQL para criar públicos de usuários."
tool: Segments
---

# Segments de catálogo {#catalog-segments}

> Segments de catálogo são um tipo de extensão de segmento SQL criados pela combinação de dados de catálogo com dados de eventos personalizados ou compras. Eles podem ser referenciados em um Segment e, em seguida, direcionados por Campaigns e Canvas.

Segments de catálogo usam SQL para unir dados de catálogos e dados de eventos personalizados ou compras. Para isso, você precisa ter um campo identificador comum entre seus catálogos e seus eventos personalizados ou compras. Por exemplo, o valor de um ID de item em um catálogo deve corresponder ao valor de uma propriedade em um evento personalizado.

## Criando um segment de catálogo {#creating-a-catalog-segment}

1. Acesse **Extensões de segmento** > **Criar nova extensão** > **Começar com modelo** e selecione um modelo. <br>![Modal com a opção de criar um segment de catálogo para eventos, compras ou segments RFM.]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2. O editor SQL é preenchido automaticamente com um modelo. <br>![Editor SQL com um modelo pré-gerado.]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>Esse modelo une dados de eventos de usuários com dados de catálogo para segmentar usuários que interagiram com determinados itens do catálogo.

3. Use a guia **Variáveis** para fornecer os campos necessários para o seu modelo antes de gerar o segment. <br>Para que a Braze identifique os usuários com base no engajamento deles com itens do catálogo, você precisa fazer o seguinte: <br> - Selecionar um catálogo que contenha um campo de catálogo <br> - Selecionar um evento personalizado que contenha uma propriedade de evento <br> - Fazer a correspondência entre os valores do campo de catálogo e da propriedade de evento

Veja as diretrizes para selecionar as variáveis:

| Campo de variável | Descrição |
| --- | --- |
| `Catalog` | O nome do catálogo que você está usando para direcionar usuários. |
| `Catalog field` | O campo no seu catálogo que contém os mesmos valores que a sua `Custom event property`. Geralmente é um tipo de ID. No caso de uso de eCommerce, seria `shopify_id`. |
| `Custom event` | O nome do seu evento personalizado, que é o mesmo evento que contém uma propriedade com valores correspondentes ao seu `Catalog field`. No caso de uso de eCommerce, seria `Made Order`. |
| `Custom event property` | O nome da propriedade do seu evento personalizado, que corresponde aos valores do seu `Catalog field`. No exemplo de caso de uso de eCommerce, seria `Shopify_ID.` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Criando um segment de catálogo" }

{: start="4"}
4. Se necessário, preencha campos opcionais adicionais para o seu caso de uso, a fim de segmentar por um valor de campo específico dentro do seu catálogo:
- `Catalog field`: Um campo específico (nome da coluna) dentro deste catálogo
- `Value`: Um valor específico dentro desse campo ou coluna <br><br> Usando o app de saúde como exemplo, digamos que dentro do catálogo de cada médico que você pode agendar, existe um campo chamado `specialty` que contém um valor como `vision` ou `dental`. Para segmentar usuários que visitaram médicos com o valor `dental`, você pode selecionar `specialty` como o `Catalog field` e selecionar `dental` como o `Value`.

5. Após criar uma extensão de segmento SQL, recomendamos clicar em **Executar pré-visualização** para verificar se a sua consulta retorna usuários ou se há erros. Para saber mais sobre [pré-visualização de resultados de consulta]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#previewing-results), gerenciamento de [extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#managing-sql-segment-extensions) e mais, confira [Extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).

{% alert note %}
Se você estiver criando um segment SQL que usa a tabela `CATALOGS_ITEMS_SHARED`, é necessário especificar um ID de catálogo. Por exemplo:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Determinando se você precisa inverter o SQL {#determining-if-you-need-to-invert-sql}

Embora não seja possível consultar diretamente usuários com zero eventos, você pode usar **Inverter SQL** para direcionar esses usuários.

Por exemplo, para direcionar usuários que fizeram menos de três compras, primeiro escreva uma consulta para selecionar usuários que fizeram três ou mais compras. Em seguida, selecione **Inverter SQL** para direcionar usuários com menos de três compras (incluindo aqueles com zero compras).

![Extensão de segmento chamada "Clicked 1-4 emails in the last 30 days" com a opção de inverter SQL selecionada.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:70%;"}

{% alert important %}
A menos que você esteja especificamente tentando direcionar usuários com zero eventos, não será necessário inverter o SQL. Se **Inverter SQL** estiver selecionado, confirme que o recurso é necessário e que o segment corresponde ao público desejado. Por exemplo, se uma consulta direciona usuários com pelo menos um evento, ela direcionará apenas usuários com zero eventos quando invertida.
{% endalert %}

## Atualizando a associação ao segment {#refreshing-segment-membership}

Para atualizar a associação de qualquer segment de catálogo, abra o segment de catálogo e selecione **Ações** > **Atualizar** > **Sim, atualizar**.

{% alert tip %}
Se você criou um segment em que espera que os usuários entrem e saiam regularmente, atualize manualmente o segment de catálogo que ele usa antes de direcionar esse segment em uma Campaign ou Canvas.
{% endalert %}

### Definindo configurações de atualização {#designating-refresh-settings}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

## Casos de uso {#use-cases}

{% tabs local %}
{% tab Saúde %}

### App de saúde {#health-app}

Digamos que você tem um app de saúde e quer segmentar usuários que agendaram uma visita ao dentista. Você também tem o seguinte:

- Um catálogo `Doctors` que contém os diferentes médicos que um paciente pode agendar, cada um com um `doctor ID` atribuído
- Um evento personalizado `Booked Visit` com uma propriedade `doctor ID` que compartilha os mesmos valores do campo `doctor ID` no seu catálogo
- Um campo `speciality` dentro do seu catálogo que contém o valor `dental`

Você configuraria um segment de catálogo usando as seguintes variáveis:

| Variável | Propriedade |
| --- | --- |
| `Catalog` | Doctors |
| `Catalog field` | doctor ID |
| `Custom event` | Booked Visit |
| `Custom event property` | doctor ID |
| `(Under Filter SQL Results) Catalog field` | Specialty |
| `(Under Filter SQL Results) Value` | Dental |
{: .reset-td-br-1 .reset-td-br-2 aria-label="App de saúde" }

{% endtab %}
{% tab SaaS %}

### Plataforma SaaS {#saas-platform}

Digamos que você tem uma plataforma SaaS B2B e quer segmentar usuários que são colaboradores de um cliente existente. Você também tem o seguinte:

- Um catálogo `Accounts` que contém as diferentes contas que estão usando sua plataforma SaaS atualmente, cada uma com um `account ID` atribuído
- Um evento personalizado `Event Attendance` com uma propriedade "account ID" que compartilha os mesmos valores do campo "account ID" no seu catálogo
- Um campo `Classification` dentro do seu catálogo que contém o valor `enterprise`

Você configuraria um segment de catálogo usando as seguintes variáveis:

| Variável | Propriedade |
| --- | --- |
| `Catalog` | Accounts |
| `Catalog field` | account ID |
| `Custom event` | Event Attendance |
| `Custom event property` | account ID |
| `(Under Filter SQL Results) Catalog field` | Classification |
| `(Under Filter SQL Results) Value` | Enterprise |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plataforma SaaS" }

{% endtab %}
{% endtabs %}

## Perguntas frequentes {#frequently-asked-questions}

### Executar um segment de catálogo consome créditos de extensão de segmento SQL? {#does-running-a-catalog-segment-consume-sql-segment-extension-credits}

Sim, segments de catálogo são alimentados por SQL e consomem créditos de extensão de segmento SQL. Para saber mais, confira [Uso de Segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#monitoring-your-sql-segments-usage).

### Criar um segment de catálogo consome a cota de extensões de segmento SQL? {#does-creating-a-catalog-segment-consume-sql-segment-extension-allotments}

Sim. Da mesma forma que as extensões de segmento SQL contam para a sua cota de extensões de segmento, os segments de catálogo também contam para essa cota.

### Tenho um caso de uso de segment de catálogo que o modelo atual não atende. Como devo configurar isso? {#i-have-a-catalog-segment-use-case-that-the-current-template-doesnt-serve-how-should-i-set-that-up}

Fale com o seu gerente de suporte ao cliente ou com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) para orientação adicional.