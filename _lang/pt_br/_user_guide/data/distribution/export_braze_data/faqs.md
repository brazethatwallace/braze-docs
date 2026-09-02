---
nav_title: FAQ
article_title: FAQ sobre exportação
page_order: 7
page_type: FAQ
description: "Este artigo aborda algumas perguntas frequentes sobre exportações via API e CSV."

---

# Perguntas frequentes {#frequently-asked-questions}

> Esta página fornece respostas para algumas perguntas frequentes sobre exportações via API e CSV.

## Posso fazer com que certas exportações apareçam no meu bucket S3 e outras não? {#can-you-make-certain-exports-appear-in-your-s3-bucket-and-others-not}

Não. Se você forneceu credenciais do S3, todas as suas exportações aparecerão no seu bucket S3. Caso contrário, se nenhuma credencial for fornecida, todas as exportações aparecerão em um bucket S3 pertencente à Braze.

## Preciso adicionar credenciais S3 à Braze para exportar dados? {#do-i-have-to-add-s3-credentials-to-braze-to-export-data}

Não. Se você não adicionar credenciais S3, suas exportações aparecerão em um bucket S3 pertencente à Braze.

## O que acontece se eu configurar as credenciais do S3 no dashboard, mas não selecionar "Make this the default data export destination"? {#what-happens-if-you-set-up-s3-credentials-in-the-dashboard-but-dont-select-make-this-the-default-data-export-destination}

A caixa de seleção **Make this the default data export destination** define se as exportações vão para o S3 ou para o Azure, supondo que você tenha adicionado credenciais para ambos.

## O destino padrão de exportação de dados afeta o Braze Currents? {#does-the-default-data-export-destination-affect-braze-currents}

Não. O Currents usa seu próprio conector e configurações de armazenamento. Escolher um destino padrão de exportação para exportações via CSV e API não altera o local onde os dados do Currents são gravados.

## Por que recebi vários arquivos ao exportar perfis de usuários para o S3? {#why-did-i-receive-multiple-files-when-exporting-user-profiles-to-s3}

Esse é o comportamento esperado para espaços de trabalho com muitos usuários. A Braze divide sua exportação em vários arquivos com base no número de usuários no seu espaço de trabalho. Geralmente, há um arquivo de saída para cada 5.000 usuários. Observe que, se você estiver exportando um Segment pequeno dentro de um espaço de trabalho grande, ainda poderá receber vários arquivos.

## Por que vejo duplicatas quando exporto usuários por Segment por meio da REST API? {#why-do-i-see-duplicates-when-i-export-users-by-segment-through-rest-api}

Essa é uma ocorrência muito rara causada pela arquitetura subjacente do provedor de banco de dados. As duplicatas são removidas toda semana; no entanto, na maioria das semanas, nenhuma duplicata é encontrada.

## Como abro relatórios CSV no Excel? {#how-do-i-open-csv-reports-in-excel}

Embora arquivos CSV geralmente sejam abertos automaticamente no Excel por padrão, isso nem sempre acontece. Consulte os artigos de solução de problemas para [Windows](https://support.microsoft.com/en-us/windows/change-which-programs-windows-7-uses-by-default-62fd162f-8c82-0436-806f-c60d69dcf495) e [Apple](https://support.apple.com/guide/mac-help/choose-an-app-to-open-a-file-on-mac-mh35597/mac) para saber como definir o Excel como programa padrão.

Para converter um CSV em XLSX ou XLS, ou remover a vírgula entre os valores de dados, consulte [este guia sobre como importar CSVs no Excel](https://www.ablebits.com/office-addins-blog/convert-csv-excel/#import-csv-wizard).

Se você perceber que os zeros à esquerda estão sendo removidos dos IDs de usuário na sua exportação CSV, isso acontece porque o Excel trata os números em um CSV como dados numéricos em vez de texto. Para resolver isso, execute o [Assistente de Importação de Texto do Excel](https://www.ablebits.com/office-addins-blog/converting-csv-excel-issues/#leading-zeros).