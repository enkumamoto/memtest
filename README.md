```markdown
# Memory Stress Test

Um script Python simples para testar e analisar o comportamento da memória RAM do sistema através de operações controladas de alocação, escrita e leitura.

## 📋 Descrição

Este script realiza testes de estresse na memória RAM alocando blocos de memória de tamanho especificado, preenchendo-os com dados e medindo:
- Uso de memória antes/depois
- Tempo de alocação e escrita
- Tempo de leitura
- Liberação de memória

## 🚀 Funcionalidades

- **Alocação controlada**: Aloca blocos de memória de tamanho personalizável
- **Operações de E/S**: Realiza escrita e leitura sequenciais
- **Monitoramento em tempo real**: Usa `psutil` para monitorar uso da memória
- **Iterações múltiplas**: Permite repetir o teste várias vezes
- **Limpeza adequada**: Garante liberação de memória entre iterações

## 📁 Estrutura do Código

### Função Principal
```python
memory_test(size_mb: int, iterations: int = 3)
```

### Parâmetros
| Parâmetro | Tipo | Padrão | Descrição |
|-----------|------|--------|-----------|
| `size_mb` | int | - | Tamanho do bloco de memória em MB |
| `iterations` | int | 3 | Número de repetições do teste |

## 🔧 Instalação

### Pré-requisitos
- Python 3.6 ou superior
- Biblioteca `psutil`

### Instalar dependências
```bash
pip install psutil
```

## 🎯 Uso

### Execução básica
```python
# Teste com 500 MB, 3 iterações
memory_test(size_mb=500, iterations=3)
```

### Executar como script
```bash
python memory_test.py
```

### Uso personalizado
```python
# Teste com diferentes configurações
memory_test(size_mb=1000, iterations=5)  # 1 GB, 5 iterações
memory_test(size_mb=250, iterations=1)   # 250 MB, 1 iteração
```

## 📊 Saída do Script

```
🔍 Iniciando teste com blocos de 500 MB (524,288,000 bytes)...

▶ Iteração 1/3
Memória em uso antes: 45.32%
Tempo para alocação e escrita: 0.1523 segundos
Memória em uso depois: 78.15%
Tempo de leitura: 0.2345 segundos (checksum=128000)
Memória após liberação: 46.01%

▶ Iteração 2/3
...
```

## ⚙️ Como Funciona

1. **Monitoramento inicial**: Verifica o uso atual da memória
2. **Alocação**: Cria um `bytearray` do tamanho especificado
3. **Escrita**: Preenche o bloco em incrementos de 4KB
4. **Leitura**: Calcula checksum para forçar leitura completa
5. **Liberação**: Remove a referência e permite coleta de lixo
6. **Pausa**: Aguarda 1 segundo para estabilização

## 🔍 Casos de Uso

### 1. Teste de Hardware
- Verificar estabilidade da RAM
- Detectar possíveis falhas de memória
- Testar capacidade de troca (swap)

### 2. Benchmarking
- Comparar desempenho entre sistemas
- Medir latência de memória
- Testar diferentes tamanhos de página

### 3. Desenvolvimento
- Testar aplicações com uso intensivo de memória
- Simular condições de alta carga
- Verificar vazamentos de memória

## ⚠️ Precauções

1. **Não execute como superusuário** sem necessidade
2. **Monitore a temperatura** do sistema durante testes prolongados
3. **Use com moderação** em sistemas de produção
4. **Ajuste o tamanho** conforme a memória disponível:
   - Para 8GB RAM: 100-2000 MB
   - Para 16GB RAM: 500-4000 MB
   - Para 32GB+ RAM: 1000-8000 MB

## 🛠️ Personalização

### Modificar tamanho do bloco de escrita
```python
# Alterar de 4096 para outro valor
for j in range(0, len(block), 8192):  # blocos de 8KB
    block[j] = 1
```

### Adicionar mais métricas
```python
# Exemplo: monitorar swap
swap_before = psutil.swap_memory().percent
# ... operações ...
swap_after = psutil.swap_memory().percent
```

### Teste contínuo
```python
# Loop infinito com pausas
while True:
    memory_test(size_mb=1000, iterations=1)
    time.sleep(10)
```

## 📈 Interpretação dos Resultados

### Indicadores normais:
- **Tempo de alocação crescente**: Pode indicar fragmentação
- **Uso de swap aumentando**: Memória insuficiente
- **Checksum inconsistente**: Possível erro de hardware

### Sinais de alerta:
- **Erros de alocação**: Falta de memória
- **Tempos muito variáveis**: Problemas de consistência
- **Memória não liberada**: Vazamento no sistema

## 🔗 Dependências

- [psutil](https://github.com/giampaolo/psutil): Biblioteca para monitoramento do sistema
- time: Módulo padrão do Python para temporização

## 📝 Licença

Este código é disponibilizado para fins educacionais e de teste. Use por sua conta e risco.

## 🤝 Contribuições

Sugestões de melhorias:
- Adicionar gráficos em tempo real
- Implementar testes multi-thread
- Adicionar suporte para argumentos de linha de comando
- Incluir mais métricas do sistema

## 🆘 Suporte

Para problemas ou dúvidas:
1. Verifique se `psutil` está instalado
2. Confira as permissões de execução
3. Ajuste o tamanho do bloco conforme sua RAM disponível

---

**⚠️ Aviso**: Este script aloca grandes quantidades de memória. Use com cuidado em sistemas críticos ou com pouca memória disponível.
```

Este README fornece uma documentação completa e profissional para o seu script de teste de memória, incluindo:
- Descrição clara do propósito
- Instruções de instalação e uso
- Explicação detalhada do funcionamento
- Casos de uso práticos
- Precauções importantes
- Sugestões de personalização
- Interpretação dos resultados

O formato é visualmente organizado e fácil de seguir para usuários de todos os níveis.
