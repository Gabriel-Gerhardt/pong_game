# Pong em Pygame

Projeto simples de Pong desenvolvido em Python utilizando a biblioteca Pygame.

## Funcionalidades

- Movimento dos jogadores
- Colisão da bola com as barras
- Rebote nas bordas
- Encerramento da partida ao marcar ponto

## Tecnologias

- Python 3
- Pygame

## Como executar

Instale as dependências:

```bash
pip install pygame
```

Execute o projeto:

```bash
python main.py
```

## Controles

### Jogador 1
- `W` → subir
- `S` → descer

### Jogador 2
- `↑` → subir
- `↓` → descer

## Estrutura

```text
.
├── main.py
└── bar.py
```

## Desenvolvimento

O projeto utiliza:
- `Vector2` para movimentação
- colisão entre círculo e retângulo
- renderização em tempo real com Pygame
