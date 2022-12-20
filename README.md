# Primeiro ETL com a API do Twitter 💻

### 📃 Descrição
Este repositório contém o arquivo para fazer o "scraping de tweets" de determinado usuário, usando a API do Twitter. Também contém o código de inicialização das DAGs para o Airflow.

O processo se dá através dos seguintes passos: **Conectar à API do Twitter -> Fazer Scraping dos Tweets -> Transformar em CSV -> Fazer upload no Bucket S3**

Tudo isso é executado de acordo com o schedule do Airflow, que está rodando em uma instância de EC2, pelos seus DAGs.

![pipeline](https://user-images.githubusercontent.com/90157378/206926584-fbaa0afd-58c0-457b-ab9d-f30c2d3cd341.png)

### 📚 Conteúdo
Dag e ETL(Scraper)

### 🌐 Motivação
Ampliar meus conhecimentos sobre **Engenharia de Dados**

