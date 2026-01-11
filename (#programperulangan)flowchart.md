```mermaid
flowchart TD
    A[Mulai]
    B[i = 1]
    C{i <= 10?}
    D{i mod 2 ==0?}
    E[Tampilkan i]
    F[i = i + 1]
    G[Selesai]
        A --> B --> C
        C -- Ya --> D 
        D -- Ya --> E --> F --> C
        D -- Tidak --> F --> C
        c --Tidak --> G
```        
    