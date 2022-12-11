# Primeiro ETL com a API do Twitter 💻

### 📃 Descrição
Este contém o arquivo para fazer o "scraping de tweets" de determinado usuário, usando a API do Twitter. Também contém o código de inicialização das DAGs para o Airflow.

O processo se dá através dos seguintes passos: **Conectar à API do Twitter -> Fazer Scraping dos Tweets -> Transformar em CSV -> Fazer upload no Bucket S3**
Tudo isso é executado de acordo com o schedule do Airflow, que está rodando em uma instância de EC2, pelas seus DAGs.

### 📚 Conteúdo
Dag e ETL(Scraper)

### 🌐 Motivação
Ampliar meus conhecimentos sobre **Engenharia de Dados**
