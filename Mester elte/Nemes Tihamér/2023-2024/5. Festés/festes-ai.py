def minimal_fencing_cost():
    import sys
    input = sys.stdin.read
    data = input().split()

    # Első sor: sorok (És oszlopok száma)
    N, M = map(int, data[:2])

    # Második sor: sorok teljes lefestésének költségei
    R = list(map(int, data[2:2 + N]))

    # Oszlopokra vonatkozó költségek (Összes C_{j,l,r} bemenet)
    costs = data[2 + N:]
    print(costs)
    # Feldolgozás: oszlopköltségek beolvasása struktúrrá
    C = []
    index = 0
    for _ in range(M):
        column_costs = []
        for i in range(1, N + 1):
            for j in range(i, N + 1):
                column_costs.append(int(costs[index]))
                index += 1
        C.append(column_costs)

    # DP tömb inicializálása
    dp = [float('inf')] * M

    # Első oszlop: kombinációk számítása, sorok teljes festésének figyelembevételével
    for i in range(len(C[0])):
        dp[0] = min(dp[0], C[0][i])
    dp[0] = min(dp[0], sum(R))  # Első oszlop esetén teljes sor festés is lehet opció

    # Dinamikus programozás az oszlopokon
    for j in range(1, M):
        # Minimális költség keresése az aktuális oszlophoz
        current_min = float('inf')
        for i in range(len(C[j])):
            current_min = min(current_min, dp[j - 1] + C[j][i])

        # Teljes sorok festéseinek figyelembe vétele
        total_row_paint = sum(R) + dp[j - 1]
        dp[j] = min(current_min, total_row_paint)

    # Az utolsó oszlop lefestésének minimális költsége
    print(dp[-1])

minimal_fencing_cost()