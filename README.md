# 📊 Reddit Real-Time Sentiment Analysis Pipeline

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-Streaming-231F20?style=for-the-badge&logo=apachekafka&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📖 Aperçu du Projet

Ce projet met en œuvre une **architecture de streaming de données** complète pour analyser en temps réel le sentiment des discussions sur **Reddit**.

L'objectif est de capter le flux de commentaires, de prédire instantanément si le ton est positif ou négatif grâce à un modèle de Machine Learning, et de stocker les résultats pour une analyse ultérieure. Le projet repose sur **Apache Kafka** pour garantir la robustesse et la scalabilité du transport des données.



[Image of Data Pipeline Architecture Diagram]


## 📂 Architecture et Structure du Code

Le projet est découpé en composants indépendants (Microservices pattern) :

### 1. Ingestion et Streaming (Kafka Producer)
* **`kafkaproducer.ipynb` / `streamindata.py`** : Ces scripts se connectent à l'API de Reddit. Ils extraient les nouveaux posts/commentaires en temps réel et les publient ("produce") dans un **Topic Kafka**.
* Utilisation de la librairie `kafka-python` pour l'envoi des messages JSON.

### 2. Moteur de Machine Learning (Model Training)
Avant de traiter le flux, un modèle a été entraîné sur un dataset historique :
* **`trainindata.ipynb`** : Préparation et nettoyage des données d'entraînement.
* **`sentiment_model.ipynb`** : Entraînement du modèle de classification (NLP). Le modèle est sérialisé (sauvegardé) pour être réutilisé par le consommateur sans ré-entraînement.

### 3. Traitement et Stockage (Kafka Consumer)
* **`kafkaconsumer.ipynb`** : Ce notebook écoute ("consume") le Topic Kafka en continu.
    * Il reçoit les messages Reddit bruts.
    * Il applique le modèle de sentiment pré-entraîné.
* **`storedatainpost.ipynb` / `loaddata.py`** : Gestion de la persistance des données. Les résultats (Texte + Sentiment Prédit) sont insérés dans une base de données **PostgreSQL**.

## 🛠️ Stack Technique

* **Langage :** Python
* **Streaming Platform :** Apache Kafka & Zookeeper
* **Data Source :** Reddit API (PRAW)
* **Machine Learning :** Scikit-learn (Pipeline NLP, Vectorization, Classification)
* **Base de Données :** PostgreSQL (via `psycopg2` ou SQLAlchemy)

## 🚀 Guide de Démarrage

Pour faire tourner le pipeline complet, suivez cet ordre d'exécution :

1.  **Infrastructure :** Démarrez vos services Zookeeper et Kafka (localement ou via Docker).
2.  **Base de données :** Assurez-vous que votre instance PostgreSQL est active et que les tables sont créées.
3.  **Modèle :** Exécutez `sentiment_model.ipynb` une fois pour générer et sauvegarder le fichier du modèle `.pkl`.
4.  **Consumer :** Lancez `kafkaconsumer.ipynb`. Il restera en attente de messages.
5.  **Producer :** Lancez `kafkaproducer.ipynb`. Le flux de données commencera à traverser le système.

## 📊 Fonctionnalités Clés

* **Temps Réel :** Latence minimale entre la publication sur Reddit et l'analyse.
* **Découplage :** L'utilisation de Kafka permet de séparer la collecte (Producer) de l'analyse (Consumer).
* **Persistance :** Archivage structuré des analyses dans une base relationnelle SQL.

---

## 🇬🇧 English Summary

**Project:** Real-Time Reddit Sentiment Analysis with Kafka

**Goal:** Build a streaming data pipeline to fetch Reddit comments, analyze their sentiment using ML, and store the results in a database.

**Key Features:**
* **Kafka Architecture:** Implements a Producer (fetching Reddit data) and a Consumer (processing data) decoupled via Kafka topics.
* **NLP Model:** Custom Machine Learning model trained to classify text sentiment, integrated directly into the consumption loop.
* **PostgreSQL Integration:** Processed data is automatically stored in a SQL database for reporting.

**Tech Stack:** Python, Apache Kafka, PostgreSQL, Scikit-Learn.
