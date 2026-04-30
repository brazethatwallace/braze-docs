---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre exportação
page_order: 7
page_type: FAQ
description: "Este artigo aborda algumas perguntas frequentes sobre exportações via API e CSV."

---

# Perguntas frequentes

> Esta página fornece respostas para algumas perguntas frequentes sobre exportações via API e CSV.

### Posso fazer com que certas exportações apareçam no meu bucket S3 e outras não?

Não. Se você forneceu credenciais do S3, todas as suas exportações aparecerão no seu bucket S3. Caso contrário, se nenhuma credencial for fornecida, todas as exportações aparecerão em um bucket S3 pertencente à Braze.

### Preciso adicionar credenciais S3 à Braze para exportar dados?

Não. Se você não adicionar credenciais S3, suas exportações aparecerão em um bucket S3 pertencente à Braze.

### O que acontece se eu configurar as credenciais do S3 no dashboard, mas não selecionar "Tornar este o destino padrão de exportação de dados"?

A caixa de seleção **Tornar este o destino padrão de exportação de dados** define se as exportações vão para o S3 ou para o Azure, supondo que você tenha adicionado credenciais para ambos.

### Por que recebi vários arquivos ao exportar perfis de usuários para o S3?

Esse é o comportamento esperado para espaços de trabalho com muitos usuários. A Braze divide sua exportação em vários arquivos com base no número de usuários no seu espaço de trabalho. Geralmente, há um arquivo de saída para cada 5.000 usuários. Observe que, se você estiver exportando um segmento pequeno dentro de um espaço de trabalho grande, ainda poderá receber vários arquivos.

### Por que vejo duplicatas quando exporto usuários por segmento por meio da REST API?

Essa é uma ocorrência muito rara causada pela arquitetura subjacente do provedor de banco de dados. As duplicatas são removidas toda semana; no entanto, na maioria das semanas, nenhuma duplicata é encontrada.

### Como abro relatórios CSV no Excel?

Embora arquivos CSV geralmente sejam abertos automaticamente no Excel por padrão, isso nem sempre acontece. Consulte os artigos de solução de problemas para [Windows](https://support.microsoft.com/en-us/windows/change-which-programs-windows-7-uses-by-default-62fd162f-8c82-0436-806f-c60d69dcf495) e [Apple](https://support.apple.com/guide/mac-help/choose-an-app-to-open-a-file-on-mac-mh35597/mac) para saber como definir o Excel como programa padrão.

Para converter um CSV em XLSX ou XLS, ou remover a vírgula entre os valores de dados, consulte [este guia](https://www.ablebits.com/office-addins-blog/convert-csv-excel/#import-csv-wizard) sobre como importar CSVs no Excel.

Se você perceber que os zeros à esquerda estão sendo removidos dos IDs de usuário na sua exportação CSV, isso acontece porque o Excel trata os números em um CSV como dados numéricos em vez de texto. Para resolver isso, execute o [Assistente de Importação de Texto do Excel](https://www.ablebits.com/office-addins-blog/converting-csv-excel-issues/#leading-zeros).