# GnoelixiAI Simple Neural Network

Welcome to the **GnoelixiAI Simple Neural Network** project! This repository provides the code and resources for building a simple neural network using **Keras**, **TensorFlow**, **Python**, and **Microsoft SQL Server**. The project was initially featured in the GnoelixiAI Hub newsletter and is designed to train a model on the Iris dataset stored in SQL Server.

## Project Overview

This project demonstrates how to:
- Connect Python to SQL Server to fetch data.
- Build, train, and evaluate a neural network using Keras and TensorFlow.
- Use the Iris dataset to classify flower species based on sepal and petal measurements.

## Architecture

The neural network has the following layers:
1. **Input Layer**: Four features from the Iris dataset.
2. **Hidden Layer**: 64 neurons with ReLU activation.
3. **Output Layer**: 3 neurons with Softmax activation for classification.

![Network Architecture](GnoelixiAI_NN_Architecture.jpg)

## Getting Started

To get started, clone this repository and follow the steps below to set up the environment, prepare the SQL Server database, and run the model.

### Prerequisites

1. **Python 3.9+**
2. **SQL Server** with the Iris dataset in a database (instructions below)
3. Required Python libraries (listed in `requirements.txt`)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/gnoelixiai-simple-neural-network.git
   cd gnoelixiai-simple-neural-network
