> [!WARNING]  
> This repository was built using bazel version 5, which is deprecated.

# Simple Bazel Project

This repository demonstrates a simple project setup using [Bazel](https://bazel.build) to organize code across multiple repositories and manage shared dependencies. It serves as a practical example inspired by the article “[Usando Bazel para Organizar Múltiplos Repositórios e Dependências Compartilhadas](https://medium.com/mercafacil/usando-bazel-para-organizar-multiplos-repositórios-e-dependencias-compartilhadas-aea86b2cf95)”.

## Overview

Bazel is a fast, reliable, and extensible build system that helps manage complex builds with many dependencies. This project illustrates how to:
- Structure a Bazel project with a `WORKSPACE` file and `BUILD` targets.
- Organize shared dependencies and multiple repositories in a scalable way.
- Leverage Bazel’s caching and incremental build capabilities for efficient development.

## Getting Started

### Prerequisites

- **Bazel:** Install the latest version of Bazel from the [official installation guide](https://bazel.build/install).
- **Git:** To clone the repository.

### Cloning the Repository

Clone the repository using:

```bash
git clone https://github.com/christianfds/article-simple-bazel.git
cd article-simple-bazel
```

### Building the Project
To build all targets in the project, run:

```bash
bazel build //...
# Or
bazelisk build //...
```

### Running Tests
To run tests defined in the repository:

```bash
bazel test //...
# Or
bazelisk test //...
```

## Further Reading
* **Medium Article**: For an in-depth discussion on organizing multiple repositories and shared dependencies with Bazel, read the article “[Usando Bazel para Organizar Múltiplos Repositórios e Dependências Compartilhadas](https://medium.com/mercafacil/usando-bazel-para-organizar-multiplos-reposit%C3%B3rios-e-dependencias-compartilhadas-aea86b2cf95)”.
* **Bazel Documentation**: Explore the [Bazel documentation](https://bazel.build/) for more details on advanced configurations and best practices.
* **[BazelCon 2018 Day 2: Python in Bazel (NVIDIA)](https://www.youtube.com/watch?v=9mhmGcR6CPo)**
* **[Building Real-time Systems with Bazel w/ SpaceX](https://www.youtube.com/watch?v=t_3bckhV_YI)**
* **[Integration testing with Bazel w/Dropbox](https://www.youtube.com/watch?v=muvU1DYrY0w)**
