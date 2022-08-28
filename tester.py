while not enterClick:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                username.append("A")
            if event.key == pygame.K_b:
                username.append("B")
            if event.key == pygame.K_c:
                username.append("C")
            if event.key == pygame.K_d:
                username.append("D")
            if event.key == pygame.K_e:
                username.append("E")
            if event.key == pygame.K_f:
                username.append("F")
            if event.key == pygame.K_g:
                username.append("G")
            if event.key == pygame.K_h:
                username.append("H")
            if event.key == pygame.K_i:
                username.append("I")
            if event.key == pygame.K_j:
                username.append("J")
            if event.key == pygame.K_k:
                username.append("K")
            if event.key == pygame.K_l:
                username.append("L")
            if event.key == pygame.K_m:
                username.append("M")
            if event.key == pygame.K_n:
                username.append("N")
            if event.key == pygame.K_o:
                username.append("O")
            if event.key == pygame.K_p:
                username.append("P")
            if event.key == pygame.K_q:
                username.append("Q")
            if event.key == pygame.K_r:
                username.append("R")
            if event.key == pygame.K_s:
                username.append("S")
            if event.key == pygame.K_t:
                username.append("T")
            if event.key == pygame.K_u:
                username.append("U")
            if event.key == pygame.K_v:
                username.append("V")
            if event.key == pygame.K_w:
                username.append("W")
            if event.key == pygame.K_x:
                username.append("X")
            if event.key == pygame.K_y:
                username.append("Y")
            if event.key == pygame.K_z:
                username.append("Z")
            if event.key == pygame.K_BACKSPACE and len(username) > 0:
                username.pop(len(username) - 1)
            if len(username) == 6:
                username.pop(5)

            if event.key == pygame.K_RETURN: