import time
import psutil

def memory_test(size_mb: int, iterations: int = 3):
    """
    Teste de estresse na memória RAM.
    :param size_mb: Tamanho do bloco de memória a ser alocado (em MB)
    :param iterations: Número de repetições do teste
    """
    size_bytes = size_mb * 1024 * 1024
    print(f"🔍 Iniciando teste com blocos de {size_mb} MB ({size_bytes:,} bytes)...")
    
    for i in range(iterations):
        print(f"\n▶ Iteração {i+1}/{iterations}")

        # Ver uso atual de memória antes
        mem_before = psutil.virtual_memory().percent
        print(f"Memória em uso antes: {mem_before:.2f}%")

        # Alocar memória
        start = time.time()
        block = bytearray(size_bytes)
        for j in range(0, len(block), 4096):  # preencher em blocos de 4KB
            block[j] = 1
        alloc_time = time.time() - start
        print(f"Tempo para alocação e escrita: {alloc_time:.4f} segundos")

        # Ver uso após alocação
        mem_after = psutil.virtual_memory().percent
        print(f"Memória em uso depois: {mem_after:.2f}%")

        # Leitura da memória
        start = time.time()
        checksum = sum(block)
        read_time = time.time() - start
        print(f"Tempo de leitura: {read_time:.4f} segundos (checksum={checksum})")

        # Liberar memória
        del block
        time.sleep(1)  # tempo para o GC liberar

        mem_final = psutil.virtual_memory().percent
        print(f"Memória após liberação: {mem_final:.2f}%")

if __name__ == "__main__":
    # Exemplo: 500 MB por iteração, 3 vezes
    memory_test(size_mb=500, iterations=3)
